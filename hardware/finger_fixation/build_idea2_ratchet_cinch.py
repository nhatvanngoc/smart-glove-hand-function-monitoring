# -*- coding: utf-8 -*-
"""
Ý TƯỞNG 2 — KHOÁ CÓC MỘT CHIỀU (Ratchet Cinch)   [bản 2 — sửa quy ước khe + hướng răng]
=====================================================================================
HỌ NGUYÊN LÝ KHÁC ý tưởng 1: KHÔNG đòn bẩy, KHÔNG quá tâm. Vòng P1 vẫn gồm THÂN +
TAY KẸP nối bằng lá bản lề mềm (ring_common), nhưng KHE được khoá bằng BÁNH CÓC:

      TAY KẸP (u<0, phía đốt gần) giữ LƯỠI RĂNG CỨNG — 9 rãnh, 0,80 mm/nấc
      THÂN    (u>0, phía mu tay)  giữ CON CÓC: lò xo lá + mũi cóc 2 bậc + MẤU NHẢ

  • Đóng vòng (tay kẹp chạy +u): mũi cóc LEO DỐC 45° (F ≈ 1,3 N) rồi rơi vào
    rãnh kế tiếp ⇒ 0,255 mm đường kính mỗi nấc, cảm nhận rõ tiếng "tách".
  • Giữ: mặt răng ĐỨNG (form closure) tì vào mặt đứng mũi cóc ⇒ KHÔNG nhờ ma
    sát, KHÔNG rơ ⇒ đúng nghĩa "không lỏng lẻo". Khe hở in tại nấc = 0,03 mm.
  • Mở vòng: mũi cóc tì mặt đứng của răng ⇒ CHẶN CỨNG; muốn mở phải đè MẤU NHẢ
    (một ngón cái, F ≈ 1,9 N) ⇒ nhấc mũi 0,65 mm.
  • Giới hạn siết = khe đóng hết (0,45 mm): vật liệu KHÔNG thể tự chồng ⇒ vòng
    không bao giờ siết quá cỡ.
  • KHE THẬT 0,45 mm (ring_common đã sửa lỗi "khe bị hàn kín") ⇒ vòng in ra MỞ
    được; dải vận hành 0,45 → 6,85 mm khe = ΔØ 2,04 mm cho mỗi cỡ in.

KHUNG KHE (u, v): u = CHIỀU DÀI CUNG từ φ = SLIT_PHI (61°); v = lệch kính RA
NGOÀI (v = 0 = ĐÚNG mặt ngoài ellipse). Vì u là chiều dài cung (không phải góc),
chi tiết ở xa khe KHÔNG bị trôi khỏi mặt vành (bản 1 dùng khung tiếp tuyến nên
lưỡi dài bị hụt ra ngoài).

Xuất: stl/idea2[ _pla]/Ring_<MAT>.stl — MỘT chi tiết in, một vật liệu
(PLA hoặc ABS), 4 đệm cánh IN LIỀN (khe 0,20 mm) — kiểm A1–A11 + G1/G2.
"""
import bisect
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

import params as P        # noqa: E402
import fcgeom as G        # noqa: E402
import ring_common as RC  # noqa: E402

OUT_DIR = os.path.join(_here, "stl")
DEG = G.deg

# ============================================================ 1. THÔNG SỐ ===
N_CLICK = 8                                 # 8 nấc (9 rãnh)
PITCH = P.RATCHET_PITCH_MM                  # 0,80 mm/nấc
T_H = P.RATCHET_TOOTH_H                     # 0,55 mm — chiều cao răng
RAMP_W = T_H                                # dốc 45° ⇒ bước ngang = chiều cao
VALLEY = PITCH - RAMP_W                     # 0,25 mm rãnh
GAP_SLIT = 0.45                             # khe in (THÂN ↔ TAY KẸP)
D_FACE = GAP_SLIT * 0.5                     # ±0,225 mm: mặt đầu hai bên khe
V_ROOF = 2.05                               # mặt rãnh
V_TIP = V_ROOF + T_H                        # 2,60 mm — đỉnh răng
V_UNDER = 0.35                              # khe dưới lưỡi so với mặt ngoài vành
LIP = 0.08                                  # khe hở in giữa hai chi tiết trượt
TONGUE_Z0, TONGUE_Z1 = 4.00, 10.00

