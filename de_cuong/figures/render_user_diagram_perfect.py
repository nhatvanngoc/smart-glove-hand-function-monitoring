import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import numpy as np
import os

FIGURES_DIR = r'd:\Desktop\AI Agent\smart-glove-hand-function-monitoring\de_cuong\figures'
DOWNLOADS_DIR = r'C:\Users\user\Downloads'
ASSETS_DIR = os.path.join(FIGURES_DIR, 'assets')

# Kích thước khung hình 16:9 độ phân giải cao (16 inch x 9.5 inch @ 300 DPI = 4800 x 2850 px)
fig, ax = plt.subplots(figsize=(16.8, 10.0), dpi=300)
fig.patch.set_facecolor('#FFFFFF')
ax.set_facecolor('#FFFFFF')

# Khung tọa độ chuẩn [0, 100] x [0, 100]
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Font family
plt.rcParams['font.sans-serif'] = ['Arial', 'Segoe UI', 'DejaVu Sans']

# Hàm vẽ khung nét đứt bo góc chuẩn
def draw_dashed_box(x, y, w, h, label=""):
    box = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.8,rounding_size=1.8",
        linestyle=(0, (6, 4)),
        linewidth=2.2,
        edgecolor='#1E293B',
        facecolor='#FFFFFF',
        zorder=1
    )
    ax.add_patch(box)
    if label:
        ax.text(x + w / 2, y + h - 1.2, label,
                ha='center', va='top',
                fontsize=18, fontweight='bold', color='#0F172A',
                zorder=2)

# Hàm đặt ảnh
def place_image(path, x, y, zoom=1.0, zorder=3):
    img = Image.open(path)
    im_box = OffsetImage(img, zoom=zoom)
    ab = AnnotationBbox(im_box, (x, y), frameon=False, zorder=zorder)
    ax.add_artist(ab)
    return ab

# ==================== 1. KHỐI TRÁI: GĂNG NẸP 3 NGÓN & 3 SERVO ====================
draw_dashed_box(3.5, 4.0, 31.0, 91.0, "Găng nẹp 3 ngón & 3 Servo")
place_image(os.path.join(ASSETS_DIR, 'clean_hand.png'), 19.0, 48.0, zoom=0.55)

# ==================== 2. KHỐI GIỮA - TRÊN: CAMERA RGB & THỊ GIÁC ====================
draw_dashed_box(37.5, 52.0, 38.0, 43.0, "Camera RGB")

# Ảnh Camera
place_image(os.path.join(ASSETS_DIR, 'clean_cam.png'), 44.5, 76.0, zoom=0.52)

# Mũi tên từ Camera sang Depth Map
ax.annotate('', xy=(66.5, 78.5), xytext=(51.0, 78.5),
            arrowprops=dict(arrowstyle="-|>", lw=2.5, color='#0F172A', mutation_scale=18),
            zorder=4)

# Ảnh Depth Map
place_image(os.path.join(ASSETS_DIR, 'clean_depth.png'), 70.0, 78.5, zoom=0.50)

# Mũi tên từ Camera xuống Orange Pi 5 Pro
ax.annotate('', xy=(64.5, 62.0), xytext=(51.0, 73.0),
            arrowprops=dict(arrowstyle="-|>", lw=2.5, color='#0F172A', mutation_scale=18),
            zorder=4)

# Ảnh Orange Pi 5 Pro
place_image(os.path.join(ASSETS_DIR, 'clean_opi.png'), 69.5, 61.5, zoom=0.52)
ax.text(54.5, 61.5, "Orange Pi 5 Pro", ha='center', va='center',
        fontsize=14, fontweight='bold', color='#0F172A', zorder=4)

# ==================== 3. KHỐI GIỮA - DƯỚI: 21 KÊNH CẢM BIẾN & DSP ====================
draw_dashed_box(37.5, 4.0, 38.0, 45.0, "21 kênh cảm biến")

# Ảnh 2x CD74HC4067
place_image(os.path.join(ASSETS_DIR, 'clean_mux.png'), 43.5, 27.0, zoom=0.56)
ax.text(43.5, 14.5, "2x CD74HC4067", ha='center', va='center',
        fontsize=13, fontweight='bold', color='#0F172A', zorder=4)

# Mũi tên từ MUX sang ADS1115 (hai nhánh gom lại)
ax.annotate('', xy=(52.8, 26.5), xytext=(48.5, 30.5),
            arrowprops=dict(arrowstyle="-|>", lw=2.2, color='#0F172A', mutation_scale=15),
            zorder=4)
