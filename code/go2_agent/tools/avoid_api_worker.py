import json
import sys
import time

import rclpy
from rclpy.node import Node
from unitree_api.msg import Request


def build_request(message):
    msg = Request()
    msg.header.identity.id = int(time.monotonic_ns())
    msg.header.identity.api_id = int(message["api_id"])
    msg.header.lease.id = 0
    msg.header.policy.priority = 0
    msg.header.policy.noreply = bool(message["noreply"])
    msg.parameter = json.dumps(message["parameter"], separators=(",", ":"))
    msg.binary = []
    return msg


def write_response(ok, **payload):
    payload["ok"] = ok
    sys.stdout.write(json.dumps(payload, separators=(",", ":")) + "\n")
    sys.stdout.flush()


def wait_for_subscriber(node, publisher, timeout_seconds):
    start = time.monotonic()
    while time.monotonic() - start < timeout_seconds:
        rclpy.spin_once(node, timeout_sec=0.05)
        if publisher.get_subscription_count() > 0:
            return True
    return False


def handle_publish(node, publisher, request):
    message = build_request(request["message"])
    duration_seconds = max(float(request.get("duration_seconds", 0.0)), 0.0)
    rate_hz = max(float(request.get("rate_hz", 10.0)), 1.0)
    interval = 1.0 / rate_hz
    match_timeout_seconds = max(float(request.get("match_timeout_seconds", 3.0)), 0.0)

    matched = wait_for_subscriber(node, publisher, match_timeout_seconds)
    publish_until = time.monotonic() + duration_seconds

    while True:
        publisher.publish(message)
        rclpy.spin_once(node, timeout_sec=0.0)
        if time.monotonic() >= publish_until:
            break
        time.sleep(interval)

    write_response(
        True,
        matched_subscriber=matched,
        subscription_count=publisher.get_subscription_count(),
        published_for=duration_seconds,
    )


def main():
    rclpy.init()
    node = Node("avoid_api_worker")
    publishers = {}

    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue

            try:
                request = json.loads(line)
            except json.JSONDecodeError as exc:
                write_response(False, error=str(exc))
                continue

            command = request.get("cmd")

            if command == "shutdown":
                write_response(True)
                break

            if command != "publish":
                write_response(False, error="Unknown command.")
                continue

            topic_name = request.get("topic_name")
            if not topic_name:
                write_response(False, error="Missing topic_name.")
                continue

            publisher = publishers.get(topic_name)
            if publisher is None:
                publisher = node.create_publisher(Request, topic_name, 10)
                publishers[topic_name] = publisher

            try:
                handle_publish(node, publisher, request)
            except Exception as exc:
                write_response(False, error=str(exc))
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
