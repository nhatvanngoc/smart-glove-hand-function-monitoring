"""
Eye-Tracking Pipeline — Stereo Pupil + Gaze Estimation
=====================================================
Reference implementation using OpenCV. For production, swap MediaPipe Face Mesh
(tham khảo docs/07_ML_Models.md).

Pipeline:
    Frame sync → Rectify → Pupil detect → Stereo triangulate → Gaze vector
                  │
                  └──→ Robot arm recenter face ROI
"""
from __future__ import annotations
import numpy as np
from dataclasses import dataclass
from typing import Tuple, Optional


# Camera intrinsics (placeholder; calibrated at runtime)
DEFAULT_K = np.array([[600.0, 0, 320], [0, 600, 240], [0, 0, 1]], dtype=np.float32)
DEFAULT_D = np.zeros((4, 1), dtype=np.float32)
BASELINE_MM = 60.0


@dataclass
class StereoEyeTracker:
    K1: np.ndarray = None
    K2: np.ndarray = None
    D1: np.ndarray = None
    D2: np.ndarray = None
    baseline: float = BASELINE_MM
    R: np.ndarray = None   # 3x3 rotation between cams
    T: np.ndarray = None   # 3x1 translation

    def __post_init__(self):
        self.K1 = self.K1 if self.K1 is not None else DEFAULT_K.copy()
        self.K2 = self.K2 if self.K2 is not None else DEFAULT_K.copy()
        self.D1 = self.D1 if self.D1 is not None else DEFAULT_D.copy()
        self.D2 = self.D2 if self.D2 is not None else DEFAULT_D.copy()
        self.R = self.R if self.R is not None else np.eye(3, dtype=np.float32)
        self.T = self.T if self.T is not None else np.array([[self.baseline], [0], [0]], dtype=np.float32)

    def detect_pupil(self, frame_gray: np.ndarray) -> Optional[Tuple[int, int, int]]:
        """Detect pupil via simple blob detection (OpenCV SimpleBlobDetector
        in production; here fallback heuristic for offline testing).

        Returns (cx, cy, radius) in pixel coordinates, or None.
        """
        if frame_gray is None or frame_gray.size == 0:
            return None
        # Simple heuristic: darkest circular region in central ROI
        h, w = frame_gray.shape
        cx_roi, cy_roi = w // 2, h // 2
        roi = frame_gray[max(0, cy_roi - 60):cy_roi + 60, max(0, cx_roi - 60):cx_roi + 60]
        if roi.size == 0:
            return None
        # invert to find darkest as bright blob
        roi_inv = 255 - roi
        yy, xx = np.unravel_index(np.argmax(roi_inv), roi_inv.shape)
        return (xx + cx_roi - 60, yy + cy_roi - 60, 8)

    def triangulate(self, p_left: Tuple[int, int], p_right: Tuple[int, int]) -> np.ndarray:
        """Stereo triangulation → 3D point in camera frame (mm).

        Reference: Hartley & Zisserman, Multiple View Geometry.
        Simplified linear triangulation here.
        """
        xl = np.array(p_left, dtype=np.float32)
        xr = np.array(p_right, dtype=np.float32)

        # Normalize
        xln = (xl - self.K1[:2, 2]) / np.array([self.K1[0, 0], self.K1[1, 1]])
        xrn = (xr - self.K2[:2, 2]) / np.array([self.K2[0, 0], self.K2[1, 1]])

        # Disparity
        d = xln[0] - xrn[0]
        if abs(d) < 1e-3:
            return np.array([0.0, 0.0, 500.0])  # fallback 500 mm
        Z = self.baseline * self.K1[0, 0] / d
        X = (xln[0] * Z) / self.K1[0, 0]
        Y = (xln[1] * Z) / self.K1[1, 1]
        return np.array([X, Y, Z])

    def gaze_vector(self, p3d: np.ndarray, cornea_center_3d: np.ndarray) -> np.ndarray:
        """Gaze direction = (pupil - cornea_center)."""
        g = p3d - cornea_center_3d
        norm = np.linalg.norm(g)
        return g / norm if norm > 1e-6 else g

    def process(self, left_gray: np.ndarray, right_gray: np.ndarray,
                cornea_3d: Optional[np.ndarray] = None) -> dict:
        """Full pipeline: detect + triangulate + gaze."""
        p_left  = self.detect_pupil(left_gray)
        p_right = self.detect_pupil(right_gray)
        if p_left is None or p_right is None:
            return {"ok": False, "reason": "pupil not found"}

        p3d = self.triangulate((p_left[0], p_left[1]), (p_right[0], p_right[1]))
        cornea = cornea_3d if cornea_3d is not None else np.array([0.0, 0.0, 50.0])
        g = self.gaze_vector(p3d, cornea)
        return {
            "ok": True,
            "pupil_left_px": (p_left[0], p_left[1]),
            "pupil_right_px": (p_right[0], p_right[1]),
            "pupil_3d_mm": p3d,
            "gaze_vector": g,
            "depth_mm": float(p3d[2]),
        }


@dataclass
class RobotArm3DOF:
    """Simple 3-DOF servo arm controller."""
    pan:  float = 0.0   # ±30°
    tilt: float = 0.0   # ±20°
    roll: float = 0.0   # ±10°
    limits: dict = None

    def __post_init__(self):
        self.limits = {"pan": (-30, 30), "tilt": (-20, 20), "roll": (-10, 10)}

    def clamp(self, v, lo, hi):
        return max(lo, min(hi, v))

    def move_to(self, pan: float, tilt: float, roll: float) -> None:
        self.pan  = self.clamp(pan,  *self.limits["pan"])
        self.tilt = self.clamp(tilt, *self.limits["tilt"])
        self.roll = self.clamp(roll, *self.limits["roll"])

    def recenter_face(self, gaze: np.ndarray, target_in_frame: bool = True) -> dict:
        """Adjust arm to keep face ROI centered based on gaze.

        If gaze points up → tilt down; right → pan left; etc.
        """
        # Heuristic proportional control
        pan_corr  = -5.0 * float(gaze[0])    # negative: gaze right → pan left
        tilt_corr = -5.0 * float(gaze[1])    # negative: gaze up → tilt down
        self.move_to(self.pan + pan_corr, self.tilt + tilt_corr, self.roll)
        return {"pan": self.pan, "tilt": self.tilt, "roll": self.roll}


if __name__ == "__main__":
    # Smoke test with synthetic frames
    rng = np.random.RandomState(123)
    left = (rng.rand(480, 640) * 255).astype(np.uint8)
    right = (rng.rand(480, 640) * 255).astype(np.uint8)

    tracker = StereoEyeTracker()
    out = tracker.process(left, right)
    print("Eye-tracking output:", {k: v for k, v in out.items() if k != "gaze_vector"})
    print("Gaze vector:", out.get("gaze_vector"))

    arm = RobotArm3DOF()
    if out["ok"]:
        arm.move_to(0, 0, 0)
        ctrls = arm.recenter_face(out["gaze_vector"])
        print("Arm controls:", ctrls)
