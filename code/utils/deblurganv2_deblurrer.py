import os
import sys
import time

import cv2
import numpy as np
import torch
import torch.nn as nn

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _candidate_deblurgan_dirs():
    env_dir = os.getenv("DEBLURGANV2_DIR", "").strip()
    candidates = [
        env_dir,
        os.path.join(ROOT_DIR, "DeblurGANv2"),
        os.path.join(ROOT_DIR, "Thirdparty", "deblurganv2"),
        os.path.join(ROOT_DIR, "okiamtrash", "DeblurGANv2"),
    ]
    return [os.path.abspath(path) for path in candidates if path]


def _resolve_deblurgan_dir():
    for path in _candidate_deblurgan_dirs():
        if os.path.isdir(path):
            return path
    return os.path.abspath(os.path.join(ROOT_DIR, "Thirdparty", "deblurganv2"))


DEBLURGAN_DIR = _resolve_deblurgan_dir()
if DEBLURGAN_DIR not in sys.path:
    sys.path.insert(0, DEBLURGAN_DIR)


def _resolve_default_weights():
    env_weights = os.getenv("DEBLURGANV2_WEIGHTS", "").strip()
    candidates = [
        env_weights,
        os.path.join(DEBLURGAN_DIR, "weights", "fpn_mobilenet.h5"),
        os.path.join(DEBLURGAN_DIR, "fpn_mobilenet.h5"),
        os.path.join(ROOT_DIR, "weights", "fpn_mobilenet.h5"),
        os.path.join(ROOT_DIR, "utils", "fpn_mobilenet.h5"),
        os.path.join(os.path.expanduser("~"), ".cache", "deblurganv2", "fpn_mobilenet.h5"),
    ]
    for path in candidates:
        if path and os.path.exists(path):
            return os.path.abspath(path)
    return os.path.abspath(os.path.join(DEBLURGAN_DIR, "weights", "fpn_mobilenet.h5"))


try:
    from run_mobilenet_deblur import DEFAULT_WEIGHTS, MobileNetDeblurPredictor
except ModuleNotFoundError:
    DEFAULT_WEIGHTS = _resolve_default_weights()
    from aug import get_normalize
    from models.fpn_mobilenet import FPNMobileNet

    def get_norm_layer(norm_type="instance"):
        if norm_type == "batch":
            return nn.BatchNorm2d
        if norm_type == "instance":
            return lambda channels: nn.InstanceNorm2d(
                channels,
                affine=False,
                track_running_stats=True,
            )
        raise ValueError(f"Unsupported norm layer: {norm_type}")

    def strip_module_prefix(state_dict):
        if not state_dict:
            return state_dict
        first_key = next(iter(state_dict))
        if not first_key.startswith("module."):
            return state_dict
        return {key[len("module.") :]: value for key, value in state_dict.items()}

    class MobileNetDeblurPredictor:
        def __init__(self, weights_path, device="auto", use_fp16=None):
            self.weights_path = os.path.abspath(weights_path)
            if not os.path.exists(self.weights_path):
                raise FileNotFoundError(
                    "DeblurGAN-v2 MobileNet weights not found: "
                    f"{self.weights_path}. Set DEBLURGANV2_WEIGHTS to fpn_mobilenet.h5."
                )

            if device == "auto":
                device = "cuda" if torch.cuda.is_available() else "cpu"
            self.device = torch.device(device)
            if use_fp16 is None:
                use_fp16 = self.device.type == "cuda"
            self.use_fp16 = bool(use_fp16 and self.device.type == "cuda")

            if self.device.type == "cuda":
                torch.backends.cudnn.benchmark = True

            model = FPNMobileNet(
                norm_layer=get_norm_layer("instance"),
                pretrained=False,
            )
            checkpoint = torch.load(self.weights_path, map_location="cpu")
            state_dict = checkpoint["model"] if isinstance(checkpoint, dict) and "model" in checkpoint else checkpoint
            model.load_state_dict(strip_module_prefix(state_dict), strict=True)

            self.model = model.to(self.device)
            self.model.eval()
            if self.use_fp16:
                self.model = self.model.half()
            self.normalize_fn = get_normalize()

            print(
                f"[DeblurGANv2-MobileNet] weights={self.weights_path} "
                f"device={self.device} fp16={self.use_fp16}"
            )
            self._warmup()

        @staticmethod
        def _array_to_batch(x):
            x = np.transpose(x, (2, 0, 1))
            x = np.expand_dims(x, 0)
            return torch.from_numpy(x)

        def _preprocess(self, x):
            x, _ = self.normalize_fn(x, x)
            h, w, _ = x.shape

            block_size = 32
            min_height = ((h + block_size - 1) // block_size) * block_size
            min_width = ((w + block_size - 1) // block_size) * block_size

            x = np.pad(
                x,
                mode="constant",
                constant_values=0,
                pad_width=((0, min_height - h), (0, min_width - w), (0, 0)),
            )
            tensor = self._array_to_batch(x)
            tensor = tensor.half() if self.use_fp16 else tensor.float()
            return tensor, h, w

        @staticmethod
        def _postprocess(x):
            x = x[0].detach().cpu().float().numpy()
            x = (np.transpose(x, (1, 2, 0)) + 1.0) / 2.0 * 255.0
            return np.clip(x, 0, 255).astype(np.uint8)

        def _warmup(self):
            if self.device.type != "cuda":
                return
            dummy = np.zeros((480, 640, 3), dtype=np.uint8)
            img_tensor, _, _ = self._preprocess(dummy)
            img_tensor = img_tensor.to(self.device)
            start = time.time()
            with torch.inference_mode():
                _ = self.model(img_tensor)
            torch.cuda.synchronize(self.device)
            print(f"[DeblurGANv2-MobileNet] warmup_ms={(time.time() - start) * 1000.0:.1f}")

        def predict_rgb(self, img_rgb):
            original_height, original_width = img_rgb.shape[:2]
            img_tensor, h, w = self._preprocess(img_rgb)
            img_tensor = img_tensor.to(self.device)
            with torch.inference_mode():
                pred = self.model(img_tensor)
            out = self._postprocess(pred)[:h, :w, :]
            if out.shape[:2] != (original_height, original_width):
                out = cv2.resize(
                    out,
                    (original_width, original_height),
                    interpolation=cv2.INTER_LINEAR,
                )
            return out


class DeblurGANV2Deblurrer:
    def __init__(self, weights_path, device):
        self.predictor = MobileNetDeblurPredictor(
            weights_path=weights_path,
            device=device,
        )

    def deblur(self, rgb_image):
        return self.predictor.predict_rgb(rgb_image)


def build_deblurrer():
    weights_path = os.path.abspath(os.getenv("DEBLURGANV2_WEIGHTS", DEFAULT_WEIGHTS))
    device = os.getenv("DEBLURGANV2_DEVICE", "cuda")
    return DeblurGANV2Deblurrer(
        weights_path=weights_path,
        device=device,
    )
