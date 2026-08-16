"""
Velostat + copper tape pressure sensor simulation.

Purpose
-------
Simulate one pressure-sensing layer for the adaptive air cushion:
    pressure map -> Velostat resistance -> voltage divider ADC -> reconstructed pressure -> heatmap

Default layout:
    rows = 9 along body length, cols = 5 across body width  (5 x 9 cushion)

Run:
    python3 simulation/velostat_heatmap_sim.py

Outputs:
    outputs/figures/velostat_pressure_heatmap_sim.png
    outputs/figures/velostat_sensor_curve.png
    outputs/reports/velostat_true_pressure.csv
    outputs/reports/velostat_adc_counts.csv
    outputs/reports/velostat_reconstructed_pressure.csv
"""
from __future__ import annotations

from pathlib import Path
import argparse
import numpy as np
import matplotlib.pyplot as plt

try:
    from scipy.ndimage import zoom
except Exception:  # pragma: no cover
    zoom = None


# -----------------------------
# Sensor/electronics parameters
# -----------------------------
VCC = 3.3
ADC_BITS = 12
ADC_MAX = (2 ** ADC_BITS) - 1
R_FIXED_OHM = 47_000.0  # voltage divider fixed resistor

# Empirical Velostat model. Must be replaced by calibration values later.
# R(P) = R_min + (R_max - R_min) / (1 + (P/P50)^gamma)
R_MAX_OHM = 900_000.0   # near no load
R_MIN_OHM = 4_000.0     # high pressure saturation
P50_MMHG = 32.0         # pressure at mid transition
GAMMA = 1.45            # curve steepness


# -----------------------------
# Pressure map model
# -----------------------------
def gaussian_2d(rows: int, cols: int, r0: float, c0: float, amp: float, sr: float, sc: float) -> np.ndarray:
    rr, cc = np.mgrid[0:rows, 0:cols]
    return amp * np.exp(-(((rr - r0) ** 2) / (2 * sr ** 2) + ((cc - c0) ** 2) / (2 * sc ** 2)))


def make_supine_pressure_map(rows: int = 9, cols: int = 5, seed: int = 7) -> np.ndarray:
    """Create an example mmHg pressure map for a person lying supine.

    Row meaning for 9 rows:
        0-1 shoulder/scapula, 2-3 back, 4-5 sacrum/buttock, 6-8 upper thigh.
    Column meaning for 5 cols:
        left side -> center -> right side.
    """
    rng = np.random.default_rng(seed)
    p = np.full((rows, cols), 12.0, dtype=float)  # base soft contact

    center = (cols - 1) / 2
    # shoulder blades: two moderate hotspots
    p += gaussian_2d(rows, cols, 1.1, center - 1.0, 17, 0.75, 0.55)
    p += gaussian_2d(rows, cols, 1.1, center + 1.0, 17, 0.75, 0.55)
    # lumbar/back contact
    p += gaussian_2d(rows, cols, 3.0, center, 10, 1.0, 1.2)
    # sacrum / buttock high-risk zone
    p += gaussian_2d(rows, cols, 5.1, center, 42, 0.85, 0.9)
    # upper thighs
    p += gaussian_2d(rows, cols, 7.2, center - 0.85, 20, 0.9, 0.55)
    p += gaussian_2d(rows, cols, 7.2, center + 0.85, 20, 0.9, 0.55)

    p += rng.normal(0, 1.3, size=(rows, cols))
    return np.clip(p, 0, 90)


# -----------------------------
# Electrode geometry approximation
# -----------------------------
def electrode_resistance_scale(
    mode: str,
    patch_mm: float = 50.0,
    finger_gap_mm: float = 2.0,
    finger_length_mm: float = 34.0,
    n_gaps: int = 8,
) -> float:
    """Return a simple scale factor for resistance caused by electrode geometry.

    This is not FEA. It is a first-order approximation:
    - Sandwich: R ~ rho*t/A. Bigger patch area -> lower resistance.
    - Interdigitated: conductance ~ n_gaps*finger_length/gap.

    scale > 1 means larger measured resistance.
    """
    mode = mode.lower().strip()
    if mode == "sandwich":
        ref_area = 50.0 * 50.0
        area = patch_mm * patch_mm
        return ref_area / max(area, 1e-9)
    if mode in {"interdigitated", "comb", "rang_luoc"}:
        ref_conductance = 8 * 34.0 / 2.0
        conductance = max(n_gaps * finger_length_mm / max(finger_gap_mm, 1e-9), 1e-9)
        return ref_conductance / conductance
    raise ValueError(f"Unknown electrode mode: {mode}")


