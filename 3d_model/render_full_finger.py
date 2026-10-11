import sys
import os
import io
import struct
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

out_dir = r"D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\3d_model\custom_exo\full_finger_modular"
fig_out = r"C:\Users\user\.gemini\antigravity-ide\brain\db0fa2d1-bc0a-41c8-87e6-b71131f46734\full_finger_preview.png"

def load_stl_fast(stl_path, max_facets=2500):
    if not os.path.exists(stl_path):
        print(f"Warning: {stl_path} not found")
        return np.zeros((0, 3, 3))
    with open(stl_path, 'rb') as f:
        f.seek(80)
        c_bytes = f.read(4)
        if len(c_bytes) < 4:
            return np.zeros((0, 3, 3))
        n_tri = struct.unpack('<I', c_bytes)[0]
        data = f.read()
    
    step = max(1, n_tri // max_facets)
    triangles = []
    for i in range(0, n_tri, step):
        offset = i * 50
        if offset + 48 > len(data):
            break
        v = struct.unpack('<9f', data[offset + 12 : offset + 48])
        triangles.append([[v[0], v[1], v[2]], [v[3], v[4], v[5]], [v[6], v[7], v[8]]])
    return np.array(triangles)

print("Đang đọc nhanh dữ liệu STL nhị phân...")
f_p1 = load_stl_fast(os.path.join(out_dir, "phalanx1_proximal_open.stl"))
f_p2 = load_stl_fast(os.path.join(out_dir, "phalanx2_middle_open.stl"))
f_p3 = load_stl_fast(os.path.join(out_dir, "phalanx3_distal_open.stl"))
f_straight = load_stl_fast(os.path.join(out_dir, "full_finger_assembly_straight.stl"), max_facets=4000)
f_flexed = load_stl_fast(os.path.join(out_dir, "full_finger_assembly_flexed.stl"), max_facets=4000)

print(f"Đã nạp xong: P1={len(f_p1)}, P2={len(f_p2)}, P3={len(f_p3)}, Straight={len(f_straight)}, Flexed={len(f_flexed)}")

fig = plt.figure(figsize=(18, 13), facecolor='#0b1120')
fig.suptitle("HỆ THỐNG GĂNG TAY 3 ĐỐT NGUYÊN KHỐI PRINT-IN-PLACE V3.4 (CẢI TIẾN TRIỆT ĐỂ)\n(Móc Gài Bậc Thang 4 Nấc Theo Cung Xoay + Khớp Liên Đốt Xỏ Chốt Tự Khóa Rời / Ốc M3 + Bản Lề 0.75mm + Hốc Velostat 9.8x7.1mm)", 
             fontsize=12, fontweight='bold', color='#f8fafc', y=0.97)

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

# View 1: 3 Đốt in rời dạng Print-in-Place mở -90 độ
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
style_ax(ax1, "1. BỘ 3 ĐỐT IN RỜI PRINT-IN-PLACE (MỞ -90°, ZERO OVERHANG)\n- Đốt 1 (Ø23.6mm) | Đốt 2 (Ø21.6mm) | Đốt 3 (Ø19.6mm) Hở đầu thoáng khí")
p1_shift = f_p1.copy(); p1_shift[:,:,0] -= 32
p3_shift = f_p3.copy(); p3_shift[:,:,0] += 32
col_p1 = Poly3DCollection(p1_shift, facecolors='#3b82f6', edgecolors='#1d4ed8', linewidths=0.1, alpha=0.9)
col_p2 = Poly3DCollection(f_p2, facecolors='#10b981', edgecolors='#047857', linewidths=0.1, alpha=0.9)
col_p3 = Poly3DCollection(p3_shift, facecolors='#f59e0b', edgecolors='#b45309', linewidths=0.1, alpha=0.9)
ax1.add_collection3d(col_p1)
ax1.add_collection3d(col_p2)
ax1.add_collection3d(col_p3)
all_p = np.vstack([p1_shift.reshape(-1,3), f_p2.reshape(-1,3), p3_shift.reshape(-1,3)])
ax1.set_xlim(all_p[:,0].min()-2, all_p[:,0].max()+2)
ax1.set_ylim(all_p[:,1].min()-2, all_p[:,1].max()+2)
ax1.set_zlim(all_p[:,2].min()-2, all_p[:,2].max()+2)
ax1.view_init(elev=24, azim=-65)

# View 2: Lắp ráp hoàn chỉnh 3 đốt ở tư thế duỗi thẳng 0 độ (Straight 0°)
ax2 = fig.add_subplot(2, 2, 2, projection='3d')
style_ax(ax2, "2. CỤM LẮP RÁP DUỖI THẲNG 0° (KHỚP NỐI 0 LỰC CẢN + CHỐT XỎ TỰ KHÓA)\n- Đốt 2 trượt nhẹ vào Đốt 1 (khe 0.3mm) + Xỏ chốt Snap-Pin/Ốc M3 qua 5 lỗ chỉnh chiều dài")
col2 = Poly3DCollection(f_straight, facecolors='#0ea5e9', edgecolors='#0284c7', linewidths=0.12, alpha=0.9)
ax2.add_collection3d(col2)
all_s = f_straight.reshape(-1, 3)
ax2.set_xlim(all_s[:,0].min()-2, all_s[:,0].max()+2)
ax2.set_ylim(all_s[:,1].min()-2, all_s[:,1].max()+2)
ax2.set_zlim(all_s[:,2].min()-2, all_s[:,2].max()+2)
ax2.view_init(elev=22, azim=130)

# View 3: Lắp ráp hoàn chỉnh 3 đốt ở tư thế gập ôm nắm vật thể 45° (Flexed Grasping)
ax3 = fig.add_subplot(2, 2, 3, projection='3d')
style_ax(ax3, "3. CỤM LẮP RÁP CO GẬP ÔM NẮM 45° (CỬ ĐỘNG GIẢI PHẪU TỰ NHIÊN)\n- Khớp xoay trơn tru quanh trục xỏ, không cong vênh nạng kẹp, khuyên luồn gân mu ngón")
col3 = Poly3DCollection(f_flexed, facecolors='#a855f7', edgecolors='#7e22ce', linewidths=0.12, alpha=0.9)
ax3.add_collection3d(col3)
all_fl = f_flexed.reshape(-1, 3)
ax3.set_xlim(all_fl[:,0].min()-2, all_fl[:,0].max()+2)
ax3.set_ylim(all_fl[:,1].min()-2, all_fl[:,1].max()+2)
ax3.set_zlim(all_fl[:,2].min()-2, all_fl[:,2].max()+2)
ax3.view_init(elev=18, azim=110)

# View 4: Cận cảnh Móc Gài Bậc Thang (Hook-and-Ladder Clasp) & Hốc Velostat
ax4 = fig.add_subplot(2, 2, 4, projection='3d')
style_ax(ax4, "4. CẬN CẢNH MÓC GÀI BẬC THANG & ĐẾ VELOSTAT (HOOK CLASP & SENSOR)\n- Móc gài tự động ăn khớp 4 bậc thang theo cung xoay + Tai gạt tháo 0.1s + Hốc Velostat 9.8x7.1mm")
col4 = Poly3DCollection(f_straight, facecolors='#10b981', edgecolors='#047857', linewidths=0.15, alpha=0.92)
ax4.add_collection3d(col4)
ax4.set_xlim(-18, 22)
ax4.set_ylim(-16, 16)
ax4.set_zlim(0, 22)
ax4.view_init(elev=-25, azim=-45)

plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig(fig_out, dpi=180, facecolor=fig.get_facecolor(), edgecolor='none')
print(f"Ảnh kết xuất 3 đốt đã lưu tại: {fig_out}")
