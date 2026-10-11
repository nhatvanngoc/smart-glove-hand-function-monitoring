import sys
import os
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import FreeCAD
import Mesh
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

models_dir = r"D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\3d_model\custom_exo\dovetail_ratchet_finger"
fig_out = r"C:\Users\user\.gemini\antigravity-ide\brain\db0fa2d1-bc0a-41c8-87e6-b71131f46734\dovetail_ratchet_preview.png"

def load_mesh_facets(stl_name, max_facets=2500):
    path = os.path.join(models_dir, stl_name)
    if not os.path.exists(path):
        print(f"Warning: {path} not found")
        return np.zeros((0, 3, 3))
    mesh = Mesh.Mesh(path)
    count = len(mesh.Facets)
    step = max(1, count // max_facets)
    facets = []
    for i in range(0, count, step):
        facet = mesh.Facets[i]
        pts = [[p[0], p[1], p[2]] for p in facet.Points]
        facets.append(pts)
    return np.array(facets)

print("Đang đọc dữ liệu mesh STL hệ thống Dovetail Ratchet...")
f_c1 = load_mesh_facets("cuff1_proximal.stl")
f_c2 = load_mesh_facets("cuff2_middle.stl")
f_c3 = load_mesh_facets("cuff3_distal.stl")
f_s_pip = load_mesh_facets("slider_pip_dovetail.stl")
f_s_dip = load_mesh_facets("slider_dip_dovetail.stl")
f_p_lock = load_mesh_facets("pin_lock_dovetail.stl")
f_p_clevis = load_mesh_facets("pin_clevis_pivot.stl")
f_straight = load_mesh_facets("full_finger_dovetail_assembly_straight.stl", max_facets=5000)

fig = plt.figure(figsize=(18, 14), facecolor='#0b1120')
fig.suptitle("HỆ THỐNG GĂNG TAY THÍCH ỨNG ĐỘT PHÁ: QUAI ĐAI ĐỒNG TÂM + THANH TRƯỢT ĐUÔI ÉN DOVETAIL\n(8 Nấc Chu Vi Bụng phi 17-24.5mm Luồn Máng | 3 Nấc Chiều Dài Đuôi Én Khóa Cứng Cắt Kép | Khoang Velostat 9.8x7.1mm Chuẩn)", 
             fontsize=13, fontweight='bold', color='#f8fafc', y=0.97)

def style_ax(ax, title):
    ax.set_facecolor('#0f172a')
    ax.set_title(title, fontsize=11, fontweight='bold', color='#38bdf8', pad=10)
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('#1e293b')
    ax.yaxis.pane.set_edgecolor('#1e293b')
    ax.zaxis.pane.set_edgecolor('#1e293b')
    ax.tick_params(colors='#64748b', labelsize=8)
    ax.grid(True, linestyle='--', alpha=0.25, color='#334155')

# View 1: Bộ linh kiện in FDM xếp bàn (3 Cuffs + 2 Sliders + Chốt)
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
style_ax(ax1, "1. BỘ LINH KIỆN IN RỜI FDM CHUẨN XÁC\n- 3 Máng Đốt Ngón + 2 Thanh Trượt Đuôi Én Clevis + Bộ Chốt Chịu Cắt Kép")

c1_s = f_c1.copy(); c1_s[:,:,0] -= 38
c3_s = f_c3.copy(); c3_s[:,:,0] += 38
s_pip_s = f_s_pip.copy(); s_pip_s[:,:,0] -= 18; s_pip_s[:,:,1] -= 25
s_dip_s = f_s_dip.copy(); s_dip_s[:,:,0] += 18; s_dip_s[:,:,1] -= 25

col_c1 = Poly3DCollection(c1_s, facecolors='#3b82f6', edgecolors='#1d4ed8', linewidths=0.1, alpha=0.9)
col_c2 = Poly3DCollection(f_c2, facecolors='#10b981', edgecolors='#047857', linewidths=0.1, alpha=0.9)
col_c3 = Poly3DCollection(c3_s, facecolors='#f59e0b', edgecolors='#b45309', linewidths=0.1, alpha=0.9)
col_sp = Poly3DCollection(s_pip_s, facecolors='#ec4899', edgecolors='#be185d', linewidths=0.1, alpha=0.95)
col_sd = Poly3DCollection(s_dip_s, facecolors='#8b5cf6', edgecolors='#6d28d9', linewidths=0.1, alpha=0.95)

ax1.add_collection3d(col_c1)
ax1.add_collection3d(col_c2)
ax1.add_collection3d(col_c3)
ax1.add_collection3d(col_sp)
ax1.add_collection3d(col_sd)

all_v1 = np.vstack([c1_s.reshape(-1,3), f_c2.reshape(-1,3), c3_s.reshape(-1,3), s_pip_s.reshape(-1,3)])
ax1.set_xlim(all_v1[:,0].min()-2, all_v1[:,0].max()+2)
ax1.set_ylim(all_v1[:,1].min()-2, all_v1[:,1].max()+2)
ax1.set_zlim(all_v1[:,2].min()-2, all_v1[:,2].max()+2)
ax1.view_init(elev=28, azim=-60)

# View 2: Cụm lắp ráp duỗi thẳng 0° (Isometric mu ngón)
ax2 = fig.add_subplot(2, 2, 2, projection='3d')
style_ax(ax2, "2. CỤM LẮP RÁP DUỖI THẲNG (Góc Nhìn Mu Ngón Dorsal)\n- Rãnh đuôi én 45° triệt tiêu 100% xoắn vặn | Khớp Clevis đôi chịu tải mượt mà")
col2 = Poly3DCollection(f_straight, facecolors='#0ea5e9', edgecolors='#0284c7', linewidths=0.12, alpha=0.88)
ax2.add_collection3d(col2)
all_s = f_straight.reshape(-1, 3)
ax2.set_xlim(all_s[:,0].min()-2, all_s[:,0].max()+2)
ax2.set_ylim(all_s[:,1].min()-2, all_s[:,1].max()+2)
ax2.set_zlim(all_s[:,2].min()-2, all_s[:,2].max()+2)
ax2.view_init(elev=25, azim=135)

# View 3: Góc nhìn mặt bụng (Palmar view) khoang cảm biến Velostat & quai đai
ax3 = fig.add_subplot(2, 2, 3, projection='3d')
style_ax(ax3, "3. GÓC NHÌN MẶT BỤNG (Palmar Contact Surface)\n- 3 Khoang Velostat phẳng 9.8x7.1mm | Quai đai dẻo răng cưa 8 nấc ôm sát đồng tâm")
col3 = Poly3DCollection(f_straight, facecolors='#10b981', edgecolors='#047857', linewidths=0.12, alpha=0.88)
ax3.add_collection3d(col3)
ax3.set_xlim(all_s[:,0].min()-2, all_s[:,0].max()+2)
ax3.set_ylim(all_s[:,1].min()-2, all_s[:,1].max()+2)
ax3.set_zlim(all_s[:,2].min()-2, all_s[:,2].max()+2)
ax3.view_init(elev=-25, azim=-45)

# View 4: Cận cảnh cơ cấu Máng dẫn hướng Buckle Sleeve & Ngàm Đuôi Én Dovetail
ax4 = fig.add_subplot(2, 2, 4, projection='3d')
style_ax(ax4, "4. CẬN CẢNH MÁNG DẪN HƯỚNG BUCKLE & KHỚP CLEVIS\n- Quai răng cưa trượt qua khe hở 1.8mm | Chốt nêm xỏ ngang chịu cắt đôi vững chãi")
col4 = Poly3DCollection(f_straight, facecolors='#f59e0b', edgecolors='#b45309', linewidths=0.15, alpha=0.9)
ax4.add_collection3d(col4)
# Zoom into Middle Phalanx & PIP joint area
mid_z = (all_s[:,2].min() + all_s[:,2].max()) / 2
ax4.set_xlim(-15, 15)
ax4.set_ylim(-15, 20)
ax4.set_zlim(mid_z - 22, mid_z + 22)
ax4.view_init(elev=18, azim=40)

plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig(fig_out, dpi=180, facecolor=fig.get_facecolor(), edgecolor='none')
print(f"Đã lưu ảnh render thành công tại: {fig_out}")
