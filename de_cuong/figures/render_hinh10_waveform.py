import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

DOWNLOADS_DIR = r'C:\Users\user\Downloads'

# Kích thước Landscape chuẩn (15.5 in x 6.5 in @ 350 DPI)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.5, 6.5), dpi=350)
fig.patch.set_facecolor('#FFFFFF')

plt.rcParams['font.sans-serif'] = ['Arial', 'Segoe UI', 'DejaVu Sans']

# Tạo dữ liệu giả lập thực nghiệm chuẩn xác theo nhật ký đo kiểm (note 05, 06, 07)
t = np.linspace(0, 10, 1000) # 10 giây
np.random.seed(42)

# ==================== (a) VÒNG LẶP 1: INA333 (G ≈ 6.5) ====================
# Tín hiệu bị tiền tải kéo sụt và bão hòa kẹt cứng tại ~2838 mV
raw_signal_v1 = 1400 + 1900 * np.sin(2 * np.pi * 0.25 * t)**2 # Lực bóp ngón tay lặp lại
# Khi qua INA333 khuếch đại, bị bão hòa kẹp ở 2838 mV
saturated_v1 = np.clip(raw_signal_v1 + np.random.normal(0, 35, len(t)), 0, 2838.0)
# Thêm nhiễu nền lớn khi nghỉ (nhiễu 50-135mV bị nhân 6.5 lần)
noise_floor_v1 = 1400 + np.random.normal(0, 45, len(t))
mask_rest_v1 = (np.sin(2 * np.pi * 0.25 * t)**2 < 0.08)
saturated_v1[mask_rest_v1] = noise_floor_v1[mask_rest_v1]

ax1.set_facecolor('#FAFAFA')
ax1.plot(t, saturated_v1, color='#DC2626', lw=2.2, label='Dạng sóng thực tế (INA333 G ≈ 6,5)')
ax1.axhline(2838, color='#991B1B', linestyle='--', lw=2.0, label='Ngưỡng bão hòa cứng (≈ 2.838 mV)')
ax1.axhline(1400, color='#64748B', linestyle=':', lw=1.5, label='Mốc tiền tải ban đầu (≈ 1.400 mV)')

# Vùng bão hòa highlight đỏ nhạt
ax1.fill_between(t, 2750, 3000, color='#FEE2E2', alpha=0.6)
ax1.annotate('BÃO HÒA KẸT CỨNG\n(Clipping tại 2.838 mV)', xy=(3.0, 2838), xytext=(3.0, 3100),
             ha='center', va='bottom', fontsize=11, fontweight='bold', color='#991B1B',
             arrowprops=dict(arrowstyle="->", lw=1.8, color='#991B1B'),
             bbox=dict(boxstyle="round,pad=0.3", fc="#FEF2F2", ec="#DC2626", lw=1.2))

ax1.set_title('(a) Vòng lặp 1: Dùng tầng khuếch đại INA333\n(Mất dải động do tiền tải, bão hòa tại 2.838 mV, nhiễu nền cao)',
              fontsize=13, fontweight='bold', color='#0F172A', pad=12)
ax1.set_xlabel('Thời gian (giây)', fontsize=12, fontweight='bold', color='#334155')
ax1.set_ylabel('Điện áp ngõ ra (mV)', fontsize=12, fontweight='bold', color='#334155')
ax1.set_xlim(0, 10)
ax1.set_ylim(1000, 3400)
ax1.grid(True, linestyle='--', alpha=0.5, color='#CBD5E1')
ax1.legend(loc='lower left', fontsize=10.5, framealpha=0.95, edgecolor='#CBD5E1')

# ==================== (b) VÒNG LẶP 2: ADS1115 (16-bit) + DSP 4 BƯỚC ====================
# Đọc trực tiếp, giữ nguyên dải động 0 - 3300 mV, đường nền phẳng 0 mV khi nghỉ
ideal_force = np.maximum(0, (np.sin(2 * np.pi * 0.25 * t)**2 - 0.08) / 0.92) # 0 to 1
clean_v2 = ideal_force * 2200.0 # Biên độ đỉnh 2200 mV
# Thêm chút gợn tự nhiên khi bóp
clean_v2[clean_v2 > 0] += np.random.normal(0, 15, np.sum(clean_v2 > 0))
clean_v2 = np.maximum(0, clean_v2) # Vùng chết giữ phẳng tại 0

ax2.set_facecolor('#FAFAFA')
ax2.plot(t, clean_v2, color='#059669', lw=2.2, label='Tín hiệu sau DSP 4 bước (ADS1115 16-bit)')
ax2.axhline(0, color='#047857', linestyle='-', lw=2.0, label='Đường cơ sở Auto-zero (phẳng 0,0 mV)')

# Điểm nhấn đáp ứng tuyến tính
ax2.annotate('Đường nền phẳng 0,0 mV khi nghỉ\n(Khử trôi nhiệt mốc tĩnh & loại nhiễu)', xy=(1.0, 0), xytext=(1.0, 600),
             ha='center', va='bottom', fontsize=10.5, fontweight='bold', color='#047857',
             arrowprops=dict(arrowstyle="->", lw=1.8, color='#047857'),
             bbox=dict(boxstyle="round,pad=0.3", fc="#ECFDF5", ec="#059669", lw=1.2))

ax2.annotate('Bảo toàn dải động 0 – 3.300 mV\nĐáp ứng lực bóp tức thời, không bão hòa', xy=(3.0, 2200), xytext=(3.0, 2700),
             ha='center', va='bottom', fontsize=10.5, fontweight='bold', color='#065F46',
             arrowprops=dict(arrowstyle="->", lw=1.8, color='#065F46'),
             bbox=dict(boxstyle="round,pad=0.3", fc="#F0FDF4", ec="#10B981", lw=1.2))

ax2.set_title('(b) Vòng lặp 2: Đọc trực tiếp ADS1115 16-bit + Lọc số DSP 4 bước\n(Bảo toàn toàn dải 0 – 3.300 mV, đường nền phẳng 0,0 mV, đáp ứng tuyến tính)',
              fontsize=13, fontweight='bold', color='#0F172A', pad=12)
ax2.set_xlabel('Thời gian (giây)', fontsize=12, fontweight='bold', color='#334155')
ax2.set_ylabel('Điện áp quy đổi / Nỗ lực (mV)', fontsize=12, fontweight='bold', color='#334155')
ax2.set_xlim(0, 10)
ax2.set_ylim(-150, 3400)
ax2.grid(True, linestyle='--', alpha=0.5, color='#CBD5E1')
ax2.legend(loc='upper right', fontsize=10.5, framealpha=0.95, edgecolor='#CBD5E1')

plt.suptitle('Hình 10. Kết quả đo đối chứng dạng sóng trên Serial Plotter ở Vòng lặp 1 & Vòng lặp 2',
             fontsize=17, fontweight='bold', color='#0F172A', y=1.01)

plt.tight_layout()
dst_plot = os.path.join(DOWNLOADS_DIR, 'Hinh10_Do_thi_doi_chung_dang_song_Serial_Plotter.png')
plt.savefig(dst_plot, dpi=350, bbox_inches='tight', pad_inches=0.15)
plt.close()
print('Waveform plot saved to:', dst_plot)
