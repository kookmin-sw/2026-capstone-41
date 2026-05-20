import cv2
import multiprocessing
import numpy as np
import os
import queue
import time

os.environ["RMW_IMPLEMENTATION"] = "rmw_cyclonedds_cpp"


def publish_images(image_queue):
    import rclpy
    from sensor_msgs.msg import Image

    rclpy.init()
    node = rclpy.create_node("inner_camera_stream")
    rgb_pub = node.create_publisher(Image, "/camera/color/image_raw", 10)
    depth_pub = node.create_publisher(Image, "/camera/aligned_depth_to_color/image_raw", 10)

    try:
        while rclpy.ok():
            try:
                image_pack = image_queue.get(timeout=1)
            except queue.Empty:
                continue
            if image_pack is None:
                break
            rgb_image, depth_image = image_pack

            stamp = node.get_clock().now().to_msg()

            rgb_msg = Image()
            rgb_msg.header.stamp = stamp
            rgb_msg.header.frame_id = "camera_color_optical_frame"
            rgb_msg.height = rgb_image.shape[0]
            rgb_msg.width = rgb_image.shape[1]
            rgb_msg.encoding = "rgb8"
            rgb_msg.is_bigendian = 0
            rgb_msg.step = rgb_image.shape[1] * 3
            rgb_msg.data = rgb_image.tobytes()

            depth_msg = Image()
            depth_msg.header.stamp = stamp
            depth_msg.header.frame_id = "camera_aligned_depth_to_color_frame"
            depth_msg.height = depth_image.shape[0]
            depth_msg.width = depth_image.shape[1]
            depth_msg.encoding = "16UC1"
            depth_msg.is_bigendian = 0
            depth_msg.step = depth_image.shape[1] * 2
            depth_msg.data = depth_image.tobytes()

            rgb_pub.publish(rgb_msg)
            depth_pub.publish(depth_msg)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


def main():
    context = multiprocessing.get_context("spawn")
    image_queue = context.Queue(maxsize=1)
    publisher = context.Process(target=publish_images, args=(image_queue,))
    publisher.start()

    from unitree_sdk2py.core.channel import ChannelFactoryInitialize
    from unitree_sdk2py.go2.video.video_client import VideoClient

    ChannelFactoryInitialize(0)
    video_client = VideoClient()
    video_client.SetTimeout(3.0)
    video_client.Init()

    try:
        while publisher.is_alive():
            code, data = video_client.GetImageSample()
            if code != 0:
                time.sleep(0.1)
                continue

            if isinstance(data, list):
                data = bytes(data)
            if len(data) == 0:
                continue

            image = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
            if image is None:
                continue

            image = cv2.resize(image, (640, 480), interpolation=cv2.INTER_AREA)
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            depth_image = np.full((rgb_image.shape[0], rgb_image.shape[1]), 1000, dtype=np.uint16)

            if image_queue.full():
                try:
                    image_queue.get_nowait()
                except queue.Empty:
                    pass
            image_queue.put((rgb_image, depth_image))

            time.sleep(1.0 / 30.0)
    except KeyboardInterrupt:
        pass
    finally:
        if publisher.is_alive():
            try:
                if image_queue.full():
                    image_queue.get_nowait()
                image_queue.put_nowait(None)
            except queue.Empty:
                pass
            except queue.Full:
                pass
            publisher.join(timeout=2)
        if publisher.is_alive():
            publisher.terminate()
            publisher.join()
        image_queue.close()
        image_queue.join_thread()


if __name__ == "__main__":
    main()
