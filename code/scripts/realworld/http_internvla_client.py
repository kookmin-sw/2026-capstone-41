import copy
import io
import json
import math
import threading
import time
from collections import deque
from enum import Enum
from unitree_api.msg import Request
import os
import sys
import signal
import subprocess
import time
import numpy as np
import rclpy
import requests
from nav_msgs.msg import Odometry
from PIL import Image as PIL_Image
from sensor_msgs.msg import Image
import cv2

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

frame_data = {}
frame_idx = 0
# user-specific
from controllers import Mpc_controller, PID_controller
from cv_bridge import CvBridge
from message_filters import ApproximateTimeSynchronizer, Subscriber
from rclpy.node import Node
from rclpy.qos import HistoryPolicy, QoSProfile, ReliabilityPolicy
from thread_utils import ReadWriteLock
from utils.deblurganv2_deblurrer import build_deblurrer
from std_msgs.msg import Bool
from std_srvs.srv import SetBool

run_enabled = threading.Event()

class ControlMode(Enum):
    PID_Mode = 1
    MPC_Mode = 2


# global variable
policy_init = True
mpc = None
pid = PID_controller(Kp_trans=2.0, Kd_trans=0.0, Kp_yaw=1.5, Kd_yaw=0.0, max_v=0.6, max_w=0.5)
http_idx = -1
first_running_time = 0.0
last_pixel_goal = None
last_s2_step = -1
manager = None
current_control_mode = ControlMode.MPC_Mode
trajs_in_world = None

desired_v, desired_w = 0.0, 0.0
rgb_depth_rw_lock = ReadWriteLock()
odom_rw_lock = ReadWriteLock()
mpc_rw_lock = ReadWriteLock()

####### Slowdown
ENABLE_BLUR_FILTER = False
TRAJ_SLOWDOWN_FACTOR = 4
# TRAJ_SLOWDOWN_FACTOR = 1
ROTATE_STEP_DEG = 22.0
####### Slowdown

def dual_sys_eval(image_bytes, depth_bytes, front_image_bytes, url='http://192.168.0.60:5801/eval_dual'):
    global policy_init, http_idx, first_running_time
    data = {"reset": policy_init, "idx": http_idx}
    json_data = json.dumps(data)

    policy_init = False
    files = {
        'image': ('rgb_image', image_bytes, 'image/jpeg'),
        'depth': ('depth_image', depth_bytes, 'image/png'),
    }
    start = time.time()
    response = requests.post(url, files=files, data={'json': json_data}, timeout=100)
    print(f"response {response.text}")
    http_idx += 1
    if http_idx == 0:
        first_running_time = time.time()
    print(f"idx: {http_idx} after http {time.time() - start}")

    return json.loads(response.text)

def control_thread():
    global desired_v, desired_w
    while True:
        if not run_enabled.is_set():
            time.sleep(0.1)
            continue

        global current_control_mode
        if current_control_mode == ControlMode.MPC_Mode:
            odom_rw_lock.acquire_read()
            odom = manager.odom.copy() if manager.odom else None
            odom_rw_lock.release_read()
            if mpc is not None and manager is not None and odom is not None:
                local_mpc = mpc
                opt_u_controls, opt_x_states = local_mpc.solve(np.array(odom))
                v, w = opt_u_controls[0, 0], opt_u_controls[0, 1]
                desired_v, desired_w = v, w
                manager.move(v, 0.0, w)

        elif current_control_mode == ControlMode.PID_Mode:
            odom_rw_lock.acquire_read()
            odom = manager.odom.copy() if manager.odom else None
            odom_rw_lock.release_read()
            homo_odom = manager.homo_odom.copy() if manager.homo_odom is not None else None
            vel = manager.vel.copy() if manager.vel is not None else None
            homo_goal = manager.homo_goal.copy() if manager.homo_goal is not None else None

            if homo_odom is not None and vel is not None and homo_goal is not None:
                v, w, e_p, e_r = pid.solve(homo_odom, homo_goal, vel)

                # print(f"Current Error -> e_p: {abs(e_p):.3f}, e_r: {abs(e_r):.3f}")

                MIN_W = 0.5
                if abs(e_r) >= 0.05 and abs(w) < MIN_W:
                    w = MIN_W if w > 0 else -MIN_W

                if v < 0.0:
                    v = 0.0

                desired_v, desired_w = v, w
                manager.move(v, 0.0, w)

        time.sleep(0.1)

