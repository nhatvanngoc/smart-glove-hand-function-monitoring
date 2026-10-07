# -*- coding: utf-8 -*-
"""
Ý TƯỞNG 3 — ĐAI QUẤN SIẾT CƠ HỌC + CHÊM TỰ HÃM (Wrap Band + Self-Locking Wedge)
================================================================================
HỌ NGUYÊN LÝ KHÁC ý tưởng 1 (đòn bẩy quá tâm) và ý tưởng 2 (răng cóc):
KHÔNG bản lề sống, KHÔNG răng cóc, KHÔNG khớp quá tâm. Ba cơ chế tách bạch:

  1) ĐAI QUẤN 355° × 0.80 × 9.0 mm (in CÙNG vật liệu với khung): lực kẹp do
     LỰC CĂNG CƠ HỌC T (kéo đầu đai bằng tay rồi chêm giữ), KHÔNG do ép đàn hồi
     ⇒ áp lực phân bố trên toàn cung 355° (A_tiếp xúc 649 mm² — gấp 2,01× tổng
     diện tích 4 đệm cánh của ý tưởng 1/2) ⇒ áp lực đỉnh thấp nhất.
  2) GỜ MÓC + RÃNH TRÊN SÀN MÁNG (form closure): gờ đai cắm vào rãnh khung,
     chặn trượt TIẾP TUYẾN bằng HÌNH HỌC (τ 2.08 MPa), không bằng ma sát,
     không bằng keo dán.
  3) CHÊM 10° TỰ HÃM: chêm trượt trong máng khung, lực căng đai kéo chêm SÂU
     THÊM. tan 10° = 0.176 ≤ μ(nhựa–nhựa)/1.3 = 0.231 (μ_self 0.30 = ngân sách
     thiết kế, CẦN ĐO TRÊN BĂNG THỬ) ⇒ biên 1.31×. Nhả bằng cách miết ngược.

Vì sao giải được kẹp sườn ngón + biến dạng mô mềm:
  – Khung chỉ nằm ở NỬA LƯNG (φ 88°–152°); nửa sườn (φ≈0° và φ≈180°) trống hoàn
    toàn ⇒ không giành chỗ với ngón kế cận, không có đòn bẩy thò ra sườn.
  – Áp lực kẹp phân bố liên tục trên cung 355°: không "điểm tì" cứng, không
    "nhấp nhả" như răng cóc.
  – Chêm tì lên mặt NGOÀI đai: phản lực kẹp đi vào VÒM KHUNG, không tăng áp lực
    lên da tại chỗ chêm.

GIỚI HẠN ĐÃ BIẾT (ghi thẳng — nằm trong mục "mở" của báo cáo; số của bản này):
  – Đánh đổi S7 KHÔNG thể đồng thời: T = 9.0 N ⇒ giữ trục 25.4 N nhưng p = 87.2 kPa
    (vượt 20 kPa); muốn p = 20 kPa thì T = 2.06 N và chỉ giữ được 5.8 N.
    ⇒ MỘT vòng P1 chưa đủ 25 N; cần chia tải qua P1+P2 (2 đai) hoặc tăng chiều
    rộng đai. Đây là phép kiểm "thông tin", không phải PASS giả.
  – Tải TRỤC đi qua 2 VAI MÁNG bằng form closure (σ_bearing = 25 N / 130 mm² =
    0.19 MPa) — KHÔNG cần keo dán (bản TPU cũ mới cần keo).

Xuất: stl/idea3/{Ring_<MAT> (khung), Band_<MAT> (đai), Wedge_<MAT> (chêm)}.stl
Kiểm: 13 mục S1–S11 + G1 (in ở cuối).
"""

import math
import os
import sys

import FreeCAD as App
import Part
import Mesh

def _script_dir():
    """Thư mục chứa script — chạy được cả khi exec() trong FreeCAD GUI (không có __file__)."""
    if "__file__" in globals():
        return os.path.dirname(os.path.abspath(__file__))
    _cwd = os.getcwd()
    for _d in (_cwd, os.path.join(_cwd, "hardware", "finger_fixation")):
        if os.path.isfile(os.path.join(_d, "params.py")):
            return _d
    raise RuntimeError("Không tìm thấy params.py cạnh script — hãy chạy run_in_freecad.py "
                       "(hoặc cd hardware/finger_fixation trước khi exec).")