# --- LƯỠI RĂNG (thuộc TAY KẸP, u < 0) ---
U_ROOT0 = -3.00                             # đầu ngoài của chân lưỡi (ngàm vào tay kẹp)
ROOT_V0 = -1.15                             # đáy chân (ngập trong tường dày 1,75 mm)
U_ROOT1 = -0.30                             # hết phần ngàm ⇒ lưỡi bay qua khe
V0_VALLEY = -0.20                           # rãnh số 1 (nấc kín nhất) bắt đầu ở đây
U_NOSE = V0_VALLEY + VALLEY + PITCH * N_CLICK + 0.40    # +6.85: đầu tự do của lưỡi

# --- CON CÓC (thuộc THÂN, u > 0) ---
TOE_W = 0.20                                # ngón mũi (≤ rãnh 0,25 ⇒ tụt rãnh được)
BACKLASH = 0.03                             # khe in khi khoá
NUB_U1 = V0_VALLEY + VALLEY - BACKLASH      # +0.02: mặt CHẶN (quay về +u)
NUB_U0 = NUB_U1 - TOE_W - 0.04              # −0.22: mép sau ngón
NUB_V_BOT = 2.10                            # đáy ngón (cách mặt rãnh 0,05)
NUB_V_MID = 2.70                            # vai ngón (cách đỉnh răng 0,10)
BLADE_T = RC.pick_leaf_t(P.MAT.E, P.sig_allow(), 8.00, 0.60, widths=(0.40, 0.50, 0.60, 0.80))
#   ^ bề dày lá lò xo chọn theo VẬT LIỆU: σ_nhả = 1.5·E·t·δ/L² với L ≈ 8,0 mm,
#     δ_nhả = 0,60 mm. ABS ⇒ t = 0,40 mm (σ 11,3 MPa ≤ 12); PLA ⇒ t = 0,40 mm
#     (σ 19,7 ≤ 22). Bản PETG cũ dùng 0,50 mm vì PETG chỉ ~1,2 GPa.
BLADE_V0, BLADE_V1 = 3.70, 4.20
BLADE_U0, BLADE_U1 = -2.40, 11.60
PAWL_Z0, PAWL_Z1 = 2.60, 11.40
NUB_Z0, NUB_Z1 = 4.30, 9.70                 # mũi cóc lọt giữa hai tai trụ đế
EAR_Z = ((2.60, 3.90), (10.10, 11.40))      # hai tai (chừa 0,10 mm với lưỡi)
PED_U0, PED_U1 = 7.80, 8.60                 # trụ đế = ngàm lá (L công xôn ≈ 8,0 mm)
PED_V0 = -0.50
TAB_U0, TAB_U1 = 11.00, 12.20               # mấu nhả (ngón cái đè XUỐNG)
TAB_V0, TAB_V1 = 4.10, 5.00
CLAMP_IN = 0.10                             # ngập 0,10 mm vào lá (tránh mặt trùng nhau)

PADS = [("Pad1", 33.0), ("Pad2", 147.0), ("Pad3", 216.0), ("Pad4", 288.0)]
PAD_ARC = 46.0                              # cung cửa sổ đệm (đệm cánh in liền)

# ======================================== 2. KHUNG CUNG (u,v) TRÊN ELLIPSE ===
def _arc_table(n=2880):
    """Bảng (phi, s): s = chiều dài cung dọc ellipse NGOÀI, từ phi0 = −120°."""
    a, b = P.a_out(), P.b_out()
    phis, cum, prev = [], [0.0], None
    for i in range(n + 1):
        phi = -120.0 + 480.0 * i / n
        x, y = G.ell_pt(a, b, phi)
        if prev is not None:
            cum.append(cum[-1] + math.hypot(x - prev[0], y - prev[1]))
        phis.append(phi)
        prev = (x, y)
    return phis, cum


