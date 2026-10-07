#!/usr/bin/env python3
"""Xuất ảnh xem nhanh (PNG) từ các file STL trong out/, dùng matplotlib
(không cần GPU/OpenGL thật — môi trường sandbox không có driver đồ họa).

Chạy sau khi đã chạy finger_shell_hinge.py để sinh STL:
    python3 render_preview.py
"""
import os
import numpy as np
from stl import mesh
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "out")
RENDER_DIR = os.path.join(HERE, "out", "renders")
os.makedirs(RENDER_DIR, exist_ok=True)

DORSAL_COLOR = "#d9a066"   # nửa mu tay (cố định, mang khối ngàm)
PALMAR_COLOR = "#6699cc"   # nửa lòng tay (xoay quanh bản lề, mang tay địn ngàm)
PIN_COLOR    = "#333333"   # trục bản lề (hinge_pin) -- xem loi da sua 2026-10-07


def render(paths, colors, out_name, elev=20, azim=-55, title="", alpha=1.0):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="3d")
    all_pts = []
    for path, c in zip(paths, colors):
        m = mesh.Mesh.from_file(path)
        coll = Poly3DCollection(
            m.vectors, facecolor=c, edgecolor="k", linewidths=0.05, alpha=alpha
        )
        ax.add_collection3d(coll)
        all_pts.append(m.vectors.reshape(-1, 3))
    pts = np.concatenate(all_pts, axis=0)
    mins, maxs = pts.min(axis=0), pts.max(axis=0)
    center = (mins + maxs) / 2
    rng = (maxs - mins).max() / 2 * 1.15
    ax.set_xlim(center[0] - rng, center[0] + rng)
    ax.set_ylim(center[1] - rng, center[1] + rng)
    ax.set_zlim(center[2] - rng, center[2] + rng)
    ax.set_box_aspect([1, 1, 1])
    ax.view_init(elev=elev, azim=azim)
    ax.set_xlabel("X - doc than ngon (mm)")
    ax.set_ylabel("Y - ngang (mm)")
    ax.set_zlabel("Z - mu/long tay (mm)")
    ax.set_title(title)
    plt.tight_layout()
    out_path = os.path.join(RENDER_DIR, out_name)
    plt.savefig(out_path, dpi=150)
    plt.close(fig)
    print("saved", out_path)


def main():
    b = os.path.join(OUT_DIR, "")
    render(
        [b + "top_shell_dorsal.stl"],
        [DORSAL_COLOR],
        "01_top_shell_dorsal.png",
        title="Nua MU TAY (co dinh) - 3 khop ban le + khoi ngam",
    )
    render(
        [b + "bottom_shell_palmar.stl"],
        [PALMAR_COLOR],
        "02_bottom_shell_palmar.png",
        title="Nua LONG TAY (xoay quanh ban le) - 2 khop ban le + tay don ngam",
    )
    render(
        [b + "assembly_closed__top.stl", b + "assembly_closed__bottom.stl", b + "assembly_closed__pin.stl"],
        [DORSAL_COLOR, PALMAR_COLOR, PIN_COLOR],
        "03_assembly_closed_iso.png",
        title="Trang thai DONG (khi da cai ngam) - goc nhin iso (co truc ban le)",
        elev=20,
        azim=-55,
    )
    render(
        [b + "assembly_closed__top.stl", b + "assembly_closed__bottom.stl", b + "assembly_closed__pin.stl"],
        [DORSAL_COLOR + "aa", PALMAR_COLOR + "aa", PIN_COLOR + "cc"],
        "04_assembly_closed_end.png",
        title="Trang thai DONG - nhin doc truc ngon tay (tiet dien, co truc ban le)",
        elev=0,
        azim=0,
    )
    render(
        [b + "assembly_open__top.stl", b + "assembly_open__bottom.stl", b + "assembly_open__pin.stl"],
        [DORSAL_COLOR, PALMAR_COLOR, PIN_COLOR],
        "05_assembly_open_iso.png",
        title="Trang thai MO (ban le xoay ~150 do) - dat ngon vao, chua cai ngam (co truc ban le)",
        elev=22,
        azim=-60,
    )
    render(
        [b + "assembly_open__top.stl", b + "assembly_open__bottom.stl", b + "assembly_open__pin.stl"],
        [DORSAL_COLOR + "cc", PALMAR_COLOR + "cc", PIN_COLOR],
        "06_assembly_open_end.png",
        title="Trang thai MO - nhin doc truc ngon tay (co truc ban le)",
        elev=0,
        azim=0,
    )
    render(
        [b + "hinge_pin.stl"],
        ["#444444"],
        "07_hinge_pin.png",
        title="Chot ban le (truc), rieng le - in PETG hoac dung que nhua/kim loai phi ~2mm",
    )


if __name__ == "__main__":
    main()