_here = _script_dir()
if _here not in sys.path:
    sys.path.insert(0, _here)

import params as P            # noqa: E402
import fcgeom as G            # noqa: E402
import ring_common as RC      # noqa: E402

OUT_DIR = os.path.join(_here, "stl")
_D = G.deg

# ============================================================ 1. THÔNG SỐ ===
FRAME_PHI0, FRAME_PHI1 = 88.0, 152.0       # khung chỉ ở nửa lưng
FRAME_Z0, FRAME_Z1 = 0.00, 13.00
FRAME_R_IN = 2.05                          # mặt trong vòm (trên đai-da 0,20 khe)
FRAME_RO = ((88.0, 2.90), (98.0, 6.30), (142.0, 6.30), (152.0, 2.90))  # r_ngoài (so a_in)
GROOVE_FLOOR = 2.75                        # sàn máng (đai nằm ở 2,85 → khe 0,10)
ROOF_R0, ROOF_R1 = 5.45, 4.35              # trần máng: 5,45 phẳng → 4,35 (họng chêm)
ROOF_PHI0, ROOF_RAMP0, ROOF_RAMP1 = 120.0, 128.0, 142.0

BAND_PHI0, BAND_PHI1 = 95.0, 450.0         # cung tiếp xúc da 355° (hở 5° ở lưng)
# ĐAI MỘT VẬT LIỆU (PLA/ABS): KHÔNG còn dựa vào biến dạng đàn hồi ε=6 % như bản TPU.
# Nhựa cứng có E ≈ 2–3,5 GPa (TPU 85A chỉ 4 MPa ⇒ gấp ~500–900 lần): nếu vẫn ép đai
# vào cỡ nhỏ hơn để "tự căng", lực căng sẽ lên tới hàng trăm N và phá vòng. Vì vậy:
#   * Đai in SẴN theo đúng cung (đúc cong), chỉ cần mở ~1,5 mm bán kính khi xỏ ngón
#     ⇒ biến dạng khi mở chỉ ~0,4 % (xem S2b), nằm dưới giới hạn mọi vật liệu.
#   * LỰC CĂNG do NGƯỜI DÙNG kéo/đẩy chêm sang ngang (căng cơ học), KHÔNG do đàn hồi.
#   * Khoá một chiều bằng CHÊM 10° tự hãm với μ(nhựa–nhựa) ≈ 0,30.
BAND_R0, BAND_T = 0.35, 0.80               # khe hở da 0,35 | dày 0,80 = 2 đường in
BAND_Z0, BAND_Z1 = 2.00, 11.00
RISER_PHI = 95.0
OUT_PHI0, OUT_PHI1 = 95.0, 146.0           # đoạn đai TRONG máng khung (dưới chêm)
OUT_R0 = 2.85                              # = sàn 2,75 + 0,10 khe
OUT_R1 = OUT_R0 + BAND_T                   # 4,35
OUT_Z0, OUT_Z1 = 2.60, 10.40               # vai máng: z 0–2,60 và 10,60–13 (khe 0,20)

# GỜ MÓC (form closure chặn trượt TIẾP TUYẾN) — SỬA LỖI 2026-10-07:
#   Bản cũ khai KEY_R1 = 3,50 với đai dày 1,50 (mặt ngoài 4,35) ⇒ "gờ" nằm LỌT TRONG
#   bề dày đai, KHÔNG hề nhô ra ⇒ chưa từng ăn vào rãnh (chặn tiếp tuyến thực chất
#   chỉ nhờ ma sát). Nay gờ nhô VÀO TRONG khỏi mặt trong đai để cắm vào rãnh khoét
#   trên SÀN MÁNG của khung: đai trong 2,85 → gờ 2,45…2,90 (nhô 0,40; ngập 0,05 vào đai).
KEY_PHI0, KEY_PHI1 = 106.0, 116.0          # gờ móc (10° ≈ 2,5 mm cung)
KEY_R0, KEY_R1 = 2.45, 2.90
KEY_Z0, KEY_Z1 = 3.50, 8.50
NOTCH_PHI0, NOTCH_PHI1 = 105.85, 116.15    # rãnh trên sàn máng (khe 0,15° ≈ 0,03 mm cung)
NOTCH_R0, NOTCH_R1 = 2.35, 2.90            # đáy rãnh 2,35 → còn 0,30 mm vách (lòng 2,05)
NOTCH_Z0, NOTCH_Z1 = 3.40, 8.60

