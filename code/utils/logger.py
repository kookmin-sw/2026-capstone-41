import time
import sys
import signal
import sqlite3
import json
from datetime import datetime
import os
import builtins
import threading
import io
import subprocess

import rclpy
from rclpy.node import Node
from rosidl_runtime_py.utilities import get_message
from rclpy.serialization import serialize_message
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy

from PIL import Image as PIL_Image
from sensor_msgs.msg import Image, CompressedImage


class Logger(Node):
    def __init__(
        self,
        logging_path,
        hz=10.0,
        batch_size=100,
        flush_interval=5.0,
        image_encoding=None,
        bridge_only=False,
        zenoh_config_path=None,
        zenoh_working_dir=None,
        auto_start_bridge=False,
    ):
        super().__init__("logging_node")

        self.logging_path = logging_path
        self.hz = hz
        self.batch_size = batch_size
        self.flush_interval = flush_interval
        self.image_encoding = image_encoding.lower() if image_encoding else None
        self.bridge_only = bridge_only

        self.zenoh_config_path = zenoh_config_path
        self.zenoh_working_dir = zenoh_working_dir
        self.auto_start_bridge = auto_start_bridge
        self.bridge_proc = None

        self.conn = None
        self.cursor = None
        self.buffer = []
        self.last_flush_time = time.monotonic()

        self._original_print = builtins.print
        self.db_lock = threading.Lock()

        self.save_dir = None
        self.file_index = {}

        self.subscribers = {}
        self.publishers_map = {}
        self.rate_limiters = {
            "log": {},
            "publish": {},
        }
        self.crop_ratio = 1.0

        if self.auto_start_bridge:
            self.start_bridge()

    def _now_iso(self):
        return datetime.now().isoformat()

    def _default_qos(self, reliability, depth=10):
        return QoSProfile(
            reliability=reliability,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.KEEP_LAST,
            depth=depth,
        )

    def _should_run(self, group, name, hz):
        if hz is None:
            return True

        now = time.monotonic()

        with self.db_lock:
            prev = self.rate_limiters[group].get(name, 0.0)
            if now - prev < 1.0 / hz:
                return False
            self.rate_limiters[group][name] = now

        return True

    def _flush_buffer_locked(self):
        if not self.buffer or self.conn is None:
            return

        self.cursor.executemany(
            """
            INSERT INTO logs (name, type, timestamp, data)
            VALUES (?, ?, ?, ?)
            """,
            self.buffer,
        )
        self.conn.commit()
        self.buffer.clear()
        self.last_flush_time = time.monotonic()

    def _maybe_flush_locked(self):
        now = time.monotonic()
        if len(self.buffer) >= self.batch_size or now - self.last_flush_time >= self.flush_interval:
            self._flush_buffer_locked()

    def _create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                data TEXT NOT NULL
            )
            """
        )
        self.conn.commit()

    def _topic_to_filename_prefix(self, topic_name):
        return topic_name.strip("/").replace("/", "_")

    def _save_raw_message(self, topic_name, msg):
        if self.bridge_only or self.save_dir is None:
            return None

        prefix = self._topic_to_filename_prefix(topic_name)
        topic_dir = os.path.join(self.save_dir, prefix)
        os.makedirs(topic_dir, exist_ok=True)

        with self.db_lock:
            idx = self.file_index.get(topic_name, 0)
            self.file_index[topic_name] = idx + 1

        file_path = os.path.join(topic_dir, f"{prefix}_{idx}")

        with open(file_path, "wb") as f:
            f.write(serialize_message(msg))

        return os.path.relpath(file_path, self.logging_path)

    def _log_print(self, *args, **kwargs):
        msg = " ".join(str(arg) for arg in args)
        timestamp = self._now_iso()

        self._original_print(f"[{timestamp}]", *args, **kwargs)

        if not self.bridge_only and self.conn is not None:
            self.write_log(
                name="print",
                type_="stdout",
                data={
                    "timestamp": timestamp,
                    "message": msg,
                },
            )

    def start_bridge(self):
        if self.bridge_proc is not None:
            print("zenoh bridge already started")
            return

        if self.zenoh_config_path is None:
            raise ValueError("zenoh_config_path is required to start bridge")

        working_dir = self.zenoh_working_dir
        if working_dir is None:
            working_dir = os.path.dirname(self.zenoh_config_path)

        self.bridge_proc = subprocess.Popen(
            [
                "zenoh-bridge-ros2dds",
                "-c",
                self.zenoh_config_path,
            ],
            cwd=working_dir,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            preexec_fn=os.setsid,
        )
        print(f"zenoh bridge started: pid={self.bridge_proc.pid}")

    def stop_bridge(self):
        if self.bridge_proc is None:
            return

        try:
            os.killpg(os.getpgid(self.bridge_proc.pid), signal.SIGTERM)
            self.bridge_proc.wait(timeout=3.0)
        except Exception:
            try:
                os.killpg(os.getpgid(self.bridge_proc.pid), signal.SIGKILL)
            except Exception:
                pass

        self.bridge_proc = None
        self._original_print("zenoh bridge stopped")

    def logging_start(self):
        builtins.print = self._log_print
        signal.signal(signal.SIGINT, self.signal_handler)

        if self.auto_start_bridge and self.bridge_proc is None:
            self.start_bridge()

        if self.bridge_only:
            print("bridge_only=True, logging database will not be created")
            return

        folder_name = datetime.now().strftime("%Y%m%d-%H%M%S")
        self.save_dir = os.path.join(self.logging_path, folder_name)
        os.makedirs(self.save_dir, exist_ok=True)

        db_path = os.path.join(self.save_dir, "log.db")
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()

        self.cursor.execute("PRAGMA journal_mode=WAL")
        self.cursor.execute("PRAGMA synchronous=NORMAL")

        self._create_table()
        print(f"logging started: {self.save_dir}")

    def write_log(self, name, type_, data):
        if self.bridge_only or self.conn is None:
            return

        row = (
            name,
            type_,
            self._now_iso(),
            json.dumps(data, ensure_ascii=False),
        )

        with self.db_lock:
            self.buffer.append(row)
            self._maybe_flush_locked()

    def flush(self):
        if self.bridge_only or self.conn is None:
            return

        with self.db_lock:
            self._flush_buffer_locked()

    def logging_terminate(self):
        if self.conn:
            self.flush()
            self.conn.close()
            self.conn = None
            self.cursor = None

        self.stop_bridge()

        builtins.print = self._original_print
        print("#### logger terminated")

    def signal_handler(self, sig, frame):
        self._original_print("\nCtrl+C was pressed. Exiting gracefully...")
        self.logging_terminate()
        rclpy.shutdown()
        sys.exit(0)

    def add_publisher(
        self,
        pub_type,
        topic_name=None,
        topic_type_str=None,
        input_topic=None,
        output_topic=None,
        hz=None,
        jpeg_quality=45,
        input_qos_profile=None,
        output_qos_profile=None,
        qos_profile=None,
    ):
        if pub_type == "dummy":
            msg_type = get_message(topic_type_str)

            if qos_profile is None:
                qos_profile = self._default_qos(ReliabilityPolicy.RELIABLE, depth=10)

            pub = self.create_publisher(msg_type, topic_name, qos_profile)
            self.publishers_map[topic_name] = {
                "type": "dummy",
                "publisher": pub,
            }
            print(f"dummy publisher created: {topic_name} [{topic_type_str}]")
            return

        if pub_type == "compressed":
            if output_topic is None:
                output_topic = f"{input_topic}/compressed"

            if input_qos_profile is None:
                input_qos_profile = self._default_qos(ReliabilityPolicy.RELIABLE, depth=5)

            if output_qos_profile is None:
                output_qos_profile = self._default_qos(ReliabilityPolicy.BEST_EFFORT, depth=5)

            pub = self.create_publisher(CompressedImage, output_topic, output_qos_profile)
            self.publishers_map[output_topic] = {
                "type": "compressed",
                "publisher": pub,
            }

            def callback(msg):
                if not self._should_run("publish", output_topic, hz):
                    return

                try:
                    compressed_data, fmt = self._encode_image_to_jpeg(msg, jpeg_quality)
                except Exception as e:
                    print(f"compressed publish failed: {input_topic} -> {output_topic} ({e})")
                    return

                out_msg = CompressedImage()
                out_msg.header = msg.header
                out_msg.format = fmt
                out_msg.data = compressed_data
                pub.publish(out_msg)

            sub = self.create_subscription(
                Image,
                input_topic,
                callback,
                input_qos_profile,
            )
            self.subscribers[f"{output_topic}__compressed_pub"] = sub
            print(f"compressed publisher created: {input_topic} -> {output_topic} hz={hz} quality={jpeg_quality}")
            return

        raise ValueError(f"unsupported publisher type: {pub_type}")

    def set_ros2_topic(self, topic_name, topic_type_str, hz=None, qos_profile=10, raw=False):
        if self.bridge_only:
            print(f"bridge_only=True, skip logging subscriber: {topic_name} [{topic_type_str}]")
            return

        msg_type = get_message(topic_type_str)

        def callback(msg):
            if not self._should_run("log", topic_name, hz):
                return

            data = self._save_raw_message(topic_name, msg) if raw else self._convert_value(msg)

            self.write_log(
                name=topic_name,
                type_=topic_type_str,
                data=data,
            )

        sub = self.create_subscription(
            msg_type,
            topic_name,
            callback,
            qos_profile,
        )
        self.subscribers[topic_name] = sub
        print(f"subscriber created: {topic_name} [{topic_type_str}] raw={raw}")

    def _encode_image_to_jpeg(self, msg, jpeg_quality):
        width = int(msg.width)
        height = int(msg.height)
        raw = bytes(msg.data)

        if width <= 0 or height <= 0:
            raise ValueError("invalid image size")

        msg_encoding = str(msg.encoding).lower()

        if msg_encoding == "bgr8":
            expected_size = width * height * 3
            if len(raw) < expected_size:
                raise ValueError(f"invalid data size for bgr8: {len(raw)} < {expected_size}")
            image = PIL_Image.frombytes("RGB", (width, height), raw[:expected_size], "raw", "BGR")

        elif msg_encoding == "rgb8":
            expected_size = width * height * 3
            if len(raw) < expected_size:
                raise ValueError(f"invalid data size for rgb8: {len(raw)} < {expected_size}")
            image = PIL_Image.frombytes("RGB", (width, height), raw[:expected_size], "raw", "RGB")

        elif msg_encoding == "mono8":
            expected_size = width * height
            if len(raw) < expected_size:
                raise ValueError(f"invalid data size for mono8: {len(raw)} < {expected_size}")
            image = PIL_Image.frombytes("L", (width, height), raw[:expected_size], "raw", "L")

        else:
            raise ValueError(f"unsupported encoding: {msg.encoding}")

        if self.crop_ratio < 1.0:
            crop_w = int(width * self.crop_ratio)
            crop_h = int(height * self.crop_ratio)

            left = (width - crop_w) // 2
            top = (height - crop_h) // 2
            right = left + crop_w
            bottom = top + crop_h

            image = image.crop((left, top, right, bottom))

        image = image.resize(( int(480*0.9), int(360*0.9)), PIL_Image.BILINEAR)

        buf = io.BytesIO()
        image.save(buf, format="JPEG", quality=int(jpeg_quality), optimize=False)
        return buf.getvalue(), "jpeg"

    def _convert_value(self, value):
        if isinstance(value, (bool, int, float, str)):
            return value

        if isinstance(value, (list, tuple)):
            return [self._convert_value(v) for v in value]

        if hasattr(value, "__slots__"):
            return {
                field.lstrip("_"): self._convert_value(getattr(value, field))
                for field in value.__slots__
            }

        return str(value)
