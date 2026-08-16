"""
Test: Lateral scenario — 70 kg mannequin nằm nghiêng.

Hotspot chuyển từ sacrum → trochanter (hông).
"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import numpy as np

from simulation.plugins.cushion_dynamics_simulator import CushionDynamics


def run_test(duration_s: float = 60.0):
    cushion = CushionDynamics(tau=0.3, dt=0.1)

    print(f"\nSimulating {duration_s:.0f}s LATERAL position (70 kg)...")
    history_p = []
    t = 0.0
    while t < duration_s:
        buildup = t / duration_s

        # Setpoint (lateral: trochanter zone reduced)
        sp = np.full((8, 8), 28.0, dtype=np.float32)
        sp[3:5, 2:4] = 15.0 - buildup * 5   # trochanter (lateral)
        sp[7, :] = 18.0                       # heels

        cushion.step(sp)
        if t > 5.0:
            cushion.add_disturbance(sacrum_pressure=40.0 + buildup * 15)

        history_p.append(cushion.get_pressure().copy())
        if int(t) % 10 == 0:
            print(f"t={t:5.1f}s | peak={cushion.p.max():.1f} | "
                  f"trochanter mean={cushion.p[3:5, 2:4].mean():.1f} mmHg")
        t += cushion.dt

    history_p = np.stack(history_p, axis=0)
    troch = history_p[:, 3:5, 2:4].mean(axis=(1, 2))
    peak = history_p.max(axis=(1, 2))

    steady = slice(int(10 / cushion.dt), None)
    troch_steady = float(troch[steady].mean())
    peak_steady = float(peak[steady].mean())

    print("\n" + "=" * 60)
    print("TEST RESULTS — Lateral")
    print("=" * 60)
    print(f"Trochanter steady:    {troch_steady:.2f} mmHg")
    print(f"Peak steady:          {peak_steady:.2f} mmHg")
    print()
    print(f"Acceptance (troch < 32 mmHg): {'PASS' if troch_steady < 32 else 'FAIL'}")

    return {
        "trochanter_steady": troch_steady,
        "peak_steady": peak_steady,
        "final_pressure": history_p[-1],
    }


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--duration", type=float, default=60.0)
    args = parser.parse_args()
    run_test(args.duration)
