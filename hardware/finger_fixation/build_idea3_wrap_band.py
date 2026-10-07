# -*- coding: utf-8 -*-
"""
Ý TƯỞNG 3 — ĐAI QUẤN TỰ CƯỠNG HOÁ BẰNG CHÊM (Wrap Band + Self-Energising Wedge)
================================================================================
HỌ NGUYÊN LÝ KHÁC HẲN ý tưởng 1 (đòn bẩy quá tâm) và ý tưởng 2 (răng cưa):
KHÔNG bản lề sống, KHÔNG răng cưa, KHÔNG khớp quá tâm. Ba cơ chế tách bạch:

  1) ĐAI TPU 85A QUẤN 355° — lực kẹp sinh bởi BIẾN DẠNG ĐÀN HỒI (ε ≈ 6 %), phân
     bố trên TOÀN BỘ cung quấn ⇒ áp lực ĐỈNH thấp nhất trong 3 ý tưởng (không
     có bốn "điểm tì" rời như ý tưởng 1/2).
  2) GỜ MÓC + RÃNH MÓC (form closure) — gờ TPU trên đai ăn vào rãnh trên sàn
     máng khung: chặn trượt TIẾP TUYẾN bằng hình học, KHÔNG bằng ma sát.
  3) CHÊM 20° TỰ CƯỠNG HOÁ — chêm trượt TRÊN đai trong máng khung; lực căng
     của đai kéo chêm SÂU THÊM (không đẩy ra). tan 20° = 0,364 ≤ μ(TPU–PETG)/1,3
     ⇒ khoá một chiều; nhả bằng cách miết ngược đầu đai.

Vì sao giải được kẹp sườn ngón + biến dạng mô mềm:
  – Khung chỉ nằm ở NỬA LƯNG (φ 88°–152°); nửa sườn (φ≈0° và φ≈180°) trống hoàn
    toàn ⇒ không giành chỗ với ngón kế cận, không có đòn bẩy thò ra sườn.
  – Áp lực kẹp do biến dạng đàn hồi của đai, phân bố liên tục: không "điểm tì"
    cứng, không "nhấp nhả" như răng cưa.
  – Chêm tì lên mặt NGOÀI đai: toàn bộ phản lực kẹp đi vào VÒM KHUNG PETG,
    KHÔNG tăng áp lực lên da tại chỗ chêm.

GIỚI HẠN ĐÃ BIẾT (ghi thẳng — nằm trong mục "mở" của báo cáo):
  – Ở 25 N lực gân: ΣN = 2πT = 25 N ⇒ p_trung ≈ 40 kPa > ngưỡng 20 kPa của đề
    cương. CẢ BA ý tưởng đều vượt ngưỡng này khi chỉ dựa vào ma sát trên đốt gần
    ⇒ cần giảm tải hoặc tăng diện tích (đai rộng hơn / thêm đốt giữa).
  – Đường truyền tải TRỤC dựa vào vai máng (bearing 0,19 MPa trên TPU) + lớp
    DÁN kết cấu đai–khung; không dán thì TPU trượt dọc trục (biến dạng cắt ~15 %)
    ⇒ đây là yêu cầu LẮP RÁP, không phải chi tiết in.

Xuất: stl/idea3/{Ring_PETG (khung), Band_TPU (đai), Wedge_PETG (chêm)}.stl
Kiểm: 11 mục S1–S11 (in ở cuối).
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
BAND_R0, BAND_T = 0.35, 1.50               # khe hở da 0,35 | dày 1,50 (≈3,7 đường in)
BAND_Z0, BAND_Z1 = 2.00, 11.00
RISER_PHI = 95.0
OUT_PHI0, OUT_PHI1 = 95.0, 146.0           # đoạn đai TRONG máng khung (dưới chêm)
OUT_R0 = 2.85                              # = sàn 2,75 + 0,10 khe
OUT_R1 = OUT_R0 + BAND_T                   # 4,35
OUT_Z0, OUT_Z1 = 2.60, 10.40               # vai máng: z 0–2,60 và 10,60–13 (khe 0,20)

KEY_PHI0, KEY_PHI1 = 106.0, 116.0          # gờ móc TPU (10° ≈ 2,5 mm cung)
KEY_R1 = 3.50
KEY_Z0, KEY_Z1 = 3.50, 8.50
NOTCH_PHI0, NOTCH_PHI1 = 105.85, 116.15    # rãnh trên sàn máng (khe 0,15° ≈ 0,03 mm cung)
NOTCH_R1 = 3.60                            # rãnh trên sàn máng (khe 0,10 mọi phía)
NOTCH_Z0, NOTCH_Z1 = 3.40, 8.60

# LƯU Ý CHIỀU: trong hệ local_frame, trục u chạy theo chiều −φ. Chêm bị ĐẨY về
# phía φ LỚN (vào họng 128°→142°) ⇒ đầu MỎNG nằm ở u NHỎ (φ≈128°), đầu DÀY ở u LỚN.
WEDGE_PHI = 124.0
WEDGE_U_TIP, WEDGE_RAMP_L = -0.90, 2.47    # đầu mỏng 0,20 mm (φ≈128) → dày 1,10 mm (20°)
WEDGE_BACK_H, WEDGE_TIP_H = 1.10, 0.20
WEDGE_U_BACK = WEDGE_U_TIP + WEDGE_RAMP_L  # +1,57
PAD_U0, PAD_U1 = 5.07, WEDGE_U_BACK        # tấm miết ngón cái (vùng máng KHÔNG nắp)
PAD_V1 = 5.00
WEDGE_Z0, WEDGE_Z1 = OUT_Z0, OUT_Z1

BAND_STRETCH = 0.06
SHEAR_TPU_MAX = 4.0                        # MPa, giới hạn cắt thiết kế TPU 85A


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


# ====================================================== 2. KHUNG PETG =======
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
notch = RC.band_prism(P.a_in() + GROOVE_FLOOR - 0.15, P.b_in() + GROOVE_FLOOR - 0.15,
                      P.a_in() + NOTCH_R1, P.b_in() + NOTCH_R1,
                      NOTCH_PHI0, NOTCH_PHI1, NOTCH_Z0, NOTCH_Z1, n=60)
riser_slot = RC.band_prism(P.a_in() + BAND_R0 - 0.45, P.b_in() + BAND_R0 - 0.45,
                          P.a_in() + OUT_R1 + 0.25, P.b_in() + OUT_R1 + 0.25,
                          RISER_PHI - 5.2, RISER_PHI + 5.2, OUT_Z0 - 0.20, OUT_Z1 + 0.20, n=60)
# CẮT MỘT LƯỢT: ba dao dùng chung mặt phẳng z = 2,40 / 10,60 — cắt
# trong một phép BOP để OCCT hợp nhất mặt trùng giữa các dao thay vì để lại vết.
# Cắt lần lượt từng dao (FreeCAD chỉ nhận 1 đối tượng cho cut()); sau đó
# removeSplitter() hợp nhất các mặt đồng phẳng do boolean để lại ⇒ lưới sạch.
frame = frame.cut(ch_out).cut(notch).cut(riser_slot).removeSplitter()

# ======================================================= 3. ĐAI TPU 85A =====
band = RC.band_prism(P.a_in() + BAND_R0, P.b_in() + BAND_R0,
                     P.a_in() + BAND_R0 + BAND_T, P.b_in() + BAND_R0 + BAND_T,
                     BAND_PHI0, BAND_PHI1, BAND_Z0, BAND_Z1, n=260)
riser = RC.band_prism(P.a_in() + BAND_R0 - 0.05, P.b_in() + BAND_R0 - 0.05,
                     P.a_in() + OUT_R1, P.b_in() + OUT_R1,
                     RISER_PHI - 4.5, RISER_PHI + 4.5, OUT_Z0, OUT_Z1, n=60)
out_seg = RC.band_prism(P.a_in() + OUT_R0, P.b_in() + OUT_R0, P.a_in() + OUT_R1, P.b_in() + OUT_R1,
                        OUT_PHI0, OUT_PHI1, OUT_Z0, OUT_Z1, n=140)
key = RC.band_prism(P.a_in() + OUT_R0, P.b_in() + OUT_R0, P.a_in() + KEY_R1, P.b_in() + KEY_R1,
                    KEY_PHI0, KEY_PHI1, KEY_Z0, KEY_Z1, n=40)
belt = RC.union_all([band, riser, out_seg, key]).removeSplitter()

# ==================================================== 4. CHÊM PETG (nêm) ====
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
T_design = P.E_TPU85 * (BAND_T * (BAND_Z1 - BAND_Z0)) * BAND_STRETCH   # σ = E·ε ⇒ T = E·A·ε (KHÔNG chia chiều dài)
SIG_N = 2.0 * math.pi * T_design
p_mean = SIG_N / A_contact
F_fric = P.MU_DESIGN * SIG_N
key_w = _D(KEY_PHI1 - KEY_PHI0) * (P.a_in() + KEY_R1)
A_key = key_w * (KEY_Z1 - KEY_Z0)
tau_key = P.F_TENDON_NOM / A_key
A_shoulder = _D(FRAME_PHI1 - FRAME_PHI0) * (P.a_in() + OUT_R1) * (BAND_Z1 - BAND_Z0 - 1.0)
sigma_axial = P.F_TENDON_NOM / A_shoulder
taper_deg = math.degrees(math.atan((WEDGE_BACK_H - WEDGE_TIP_H) / WEDGE_RAMP_L))
gap_throat = ROOF_R1 - GROOVE_FLOOR          # khe nhỏ nhất ở họng (1,60 mm)
gap_mouth = ROOF_R0 - GROOVE_FLOOR           # khe lớn (2,70 mm)
st = RC.stats(frame, [], ref_lat=None)
st["vol_tpu_cm3"] = belt.Volume / 1000.0
st["mass_tpu"] = belt.Volume / 1000.0 * P.RHO_TPU * 1000.0
st["mass_wedge"] = wedge.Volume / 1000.0 * P.RHO_PETG * 1000.0

RC.check("S1. Đai quấn ≥ 300° (áp lực phân bố, không điểm tì cứng)",
         wrap_deg >= 300.0,
         "cung quấn %.0f° | A_tiếp xúc ≈ %.0f mm² (gấp %.2f× tổng 4 đệm ý tưởng 1 = 479 mm²) | "
         "tiết diện đai %.1f × %.1f mm²" % (wrap_deg, A_contact, A_contact / 479.0,
                                            BAND_T, BAND_Z1 - BAND_Z0))
RC.check("S2. Đai in được ở nozzle 0,4 (≥ 3 đường) + biến dạng đàn hồi ≤ 10 %",
         BAND_T >= 3 * 0.40 and BAND_STRETCH <= 0.10,
         "dày %.2f mm = %.1f đường in | ε ≈ %.0f %% ở Ø%.0f ⇒ T ≈ %.2f N (TPU 85A E=%.0f MPa)"
         % (BAND_T, BAND_T / 0.40, BAND_STRETCH * 100, P.D_NOM, T_design, P.E_TPU85))
RC.check("S3. Gờ móc chặn trượt TIẾP TUYẾN bằng hình học, τ ở 25 N ≤ 4 MPa",
         tau_key <= SHEAR_TPU_MAX,
         "gờ %.1f mm cung × %.1f mm cao = %.1f mm² ⇒ τ = %.2f MPa ≤ %.1f MPa (FS ≈ %.1f)"
         % (key_w, KEY_Z1 - KEY_Z0, A_key, tau_key, SHEAR_TPU_MAX, SHEAR_TPU_MAX / tau_key))
RC.check("S4. Tải TRỤC qua 2 vai máng: bearing ≤ 1 MPa (nền cho lớp dán kết cấu)",
         sigma_axial <= 1.0,
         "σ_bearing = 25 N / %.0f mm² = %.2f MPa (vai máng z 0–2,60 và 10,60–13) | "
         "yêu cầu DÁN đai–khung, nếu không TPU trượt dọc trục" % (A_shoulder, sigma_axial))
RC.check("S5. Chêm TỰ CƯỠNG HOÁ: tan(góc vát thực) ≤ μ(TPU–PETG)/1,3",
         math.tan(_D(taper_deg)) <= P.MU_DESIGN / 1.3,
         "góc vát thực %.1f° (thiết kế %.0f°) → tan %.3f ≤ %.3f ⇒ biên %.2f× (lực căng đai "
         "kéo chêm SÂU THÊM)" % (taper_deg, P.WEDGE_DEG, math.tan(_D(taper_deg)),
                                 P.MU_DESIGN / 1.3, (P.MU_DESIGN / 1.3) / math.tan(_D(taper_deg))))
RC.check("S6. Chêm VÀO được họng (mỏng đầu) và KẸT lại (dày cuối) — tự hãm",
         BAND_T + WEDGE_TIP_H <= gap_mouth and BAND_T + WEDGE_BACK_H > gap_throat,
         "đầu mỏng: %.2f + %.2f = %.2f ≤ khe miệng %.2f | đầu dày: %.2f + %.2f = %.2f > "
         "khe họng %.2f ⇒ kẹt đúng họng, không lọt qua"
         % (BAND_T, WEDGE_TIP_H, BAND_T + WEDGE_TIP_H, gap_mouth,
            BAND_T, WEDGE_BACK_H, BAND_T + WEDGE_BACK_H, gap_throat))
RC.check("S7. Áp lực kẹp trung bình (thông tin — ngân sách gián đoạn 20 kPa)",
         True,
         "ΣN = 2πT = %.1f N trên %.0f mm² ⇒ p ≈ %.1f kPa; giữ được theo trục ≈ μ·ΣN = %.1f N "
         "(μ=%.2f) — VƯỢT 20 kPa, xem mục 'mở' của báo cáo"
         % (SIG_N, A_contact, p_mean * 1000.0, F_fric, P.MU_DESIGN))
RC.check("S8. Khung – đai – chêm KHÔNG chồng khối (khe hở lắp ráp thật)",
         frame.common(belt).Volume <= 1e-3 and frame.common(wedge).Volume <= 1e-3
         and belt.common(wedge).Volume <= 1e-3,
         "V_chung: khung∩đai = %.4f | khung∩chêm = %.4f | đai∩chêm = %.4f mm³"
         % (frame.common(belt).Volume, frame.common(wedge).Volume, belt.common(wedge).Volume))
r_key_arc = G.ell_r(P.a_in() + KEY_R1, P.b_in() + KEY_R1, KEY_PHI0)
gap_phi0 = _D(KEY_PHI0 - NOTCH_PHI0) * r_key_arc          # khe hở TIẾP TUYẾN mỗi bên
gap_phi1 = _D(NOTCH_PHI1 - KEY_PHI1) * r_key_arc
gap_rad_out = NOTCH_R1 - KEY_R1                            # khe hở HƯỚNG KÍNH (ngoài)
gap_z0 = KEY_Z0 - NOTCH_Z0                                 # khe hở DỌC TRỤC hai đầu
gap_z1 = NOTCH_Z1 - KEY_Z1
RC.check("S9. Gờ móc NẰM TRONG rãnh móc — khít tiếp tuyến (chống rơ), hở 0,10 khi lắp",
         NOTCH_PHI0 < KEY_PHI0 and NOTCH_PHI1 > KEY_PHI1 and NOTCH_R1 > KEY_R1
         and NOTCH_Z0 < KEY_Z0 and NOTCH_Z1 > KEY_Z1
         and KEY_PHI0 > FRAME_PHI0 and KEY_PHI1 < ROOF_PHI0
         and min(gap_phi0, gap_phi1) >= 0.02 and gap_rad_out >= 0.05
         and gap_z0 >= 0.05 and gap_z1 >= 0.05 and max(gap_phi0, gap_phi1) <= 0.15,
         "gờ φ %.0f–%.0f / r→%.2f / z %.1f–%.1f | rãnh φ %.2f–%.2f / r→%.2f / z %.2f–%.2f | "
         "khe hở: φ %.3f+%.3f (khít chống rơ) | kính %.2f | z %.2f+%.2f mm"
         % (KEY_PHI0, KEY_PHI1, KEY_R1, KEY_Z0, KEY_Z1,
            NOTCH_PHI0, NOTCH_PHI1, NOTCH_R1, NOTCH_Z0, NOTCH_Z1,
            gap_phi0, gap_phi1, gap_rad_out, gap_z0, gap_z1))
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
    "A. ĐAI QUẤN: %.0f° | %.2f × %.1f mm | V = %.2f cm³ ≈ %.2f g (TPU 85A)"
    % (wrap_deg, BAND_T, BAND_Z1 - BAND_Z0, st["vol_tpu_cm3"], st["mass_tpu"]),
    "   T(ε=%.0f %%) = %.2f N ⇒ ΣN = 2πT = %.1f N | p ≈ %.1f kPa | giữ trục ≈ %.1f N"
    % (BAND_STRETCH * 100, T_design, SIG_N, p_mean * 1000.0, F_fric),
    "B. KHUNG LƯNG: φ %.0f°–%.0f° | V_PETG = %.2f cm³ ≈ %.2f g | r_ngoài max = a_in+%.2f mm"
    % (FRAME_PHI0, FRAME_PHI1, st["vol_petg_cm3"], st["mass_petg"], max(r for _, r in FRAME_RO)),
    "   CHÊM: vát %.1f° | %.2f→%.2f mm | V = %.2f cm³ ≈ %.2f g | miệng %.2f mm → họng %.2f mm"
    % (taper_deg, WEDGE_TIP_H, WEDGE_BACK_H, wedge.Volume / 1000.0, st["mass_wedge"],
       gap_mouth, gap_throat),
    "C. ENVELOPE: %.2f × %.2f × %.2f mm | ΔX = %+.2f mm (ngân sách 2,00) | X_max = %.2f mm"
    % (frame.BoundBox.XLength, frame.BoundBox.YLength, frame.BoundBox.ZLength,
       st["dx_lat"], st["x_max"]),
]
_rc = RC.finish(frame, [], "Idea3_WrapBand", extras, subdir="idea3",
                extra_parts=[("Band_TPU", belt), ("Wedge_PETG", wedge)])
RC.exit_code(_rc)   # FF_NO_SYS_EXIT=1 khi chạy trong FreeCAD GUI
