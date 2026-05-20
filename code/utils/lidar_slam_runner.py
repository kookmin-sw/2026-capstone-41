#!/usr/bin/env python3

from dataclasses import dataclass, field
import json
import math
import os
import time
from collections import deque

os.environ.setdefault("RMW_IMPLEMENTATION", "rmw_cyclonedds_cpp")
os.environ.setdefault("ROS_LOCALHOST_ONLY", "0")
os.environ.setdefault("CYCLONEDDS_URI", "/home/unitree/cyclonedds_ws/cyclonedds.xml")

import rclpy
from nav_msgs.msg import Odometry
from rclpy.node import Node
from rclpy.qos import HistoryPolicy, QoSProfile, ReliabilityPolicy
from std_srvs.srv import Trigger
from unitree_api.msg import Request

DEBUG_BACKTRACKING = True
BT_DEBUG_ODOM_INTERVAL_SEC = 2.0
DISTANCE_GAIN = 1
CACHE_TTL_SEC = 0.1
MAX_HISTORY_SEC = 600.0
MOVEMENT_EPS = 0.05
MOVEMENT_EPS_SEC = 0.5
MAX_BACKTRACKING_POINTS = 200
MAX_DRIVE_WAYPOINTS = 24
WAYPOINT_TOLERANCE = 0.1
GOAL_TOLERANCE = 0.2
ANGLE_THRESHOLD = 0.35
FORWARD_SPEED = 0.5
YAW_GAIN = 1.2
MAX_YAW_SPEED = 0.55
MIN_DRIVE_TIMEOUT = 8.0
MAX_DRIVE_TIMEOUT = 35.0


def path_length_xy(path):
    total = 0.0
    for i in range(1, len(path)):
        dx = path[i][0] - path[i - 1][0]
        dy = path[i][1] - path[i - 1][1]
        total += math.hypot(dx, dy)
    return total


def downsample_points(points, max_points):
    count = min(len(points), max_points)
    if count == 0:
        return []
    if count == 1:
        return [points[0]]
    last = len(points) - 1
    step = float(last) / float(count - 1)
    return [points[int(round(float(index) * step))] for index in range(count)]


def angle_diff(target, current):
    return math.atan2(math.sin(target - current), math.cos(target - current))


def clamp(value, limit):
    return max(-limit, min(limit, value))


def yaw_from_orientation(q):
    return math.atan2(2.0 * (q.w * q.z + q.x * q.y), 1.0 - 2.0 * (q.y * q.y + q.z * q.z))


def empty_backtracking_payload():
    return {
        "success": False,
        "error": "No odometry samples have been received yet.",
        "source_topic": "/utlidar/robot_odom",
        "sample_count": 0,
        "trajectory": [],
    }


def backtracking_error_payload(error, **fields):
    payload = empty_backtracking_payload()
    payload["error"] = error
    payload.update(fields)
    return payload


def set_json_response(response, payload):
    response.success = payload["success"]
    response.message = json.dumps(payload, separators=(",", ":"))
    return response


def bt_debug_value(value):
    if isinstance(value, float):
        return "%.2f" % value
    if isinstance(value, (list, tuple)):
        return "[%s]" % ",".join(bt_debug_value(item) for item in value)
    return str(value)


def bt_debug(event, **values):
    if not DEBUG_BACKTRACKING:
        return
    fields = ["event=%s" % event]
    for key, value in values.items():
        fields.append("%s=%s" % (key, bt_debug_value(value)))
    print("BT_DEBUG %s" % " ".join(fields), flush=True)