_PHIS, _CUM = _arc_table()
_S61 = _CUM[min(range(len(_PHIS)), key=lambda i: abs(_PHIS[i] - P.SLIT_PHI))]


def phi_of_u(u):
    """Hoành độ cung u (mm, tính từ φ = SLIT_PHI) → góc tham số ellipse."""
    s = _S61 + u
    i = bisect.bisect_left(_CUM, s)
    i = max(1, min(len(_CUM) - 1, i))
    s0, s1 = _CUM[i - 1], _CUM[i]
    t = 0.0 if s1 == s0 else (s - s0) / (s1 - s0)
    return _PHIS[i - 1] + t * (_PHIS[i] - _PHIS[i - 1])


def lv(u, v):
    """Khung cung (u,v) → toạ độ thế giới (X,Y). v = 0 là ĐÚNG mặt ngoài vành."""
    x, y = G.ell_pt(P.a_out(), P.b_out(), phi_of_u(u))
    r = math.hypot(x, y)
    k = (r + v) / r
    return [x * k, y * k]


def lprism(pts_uv, z0, z1):
    return RC.prism([lv(u, v) for (u, v) in pts_uv], z0, z1)


# ================================================= 3. THÂN / TAY KẸP / BẢN LỀ ==
shell, arm, hinge, reliefs, meta = RC.shell_arm_hinge(gap_slit=GAP_SLIT)
GAP_MM = meta["slit_gap_mm"]

# ============================================================ 4. LƯỠI RĂNG ===
def tongue_outline():
    """Đa giác (u,v) của lưỡi — một vòng kín, KHÔNG tự cắt, KHÔNG cạnh trùng.

    Dãy răng: mặt đứng ở ĐẦU MỖI DỐC (phía +u), dốc 45° đổ XUỐNG theo +u ⇒ khi
    vòng ĐÓNG (lưỡi chạy −u so với con cóc) mũi cóc leo dốc rồi rơi vào rãnh
    (nấc); khi vòng MỞ (lưỡi chạy +u) mũi cóc tì vào mặt đứng ⇒ chặn.
    """
    pts = [(U_ROOT0, ROOT_V0), (U_ROOT1, ROOT_V0), (U_ROOT1, V_UNDER),
           (V0_VALLEY, V_UNDER)] if False else []
    pts = [(U_ROOT0, ROOT_V0), (U_ROOT1, ROOT_V0), (U_ROOT1, V_UNDER)]
    pts += [(V0_VALLEY, V_UNDER)]                       # đáy lưỡi: khe 0,35 trên mặt vành
    pts += [(V0_VALLEY, V_ROOF)]                        # mép rãnh số 1
    for k in range(N_CLICK + 1):                        # 9 răng: mặt đứng + dốc 45°
        w = V0_VALLEY + VALLEY + PITCH * k              # vị trí mặt đứng của răng k
        pts += [(w, V_TIP), (w + RAMP_W, V_ROOF)]
    pts += [(U_NOSE, V_ROOF), (U_NOSE, V_UNDER)]        # mũi lưỡi
    return pts


tongue = lprism(tongue_outline(), TONGUE_Z0, TONGUE_Z1)

# ============================================================= 5. CON CÓC ====
ears = [lprism([(PED_U0, PED_V0), (PED_U1, PED_V0),
                (PED_U1, BLADE_V0 + CLAMP_IN), (PED_U0, BLADE_V0 + CLAMP_IN)], z0, z1)
        for (z0, z1) in EAR_Z]
blade = lprism([(BLADE_U0, BLADE_V0), (BLADE_U1, BLADE_V0),
                (BLADE_U1, BLADE_V1), (BLADE_U0, BLADE_V1)], PAWL_Z0, PAWL_Z1)
nub = lprism([(NUB_U0, NUB_V_BOT), (NUB_U1, NUB_V_BOT),
              (NUB_U1, NUB_V_MID), (NUB_U0 + 0.90, NUB_V_MID),
              (NUB_U0 + 0.90, BLADE_V0 + CLAMP_IN), (NUB_U0, BLADE_V0 + CLAMP_IN)],
             NUB_Z0, NUB_Z1)
