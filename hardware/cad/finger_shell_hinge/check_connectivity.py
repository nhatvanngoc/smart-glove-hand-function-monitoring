#!/usr/bin/env python3
"""Kiểm tra mỗi chi tiết xuất ra là MỘT khối LIỀN (1 connected component),
không phải nhiều mảnh rời trôi lơ lửng (sẽ không in được vì không có gì đỡ).

Lỗi thật đã từng xảy ra (2026-10-07, phát hiện bởi chủ dự án khi mở file
.scad bằng chính OpenSCAD): `latch_arm` (tay đòn ngàm cài) của
`bottom_shell` lệch 2.8mm so với thành vỏ, không chạm vào đâu cả -> xuất
STL ra bị tách thành 2 mảnh rời. Lỗi này tồn tại ở CẢ bản .py và .scad
(không phải lỗi chuyển soạn) vì cross_check.py trước đó chỉ so khớp 2 bản
với NHAU (nên 1 lỗi giống nhau ở cả 2 bản sẽ không bị phát hiện) — script
này bổ sung một phép kiểm tra ĐỘC LẬP: đếm số mảnh rời thật sự trong từng
file STL.

Chạy:
    pip install trimesh
    python3 check_connectivity.py
"""
import os
import sys

import trimesh

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "out")
SCAD_OUT_DIR = os.path.join(OUT_DIR, "scad")

FILES = [
    ("CadQuery", os.path.join(OUT_DIR, "top_shell_dorsal.stl")),
    ("CadQuery", os.path.join(OUT_DIR, "bottom_shell_palmar.stl")),
    ("CadQuery", os.path.join(OUT_DIR, "hinge_pin.stl")),
    ("OpenSCAD", os.path.join(SCAD_OUT_DIR, "top_shell_dorsal.stl")),
    ("OpenSCAD", os.path.join(SCAD_OUT_DIR, "bottom_shell_palmar.stl")),
    ("OpenSCAD", os.path.join(SCAD_OUT_DIR, "hinge_pin.stl")),
]


def main():
    all_ok = True
    print(f"{'Nguon':<10}{'File':<30}{'So manh roi':<14}Ket qua")
    for src, path in FILES:
        if not os.path.exists(path):
            print(f"{src:<10}{os.path.basename(path):<30}{'(khong co file)'}")
            continue
        mesh = trimesh.load(path)
        pieces = mesh.split(only_watertight=False)
        n = len(pieces)
        ok = n == 1
        all_ok &= ok
        status = "OK (1 khoi lien)" if ok else f"LOI -- {n} manh roi, se KHONG IN DUOC nguyen khoi"
        print(f"{src:<10}{os.path.basename(path):<30}{n:<14}{status}")
        if not ok:
            for i, piece in enumerate(pieces):
                dim = piece.bounds[1] - piece.bounds[0]
                print(f"    manh {i}: volume~{piece.volume:.1f} mm3, bbox~{dim}")
    print()
    if all_ok:
        print("KET LUAN: Tat ca cac chi tiet deu la 1 khoi lien mach -> in duoc nguyen khoi.")
    else:
        print("KET LUAN: CO chi tiet bi tach manh -> PHAI sua truoc khi in (xem README Sec.5a).")
        sys.exit(1)


if __name__ == "__main__":
    main()
