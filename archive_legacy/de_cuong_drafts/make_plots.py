#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sinh các ĐỒ THỊ DỮ LIỆU cho đề cương bằng matplotlib (chỉ đồ thị, không vẽ sơ
đồ — sơ đồ dùng PGF/TikZ để chữ không bao giờ lệch/tràn hộp).
P1/P2/P4/P5: số liệu MÔ PHỎNG (ghi rõ trên hình). P3 (GAP) mô phỏng.
P1b gánh nặng: số liệu THẬT đã kiểm nguồn (ghi nguồn trên hình).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/home/user/de_cuong/figures"
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif"],
    "mathtext.fontset": "dejavuserif",
    "font.size": 9.5,
    "axes.titlesize": 9.5,
    "axes.labelsize": 9.5,
    "xtick.labelsize": 8.5,
    "ytick.labelsize": 8.5,
    "legend.fontsize": 8,
    "axes.linewidth": 0.6,
    "lines.linewidth": 1.3,
    "xtick.direction": "in",
    "ytick.direction": "in",
})
C_BLUE = "#2b6cb0"; C_ORANGE = "#dd6b20"; C_GRAY = "#4a5568"
C_GREEN = "#2f855a"; C_RED = "#c53030"

# P1 — Gánh nặng đột quỵ (số liệu THẬT đã kiểm nguồn, có DOI)
def plot_burden():
    fig, axes = plt.subplots(1, 2, figsize=(6.8, 2.7), dpi=300)
    C_NEUT = "#6b7280"  # xám trung tính; xanh = điểm nhấn

    ax = axes[0]
    labels = ["Mới mắc\n(mỗi năm)", "Hiện mắc\n(tại thời điểm)"]
    vals = [222, 1541]
    bars = ax.bar(labels, vals, width=0.5,
                  color=[C_BLUE, C_NEUT], edgecolor="black", linewidth=0.6)
    ax.bar_label(bars, fmt=lambda v: f"{v:,.0f}".replace(",", "."),
                 padding=3, fontsize=9, fontweight="bold", color="#1a1a1a")
    ax.set_ylabel("Số người trên 100.000 dân")
    ax.set_ylim(0, 1750)
    ax.set_title("(a) Tỷ lệ đột quỵ tại Việt Nam [1]", fontweight="bold", loc="left")
    ax.grid(axis="y", alpha=0.25, lw=0.4)
    for s in ("top", "right"): ax.spines[s].set_visible(False)

    ax = axes[1]
    # thứ tự hiển thị đứng (barh vẽ phần tử ĐẦU TIÊN ở đáy): nhãn khớp đúng từng cột
    disp_items = ["Còn vấn đề ở bàn tay\nsau 4 năm",
                  "Liệt hoàn toàn phục hồi\nchức năng có ích sau 6 tháng",
                  "Tổn thương vận động\nchi trên giai đoạn sớm"]
    disp_vals = [50, 50, 80]
    disp_lbls = ["50% (còn di chứng)", "50% (phục hồi có ích)", "80%"]
    # xám = di chứng còn lại; xanh = thông tin tích cực (quy ước màu chung 2 panel)
    colors = [C_NEUT, C_BLUE, C_NEUT]
    bars = ax.barh(disp_items, disp_vals, height=0.5,
                   color=colors, edgecolor="black", linewidth=0.6)
    ax.bar_label(bars, labels=disp_lbls,
                 padding=3, fontsize=9, fontweight="bold", color="#1a1a1a")
    ax.set_xlim(0, 100)
    ax.set_xlabel("Tỷ lệ phần trăm (%)")
    ax.set_title("(b) Di chứng bàn tay kéo dài [2]", fontweight="bold", loc="left")
    ax.grid(axis="x", alpha=0.25, lw=0.4)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    fig.tight_layout(pad=0.8)
    fig.savefig(f"{OUT}/p1_ganh_nang_dot_quy.png", bbox_inches="tight")
    plt.close(fig)

