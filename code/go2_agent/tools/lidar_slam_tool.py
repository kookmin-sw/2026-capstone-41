import json
import math

from langchain.agents import tool

from .ros2 import execute_ros_command, ros2_service_list


def _trigger_payload(output):
    if "message='" not in output:
        return {"success": False, "error": output}
    try:
        return json.loads(output.split("message='", 1)[1].rsplit("'", 1)[0])
    except json.JSONDecodeError:
        return {"success": False, "error": output}


def _sparse_points(points, max_points=8):
    if len(points) <= max_points:
        return points
    step = (len(points) - 1) / (max_points - 1)
    return [points[round(index * step)] for index in range(max_points)]


def _path_length(points):
    total = 0.0
    for index in range(1, len(points)):
        dx = points[index][0] - points[index - 1][0]
        dy = points[index][1] - points[index - 1][1]
        total += math.hypot(dx, dy)
    return total


@tool
def get_lidar_slam_timestamp() -> dict:
    """
    Return the latest timestamp recorded by lidar_slam_runner.
    This does not move the robot.
    """
    success, output = execute_ros_command(
        "timeout 2 ros2 service call /lidar_slam_runner/backtracking "
        "std_srvs/srv/Trigger"
    )
    if not success:
        return {"success": False, "error": output}

    payload = _trigger_payload(output)
    timestamp = payload.get("latest_selected_stamp")
    if payload.get("success") and timestamp is not None:
        return {"success": True, "timestamp": timestamp}

    if timestamp is None:
        return {
            "success": False,
            "error": payload.get("error", "latest_selected_stamp missing."),
        }

    return {"success": False, "error": payload.get("error", "unknown error")}


@tool
def get_trajectory(seconds: float) -> dict:
    """
    Return a sparse backtracking trajectory and derived motion summary.
    This does not move the robot.
    """
    seconds = float(seconds)
    if seconds <= 0.0:
        return {"success": False, "error": "seconds must be positive."}

    services = ros2_service_list.invoke({"pattern": None, "blacklist": None})["services"]
    if "/lidar_slam_runner/backtracking" not in services:
        return {
            "success": False,
            "error": "Start utils/lidar_slam_runner.py first.",
        }

    command = "ros2 param set /lidar_slam_runner backtracking_seconds %s" % seconds
    success, output = execute_ros_command(command)
    if not success:
        return {"success": False, "error": output}

    _, output = execute_ros_command(
        "ros2 service call /lidar_slam_runner/backtracking std_srvs/srv/Trigger"
    )

    payload = _trigger_payload(output)
    if not payload.get("success"):
        return {
            "success": False,
            "error": payload.get("error", "unknown error"),
        }

    trajectory = payload.get("trajectory", [])
    current = payload.get("current_position")
    target = payload.get("target_past_position")
    duration = payload["latest_selected_stamp"] - payload["oldest_selected_stamp"]
    length = _path_length(trajectory)
    direct = math.hypot(target[0] - current[0], target[1] - current[1])
    direction = math.atan2(target[1] - current[1], target[0] - current[0])

    return {
        "success": True,
        "sample_count": payload.get("sample_count"),
        "trajectory_order": payload.get("trajectory_order"),
        "trajectory_sparse": _sparse_points(trajectory),
        "current_position": current,
        "target_past_position": target,
        "oldest_selected_stamp": payload.get("oldest_selected_stamp"),
        "latest_selected_stamp": payload.get("latest_selected_stamp"),
        "movement_anchor_stamp": payload.get("movement_anchor_stamp"),
        "path_length": length,
        "direct_distance": direct,
        "average_speed": length / duration if duration > 0.0 else None,
        "direction_to_target_rad": direction,
        "direction_to_target_deg": math.degrees(direction),
    }


@tool
def backtracking_via_second(seconds: float) -> dict:
    """
    Start forward-only backtracking drive to a past odom position.
    seconds : the time that user wants to drive to a past.
    """
    seconds = float(seconds)
    if seconds <= 0.0:
        return {"success": False, "error": "seconds must be positive."}

    command = "ros2 param set /lidar_slam_runner backtracking_seconds %s" % seconds
    success, output = execute_ros_command(command)
    if not success:
        return {"success": False, "error": output}

    success, output = execute_ros_command(
        "ros2 service call /lidar_slam_runner/backtracking_via_second "
        "std_srvs/srv/Trigger"
    )
    if not success:
        return {"success": False, "error": output}
    return _trigger_payload(output)


@tool
def backtracking_via_timestamp(timestamp: float) -> dict:
    """
    Start forward-only backtracking drive to a past odom timestamp.
    timestamp : absolute /utlidar/robot_odom stamp in seconds.
    """
    timestamp = float(timestamp)
    if timestamp < 0.0:
        return {"success": False, "error": "timestamp must be non-negative."}

    command = "ros2 param set /lidar_slam_runner backtracking_timestamp %s" % timestamp
    success, output = execute_ros_command(command)
    if not success:
        return {"success": False, "error": output}

    success, output = execute_ros_command(
        "ros2 service call /lidar_slam_runner/backtracking_via_timestamp "
        "std_srvs/srv/Trigger"
    )
    if not success:
        return {"success": False, "error": output}
    return _trigger_payload(output)


@tool
def stop_backtracking_drive() -> dict:
    """
    Stop the active backtracking drive.
    """
    services = ros2_service_list.invoke({"pattern": None, "blacklist": None})["services"]
    if "/lidar_slam_runner/stop_backtracking_drive" not in services:
        return {
            "success": False,
            "error": "Start utils/lidar_slam_runner.py first.",
        }

    _, output = execute_ros_command(
        "ros2 service call /lidar_slam_runner/stop_backtracking_drive "
        "std_srvs/srv/Trigger"
    )
    return _trigger_payload(output)
