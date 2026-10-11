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

sys.path.append(r'd:\Desktop\AI Agent\smart-glove-hand-function-monitoring\3d_model')
import generate_lateral_snap_finger as gen

d1, a1, p1_open, p1_closed = gen.build_phalanx_lateral_snap(
    r_in=11.8, length_z=16.0, is_distal=False, has_front_joint=True, has_rear_joint=False,
    num_length_steps=3, step_pitch=2.5, r_in_mate=10.8
)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7), facecolor='#0b1120')

def plot_slice(ax, d_shape, a_shape, title, a_angle_deg=0):
    ax.set_facecolor('#0f172a')
    ax.set_title(title, fontsize=11, fontweight='bold', color='#38bdf8', pad=10)
    
    hx = -(11.8 + 2.0 + 0.5)
    hy = -2.2
    a_rot = a_shape.copy()
    if a_angle_deg != 0:
        a_rot.rotate(FreeCAD.Vector(hx, hy, 0), FreeCAD.Vector(0,0,1), a_angle_deg)
        
    z0 = 8.0 # Mặt cắt ngang chính giữa đốt ngón Z = 8.0mm
    sec_d = d_shape.slice(FreeCAD.Vector(0,0,1), z0)
    sec_a = a_rot.slice(FreeCAD.Vector(0,0,1), z0)
    
    for comp in sec_d:
        for e in comp.Edges:
            pts = e.discretize(25)
            ax.plot([p.x for p in pts], [p.y for p in pts], color='#38bdf8', lw=2.0)
            
    for comp in sec_a:
        for e in comp.Edges:
            pts = e.discretize(25)
            ax.plot([p.x for p in pts], [p.y for p in pts], color='#f59e0b', lw=2.0)
            
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.25, color='#334155')
    ax.tick_params(colors='#64748b')
    ax.set_xlim(11, 20)
    ax.set_ylim(-3, 11)

# Subplot 1: Khi ngàm mở -10 độ đang tiến vào gài
plot_slice(ax1, d1, a1, "1. GÓC XOAY -10°: RĂNG TIẾN VÀO THEO MẶT DỐC 35°\n(Màu xanh: Rãnh cái Mu | Màu vàng: Răng đực Bụng + Dầm đàn hồi)", a_angle_deg=-10)
ax1.annotate('Mặt dốc 35° đón răng\ntrượt êm ái', xy=(15.5, 0.5), xytext=(12.0, 4.0),
             color='#38bdf8', fontsize=9, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=1.5))
ax1.annotate('Dầm đàn hồi nhún ra\nkhi leo đỉnh răng', xy=(17.5, 1.0), xytext=(17.0, 6.0),
             color='#f59e0b', fontsize=9, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#f59e0b', lw=1.5))

# Subplot 2: Khi ngàm đóng danh định 0 độ đã khóa chặt
plot_slice(ax2, d1, a1, "2. GÓC XOAY 0°: ĂN KHỚP HOÀN HẢO TẠI NẤC DANH ĐỊNH\n(Răng đực lọt trọn 100% vào túi rãnh cái, mặt khóa 90° hãm chống tuột)", a_angle_deg=0)
ax2.annotate('Mặt khóa 90° áp sát\nchống bung ngược', xy=(15.2, 0.5), xytext=(12.0, 2.5),
             color='#10b981', fontsize=9, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#10b981', lw=1.5))
ax2.annotate('Khe hở dung sai 0.15mm\nchuẩn in 3D FDM', xy=(15.0, 1.2), xytext=(11.5, 6.0),
             color='#38bdf8', fontsize=9, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=1.5))
ax2.annotate('Tai gạt mở ngàm tiện dụng\n(Thumb release tab)', xy=(18.5, 8.5), xytext=(12.5, 9.5),
             color='#f59e0b', fontsize=9, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#f59e0b', lw=1.5))

plt.tight_layout()
fig_out = r'C:\Users\user\.gemini\antigravity-ide\brain\db0fa2d1-bc0a-41c8-87e6-b71131f46734\clasp_mating_simulation.png'
plt.savefig(fig_out, dpi=180, facecolor=fig.get_facecolor(), edgecolor='none')
print(f"Mô phỏng mặt cắt ăn khớp đã lưu tại: {fig_out}")