# LƯU Ý CHIỀU: trong hệ local_frame, trục u chạy theo chiều −φ. Chêm bị ĐẨY về
# phía φ LỚN (vào họng 128°→142°) ⇒ đầu MỎNG nằm ở u NHỎ (φ≈128°), đầu DÀY ở u LỚN.
WEDGE_PHI = 124.0
# CHÊM 10° (thay 20°): góc phải thoả tan θ ≤ μ_nhựa–nhựa/1,3 thì mới TỰ HÃM. Với bản
# TPU, μ(TPU–PETG) ≈ 0,80 cho phép 20°; nhựa cứng trượt trên nhựa cứng chỉ ≈ 0,30
# ⇒ θ ≤ 13° ⇒ chọn 10° (biên 1,3×). Đổi lại: hành trình siết DÀI hơn (≈4,3 mm).
WEDGE_DEG = 10.0
WEDGE_TIP_H, WEDGE_BACK_H = 0.10, 0.85     # vào được họng (mỏng) → kẹt lại (dày)
WEDGE_RAMP_L = (WEDGE_BACK_H - WEDGE_TIP_H) / math.tan(_D(WEDGE_DEG))
WEDGE_U_TIP = -0.90
WEDGE_U_BACK = WEDGE_U_TIP + WEDGE_RAMP_L
PAD_U0, PAD_U1 = 5.07, WEDGE_U_BACK        # tấm miết ngón cái (vùng máng KHÔNG nắp)
PAD_V1 = 5.00
WEDGE_Z0, WEDGE_Z1 = OUT_Z0, OUT_Z1

T_CINCH = 9.00                             # [EST] lực căng ĐẶT BẰNG TAY (N) — đủ giữ 25 N
DON_R_OPEN = 1.50                          # [EST] bán kính đai phải MỞ thêm khi xỏ ngón (mm)
SHEAR_ALLOW = P.sig_allow() / math.sqrt(3.0)   # τ cho phép (von Mises) ≈ 0,577·σ_cho phép
TAU_ALLOW_MAX = 4.0                        # MPa, trần thiết kế cũ (giữ để so sánh)


def r_out_frame(phi):
    for (p0, r0), (p1, r1) in zip(FRAME_RO, FRAME_RO[1:]):
        if p0 <= phi <= p1:
            return r0 + (r1 - r0) * (phi - p0) / (p1 - p0)
    return FRAME_RO[0][1] if phi < FRAME_RO[0][0] else FRAME_RO[-1][1]


def roof_in(phi):
    """Mặt dưới trần máng (chỉ có nắp ở φ ≥ 120°): 5,45 → 4,35 (họng chêm 20°)."""
    if phi <= ROOF_RAMP0:
        return ROOF_R0
    t = min(1.0, (phi - ROOF_RAMP0) / (ROOF_RAMP1 - ROOF_RAMP0))
    return ROOF_R0 + (ROOF_R1 - ROOF_R0) * t


def ceil_in(phi):
    """Trần thực của máng: hở nắp ở vùng miết chêm, có nắp (5,45→4,35) ở họng.

    +0,35 mm ở mép ngoài để dao cắt KHÔNG trùng mặt với mặt ngoài khung (trùng mặt
    ⇒ tessellate sinh tam giác diện tích ~0 — đúng lỗi đã gặp ở ý tưởng 1).
    """
    if phi < ROOF_PHI0:
        return r_out_frame(phi) + 0.35
    return min(r_out_frame(phi) + 0.35, roof_in(phi))