# -----------------------------
# Velostat + ADC model
# -----------------------------
def pressure_to_resistance(pressure_mmhg: np.ndarray, r_scale: float = 1.0) -> np.ndarray:
    p = np.maximum(pressure_mmhg, 0.0)
    r = R_MIN_OHM + (R_MAX_OHM - R_MIN_OHM) / (1.0 + (p / P50_MMHG) ** GAMMA)
    return r * r_scale


def resistance_to_adc(r_sensor_ohm: np.ndarray, noise_counts: float = 5.0, seed: int = 3) -> np.ndarray:
    """Voltage divider: VCC -> R_sensor -> ADC node -> R_FIXED -> GND.

    Pressure up -> R_sensor down -> Vout up -> ADC count up.
    """
    rng = np.random.default_rng(seed)
    vout = VCC * R_FIXED_OHM / (r_sensor_ohm + R_FIXED_OHM)
    adc = vout / VCC * ADC_MAX
    adc += rng.normal(0, noise_counts, size=adc.shape)
    return np.clip(np.rint(adc), 0, ADC_MAX).astype(int)


def adc_to_resistance(adc_counts: np.ndarray) -> np.ndarray:
    adc = np.clip(adc_counts.astype(float), 1, ADC_MAX - 1)
    vout = adc / ADC_MAX * VCC
    return R_FIXED_OHM * (VCC / vout - 1.0)


def resistance_to_pressure(r_sensor_ohm: np.ndarray, r_scale: float = 1.0) -> np.ndarray:
    r = np.maximum(r_sensor_ohm / r_scale, R_MIN_OHM + 1.0)
    ratio = (r - R_MIN_OHM) / (R_MAX_OHM - R_MIN_OHM)
    ratio = np.clip(ratio, 1e-6, 0.999999)
    p = P50_MMHG * ((1.0 / ratio) - 1.0) ** (1.0 / GAMMA)
    return np.clip(p, 0, 150)


def add_soft_mechanical_crosstalk(pressure: np.ndarray, strength: float = 0.08) -> np.ndarray:
    """Simple nearest-neighbor blur to mimic fabric/silicone spreading.

    Keep strength small. In real hardware, this must be identified experimentally.
    """
    p = pressure.copy()
    up = np.vstack([p[0:1, :], p[:-1, :]])
    down = np.vstack([p[1:, :], p[-1:, :]])
    left = np.hstack([p[:, 0:1], p[:, :-1]])
    right = np.hstack([p[:, 1:], p[:, -1:]])
    return (1 - 4 * strength) * p + strength * (up + down + left + right)


# -----------------------------
# Plot/output helpers
# -----------------------------
def smooth_for_display(arr: np.ndarray, factor: int = 14) -> np.ndarray:
    if zoom is None:
        return arr
    return zoom(arr, factor, order=3)


def save_matrix_csv(path: Path, arr: np.ndarray, fmt: str = "%.3f") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    np.savetxt(path, arr, delimiter=",", fmt=fmt)


def plot_heatmaps(true_p: np.ndarray, adc: np.ndarray, rec_p: np.ndarray, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 3, figsize=(14, 5), constrained_layout=True)

    panels = [
        (true_p, "Ap suat that mo phong\nmmHg", "inferno", 0, 80),
        (adc.astype(float), "Gia tri ADC doc duoc\n12-bit counts", "viridis", 0, ADC_MAX),
        (rec_p, "Ap suat tai tao tu ADC\nmmHg", "inferno", 0, 80),
    ]

    for ax, (data, title, cmap, vmin, vmax) in zip(axes, panels):
        img = smooth_for_display(data)
        im = ax.imshow(img, cmap=cmap, vmin=vmin, vmax=vmax, origin="upper", aspect="auto")
        ax.set_title(title, fontsize=12)
        ax.set_xlabel("Ngang than nguoi: trai -> phai")
        ax.set_ylabel("Doc than nguoi: vai -> dui")
        ax.set_xticks([])
        ax.set_yticks([])
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

        # Overlay original cell grid
        rows, cols = data.shape
        h, w = img.shape
        for r in range(1, rows):
            ax.axhline(r * h / rows - 0.5, color="white", lw=0.45, alpha=0.65)
        for c in range(1, cols):
            ax.axvline(c * w / cols - 0.5, color="white", lw=0.45, alpha=0.65)

    fig.suptitle("Mo phong Velostat + copper tape tren ma tran 5 x 9", fontsize=15)
    fig.savefig(out_path, dpi=180)
    plt.close(fig)


