# -*- coding: utf-8 -*-
"""
params.py — THAM SỐ DÙNG CHUNG cho bộ cố định đốt gần P1 (Smart Exo-Glove Fixation v0.1).

NGUỒN SỐ LIỆU & TRẠNG THÁI (theo AGENTS.md — phân cấp bằng chứng):
  [BRIEF]  = ràng buộc do chủ dự án đặt ra trong brief 2026-10-06 (hard constraint).
  [EST]    = giá trị kỹ thuật ước lượng/tính toán thiết kế — PHẢI ĐO LẠI (bench).
  [LIT]    = tham chiếu tài liệu — CHƯA xác minh tới bản gốc, phải tra trước khi trích dẫn.
  [MEASURE]= phải đo bằng thước kẹp/thước dây trên chính bệnh nhân hoặc trên phantom.

Mọi con số "an toàn sinh học" trong file này là NGÂN SÁCH THIẾT KẾ, không phải kết quả
thực nghiệm. Không được trích như dữ liệu đo.
"""

# =============================================================================
# 1. GIẢI PHẪU NGÓN — ĐỐT GẦN (PROXIMAL PHALANX 1)
# =============================================================================
D_NOM = 22.0          # [BRIEF] đường kính danh nghĩa P1 (dải làm việc 20–24 mm)
A_F1 = 10.6           # [MEASURE] nửa bề rộng NGANG của P1 (trục X)   (Ø21.2)
B_F1 = 10.0           # [MEASURE] nửa bề sâu MU–LÒNG của P1 (trục Y)  (Ø20.0)
A_KNUCK = 12.2        # [MEASURE] nửa bề rộng lớn nhất trong khoảng ôm (khớp MCP)
                      #   → dùng làm "ngân sách ΔX" (xem docs: quy tắc ΔX)
H_RING = 14.0         # [BRIEF] chiều dài trục của vòng (12–16 mm)
H_PAD = 9.0           # [EST]   chiều cao trục của đệm TPU
N_PAD = 4             # [EST]   số đệm tiếp xúc (4 góc phần tư = 4 điểm tựa xác định)

# Khe hở lắp (bán kính) giữa lòng vòng PETG và da, ở vùng KHÔNG có đệm.
# Vùng cảm biến (vách mu) = khe hở này ⇒ phim Velostat+đồng (~0.25 mm) vừa khít.
GAP_FIT = 0.28        # [EST]
SENSOR_T = 0.25       # [EST] chiều dày chồng cảm biến (Velostat + băng đồng + keo)
SENSOR_PHI0 = 74.0    # [EST] cửa sổ vách cảm biến trên mặt mu (độ)
SENSOR_PHI1 = 106.0

# =============================================================================
# 2. RÀNG BUỘC HÌNH HỌC (HARD CONSTRAINTS từ brief)
# =============================================================================
DX_MAX = 2.0          # [BRIEF] độ nhô ngang tối đa sang mỗi sườn (mm)
T_SIDE = 1.75         # [EST] chiều dày thành tại sườn (đường giữa bên 0°/180°)
T_DV = 2.60           # [EST] chiều dày thành tại mu/lòng (nơi không có ngón kề)
RELIEF_D = 0.60       # [EST] khoét lõm ngoài tại đường giữa bên (giảm ΔX)
RELIEF_PHI = 15.0     # [EST] nửa độ rộng cung khoét lõm đó
TAPER_DROP = 0.55     # [EST] vuốt côn đầu xa (bám theo độ thon của ngón) — giảm ΔX đầu xa
TAPER_Z0 = 8.5        # [EST] z bắt đầu vuốt côn

# =============================================================================
# 3. CƠ CẤU Ý TƯỞNG 1 — VÒNG KHOÁ QUÁ TÂM KIỂU MÓC SƯỜN (Side Toggle Clasp)
# =============================================================================
SLIT_PHI = 61.0       # [EST] vị trí khe hở (độ, lệch khỏi sườn về phía mu → an toàn)
GAP_SLIT = 0.45       # [EST] khe hở thật giữa mặt đầu THÂN và mặt đầu TAY KẸP (mm)
HINGE_PHI = 336.0     # [EST] tâm bản lề mềm (độ)
RELIEF_HINGE = 30.0   # [EST] cửa sổ nhả vật liệu quanh bản lề (độ) — chống va chạm khi mở
WAIST_ARC = 42.0      # [EST] cung của lá bản lề (độ) — phần chui vào thân 2 bên
T_HINGE = 0.50        # [EST] chiều dày lá bản lề (mm) — quyết định biến dạng
Z_HINGE0, Z_HINGE1 = 2.5, 11.5   # [EST] chiều cao lá bản lề theo Z

T_LINK = 0.50         # [EST] eo lá khớp của thanh truyền (link)
W_LINK_RIGID = 2.2    # [EST] bề dày phần cứng của thanh truyền
L_WAIST = 2.6         # [EST] chiều dài mỗi eo lá khớp
H_LEVER = 8.0         # [EST] chiều cao Z của cần gạt / thanh truyền

