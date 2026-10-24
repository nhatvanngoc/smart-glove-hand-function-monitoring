import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import numpy as np
import os

FIGURES_DIR = r'd:\Desktop\AI Agent\smart-glove-hand-function-monitoring\de_cuong\figures'
DOWNLOADS_DIR = r'C:\Users\user\Downloads'
ASSETS_DIR = os.path.join(FIGURES_DIR, 'assets')

# Kích thước khung hình Landscape 16:9 chuẩn cực lớn (18.2 in x 10.2 in @ 350 DPI = 6370 x 3570 px)
fig, ax = plt.subplots(figsize=(18.2, 10.2), dpi=350)
fig.patch.set_facecolor('#FFFFFF')
ax.set_facecolor('#FFFFFF')

# Khung tọa độ chuẩn [0, 100] x [0, 100]
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Cài đặt font chữ chuẩn
plt.rcParams['font.sans-serif'] = ['Arial', 'Segoe UI', 'DejaVu Sans']

# ==================== TIÊU ĐỀ SƠ ĐỒ CHUẨN KHOA HỌC ====================
ax.text(50.0, 97.2, "Hình 4. Sơ đồ khối kết nối hệ thống kiến trúc phân tán",
        ha='center', va='center', fontsize=22, fontweight='bold', color='#0F172A')
ax.text(50.0, 94.0, "Sơ đồ đấu nối và luồng tương tác giữa 4 tầng: Thiết bị đeo – Mạch DSP – Thị giác 3D – Phản hồi trực quan",
        ha='center', va='center', fontsize=13.5, color='#475569')

# Hàm vẽ khung nét đứt bo góc chuẩn BCTT
def draw_dashed_box(x, y, w, h, title, subtitle="", header_color='#0F172A', bg_color='#FFFFFF'):
    box = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.7,rounding_size=1.6",
        linestyle=(0, (6, 4)),
        linewidth=2.2,
        edgecolor='#1E293B',
        facecolor=bg_color,
        zorder=1
    )
    ax.add_patch(box)
    
    ax.text(x + w / 2, y + h - 2.2, title,
            ha='center', va='top',
            fontsize=15, fontweight='bold', color=header_color,
            zorder=2)
    if subtitle:
        ax.text(x + w / 2, y + h - 5.0, subtitle,
                ha='center', va='top',
                fontsize=11.5, color='#64748B', style='italic',
                zorder=2)

# Hàm đặt ảnh linh kiện với zoom chuẩn
def place_image(path, x, y, zoom=1.0, zorder=3):
    img = Image.open(path)
    im_box = OffsetImage(img, zoom=zoom)
    ab = AnnotationBbox(im_box, (x, y), frameon=False, zorder=zorder)
    ax.add_artist(ab)
    return ab

# ==================== 1. KHỐI TRÁI: TẦNG 1 — THIẾT BỊ ĐEO & TRỢ LỰC ====================
draw_dashed_box(2.5, 12.0, 26.0, 78.0, "TẦNG 1: THIẾT BỊ ĐEO & TRỢ LỰC", "Găng nẹp 3 ngón & Cụm 3 Servo")
# Ảnh nẹp bàn tay siêu sạch
place_image(os.path.join(ASSETS_DIR, 'ultra_clean_hand.png'), 15.5, 52.0, zoom=0.44)
# Chú thích linh kiện tầng 1
ax.text(15.5, 23.5, "• 16 Ô Velostat vi sai lòng - mu", ha='center', va='center', fontsize=13.0, fontweight='bold', color='#1E293B')
ax.text(15.5, 19.5, "• 3 Cảm biến góc uốn Flex", ha='center', va='center', fontsize=12.5, fontweight='bold', color='#047857')
ax.text(15.5, 15.5, "• 3 Động cơ Servo kéo cáp Bowden", ha='center', va='center', fontsize=12.5, fontweight='bold', color='#2563EB')

# ==================== 2. KHỐI GIỮA - TRÊN: TẦNG 3 — THỊ GIÁC 3D ĐÓN TRƯỚC ====================
draw_dashed_box(32.5, 54.0, 38.5, 36.0, "TẦNG 3: THỊ GIÁC 3D ĐÓN TRƯỚC", "Ước lượng độ sâu Depth Anything V2")

