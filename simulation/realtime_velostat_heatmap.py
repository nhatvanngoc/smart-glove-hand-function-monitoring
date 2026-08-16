"""
Realtime Velostat heatmap simulator for the final 5x9 cushion.

What it simulates
-----------------
body pressure -> Velostat resistance -> voltage divider ADC -> reconstructed pressure -> heatmap

This is intentionally NOT a Gazebo/URDF simulation. It is a realtime sensor/control
simulation that is much more useful for the current Velostat + copper tape layer.

Run on your PC:
    cd adaptive_cushion_aac
    python simulation/realtime_velostat_heatmap.py

Optional modes:
    python simulation/realtime_velostat_heatmap.py --mode supine
    python simulation/realtime_velostat_heatmap.py --mode lateral_left
    python simulation/realtime_velostat_heatmap.py --mode breathing
    python simulation/realtime_velostat_heatmap.py --fps 15

Optional serial input from STM32/Arduino later:
    python simulation/realtime_velostat_heatmap.py --serial COM5 --baud 115200

Serial line format expected later:
    45 comma-separated ADC values per line
Example:
    315,320,318,... total 45 values

Dependencies:
    numpy, matplotlib
Optional:
    pyserial, only if using --serial
"""
from __future__ import annotations

import argparse
import math
import time
from collections import deque
from dataclasses import dataclass
from typing import Optional

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

try:
    import serial  # type: ignore
except Exception:  # pyserial optional
    serial = None


ROWS = 9
COLS = 5
N = ROWS * COLS

VCC = 3.3
ADC_BITS = 12
ADC_MAX = (2 ** ADC_BITS) - 1
R_FIXED_OHM = 47_000.0

# Placeholder calibration. Replace after real weight tests.
R_MAX_OHM = 900_000.0
R_MIN_OHM = 4_000.0
P50_MMHG = 32.0
GAMMA = 1.45


@dataclass
class RealtimeState:
    frame_idx: int = 0
    last_adc: Optional[np.ndarray] = None
    last_pressure: Optional[np.ndarray] = None
    max_hist: deque = None  # type: ignore
    mean_hist: deque = None  # type: ignore

    def __post_init__(self):
        self.max_hist = deque(maxlen=240)
        self.mean_hist = deque(maxlen=240)


def gaussian_2d(rows: int, cols: int, r0: float, c0: float, amp: float, sr: float, sc: float) -> np.ndarray:
    rr, cc = np.mgrid[0:rows, 0:cols]
    return amp * np.exp(-(((rr - r0) ** 2) / (2 * sr ** 2) + ((cc - c0) ** 2) / (2 * sc ** 2)))


def pressure_pattern(mode: str, t: float) -> np.ndarray:
    """Realtime synthetic body pressure pattern, mmHg."""
    p = np.full((ROWS, COLS), 10.0, dtype=float)
    center = (COLS - 1) / 2

    # slow respiration / small body motion
    breath = 1.0 + 0.08 * math.sin(2 * math.pi * 0.25 * t)
    drift = 0.4 * math.sin(2 * math.pi * 0.04 * t)

    if mode == "supine":
        # shoulder blades
        p += gaussian_2d(ROWS, COLS, 1.1, center - 1.0, 15 * breath, 0.75, 0.55)
        p += gaussian_2d(ROWS, COLS, 1.1, center + 1.0, 15 * breath, 0.75, 0.55)
        # back
        p += gaussian_2d(ROWS, COLS, 3.1, center + drift, 10, 1.0, 1.15)
        # sacrum/buttock high risk
        p += gaussian_2d(ROWS, COLS, 5.1, center + 0.2 * drift, 45 * breath, 0.85, 0.9)
        # upper thighs
        p += gaussian_2d(ROWS, COLS, 7.2, center - 0.85, 19, 0.9, 0.55)
        p += gaussian_2d(ROWS, COLS, 7.2, center + 0.85, 19, 0.9, 0.55)

    elif mode == "lateral_left":
        # body rolled left: pressure shifts to left columns
        p += gaussian_2d(ROWS, COLS, 1.3, 1.0, 20 * breath, 0.9, 0.65)
        p += gaussian_2d(ROWS, COLS, 3.4, 1.0, 16, 1.0, 0.7)
        p += gaussian_2d(ROWS, COLS, 5.3, 1.0, 52 * breath, 0.9, 0.65)
        p += gaussian_2d(ROWS, COLS, 7.1, 1.1, 26, 1.1, 0.65)

    elif mode == "lateral_right":
        p += gaussian_2d(ROWS, COLS, 1.3, 3.0, 20 * breath, 0.9, 0.65)
        p += gaussian_2d(ROWS, COLS, 3.4, 3.0, 16, 1.0, 0.7)
        p += gaussian_2d(ROWS, COLS, 5.3, 3.0, 52 * breath, 0.9, 0.65)
        p += gaussian_2d(ROWS, COLS, 7.1, 2.9, 26, 1.1, 0.65)

    elif mode == "breathing":
        # same as supine but more dynamic; useful for demo
        dynamic = 1.0 + 0.18 * math.sin(2 * math.pi * 0.22 * t)
        p += gaussian_2d(ROWS, COLS, 1.1, center - 1.0, 15 * dynamic, 0.75, 0.55)
        p += gaussian_2d(ROWS, COLS, 1.1, center + 1.0, 15 * dynamic, 0.75, 0.55)
        p += gaussian_2d(ROWS, COLS, 5.1, center + 0.15 * math.sin(t), 45 * dynamic, 0.85, 0.9)
        p += gaussian_2d(ROWS, COLS, 7.2, center, 21 * (2 - dynamic), 1.1, 1.2)

    elif mode == "cycle":
        period = 18.0
        phase = (t % period) / period
        if phase < 1 / 3:
            return pressure_pattern("supine", t)
        if phase < 2 / 3:
            return pressure_pattern("lateral_left", t)
        return pressure_pattern("lateral_right", t)

    else:
        raise ValueError(f"Unknown mode: {mode}")

    # deterministic small texture/noise
    rng = np.random.default_rng(int(t * 30) % 10_000)
    p += rng.normal(0, 0.7, size=(ROWS, COLS))
    return np.clip(p, 0, 90)