def plot_sensor_curve(out_path: Path, r_scale: float) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    p = np.linspace(0, 100, 300)
    r = pressure_to_resistance(p, r_scale=r_scale)
    adc = resistance_to_adc(r, noise_counts=0)

    fig, ax1 = plt.subplots(figsize=(8, 4.8), constrained_layout=True)
    ax1.plot(p, r / 1000.0, color="#1565C0", lw=2)
    ax1.set_xlabel("Ap suat (mmHg)")
    ax1.set_ylabel("Dien tro Velostat (kOhm)", color="#1565C0")
    ax1.tick_params(axis="y", labelcolor="#1565C0")
    ax1.grid(True, alpha=0.25)

    ax2 = ax1.twinx()
    ax2.plot(p, adc, color="#D32F2F", lw=2)
    ax2.set_ylabel("ADC 12-bit count", color="#D32F2F")
    ax2.tick_params(axis="y", labelcolor="#D32F2F")

    ax1.set_title("Duong dac tinh mo phong: ap suat -> dien tro -> ADC")
    fig.savefig(out_path, dpi=180)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", type=int, default=9, help="Rows along body length")
    parser.add_argument("--cols", type=int, default=5, help="Columns across body width")
    parser.add_argument("--electrode", default="sandwich", choices=["sandwich", "interdigitated", "comb", "rang_luoc"])
    parser.add_argument("--patch-mm", type=float, default=50.0)
    parser.add_argument("--noise", type=float, default=5.0, help="ADC noise in counts")
    parser.add_argument("--crosstalk", type=float, default=0.08, help="Mechanical crosstalk 0..0.15 recommended")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    figures = root / "outputs" / "figures"
    reports = root / "outputs" / "reports"

    r_scale = electrode_resistance_scale(args.electrode, patch_mm=args.patch_mm)

    true_pressure = make_supine_pressure_map(args.rows, args.cols)
    sensed_pressure = add_soft_mechanical_crosstalk(true_pressure, strength=args.crosstalk)
    r_sensor = pressure_to_resistance(sensed_pressure, r_scale=r_scale)
    adc = resistance_to_adc(r_sensor, noise_counts=args.noise)
    rec_r = adc_to_resistance(adc)
    rec_pressure = resistance_to_pressure(rec_r, r_scale=r_scale)

    save_matrix_csv(reports / "velostat_true_pressure.csv", true_pressure)
    save_matrix_csv(reports / "velostat_adc_counts.csv", adc, fmt="%d")
    save_matrix_csv(reports / "velostat_reconstructed_pressure.csv", rec_pressure)

    plot_heatmaps(true_pressure, adc, rec_pressure, figures / "velostat_pressure_heatmap_sim.png")
    plot_sensor_curve(figures / "velostat_sensor_curve.png", r_scale=r_scale)

    err = rec_pressure - true_pressure
    print("Velostat heatmap simulation complete")
    print(f"  layout: {args.cols} x {args.rows} cells (cols x rows)")
    print(f"  electrode: {args.electrode}, patch={args.patch_mm:.1f} mm, r_scale={r_scale:.3f}")
    print(f"  true pressure range: {true_pressure.min():.1f}..{true_pressure.max():.1f} mmHg")
    print(f"  adc range: {adc.min()}..{adc.max()} counts")
    print(f"  reconstruction MAE: {np.mean(np.abs(err)):.2f} mmHg")
    print(f"  saved: {figures / 'velostat_pressure_heatmap_sim.png'}")
    print(f"  saved: {figures / 'velostat_sensor_curve.png'}")


if __name__ == "__main__":
    main()