def planning_thread():
    global trajs_in_world

    while True:
        if not run_enabled.is_set():
            time.sleep(0.1)
            continue

        start_time = time.time()
        DESIRED_TIME = 0.1
        time.sleep(0.05)

        if not manager.new_image_arrived:
            time.sleep(0.01)
            continue
        manager.new_image_arrived = False

        rgb_depth_rw_lock.acquire_read()
        rgb_bytes = copy.deepcopy(manager.rgb_bytes)
        depth_bytes = copy.deepcopy(manager.depth_bytes)
        infer_rgb = copy.deepcopy(manager.rgb_image)
        infer_depth = copy.deepcopy(manager.depth_image)
        rgb_time = manager.rgb_time
        rgb_depth_rw_lock.release_read()

        odom_rw_lock.acquire_read()
        min_diff = 1e10
        odom_infer = None
        for odom in manager.odom_queue:
            diff = abs(odom[0] - rgb_time)
            if diff < min_diff:
                min_diff = diff
                odom_infer = copy.deepcopy(odom[1])
        odom_rw_lock.release_read()

        if odom_infer is not None and rgb_bytes is not None and depth_bytes is not None:
            global frame_data
            frame_data[http_idx] = {
                'infer_rgb': copy.deepcopy(infer_rgb),
                'infer_depth': copy.deepcopy(infer_depth),
                'infer_odom': copy.deepcopy(odom_infer),
            }
            if len(frame_data) > 100:
                del frame_data[min(frame_data.keys())]

            response = dual_sys_eval(rgb_bytes, depth_bytes, None)

            global current_control_mode
            if 'trajectory' in response:
                trajectory = response['trajectory']
                trajs_in_world = []
                odom = odom_infer

                for i, traj in enumerate(trajectory):
                    if i < 3:
                        continue

                    x_, y_, yaw_ = odom[0], odom[1], odom[2]
                    w_T_b = np.array([
                        [np.cos(yaw_), -np.sin(yaw_), 0, x_],
                        [np.sin(yaw_),  np.cos(yaw_), 0, y_],
                        [0.0, 0.0, 1.0, 0],
                        [0.0, 0.0, 0.0, 1.0],
                    ])
                    w_P = (w_T_b @ np.array([traj[0], traj[1], 0.0, 1.0]).T)[:2]
                    trajs_in_world.append(w_P)

                trajs_in_world = np.array(trajs_in_world)

                if len(trajs_in_world) > 1:
                    old_indices = np.arange(len(trajs_in_world))
                    num_new_points = (len(trajs_in_world) - 1) * TRAJ_SLOWDOWN_FACTOR + 1
                    new_indices = np.linspace(0, len(trajs_in_world) - 1, num_new_points)
                    x_interp = np.interp(new_indices, old_indices, trajs_in_world[:, 0])
                    y_interp = np.interp(new_indices, old_indices, trajs_in_world[:, 1])
                    trajs_in_world = np.column_stack((x_interp, y_interp))

                manager.last_trajs_in_world = trajs_in_world

                mpc_rw_lock.acquire_write()
                global mpc
                if mpc is None:
                    mpc = Mpc_controller(np.array(trajs_in_world))
                else:
                    mpc.update_ref_traj(np.array(trajs_in_world))
                manager.request_cnt += 1
                mpc_rw_lock.release_write()

                current_control_mode = ControlMode.MPC_Mode

            elif 'discrete_action' in response:
                actions = response['discrete_action']
                if -1 in actions:
                    print("received -1 action, turning thread state OFF")
                    run_enabled.clear()
                    manager.move(0.0, 0.0, 0.0)
                    continue
                if actions != [5] and actions != [9]:
                    x_, y_, yaw_ = odom_infer
                    base_homo = np.array([
                        [np.cos(yaw_), -np.sin(yaw_), 0, x_],
                        [np.sin(yaw_),  np.cos(yaw_), 0, y_],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1],
                    ])
                    manager.incremental_change_goal(actions, base_homo=base_homo)
                    current_control_mode = ControlMode.PID_Mode
        else:
            print(f"skip planning. odom_infer: {odom_infer is not None} rgb_bytes: {rgb_bytes is not None} depth_bytes: {depth_bytes is not None}")
            time.sleep(0.1)

        time.sleep(max(0, DESIRED_TIME - (time.time() - start_time)))