OPEN_ANGLE_DEG = 17.0  # [EST] góc mở của tay kẹp ở trạng thái IN (chưa gài)
PEG_R = 1.5           # [EST] bán kính chốt (trục) trên tay kẹp
SCARF_DEG = 30.0      # [EST] góc vát của khe hở (chống kẹp da, tăng diện tích tựa)
STOP_GAP = 0.05       # [EST] khe hở danh nghĩa giữa mặt tựa cứng khi đã khoá

# =============================================================================
# 4. CƠ CẤU Ý TƯỞNG 2 — ĐAI RĂNG CƯA VI SAI + LÒ XO MEANDER (Ratchet Cinch)
# =============================================================================
RATCHET_PITCH_MM = 0.80   # [EST] bước răng (độ phân giải điều chỉnh) — càng nhỏ càng "khít"
RATCHET_TOOTH_H = 0.55    # [EST] chiều cao răng
RATCHET_N = 22            # [EST] số răng trên đai
STRAP_T = 0.90            # [EST] chiều dày đai (in TPU hoặc PETG mỏng)
MEANDER_K = 1.10          # [EST] độ cứng lò xo meander (N/mm) — GIỚI HẠN ÁP SUẤT
MEANDER_STROKE = 2.0      # [EST] hành trình lò xo meander (mm) ⇒ F_max = 2.2 N
LEVER_RATIO = 2.6         # [EST] tỉ số đòn bẩy của cần siết (giảm lực tay bệnh nhân)

# =============================================================================
# 5. CƠ CẤU Ý TƯỞNG 3 — BĂNG QUẤN XOẮN TỰ SIẾT CÓ CHẶN HÀNH TRÌNH (Wrap Band)
# =============================================================================
WRAP_TURNS = 2.4          # [EST] số vòng quấn
WRAP_T = 1.10             # [EST] chiều dày băng (hướng kính)
WRAP_H = 9.0              # [EST] chiều cao băng (theo Z)
WRAP_GAP = 0.55           # [EST] khe giữa 2 vòng liền kề khi CHƯA siết
WEDGE_DEG = 20.0          # [EST] góc nêm chuyển lực dọc trục → lực tiếp tuyến (tự siết)
WEDGE_STOP = 1.4          # [EST] hành trình nêm tối đa (mm) = CHẶN ÁP SUẤT CỨNG

# =============================================================================
# 6. VẬT LIỆU (giá trị [LIT]/[EST] — phải đo lại trên mẫu in thật)
# =============================================================================
RHO_PETG = 1.27e-3        # g/cm^3 → dùng để ước lượng khối lượng
RHO_TPU = 1.21e-3
E_PETG = 1200.0           # [EST] MPa, mô đun hiệu dụng mẫu in FDM (không phải 2000 nominal)
E_TPU85 = 4.0             # [EST] MPa, TPU 85A ở biến dạng nhỏ
EPS_ALLOW = 0.015         # [EST] biến dạng bền mỏi cho phép của PETG in FDM (1.5%)
MU_DESIGN = 0.80          # [LIT-E] μ thiết kế TPU–da (Zhang & Mak 1999: silicone 0.61±0.21)
MU_OPT = 1.10             # [LIT-E] μ lạc quan (đệm TPU 85A bám, da ẩm nhẹ)

# =============================================================================
# 7. NGÂN SÁCH ÁP SUẤT TIẾP XÚC (an toàn mô mềm) — NGÂN SÁCH, KHÔNG PHẢI KẾT QUẢ ĐO
# =============================================================================
P_SAFE_CONT = 8.0         # [LIT-E] kPa (≈60 mmHg) cho đeo liên tục nhiều giờ
P_SAFE_INTER = 20.0       # [LIT-E] kPa (≈150 mmHg) cho kích hoạt ngắt quãng (<2 phút)
F_TENDON_NOM = 25.0       # [BRIEF] lực gân danh nghĩa cần chịu theo trục ngón (N)
F_TENDON_SAFE = 10.0      # [EST] lực khuyến nghị cho 1 vòng P1 đơn độc (xem báo cáo §2)


# =============================================================================
# HÀM DẪN XUẤT + TỰ KIỂM TRA
# =============================================================================
def a_in():
    return A_F1 + GAP_FIT


def b_in():
    return B_F1 + GAP_FIT


def a_out():
    return A_F1 + GAP_FIT + T_SIDE


def b_out():
    return B_F1 + GAP_FIT + T_DV


def contact_area_mm2():
    """Diện tích tiếp xúc thực của N_PAD đệm (ước lượng hình học, mm^2)."""
    # mỗi đệm: cung ~ (360/N_PAD - 20) độ ở bán kính a_in, cao H_PAD
    arc_deg = 360.0 / N_PAD - 20.0
    arc_len = math.pi * a_in() * arc_deg / 180.0
    return N_PAD * arc_len * H_PAD


def budget_table():
    """Bảng cân bằng lực: ngân sách ma sát ở các mức áp suất khác nhau."""
    import math
    A = contact_area_mm2()
    rows = []
    for p in (5.0, 8.0, 10.0, 15.0, 20.0):
        N = p * 1e-3 * A          # kPa * mm^2 = N
        rows.append((p, N, MU_DESIGN * N, MU_OPT * N))
    return A, rows


import math  # noqa: E402  (đặt cuối để tránh vòng import khi copy file)
