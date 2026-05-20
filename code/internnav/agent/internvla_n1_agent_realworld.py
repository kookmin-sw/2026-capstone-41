import copy
import itertools
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import numpy as np
import torch

sys.path.append(str(Path(__file__).parent.parent.parent))

from collections import OrderedDict

from PIL import Image
from transformers import AutoProcessor

from internnav.model.basemodel.internvla_n1.internvla_n1 import InternVLAN1ForCausalLM
from internnav.model.utils.vln_utils import S2Output, split_and_clean, traj_to_actions

DEFAULT_IMAGE_TOKEN = "<image>"

# ------------------- YOLO ------------------
sys.path.append('/home/tenstorrent/LOVON')
from ultralytics import YOLO
from models.api_object_extraction import SequenceToSequenceClassAPI

import logging
logging.getLogger('ultralytics').setLevel(logging.ERROR)

# LOVON 모델 절대경로 하드코딩
YOLO_MODEL_PATH = "/home/tenstorrent/LOVON/deploy/models/yolo-models/yolo26x.pt"
OBJECT_EXTRACTION_MODEL_PATH = "/home/tenstorrent/LOVON/models/model_object_extraction_n1000000_d64_h4_l2_f256_msl64_hold_success_legacy"
LOVON_TOKENIZER_PATH = "/home/tenstorrent/LOVON/models/tokenizer_language2motion_n1000000"
# ------------------------------------------------

