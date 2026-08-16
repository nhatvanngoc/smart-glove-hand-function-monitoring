"""
Stage 0 INTAKE — Khởi tạo dự án + load đề cương
=================================================
Output: Stage 0 status, RQ Brief confirmation.
"""
from __future__ import annotations
import sys, os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def run_stage_0() -> dict:
    print("\n" + "=" * 60)
    print(" STAGE 0 — INTAKE")
    print("=" * 60)

    # Load RQ brief
    rq_path = ROOT / "docs" / "01_RQ_Brief.md"
    if not rq_path.exists():
        print("  ! RQ Brief not found")
        return {"ok": False}

    content = rq_path.read_text(encoding="utf-8")
    print(f"  ✓ Loaded RQ Brief ({len(content)} chars)")

    # Confirm key elements
    key_items = {
        "topic":   "Nghiên cứu và phát triển hệ thống đệm khí thích ứng",
        "field":   "Hệ thống nhúng",
        "student": "Văn Ngọc Nhật Anh",
        "school":  "THPT Quảng Trị",
    }
    for k, v in key_items.items():
        present = v in content
        print(f"  {'✓' if present else '✗'} {k}: {v}")
    return {"ok": True, "rq_brief_chars": len(content)}


if __name__ == "__main__":
    run_stage_0()