class Go2Manager(Node):
    def __init__(self):
        super().__init__('go2_manager')

        rgb_down_sub = Subscriber(self, Image, "/camera/color/image_raw")
        depth_down_sub = Subscriber(self, Image, "/camera/aligned_depth_to_color/image_raw")

        qos_profile = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT, history=HistoryPolicy.KEEP_LAST, depth=10)

        self.syncronizer = ApproximateTimeSynchronizer([rgb_down_sub, depth_down_sub], 1, 0.1)
        self.syncronizer.registerCallback(self.rgb_depth_down_callback)
        self.odom_sub = self.create_subscription(Odometry, "/utlidar/robot_odom", self.odom_callback, qos_profile)
        self.control_pub = self.create_publisher(Request, '/api/obstacles_avoid/request', 5)
        self.toggle_srv = self.create_service(SetBool, '/toggle_run_threads', self.toggle_run_threads_cb)
        self.thread_state_pub = self.create_publisher(Bool, '/thread_state', 10)
        self.thread_state_timer = self.create_timer(0.5, self.publish_thread_state)

        # class member variable
        self.cv_bridge = CvBridge()
        self.deblurrer = build_deblurrer()
        self.rgb_image = None
        self.rgb_bytes = None
        self.depth_image = None
        self.depth_bytes = None
        self.rgb_forward_image = None
        self.rgb_forward_bytes = None
        self.new_image_arrived = False
        self.new_vis_image_arrived = False
        self.rgb_time = 0.0

        self.odom = None
        self.linear_vel = 0.0
        self.angular_vel = 0.0
        self.request_cnt = 0
        self.odom_cnt = 0
        self.odom_queue = deque(maxlen=50)
        self.odom_timestamp = 0.0

        self.last_s2_step = -1
        self.last_trajs_in_world = None
        self.last_all_trajs_in_world = None
        self.homo_odom = None
        self.homo_goal = None
        self.vel = None
        

        ######## Blur filter
        self.prev_img_pack = None
        self.LAPLACIAN_THRESHOLD = 80.0


    def publish_thread_state(self):
        msg = Bool()
        msg.data = run_enabled.is_set()
        self.thread_state_pub.publish(msg)

    def toggle_run_threads_cb(self, request, response):
        if request.data:
            run_enabled.set()
            response.message = "control/planning threads enabled"
        else:
            run_enabled.clear()
            self.move(0.0, 0.0, 0.0)
            response.message = "control/planning threads disabled"
        response.success = True
        return response

    def rgb_forward_callback(self, rgb_msg):
        raw_image = self.cv_bridge.imgmsg_to_cv2(rgb_msg, 'rgb8')[:, :, :]
        self.rgb_forward_image = raw_image
        image = PIL_Image.fromarray(self.rgb_forward_image)
        image_bytes = io.BytesIO()
        image.save(image_bytes, format='JPEG')
        image_bytes.seek(0)
        self.rgb_forward_bytes = image_bytes
        self.new_vis_image_arrived = True
        self.new_image_arrived = True

    def rgb_depth_down_callback(self, rgb_msg, depth_msg):
        raw_image = self.cv_bridge.imgmsg_to_cv2(rgb_msg, 'rgb8')[:, :, :]
        raw_depth = self.cv_bridge.imgmsg_to_cv2(depth_msg, '16UC1')

        ######## Blur filter
        # if ENABLE_BLUR_FILTER:
        #     if self.prev_img_pack is None:
        #         self.prev_img_pack = (raw_image.copy(), raw_depth.copy())
        #     else:
        #         gray = cv2.cvtColor(raw_image, cv2.COLOR_RGB2GRAY)
        #         laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()                
        #         if laplacian_var < self.LAPLACIAN_THRESHOLD:
        #             raw_image, raw_depth = self.prev_img_pack
        #         else:
        #             self.prev_img_pack = (raw_image.copy(), raw_depth.copy())
        self.rgb_image = self.deblurrer.deblur(raw_image)
        ######## Blur filter

        image = PIL_Image.fromarray(self.rgb_image)
        image_bytes = io.BytesIO()
        image.save(image_bytes, format='JPEG')
        image_bytes.seek(0)

        raw_depth[np.isnan(raw_depth)] = 0
        raw_depth[np.isinf(raw_depth)] = 0
        self.depth_image = raw_depth / 1000.0
        self.depth_image -= 0.0
        self.depth_image[np.where(self.depth_image < 0)] = 0
        depth = (np.clip(self.depth_image * 10000.0, 0, 65535)).astype(np.uint16)
        depth = PIL_Image.fromarray(depth)
        depth_bytes = io.BytesIO()
        depth.save(depth_bytes, format='PNG')
        depth_bytes.seek(0)

        rgb_depth_rw_lock.acquire_write()
        self.rgb_bytes = image_bytes

        self.rgb_time = rgb_msg.header.stamp.sec + rgb_msg.header.stamp.nanosec / 1.0e9
        self.last_rgb_time = self.rgb_time

        self.depth_bytes = depth_bytes
        self.depth_time = depth_msg.header.stamp.sec + depth_msg.header.stamp.nanosec / 1.0e9
        self.last_depth_time = self.depth_time

        rgb_depth_rw_lock.release_write()

        self.new_vis_image_arrived = True
        self.new_image_arrived = True

    def odom_callback(self, msg):
        self.odom_cnt += 1
        odom_rw_lock.acquire_write()
        zz = msg.pose.pose.orientation.z
        ww = msg.pose.pose.orientation.w
        yaw = math.atan2(2 * zz * ww, 1 - 2 * zz * zz)
        self.odom = [msg.pose.pose.position.x, msg.pose.pose.position.y, yaw]
        odom_time = msg.header.stamp.sec + msg.header.stamp.nanosec / 1.0e9
        self.odom_timestamp = odom_time
        self.odom_queue.append((odom_time, copy.deepcopy(self.odom)))
        self.linear_vel = msg.twist.twist.linear.x
        self.angular_vel = msg.twist.twist.angular.z
        odom_rw_lock.release_write()

        R0 = np.array([[np.cos(yaw), -np.sin(yaw)], [np.sin(yaw), np.cos(yaw)]])
        self.homo_odom = np.eye(4)
        self.homo_odom[:2, :2] = R0
        self.homo_odom[:2, 3] = [msg.pose.pose.position.x, msg.pose.pose.position.y]
        self.vel = [msg.twist.twist.linear.x, msg.twist.twist.angular.z]

        if self.odom_cnt == 1:
            self.homo_goal = self.homo_odom.copy()

    def incremental_change_goal(self, actions, base_homo=None):
        if self.homo_goal is None:
            raise ValueError("Please initialize homo_goal before change it!")
        # base_homo가 주어지면 그 시점(사진 찍힌 순간 odom_infer)을 기준으로 목표를 계산한다.
        # None이면 현재 위치 기준(구버전 동작, 과회전 발생 가능).
        homo_goal = base_homo.copy() if base_homo is not None else self.homo_odom.copy()
        for each_action in actions:
            if each_action == 0:
                pass
            elif each_action == 1:
                yaw = math.atan2(homo_goal[1, 0], homo_goal[0, 0])
                homo_goal[0, 3] += 0.25 * np.cos(yaw)
                homo_goal[1, 3] += 0.25 * np.sin(yaw)
            elif each_action == 2:
                angle = math.radians(ROTATE_STEP_DEG)
                rotation_matrix = np.array(
                    [[math.cos(angle), -math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 0, 1]]
                )
                homo_goal[:3, :3] = np.dot(rotation_matrix, homo_goal[:3, :3])
            elif each_action == 3:
                angle = -math.radians(ROTATE_STEP_DEG)
                rotation_matrix = np.array(
                    [[math.cos(angle), -math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 0, 1]]
                )
                homo_goal[:3, :3] = np.dot(rotation_matrix, homo_goal[:3, :3])
        self.homo_goal = homo_goal

    def make_avoid_request(self, api_id, parameter, noreply=True):
        req = Request()
        req.header.identity.id = time.monotonic_ns()
        req.header.identity.api_id = api_id
        req.header.lease.id = 0
        req.header.policy.priority = 0
        req.header.policy.noreply = noreply
        req.parameter = json.dumps(parameter, separators=(",", ":"))
        req.binary = []
        return req

    def move(self, vx, vy, vyaw):
        self.control_pub.publish(
            self.make_avoid_request(
                1003,
                {"x": float(vx), "y": float(vy), "yaw": float(vyaw), "mode": 0},
            )
        )

if __name__ == '__main__':
    control_thread_instance = threading.Thread(target=control_thread)
    planning_thread_instance = threading.Thread(target=planning_thread)
    control_thread_instance.daemon = True
    planning_thread_instance.daemon = True
    rclpy.init()
    print("waiting for client active")
    try:
        manager = Go2Manager()

        control_thread_instance.start()
        planning_thread_instance.start()

        rclpy.spin(manager)
    except KeyboardInterrupt:
        pass
    finally:
        manager.destroy_node()
        rclpy.shutdown()
