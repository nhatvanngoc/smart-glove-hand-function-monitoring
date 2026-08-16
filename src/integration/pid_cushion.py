"""
PID Cushion Controller — 64-cell independent PID loops
======================================================
Each cell (i, j) of the 8×8 cushion has independent PID control driven by
target pressure (from PTI risk map). Output: PWM duty for valve.

Anti-windup: clamping + back-calculation.
Safety: max 80 mmHg per cell.
"""
from __future__ import annotations
import numpy as np
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class PIDState:
    integral: float = 0.0
    last_error: float = 0.0
    last_pwm: float = 0.0


@dataclass
class PIDController:
    """64-cell array of independent PIDs."""
    kp: float = 1.0
    ki: float = 0.1
    kd: float = 0.05
    dt: float = 0.1               # 10 Hz
    max_pwm: float = 4095.0       # 12-bit
    max_cell_pressure: float = 80.0
    states: list = field(default_factory=list)

    def __post_init__(self):
        if not self.states:
            self.states = [[PIDState() for _ in range(8)] for _ in range(8)]

    def clamp(self, v, lo, hi):
        return max(lo, min(hi, v))

    def step_cell(self, i: int, j: int, current_p: float, setpoint: float) -> float:
        s = self.states[i][j]
        # Clamp setpoint for safety
        setpoint = self.clamp(setpoint, 0.0, self.max_cell_pressure)

        error = setpoint - current_p
        s.integral += error * self.dt

        # Anti-windup: clamp integral
        max_i = self.max_pwm / max(self.ki, 1e-6)
        s.integral = self.clamp(s.integral, -max_i, max_i)

        derivative = (error - s.last_error) / max(self.dt, 1e-6)
        out = self.kp * error + self.ki * s.integral + self.kd * derivative

        # Saturate
        out_sat = self.clamp(out, 0.0, self.max_pwm)

        # Back-calculation anti-windup
        s.integral += (out_sat - out) / max(self.ki, 1e-6) * 0.1

        s.last_error = error
        s.last_pwm   = out_sat
        return out_sat

    def step(self, current_pressure: np.ndarray, setpoint_map: np.ndarray) -> np.ndarray:
        """Step all 64 cells.

        current_pressure: (8, 8) mmHg
        setpoint_map:     (8, 8) mmHg (from PTI risk)
        returns: (8, 8) PWM duty (12-bit)
        """
        assert current_pressure.shape == (8, 8) and setpoint_map.shape == (8, 8)
        pwm = np.zeros((8, 8), dtype=np.float32)
        for i in range(8):
            for j in range(8):
                pwm[i, j] = self.step_cell(i, j, float(current_pressure[i, j]),
                                              float(setpoint_map[i, j]))
        return pwm


def risk_to_setpoint(risk_map: np.ndarray,
                      low_set: float = 25.0,
                      mod_set: float = 22.0,
                      high_set: float = 18.0,
                      crit_set: float = 15.0) -> np.ndarray:
    """Map risk levels to cushion pressure setpoints (deflate risky cells)."""
    sp = np.full_like(risk_map, low_set, dtype=np.float32)
    sp[risk_map == 1] = mod_set
    sp[risk_map == 2] = high_set
    sp[risk_map == 3] = crit_set
    return sp


if __name__ == "__main__":
    rng = np.random.RandomState(0)
    pid = PIDController()
    # Simulate 100 steps
    p = np.full((8, 8), 30.0, dtype=np.float32)
    risk = rng.randint(0, 4, size=(8, 8))
    sp = risk_to_setpoint(risk)
    print("Initial setpoint map:\n", sp)
    for step in range(50):
        pwm = pid.step(p, sp)
        # Simulate plant: pressure moves toward setpoint
        p = p + 0.1 * (sp - p) + rng.randn(8, 8) * 0.5
    print(f"\nAfter 50 steps:")
    print(f"Mean sacrum (rows 3..6, cols 3..6): {p[3:6, 3:6].mean():.2f} mmHg")
    print(f"Peak pressure: {p.max():.2f} mmHg")
    print(f"All cells < 80 mmHg? {(p < 80).all()}")
