"""
Pipeline Runner — Chạy toàn bộ experiments và tạo báo cáo tổng hợp
=================================================================
"""
from __future__ import annotations
import sys, os
import json
import time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent.parent / "outputs" / "reports"
OUT.mkdir(parents=True, exist_ok=True)


def run_all_experiments() -> dict:
    """Run all 7 experiments and collect results."""
    results = {}

    print("\n" + "=" * 70)
    print(" ADAPTIVE AIR CUSHION + AAC — FULL EXPERIMENT SUITE")
    print("=" * 70)
    print(f" Start: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    import importlib

    exps = [
        ("EXP-01 Hybrid Calibration",       "experiments.exp01_hybrid_calibration"),
        ("EXP-02 PTI Engine",                "experiments.exp02_pti_model"),
        ("EXP-03 CNN-LSTM Forecaster",       "experiments.exp03_cnn_lstm"),
        ("EXP-04 Eye-Tracking Accuracy",     "experiments.exp04_eye_tracking"),
        ("EXP-05 Cushion Control",           "experiments.exp05_cushion_control"),
        ("EXP-06 AAC Sentence Quality",      "experiments.exp06_qwen_lora"),
        ("EXP-07 Self-Improving Loop",       "experiments.exp07_pipeline_e2e"),
    ]

    for name, module_path in exps:
        print(f"\n{'─' * 70}")
        print(f" Running {name}")
        print(f"{'─' * 70}")
        try:
            mod = importlib.import_module(module_path)
            # Try run_experiment function first
            if hasattr(mod, "run_experiment"):
                res = mod.run_experiment()
            else:
                res = {"status": "no run_experiment"}
            results[name] = {"ok": True, "result": res}
        except Exception as e:
            print(f"  ! Error: {e}")
            results[name] = {"ok": False, "error": str(e)}

    # Persist JSON report
    report_path = OUT / "experiment_results.json"
    with open(report_path, "w", encoding="utf-8") as f:
        # Make numpy types JSON-serializable
        def convert(o):
            if isinstance(o, dict):
                return {k: convert(v) for k, v in o.items()}
            if isinstance(o, (list, tuple)):
                return [convert(x) for x in o]
            if isinstance(o, (np.floating, np.integer)):
                return float(o)
            if isinstance(o, np.ndarray):
                return o.tolist()
            if isinstance(o, (bool, np.bool_)):
                return bool(o)
            return str(o)
        json.dump(convert(results), f, indent=2, ensure_ascii=False)

    print(f"\n\n{'=' * 70}")
    print(" SUMMARY")
    print(f"{'=' * 70}")
    for name, info in results.items():
        status = "✓ OK" if info["ok"] else "✗ FAIL"
        print(f"  {status}  {name}")

    print(f"\n Full results saved → {report_path}")
    return results


if __name__ == "__main__":
    run_all_experiments()