def var_band(phi0, phi1, r_in_fn, r_out_fn, z0, z1, n=200):
    """Lăng trụ vành khuyên có bán kính trong/ngoài biến thiên theo φ."""
    outer = [RC.polar(G.ell_r(P.a_in() + r_in_fn(phi), P.b_in() + r_in_fn(phi), phi), phi)
             for phi in (phi0 + (phi1 - phi0) * i / n for i in range(n + 1))]
    inner = [RC.polar(G.ell_r(P.a_in() + r_out_fn(phi), P.b_in() + r_out_fn(phi), phi), phi)
             for phi in (phi1 - (phi1 - phi0) * i / n for i in range(n + 1))]
    return RC.prism(outer + inner, z0, z1)


# ================================ 2. KHUNG LƯNG (một vật liệu) ============
frame = var_band(FRAME_PHI0, FRAME_PHI1, lambda p: FRAME_R_IN,
                 r_out_frame, FRAME_Z0, FRAME_Z1)
# GHI CHÚ (sửa lỗi lưới 2026-10): bản trước có thêm dao `ch_skin` cắt kênh da
# (r_in = BAND_R0−0.20 → r_out = BAND_R0+BAND_T+0.20 = 2,05 mm offset). Nhưng
# 2,05 mm CHÍNH LÀ bán kính lòng khung (FRAME_R_IN) ⇒ mặt dao TRÙNG khít mặt
# lòng khung ⇒ OCCT tách mặt tại đường trùng rồi tessellate sinh tam giác
# diện tích ~0 (đúng lỗi đã gặp ở Ý TƯỞNG 1/2). Không cần dao này nữa: lòng
# khung (2,05) đã tự chừa khe hở 0,20 mm cho mặt ngoài đai phần da (1,85 mm
# offset) ⇒ BỎ dao, lưới sạch (kiểm bằng headless/mesh_qa.py: 0 tam giác suy biến).
ch_out = var_band(FRAME_PHI0, FRAME_PHI1, lambda p: GROOVE_FLOOR, ceil_in,
                  OUT_Z0 - 0.2, OUT_Z1 + 0.2)
# Rãnh móc: đáy rãnh nằm SÂU hơn sàn máng 0,15 mm (bản trước 0,02 mm ⇒ hai mặt
# gần trùng nhau, sinh 2 tam giác diện tích ~5e-5 mm² khi tessellate).
notch = RC.band_prism(P.a_in() + NOTCH_R0, P.b_in() + NOTCH_R0,
                      P.a_in() + NOTCH_R1 + 0.10, P.b_in() + NOTCH_R1 + 0.10,
                      NOTCH_PHI0, NOTCH_PHI1, NOTCH_Z0, NOTCH_Z1, n=60)
riser_slot = RC.band_prism(P.a_in() + BAND_R0 - 0.45, P.b_in() + BAND_R0 - 0.45,
                          P.a_in() + OUT_R1 + 0.25, P.b_in() + OUT_R1 + 0.25,
                          RISER_PHI - 5.2, RISER_PHI + 5.2, OUT_Z0 - 0.20, OUT_Z1 + 0.20, n=60)
# CẮT MỘT LƯỢT: ba dao dùng chung mặt phẳng z = 2,40 / 10,60 — cắt
# trong một phép BOP để OCCT hợp nhất mặt trùng giữa các dao thay vì để lại vết.
# Cắt lần lượt từng dao (FreeCAD chỉ nhận 1 đối tượng cho cut()); sau đó
# removeSplitter() hợp nhất các mặt đồng phẳng do boolean để lại ⇒ lưới sạch.
frame = frame.cut(ch_out).cut(notch).cut(riser_slot).removeSplitter()

# ============================ 3. ĐAI QUẤN 355° (một vật liệu) ===============
band = RC.band_prism(P.a_in() + BAND_R0, P.b_in() + BAND_R0,
                     P.a_in() + BAND_R0 + BAND_T, P.b_in() + BAND_R0 + BAND_T,
                     BAND_PHI0, BAND_PHI1, BAND_Z0, BAND_Z1, n=260)
