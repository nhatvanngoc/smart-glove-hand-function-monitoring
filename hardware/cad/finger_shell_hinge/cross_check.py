#!/usr/bin/env python3
"""Đối chiếu hình học giữa 2 bản CAD độc lập của cùng 1 thiết kế:

  - out/*.stl              <- xuất từ finger_shell_hinge.py  (CadQuery / lõi Open CASCADE)
  - out/scad/*.stl          <- xuất từ finger_shell_hinge.scad (render_scad_wasm.mjs / lõi CGAL qua OpenSCAD thật)

Hai lõi hình học hoàn toàn khác nhau (OCCT vs CGAL). Nếu thể tích và
bounding-box của từng chi tiết khớp nhau (sai số chỉ do rời rạc hoá
$fn/hình tròn), đó là bằng chứng khá mạnh rằng công thức/toạ độ trong
file .scad được chép đúng từ file .py — KHÔNG phải bằng chứng là thiết
kế đã đúng về mặt công thái học/lực học (việc đó vẫn cần in + đo thật,
xem README §8).

Chạy:
    pip install numpy-stl
    python3 cross_check.py
"""
import os
from stl import mesh

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "out")
SCAD_OUT_DIR = os.path.join(OUT_DIR, "scad")

PAIRS = [
    ("top_shell_dorsal.stl", "top_shell_dorsal.stl"),
    ("bottom_shell_palmar.stl", "bottom_shell_palmar.stl"),
    ("hinge_pin.stl", "hinge_pin.stl"),
    ("top_shell_dorsal_print_ready.stl", "top_shell_dorsal_print_ready.stl"),
    ("bottom_shell_palmar_print_ready.stl", "bottom_shell_palmar_print_ready.stl"),
]

TOL_VOL_PCT = 1.0   # sai số thể tích chấp nhận được (%), chỉ do rời rạc hoá hình tròn
TOL_BBOX_MM = 0.05  # sai số bounding-box chấp nhận được (mm)


def load_stats(path):
    m = mesh.Mesh.from_file(path)
    vol, _, _ = m.get_mass_properties()
    pts = m.vectors.reshape(-1, 3)
    bbox = pts.max(axis=0) - pts.min(axis=0)
    return abs(vol), bbox


def main():
    print(f"{'Chi tiet':<24}{'Vol CadQuery':>14}{'Vol OpenSCAD':>14}{'Lech %':>10}  BBox khop?")
    all_ok = True
    for cq_name, scad_name in PAIRS:
        cq_path = os.path.join(OUT_DIR, cq_name)
        scad_path = os.path.join(SCAD_OUT_DIR, scad_name)
        if not (os.path.exists(cq_path) and os.path.exists(scad_path)):
            print(f"  (bo qua {cq_name}: chua co ca 2 file xuat)")
            continue
        v1, b1 = load_stats(cq_path)
        v2, b2 = load_stats(scad_path)
        diff_pct = abs(v1 - v2) / v1 * 100
        bbox_ok = all(abs(a - b) <= TOL_BBOX_MM for a, b in zip(b1, b2))
        ok = diff_pct <= TOL_VOL_PCT and bbox_ok
        all_ok &= ok
        status = "OK" if ok else "LECH -- can kiem tra lai .scad"
        print(f"{cq_name:<24}{v1:>14.1f}{v2:>14.1f}{diff_pct:>9.2f}%  {bbox_ok}  [{status}]")
        if not bbox_ok:
            print(f"    bbox CadQuery={b1}, bbox OpenSCAD={b2}")
    print()
    print("KET LUAN:", "2 ban CAD khop hinh hoc (trong sai so roi rac hoa)." if all_ok
          else "CO LECH -- sua lai finger_shell_hinge.scad cho khop finger_shell_hinge.py")


if __name__ == "__main__":
    main()
