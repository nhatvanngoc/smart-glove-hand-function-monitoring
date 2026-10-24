import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import numpy as np
import os

FIGURES_DIR = r'd:\Desktop\AI Agent\smart-glove-hand-function-monitoring\de_cuong\figures'
DOWNLOADS_DIR = r'C:\Users\user\Downloads'
ASSETS_DIR = os.path.join(FIGURES_DIR, 'assets')

# Kích thước khung hình Landscape 16:9 cực lớn (18.2 in x 9.8 in @ 350 DPI = 6370 x 3430 px)
fig, ax = plt.subplots(figsize=(18.2, 9.8), dpi=350)
fig.patch.set_facecolor('#FFFFFF')
ax.set_facecolor('#FFFFFF')

# Khung tọa độ chuẩn [0, 100] x [0, 100]
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Cài đặt font chữ chuẩn
plt.rcParams['font.sans-serif'] = ['Arial', 'Segoe UI', 'DejaVu Sans']

# ==================== TIÊU ĐỀ SƠ ĐỒ CHUẨN KHOA HỌC ====================
ax.text(50.0, 96.5, "Hình 10. Chuỗi thu nhận tín hiệu và thuật toán tự cân chỉnh điểm 0",
        ha='center', va='center', fontsize=22, fontweight='bold', color='#0F172A')