riser = RC.band_prism(P.a_in() + BAND_R0 - 0.05, P.b_in() + BAND_R0 - 0.05,
                     P.a_in() + OUT_R1, P.b_in() + OUT_R1,
                     RISER_PHI - 4.5, RISER_PHI + 4.5, OUT_Z0, OUT_Z1, n=60)
out_seg = RC.band_prism(P.a_in() + OUT_R0, P.b_in() + OUT_R0, P.a_in() + OUT_R1, P.b_in() + OUT_R1,
                        OUT_PHI0, OUT_PHI1, OUT_Z0, OUT_Z1, n=140)
key = RC.band_prism(P.a_in() + KEY_R0, P.b_in() + KEY_R0, P.a_in() + KEY_R1, P.b_in() + KEY_R1,
                    KEY_PHI0, KEY_PHI1, KEY_Z0, KEY_Z1, n=40)
belt = RC.union_all([band, riser, out_seg, key]).removeSplitter()

# ================================== 4. CHÊM TỰ HÃM (nêm 10°) ===============
wedge_pts = [(WEDGE_U_TIP, OUT_R1), (WEDGE_U_TIP, OUT_R1 + WEDGE_TIP_H),
             (WEDGE_U_BACK, OUT_R1 + WEDGE_BACK_H), (PAD_U0, OUT_R1 + WEDGE_BACK_H),
             (PAD_U0, OUT_R1)]
pad_pts = [(PAD_U0, OUT_R1), (PAD_U1, OUT_R1), (PAD_U1, PAD_V1), (PAD_U0, PAD_V1)]
wedge = RC.union_all([
    RC.local_prism(wedge_pts, WEDGE_PHI, G.ell_r(P.a_in(), P.b_in(), WEDGE_PHI), WEDGE_Z0, WEDGE_Z1),
    RC.local_prism(pad_pts, WEDGE_PHI, G.ell_r(P.a_in(), P.b_in(), WEDGE_PHI),
                   OUT_Z0 + 0.2, OUT_Z1 - 0.2)]).removeSplitter()

# ======================================================= 5. SỐ LIỆU KIỂM =====
r_wrap = P.a_in() + BAND_R0 + BAND_T / 2.0
wrap_deg = BAND_PHI1 - BAND_PHI0
A_contact = _D(wrap_deg) * r_wrap * (BAND_Z1 - BAND_Z0)
# MÔ HÌNH LỰC (đai căng cơ học): lực căng T do người dùng đặt khi siết chêm.
# Vòng đai chịu lực căng T ⇒ tổng phản lực kính ΣN = 2πT (kết quả chuẩn của vòng
# mềm chịu căng). Đai KHÔNG còn dựa vào biến dạng đàn hồi ε (bản TPU cũ).
T_design = T_CINCH
SIG_N = 2.0 * math.pi * T_design
p_mean = SIG_N / A_contact
F_fric = P.MAT.mu * SIG_N
T_for_cap = P.P_SAFE_INTER * 1e-3 * A_contact / (2.0 * math.pi)     # T ứng với p = 20 kPa
F_hold_cap = P.MAT.mu * 2.0 * math.pi * T_for_cap
sig_strap = T_design / (BAND_T * (BAND_Z1 - BAND_Z0))               # kéo dọc đai (MPa)
eps_don = 0.5 * BAND_T * (1.0 / (P.a_in() + BAND_R0) - 1.0 / (P.a_in() + BAND_R0 + DON_R_OPEN))
key_w = _D(KEY_PHI1 - KEY_PHI0) * (P.a_in() + KEY_R1)
A_key = key_w * (KEY_Z1 - KEY_Z0)
tau_key = P.F_TENDON_NOM / A_key
A_shoulder = _D(FRAME_PHI1 - FRAME_PHI0) * (P.a_in() + OUT_R1) * (BAND_Z1 - BAND_Z0 - 1.0)
sigma_axial = P.F_TENDON_NOM / A_shoulder
taper_deg = math.degrees(math.atan((WEDGE_BACK_H - WEDGE_TIP_H) / WEDGE_RAMP_L))
gap_throat = ROOF_R1 - GROOVE_FLOOR          # khe nhỏ nhất ở họng (1,60 mm)
gap_mouth = ROOF_R0 - GROOVE_FLOOR           # khe lớn (2,70 mm)
st = RC.stats(frame, [], ref_lat=None)
st["vol_tpu_cm3"] = belt.Volume / 1000.0          # tên giữ để tương thích bảng tổng hợp
st["mass_tpu"] = belt.Volume / 1000.0 * P.MAT.rho
st["mass_wedge"] = wedge.Volume / 1000.0 * P.MAT.rho

