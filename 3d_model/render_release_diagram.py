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
import matplotlib.patches as patches

fig_out = r"C:\Users\user\.gemini\antigravity-ide\brain\db0fa2d1-bc0a-41c8-87e6-b71131f46734\release_mechanism_diagram.png"

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7.5), facecolor='#0b1120')
fig.suptitle("CƠ CHẾ KHÓA CHẮC CHẮN & THÁO NHANH 1 CHẠM (QUICK-RELEASE MECHANISM)\n(Cơ cấu mềm Compliant Lever - Thao tác tháo găng tay trong 1 giây cực kỳ dễ dàng)", 
             fontsize=13, fontweight='bold', color='#f8fafc', y=0.97)

def draw_schematic(ax, mode="locked"):
    ax.set_facecolor('#0f172a')
    ax.set_xlim(-2, 22)
    ax.set_ylim(-6, 16)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.2, color='#334155')
    ax.tick_params(colors='#64748b', labelsize=8)
    
    # 1. Vách trong của Họng khóa (Gắn vào máng mu ngón)
    rect_inner = patches.Rectangle((0, -3), 2.0, 15, facecolor='#1e293b', edgecolor='#38bdf8', lw=2.0)
    ax.add_patch(rect_inner)
    ax.text(1.0, 4.5, "VÁCH TRONG\n(Mu ngón)", color='#94a3b8', fontsize=8, ha='center', va='center', rotation=90)
    
    # 2. Khe trượt (Rãnh thông suốt X = 2.0 đến 4.5)
    # Đường hầm thông suốt từ dưới lên trên
    
    # 3. Dải răng đực (Palmar Ratchet Rack)
    rack_x = 2.4
    rack_w = 1.6
    rect_rack = patches.Rectangle((rack_x, -5), rack_w, 18, facecolor='#d97706', edgecolor='#f59e0b', lw=1.8, alpha=0.9)
    ax.add_patch(rect_rack)
    
    # Răng đực tam giác (6 răng)
    P = 2.0
    for i in range(6):
        y_t = -1.0 + i * P
        pts = [(rack_x + rack_w, y_t), 
               (rack_x + rack_w + 1.1, y_t), 
               (rack_x + rack_w, y_t + 1.6)]
        tri = patches.Polygon(pts, facecolor='#f59e0b', edgecolor='#b45309', lw=1.2)
        ax.add_patch(tri)
        
    ax.text(rack_x + rack_w/2, -3.5, "DẢI RĂNG ĐỰC (BỤNG NGÓN)", color='#fef3c7', fontsize=8, ha='center', va='center', rotation=90, fontweight='bold')
    
    # 4. Vách ngoài & Lẫy khóa đàn hồi (Compliant Lever)
    x_outer = 5.6
    w_outer = 1.6
    
    if mode == "locked":
        ax.set_title("1. TRẠNG THÁI KHÓA CHẮC CHẮN (LOCKED)\n- Mặt răng 90° khóa chết, co duỗi ngón tay không thể tuột\n- Đầu dải răng đâm xuyên thấu qua cửa trên tự do", 
                     fontsize=11, fontweight='bold', color='#10b981', pad=10)
        
        # Răng khóa cái ăn sâu vào răng đực
        y_lock = 3.0
        pawl_pts = [(x_outer, y_lock),
                    (x_outer - 1.1, y_lock),
                    (x_outer, y_lock + 1.6)]
        pawl = patches.Polygon(pawl_pts, facecolor='#10b981', edgecolor='#059669', lw=1.5)
        ax.add_patch(pawl)
        
        # Dầm đàn hồi ở vị trí cân bằng
        rect_beam = patches.Rectangle((x_outer, -3), w_outer, 15, facecolor='#1e293b', edgecolor='#10b981', lw=2.0)
        ax.add_patch(rect_beam)
        
        # Tai mở nhanh
        tab_x = x_outer + w_outer
        rect_tab = patches.Rectangle((tab_x, 1.5), 3.5, 5.0, facecolor='#047857', edgecolor='#34d399', lw=1.8)
        ax.add_patch(rect_tab)
        # Khía nhám
        for k in range(3):
            ax.plot([tab_x + 3.5, tab_x + 3.5], [2.2 + k*1.3, 3.0 + k*1.3], color='#a7f3d0', lw=2.5)
            
        ax.text(tab_x + 1.7, 4.0, "TAI BẨY\nNHẢ KHÓA", color='#ecfdf5', fontsize=8, ha='center', va='center', fontweight='bold')
        
        # Mũi tên chỉ lực khóa
        ax.annotate('Mặt khóa 90°\nôm khít 100%', xy=(x_outer - 0.5, y_lock), xytext=(x_outer - 3.5, y_lock - 3.5),
                    color='#34d399', fontsize=9, fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color='#34d399', lw=1.8))
        
        ax.annotate('Đầu dải răng đâm xuyên\nra ngoài cổng trên', xy=(rack_x + 0.8, 12.0), xytext=(6.0, 13.5),
                    color='#38bdf8', fontsize=9, fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=1.8))
                    
    else: # mode == "unlocked"
        ax.set_title("2. THAO TÁC THÁO NHANH 1 CHẠM (QUICK-RELEASE IN 1s)\n- Dùng ngón cái gạt nhẹ tai bẩy ra ngoài (~1.0mm, lực 3N)\n- Răng nhấc bổng khỏi rãnh, rút nhẹ dải răng ra ngoài dễ dàng", 
                     fontsize=11, fontweight='bold', color='#f59e0b', pad=10)
        
        # Dầm đàn hồi bị uốn cong ra ngoài sang phải (+X)
        delta_x = 1.8
        y_lock = 3.0
        pawl_pts = [(x_outer + delta_x, y_lock),
                    (x_outer + delta_x - 1.1, y_lock),
                    (x_outer + delta_x, y_lock + 1.6)]
        pawl = patches.Polygon(pawl_pts, facecolor='#ef4444', edgecolor='#b91c1c', lw=1.5)
        ax.add_patch(pawl)
        
        rect_beam = patches.Rectangle((x_outer + delta_x, -3), w_outer, 15, facecolor='#1e293b', edgecolor='#ef4444', lw=2.0)
        ax.add_patch(rect_beam)
        
        tab_x = x_outer + w_outer + delta_x
        rect_tab = patches.Rectangle((tab_x, 1.5), 3.5, 5.0, facecolor='#b91c1c', edgecolor='#f87171', lw=1.8)
        ax.add_patch(rect_tab)
        for k in range(3):
            ax.plot([tab_x + 3.5, tab_x + 3.5], [2.2 + k*1.3, 3.0 + k*1.3], color='#fecaca', lw=2.5)
            
        ax.text(tab_x + 1.7, 4.0, "TAI BẨY\nĐÃ GẠT", color='#fff', fontsize=8, ha='center', va='center', fontweight='bold')
        
        # Mũi tên ngón tay ấn / gạt
        ax.annotate('NGÓN CÁI GẠT NHẸ SANG PHẢI\n(Lực ấn ~3N như phím cơ)', xy=(tab_x + 3.5, 4.0), xytext=(tab_x + 5.0, 4.0),
                    color='#f87171', fontsize=9, fontweight='bold',
                    arrowprops=dict(arrowstyle='<-', color='#f87171', lw=2.5))
        
        # Khoảng hở giải phóng
        ax.annotate('KHE HỞ GIẢI PHÓNG:\nRăng nhấc ra hoàn toàn!', xy=(x_outer + 0.3, y_lock + 0.8), xytext=(x_outer - 5.5, y_lock + 2.5),
                    color='#fbbf24', fontsize=9, fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color='#fbbf24', lw=1.8))
        
        # Mũi tên rút dây ra
        ax.annotate('RÚT DẢI RĂNG RA NGOÀI\n(Trượt tự do không cấn)', xy=(rack_x + 0.8, -4.0), xytext=(rack_x + 0.8, -7.5),
                    color='#38bdf8', fontsize=10, fontweight='bold', ha='center',
                    arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=2.5))

draw_schematic(ax1, mode="locked")
draw_schematic(ax2, mode="unlocked")

plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig(fig_out, dpi=180, facecolor=fig.get_facecolor(), edgecolor='none')
print(f"Đã lưu sơ đồ hướng dẫn tháo khóa tại: {fig_out}")