ax.text(50.0, 93.0, "Chuỗi phần cứng thu nhận từ cảm biến ngón tay đến bộ chỉ số EI – GAP – RAL và vòng phản hồi bù trôi mốc tĩnh",
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

# ==================== 1. KHỐI 1: CẢM BIẾN VẬT LÝ & Ô THAM CHIẾU ====================
draw_dashed_box(2.5, 19.5, 17.0, 69.0, "1. CẢM BIẾN VẬT LÝ", "Găng nẹp ngón in 3D")
# Đặt ảnh nẹp bàn tay mang cảm biến đã khử sạch text
place_image(os.path.join(ASSETS_DIR, 'ultra_clean_hand.png'), 11.0, 56.5, zoom=0.36)
# Chú thích linh kiện khối 1
ax.text(11.0, 31.0, "• 16 Ô Velostat vi sai", ha='center', va='center', fontsize=12.5, fontweight='bold', color='#1E293B')
ax.text(11.0, 27.0, "• 2 Ô tham chiếu REF", ha='center', va='center', fontsize=12.5, fontweight='bold', color='#2563EB')
ax.text(11.0, 23.0, "• 3 Cảm biến uốn Flex", ha='center', va='center', fontsize=12.0, fontweight='bold', color='#047857')

# ==================== 2. KHỐI 2: CẦU PHÂN ÁP ====================
draw_dashed_box(22.5, 19.5, 15.0, 69.0, "2. CẦU PHÂN ÁP", "Chuyển đổi ΔR → ΔV")

# Vẽ sơ đồ mạch phân áp thu nhỏ bằng vector
# VCC
ax.plot([30.0, 30.0], [75.0, 71.0], color='#0F172A', lw=2.0, zorder=3)
ax.text(30.0, 76.5, "+3.3V (VCC)", ha='center', va='center', fontsize=11, fontweight='bold', color='#DC2626')
# Điện trở R_ref (hộp chữ nhật)
r_ref = patches.Rectangle((28.5, 63.5), 3.0, 7.5, linewidth=1.8, edgecolor='#0F172A', facecolor='#F8FAFC', zorder=3)
ax.add_patch(r_ref)
ax.text(30.0, 67.2, "R_ref\n10 kΩ", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#1E293B')
ax.text(32.8, 67.2, "(0.1%)", ha='left', va='center', fontsize=9.0, color='#64748B')

# Điểm đo V_analog giữa cầu
ax.plot([30.0, 30.0], [63.5, 56.5], color='#0F172A', lw=2.0, zorder=3)
ax.scatter([30.0], [60.0], s=65, color='#2563EB', zorder=4)
ax.plot([30.0, 35.5], [60.0, 60.0], color='#2563EB', lw=2.2, zorder=3)
ax.text(32.8, 62.2, "V_analog", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#2563EB')

# Điện trở màng Velostat (hộp có mũi tên biến thiên áp trở)
r_velo = patches.Rectangle((28.5, 49.0), 3.0, 7.5, linewidth=1.8, edgecolor='#0F172A', facecolor='#FEF3C7', zorder=3)
ax.add_patch(r_velo)
ax.text(30.0, 52.7, "Màng\nVelostat", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#B45309')
# Mũi tên biến thiên xuyên qua điện trở
ax.annotate('', xy=(32.5, 57.5), xytext=(27.5, 48.0),
            arrowprops=dict(arrowstyle="->", lw=1.6, color='#B45309'), zorder=4)

# GND
ax.plot([30.0, 30.0], [49.0, 44.5], color='#0F172A', lw=2.0, zorder=3)
ax.plot([28.0, 32.0], [44.5, 44.5], color='#0F172A', lw=2.0, zorder=3)
ax.plot([28.7, 31.3], [43.2, 43.2], color='#0F172A', lw=1.8, zorder=3)
ax.plot([29.3, 30.7], [41.9, 41.9], color='#0F172A', lw=1.5, zorder=3)
ax.text(30.0, 39.8, "GND", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#64748B')

# Chú thích khối 2
ax.text(30.0, 31.0, "Điện trở chuẩn 0,1%", ha='center', va='center', fontsize=11.5, fontweight='bold', color='#1E293B')
ax.text(30.0, 26.5, "ΔR → Tín hiệu 0 – 3.3V", ha='center', va='center', fontsize=11.5, color='#475569')

# ==================== 3. KHỐI 3: DỒN KÊNH 16:1 ====================
draw_dashed_box(40.5, 19.5, 15.0, 69.0, "3. DỒN KÊNH 16:1", "Quét 21 kênh tuần tự")
place_image(os.path.join(ASSETS_DIR, 'pristine_mux.png'), 48.0, 56.5, zoom=0.55)
ax.text(48.0, 33.5, "2x CD74HC4067", ha='center', va='center', fontsize=13.5, fontweight='bold', color='#1E293B')
ax.text(48.0, 29.0, "• Quét tuần tự 21 kênh", ha='center', va='center', fontsize=12.0, color='#334155')
ax.text(48.0, 25.0, "• Tần số quét ≥ 15 Hz", ha='center', va='center', fontsize=12.0, color='#334155')

# ==================== 4. KHỐI 4: SỐ HÓA ADC 16-BIT ====================
draw_dashed_box(58.5, 19.5, 15.0, 69.0, "4. ADC 16-BIT PGA", "Số hóa độ chính xác cao")
place_image(os.path.join(ASSETS_DIR, 'pristine_ads.png'), 66.0, 56.5, zoom=0.56)
ax.text(66.0, 33.5, "ADS1115 (PGA)", ha='center', va='center', fontsize=13.5, fontweight='bold', color='#1E293B')
ax.text(66.0, 29.0, "• Độ phân giải 16-bit", ha='center', va='center', fontsize=12.0, color='#334155')
ax.text(66.0, 25.0, "• Dải đo 0 – 3.300 mV", ha='center', va='center', fontsize=12.0, color='#334155')

# ==================== 5. KHỐI 5: ESP32-S3 & AUTO-ZERO ====================
draw_dashed_box(76.5, 19.5, 21.0, 69.0, "5. XỬ LÝ SỐ & ĐẦU RA", "ESP32-S3 Auto-zero")
place_image(os.path.join(ASSETS_DIR, 'esp_rot90.png'), 87.0, 67.5, zoom=0.48)
ax.text(87.0, 56.0, "ESP32-S3 (Dual-Core 240MHz)", ha='center', va='center', fontsize=12.5, fontweight='bold', color='#0F172A')

# Hộp mini hiển thị thuật toán Auto-zero
dsp_box = patches.FancyBboxPatch(
    (78.0, 36.0), 18.0, 16.0,
    boxstyle="round,pad=0.3,rounding_size=0.8",
    linewidth=1.2, edgecolor='#94A3B8', facecolor='#F1F5F9', zorder=2
)
ax.add_patch(dsp_box)
ax.text(87.0, 49.0, "THUẬT TOÁN AUTO-ZERO", ha='center', va='center', fontsize=11.0, fontweight='bold', color='#1E3A8A')
ax.text(87.0, 45.3, "V_base[k] = 0.998 V_base + 0.002 V_raw", ha='center', va='center', fontsize=9.2, fontweight='bold', color='#0369A1')
ax.text(87.0, 41.7, "F_clean = max(0, |V_raw - V_base| - 180mV)", ha='center', va='center', fontsize=9.2, fontweight='bold', color='#047857')
ax.text(87.0, 38.1, "Lọc vi sai: d = V_lòng - V_mu", ha='center', va='center', fontsize=10.0, color='#334155')

# Đầu ra chỉ số nỗ lực
ax.text(87.0, 30.5, "ĐẦU RA BỘ BA CHỈ SỐ:", ha='center', va='center', fontsize=12.0, fontweight='bold', color='#0F172A')
ax.text(87.0, 26.0, "EI (Nỗ lực) · GAP (Góc) · RAL (Trợ giúp)", ha='center', va='center', fontsize=12.0, fontweight='bold', color='#2563EB')

# ==================== MŨI TÊN KẾT NỐI CHÍNH (TRÁI -> PHẢI) ====================
def draw_main_arrow(x0, x1, y, label=""):
    ax.annotate('', xy=(x1, y), xytext=(x0, y),
                arrowprops=dict(arrowstyle="-|>", lw=2.6, color='#1E293B', mutation_scale=18),
                zorder=4)
    if label:
        ax.text((x0 + x1) / 2, y + 2.4, label, ha='center', va='bottom',
                fontsize=11.0, fontweight='bold', color='#1E293B',
                bbox=dict(boxstyle="round,pad=0.25", fc="#FFFFFF", ec="#CBD5E1", lw=1.1),
                zorder=5)

draw_main_arrow(19.5, 22.5, 56.0, "Lực ép F")
draw_main_arrow(37.5, 40.5, 56.0, "ΔV")
draw_main_arrow(55.5, 58.5, 56.0, "Kênh")
draw_main_arrow(73.5, 76.5, 56.0, "I2C")

# ==================== VÒNG TỰ CÂN CHỈNH ĐIỂM 0 (LANE RIÊNG DƯỚI ĐÁY) ====================
lane_y = 9.0
# Đoạn dọc xuống từ ESP32
ax.plot([87.0, 87.0], [19.5, lane_y], color='#2563EB', lw=2.8, linestyle=(0, (6, 4)), zorder=4)
# Đoạn ngang dài sang trái
ax.plot([87.0, 11.0], [lane_y, lane_y], color='#2563EB', lw=2.8, linestyle=(0, (6, 4)), zorder=4)
# Đoạn dọc lên Khối 1 với mũi tên trỏ vào Ô tham chiếu REF
ax.annotate('', xy=(11.0, 19.5), xytext=(11.0, lane_y),
            arrowprops=dict(arrowstyle="-|>", lw=2.8, color='#2563EB', linestyle=(0, (6, 4)), mutation_scale=20),
            zorder=4)

# Nhãn nổi bật chính giữa lane dưới đáy kèm mũi tên vector trái phải
loop_badge = patches.FancyBboxPatch(
    (22.0, lane_y - 2.8), 54.0, 5.6,
    boxstyle="round,pad=0.3,rounding_size=1.2",
    linewidth=2.0, edgecolor='#2563EB', facecolor='#EFF6FF', zorder=5
)
ax.add_patch(loop_badge)

# Mũi tên vector chỉ hướng bên trong badge
ax.annotate('', xy=(24.5, lane_y), xytext=(27.5, lane_y),
            arrowprops=dict(arrowstyle="-|>", lw=2.4, color='#1D4ED8', mutation_scale=16), zorder=6)
ax.annotate('', xy=(70.5, lane_y), xytext=(73.5, lane_y),
            arrowprops=dict(arrowstyle="-|>", lw=2.4, color='#1D4ED8', mutation_scale=16), zorder=6)

ax.text(49.0, lane_y, "Vòng tự cân chỉnh điểm 0 (Auto-zero) & Đối chiếu ô tham chiếu REF (khử sạch trôi nhiệt)",
        ha='center', va='center', fontsize=13.0, fontweight='bold', color='#1D4ED8', zorder=6)

# Lưu ảnh chất lượng cao 350 DPI
plt.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
dst_downloads = os.path.join(DOWNLOADS_DIR, 'Hinh10_Chuoi_thu_nhan_tin_hieu_tu_can_chinh_diem_0.png')
dst_figures = os.path.join(FIGURES_DIR, 'd6_sigchain-1.png')

plt.savefig(dst_downloads, dpi=350, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight', pad_inches=0.2)
plt.savefig(dst_figures, dpi=350, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight', pad_inches=0.2)
plt.close()

print('Saved successfully to:')
print('1.', dst_downloads)
print('2.', dst_figures)
im = Image.open(dst_downloads)
print('Output Dimensions:', im.size)