RC.check("S1. Đai quấn ≥ 300° (áp lực phân bố, không điểm tì cứng)",
         wrap_deg >= 300.0,
         "cung quấn %.0f° | A_tiếp xúc ≈ %.0f mm² (gấp %.2f× diện tích đệm ý tưởng 1) | "
         "tiết diện đai %.2f × %.1f mm²" % (wrap_deg, A_contact, A_contact / 323.0,
                                            BAND_T, BAND_Z1 - BAND_Z0))
RC.check("S2. Đai in được ở nozzle 0,4 (≥ 2 đường) + lực căng cơ học (không ép đàn hồi)",
         2 * 0.40 - 1e-9 <= BAND_T,
         "%s dày %.2f mm = %.1f đường in | T_đặt = %.2f N (do người dùng siết chêm) ⇒ "
         "ΣN = 2πT = %.1f N | σ_kéo_đai = %.2f MPa (nhỏ)"
         % (P.MAT.key, BAND_T, BAND_T / 0.40, T_design, SIG_N, sig_strap))
RC.check("S2b. Mở đai ~%.1f mm bán kính để xỏ ngón: biến dạng ≤ ε_cho phép (%.1f %%)"
         % (DON_R_OPEN, P.MAT.eps_allow * 100),
         eps_don <= P.MAT.eps_allow,
         "ε_mở = %.2f %% ≤ %.2f %% (%s) — đai IN SẴN theo cung nên chỉ cần nới nhẹ; "
         "KHÔNG dùng đai như lò xo đàn hồi"
         % (eps_don * 100, P.MAT.eps_allow * 100, P.MAT.key))
RC.check("S3. Gờ móc chặn trượt TIẾP TUYẾN bằng hình học (form closure), τ ở 25 N",
         tau_key <= min(SHEAR_ALLOW, TAU_ALLOW_MAX),
         "gờ %.1f mm cung × %.1f mm cao = %.1f mm² ⇒ τ = %.2f ≤ %.2f MPa "
         "(= σ_cho phép/√3; trần cũ 4,0 MPa)" % (key_w, KEY_Z1 - KEY_Z0, A_key, tau_key,
                                                 min(SHEAR_ALLOW, TAU_ALLOW_MAX)))
RC.check("S4. Tải TRỤC đi qua 2 VAI MÁNG bằng FORM CLOSURE (không cần keo)",
         sigma_axial <= 1.0,
         "σ_bearing = 25 N / %.0f mm² = %.2f MPa trên vai máng z 0–2,60 và 10,60–13 | "
         "đai nằm TRONG máng nên hai vai chặn trượt dọc trục bằng HÌNH HỌC; gờ móc (S3) "
         "chặn trượt tiếp tuyến ⇒ KHÔNG cần lớp dán kết cấu (đã bỏ theo ràng buộc mới)"
         % (A_shoulder, sigma_axial))
RC.check("S5. Chêm TỰ HÃM: tan θ ≤ μ(nhựa–nhựa)/1,3 = %.3f"
         % (P.MAT.mu_self / 1.3),
         math.tan(_D(taper_deg)) <= P.MAT.mu_self / 1.3,
         "góc chêm thực %.1f° (thiết kế %.0f°) → tan %.3f ≤ %.3f ⇒ biên %.2f× | "
         "μ(nhựa–nhựa) = %.2f [LIT] ⇒ lực căng đai KÉO CHÊM SÂU THÊM (tự cưỡng hoá); "
         "nhả bằng cách miết ngược đầu đai"
         % (taper_deg, WEDGE_DEG, math.tan(_D(taper_deg)), P.MAT.mu_self / 1.3,
            (P.MAT.mu_self / 1.3) / math.tan(_D(taper_deg)), P.MAT.mu_self))