class InternVLAN1AsyncAgent:
    def __init__(self, args):
        self.device = torch.device(args.device)
        self.save_dir = "test_data/" + datetime.now().strftime("%Y%m%d_%H%M%S")
        os.makedirs(self.save_dir, exist_ok=True)
        print(f"args.model_path{args.model_path}")
        self.model = InternVLAN1ForCausalLM.from_pretrained(
            args.model_path,
            torch_dtype=torch.bfloat16,
            attn_implementation="flash_attention_2",
            device_map={"": self.device},
        )
        self.model.eval()
        self.model.to(self.device)

        self.processor = AutoProcessor.from_pretrained(args.model_path)
        self.processor.tokenizer.padding_side = 'left'

        self.resize_w = args.resize_w
        self.resize_h = args.resize_h
        self.num_history = args.num_history
        # S2 Inference gap
        # S1 is inferred every time
        self.PLAN_STEP_GAP = args.plan_step_gap

        prompt = "You are an autonomous navigation assistant. Your task is to <instruction>. Where should you go next to stay on track? Please output the next waypoint's coordinates in the image. Please output STOP when you have successfully completed the task."
        answer = ""
        self.conversation = [{"from": "human", "value": prompt}, {"from": "gpt", "value": answer}]
        self.conjunctions = [
            'you can see ',
            'in front of you is ',
            'there is ',
            'you can spot ',
            'you are toward the ',
            'ahead of you is ',
            'in your sight is ',
        ]

        self.actions2idx = OrderedDict(
            {
                'STOP': [0],
                "↑": [1],
                "←": [2],
                "→": [3],
                "↓": [5],
            }
        )

        self.rgb_list = []
        self.depth_list = []
        self.pose_list = []
        self.episode_idx = 0
        self.conversation_history = []
        self.llm_output = ""
        self.past_key_values = None
        self.last_s2_idx = -100

        # output
        self.output_action = None
        self.output_latent = None
        self.output_pixel = None
        self.pixel_goal_rgb = None
        self.pixel_goal_depth = None
        self.output_source = None
        self.output_target = None
        self.output_trajectory_cache = None
        self.has_seen_first_yolo = False
        self.pre_yolo_stop_count = 0
        self.pre_yolo_stop_limit = 5
        self.search_turn_action = None
        self.miss_action_history = []

        # YOLO + Object Extractor 초기화 (LOVON 절대경로)
        self.yolo_model = YOLO(YOLO_MODEL_PATH)
        self.object_extractor = SequenceToSequenceClassAPI(
            model_path=OBJECT_EXTRACTION_MODEL_PATH,
            tokenizer_path=LOVON_TOKENIZER_PATH,
        )
        # confidence score의 threshold 초기화 (default=0.5)
        self.yolo_conf_threshold = getattr(args, 'yolo_conf_threshold', 0.5)
        # 최근 3개 same-target YOLO 결과만 짧게 유지하고, 현재 프레임이 미검출이면 최근 valid detection들의 평균값으로 한 번 fallback 하도록 넣었습니다.
        self.yolo_history_size = 3
        self.yolo_history_target = None
        self.yolo_history = []
        self.yolo_traj_mismatch_target = None
        self.yolo_traj_mismatch_count = 0
        self.yolo_traj_mismatch_limit = 2
        self.llm_traj_mismatch_count = 0
        self.llm_traj_mismatch_limit = 2

    def reset(self):
        self.rgb_list = []
        self.depth_list = []
        self.pose_list = []
        self.episode_idx = 0
        self.conversation_history = []
        self.llm_output = ""
        self.past_key_values = None

        self.output_action = None
        self.output_latent = None
        self.output_pixel = None
        self.pixel_goal_rgb = None
        self.pixel_goal_depth = None
        self.output_source = None
        self.output_target = None
        self.output_trajectory_cache = None
        self.has_seen_first_yolo = False
        self.pre_yolo_stop_count = 0
        self.search_turn_action = None
        self.miss_action_history = []

        self.save_dir = "test_data/" + datetime.now().strftime("%Y%m%d_%H%M%S")
        os.makedirs(self.save_dir, exist_ok=True)
        self.input_images = []
        self.yolo_history_target = None
        self.yolo_history = []
        self.yolo_traj_mismatch_target = None
        self.yolo_traj_mismatch_count = 0
        self.llm_traj_mismatch_count = 0
        torch.cuda.empty_cache()

    def parse_actions(self, output):
        action_patterns = '|'.join(re.escape(action) for action in self.actions2idx)
        regex = re.compile(action_patterns)
        matches = regex.findall(output)
        actions = [self.actions2idx[match] for match in matches]
        actions = itertools.chain.from_iterable(actions)
        return list(actions)

    def step_no_infer(self, rgb, depth, pose):
        image = Image.fromarray(rgb).convert('RGB')
        image = image.resize((self.resize_w, self.resize_h))
        self.rgb_list.append(image)
        image.save(f"{self.save_dir}/debug_raw_{self.episode_idx: 04d}.jpg")
        self.episode_idx += 1

    def trajectory_tovw(self, trajectory, kp=1.0):
        subgoal = trajectory[-1]
        linear_vel, angular_vel = kp * np.linalg.norm(subgoal[:2]), kp * subgoal[2]
        linear_vel = np.clip(linear_vel, 0, 0.5)
        angular_vel = np.clip(angular_vel, -0.5, 0.5)
        return linear_vel, angular_vel

    def _find_target_bbox(self, yolo_results, target_object):
        """YOLO 결과에서 target_object의 가장 높은 confidence bbox 중심 반환.

        Args:
            yolo_results: YOLO model inference 결과
            target_object: 찾으려는 객체 이름 (e.g., "chair", "person")

        Returns:
            (cx, cy, conf) tuple in original image pixel coordinates + confidence,
            or None if not found or confidence below threshold
        """
        best_conf = 0.0
        best_center = None
        best_bbox = None
        for result in yolo_results:
            for box in result.boxes:
                class_name = result.names[int(box.cls)]
                conf = float(box.conf)
                if class_name == target_object and conf > best_conf:
                    best_conf = conf
                    x1, y1, x2, y2 = box.xyxy[0].tolist()
                    best_center = ((x1 + x2) / 2, (y1 + y2) / 2)
                    best_bbox = (int(x1), int(y1), int(x2), int(y2))

        # threshold 미만이면 무시하고 None 반환
        if best_center is not None and best_conf < self.yolo_conf_threshold:
            print(
                f"[YOLO] target={target_object} detected but confidence "
                f"{best_conf:.3f} < threshold {self.yolo_conf_threshold}, ignoring."
            )
            return None

        if best_center is not None:
            return (best_center[0], best_center[1], best_conf, best_bbox)
        return None

    def _scale_yolo_to_llm_coords(self, cx, cy, orig_h, orig_w):
        """YOLO 좌표(원본 해상도)를 LLM 좌표(리사이즈 해상도)로 스케일링.

        YOLO는 원본 이미지 해상도에서 동작하고,
        LLM은 resize_w x resize_h로 리사이즈된 이미지에서 좌표를 출력하므로
        좌표계를 맞춰야 한다.

        Args:
            cx, cy: YOLO bbox 중심 (원본 해상도 기준 pixel 좌표)
            orig_h, orig_w: 원본 이미지의 높이, 너비

        Returns:
            (cx_scaled, cy_scaled): LLM 좌표계로 스케일링된 정수 좌표
        """
        scale_x = self.resize_w / orig_w
        scale_y = self.resize_h / orig_h
        cx_scaled = int(cx * scale_x)
        cy_scaled = int(cy * scale_y)
        return cx_scaled, cy_scaled

    def _is_valid_depth(self, depth_value):
        return np.isfinite(depth_value) and 0.05 < float(depth_value) < 10.0

    def _find_yolo_goal_point(self, bbox, depth):
        """bbox 중심이 아니라 하단부에서 depth가 유효한 navigation point를 찾습니다."""
        img_h, img_w = depth.shape[:2]
        x1, y1, x2, y2 = bbox
        box_h = max(1, y2 - y1)
        base_x = int(round((x1 + x2) / 2))
        base_y = int(min(img_h - 1, max(0, y2 - max(4, box_h // 10))))

        x_offsets = [0, -8, 8, -16, 16, -24, 24, -32, 32]
        y_offsets = [0, -6, -12, -18, 6, 12]
        for dy in y_offsets:
            y = int(np.clip(base_y + dy, 0, img_h - 1))
            for dx in x_offsets:
                x = int(np.clip(base_x + dx, 0, img_w - 1))
                depth_value = depth[y, x]
                if self._is_valid_depth(depth_value):
                    return x, y, float(depth_value)
        return None

    def _trajectory_matches_goal(self, planned_trajectory, goal_pixel):
        traj = np.asarray(planned_trajectory)
        if traj.ndim != 2 or traj.shape[0] < 2 or traj.shape[1] < 2:
            return False

        goal_dx = float(goal_pixel[1]) - (self.resize_w / 2.0)
        side_margin = max(12.0, self.resize_w * 0.06)
        probe_idx = min(len(traj) - 1, 3)
        p1_idx = min(len(traj) - 1, 1)
        p2_idx = min(len(traj) - 1, 2)
        endpoint = traj[-1]
        probe_point = traj[probe_idx]
        p1 = traj[p1_idx]
        p2 = traj[p2_idx]
        forward_endpoint = float(endpoint[0])
        lateral_endpoint = float(endpoint[1])
        lateral_probe = float(probe_point[1])
        min_early_lateral = float(min(p1[1], p2[1], probe_point[1]))
        max_early_lateral = float(max(p1[1], p2[1], probe_point[1]))

        if forward_endpoint < -0.02:
            return False
        if goal_dx < -side_margin:
            if lateral_endpoint < -0.03 or lateral_probe < -0.01 or min_early_lateral < -0.02:
                return False
        elif goal_dx > side_margin:
            if lateral_endpoint > 0.03 or lateral_probe > 0.01 or max_early_lateral > 0.02:
                return False
        else:
            if abs(lateral_endpoint) > 0.08 or abs(lateral_probe) > 0.03:
                return False
        return True

    def _goal_side_action(self, goal_pixel):
        goal_dx = float(goal_pixel[1]) - (self.resize_w / 2.0)
        side_margin = max(12.0, self.resize_w * 0.06)
        if goal_dx < -side_margin:
            return [2]
        if goal_dx > side_margin:
            return [3]
        return [1]

    def _postprocess_trajectory_for_goal(self, planned_trajectory, goal_pixel):
        traj = np.asarray(planned_trajectory, dtype=np.float32).copy()
        if traj.ndim != 2 or traj.shape[0] < 2 or traj.shape[1] < 2:
            return planned_trajectory

        goal_dx = float(goal_pixel[1]) - (self.resize_w / 2.0)
        side_margin = max(12.0, self.resize_w * 0.06)
        start_idx = min(len(traj) - 1, 3)
        if start_idx <= 0:
            return traj

        for i in range(1, len(traj)):
            if traj[i, 0] < traj[i - 1, 0]:
                traj[i, 0] = traj[i - 1, 0]

        lateral_target = min(0.18, max(0.03, 0.16 * abs(goal_dx) / (self.resize_w / 2.0)))
        ramp_steps = 6.0
        if goal_dx < -side_margin:
            for i in range(start_idx, len(traj)):
                progress = min(1.0, (i - start_idx + 1) / ramp_steps)
                traj[i, 1] = max(traj[i, 1], lateral_target * progress)
        elif goal_dx > side_margin:
            for i in range(start_idx, len(traj)):
                progress = min(1.0, (i - start_idx + 1) / ramp_steps)
                traj[i, 1] = min(traj[i, 1], -lateral_target * progress)
        else:
            for i in range(start_idx, len(traj)):
                traj[i, 1] *= 0.35
        return traj

    def step(self, rgb, depth, pose, instruction, intrinsic, look_down=False):
        dual_sys_output = S2Output()
        yolo_output = None
        no_output_flag = self.output_action is None and self.output_latent is None
        if (self.episode_idx - self.last_s2_idx > self.PLAN_STEP_GAP) or look_down or no_output_flag:
            self.output_action, self.output_latent, self.output_pixel, yolo_output = self.step_s2(
                rgb, depth, pose, instruction, intrinsic, look_down
            )
            self.output_trajectory_cache = None
            self.last_s2_idx = self.episode_idx
            dual_sys_output.output_pixel = self.output_pixel
            self.pixel_goal_rgb = copy.deepcopy(rgb)
            self.pixel_goal_depth = copy.deepcopy(depth)
        else:
            self.step_no_infer(rgb, depth, pose)

        if self.output_action is not None:
            dual_sys_output.output_action = copy.deepcopy(self.output_action)
            self.output_action = None
            self.output_source = None
            self.output_target = None
            self.output_trajectory_cache = None
        elif self.output_latent is not None:
            if self.output_trajectory_cache is None:
                processed_pixel_rgb = np.array(Image.fromarray(self.pixel_goal_rgb).resize((224, 224))) / 255
                processed_pixel_depth = np.array(Image.fromarray(self.pixel_goal_depth).resize((224, 224)))
                processed_rgb = np.array(Image.fromarray(rgb).resize((224, 224))) / 255
                processed_depth = np.array(Image.fromarray(depth).resize((224, 224)))

                rgbs = (
                    torch.stack([torch.from_numpy(processed_pixel_rgb), torch.from_numpy(processed_rgb)])
                    .unsqueeze(0)
                    .to(self.device)
                )
                depths = (
                    torch.stack([torch.from_numpy(processed_pixel_depth), torch.from_numpy(processed_depth)])
                    .unsqueeze(0)
                    .unsqueeze(-1)
                    .to(self.device)
                )
                trajectories = self.step_s1(self.output_latent, rgbs, depths)
                planned_trajectory = traj_to_actions(trajectories, use_discrate_action=False)
                if self.output_source == "YOLO" and self.output_pixel is not None:
                    planned_trajectory = self._postprocess_trajectory_for_goal(
                        planned_trajectory, self.output_pixel
                    )
                self.output_trajectory_cache = copy.deepcopy(planned_trajectory)
            else:
                planned_trajectory = copy.deepcopy(self.output_trajectory_cache)
            if self.output_pixel is not None:
                traj = np.asarray(planned_trajectory)
                traj_p0 = traj[0].tolist() if traj.ndim == 2 and len(traj) > 0 else None
                traj_p1 = traj[1].tolist() if traj.ndim == 2 and len(traj) > 1 else None
                traj_p2 = traj[2].tolist() if traj.ndim == 2 and len(traj) > 2 else None
                traj_p3 = traj[3].tolist() if traj.ndim == 2 and len(traj) > 3 else None
                traj_end = traj[-1].tolist() if traj.ndim == 2 and len(traj) > 0 else None
                traj_match = self._trajectory_matches_goal(planned_trajectory, self.output_pixel)
                print(
                    f"[TRAJ] src={self.output_source} goal={self.output_pixel} "
                    f"live_yolo={yolo_output is not None} "
                    f"planner_mode={None if yolo_output is None else yolo_output.get('planner_mode')} "
                    f"cached={self.output_trajectory_cache is not None} "
                    f"p0={traj_p0} p1={traj_p1} p2={traj_p2} p3={traj_p3} end={traj_end} "
                    f"match={traj_match}"
                )
                if self.output_source == "YOLO":
                    current_target = self.output_target
                    if current_target != self.yolo_traj_mismatch_target:
                        self.yolo_traj_mismatch_target = current_target
                        self.yolo_traj_mismatch_count = 0
                    if not self._trajectory_matches_goal(planned_trajectory, self.output_pixel):
                        if yolo_output is not None and yolo_output.get('planner_mode') == 'yolo_direct':
                            fallback_action = self._goal_side_action(self.output_pixel)
                            print(
                                f"[YOLO] visible target but inconsistent trajectory for goal={self.output_pixel}, "
                                f"override with action={fallback_action}"
                            )
                            self.output_latent = None
                            self.output_pixel = None
                            self.output_source = None
                            self.output_target = None
                            self.output_trajectory_cache = None
                            dual_sys_output.output_pixel = None
                            dual_sys_output.output_action = fallback_action
                            return dual_sys_output, yolo_output
                        self.yolo_traj_mismatch_count += 1
                        self.llm_traj_mismatch_count = 0
                        if self.yolo_traj_mismatch_count <= self.yolo_traj_mismatch_limit:
                            print(
                                f"[YOLO] inconsistent trajectory for goal={self.output_pixel}, "
                                f"hold with STOP ({self.yolo_traj_mismatch_count}/{self.yolo_traj_mismatch_limit})"
                            )
                            dual_sys_output.output_pixel = None
                            dual_sys_output.output_action = [0]
                            return dual_sys_output, yolo_output
                        print(
                            f"[YOLO] inconsistent trajectory persists for target={current_target}, "
                            "allow trajectory to continue."
                        )
                    else:
                        self.yolo_traj_mismatch_count = 0
                    self.llm_traj_mismatch_count = 0
                else:
                    self.yolo_traj_mismatch_target = None
                    self.yolo_traj_mismatch_count = 0
                    if not self._trajectory_matches_goal(planned_trajectory, self.output_pixel):
                        self.llm_traj_mismatch_count += 1
                        if self.llm_traj_mismatch_count <= self.llm_traj_mismatch_limit:
                            print(
                                f"[LLM] inconsistent trajectory for goal={self.output_pixel}, "
                                f"hold with STOP ({self.llm_traj_mismatch_count}/{self.llm_traj_mismatch_limit})"
                            )
                            dual_sys_output.output_pixel = None
                            dual_sys_output.output_action = [0]
                            return dual_sys_output, yolo_output
                        print(
                            "[LLM] inconsistent trajectory persists for pixel goal, "
                            "allow trajectory to continue."
                        )
                    else:
                        self.llm_traj_mismatch_count = 0
            else:
                self.yolo_traj_mismatch_target = None
                self.yolo_traj_mismatch_count = 0
                self.llm_traj_mismatch_count = 0
            dual_sys_output.output_trajectory = planned_trajectory

        return dual_sys_output, yolo_output

    def step_s2(self, rgb, depth, pose, instruction, intrinsic, look_down=False):
        image = Image.fromarray(rgb).convert('RGB')
        if not look_down:
            image = image.resize((self.resize_w, self.resize_h))
            self.rgb_list.append(image)
            image.save(f"{self.save_dir}/debug_raw_{self.episode_idx: 04d}.jpg")
        else:
            image.save(f"{self.save_dir}/debug_raw_{self.episode_idx: 04d}_look_down.jpg")
            image = image.resize((self.resize_w, self.resize_h))
        if not look_down:
            self.conversation_history = []
            self.past_key_values = None

            sources = copy.deepcopy(self.conversation)
            sources[0]["value"] = sources[0]["value"].replace('<instruction>', instruction)
            cur_images = self.rgb_list[-1:]
            if self.episode_idx == 0:
                history_id = []
            else:
                history_id = np.unique(np.linspace(0, self.episode_idx - 1, self.num_history, dtype=np.int32)).tolist()
                placeholder = (DEFAULT_IMAGE_TOKEN + '\n') * len(history_id)
                sources[0]["value"] += f' These are your historical observations: {placeholder}.'

            history_id = sorted(history_id)
            self.input_images = [self.rgb_list[i] for i in history_id] + cur_images
            input_img_id = 0
            self.episode_idx += 1
        else:
            self.input_images.append(image)
            input_img_id = -1
            assert self.llm_output != "", "Last llm_output should not be empty when look down"
            sources = [{"from": "human", "value": ""}, {"from": "gpt", "value": ""}]
            self.conversation_history.append(
                {'role': 'assistant', 'content': [{'type': 'text', 'text': self.llm_output}]}
            )

        ############################## CHANGED
        # prompt = self.conjunctions[0] + DEFAULT_IMAGE_TOKEN
        prompt = self.conjunctions[-1] + DEFAULT_IMAGE_TOKEN
        ############################## CHANGED
        sources[0]["value"] += f" {prompt}."
        prompt_instruction = copy.deepcopy(sources[0]["value"])
        parts = split_and_clean(prompt_instruction)

        content = []
        for i in range(len(parts)):
            if parts[i] == "<image>":
                content.append({"type": "image", "image": self.input_images[input_img_id]})
                input_img_id += 1
            else:
                content.append({"type": "text", "text": parts[i]})

        self.conversation_history.append({'role': 'user', 'content': content})

        text = self.processor.apply_chat_template(self.conversation_history, tokenize=False, add_generation_prompt=True)

        inputs = self.processor(text=[text], images=self.input_images, return_tensors="pt").to(self.device)

        # ---- YOLO detection (LLM generate 전에 실행) ----
        target_object = self.object_extractor.predict(instruction) # TODO: instruction 바뀔 때만 새로 호출하도록 최적화
        rgb_bgr = rgb[:, :, ::-1]  # RGB → BGR (YOLO expects BGR)
        yolo_results = self.yolo_model(rgb_bgr, verbose=False)
        yolo_detection = self._find_target_bbox(yolo_results, target_object)
        if target_object != self.yolo_history_target:
            self.yolo_history_target = target_object
            self.yolo_history = []
        self.yolo_history.append(yolo_detection)
        if len(self.yolo_history) > self.yolo_history_size:
            self.yolo_history.pop(0)
        yolo_center = (yolo_detection[0], yolo_detection[1]) if yolo_detection else None
        yolo_conf = yolo_detection[2] if yolo_detection else None
        yolo_bbox = yolo_detection[3] if yolo_detection else None
        yolo_output = None  # YOLO 감지 결과 (감지 시 채워짐)

        if yolo_detection is not None:
            orig_h, orig_w = rgb.shape[:2]
            goal_point = self._find_yolo_goal_point(yolo_bbox, depth)
            if goal_point is not None:
                goal_x, goal_y, _ = goal_point
                goal_x_scaled, goal_y_scaled = self._scale_yolo_to_llm_coords(
                    goal_x, goal_y, orig_h, orig_w
                )
                yolo_coord_str = f"{goal_x_scaled}, {goal_y_scaled}"
                yolo_output = {
                    'target': target_object,
                    'confidence': yolo_conf,
                    'coord': yolo_coord_str,
                    'bbox': yolo_bbox,
                    'planner_mode': 'yolo_direct',
                }
                pixel_goal = [goal_y_scaled, goal_x_scaled]  # [y, x] LLM 좌표계
                self.output_source = "YOLO"
                self.output_target = target_object
                self.llm_output = yolo_coord_str
                with open(f"{self.save_dir}/llm_output_{self.episode_idx: 04d}.txt", 'w') as f:
                    f.write(self.llm_output)
                yolo_tokens = self.processor.tokenizer.encode(
                    yolo_coord_str, add_special_tokens=False
                )
                yolo_token_ids = torch.tensor([yolo_tokens], device=inputs.input_ids.device)
                modified_output_ids = torch.cat([inputs.input_ids, yolo_token_ids], dim=1)
                image_grid_thw = torch.cat(
                    [thw.unsqueeze(0) for thw in inputs.image_grid_thw], dim=0
                )
                pixel_values = inputs.pixel_values
                with torch.inference_mode():
                    traj_latents = self.model.generate_latents(
                        modified_output_ids, pixel_values, image_grid_thw
                    )
                traj_latents = traj_latents.clone()
                print(
                    f"[YOLO] target={target_object}, conf={yolo_conf:.3f}, "
                    f"goal_pixel={pixel_goal}, bbox={yolo_bbox}"
                )
                print(
                    f"[GOAL] src=YOLO target={target_object} bbox={yolo_bbox} "
                    f"goal_raw=({goal_x}, {goal_y}, {goal_point[2]:.3f}) "
                    f"goal_scaled={pixel_goal} goal_dx={goal_x_scaled - self.resize_w / 2:.1f}"
                )
                print("[YOLO] visible target, generate trajectory and postprocess it")
                self.has_seen_first_yolo = True
                self.pre_yolo_stop_count = 0
                self.search_turn_action = None
                self.miss_action_history = []
                del inputs, pixel_values, image_grid_thw
                torch.cuda.empty_cache()
                return None, traj_latents, pixel_goal, yolo_output
            print(
                f"[YOLO] target={target_object} detected but goal point is invalid, "
                "fallback to LLM."
            )

        t0 = time.time()
        with torch.inference_mode():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=128,
                do_sample=False,
                return_dict_in_generate=True,
            )
        output_ids = outputs.sequences

        t1 = time.time()
        self.llm_output = self.processor.tokenizer.decode(
            output_ids[0][inputs.input_ids.shape[1] :], skip_special_tokens=True
        )
        is_pixel_goal = bool(re.search(r'\d', self.llm_output))
        if not is_pixel_goal and self.llm_output != 'STOP':
            self.llm_output = self.llm_output[0]
        with open(f"{self.save_dir}/llm_output_{self.episode_idx: 04d}.txt", 'w') as f:
            f.write(self.llm_output)
        self.last_output_ids = copy.deepcopy(output_ids[0])
        self.past_key_values = copy.deepcopy(outputs.past_key_values)
        print(f"output {self.episode_idx}  {self.llm_output} cost: {t1 - t0}s")

        # ---- YOLO 미감지 → 기존 LLM 기반 분기 유지 ----
        if is_pixel_goal:
            coord = [int(c) for c in re.findall(r'\d+', self.llm_output)]
            pixel_goal = [int(coord[1]), int(coord[0])]
            self.output_source = "LLM_PIXEL"
            self.output_target = None
            self.pre_yolo_stop_count = 0
            self.search_turn_action = None
            self.miss_action_history = []
            print(
                f"[GOAL] src=LLM_PIXEL text='{self.llm_output}' "
                f"goal_scaled={pixel_goal} goal_dx={coord[0] - self.resize_w / 2:.1f}"
            )
            image_grid_thw = torch.cat([thw.unsqueeze(0) for thw in inputs.image_grid_thw], dim=0)
            pixel_values = inputs.pixel_values
            t0 = time.time()
            with torch.inference_mode():
                traj_latents = self.model.generate_latents(output_ids, pixel_values, image_grid_thw)
            return None, traj_latents, pixel_goal, None
        else:
            action_seq = self.parse_actions(self.llm_output)
            action_seq = [0 if action == 5 else action for action in action_seq]
            primary_action = action_seq[0] if len(action_seq) > 0 else 0
            self.miss_action_history.append(primary_action)
            if len(self.miss_action_history) > 3:
                self.miss_action_history = self.miss_action_history[-3:]
            if primary_action == 0:
                self.pre_yolo_stop_count += 1
            else:
                self.pre_yolo_stop_count = 0
            if not self.has_seen_first_yolo:
                recent_actions = self.miss_action_history[-3:]
                if recent_actions == [2, 0, 3]:
                    self.search_turn_action = 2
                    print("[SEARCH] pattern [2, 0, 3] detected, lock search direction to LEFT")
                elif recent_actions == [3, 0, 2]:
                    self.search_turn_action = 3
                    print("[SEARCH] pattern [3, 0, 2] detected, lock search direction to RIGHT")
                if self.search_turn_action is None and self.pre_yolo_stop_count >= self.pre_yolo_stop_limit:
                    last_turn_action = next((action for action in reversed(self.miss_action_history) if action in [2, 3]), 3)
                    self.search_turn_action = last_turn_action
                    print(
                        f"[SEARCH] repeated STOP before first YOLO ({self.pre_yolo_stop_count}), "
                        f"ignore STOP and lock search direction to {self.search_turn_action}"
                    )
                if self.search_turn_action is not None:
                    self.output_source = "SEARCH_ACTION"
                    self.output_target = None
                    return [self.search_turn_action], None, None, None
            self.output_source = "ACTION"
            self.output_target = None
            return action_seq, None, None, None

    def step_s1(self, latent, rgb, depth):
        latent = latent.to(self.device, non_blocking=True)
        with torch.inference_mode():
            all_trajs = self.model.generate_traj(latent, rgb, depth)
        return all_trajs