# Camera RGB
place_image(os.path.join(ASSETS_DIR, 'pristine_cam.png'), 38.5, 72.0, zoom=0.46)
ax.text(38.5, 60.5, "Camera RGB", ha='center', va='center', fontsize=12.5, fontweight='bold', color='#1E293B')
ax.text(38.5, 57.0, "(Thu nhận cảnh 3D)", ha='center', va='center', fontsize=10.5, color='#64748B')

# Mũi tên từ Camera sang Depth Map
ax.annotate('', xy=(47.5, 72.0), xytext=(43.0, 72.0),
            arrowprops=dict(arrowstyle="-|>", lw=2.4, color='#1E293B', mutation_scale=16), zorder=4)

# Depth Map 3D
place_image(os.path.join(ASSETS_DIR, 'pristine_depth.png'), 52.0, 72.0, zoom=0.44)
ax.text(52.0, 60.5, "Depth Map 3D", ha='center', va='center', fontsize=12.5, fontweight='bold', color='#1E293B')
ax.text(52.0, 57.0, "(Depth Anything V2)", ha='center', va='center', fontsize=10.5, color='#64748B')

# Mũi tên từ Depth Map sang Orange Pi
ax.annotate('', xy=(60.5, 72.0), xytext=(56.5, 72.0),
            arrowprops=dict(arrowstyle="-|>", lw=2.4, color='#1E293B', mutation_scale=16), zorder=4)

# Orange Pi 5 Pro
place_image(os.path.join(ASSETS_DIR, 'pristine_opi.png'), 65.5, 72.0, zoom=0.46)
ax.text(65.5, 60.5, "Orange Pi 5 Pro", ha='center', va='center', fontsize=12.5, fontweight='bold', color='#1E293B')
ax.text(65.5, 57.0, "(NPU 6 TOPS · Xử lý TTC)", ha='center', va='center', fontsize=10.5, color='#64748B')

# ==================== 3. KHỐI GIỮA - DƯỚI: TẦNG 2 — THU THẬP & XỬ LÝ DSP ====================
draw_dashed_box(32.5, 12.0, 38.5, 36.5, "TẦNG 2: THU THẬP & XỬ LÝ DSP", "21 Kênh cảm biến & Thuật toán AAN")

# 2x MUX CD74HC4067
place_image(os.path.join(ASSETS_DIR, 'pristine_mux.png'), 38.5, 30.5, zoom=0.52)
ax.text(38.5, 19.5, "2x CD74HC4067", ha='center', va='center', fontsize=12.5, fontweight='bold', color='#1E293B')
ax.text(38.5, 16.0, "(Dồn 21 kênh tương tự)", ha='center', va='center', fontsize=10.5, color='#64748B')

# Mũi tên từ MUX sang ADS1115
ax.annotate('', xy=(47.5, 30.5), xytext=(43.0, 30.5),
            arrowprops=dict(arrowstyle="-|>", lw=2.4, color='#1E293B', mutation_scale=16), zorder=4)

# ADS1115 ADC
place_image(os.path.join(ASSETS_DIR, 'pristine_ads.png'), 52.0, 30.5, zoom=0.54)
ax.text(52.0, 19.5, "ADS1115 PGA", ha='center', va='center', fontsize=12.5, fontweight='bold', color='#1E293B')
ax.text(52.0, 16.0, "(ADC 16-bit · Dải 0-3.3V)", ha='center', va='center', fontsize=10.5, color='#64748B')

# Mũi tên 2 chiều giữa ADS1115 và ESP32 (I2C)
ax.annotate('', xy=(61.0, 30.5), xytext=(56.5, 30.5),
            arrowprops=dict(arrowstyle="<|-|>", lw=2.4, color='#1E293B', mutation_scale=16), zorder=4)
ax.text(58.8, 32.5, "I2C", ha='center', va='center', fontsize=10.0, fontweight='bold', color='#2563EB')