class OdomHistoryBuffer:
    def __init__(self, max_history_sec, movement_eps=None, movement_sec=None):
        self.max_history_sec = max_history_sec
        self.movement_eps = movement_eps
        self.movement_sec = movement_sec
        self.last_movement_anchor_stamp = None
        self.last_movement_anchor_distance = 0.0
        self.samples = deque()

    def __len__(self):
        return len(self.samples)

    def append_odom(self, stamp, x, y, z, yaw):
        self.samples.append((stamp, x, y, z, yaw))
        self.update_movement_anchor(stamp, x, y)
        cutoff = stamp - self.max_history_sec
        while self.samples and self.samples[0][0] < cutoff:
            self.samples.popleft()
        if (
            self.samples
            and self.last_movement_anchor_stamp is not None
            and self.last_movement_anchor_stamp < self.samples[0][0]
        ):
            self.last_movement_anchor_stamp = None
            self.last_movement_anchor_distance = 0.0

    def update_movement_anchor(self, stamp, x, y):
        if self.movement_eps is None or self.movement_sec is None:
            return

        baseline = None
        target_stamp = stamp - self.movement_sec
        for entry in reversed(self.samples):
            if entry[0] <= target_stamp:
                baseline = entry
                break
        if baseline is None:
            return

        distance = math.hypot(x - baseline[1], y - baseline[2])
        if distance >= self.movement_eps:
            self.last_movement_anchor_stamp = stamp
            self.last_movement_anchor_distance = distance

    def latest(self):
        if not self.samples:
            return None
        return self.samples[-1]

    def stamp_bounds(self):
        if not self.samples:
            return None, None
        stamps = [entry[0] for entry in self.samples]
        return min(stamps), max(stamps)

    def recent_since(self, seconds):
        latest = self.latest()
        if latest is None:
            return []

        cutoff = latest[0] - seconds
        selected = []
        for entry in reversed(self.samples):
            if entry[0] < cutoff:
                break
            selected.append(entry)
        selected.reverse()
        return selected

    def recent_downsampled(self, seconds, max_points):
        return downsample_points(self.recent_since(seconds), max_points)

    def movement_anchor(self, movement_eps, movement_sec):
        latest = self.latest()
        if latest is None:
            return None, False, 0.0

        if movement_eps == self.movement_eps and movement_sec == self.movement_sec:
            if self.last_movement_anchor_stamp is None:
                return latest[0], False, 0.0
            return self.last_movement_anchor_stamp, True, self.last_movement_anchor_distance

        if len(self.samples) < 2:
            return latest[0], False, 0.0

        samples = list(self.samples)
        start_index = 0
        anchor_stamp = None
        anchor_distance = 0.0
        for end_index, end in enumerate(samples):
            while (
                start_index + 1 < end_index
                and samples[start_index + 1][0] <= end[0] - movement_sec
            ):
                start_index += 1
            if end[0] - samples[start_index][0] < movement_sec * 0.8:
                continue

            distance = math.hypot(end[1] - samples[start_index][1], end[2] - samples[start_index][2])
            if distance >= movement_eps:
                anchor_stamp = end[0]
                anchor_distance = distance

        if anchor_stamp is None:
            latest = self.latest()
            return latest[0], False, 0.0
        return anchor_stamp, True, anchor_distance

    def anchored_downsampled(self, seconds, max_points, movement_eps, movement_sec):
        anchor_stamp, found, anchor_distance = self.movement_anchor(movement_eps, movement_sec)
        if anchor_stamp is None:
            return [], None, False, 0.0

        cutoff = anchor_stamp - seconds
        selected = []
        for entry in reversed(self.samples):
            if entry[0] > anchor_stamp:
                continue
            if entry[0] < cutoff:
                break
            selected.append(entry)
        selected.reverse()
        return downsample_points(selected, max_points), anchor_stamp, found, anchor_distance

    def timestamp_downsampled(self, timestamp, max_points):
        if not self.samples:
            return [], False

        sorted_samples = sorted(self.samples, key=lambda entry: entry[0])
        selected = [entry for entry in sorted_samples if entry[0] >= timestamp]
        clamped_to_oldest = timestamp < sorted_samples[0][0]
        return downsample_points(selected, max_points), clamped_to_oldest


@dataclass
class BacktrackingSnapshot:
    seconds: float
    selected: list
    anchor_stamp: float
    movement_found: bool
    anchor_distance: float
    mode: str = "second"
    requested_timestamp: float = None
    timestamp_clamped_to_oldest: bool = False
    oldest_available_stamp: float = None
    latest_available_stamp: float = None
    _trajectory: list = field(default=None, init=False, repr=False)

    def trajectory(self):
        if self._trajectory is None:
            self._trajectory = [list(entry[1:4]) for entry in reversed(self.selected)]
        return self._trajectory

    def to_payload(self):
        trajectory = self.trajectory()
        payload = {
            "success": True,
            "mode": self.mode,
            "source_topic": "/utlidar/robot_odom",
            "requested_seconds": self.seconds,
            "sample_count": len(trajectory),
            "trajectory_order": "current_to_past",
            "trajectory": trajectory,
            "current_position": trajectory[0],
            "current_yaw": self.selected[-1][4],
            "target_past_position": trajectory[-1],
            "oldest_selected_stamp": self.selected[0][0],
            "latest_selected_stamp": self.selected[-1][0],
            "movement_anchor_stamp": self.anchor_stamp,
            "movement_anchor_found": self.movement_found,
            "movement_anchor_distance": self.anchor_distance,
            "safety": "Reverse movement is prohibited. Follow waypoints by turning toward the next waypoint and commanding forward motion only.",
            "generated_at": time.time(),
        }
        if self.requested_timestamp is not None:
            payload["requested_timestamp"] = self.requested_timestamp
            payload["timestamp_clamped_to_oldest"] = self.timestamp_clamped_to_oldest
        if self.oldest_available_stamp is not None:
            payload["oldest_available_stamp"] = self.oldest_available_stamp
            payload["latest_available_stamp"] = self.latest_available_stamp
        return payload


