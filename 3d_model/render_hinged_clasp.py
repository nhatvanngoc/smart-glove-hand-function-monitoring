import sys
import os
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import FreeCAD
import Part
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

out_dir = r"D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\3d_model\custom_exo\hinged_clasp_adult"
dorsal_stl = os.path.join(out_dir, "indice2_dorsal_shell.stl")
palmar_stl = os.path.join(out_dir, "indice2_palmar_swing_arm.stl")
pin_stl = os.path.join(out_dir, "clasp_hinge_pin_2mm.stl")

fig_out = r"C:\Users\user\.gemini\antigravity-ide\brain\db0fa2d1-bc0a-41c8-87e6-b71131f46734\hinged_clasp_preview.png"

def load_mesh_facets(stl_path):
    import Mesh
    mesh = Mesh.Mesh(stl_path)
    facets = []
    for facet in mesh.Facets:
        pts = [[p[0], p[1], p[2]] for p in facet.Points]
        facets.append(pts)
    return np.array(facets)

print("Đang đọc dữ liệu mesh STL...")
facets_dorsal = load_mesh_facets(dorsal_stl)
facets_palmar = load_mesh_facets(palmar_stl)
facets_pin = load_mesh_facets(pin_stl)

fig = plt.figure(figsize=(16, 12), facecolor='#0f172a')
fig.suptitle("HỆ THỐNG GÀI BẢN LỀ XOAY (HINGED SWING-ARM CLASP) CHO NGÓN TAY NGƯỜI LỚN\n(Tích hợp khoang chịu tải cảm biến Velostat & Đốt ngón người trưởng thành phi 19-21mm)", 
             fontsize=14, fontweight='bold', color='#f8fafc', y=0.96)

def style_ax(ax, title):
    ax.set_facecolor('#0f172a')
    ax.set_title(title, fontsize=11, fontweight='bold', color='#38bdf8', pad=10)
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('#334155')
    ax.yaxis.pane.set_edgecolor('#334155')
    ax.zaxis.pane.set_edgecolor('#334155')
    ax.tick_params(colors='#94a3b8', labelsize=8)
    ax.grid(True, linestyle='--', alpha=0.3, color='#475569')

# View 1: Máng mu ngón tay (Dorsal Shell)
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
style_ax(ax1, "1. MÁNG MU NGÓN TAY (Dorsal Shell)\n- Tai bản lề chạc đôi Z=0-12mm | Khuyên luồn gân | Ngàm gài 2 nấc")
col1 = Poly3DCollection(facets_dorsal, facecolors='#38bdf8', edgecolors='#0284c7', linewidths=0.2, alpha=0.9)
ax1.add_collection3d(col1)
all_pts1 = facets_dorsal.reshape(-1, 3)
ax1.set_xlim(all_pts1[:,0].min()-2, all_pts1[:,0].max()+2)
ax1.set_ylim(all_pts1[:,1].min()-2, all_pts1[:,1].max()+2)
ax1.set_zlim(all_pts1[:,2].min()-2, all_pts1[:,2].max()+2)
ax1.view_init(elev=25, azim=-60)

# View 2: Thanh gài xoay bản lề (Palmar Swing-Arm)
ax2 = fig.add_subplot(2, 2, 2, projection='3d')
style_ax(ax2, "2. THANH GÀI BỤNG NGÓN (Palmar Swing-Arm)\n- Tai giữa lồng chạc | Khoang Velostat 9.5x7x1.2mm | Móc lẫy gờ ngón")
col2 = Poly3DCollection(facets_palmar, facecolors='#f59e0b', edgecolors='#d97706', linewidths=0.2, alpha=0.9)
ax2.add_collection3d(col2)
all_pts2 = facets_palmar.reshape(-1, 3)
ax2.set_xlim(all_pts2[:,0].min()-2, all_pts2[:,0].max()+2)
ax2.set_ylim(all_pts2[:,1].min()-2, all_pts2[:,1].max()+2)
ax2.set_zlim(all_pts2[:,2].min()-2, all_pts2[:,2].max()+2)
ax2.view_init(elev=20, azim=130)

# View 3: Cận cảnh Chi tiết C: Chốt nhựa Snap-Rivet tự khóa (Plastic Snap-Pin)
ax3 = fig.add_subplot(2, 2, 3, projection='3d')
style_ax(ax3, "3. CHI TIẾT C: CHỐT NHỰA SNAP-RIVET TỰ KHÓA\n- Mũ chặn phi 4.4mm | Thân phi 1.95mm | Đầu nón có rãnh xẻ đàn hồi")
col3_pin = Poly3DCollection(facets_pin, facecolors='#ef4444', edgecolors='#b91c1c', linewidths=0.3, alpha=1.0)
ax3.add_collection3d(col3_pin)
all_pts_pin = facets_pin.reshape(-1, 3)
ax3.set_xlim(all_pts_pin[:,0].min()-2, all_pts_pin[:,0].max()+2)
ax3.set_ylim(all_pts_pin[:,1].min()-2, all_pts_pin[:,1].max()+2)
ax3.set_zlim(all_pts_pin[:,2].min()-1, all_pts_pin[:,2].max()+1)
ax3.view_init(elev=20, azim=45)

# View 4: Lắp ráp đóng hoàn chỉnh 100% nhựa (Full Plastic Assembly)
ax4 = fig.add_subplot(2, 2, 4, projection='3d')
style_ax(ax4, "4. CỤM LẮP RÁP 100% NHỰA HOÀN CHỈNH (Assembled & Locked)\n- Khóa ngàm chịu lực kéo | Bản lề chạc lồng chốt nhựa không tuột")
col4_d = Poly3DCollection(facets_dorsal, facecolors='#38bdf8', edgecolors='#0284c7', linewidths=0.2, alpha=0.85)
col4_p = Poly3DCollection(facets_palmar, facecolors='#f59e0b', edgecolors='#d97706', linewidths=0.2, alpha=0.85)
col4_pin_all = Poly3DCollection(facets_pin, facecolors='#ef4444', edgecolors='#dc2626', linewidths=0.3, alpha=1.0)
ax4.add_collection3d(col4_d)
ax4.add_collection3d(col4_p)
ax4.add_collection3d(col4_pin_all)
comb_pts = np.vstack([all_pts1, all_pts2])
ax4.set_xlim(comb_pts[:,0].min()-2, comb_pts[:,0].max()+2)
ax4.set_ylim(comb_pts[:,1].min()-2, comb_pts[:,1].max()+2)
ax4.set_zlim(comb_pts[:,2].min()-2, comb_pts[:,2].max()+2)
ax4.view_init(elev=20, azim=-45)

plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig(fig_out, dpi=200, facecolor=fig.get_facecolor(), edgecolor='none')
print(f"Ảnh kết xuất đã lưu tại: {fig_out}")