# ESP32-S3
place_image(os.path.join(ASSETS_DIR, 'esp_rot90.png'), 65.5, 30.5, zoom=0.42)
ax.text(65.5, 19.5, "ESP32-S3 Dual-Core", ha='center', va='center', fontsize=12.5, fontweight='bold', color='#1E293B')
ax.text(65.5, 16.0, "(DSP 2 nhánh · Điều khiển AAN)", ha='center', va='center', fontsize=10.5, color='#64748B')

# ==================== 4. KHỐI PHẢI: TẦNG 4 — PHẢN HỒI THỊ GIÁC & TÁC VỤ ====================
draw_dashed_box(74.5, 12.0, 23.0, 78.0, "TẦNG 4: PHẢN HỒI THỊ GIÁC", "Giao diện Dashboard & Vỏ não")

# Màn hình Dashboard
place_image(os.path.join(ASSETS_DIR, 'pristine_mon.png'), 86.0, 68.0, zoom=0.50)
ax.text(86.0, 52.5, "Dashboard thời gian thực", ha='center', va='center', fontsize=13.0, fontweight='bold', color='#1E293B')
ax.text(86.0, 49.0, "Hiển thị bộ chỉ số EI – GAP – RAL", ha='center', va='center', fontsize=11.0, color='#2563EB', fontweight='bold')

# Vỏ não vận động (Sensory-Motor Cortex)
place_image(os.path.join(ASSETS_DIR, 'pristine_brain.png'), 86.0, 29.0, zoom=0.48)
ax.text(86.0, 16.0, "Vỏ não vận động (Cortex)", ha='center', va='center', fontsize=13.0, fontweight='bold', color='#1E293B')

# Cặp mũi tên cong tròn phản hồi sinh học 2 chiều giữa Dashboard và Não bộ
arc_down = patches.FancyArrowPatch(
    (79.0, 46.5), (79.0, 34.5),
    connectionstyle="arc3,rad=-0.38",
    arrowstyle="-|>",
    lw=2.6, color='#2563EB',
    mutation_scale=18,
    zorder=5
)
ax.add_patch(arc_down)
ax.text(75.5, 40.5, "Phản hồi\nthị giác", ha='center', va='center', fontsize=10.0, fontweight='bold', color='#2563EB')

arc_up = patches.FancyArrowPatch(
    (93.0, 34.5), (93.0, 46.5),
    connectionstyle="arc3,rad=-0.38",
    arrowstyle="-|>",
    lw=2.6, color='#047857',
    mutation_scale=18,
    zorder=5
)
ax.add_patch(arc_up)
ax.text(96.5, 40.5, "Nỗ lực\nchủ động", ha='center', va='center', fontsize=10.0, fontweight='bold', color='#047857')

# ==================== CÁC ĐƯỜNG KẾT NỐI LIÊN TẦNG (INTER-TIER CONNECTIONS) ====================

# 1. Đường truyền tín hiệu cảm biến từ Tầng 1 sang Tầng 2 (MUX)
ax.annotate('', xy=(32.5, 33.5), xytext=(28.5, 33.5),
            arrowprops=dict(arrowstyle="-|>", lw=2.8, color='#1E293B', mutation_scale=18), zorder=6)
ax.text(30.5, 36.0, "21 Kênh\ntương tự", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#1E293B',
        bbox=dict(boxstyle="round,pad=0.2", fc="#FFFFFF", ec="#CBD5E1", lw=1.0))

# 2. Đường điều khiển xung PWM Servo từ ESP32-S3 về 3 Động cơ Servo ở cổ tay
# Đường uốn khúc chữ U vuông góc chạy ngang qua khe giữa Tầng 1 và 2
ax.plot([65.5, 65.5, 30.5, 30.5, 25.5], [22.0, 13.5, 13.5, 23.5, 23.5],
        color='#DC2626', lw=2.6, zorder=6)
ax.annotate('', xy=(23.5, 23.5), xytext=(25.5, 23.5),
            arrowprops=dict(arrowstyle="-|>", lw=2.6, color='#DC2626', mutation_scale=18), zorder=6)
ax.text(48.0, 13.5, "Lệnh xung PWM điều khiển 3 Servo (Hỗ trợ kéo gập AAN)",
        ha='center', va='center', fontsize=11.0, fontweight='bold', color='#DC2626',
        bbox=dict(boxstyle="round,pad=0.25", fc="#FEF2F2", ec="#DC2626", lw=1.1))

