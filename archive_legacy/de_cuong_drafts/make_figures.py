#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sinh toàn bộ hình ảnh / sơ đồ cho ĐỀ CƯƠNG (định dạng Word — Times New Roman).
Toàn bộ số liệu trong đồ thị là MINH HOẠ (synthetic/illustrative),
trừ các sơ đồ cấu trúc (khối / chuỗi tín hiệu / luồng quy trình) vẽ theo
tài liệu thiết kế đã chốt trong repo.
Font: DejaVu Serif (tương thích metric với Times New Roman).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUT = "/home/user/de_cuong/figures"
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif"],
    "mathtext.fontset": "dejavuserif",
    "font.size": 9,
    "axes.titlesize": 9,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "axes.linewidth": 0.6,
    "lines.linewidth": 1.2,
    "xtick.direction": "in",
    "ytick.direction": "in",
})
C_DARK = "#1a1a1a"
C_BLUE = "#2b6cb0"
C_BLUE2 = "#3182ce"
C_ORANGE = "#dd6b20"
C_GREEN = "#2f855a"
C_GRAY = "#4a5568"

# =========================================================================
# Hình 1 — Sơ đồ kiến trúc 3 tầng (cho mục 11.1)
# =========================================================================
def fig_architecture():
    fig, ax = plt.subplots(figsize=(6.8, 4.6), dpi=300)
    ax.set_xlim(0, 10); ax.set_ylim(0, 7.2); ax.axis("off")

    def box(x, y, w, h, title, lines, fc, ec=C_DARK, title_fc=None, tsize=8.5):
        ax.add_patch(FancyBboxPatch((x, y), w, h,
                    boxstyle="round,pad=0.06,rounding_size=0.12",
                    linewidth=1.0, edgecolor=ec, facecolor=fc, zorder=2))
        ty = y + h - 0.42
        if title_fc is not None:
            ax.add_patch(FancyBboxPatch((x, y + h - 0.62), w, 0.62,
                        boxstyle="round,pad=0.02,rounding_size=0.08",
                        linewidth=0, facecolor=title_fc, zorder=3))
            t = ax.text(x + w/2, ty, title, ha="center", va="center",
                    fontsize=tsize, fontweight="bold", zorder=4)
            t.set_color("white")
        else:
            ax.text(x + w/2, ty, title, ha="center", va="center",
                    fontsize=tsize, fontweight="bold", zorder=4)
        start = y + h - (1.05 if title_fc is not None else 0.85)
        for i, ln in enumerate(lines):
            yy = start - i * 0.37
            if yy < y + 0.22: break
            ax.text(x + w/2, yy, ln, ha="center", va="center", fontsize=7.4,
                    wrap=True, zorder=4)

    def arrow(x0, y0, x1, y1, label=""):
        ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>",
                    mutation_scale=13, linewidth=1.1, color=C_DARK, zorder=5))
        if label:
            ax.text((x0+x1)/2, (y0+y1)/2 + 0.16, label, ha="center",
                    va="bottom", fontsize=7.2, style="italic", color=C_GRAY, zorder=6)

    # Tầng 1 — cảm biến (đeo trên tay)
    box(0.35, 4.55, 3.4, 2.15, "TẦNG 1 — CẢM BIẾN (đeo trên tay)", [
        "Ốp ngón khung cứng (in 3D)",
        "Mảng Velostat 12 → 24 kênh vi sai",
        "6× IMU + ô tham chiếu đo trôi nền"
    ], fc="#ebf4fb", title_fc=C_BLUE)

    # Tầng 2 — thu thập
    box(4.25, 4.55, 2.6, 2.15, "TẦNG 2 — THU THẬP", [
        "CD74HC4067 chọn kênh",
        "ESP32-S3 (ADC1 12-bit)",
        "BLE 5 — truyền không dây"
    ], fc="#e6fffa", title_fc="#2c7a7b")

    # Tầng 3 — xử lý biên
    box(7.15, 4.55, 2.5, 2.15, "TẦNG 3 — XỬ LÝ BIÊN", [
        "Orange Pi 5 Pro (RK3588)",
        "Trích đặc trưng EI · GAP · RAL",
        "Ghi log nguồn + dashboard"
    ], fc="#faf5ff", title_fc="#6b46c1")

    # Người dùng / kết quả
    box(0.35, 0.7, 3.4, 1.15, "ĐỐI TƯỢNG SỬ DỤNG", [
        "Người bệnh tập tại nhà",
        "Kỹ thuật viên VLTL–PHCN đọc báo cáo"
    ], fc="#f7f7f7", title_fc=C_GRAY)
    box(7.15, 0.7, 2.5, 1.15, "KẾT QUẢ", [
        "Đường cong chức năng theo tuần",
        "Cờ độ tin cậy từng phiên"
    ], fc="#fff5f5", title_fc=C_ORANGE)

    # Mũi tên luồng chính
    arrow(3.85, 5.62, 4.16, 5.62)
    arrow(6.95, 5.62, 7.06, 5.62)
    arrow(2.05, 4.46, 2.05, 1.95, "đeo / cởi")
    arrow(7.15 + 1.25, 4.46, 7.15 + 1.25, 1.95, "báo cáo")
    ax.text(5.05, 6.45, "tín hiệu tương tự      I²C/SPI      USB / BLE",
            ha="center", fontsize=7.2, style="italic", color=C_GRAY)

    fig.savefig(f"{OUT}/hinh1_kien_truc_he_thong.png", bbox_inches="tight")
    plt.close(fig)