RC.check("S6. Chêm VÀO được họng (mỏng đầu) và KẸT lại (dày cuối) — tự hãm",
         BAND_T + WEDGE_TIP_H <= gap_mouth and BAND_T + WEDGE_BACK_H > gap_throat,
         "đầu mỏng: %.2f + %.2f = %.2f ≤ khe miệng %.2f | đầu dày: %.2f + %.2f = %.2f > "
         "khe họng %.2f ⇒ kẹt đúng họng, không lọt qua"
         % (BAND_T, WEDGE_TIP_H, BAND_T + WEDGE_TIP_H, gap_mouth,
            BAND_T, WEDGE_BACK_H, BAND_T + WEDGE_BACK_H, gap_throat))
RC.check("G1. MỘT VẬT LIỆU (%s) cho cả khung, đai và chêm — không keo, không TPU"
         % P.MAT.key,
         P.MAT.key in ("PLA", "ABS"),
         "E=%.0f MPa, σ_y=%.0f MPa, ρ=%.2f g/cm³, μ da = %.2f, μ nhựa–nhựa = %.2f"
         % (P.MAT.E, P.MAT.sig_y, P.MAT.rho, P.MAT.mu, P.MAT.mu_self))
RC.check("S7. Ngân sách kẹp (thông tin): hai chế độ KHÔNG thể đồng thời đạt",
         True,
         "CHẾ ĐỘ ĐỦ TẢI: T = %.2f N ⇒ ΣN = %.1f N, giữ trục ≈ %.1f N (μ=%.2f) NHƯNG "
         "p ≈ %.1f kPa > 20 kPa | CHẾ ĐỘ ĐỦ AN TOÀN: p = 20 kPa ⇒ T = %.2f N, chỉ giữ "
         "≈ %.1f N. MỘT vòng P1 không thể vừa giữ 25 N vừa dưới 20 kPa ⇒ cần chia tải "
         "sang 2 đốt (P1+P2) — mục 'mở' của báo cáo"
         % (T_design, SIG_N, F_fric, P.MAT.mu, p_mean * 1000.0, T_for_cap, F_hold_cap))
RC.check("S8. Khung – đai – chêm KHÔNG chồng khối (khe hở lắp ráp thật)",
         frame.common(belt).Volume <= 1e-3 and frame.common(wedge).Volume <= 1e-3
         and belt.common(wedge).Volume <= 1e-3,
         "V_chung: khung∩đai = %.4f | khung∩chêm = %.4f | đai∩chêm = %.4f mm³"
         % (frame.common(belt).Volume, frame.common(wedge).Volume, belt.common(wedge).Volume))
r_key_arc = G.ell_r(P.a_in() + KEY_R0, P.b_in() + KEY_R0, KEY_PHI0)
gap_phi0 = _D(KEY_PHI0 - NOTCH_PHI0) * r_key_arc          # khe hở TIẾP TUYẾN mỗi bên
gap_phi1 = _D(NOTCH_PHI1 - KEY_PHI1) * r_key_arc
gap_rad = KEY_R0 - NOTCH_R0                                # khe hở ĐÁY RÃNH (hướng kính)
depth_in = P.a_in() + GROOVE_FLOOR - (P.a_in() + KEY_R0)   # gờ ngập vào SÀN bao nhiêu
wall_left = NOTCH_R0 - FRAME_R_IN                         # vách còn lại dưới đáy rãnh
gap_z0 = KEY_Z0 - NOTCH_Z0                                 # khe hở DỌC TRỤC hai đầu
gap_z1 = NOTCH_Z1 - KEY_Z1
RC.check("S9. Gờ móc CẮM vào rãnh trên sàn máng (form closure chặn tiếp tuyến)",
         NOTCH_PHI0 < KEY_PHI0 and NOTCH_PHI1 > KEY_PHI1
         and NOTCH_Z0 < KEY_Z0 and NOTCH_Z1 > KEY_Z1
         and KEY_PHI0 > FRAME_PHI0 and KEY_PHI1 < ROOF_PHI0
         and gap_rad >= 0.05 and depth_in >= 0.20 and wall_left >= 0.25
         and min(gap_phi0, gap_phi1) >= 0.02 and max(gap_phi0, gap_phi1) <= 0.15
         and gap_z0 >= 0.05 and gap_z1 >= 0.05,
         "gờ φ %.0f–%.0f / r %.2f→%.2f / z %.1f–%.1f | rãnh φ %.2f–%.2f / đáy r %.2f / "
         "z %.2f–%.2f | gờ NGẬP %.2f mm vào sàn (vách còn %.2f) | khe: φ %.3f+%.3f | "
         "đáy %.2f | z %.2f+%.2f mm"
         % (KEY_PHI0, KEY_PHI1, KEY_R0, KEY_R1, KEY_Z0, KEY_Z1,
            NOTCH_PHI0, NOTCH_PHI1, NOTCH_R0, NOTCH_Z0, NOTCH_Z1,
            depth_in, wall_left, gap_phi0, gap_phi1, gap_rad, gap_z0, gap_z1))