# P2 — Đặc tính Velostat (MÔ PHỎNG)
def plot_velostat():
    fig, axes = plt.subplots(1, 2, figsize=(6.8, 2.8), dpi=300)
    # (a) đặc tính lực – điện trở, thang kΩ (giá trị MÔ PHỎNG minh hoạ)
    F = np.linspace(0.1, 60, 300)
    R = 1.5 / (F + 2.5) + 0.006                      # kΩ — dạng nghịch đảo: giảm nhanh ở lực nhỏ
    ax = axes[0]
    ax.plot(F, R, lw=1.6, color=C_BLUE)
    ax.axvspan(5, 18, color="gray", alpha=0.12)
    ax.text(11.5, 0.58, "vùng gần\ntuyến tính", fontsize=8, color="0.35",
            ha="center", va="top")
    ax.annotate("", xy=(11.5, 0.13), xytext=(11.5, 0.52),
                arrowprops=dict(arrowstyle="->", lw=0.6, color="0.4"))
    ax.annotate("điện trở giảm nhanh\nở lực nhỏ", xy=(2.5, 0.31), xytext=(20, 0.52),
                fontsize=7.5, color=C_GRAY,
                arrowprops=dict(arrowstyle="->", lw=0.7, color=C_GRAY))
    ax.annotate("bão hòa ở lực lớn", xy=(50, 0.045), xytext=(32, 0.24),
                fontsize=7.5, color=C_GRAY,
                arrowprops=dict(arrowstyle="->", lw=0.7, color=C_GRAY))
    ax.set_xlabel("Lực ép lên màng F (N)")
    ax.set_ylabel("Điện trở màng R (kΩ)")
    ax.set_title("(a) Điện trở giảm khi bị nén", fontweight="bold", loc="left")
    ax.set_ylim(0, 0.7)
    ax.grid(alpha=0.25, lw=0.4)

    Fp = np.linspace(0.1, 60, 500)
    # độ nhạy mượt: bão hoà rồi suy giảm trơn (không gãy khúc tại 34 N)
    sens = (24.8 / (Fp + 5.0)) * np.exp(-np.maximum(Fp - 34.0, 0.0) / 14.0)
    ax = axes[1]
    ax.plot(Fp, sens, lw=1.6, color=C_ORANGE)
    ax.annotate("độ nhạy (mô hình)", xy=(22, 0.93), xytext=(30, 2.1), fontsize=6.8,
                color=C_ORANGE, arrowprops=dict(arrowstyle="->", lw=0.6, color=C_ORANGE))
    ax.axhline(1.21, color=C_RED, ls="--", lw=1.0)
    ax.text(58.5, 1.45, "ngưỡng nhạy tối thiểu\n(8 LSB)", fontsize=6.8, color=C_RED,
            ha="right", va="bottom")
    # cửa sổ tiền tải = GIAO của giới hạn nhạy (mép phải) và giới hạn ổn định (mép trái)
    ax.axvspan(5, 15.5, color=C_GREEN, alpha=0.12)
    ax.axvline(5,    color=C_GREEN, ls=":", lw=1.0)
    ax.axvline(15.5, color=C_GREEN, ls=":", lw=1.0)
    # hai chú thích mép: trái nằm góc trên-trái, phải nằm TRONG khung (ha=right, không tràn spine)
    ax.annotate("mép trái (Fp ≈ 5 N):\ngiới hạn ổn định —\ncreep tăng khi tiền tải nhỏ",
                xy=(5, 1.15), xytext=(2, 4.85), fontsize=6.8, color=C_GRAY,
                ha="left", va="top",
                arrowprops=dict(arrowstyle="->", lw=0.7, color=C_GRAY))
    ax.annotate("mép phải (Fp ≈ 15 N):\ngiới hạn nhạy —\ntín hiệu dưới 8 LSB",
                xy=(15.5, 1.5), xytext=(58, 4.85), fontsize=6.8, color=C_GRAY,
                ha="right", va="top",
                arrowprops=dict(arrowstyle="->", lw=0.7, color=C_GRAY))
    # nhãn cửa sổ đặt sát đáy trục (dưới dải tô), nền trắng để không cọ đường nhạy
    ax.text(10.2, 0.30, "khoảng tiền tải khả dụng", fontsize=7.5, color=C_GREEN,
            ha="center", va="bottom",
            bbox=dict(fc="white", ec="none", alpha=0.85, pad=0.5))
    ax.set_xlabel("Lực tiền tải Fp (N)")
    ax.set_ylabel("Độ nhạy (mV/N)")
    ax.set_title("(b) Cửa sổ tiền tải hai phía", fontweight="bold", loc="left")
    ax.grid(alpha=0.25, lw=0.4)
    ax.set_ylim(0, 5.2)
    plt.subplots_adjust(bottom=0.16)
    fig.savefig(f"{OUT}/p2_velostat_minhhoa.png", bbox_inches="tight")
    plt.close(fig)