# =========================================================================
# Hình 2 — Chronological flow: chuỗi tín hiệu vật lý → chỉ số (cho mục 11.4)
# =========================================================================
def fig_signal_chain():
    fig, ax = plt.subplots(figsize=(6.8, 3.3), dpi=300)
    ax.set_xlim(0, 10); ax.set_ylim(0, 4.6); ax.axis("off")
    steps = [
        ("Lực ép ngón\nđè lên vách cứng", "#ebf4fb"),
        ("Velostat nén\n→ ΔR/R₀ giảm", "#e6fffa"),
        ("Nửa cầu\nWheatstone\n→ ΔV", "#f0fff4"),
        ("MUX chọn kênh\nCD74HC4067", "#faf5ff"),
        ("ESP32-S3\nADC 12-bit\n20 Hz", "#fff5f5"),
        ("EI · GAP · RAL\n(kèm cờ tin cậy)", "#fffbeb"),
    ]
    n = len(steps); w, h = 1.42, 1.7; gap = 0.18
    total = n * w + (n - 1) * gap
    x0 = (10 - total) / 2
    for i, (label, fc) in enumerate(steps):
        x = x0 + i * (w + gap)
        ax.add_patch(FancyBboxPatch((x, 1.55), w, h,
                    boxstyle="round,pad=0.05,rounding_size=0.1",
                    linewidth=0.9, edgecolor=C_DARK, facecolor=fc, zorder=2))
        ax.text(x + w/2, 1.55 + h/2, label, ha="center", va="center", fontsize=7.6, zorder=3)
        if i < n - 1:
            ax.add_patch(FancyArrowPatch((x + w + 0.02, 1.55 + h/2),
                        (x + w + gap - 0.02, 1.55 + h/2), arrowstyle="-|>",
                        mutation_scale=11, linewidth=1.0, color=C_DARK, zorder=4))
    ax.text(5, 3.6, "Chuỗi tín hiệu: từ chuyển động của ngón tay đến chỉ số đo được (sơ đồ nguyên lý)",
            ha="center", fontsize=9.5, fontweight="bold")
    ax.text(5, 0.85, "Quy ước: ΔR/R₀ = độ thay đổi điện trở tương đối;  ΔV = điện áp ra nửa cầu;  ADC = bộ chuyển đổi tương tự–số.\nEI, GAP, RAL là ba chỉ số dẫn xuất, định nghĩa ở Mục 11.3.",
            ha="center", va="center", fontsize=7.3, color=C_GRAY, style="italic")
    fig.savefig(f"{OUT}/hinh2_chuoi_tin_hieu.png", bbox_inches="tight")
    plt.close(fig)

# =========================================================================
# Hình 3 — Đồ thị minh hoạ: đáp ứng Velostat (số liệu MINH HOẠ)
# =========================================================================
def fig_velostat():
    fig, axes = plt.subplots(1, 2, figsize=(6.8, 2.7), dpi=300)
    p = np.logspace(-0.5, 2.3, 200)
    dR = 100 * (p / 10.0) ** (-0.5)
    ax = axes[0]
    ax.loglog(p, dR, lw=1.6, color=C_BLUE)
    ax.axvspan(1.0, 80.0, color="gray", alpha=0.10)
    ax.annotate("cửa sổ làm việc dự kiến", xy=(6, 10), xytext=(0.18, 40),
                fontsize=7.5, arrowprops=dict(arrowstyle="->", lw=0.7, color="0.3"))
    ax.set_xlabel("Áp suất tiếp xúc p (kPa)")
    ax.set_ylabel(r"−ΔR/R₀  (%)")
    ax.set_title("(a) Đặc tính giảm điện trở theo áp suất", fontweight="bold", loc="left")
    ax.grid(which="both", alpha=0.25, lw=0.4)
    ax.minorticks_off()

    Fp = np.linspace(0.1, 60, 400)
    sens = 24.8 / (Fp + 5.0)
    sens[Fp > 34] *= np.exp(-(Fp[Fp > 34] - 34) / 14)
    ax = axes[1]
    ax.plot(Fp, sens, lw=1.6, color=C_ORANGE, label="độ nhạy (mô hình)  ")
    ax.axhline(1.21, color="crimson", ls="--", lw=1.0,
               label="ngưỡng cần: ΔV ≥ 8 LSB  ")
    ax.axvspan(5, 34, color=C_GREEN, alpha=0.12)
    ax.annotate("cửa sổ tiền tải\nkhả dụng", xy=(20, 0.35), xytext=(20, 1.35),
                ha="center", fontsize=7.5,
                arrowprops=dict(arrowstyle="->", lw=0.7, color="0.3"))
    ax.set_xlabel("Lực tiền tải Fp (N)")
    ax.set_ylabel("Độ nhạy (mV mỗi N)")
    ax.set_title("(b) Cửa sổ tiền tải bị chặn hai phía", fontweight="bold", loc="left")
    ax.legend(frameon=False, fontsize=7.2, loc="upper right")
    ax.grid(alpha=0.25, lw=0.4)
    ax.set_ylim(0, None)
    fig.text(0.5, 0.005, "Hình minh hoạ — số liệu mô phỏng, chưa phải kết quả đo thực nghiệm.",
             ha="center", fontsize=7.2, style="italic", color=C_GRAY)
    fig.tight_layout(rect=[0, 0.045, 1, 1])
    fig.savefig(f"{OUT}/hinh3_velostat_minhhoa.png", bbox_inches="tight")
    plt.close(fig)