def mechanical_crosstalk(pressure: np.ndarray, strength: float = 0.08) -> np.ndarray:
    p = pressure.copy()
    up = np.vstack([p[0:1, :], p[:-1, :]])
    down = np.vstack([p[1:, :], p[-1:, :]])
    left = np.hstack([p[:, 0:1], p[:, :-1]])
    right = np.hstack([p[:, 1:], p[:, -1:]])
    return (1 - 4 * strength) * p + strength * (up + down + left + right)


def pressure_to_resistance(pressure_mmhg: np.ndarray) -> np.ndarray:
    p = np.maximum(pressure_mmhg, 0.0)
    return R_MIN_OHM + (R_MAX_OHM - R_MIN_OHM) / (1.0 + (p / P50_MMHG) ** GAMMA)


def resistance_to_adc(r_sensor_ohm: np.ndarray, noise_counts: float = 4.0) -> np.ndarray:
    vout = VCC * R_FIXED_OHM / (r_sensor_ohm + R_FIXED_OHM)
    adc = vout / VCC * ADC_MAX
    adc += np.random.normal(0, noise_counts, size=adc.shape)
    return np.clip(np.rint(adc), 0, ADC_MAX).astype(int)


def adc_to_resistance(adc_counts: np.ndarray) -> np.ndarray:
    adc = np.clip(adc_counts.astype(float), 1, ADC_MAX - 1)
    vout = adc / ADC_MAX * VCC
    return R_FIXED_OHM * (VCC / vout - 1.0)


def resistance_to_pressure(r_sensor_ohm: np.ndarray) -> np.ndarray:
    r = np.maximum(r_sensor_ohm, R_MIN_OHM + 1.0)
    ratio = (r - R_MIN_OHM) / (R_MAX_OHM - R_MIN_OHM)
    ratio = np.clip(ratio, 1e-6, 0.999999)
    p = P50_MMHG * ((1.0 / ratio) - 1.0) ** (1.0 / GAMMA)
    return np.clip(p, 0, 150)


def simulate_adc_frame(mode: str, t: float) -> tuple[np.ndarray, np.ndarray]:
    true_p = pressure_pattern(mode, t)
    sensed_p = mechanical_crosstalk(true_p, strength=0.08)
    r = pressure_to_resistance(sensed_p)
    adc = resistance_to_adc(r)
    return adc, true_p


def parse_serial_line(line: str) -> Optional[np.ndarray]:
    parts = line.strip().replace(";", ",").split(",")
    if len(parts) != N:
        return None
    try:
        values = np.array([int(float(x)) for x in parts], dtype=int)
    except ValueError:
        return None
    return np.clip(values.reshape(ROWS, COLS), 0, ADC_MAX)