# P3 — GAP = PROM − AROM (MÔ PHỎNG)
def plot_gap():
    fig, ax = plt.subplots(figsize=(4.7, 3.0), dpi=300)
    rng = np.random.default_rng(7)
    t = np.linspace(0, 1, 300)
    # PROM (bị kéo thụ động): biên độ cao, mượt, xuất phát từ 0
    prom = 72 * (1 - np.cos(np.pi * t)) / 2
    # AROM (tự gập): thấp hơn hẳn, rung do cơ yếu; nhiễu tăng dần theo t để khởi đầu vẫn = 0
    arom = prom * (0.55 + 0.10 * np.sin(2 * np.pi * 0.7 * t))
    arom = arom + (prom / 15.0) * rng.standard_normal(len(t)) * 0.35 * t
    ax.plot(t, prom, lw=1.8, color=C_BLUE, label="PROM (bị kéo, mượt)")
    ax.plot(t, arom, lw=1.6, color=C_ORANGE, label="AROM (tự gập, thấp)")
    ax.fill_between(t, arom, prom, color="gray", alpha=0.16)
    # GAP = PROM − AROM: đo chênh lệch TẠI ĐỈNH (cuối động tác)
    xa = 0.95
    ya = np.interp(xa, t, arom)
    yp = np.interp(xa, t, prom)
    ax.annotate("", xy=(xa, ya), xytext=(xa, yp),
                arrowprops=dict(arrowstyle="<->", lw=1.0, color=C_GRAY))
    ax.text(xa - 0.025, (ya + yp) / 2, "GAP\ntại đỉnh", ha="right", va="center",
            fontsize=8, fontweight="bold", color="#1a1a1a",
            bbox=dict(boxstyle="round,pad=0.22", fc="white", ec="0.6", alpha=0.95))
    ax.set_xlabel("Thời gian (chuẩn hoá)")
    ax.set_ylabel("Góc gập quy đổi từ tín hiệu (độ)")
    ax.set_ylim(0, 82)
    ax.legend(frameon=True, fontsize=7.5, loc="lower right",
              facecolor="white", framealpha=0.9, edgecolor="0.7")
    ax.grid(alpha=0.25, lw=0.4)
    fig.tight_layout()
    fig.savefig(f"{OUT}/p3_gap_minhhoa.png", bbox_inches="tight")
    plt.close(fig)