# 3. Giao tiếp 2 chiều tốc độ cao giữa ESP32-S3 và Orange Pi 5 Pro (UART / USB)
ax.annotate('', xy=(65.5, 54.0), xytext=(65.5, 48.5),
            arrowprops=dict(arrowstyle="<|-|>", lw=3.0, color='#2563EB', mutation_scale=20), zorder=6)
ax.text(65.5, 51.2, "UART / USB (Đồng bộ EI·GAP·RAL ↔ TTC)",
        ha='center', va='center', fontsize=10.5, fontweight='bold', color='#2563EB',
        bbox=dict(boxstyle="round,pad=0.25", fc="#EFF6FF", ec="#2563EB", lw=1.1))

# 4. Xuất tín hiệu HDMI / Video từ Orange Pi 5 Pro sang Màn hình Dashboard
ax.annotate('', xy=(74.5, 72.0), xytext=(71.0, 72.0),
            arrowprops=dict(arrowstyle="-|>", lw=2.8, color='#1E293B', mutation_scale=18), zorder=6)
ax.text(72.8, 74.5, "HDMI / Video", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#1E293B',
        bbox=dict(boxstyle="round,pad=0.2", fc="#FFFFFF", ec="#CBD5E1", lw=1.0))

# 5. Vòng phản hồi thần kinh - cơ học khép kín từ Vỏ não về Bàn tay người bệnh (Bottom Lane)
lane_bottom_y = 5.0
# Từ đáy Tầng 4 (86.0, 12.0) -> xuống (86.0, 5.0) -> sang trái (15.5, 5.0) -> lên (15.5, 12.0)
ax.plot([86.0, 86.0], [12.0, lane_bottom_y], color='#4338CA', lw=2.8, linestyle=(0, (6, 4)), zorder=6)
ax.plot([86.0, 15.5], [lane_bottom_y, lane_bottom_y], color='#4338CA', lw=2.8, linestyle=(0, (6, 4)), zorder=6)
ax.annotate('', xy=(15.5, 12.0), xytext=(15.5, lane_bottom_y),
            arrowprops=dict(arrowstyle="-|>", lw=2.8, color='#4338CA', linestyle=(0, (6, 4)), mutation_scale=20), zorder=6)

# Badge chính giữa lane đáy
bio_badge = patches.FancyBboxPatch(
    (24.0, lane_bottom_y - 2.6), 52.0, 5.2,
    boxstyle="round,pad=0.3,rounding_size=1.2",
    linewidth=2.0, edgecolor='#4338CA', facecolor='#EEF2FF', zorder=7
)
ax.add_patch(bio_badge)

# Mũi tên vector chỉ hướng bên trong badge
ax.annotate('', xy=(26.0, lane_bottom_y), xytext=(29.0, lane_bottom_y),
            arrowprops=dict(arrowstyle="-|>", lw=2.4, color='#4338CA', mutation_scale=16), zorder=8)
ax.annotate('', xy=(71.0, lane_bottom_y), xytext=(74.0, lane_bottom_y),
            arrowprops=dict(arrowstyle="-|>", lw=2.4, color='#4338CA', mutation_scale=16), zorder=8)

ax.text(50.0, lane_bottom_y, "Vòng phản hồi thần kinh – vận động khép kín (Bio-feedback Closed Loop)",
        ha='center', va='center', fontsize=12.5, fontweight='bold', color='#3730A3', zorder=8)

# Xuất ảnh chất lượng cao 350 DPI
plt.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
dst_downloads = os.path.join(DOWNLOADS_DIR, 'Hinh4_So_do_khoi_ket_noi_4_tang_LANDSCAPE.png')
dst_figures = os.path.join(FIGURES_DIR, 'hinh4_kien_truc_phan_tan_kenh_hinh-1.png')

plt.savefig(dst_downloads, dpi=350, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight', pad_inches=0.2)
plt.savefig(dst_figures, dpi=350, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight', pad_inches=0.2)
plt.close()

print('Saved successfully to:')
print('1.', dst_downloads)
print('2.', dst_figures)
im = Image.open(dst_downloads)
print('Output Dimensions:', im.size)
