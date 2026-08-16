"""
Jetson Pipeline Orchestrator — End-to-End Integration
=====================================================
Mô phỏng end-to-end pipeline: sensor → AI → control → UI.

Trong production: ROS2 nodes thay cho trực tiếp gọi function.
Ở đây: cùng API surface, dễ test, không cần hardware.

Theo ARS Stage 2 design.
"""
from __future__ import annotations
import os
import sys
import time
import logging
from dataclasses import dataclass, field
from typing import Optional, Dict, Any

# Ensure src/ is importable when run as a script
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import numpy as np

from src.pressure_model.pti_engine import compute_pti, classify_risk, risk_map_for_dashboard
from src.pressure_model.cross_calibration import HybridCalibrator
from src.pressure_model.cnn_lstm import CNNLSTM
from src.aac_assistant.qwen_lora import AACAssistant
from src.aac_assistant.aac_grid import AACGrid
from src.eye_tracking.eye_tracker import StereoEyeTracker, RobotArm3DOF
from src.integration.pid_cushion import PIDController, risk_to_setpoint
from src.integration.self_improve import SelfImprovingLoop

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
log = logging.getLogger("aac_cushion")


@dataclass
class SystemState:
    timestep: int = 0
    pressure_history: list = field(default_factory=list)
    posture: int = 0
    safety_ok: bool = True
    last_aac_sentence: str = ""


class Orchestrator:
    """One-shot main loop tick.

    Real-world: called from ROS2 timer @ 10 Hz.
    """
    def __init__(self,
                 use_llm: bool = False,
                 use_lstm: bool = True,
                 seed: int = 42):
        self.calibrator = HybridCalibrator()
        self.pid        = PIDController()
        self.cnn_lstm   = CNNLSTM(seed=seed) if use_lstm else None
        self.aac        = AACAssistant(use_llm=use_llm)
        self.grid       = AACGrid()
        self.eye        = StereoEyeTracker()
        self.arm        = RobotArm3DOF()
        self.loop       = SelfImprovingLoop()
        self.state      = SystemState()

    def tick_sensor(self, v_raw: np.ndarray, p_pz: np.ndarray) -> np.ndarray:
        """Calibrate Velostat + piezocap → pressure map."""
        return self.calibrator.calibrate(v_raw, p_pz)

    def tick_perception(self, p_map: np.ndarray) -> dict:
        """Update PTI, classify risk, run CNN-LSTM forecast."""
        history_arr = np.stack(self.state.pressure_history + [p_map], axis=0) if self.state.pressure_history else p_map[None]
        out = risk_map_for_dashboard(history_arr, self.state.posture)
        forecast = None
        if self.cnn_lstm is not None and len(self.state.pressure_history) >= 60:
            frames = np.stack(self.state.pressure_history[-60:], axis=0)
            ch0 = frames / 80.0
            pti_now = compute_pti(frames, self.state.posture)
            ch1 = (pti_now >= 2.0).astype(np.float32)
            ch1 = np.broadcast_to(ch1[None], frames.shape).copy()
            ch2 = np.full_like(frames, self.state.posture / 2.0)
            frames_3 = np.stack([ch0, ch1, ch2], axis=-1)
            forecast = self.cnn_lstm.forward(frames_3)
        return {**out, "forecast_risk": forecast}

    def tick_control(self, p_map: np.ndarray, risk: np.ndarray) -> np.ndarray:
        """Compute PWM for 64 valves."""
        setpoint = risk_to_setpoint(risk)
        return self.pid.step(p_map, setpoint)

    def tick_aac(self, gaze_xy: Optional[tuple] = None, dt_ms: int = 33) -> Optional[str]:
        if gaze_xy is None:
            return None
        sel = self.grid.update(gaze_xy, dt_ms)
        if sel:
            kws = self.grid.get_keywords()
            self.grid.reset()
            sentence = self.aac.generate(kws)
            self.state.last_aac_sentence = sentence
            log.info(f"AAC: keywords={kws} -> {sentence!r}")
            return sentence
        return None

    def tick_arm(self, gaze_3d: Optional[np.ndarray] = None) -> Optional[dict]:
        if gaze_3d is None:
            return None
        return self.arm.recenter_face(gaze_3d)

    def tick_self_improve(self, p_map: np.ndarray, comfort: float = 4.0) -> dict:
        peak = float(p_map.max())
        tot  = float((p_map > 32).mean())
        aac_succ = 1.0 if self.state.last_aac_sentence else 0.5
        return self.loop.step(peak, tot, aac_succ, comfort)

    def step(self,
             v_raw: np.ndarray,
             p_pz: np.ndarray,
             gaze_xy: Optional[tuple] = None,
             comfort: float = 4.0) -> Dict[str, Any]:
        p_map = self.tick_sensor(v_raw, p_pz)
        self.state.pressure_history.append(p_map)
        if len(self.state.pressure_history) > 600:
            self.state.pressure_history.pop(0)

        perc = self.tick_perception(p_map)
        pwm  = self.tick_control(p_map, perc["risk"])
        aac_out = self.tick_aac(gaze_xy)
        si   = self.tick_self_improve(p_map, comfort)

        self.state.safety_ok = (p_map.max() < 80.0)
        if not self.state.safety_ok:
            log.warning(f"Safety violation: peak {p_map.max():.1f} mmHg >= 80")

        self.state.timestep += 1
        return {
            "t": self.state.timestep,
            "peak_mmHg": perc["peak_mmHg"],
            "mean_sacrum_mmHg": perc["mean_sacrum_mmHg"],
            "tot_pct": perc["time_over_threshold_pct"],
            "forecast_risk": perc["forecast_risk"],
            "aac_sentence": self.state.last_aac_sentence,
            "self_improve_reward": si["reward"],
            "pid_gain_delta": si["pid_gain_delta"],
            "safety_ok": self.state.safety_ok,
        }


if __name__ == "__main__":
    rng = np.random.RandomState(0)
    orch = Orchestrator(use_llm=False, use_lstm=True, seed=42)

    log.info("=== Running 60-step simulation ===")
    for t in range(60):
        # Simulate realistic Velostat ADC + Piezocap mmHg
        # v_raw: ADC 0-255 (corresponds to ~0-100 mmHg via V = a*P + b)
        # We use: V = 2.0 * P + 20 + noise  (so P = (V - 20) / 2.0)
        true_p = np.clip(20 + rng.rand(64) * 20, 0, 80)  # realistic 20-40 mmHg
        v_raw  = (2.0 * true_p + 20 + rng.randn(64) * 1.0).clip(0, 255).astype(np.float32)
        p_pz   = np.array([true_p[c] for c in orch.calibrator.anchor_cells]) + rng.randn(8) * 0.5

        # Simulate gaze on cell (2, 0) = "Nước" every 30 ticks
        gaze = (50 + 0 * 100, 50 + 2 * 100) if (t % 30 == 10) else None

        out = orch.step(v_raw, p_pz, gaze_xy=gaze, comfort=4.0)
        if t % 10 == 0 or out["aac_sentence"]:
            log.info(f"t={out['t']:3d}  peak={out['peak_mmHg']:.1f}  "
                     f"sacrum={out['mean_sacrum_mmHg']:.1f}  "
                     f"forecast={out['forecast_risk']}  "
                     f"reward={out['self_improve_reward']:.2f}  "
                     f"sentence={out['aac_sentence']!r}  "
                     f"safety={out['safety_ok']}")
