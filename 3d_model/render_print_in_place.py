import sys
import os
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import FreeCAD
import Part
import Mesh
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

out_dir = r"D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\3d_model\custom_exo\print_in_place_adult"
stl_dorsal = os.path.join(out_dir, "pip_dorsal_shell_integrated_pin.stl")
stl_arm_closed = os.path.join(out_dir, "pip_palmar_arm_closed.stl")
stl_pip_open = os.path.join(out_dir, "finger_print_in_place_open90.stl")

fig_out = r"C:\Users\user\.gemini\antigravity-ide\brain\db0fa2d1-bc0a-41c8-87e6-b71131f46734\print_in_place_preview.png"

def load_mesh_facets(stl_path):
    mesh = Mesh.Mesh(stl_path)
    facets = []
    for facet in mesh.Facets:
        pts = [[p[0], p[1], p[2]] for p in facet.Points]
        facets.append(pts)
    return np.array(facets)

print("Đang đọc dữ liệu mesh STL Print-in-Place...")
facets_dorsal = load_mesh_facets(stl_dorsal)
facets_arm_closed = load_mesh_facets(stl_arm_closed)
facets_pip_open = load_mesh_facets(stl_pip_open)

fig = plt.figure(figsize=(16, 12), facecolor='#0f172a')
fig.suptitle("HỆ THỐNG BẢN LỀ IN NGUYÊN KHỐI FDM (PRINT-IN-PLACE REVOLUTE HINGE)\n(In 1 lần duy nhất trên bàn in - Trục xoay đúc liền giam trong tai xoay - Không cần lắp ráp)", 
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

# View 1: Cụm in nguyên khối ở tư thế mở -100 độ (Khuyên dùng nạp Slicer FDM)
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
style_ax(ax1, "1. TƯ THẾ NẠP IN FDM (Print-in-Place Open -100°)\n- In 1 lần | Trục bản lề đứng Z | Khóa mỏ quạ ngoài mở thoáng hoàn toàn")
col1 = Poly3DCollection(facets_pip_open, facecolors='#10b981', edgecolors='#059669', linewidths=0.2, alpha=0.9)
ax1.add_collection3d(col1)
all_pts1 = facets_pip_open.reshape(-1, 3)
ax1.set_xlim(all_pts1[:,0].min()-2, all_pts1[:,0].max()+2)
ax1.set_ylim(all_pts1[:,1].min()-2, all_pts1[:,1].max()+2)
ax1.set_zlim(all_pts1[:,2].min()-2, all_pts1[:,2].max()+2)
ax1.view_init(elev=25, azim=-60)

# View 2: Trạng thái khi gấp đóng & khóa ngàm (Closed Position)
ax2 = fig.add_subplot(2, 2, 2, projection='3d')
style_ax(ax2, "2. TRẠNG THÁI GẬP ĐÓNG & KHÓA NGÀM (Closed & Latched)\n- Mỏ quạ sập ôm ngoài | 2 nấc chỉnh ngón to/nhỏ | Tai gạt ngón cái mở 1 tay")
col2_d = Poly3DCollection(facets_dorsal, facecolors='#38bdf8', edgecolors='#0284c7', linewidths=0.2, alpha=0.85)
col2_a = Poly3DCollection(facets_arm_closed, facecolors='#f59e0b', edgecolors='#d97706', linewidths=0.2, alpha=0.85)
ax2.add_collection3d(col2_d)
ax2.add_collection3d(col2_a)
all_pts2 = np.vstack([facets_dorsal.reshape(-1, 3), facets_arm_closed.reshape(-1, 3)])
ax2.set_xlim(all_pts2[:,0].min()-2, all_pts2[:,0].max()+2)
ax2.set_ylim(all_pts2[:,1].min()-2, all_pts2[:,1].max()+2)
ax2.set_zlim(all_pts2[:,2].min()-2, all_pts2[:,2].max()+2)
ax2.view_init(elev=20, azim=135)

# View 3: Cận cảnh cơ cấu khóa ngàm mỏ quạ ngoài (External Ratchet Clasp Close-up)
ax3 = fig.add_subplot(2, 2, 3, projection='3d')
style_ax(ax3, "3. CẬN CẢNH KHÓA MỎ QUẠ ÔM NGOÀI (External Snap-Claw)\n- 2 rãnh nấc ngoài (Xanh) | Răng mỏ quạ sập chặt | Tai tì ngón cái nhô 3.5mm")
col3_d = Poly3DCollection(facets_dorsal, facecolors='#38bdf8', edgecolors='#0284c7', linewidths=0.2, alpha=0.8)
col3_a = Poly3DCollection(facets_arm_closed, facecolors='#f59e0b', edgecolors='#d97706', linewidths=0.2, alpha=0.9)
ax3.add_collection3d(col3_d)
ax3.add_collection3d(col3_a)
# Zoom sâu vào vùng khóa ngàm bên phải (X: 9 đến 19, Y: -4 đến 6, Z: 0 đến 12)
ax3.set_xlim(9, 19)
ax3.set_ylim(-4, 6)
ax3.set_zlim(-1, 13)
ax3.view_init(elev=25, azim=60)

# View 4: Góc nhìn mặt cắt trục ngón tay (Front Axial View)
ax4 = fig.add_subplot(2, 2, 4, projection='3d')
style_ax(ax4, "4. GÓC NHÌN TRỤC DỌC NGÓN TAY (Front Axial Profile)\n- Cảm biến Velostat nằm trọn trong hốc phẳng | Lẫy gài có cữ bấm ngón cái")
col4_d = Poly3DCollection(facets_dorsal, facecolors='#38bdf8', edgecolors='#0284c7', linewidths=0.2, alpha=0.85)
col4_a = Poly3DCollection(facets_arm_closed, facecolors='#f59e0b', edgecolors='#d97706', linewidths=0.2, alpha=0.85)
ax4.add_collection3d(col4_d)
ax4.add_collection3d(col4_a)
ax4.set_xlim(all_pts2[:,0].min()-2, all_pts2[:,0].max()+2)
ax4.set_ylim(all_pts2[:,1].min()-2, all_pts2[:,1].max()+2)
ax4.set_zlim(all_pts2[:,2].min()-2, all_pts2[:,2].max()+2)
ax4.view_init(elev=12, azim=-10)

plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig(fig_out, dpi=200, facecolor=fig.get_facecolor(), edgecolor='none')
print(f"Ảnh kết xuất Print-in-Place đã lưu tại: {fig_out}")