class LidarSlamRunner(Node):
    def __init__(self):
        super().__init__("lidar_slam_runner")
        self.declare_parameter("backtracking_seconds", 10.0)
        self.declare_parameter("backtracking_timestamp", 0.0)
        self.history = OdomHistoryBuffer(MAX_HISTORY_SEC, MOVEMENT_EPS, MOVEMENT_EPS_SEC)
        self.drive_path = []
        self.drive_index = 0
        self.drive_active = False
        self.drive_started_at = 0.0
        self.drive_timeout = MIN_DRIVE_TIMEOUT
        self.last_drive_log_at = 0.0
        self.last_drive_log_index = None
        self.cached_snapshot_key = None
        self.cached_snapshot = None
        self.cached_at = 0.0
        self.last_odom_debug_at = 0.0

        qos = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT, history=HistoryPolicy.KEEP_LAST, depth=100)
        self.odom_subscription = self.create_subscription(Odometry, "/utlidar/robot_odom", self.odom_callback, qos)
        self.avoid_publisher = self.create_publisher(Request, "/api/obstacles_avoid/request", 10)
        self.backtracking_service = self.create_service(Trigger, "/lidar_slam_runner/backtracking", self.backtracking_callback)
        self.second_drive_service = self.create_service(Trigger, "/lidar_slam_runner/backtracking_via_second", self.backtracking_via_second_callback)
        self.timestamp_drive_service = self.create_service(Trigger, "/lidar_slam_runner/backtracking_via_timestamp", self.backtracking_via_timestamp_callback)
        self.drive_service = self.create_service(Trigger, "/lidar_slam_runner/start_backtracking_drive", self.backtracking_via_second_callback)
        self.stop_drive_service = self.create_service(Trigger, "/lidar_slam_runner/stop_backtracking_drive", self.stop_backtracking_drive_callback)
        self.drive_timer = self.create_timer(0.1, self.drive_step)
        self.report_timer = self.create_timer(5.0, self.report_status)

    def odom_callback(self, msg):
        stamp = float(msg.header.stamp.sec) + float(msg.header.stamp.nanosec) * 1e-9
        if not stamp:
            stamp = float(self.get_clock().now().nanoseconds) * 1e-9

        pose = msg.pose.pose.position
        x = float(pose.x)
        y = float(pose.y)
        z = float(pose.z)
        yaw = yaw_from_orientation(msg.pose.pose.orientation)
        self.history.append_odom(
            stamp,
            x,
            y,
            z,
            yaw,
        )
        now = time.time()
        if now - self.last_odom_debug_at >= BT_DEBUG_ODOM_INTERVAL_SEC:
            recent = self.history.recent_since(self.get_backtracking_seconds())
            if recent:
                raw_direct = math.hypot(recent[-1][1] - recent[0][1], recent[-1][2] - recent[0][2])
                duration = recent[-1][0] - recent[0][0]
            else:
                raw_direct = 0.0
                duration = 0.0
            bt_debug(
                "odom",
                samples=len(self.history),
                publishers=self.count_publishers("/utlidar/robot_odom"),
                pos=[x, y],
                sec=self.get_backtracking_seconds(),
                dur=duration,
                win_samples=len(recent),
                raw_m=raw_direct,
                scaled_m=raw_direct * DISTANCE_GAIN,
            )
            self.last_odom_debug_at = now

    def get_backtracking_seconds(self):
        return max(0.0, float(self.get_parameter("backtracking_seconds").value))

    def get_backtracking_timestamp(self):
        return float(self.get_parameter("backtracking_timestamp").value)

    def get_cached_snapshot(self, cache_key):
        now = time.time()
        if (
            self.cached_snapshot is not None
            and self.cached_snapshot_key == cache_key
            and now - self.cached_at <= CACHE_TTL_SEC
        ):
            return self.cached_snapshot
        return None

    def cache_snapshot(self, cache_key, snapshot):
        self.cached_snapshot_key = cache_key
        self.cached_snapshot = snapshot
        self.cached_at = time.time()

    def build_snapshot_via_second(self):
        seconds = self.get_backtracking_seconds()
        cache_key = ("second", seconds)
        cached = self.get_cached_snapshot(cache_key)
        if cached is not None:
            return cached, None

        selected, anchor_stamp, movement_found, anchor_distance = self.history.anchored_downsampled(
            seconds,
            MAX_BACKTRACKING_POINTS,
            MOVEMENT_EPS,
            MOVEMENT_EPS_SEC,
        )
        if not selected:
            bt_debug(
                "snapshot_empty",
                requested_seconds=seconds,
                history_samples=len(self.history),
            )
            return None, empty_backtracking_payload()

        selected_path = [list(entry[1:4]) for entry in selected]
        raw_length = path_length_xy(selected_path)
        raw_direct = math.hypot(
            selected[-1][1] - selected[0][1],
            selected[-1][2] - selected[0][2],
        )
        bt_debug(
            "snapshot",
            sec=seconds,
            samples=len(selected),
            dur=selected[-1][0] - selected[0][0],
            anchor_age=self.history.latest()[0] - anchor_stamp,
            moved=movement_found,
            anchor_m=anchor_distance,
            raw_path=raw_length,
            scaled_path=raw_length * DISTANCE_GAIN,
            raw_m=raw_direct,
            scaled_m=raw_direct * DISTANCE_GAIN,
        )

        snapshot = BacktrackingSnapshot(seconds, selected, anchor_stamp, movement_found, anchor_distance)
        self.cache_snapshot(cache_key, snapshot)
        return snapshot, None

    def build_snapshot_via_timestamp(self):
        timestamp = self.get_backtracking_timestamp()
        oldest_stamp, latest_stamp = self.history.stamp_bounds()
        if oldest_stamp is None:
            return None, empty_backtracking_payload()

        if timestamp < oldest_stamp:
            return None, backtracking_error_payload(
                "requested timestamp is older than the oldest odometry sample in history.",
                requested_timestamp=timestamp,
                oldest_available_stamp=oldest_stamp,
                latest_available_stamp=latest_stamp,
            )

        if timestamp > latest_stamp:
            return None, backtracking_error_payload(
                "requested timestamp is newer than the latest odometry sample.",
                requested_timestamp=timestamp,
                oldest_available_stamp=oldest_stamp,
                latest_available_stamp=latest_stamp,
            )

        cache_key = ("timestamp", timestamp)
        cached = self.get_cached_snapshot(cache_key)
        if cached is not None:
            return cached, None

        selected, clamped_to_oldest = self.history.timestamp_downsampled(
            timestamp,
            MAX_BACKTRACKING_POINTS,
        )
        if not selected:
            return None, empty_backtracking_payload()

        selected_path = [list(entry[1:4]) for entry in selected]
        raw_length = path_length_xy(selected_path)
        raw_direct = math.hypot(
            selected[-1][1] - selected[0][1],
            selected[-1][2] - selected[0][2],
        )
        seconds = selected[-1][0] - selected[0][0]
        bt_debug(
            "snapshot_timestamp",
            timestamp=timestamp,
            samples=len(selected),
            dur=seconds,
            clamped=clamped_to_oldest,
            oldest_available=oldest_stamp,
            latest_available=latest_stamp,
            first_selected=selected[0][0],
            raw_path=raw_length,
            scaled_path=raw_length * DISTANCE_GAIN,
            raw_m=raw_direct,
            scaled_m=raw_direct * DISTANCE_GAIN,
        )

        snapshot = BacktrackingSnapshot(
            seconds,
            selected,
            None,
            False,
            0.0,
            mode="timestamp",
            requested_timestamp=timestamp,
            timestamp_clamped_to_oldest=clamped_to_oldest,
            oldest_available_stamp=oldest_stamp,
            latest_available_stamp=latest_stamp,
        )
        self.cache_snapshot(cache_key, snapshot)
        return snapshot, None

    def build_snapshot(self):
        snapshot, _error_payload = self.build_snapshot_via_second()
        return snapshot

    def make_backtracking_payload(self):
        snapshot, error_payload = self.build_snapshot_via_second()
        if error_payload is not None:
            return error_payload
        return snapshot.to_payload()

    def backtracking_callback(self, request, response):
        del request
        payload = self.make_backtracking_payload()
        return set_json_response(response, payload)

    def make_avoid_request(self, api_id, parameter, noreply=True):
        msg = Request()
        msg.header.identity.id = time.monotonic_ns()
        msg.header.identity.api_id = api_id
        msg.header.lease.id = 0
        msg.header.policy.priority = 0
        msg.header.policy.noreply = noreply
        msg.parameter = json.dumps(parameter, separators=(",", ":"))
        msg.binary = []
        return msg

    def publish_avoid_ready(self):
        bt_debug("avoid_ready_publish")
        self.avoid_publisher.publish(
            self.make_avoid_request(1001, {"enable": True}, noreply=False)
        )
        self.avoid_publisher.publish(
            self.make_avoid_request(
                1004,
                {"is_remote_commands_from_api": True},
                noreply=False,
            )
        )

    def publish_move(self, x, z):
        payload = {"x": float(x), "y": 0.0, "yaw": float(z), "mode": 0}
        self.avoid_publisher.publish(self.make_avoid_request(1003, payload))

    def publish_stop(self):
        self.publish_move(0.0, 0.0)

    def stop_drive(self, reason):
        self.drive_path = []
        self.drive_index = 0
        self.drive_active = False
        self.drive_started_at = 0.0
        self.drive_timeout = MIN_DRIVE_TIMEOUT
        self.last_drive_log_at = 0.0
        self.last_drive_log_index = None
        self.publish_stop()
        bt_debug("drive_stop", reason=reason)
        print("backtracking_drive_stop: %s" % reason, flush=True)

    def add_start_profile(self, payload, mode, started_at, snapshot_sec, prepare_sec=0.0, publish_ready_sec=0.0):
        payload["profile"] = {
            "mode": mode,
            "snapshot_build_sec": snapshot_sec,
            "drive_prepare_sec": prepare_sec,
            "publish_ready_sec": publish_ready_sec,
            "total_service_sec": time.perf_counter() - started_at,
        }
        return payload

    def start_drive_from_snapshot(self, snapshot, mode, started_at, snapshot_sec):
        prepare_started_at = time.perf_counter()
        if len(snapshot.selected) < 2:
            payload = snapshot.to_payload()
            payload["status"] = "not_started_not_enough_samples"
            return self.add_start_profile(payload, mode, started_at, snapshot_sec)

        trajectory = snapshot.trajectory()
        drive_path = downsample_points(trajectory, MAX_DRIVE_WAYPOINTS)

        raw_length = path_length_xy(drive_path)
        length = raw_length * DISTANCE_GAIN
        start = drive_path[0]
        goal = drive_path[-1]
        raw_direct = math.hypot(goal[0] - start[0], goal[1] - start[1])
        direct = raw_direct * DISTANCE_GAIN
        bt_debug(
            "drive_start_check",
            waypoints=len(drive_path),
            gain=DISTANCE_GAIN,
            raw_path=raw_length,
            scaled_path=length,
            raw_m=raw_direct,
            scaled_m=direct,
            threshold=0.30,
        )

        if direct < 0.30:
            bt_debug(
                "drive_start_reject_short_path",
                scaled_m=direct,
                scaled_path=length,
                threshold=0.30,
                raw_m=raw_direct,
                raw_path=raw_length,
            )
            return self.add_start_profile(
                {
                    "success": False,
                    "mode": mode,
                    "error": "Backtracking path is too short in /utlidar/robot_odom frame.",
                    "direct_distance": direct,
                    "path_length": length,
                },
                mode,
                started_at,
                snapshot_sec,
                time.perf_counter() - prepare_started_at,
            )

        drive_timeout = min(
            MAX_DRIVE_TIMEOUT,
            max(MIN_DRIVE_TIMEOUT, snapshot.seconds * 4.0),
        )
        self.drive_path = drive_path
        self.drive_index = 1
        self.drive_active = True
        self.drive_started_at = time.time()
        self.drive_timeout = drive_timeout
        self.last_drive_log_at = 0.0
        self.last_drive_log_index = None
        prepare_sec = time.perf_counter() - prepare_started_at
        publish_started_at = time.perf_counter()
        self.publish_avoid_ready()
        publish_ready_sec = time.perf_counter() - publish_started_at
        bt_debug(
            "drive_started",
            mode=mode,
            timeout=self.drive_timeout,
            waypoints=len(self.drive_path),
            target_past_position=trajectory[-1],
        )

        return self.add_start_profile(
            {
                "success": True,
                "mode": mode,
                "status": "backtracking_drive_started",
                "waypoints": len(self.drive_path),
                "target_past_position": trajectory[-1],
                "timeout": self.drive_timeout,
                "safety": "Forward-only closed-loop follower started. Reverse movement is prohibited.",
            },
            mode,
            started_at,
            snapshot_sec,
            prepare_sec,
            publish_ready_sec,
        )

    def start_backtracking_mode(self, request, response, mode):
        del request
        started_at = time.perf_counter()
        snapshot_started_at = time.perf_counter()
        if mode == "timestamp":
            snapshot, error_payload = self.build_snapshot_via_timestamp()
        else:
            snapshot, error_payload = self.build_snapshot_via_second()
        snapshot_sec = time.perf_counter() - snapshot_started_at

        if error_payload is not None:
            payload = self.add_start_profile(error_payload, mode, started_at, snapshot_sec)
            return set_json_response(response, payload)

        payload = self.start_drive_from_snapshot(snapshot, mode, started_at, snapshot_sec)
        return set_json_response(response, payload)

    def backtracking_via_second_callback(self, request, response):
        return self.start_backtracking_mode(request, response, "second")

    def backtracking_via_timestamp_callback(self, request, response):
        return self.start_backtracking_mode(request, response, "timestamp")

    def start_backtracking_drive_callback(self, request, response):
        return self.backtracking_via_second_callback(request, response)

    def stop_backtracking_drive_callback(self, request, response):
        del request
        self.stop_drive("service_request")
        return set_json_response(response, {"success": True, "status": "backtracking_drive_stopped"})

    def drive_step(self):
        if not self.drive_active:
            return
        latest = self.history.latest()
        if latest is None:
            self.stop_drive("no_odom")
            return
        now = time.time()
        if now - self.drive_started_at > self.drive_timeout:
            self.stop_drive("timeout")
            return

        _stamp, x, y, _z, yaw = latest
        target = self.drive_path[self.drive_index]
        dx, dy = target[0] - x, target[1] - y
        distance = math.hypot(dx, dy)
        tolerance = (
            GOAL_TOLERANCE if self.drive_index == len(self.drive_path) - 1 else WAYPOINT_TOLERANCE
        ) / DISTANCE_GAIN
        scaled_distance = distance * DISTANCE_GAIN
        scaled_tolerance = tolerance * DISTANCE_GAIN

        error = angle_diff(math.atan2(dy, dx), yaw)
        yaw_cmd = clamp(YAW_GAIN * error, MAX_YAW_SPEED)
        x_cmd = 0.0 if abs(error) > ANGLE_THRESHOLD else FORWARD_SPEED

        if distance < tolerance:
            bt_debug(
                "drive_step_skip",
                index=self.drive_index,
                dist=scaled_distance,
                tol=scaled_tolerance,
            )
            self.drive_index += 1
            if self.drive_index >= len(self.drive_path):
                self.stop_drive("goal_reached")
            return

        if self.drive_index != self.last_drive_log_index or now - self.last_drive_log_at >= 1.0:
            bt_debug(
                "drive_step_publish",
                index=self.drive_index,
                waypoints=len(self.drive_path),
                elapsed=now - self.drive_started_at,
                timeout=self.drive_timeout,
                dist=scaled_distance,
                tol=scaled_tolerance,
                error=error,
                cmd_x=x_cmd,
                cmd_yaw=yaw_cmd,
            )
            self.last_drive_log_at = now
            self.last_drive_log_index = self.drive_index

        self.publish_move(x_cmd, yaw_cmd)

    def report_status(self):
        print("odom_samples: %d publishers=%d drive_active=%s" % (len(self.history), self.count_publishers("/utlidar/robot_odom"), self.drive_active), flush=True)


def main():
    rclpy.init(args=None)
    node = LidarSlamRunner()
    print("lidar_slam_runner started", flush=True)
    print("odom_topic: /utlidar/robot_odom", flush=True)
    print("service: /lidar_slam_runner/backtracking", flush=True)
    print("drive_service_second: /lidar_slam_runner/backtracking_via_second", flush=True)
    print("drive_service_timestamp: /lidar_slam_runner/backtracking_via_timestamp", flush=True)
    print("drive_service_legacy: /lidar_slam_runner/start_backtracking_drive", flush=True)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("stop requested", flush=True)
    finally:
        node.destroy_node()
        rclpy.shutdown()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