# P4 — Đọc vi sai hai vách (MÔ PHỎNG) — suy luận dấu gập/duỗi + khử trôi đồng pha
def plot_differential():
    fig, axes = plt.subplots(1, 3, figsize=(6.6, 2.5), dpi=300)
    t = np.linspace(0, 1, 400)
    YL = (-1.35, 1.35)  # đối xứng quanh 0 => đường d = 0 nằm CHÍNH GIỮA ở cả ba khung; d không bị cắt

    # (a) Gập: vách lòng tăng theo hình sin, vách mu đứng yên (phẳng) => d = lòng − mu > 0
    ax = axes[0]
    pal = 0.3 + 1.0 * np.sin(np.pi * t)          # lòng: 0.3 → 1.3 → 0.3
    dor = 0.3 + 0.0 * t                           # mu: phẳng ở 0.3
    ax.plot(t, pal, lw=1.3, color=C_BLUE, label="vách lòng")
    ax.plot(t, dor, lw=1.3, color=C_ORANGE, label="vách mu")
    ax.plot(t, pal - dor, lw=1.6, color=C_GREEN, label="d = lòng − mu")
    ax.axhline(0, color="0.45", ls="--", lw=0.8)
    ax.text(0.02, -0.22, "d = 0", fontsize=6.5, color="0.35",
            bbox=dict(fc="white", ec="none", alpha=0.9, pad=0.5))
    ax.set_title("(a) Gập:  d > 0", fontsize=8, fontweight="bold", color="0.2")
    ax.set_ylim(YL); ax.set_yticks([]); ax.set_xticks([])

    # (b) Duỗi: vách mu tăng, vách lòng phẳng => d = lòng − mu < 0
    ax = axes[1]
    pal = 0.3 + 0.0 * t
    dor = 0.3 + 1.0 * np.sin(np.pi * t)
    ax.plot(t, pal, lw=1.3, color=C_BLUE, label="vách lòng")
    ax.plot(t, dor, lw=1.3, color=C_ORANGE, label="vách mu")
    ax.plot(t, pal - dor, lw=1.6, color=C_GREEN, label="d = lòng − mu")
    ax.axhline(0, color="0.45", ls="--", lw=0.8)
    ax.text(0.02, -0.22, "d = 0", fontsize=6.5, color="0.35",
            bbox=dict(fc="white", ec="none", alpha=0.9, pad=0.5))
    ax.set_title("(b) Duỗi:  d < 0", fontsize=8, fontweight="bold", color="0.2")
    ax.set_ylim(YL); ax.set_yticks([]); ax.set_xticks([])

    # (c) Trôi đồng pha (nhiệt độ): hai vách cùng pha, d chỉ là dao động nhỏ quanh 0
    ax = axes[2]
    common = np.linspace(0.35, 0.95, len(t))      # trôi chậm chung
    wave = 0.08 * np.sin(2 * np.pi * 3 * t)       # gợn đồng pha trên cả hai vách
    pal = common + wave + 0.03 * np.sin(2 * np.pi * 0.8 * t)
    dor = common + wave
    ax.plot(t, pal, lw=1.3, color=C_BLUE, label="vách lòng")
    ax.plot(t, dor, lw=1.3, color=C_ORANGE, label="vách mu")
    ax.plot(t, pal - dor, lw=1.6, color=C_GREEN, label="d = lòng − mu")
    ax.axhline(0, color="0.45", ls="--", lw=0.8)
    ax.text(0.02, -0.22, "d = 0", fontsize=6.5, color="0.35",
            bbox=dict(fc="white", ec="none", alpha=0.9, pad=0.5))
    ax.set_title("(c) Trôi đồng pha:  d ≈ 0", fontsize=8, fontweight="bold", color="0.2")
    ax.set_ylim(YL); ax.set_yticks([]); ax.set_xticks([])

    # Chú giải đặt Ở GIỮA, phía dưới cả ba khung
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, frameon=True, fontsize=7,
               loc="lower center", ncol=3, facecolor="white",
               edgecolor="0.8", bbox_to_anchor=(0.5, -0.02))
    fig.tight_layout(rect=[0, 0.06, 1, 1])
    fig.savefig(f"{OUT}/p4_doc_vi_sai_minhhoa.png", bbox_inches="tight")
    plt.close(fig)

# P5 — Đường cong theo tuần (MÔ PHỎNG)
def plot_trajectory():
    fig, ax = plt.subplots(figsize=(5.9, 2.9), dpi=300)
    weeks = np.arange(0, 9)
    # GAP = PROM − AROM (đơn vị độ) — giảm dần = phục hồi tốt hơn (MÔ PHỎNG)
    y_all = np.array([30, 27, 24, 37, 21, 18, 15, 12, 9])   # tuần 3 = 37: bất thường, bị loại
    yerr = np.array([3, 3, 3, 2.5, 2.5, 2, 2, 1.5, 1.5])
    # tuần 3 bị loại THẬT: trend + dải tin cậy chỉ vẽ trên điểm tin cậy
    valid = np.array([i != 3 for i in range(len(weeks))])
    wv = weeks[valid]; yv = y_all[valid]; ev = yerr[valid]
    ax.plot(wv, yv, "-o", lw=1.6, ms=4, color=C_BLUE, label="GAP (PROM − AROM)")
    ax.fill_between(wv, yv - ev, yv + ev, color=C_BLUE, alpha=0.15, label="khoảng tin cậy")
    # điểm bị loại: dấu × rời, nằm cao hẳn khỏi dải, không nối vào trend
    ax.plot(weeks[3], y_all[3], "x", ms=11, mfc="none", mec=C_RED, mew=2.0, zorder=5)
    ax.annotate("BÁO: SỐ LIỆU NGHI VẤN\ntuần 3 loại khỏi xu hướng",
                xy=(3, 36), xytext=(4.35, 29.0), fontsize=7.5, color=C_RED,
                ha="left", va="center",
                arrowprops=dict(arrowstyle="->", lw=0.7, color=C_RED))
    ax.set_xlabel("Tuần theo dõi")
    ax.set_ylabel("GAP = PROM − AROM (độ)")
    ax.set_ylim(0, 42)
    ax.set_xticks(weeks)
    ax.legend(frameon=False, fontsize=7.5, loc="upper right")
    ax.grid(alpha=0.25, lw=0.4)
    fig.savefig(f"{OUT}/p5_duong_cong_tuan_minhhoa.png", bbox_inches="tight")
    plt.close(fig)

