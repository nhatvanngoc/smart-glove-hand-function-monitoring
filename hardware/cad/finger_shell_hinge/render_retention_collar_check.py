#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Xuất ảnh minh hoạ cho `check_retention_collar_exposure.py` / README §5f
("Đính chính 2026-10-08") — vẽ RIÊNG phần vật liệu MỚI mà 2 vai chặn
chống tuột trục (`pin_retain_r`) tạo ra trên `top_shell`, để thấy rõ bằng
mắt rằng đó là 2 cục u nửa-hình-trụ nhỏ (không phải lỗi dựng lưới STL).

Chạy: python3 render_retention_collar_check.py
Xuất: out/renders/17_retention_collar_bump_check.png
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

import finger_shell_hinge as fsh
from check_retention_collar_exposure import exposed_collar_bump

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PNG = os.path.join(HERE, "out", "renders", "17_retention_collar_bump_check.png")


def tessellate(shape, tol=0.1):
    verts, faces = shape.val().tessellate(tol)
    V = np.array([(v.x, v.y, v.z) for v in verts])
    F = np.array(faces)
    return V, F


def main():
    top_with = fsh.build_top_shell()
    diff, vol, bbox = exposed_collar_bump()
    print(f"The tich vat lieu MOI: {vol:.4f} mm3, bbox Z=[{bbox.zmin:.3f}, {bbox.zmax:.3f}]")

    fig = plt.figure(figsize=(14, 6))
    panels = [
        (top_with, "orange", "top_shell (full, co vai chan)"),
        (diff, "red", "Vat lieu MOI do vai chan tao ra (top_with - top_without)"),
    ]
    for i, (shape, color, title) in enumerate(panels):
        ax = fig.add_subplot(1, 2, i + 1, projection="3d")
        V, F = tessellate(shape)
        tris = V[F]
        pc = Poly3DCollection(tris, alpha=0.9, facecolor=color, edgecolor="k", linewidths=0.1)
        ax.add_collection3d(pc)
        mins = V.min(axis=0)
        maxs = V.max(axis=0)
        ax.set_xlim(mins[0], maxs[0])
        ax.set_ylim(mins[1] - 5, maxs[1] + 5)
        ax.set_zlim(mins[2] - 5, maxs[2] + 5)
        ax.set_title(title)
        ax.set_xlabel("X (doc truc ban le)")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z (mat phan 2 nua o Z=0)")
        ax.view_init(elev=15, azim=-60)

    plt.tight_layout()
    os.makedirs(os.path.dirname(OUT_PNG), exist_ok=True)
    plt.savefig(OUT_PNG, dpi=130)
    print("Da luu:", OUT_PNG)


if __name__ == "__main__":
    main()