def open_serial(port: Optional[str], baud: int):
    if port is None:
        return None
    if serial is None:
        raise RuntimeError("pyserial is not installed. Install with: pip install pyserial")
    return serial.Serial(port, baudrate=baud, timeout=0.001)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="cycle", choices=["supine", "lateral_left", "lateral_right", "breathing", "cycle"])
    parser.add_argument("--fps", type=float, default=12.0)
    parser.add_argument("--serial", default=None, help="Serial port, e.g. COM5 or /dev/ttyUSB0")
    parser.add_argument("--baud", type=int, default=115200)
    parser.add_argument("--threshold", type=float, default=32.0, help="risk threshold in mmHg")
    args = parser.parse_args()

    ser = open_serial(args.serial, args.baud)
    state = RealtimeState()
    start = time.time()

    fig = plt.figure(figsize=(12, 6))
    gs = fig.add_gridspec(2, 3, height_ratios=[5, 1.4])
    ax_heat = fig.add_subplot(gs[0, 0])
    ax_adc = fig.add_subplot(gs[0, 1])
    ax_risk = fig.add_subplot(gs[0, 2])
    ax_hist = fig.add_subplot(gs[1, :])

    p0 = np.zeros((ROWS, COLS))
    adc0 = np.zeros((ROWS, COLS))
    im_heat = ax_heat.imshow(p0, cmap="inferno", vmin=0, vmax=80, origin="upper", aspect="auto")
    im_adc = ax_adc.imshow(adc0, cmap="viridis", vmin=0, vmax=ADC_MAX, origin="upper", aspect="auto")
    im_risk = ax_risk.imshow(p0 > args.threshold, cmap="Reds", vmin=0, vmax=1, origin="upper", aspect="auto")

    for ax, title in [
        (ax_heat, "Reconstructed pressure, mmHg"),
        (ax_adc, "Raw ADC, 12-bit"),
        (ax_risk, f"Risk mask > {args.threshold:.0f} mmHg"),
    ]:
        ax.set_title(title)
        ax.set_xticks(range(COLS))
        ax.set_yticks(range(ROWS))
        ax.set_xlabel("5 columns: left -> right")
        ax.set_ylabel("9 rows: shoulder -> thigh")
        ax.set_xticklabels([str(i + 1) for i in range(COLS)])
        ax.set_yticklabels([str(i + 1) for i in range(ROWS)])
        for r in range(1, ROWS):
            ax.axhline(r - 0.5, color="white", lw=0.5, alpha=0.55)
        for c in range(1, COLS):
            ax.axvline(c - 0.5, color="white", lw=0.5, alpha=0.55)

    cb1 = fig.colorbar(im_heat, ax=ax_heat, fraction=0.046, pad=0.04)
    cb1.set_label("mmHg")
    cb2 = fig.colorbar(im_adc, ax=ax_adc, fraction=0.046, pad=0.04)
    cb2.set_label("ADC count")

    line_max, = ax_hist.plot([], [], color="#D32F2F", lw=2, label="max pressure")
    line_mean, = ax_hist.plot([], [], color="#1976D2", lw=2, label="mean pressure")
    ax_hist.axhline(args.threshold, color="#F9A825", lw=1.5, ls="--", label="risk threshold")
    ax_hist.set_ylim(0, 90)
    ax_hist.set_xlim(0, 240)
    ax_hist.set_ylabel("mmHg")
    ax_hist.set_xlabel("recent frames")
    ax_hist.grid(True, alpha=0.25)
    ax_hist.legend(loc="upper right")

    txt = fig.text(0.01, 0.97, "", ha="left", va="top", fontsize=10)

    def read_adc_frame(t: float) -> tuple[np.ndarray, Optional[np.ndarray], str]:
        if ser is not None:
            # Read latest complete line available. If malformed, keep sim fallback.
            latest = None
            for _ in range(20):
                raw = ser.readline()
                if not raw:
                    break
                try:
                    line = raw.decode("utf-8", errors="ignore")
                except Exception:
                    continue
                parsed = parse_serial_line(line)
                if parsed is not None:
                    latest = parsed
            if latest is not None:
                return latest, None, f"serial {args.serial}"
        adc, true_p = simulate_adc_frame(args.mode, t)
        return adc, true_p, f"simulation mode={args.mode}"

    def update(_frame):
        t = time.time() - start
        adc, true_p, source = read_adc_frame(t)
        rec_p = resistance_to_pressure(adc_to_resistance(adc))
        state.last_adc = adc
        state.last_pressure = rec_p
        state.max_hist.append(float(np.max(rec_p)))
        state.mean_hist.append(float(np.mean(rec_p)))
        state.frame_idx += 1

        im_heat.set_data(rec_p)
        im_adc.set_data(adc)
        im_risk.set_data((rec_p > args.threshold).astype(float))

        xs = np.arange(len(state.max_hist))
        line_max.set_data(xs, list(state.max_hist))
        line_mean.set_data(xs, list(state.mean_hist))
        ax_hist.set_xlim(0, max(240, len(xs)))

        risk_cells = int(np.sum(rec_p > args.threshold))
        txt.set_text(
            f"5x9 Velostat realtime heatmap | source: {source}\n"
            f"frame={state.frame_idx} | max={np.max(rec_p):.1f} mmHg | "
            f"mean={np.mean(rec_p):.1f} mmHg | risk cells={risk_cells}/{N}"
        )
        return im_heat, im_adc, im_risk, line_max, line_mean, txt

    fig.suptitle("Realtime Velostat + copper tape pressure heatmap, final 5 x 9 matrix", fontsize=13)
    interval_ms = max(1, int(1000 / args.fps))
    ani = FuncAnimation(fig, update, interval=interval_ms, blit=False)
    plt.tight_layout(rect=[0, 0, 1, 0.93])
    plt.show()


if __name__ == "__main__":
    main()