# P6 — Đường cong RAL: tải trợ giúp tối thiểu để hoàn thành (MÔ PHỎNG)
def plot_ral():
    fig, ax = plt.subplots(figsize=(5.6, 3.0), dpi=300)
    loads = np.array([0, 20, 40, 60, 80, 100, 120])
    # giai đoạn đầu (phiên 1): đạt >=80% chỉ từ nấc 120 g  → RAL = 120 g
    p1 = np.array([26, 37, 49, 60, 70, 79, 86])
    # về sau (phiên 3): đạt >=80% đã ở nấc 60 g            → RAL = 60 g
    p3 = np.array([46, 63, 77, 87, 93, 96, 98])
    p1 = np.clip(p1, 0, 100); p3 = np.clip(p3, 0, 100)
    ax.plot(loads, p1, "-o", lw=1.6, ms=4, color=C_BLUE, label="phiên theo dõi 1")
    ax.plot(loads, p3, "-s", lw=1.6, ms=4, color=C_ORANGE, label="phiên theo dõi 3")
    ax.axhline(80, color=C_GRAY, ls="--", lw=1.0)
    ax.text(0.6, 82.5, "ngưỡng hoàn thành 80%", fontsize=7.5, color=C_GRAY)
    def ral(p):
        idx = np.where(p >= 80)[0]
        return loads[idx[0]] if idx.size else None
    r1, r3 = ral(p1), ral(p3)
    def mark(r, p, series_color, dxt, dyt):
        # marker nằm TRÊN ĐIỂM DỮ LIỆU đạt ngưỡng (không nằm trên đường ngưỡng)
        y = p[np.where(loads == r)[0][0]]
        ax.scatter([r], [y], s=70, facecolor="white", edgecolor=series_color, zorder=5)
        ax.annotate(f"RAL = {r} g", xy=(r, y), xytext=(r + dxt, y + dyt),
                    fontsize=8, color=series_color,
                    arrowprops=dict(arrowstyle="->", lw=0.7, color=series_color))
    # phiên 1: nhãn đặt cao bên TRÁI điểm (rời xa spine + không cắt đường cam)
    if r1 is not None: mark(r1, p1, C_BLUE,   -58, +11)
    # phiên 3: nhãn lệch phải/phía dưới điểm
    if r3 is not None: mark(r3, p3, C_ORANGE,  +13, -15)
    ax.set_xlabel("Tải trợ giúp treo (g)")
    ax.set_ylabel("Tỷ lệ nhịp hoàn thành (%)")
    ax.set_ylim(0, 118)
    ax.set_xlim(-4, 126)
    ax.set_xticks(loads)
    ax.legend(frameon=False, fontsize=8, loc="lower right")
    ax.grid(alpha=0.25, lw=0.4)
    fig.text(0.5, 0.008, "Số liệu mô phỏng minh hoạ: RAL là nấc tải đầu tiên đạt ≥ 80%; RAL giảm giữa phiên 1 và 3 = cần ít trợ giúp hơn.",
             ha="center", fontsize=7.2, style="italic", color=C_GRAY)
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    fig.savefig(f"{OUT}/p6_ral_minhhoa.png", bbox_inches="tight")
    plt.close(fig)

plot_burden(); plot_velostat(); plot_gap(); plot_differential(); plot_trajectory(); plot_ral()
print("PLOTS done")
import os
for f in sorted(os.listdir(OUT)): print("  ", f)
