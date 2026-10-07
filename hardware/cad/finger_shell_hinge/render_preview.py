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


def render(paths, colors, out_name, elev=20, azim=-55, title="", alpha=1.0,
           zoom_center=None, zoom_range=None):
    """zoom_center/zoom_range (tuỳ chọn): ép khung nhìn vào 1 VÙNG CỤ THỂ
    (vd. riêng khu vực ngàm cài) thay vì tự co giãn vừa khít TOÀN BỘ khối --
    dùng để xác nhận trực quan 2 chi tiết nhỏ (móc/răng) có thực sự chồng
    lên nhau hay không (xem README §5c)."""
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
    if zoom_center is not None and zoom_range is not None:
        center = np.array(zoom_center)
        rng = zoom_range
    else:
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
    # Nếu PIN_INTEGRATED=true (mặc định từ 2026-10-07), trục đã HÀN LIỀN vào
    # top_shell nên không có file "*__pin.stl" riêng nữa (đã nằm sẵn trong
    # "*__top.stl") -> tự động bỏ qua lớp pin riêng nếu không tìm thấy file.
    has_pin_closed = os.path.exists(b + "assembly_closed__pin.stl")
    has_pin_open = os.path.exists(b + "assembly_open__pin.stl")

    def paths_colors(prefix, dorsal_c, palmar_c, has_pin):
        paths = [b + f"{prefix}__top.stl", b + f"{prefix}__bottom.stl"]
        colors = [dorsal_c, palmar_c]
        if has_pin:
            paths.append(b + f"{prefix}__pin.stl")
            colors.append(PIN_COLOR)
        return paths, colors

    render(
        [b + "top_shell_dorsal.stl"],
        [DORSAL_COLOR],
        "01_top_shell_dorsal.png",
        title="Nua MU TAY (co dinh) - 3 khop ban le + khoi ngam + truc han lien",
    )
    render(
        [b + "bottom_shell_palmar.stl"],
        [PALMAR_COLOR],
        "02_bottom_shell_palmar.png",
        title="Nua LONG TAY (xoay quanh ban le) - 2 khop ban le + tay don ngam",
    )
    p, c = paths_colors("assembly_closed", DORSAL_COLOR, PALMAR_COLOR, has_pin_closed)
    render(
        p, c,
        "03_assembly_closed_iso.png",
        title="Trang thai DONG (khi da cai ngam) - goc nhin iso",
        elev=20,
        azim=-55,
    )
    p, c = paths_colors("assembly_closed", DORSAL_COLOR + "aa", PALMAR_COLOR + "aa", has_pin_closed)
    render(
        p, c,
        "04_assembly_closed_end.png",
        title="Trang thai DONG - nhin doc truc ngon tay (tiet dien)",
        elev=0,
        azim=0,
    )
    p, c = paths_colors("assembly_open", DORSAL_COLOR, PALMAR_COLOR, has_pin_open)
    render(
        p, c,
        "05_assembly_open_iso.png",
        title="Trang thai MO (ban le xoay ~150 do) - dat ngon vao, chua cai ngam",
        elev=22,
        azim=-60,
    )
    p, c = paths_colors("assembly_open", DORSAL_COLOR + "cc", PALMAR_COLOR + "cc", has_pin_open)
    render(
        p, c,
        "06_assembly_open_end.png",
        title="Trang thai MO - nhin doc truc ngon tay",
        elev=0,
        azim=0,
    )
    render(
        [b + "hinge_pin.stl"],
        ["#444444"],
        "07_hinge_pin.png",
        title="Truc ban le (hinh dang/kich thuoc tham khao) - da han lien vao top_shell" if not has_pin_closed
        else "Chot ban le (truc), rieng le - in PETG hoac dung que nhua/kim loai phi ~2mm",
    )

    # 2026-10-07: anh can canh vung NGAM CAI (moc + rang) o trang thai DONG,
    # de xac nhan truc quan cho fix loi #3 (SS5c) -- moc phai thay ro NAM
    # TRONG vung cac nac rang, khong con cach xa nhu truoc khi sua.
    p, c = paths_colors("assembly_closed", DORSAL_COLOR, PALMAR_COLOR, has_pin_closed)
    render(
        p, c,
        "08_latch_closeup.png",
        title="Can canh NGAM CAI o trang thai DONG - moc phai nam trong vung rang (SS5c)",
        elev=8,
        azim=160,
        zoom_center=(12.0, 14.8, 11.0),
        zoom_range=5.0,
        alpha=0.85,
    )


if __name__ == "__main__":
    main()