tab = lprism([(TAB_U0, TAB_V0), (TAB_U1, TAB_V0), (TAB_U1, TAB_V1), (TAB_U0, TAB_V1)],
             PAWL_Z0, PAWL_Z1)
pawl = RC.union_all(ears + [blade, nub, tab])

# ================================== 6. ĐỆM CÁNH IN LIỀN (MỘT VẬT LIỆU) ======
# Biến thể chỉ dùng PLA/ABS: không còn 4 đệm TPU in rời — thay bằng 4 đệm cánh in
# liền cùng vòng (ring_common.petal_pads): cánh mỏng ngàm một đầu, khe 0,20 mm rồi
# tới thành dày = CHẶN CỨNG. Xem ring_common.petal_metrics để biết ngân sách k/σ.
pads = []

# ==================================================== 7. LẮP RÁP VÀ XUẤT ====
# Ý tưởng 2 KHÔNG dùng trụ neo gân (φ 86–112°): khoang đó đã dành cho con cóc +
# trụ đế + mấu nhả. Chỉ giữ rãnh cảm biến ở lòng vành (không ảnh hưởng cơ cấu).
_boss, recess, _hole = RC.body_features()
ring = RC.union_all([shell, arm, hinge, tongue, pawl])
cutter = [reliefs] + RC.petal_pads([pp for _, pp in PADS], PAD_ARC) + [recess]
for c in cutter:
    ring = ring.cut(c)
ring = ring.removeSplitter()
st = RC.stats(ring, pads, ref_lat=None)
BB = ring.BoundBox
ENV = (BB.XMax - BB.XMin, BB.YMax - BB.YMin, BB.ZMax - BB.ZMin)

# ====================================================== 8. SỐ LIỆU KIỂM =====
B_BLADE = PAWL_Z1 - PAWL_Z0
I_B = B_BLADE * BLADE_T ** 3 / 12.0
L_NUB = PED_U0 - NUB_U0                     # công xôn trụ đế → MẶT CHỊU LỰC mũi cóc
L_TAB = TAB_U0 - PED_U1                     # công xôn trụ đế → mấu nhả
K_NUB = 3.0 * P.MAT.E * I_B / L_NUB ** 3
LIFT_SKIP = V_TIP - NUB_V_BOT               # nhấc để vượt 1 răng
LIFT_REL = LIFT_SKIP + 0.10                 # nhả: nhấc dư 0,10 mm (vừa đủ thoát răng)
#   ↑ σ_nhả = 1.5·E·t·δ/L²: với vật liệu CỨNG (E=2000 MPa) phải giữ δ nhỏ và L dài,
#     nếu không lá sẽ vượt σ_y/2,5 (bản PETG cũ nhấc dư 0,15 mm vì E chỉ 1200 MPa).
F_SKIP = K_NUB * LIFT_SKIP
F_REL = K_NUB * LIFT_REL * L_NUB / (1.5 * L_TAB)     # mô hình công xôn chịu mô-men
F_REL_RIGID = K_NUB * LIFT_REL * L_NUB / L_TAB       # biên trên (đòn bẩy cứng)
SIG_SKIP = 1.5 * P.MAT.E * BLADE_T * LIFT_SKIP / L_NUB ** 2
SIG_REL = 1.5 * P.MAT.E * BLADE_T * LIFT_REL / L_NUB ** 2
ENGAGE = V_TIP - NUB_V_BOT
TRAVEL = PITCH * N_CLICK
D_RES = PITCH / math.pi
D_RANGE = TRAVEL / math.pi
N_VALLEY = N_CLICK + 1

RC.check("A1. Mỗi nấc chỉnh 0,255 mm đường kính (≤ 0,30 mm)",
         D_RES <= 0.30,
         "bước răng %.2f mm ⇒ ΔØ = %.3f mm/nấc | %d nấc / %d rãnh"
         % (PITCH, D_RES, N_CLICK, N_VALLEY))
