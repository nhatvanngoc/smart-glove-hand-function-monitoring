"""
Post-process SOFA single Velostat patch output.

GUI-scene output:
    python simulation/sofa/postprocess_single_patch.py

Batch-scene output:
    python simulation/sofa/postprocess_single_patch.py --batch

Outputs PNG response plots in simulation/sofa/outputs/.
"""
from __future__ import annotations

from pathlib import Path
import argparse
import csv

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "simulation" / "sofa" / "outputs"


def read_csv(path: Path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append({k: float(v) for k, v in row.items()})
    return rows


def plot_response(csv_path: Path, png_path: Path, title_suffix: str = ""):
    if not csv_path.exists():
        raise FileNotFoundError(f"Missing SOFA output CSV: {csv_path}")

    data = read_csv(csv_path)
    if not data:
        raise RuntimeError("CSV exists but has no data rows")

    t = [r["time_s"] for r in data]
    p = [r["pressure_mmHg"] for r in data]
    force = [r["applied_force_N"] for r in data]
    adc = [r["ADC12_placeholder"] for r in data]
    rz = [r["mean_z_mm"] for r in data]

    fig, axes = plt.subplots(4, 1, figsize=(9, 9), sharex=True, constrained_layout=True)

    axes[0].plot(t, force, color="#455A64", lw=2)
    axes[0].set_ylabel("Force (N)")
    axes[0].grid(True, alpha=0.25)

    axes[1].plot(t, p, color="#D32F2F", lw=2)
    axes[1].axhline(32, color="#F9A825", ls="--", lw=1.3, label="32 mmHg reference")
    axes[1].set_ylabel("Pressure (mmHg)")
    axes[1].legend(loc="lower right")
    axes[1].grid(True, alpha=0.25)

    axes[2].plot(t, adc, color="#1976D2", lw=2)
    axes[2].set_ylabel("ADC12 placeholder")
    axes[2].grid(True, alpha=0.25)

    axes[3].plot(t, rz, color="#388E3C", lw=2)
    axes[3].set_ylabel("Mean z (mm)")
    axes[3].set_xlabel("Time (s)")
    axes[3].grid(True, alpha=0.25)

    fig.suptitle("SOFA single Velostat patch: load -> pressure -> placeholder ADC" + title_suffix)
    png_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(png_path, dpi=180)
    print(f"Saved: {png_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", action="store_true", help="Read batch CSV instead of GUI-scene CSV")
    args = parser.parse_args()

    if args.batch:
        csv_path = OUT / "single_velostat_patch_batch_timeseries.csv"
        png_path = OUT / "single_velostat_patch_batch_response.png"
        plot_response(csv_path, png_path, title_suffix=" - batch")
    else:
        csv_path = OUT / "single_velostat_patch_timeseries.csv"
        png_path = OUT / "single_velostat_patch_response.png"
        plot_response(csv_path, png_path)


if __name__ == "__main__":
    main()