# =========================================================================
# Hình 4 — Minh hoạ GAP = AROM − PROM (vòng lặp đo 1 ngón) — MINH HOẠ
# =========================================================================
def fig_gap():
    fig, ax = plt.subplots(figsize=(3.9, 2.8), dpi=300)
    rng = np.random.default_rng(3)
    t = np.linspace(0, 1, 150)
    # PROM: góc duỗi thụ động theo vòng cung ~ lên 70° rồi về
    prom = 72 * (1 - np.cos(np.pi * t)) / 2
    arom = prom * 0.6 + 3 * np.sin(2 * np.pi * 0.6 * t) + rng.normal(0, 1.2, t.size)
    ax.plot(t, prom, lw=1.6, color=C_BLUE, label="PROM — tầm vận động thụ động")
    ax.plot(t, arom, lw=1.6, color=C_ORANGE, label="AROM — tầm vận động chủ động")
    ax.fill_between(t, prom, arom, color="gray", alpha=0.18)
    ax.annotate("GAP", xy=(0.55, 30), fontsize=9, fontweight="bold", ha="center")
    ax.annotate("GAP = AROM − PROM", xy=(0.55, 22), fontsize=7.6, ha="center", color=C_GRAY)
    ax.set_xlabel("Thời gian (chuẩn hoá)")
    ax.set_ylabel("Góc khớp (độ, thang IMU)")
    ax.set_ylim(0, 85)
    ax.legend(frameon=False, fontsize=7.4, loc="lower right")
    ax.grid(alpha=0.25, lw=0.4)
    fig.text(0.5, 0.005, "Minh hoạ — số liệu mô phỏng.", ha="center",
             fontsize=7.2, style="italic", color=C_GRAY)
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    fig.savefig(f"{OUT}/hinh4_gap_minhhoa.png", bbox_inches="tight")
    plt.close(fig)

# =========================================================================
# Hình 5 — Ví dụ kết quả dự kiến: đường cong theo tuần (MINH HOẠ)
# =========================================================================
def fig_trajectory():
    fig, ax = plt.subplots(figsize=(5.9, 3.0), dpi=300)
    weeks = np.arange(0, 9)
    y = np.array([58, 61, 60, 66, 68, 71, 72, 75, 77])  # EI chuẩn hoá, %
    yerr = np.array([4, 4, 4, 3, 3, 3, 3, 2, 2])
    ax.plot(weeks, y, "-o", lw=1.6, ms=4, color=C_BLUE)
    ax.fill_between(weeks, y - yerr, y + yerr, color=C_BLUE, alpha=0.15)
    # một phiên bị cờ từ chối
    ax.plot(weeks[3], y[3], "o", ms=9, mfc="none", mec="crimson", mew=1.5)
    ax.annotate("tuần 3: phiên bị cờ UNRELIABLE\n(không đưa vào đường xu hướng)",
                xy=(weeks[3], y[3]), xytext=(1.0, 52),
                fontsize=7.2, arrowprops=dict(arrowstyle="->", lw=0.7, color="crimson"),
                color="crimson")
    ax.set_xlabel("Tuần theo dõi")
    ax.set_ylabel("Chỉ số chức năng tay (%)")
    ax.set_ylim(40, 90)
    ax.set_xticks(weeks)
    ax.grid(alpha=0.25, lw=0.4)
    fig.text(0.5, 0.02, "Minh hoạ định dạng báo cáo — số liệu giả lập; vùng mờ là khoảng tin cậy (± sai số đo).",
             ha="center", fontsize=7.2, style="italic", color=C_GRAY)
    fig.tight_layout(rect=[0, 0.06, 1, 1])
    fig.savefig(f"{OUT}/hinh5_duong_cong_tuan_minhhoa.png", bbox_inches="tight")
    plt.close(fig)

fig_architecture()
fig_signal_chain()
fig_velostat()
fig_gap()
fig_trajectory()
print("FIGURES done:")
import os
for f in sorted(os.listdir(OUT)):
    print("  ", f)