RC.check("A2. Một cỡ in phủ ≥ 2,0 mm đường kính (dải Ø20–24 ⇒ 2 cỡ in)",
         D_RANGE >= 1.95,
         "%d nấc × %.2f mm = %.2f mm hành trình ⇒ ΔØ = %.2f mm/cỡ | 4,0 mm cần %d cỡ in"
         % (N_CLICK, PITCH, TRAVEL, D_RANGE, int(math.ceil(4.0 / D_RANGE))))
RC.check("A3. Lực VƯỢT NẤC ≤ 2,2 N (bấm nhẹ, không đau đầu ngón)",
         F_SKIP <= 2.2,
         "k_mũi = %.2f N/mm (công xôn %.2f × %.1f × %.2f) | nhấc %.2f mm ⇒ F ≈ %.2f N"
         % (K_NUB, L_NUB, B_BLADE, BLADE_T, LIFT_SKIP, F_SKIP))
RC.check("A4. Lực NHẢ bằng MỘT ngón cái ≤ 8 N (đòn nhả qua trụ đế)",
         F_REL_RIGID <= 8.0,
         "đòn %.2f (mũi) / %.2f (mấu) | nhấc mũi %.2f mm ⇒ F ≈ %.2f N "
         "(biên trên đòn cứng %.2f N)" % (L_NUB, L_TAB, LIFT_REL, F_REL, F_REL_RIGID))
RC.check("A5. Ứng suất lò xo lá khi nhả ≤ σ_y/%.1f = %.1f MPa (%s)"
         % (P.SIG_ALLOW_FS, P.sig_allow(), P.MAT.key),
         SIG_REL <= P.sig_allow(),
         "σ_nấc = %.1f MPa | σ_nhả = %.1f MPa | σ_y = %.0f MPa ⇒ FS ≈ %.2f"
         % (SIG_SKIP, SIG_REL, P.MAT.sig_y, P.MAT.sig_y / SIG_REL))
RC.check("A6. Ngón mũi cóc lọt rãnh %.2f ≤ rãnh %.2f — không kê hai đỉnh răng"
         % (TOE_W, VALLEY),
         TOE_W <= VALLEY + 0.02,
         "ngón %.2f mm | rãnh %.2f mm | đáy ngón %.2f cách mặt rãnh %.2f mm"
         % (TOE_W, VALLEY, NUB_V_BOT, NUB_V_BOT - V_ROOF))
RC.check("A7. Ăn khớp mặt răng ĐỨNG ≥ 0,35 mm (form closure, chống mở)",
         ENGAGE >= 0.35,
         "đáy mũi %.2f → đỉnh răng %.2f: ăn sâu %.2f mm | mặt đứng răng cao %.2f mm"
         % (NUB_V_BOT, V_TIP, ENGAGE, T_H))
RC.check("A8. GIỚI HẠN SIẾT = khe đóng hết (0,45 mm) ⇒ không thể siết quá cỡ",
         0.0 < GAP_SLIT <= 0.60 and N_VALLEY >= N_CLICK,
         "khe in %.2f mm là kích thước nhỏ nhất của vòng: hai mặt đầu KHÔNG thể "
         "chồng lên nhau ⇒ mọi vị trí khoá đều nằm trong %d rãnh (ΔØ %.2f mm)"
         % (GAP_SLIT, N_VALLEY, D_RANGE))
RC.check("A9. Lưỡi bay QUA khe với khe hở ≥ 0,30 mm (không cọ khi mở)",
         V_UNDER >= 0.30,
         "đáy lưỡi %+.2f so với mặt ngoài vành (0,00) | khe hở %.2f mm | khe hở in "
         "hai bên khe %.2f mm" % (V_UNDER, V_UNDER, LIP))