ax.annotate('', xy=(52.8, 26.5), xytext=(48.5, 22.5),
            arrowprops=dict(arrowstyle="-|>", lw=2.2, color='#0F172A', mutation_scale=15),
            zorder=4)

# Ảnh ADS1115
place_image(os.path.join(ASSETS_DIR, 'clean_ads.png'), 56.5, 26.5, zoom=0.55)
ax.text(56.5, 17.5, "ADS1115", ha='center', va='center',
        fontsize=13, fontweight='bold', color='#0F172A', zorder=4)

# Mũi tên 2 chiều giữa ADS1115 và ESP32-S3 (giao tiếp I2C)
ax.annotate('', xy=(67.5, 26.5), xytext=(61.5, 26.5),
            arrowprops=dict(arrowstyle="<|-|>", lw=2.2, color='#0F172A', mutation_scale=15),
            zorder=4)

# Ảnh ESP32-S3
place_image(os.path.join(ASSETS_DIR, 'clean_esp.png'), 71.5, 26.5, zoom=0.55)
ax.text(71.5, 15.5, "ESP32-S3", ha='center', va='center',
        fontsize=13, fontweight='bold', color='#0F172A', zorder=4)

# ==================== MŨI TÊN KẾT NỐI LIÊN KHỐI ====================

# 1. Hai chiều giữa Orange Pi 5 Pro và ESP32-S3 (Giao tiếp UART / USB)
ax.annotate('', xy=(69.5, 54.0), xytext=(69.5, 35.0),
            arrowprops=dict(arrowstyle="<|-|>", lw=3.0, color='#0F172A', mutation_scale=20),
            zorder=5)

# 2. Hai chiều giữa Khối Tay (cảm biến) và 2x MUX (dây dẫn tín hiệu)
ax.annotate('', xy=(39.0, 31.0), xytext=(34.5, 31.0),
            arrowprops=dict(arrowstyle="<|-|>", lw=2.6, color='#0F172A', mutation_scale=18),
            zorder=5)

# 3. Lệnh điều khiển từ Mạch về 3 Servo (đường uốn vuông góc sang cổ tay)
ax.plot([39.0, 33.0, 33.0, 26.0], [22.0, 22.0, 16.5, 16.5],
        color='#0F172A', lw=2.6, zorder=5)
ax.annotate('', xy=(24.5, 16.5), xytext=(26.0, 16.5),
            arrowprops=dict(arrowstyle="-|>", lw=2.6, color='#0F172A', mutation_scale=18),
            zorder=5)

# ==================== 4. KHỐI PHẢI: PHẢN HỒI THỊ GIÁC ====================
ax.text(88.0, 93.8, "Phản hồi thị giác", ha='center', va='top',
        fontsize=18, fontweight='bold', color='#0F172A', zorder=2)

# Màn hình Dashboard (EI - GAP - RAL)
place_image(os.path.join(ASSETS_DIR, 'clean_mon.png'), 88.0, 71.0, zoom=0.58)

# Não bộ / Vỏ não vận động (Sensory-Motor Cortex)
place_image(os.path.join(ASSETS_DIR, 'clean_brain.png'), 89.0, 24.0, zoom=0.55)

# Cặp mũi tên cong tròn phản hồi hai chiều giữa Màn hình và Não bộ
arc_down = patches.FancyArrowPatch(
    (81.0, 60.0), (81.0, 30.0),
    connectionstyle="arc3,rad=-0.42",
    arrowstyle="-|>",
    lw=2.8, color='#0F172A',
    mutation_scale=20,
    zorder=5
)
ax.add_patch(arc_down)

arc_up = patches.FancyArrowPatch(
    (96.5, 30.0), (96.5, 60.0),
    connectionstyle="arc3,rad=-0.42",
    arrowstyle="-|>",
    lw=2.8, color='#0F172A',
    mutation_scale=20,
    zorder=5
)
ax.add_patch(arc_up)

# Xuất ảnh chất lượng cao 350 DPI
plt.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
dst = os.path.join(DOWNLOADS_DIR, 'Hinh4_So_do_khoi_4_tang_LANDSCAPE_TO_RO.png')
plt.savefig(dst, dpi=350, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight', pad_inches=0.15)
plt.close()

print('Saved successfully to:', dst)
im_out = Image.open(dst)
print('Output Dimensions:', im_out.size)