RC.check("S10. In một khối liền: khung 1 khối, đai 1 khối, chêm 1 khối",
         len(frame.Solids) == 1 and len(belt.Solids) == 1 and len(wedge.Solids) == 1,
         "khung %d | đai %d | chêm %d khối"
         % (len(frame.Solids), len(belt.Solids), len(wedge.Solids)))
RC.check("S11. Khối hợp lệ (OCCT isValid) + Z trong 12–16 mm",
         bool(frame.isValid() and belt.isValid() and wedge.isValid()
              and 12.0 <= (FRAME_Z1 - FRAME_Z0) <= 16.0),
         "khung %s | đai %s | chêm %s | Z_khung = %.2f mm"
         % (frame.isValid(), belt.isValid(), wedge.isValid(), FRAME_Z1 - FRAME_Z0))

extras = [
    "-" * 78,
    "A. ĐAI QUẤN: %.0f° | %.2f × %.1f mm | V = %.2f cm³ ≈ %.2f g (%s)"
    % (wrap_deg, BAND_T, BAND_Z1 - BAND_Z0, st["vol_tpu_cm3"], st["mass_tpu"], P.MAT.key),
    "   T(siết chêm) = %.2f N ⇒ ΣN = 2πT = %.1f N | p ≈ %.1f kPa | giữ trục ≈ %.1f N"
    % (T_design, SIG_N, p_mean * 1000.0, F_fric),
    "   Chế độ an toàn (p = 20 kPa): T = %.2f N ⇒ giữ trục ≈ %.1f N | ε_mở đai = %.2f %%"
    % (T_for_cap, F_hold_cap, eps_don * 100),
    "B. KHUNG LƯNG: φ %.0f°–%.0f° | V = %.2f cm³ ≈ %.2f g (%s) | r_ngoài max = a_in+%.2f mm"
    % (FRAME_PHI0, FRAME_PHI1, st["vol_petg_cm3"], st["mass_petg"], P.MAT.key,
       max(r for _, r in FRAME_RO)),
    "   CHÊM: vát %.1f° | %.2f→%.2f mm | V = %.2f cm³ ≈ %.2f g | miệng %.2f mm → họng %.2f mm"
    % (taper_deg, WEDGE_TIP_H, WEDGE_BACK_H, wedge.Volume / 1000.0, st["mass_wedge"],
       gap_mouth, gap_throat),
    "C. ENVELOPE: %.2f × %.2f × %.2f mm | ΔX = %+.2f mm (ngân sách 2,00) | X_max = %.2f mm"
    % (frame.BoundBox.XLength, frame.BoundBox.YLength, frame.BoundBox.ZLength,
       st["dx_lat"], st["x_max"]),
]
_rc = RC.finish(frame, [], "Idea3_WrapBand", extras, subdir="idea3" + P.STL_SUFFIX,
                extra_parts=[("Band_" + P.MAT.key, belt), ("Wedge_" + P.MAT.key, wedge)])
RC.exit_code(_rc)   # FF_NO_SYS_EXIT=1 khi chạy trong FreeCAD GUI