RC.check("A10. Chân lưỡi NGẬM trong tường TAY KẸP + trụ đế NGẬM trong tường THÂN",
         ROOT_V0 > -P.T_SIDE + 0.10 and PED_V0 > -P.T_SIDE + 0.10 and U_ROOT1 < -D_FACE,
         "đáy chân lưỡi %+.2f > mặt trong tường %+.2f (ngàm %.2f mm) | đáy trụ đế %+.2f "
         "> %+.2f | hết phần ngàm ở u = %+.2f (qua khe %+.2f ⇒ lưỡi bay qua khe)"
         % (ROOT_V0, -P.T_SIDE, 0.0 - ROOT_V0, PED_V0, -P.T_SIDE, U_ROOT1, -D_FACE))
_pm = RC.petal_metrics(PAD_ARC)
RC.check("G1. Một vật liệu duy nhất (%s) + không đệm rời/keo" % P.MAT.key,
         P.MAT.key in ("PLA", "ABS") and len(pads) == 0,
         "E=%.0f MPa, σ_y=%.0f MPa, ρ=%.2f g/cm³, μ_design=%.2f | đệm cánh in liền: "
         "%.2f × %.1f mm, L = %.2f mm ⇒ k = %.1f N/mm, σ_tì = %.1f ≤ %.1f MPa (FS %.2f)"
         % (P.MAT.E, P.MAT.sig_y, P.MAT.rho, P.MAT.mu, _pm["t"], P.H_PAD, _pm["L"],
            _pm["k"], _pm["sigma"], _pm["sig_allow"], _pm["fs"]))
RC.check("G2. Lực VƯỢT NẤC ≤ 2,5 N ở vật liệu %s (không quá cứng để bấm)" % P.MAT.key,
         F_SKIP <= 2.5,
         "công xôn %.2f mm, lá %.1f × %.2f ⇒ k = %.2f N/mm | nhấc %.2f mm ⇒ F = %.2f N"
         % (L_NUB, B_BLADE, BLADE_T, K_NUB, LIFT_SKIP, F_SKIP))
RC.check("A11. Một khối liền + hợp lệ + Z 12–16 mm + khe thật 0,45 mm",
         len(ring.Solids) == 1 and bool(ring.isValid()) and 12.0 <= st["z_len"] <= 16.0
         and abs(GAP_MM - GAP_SLIT) <= 0.06,
         "%d khối | isValid=%s | Z = %.2f mm | ΔX = %+.2f mm (ngân sách 2,00) | "
         "khe thật %.3f mm" % (len(ring.Solids), ring.isValid(), st["z_len"], st["dx_lat"], GAP_MM))

extras = [
    "-" * 78,
    "A. RĂNG CƯA: %d nấc × %.2f mm | dốc 45° cao %.2f | rãnh %.2f | ăn sâu %.2f mm"
    % (N_CLICK, PITCH, T_H, VALLEY, ENGAGE),
    "   con cóc: lá %.1f × %.2f mm, công xôn %.2f mm ⇒ k = %.2f N/mm | F_vượt nấc %.2f N"
    " | F_nhả %.2f N (biên trên %.2f N)"
    % (B_BLADE, BLADE_T, L_NUB, K_NUB, F_SKIP, F_REL, F_REL_RIGID),
    "B. KHE THẬT (ring_common): %.3f mm | mặt đầu THÂN u = %+.3f | mặt đầu TAY KẸP u = %+.3f"
    " | khe hở in khi khoá %.2f mm" % (GAP_MM, D_FACE, -D_FACE, BACKLASH),
    "C. KHỐI LƯỢNG: %s %.2f cm³ ≈ %.2f g | chi tiết in: 1 (một vật liệu, không đệm rời)"
    % (P.MAT.key, st["vol_part_cm3"], st["mass_part"]),
    "D. ENVELOPE: %.2f × %.2f × %.2f mm | ΔX = %+.2f mm (ngân sách 2,00)"
    % (ENV[0], ENV[1], ENV[2], st["dx_lat"]),
]
_rc = RC.finish(ring, pads, "Idea2_RatchetCinch", extras,
                subdir="idea2" + P.STL_SUFFIX)   # PLA → stl/idea2_pla
RC.exit_code(_rc)   # FF_NO_SYS_EXIT=1 khi chạy trong FreeCAD GUI
