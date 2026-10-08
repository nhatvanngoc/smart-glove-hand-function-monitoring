#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tìm hướng ĐẶT LÊN BÀN IN (print orientation) sao cho diện tích bề mặt
"đua ra" (overhang) cần support là ÍT NHẤT, cho `top_shell_dorsal` và
`bottom_shell_palmar` — trả lời trực tiếp yêu cầu chủ dự án "xoay chỉnh
sửa sao cho khi để lên slicer thì support tạo ra sẽ ít nhất đi".

KHÔNG có trình cắt lớp (slicer) thật nào chạy được trong sandbox này
(không có PrusaSlicer/Cura CLI, không có mạng ra ngoài danh sách host cho
phép) — đây là một THƯỚC ĐO HÌNH HỌC THAY THẾ (proxy), dùng đúng tiêu chí
mà mọi slicer FDM dùng để quyết định có sinh support cho một mặt tam giác
hay không:

  "Mặt tam giác CẦN support nếu nó CHÚC XUỐNG (hướng pháp tuyến có thành
   phần Z âm) và góc giữa pháp tuyến với phương thẳng đứng-xuống (0,0,-1)
   NHỎ HƠN một ngưỡng (mặc định 45°, giống PrusaSlicer/Cura mặc định phổ
   biến cho overhang) — tức là mặt càng gần NẰM NGANG CHÚC XUỐNG thì càng
   chắc chắn cần support; mặt gần như THẲNG ĐỨNG (tường đứng) thì không
   cần."

Với mỗi chi tiết, quét qua **24 hướng đặt "theo trục chính"** (nhóm xoay
của hình hộp — mọi cách xoay sao cho 1 trong 6 mặt hộp bao úp xuống bàn
in và không bị nghiêng chéo tuỳ ý) — đây là tập hướng đặt THỰC TẾ hay
dùng nhất khi đặt tay trong slicer (đặt phẳng theo 1 mặt, rồi xoay quanh
trục thẳng đứng), tính tổng diện tích overhang cho mỗi hướng, chọn hướng
nhỏ nhất.

Loại trừ: tam giác chạm ĐÚNG mặt bàn in (Z ~ Zmin của khối, trong sai số
nhỏ) không tính là overhang — vì nó tựa thẳng lên bàn in (hoặc raft/mép
dính), không phải lơ lửng trong không khí.

Chạy:
    LD_LIBRARY_PATH=~/.local/stublibs python3 check_print_orientation.py
"""
import itertools
import math
import os

import numpy as np

import finger_shell_hinge as fsh

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "out")

OVERHANG_THRESHOLD_DEG = 45.0  # giống mặc định phổ biến (PrusaSlicer/Cura)
BED_CONTACT_EPS = 0.05  # mm, dung sai coi 1 tam giác là "chạm bàn in"


def tessellate(shape, lin_tol=0.2, ang_tol=0.25):
    verts, faces = shape.val().tessellate(lin_tol, ang_tol)
    v = np.array([[p.x, p.y, p.z] for p in verts], dtype=float)
    f = np.array(faces, dtype=int)
    return v, f


def rotation_group_24():
    """Trả về 24 ma trận xoay 3x3 (nhóm xoay đối xứng của hình lập phương)
    -- mọi cách xoay sao cho hệ trục cục bộ khớp lại với hệ trục bàn in
    (1 trong 6 mặt úp xuống, 1 trong 4 góc xoay quanh trục đứng)."""
    def Rx(d):
        t = math.radians(d)
        c, s = math.cos(t), math.sin(t)
        return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])

    def Ry(d):
        t = math.radians(d)
        c, s = math.cos(t), math.sin(t)
        return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])

    def Rz(d):
        t = math.radians(d)
        c, s = math.cos(t), math.sin(t)
        return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])

    mats = []
    seen = []
    for face_rot in [np.eye(3), Rx(90), Rx(180), Rx(270), Ry(90), Ry(270)]:
        for spin in [0, 90, 180, 270]:
            M = Rz(spin) @ face_rot
            key = tuple(np.round(M.flatten(), 6))
            if key not in seen:
                seen.append(key)
                mats.append((M, face_rot_name(face_rot), spin))
    return mats


def face_rot_name(M):
    names = {
        tuple(np.round(np.eye(3).flatten(), 6)): "mat +Z xuong duoi (khong xoay)",
    }
    key = tuple(np.round(M.flatten(), 6))
    return names.get(key, "mat khac xuong duoi")


def overhang_area(v, f, M):
    """Xoay đỉnh bằng ma trận M, tính tổng diện tích tam giác overhang."""
    vr = v @ M.T
    tri = vr[f]  # (n, 3, 3)
    p0, p1, p2 = tri[:, 0], tri[:, 1], tri[:, 2]
    normals = np.cross(p1 - p0, p2 - p0)
    areas = 0.5 * np.linalg.norm(normals, axis=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        unit_n = normals / (2 * areas[:, None])
    unit_n = np.nan_to_num(unit_n)
    z_tri = tri[:, :, 2]
    z_min_tri = z_tri.min(axis=1)
    z_global_min = vr[:, 2].min()
    is_bed_contact = z_min_tri <= z_global_min + BED_CONTACT_EPS
    cos_thresh = math.cos(math.radians(OVERHANG_THRESHOLD_DEG))
    needs_support = (unit_n[:, 2] < -cos_thresh) & (~is_bed_contact)
    return float(areas[needs_support].sum()), float(areas.sum())


def scan_part(name, shape):
    v, f = tessellate(shape)
    print(f"\n=== {name} ===  ({len(f)} tam giac, tong dien tich be mat "
          f"{0.5 * np.linalg.norm(np.cross(v[f][:,1]-v[f][:,0], v[f][:,2]-v[f][:,0]), axis=1).sum():.1f} mm2)")
    results = []
    for M, face_name, spin in rotation_group_24():
        oh, total = overhang_area(v, f, M)
        results.append((oh, total, M, face_name, spin))
    results.sort(key=lambda r: r[0])
    print(f"{'Hang':<6}{'Overhang (mm2)':<18}{'% be mat':<12}")
    for i, (oh, total, M, face_name, spin) in enumerate(results[:5]):
        pct = 100.0 * oh / total if total else 0.0
        print(f"{i+1:<6}{oh:<18.2f}{pct:<12.2f}%  M=\n{np.round(M,3)}")
    print("...")
    worst = results[-1]
    print(f"(Toi te nhat trong 24 huong: {worst[0]:.2f} mm2 = "
          f"{100.0*worst[0]/worst[1]:.2f}% be mat)")
    return results[0]  # (overhang, total, M, ...)


def main():
    top = fsh.build_top_shell()
    bot = fsh.build_bottom_shell()

    best_top = scan_part("top_shell_dorsal (nua mu tay)", top)
    best_bot = scan_part("bottom_shell_palmar (nua long tay)", bot)

    print("\n\n===== KET LUAN =====")
    for label, best in [("top_shell_dorsal", best_top), ("bottom_shell_palmar", best_bot)]:
        oh, total, M, _, _ = best
        pct = 100.0 * oh / total if total else 0.0
        print(f"{label}: huong TOT NHAT trong 24 huong goc-truc -> overhang con lai "
              f"{oh:.2f} mm2 ({pct:.2f}% be mat). Ma tran xoay (ap dung cho dinh, "
              f"v_new = v_old @ M.T):")
        print(np.round(M, 4))


if __name__ == "__main__":
    main()
