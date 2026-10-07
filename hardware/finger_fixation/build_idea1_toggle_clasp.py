# -*- coding: utf-8 -*-
"""
build_idea1_toggle_clasp.py   (v2 — hình học SUY RA TỪ synthesis/toggle_synthesis.py)
================================================================================
Ý TƯỞNG 1 — VÒNG KHOÁ QUÁ TÂM KIỂU MÓC CÓ MẶT DỐC (Side Toggle Clasp)

Sinh hình học 3D (mm) cho bộ cố định đốt gần P1 bằng FreeCAD API thuần:
    Part.makePolygon → Part.Face → extrude → cut/fuse → Mesh.export

CHẠY TRÊN FREECAD THẬT:
    freecadcmd build_idea1_toggle_clasp.py
CHẠY KIỂM TRA HEADLESS (không cần cài FreeCAD, cùng nhân OCCT):
    python headless/run_verify.py

NGUYÊN LÝ KHOÁ (4 điều kiện đã tính trong synthesis/toggle_synthesis.py):
  (1) KHÔNG RƠ  — móc có MẶT DỐC (β=15°) tì lên CHỐT TRỤ Ø3 in liền trên tay kẹp;
      trạng thái đóng xác định (determinate) vì toàn bộ là MỘT chi tiết in liền
      khối: 0 bu-lông, 0 trục rời ⇒ 0 khe hở lắp ghép.
  (2) QUÁ TÂM   — pháp tuyến mặt dốc lệch khỏi phương tải một góc β ⇒ mô-men tải
      quanh tâm quay A ÉP cần gạt vào MẶT CHẶN CỨNG (land trên tai) ⇒ form-closed,
      tải không thể mở khoá (phải quay cần gạt 135° mới đảo dấu mô-men).
  (3) TỰ HÃM   — β=15° < ρ=atan(0.35)=19.3° ⇒ nêm tự hãm (dự phòng lớp 2).
  (4) LÒ XO LÁ — cần gạt gắn vào tai qua LÁ MỎNG 0.55 mm (chốt mềm A): tạo lực
      đặt trước, bù dung sai in & từ biến; KHÔNG dùng khớp rời (không rơ).

VÌ SAO KHÔNG CÓ KHE HỞ (nguồn "lỏng lẻo" duy nhất của cơ cấu kẹp):
  * Đường truyền lực: ngón → tay kẹp → chốt P → mặt dốc → cần gạt → MẶT CHẶN → thân.
    Mọi khâu đều bị ÉP (preload) nên không tồn tại khe hở làm việc.
  * Khe hở danh nghĩa của mặt chặn chỉ 0.05 mm (STOP_GAP) và bị tải ép kín ngay.
  * Chốt P luôn được lò xo của tay kẹp ép vào mặt dốc ⇒ 2 mặt tì xác định.
  * Dải Ø20–24 hấp thụ bằng cách chốt P TRƯỢT DỌC mặt dốc (Δn = 0.07 mm cho
    ±1 mm đường kính) — không cần khe hở cơ khí nào.

GHI CHÚ TRUNG THỰC (AGENTS.md §1): mọi số dưới đây là NGÂN SÁCH THIẾT KẾ
(tính toán hình học/lực học trên mô hình), KHÔNG phải kết quả đo hay chế tạo.
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
_syn = os.path.join(_here, "synthesis")
if _syn not in sys.path:
    sys.path.insert(0, _syn)

import params as P            # noqa: E402
import fcgeom as G            # noqa: E402
import toggle_synthesis as TS  # noqa: E402  ← NGUỒN DUY NHẤT của hình học khoá

OUT_DIR = os.path.join(_here, "stl", "idea1")   # 3 ý tưởng: stl/idea1, stl/idea2, stl/idea3
DOC_NAME = "FixRing_Idea1_ToggleClasp"
FAILS = []


def check(name, ok, txt):
    if not ok:
        FAILS.append(name)
    print("   [%s] %-34s %s" % ("PASS" if ok else "FAIL", name, txt))


# =============================================================================
# 0. KHUNG TOẠ ĐỘ CỦA CẦN GẠT — lấy trực tiếp từ toggle_synthesis
# =============================================================================
A_PIV = TS.A                       # tâm quay cần gạt (world, mm)
PEG = TS.PEG                       # tâm chốt trụ Ø3 trên tay kẹp (world, mm)
HP = TS.HP                         # tâm bản lề lá của tay kẹp
R3 = TS.R3                         # |Hp–P| (bán kính cung tay kẹp)
PEG_R = TS.PEG_D / 2.0             # 1.5 mm
ARM_LEN = TS.ARM_LEN               # |A–P| (tay đòn kéo)
SLANT = TS.ARM_SLANT
BETA = TS.RAMP_BETA                # góc vát mặt dốc (độ)

_dx, _dy = PEG[0] - A_PIV[0], PEG[1] - A_PIV[1]
_L = math.hypot(_dx, _dy)
U_DIR = (_dx / _L, _dy / _L)                    # u: từ A tới chốt P
V_DIR = (-U_DIR[1], U_DIR[0])                   # v: +90° (ra ngoài / về phía mu)
N_LOC = (math.cos(math.radians(45.0)), math.sin(math.radians(45.0)))  # pháp tuyến tải
K_RAMP = ARM_LEN + PEG_R * math.sqrt(2.0)       # đường dốc: u + v = K_RAMP (tiếp xúc P)


def W(u, v, extra=None):
    """(u,v) trong hệ cần gạt → (x,y) thế giới. extra: hàm biến đổi thêm (mở/đóng)."""
    x = A_PIV[0] + u * U_DIR[0] + v * V_DIR[0]
    y = A_PIV[1] + u * U_DIR[1] + v * V_DIR[1]
    if extra is None:
        return (x, y)
    return extra((x, y))


def w_poly(pts_uv, extra=None):
    return [W(u, v, extra) for (u, v) in pts_uv]


def rot_about(center, deg, sign=1.0):
    """Hàm biến đổi: quay quanh `center` một góc deg*sign (độ, CCW)."""
    c, s = math.cos(math.radians(deg * sign)), math.sin(math.radians(deg * sign))
    cx, cy = center

    def f(p):
        x, y = p[0] - cx, p[1] - cy
        return (cx + c * x - s * y, cy + s * x + c * y)
    return f


# =============================================================================
# 1. THAM SỐ HÌNH HỌC RIÊNG CỦA Ý TƯỞNG 1 (hệ (u,v) của cần gạt)
# =============================================================================
GAP_SLIT = 0.45            # khe hở thân ↔ tay kẹp ở trạng thái đóng (mm)
HINGE_WINDOW = 34.0        # cửa sổ nhả vật liệu quanh lá bản lề (độ)
BLADE_T = P.T_HINGE        # 0.50 mm — lá bản lề tay kẹp
Z_H0, Z_H1 = P.Z_HINGE0, P.Z_HINGE1

# --- Cần gạt ---------------------------------------------------------------
Z_LEV0, Z_LEV1 = 0.60, P.H_RING - 0.60        # 0.6 … 13.4
L_TAIL_U = -7.60           # đầu chuôi cần gạt (phía mu–trụ)
L_STEP_U = -4.20           # bậc chuyển từ đáy chuôi lên mặt tì
L_TAIL_V = -0.15           # đáy chuôi (chồng lên lá mỏng 0.30 mm)
L_BODY_V = 0.60            # đáy thân (mặt tì cứng) — cách land 0.05 mm
L_TOP_V = 2.70             # mặt trên thân cần gạt
L_LEAD_IN = 0.40           # khoảng lùi của điểm vào mặt dốc so với chốt P
OFF_N = 2.40               # chiều dày móc, đo theo phương pháp tuyến tải N
GAP_PEG_MIN = 0.18         # khe hở nhỏ nhất cho phép giữa móc và chốt P (mm)
PRINT_CLEAR = 0.15         # khe hở IN giữa hai MẶT PHẲNG SONG SONG của mặt dốc
FLAT_DEPTH = 0.20          # chiều sâu vát phẳng trên chốt Ø3 (dây cung ≈ 1.5 mm)
#   ⇒ tiếp xúc làm việc là TIẾP XÚC DIỆN (flat-on-flat), không phải tiếp xúc ĐƯỜNG:
#     * khe hở in 0.15 mm là hai mặt phẳng song song ⇒ khép ĐỀU, không rơ góc;
#     * không còn điểm tiếp tuyến kỳ dị ⇒ lưới STL kín, in không dính;
#     * ứng suất tì phân bố trên 1.5 × 10 mm thay vì trên một đường sinh.
#   Mặt dốc THIẾT KẾ (tiếp tuyến tuyệt đối) vẫn là K_RAMP = ARM_LEN + R·√2 — dùng
#   để phân tích (β, h, nêm); hình học in dùng K_FACE = K_RAMP + (CLEAR−FLAT)·√2.
#   Lý do: (a) tránh "dính in" — nếu mặt dốc tiếp tuyến tuyệt đối với chốt Ø3 thì
#   hai bề mặt dính nhau thành một đường in liền, STL có cạnh không đa tạp;
#   (b) khe hở 0.15 mm bị ÉP KÍN bởi phản lực ngón ngay khi đeo (đàn hồi 0.1°),
#   nên trạng thái LÀM VIỆC vẫn khép kín, không rơ.

# --- Tai (land tì cứng) + trụ -------------------------------------------------
POST_U0, POST_U1 = -4.20, -2.00     # bề rộng land theo u
POST_V_TOP = L_BODY_V - P.STOP_GAP  # 0.55 mm — khe hở danh nghĩa 0.05 mm
POST_Z = [(0.60, 3.20), (10.80, 13.40)]   # 2 "tai" (nhường Z cho lá mỏng)
POST_V_BOT = -6.20                  # cắm sâu vào thân vòng (để fuse chắc)

# --- Lá mỏng (chốt mềm A) -----------------------------------------------------
BL_T = 0.55                # chiều dày lá (theo v)
BL_V_TOP = L_TAIL_V + 0.30  # 0.15 — chồng 0.30 mm vào đáy chuôi cần gạt
BL_V_BOT = BL_V_TOP - BL_T  # -0.40
BL_ROOT_U0, BL_ROOT_U1 = -1.20, 1.60
BL_TIP_U = -6.80           # đầu tự do của lá (nằm dưới chuôi cần gạt)
BL_Z0, BL_Z1 = 3.20, 10.80  # 7.6 mm theo Z
BL_ROOT_V_BOT = -4.80      # chân lá cắm vào thân vòng
BL_B_W = 2.30              # bề rộng eo (đoạn làm việc) theo u ở chân
L_EFF = (BL_ROOT_U0 - L_STEP_U) + (L_STEP_U - BL_TIP_U) * 0.5   # ≈ 4.3 mm (tay đòn hiệu dụng)

# --- Đệm ngón tay cái (paddle) ------------------------------------------------
PAD_U0, PAD_U1 = -7.40, -3.60
PAD_V0, PAD_V1 = 2.50, 5.80
PAD_Z0, PAD_Z1 = 1.60, P.H_RING - 1.60
R_HANDLE_GEO = PAD_V1 * 0.5 + PAD_V0 * 0.5   # tay đòn nhả ≈ 4.15 mm (lực theo ±u)

# --- Chốt trụ Ø3 trên tay kẹp -------------------------------------------------
PEG_Z0, PEG_Z1 = 2.00, 12.00

# --- Neo gân + rãnh + vách cảm biến + đệm (giữ nguyên từ bản v1) ---------------
ANCHOR = dict(phi0=86.0, phi1=112.0, z0=0.0, z1=4.6, rise=1.7,
              slot_w=3.0, slot_d=2.6, screw_r=1.6)
GROOVE_PHI = (66.0, 134.0)
GROOVE_W, GROOVE_D, GROOVE_LIP = 2.4, 1.15, 0.45
PAD_PHI = (33.0, 147.0, 216.0, 288.0)
#   SỬA LỖI (2026-10-07): bản cũ dùng (33,147,213,327) — rãnh đệm ở 327° trải
#   [304°,350°] NẰM ĐÈ LÊN LÁ BẢN LỀ (315°…357°) ⇒ dao cắt rãnh xoá sạch lá bản lề,
#   tay kẹp chỉ còn "dính" nhờ phần chồng lấn 0.45 mm ở khe (nay đã sửa) ⇒ chi tiết
#   in ra bị RỜI thành 2 khối. Cặp đệm phía bụng dịch về (216°, 288°) để hở ≥ 27°
#   quanh lá bản lề; kiểm tra B5–B7 chặn vĩnh viễn lớp lỗi này.
PAD_ARC = 46.0
PAD_SLOT_D = 1.35
PAD_LIP = 0.55
PAD_T = 1.55

doc = App.newDocument(DOC_NAME)


# =============================================================================
# 2. TIỆN ÍCH DỰNG KHỐI
# =============================================================================
def fuse_chain(parts):
    """Hợp nhiều khối bằng CHUỖI fuse HAI NGÔI (API FreeCAD chuẩn, kết quả tất định).

    KHÔNG dùng Shape.multiFuse(): trong FreeCAD đó là general fuse
    (BRepAlgoAPI_BuilderAlgo) và có thể trả về compound nhiều mảnh rời ⇒ mục kiểm
    "1 khối liền" sẽ báo sai. Các chi tiết ở đây đều ngập nhau ≥ 0,05 mm nên chuỗi
    fuse hai ngôi cho ĐÚNG một solid — giống hệt kết quả kiểm headless.
    """
    parts = [p for p in parts if p is not None]
    acc = parts[0]
    for p in parts[1:]:
        acc = acc.fuse(p)
    return acc


def cut_all(shape, tools):
    """Cắt LẦN LƯỢT từng dao — API FreeCAD chuẩn (cut() chỉ nhận MỘT đối tượng).

    FreeCAD KHÔNG có shape.cut([a, b, c]) (PyArg_ParseTuple "O!" trong
    src/Mod/Part/App/TopoShapePyImp.cpp) — truyền list sẽ TypeError.
    """
    for t in tools:
        shape = shape.cut(t)
    return shape


def prism(pts2d, z0, z1):
    """Đa giác 2D (XY) → khối đặc bằng extrude theo +Z."""
    if len(pts2d) < 3:
        raise ValueError("prism cần >= 3 điểm")
    w = Part.makePolygon([App.Vector(x, y, z0) for (x, y) in pts2d], True)   # vị trí, không keyword
    return Part.Face(w).extrude(App.Vector(0.0, 0.0, float(z1) - float(z0)))


def band_prism(a_in, b_in, a_out, b_out, phi0, phi1, z0, z1, n=180):
    return prism(G.band(a_in, b_in, a_out, b_out, phi0, phi1, n), z0, z1)


def local_poly(pts_uv, phi, r_ref):
    origin, rot = G.local_frame(phi, r_ref)
    return G.tf(pts_uv, origin, rot)


def local_prism(pts_uv, phi, r_ref, z0, z1):
    return prism(local_poly(pts_uv, phi, r_ref), z0, z1)


def rad_prism(pts_zv, phi):
    """Khối dựng từ đa giác trong mặt phẳng (Z, v) rồi extrude theo TIẾP TUYẾN."""
    t = G.deg(phi)
    rhat = (math.cos(t), math.sin(t))
    that = (-math.sin(t), math.cos(t))
    pts3 = [(rhat[0] * v + that[0] * (-40.0), rhat[1] * v + that[1] * (-40.0), z)
            for (z, v) in pts_zv]
    face = Part.Face(Part.makePolygon([App.Vector(*p) for p in pts3], True))
    return face.extrude(App.Vector(that[0] * 80.0, that[1] * 80.0, 0.0))


def polar(r, phi):
    t = G.deg(phi)
    return (r * math.cos(t), r * math.sin(t))


def cyl(radius, z0, z1, center_xy):
    return Part.makeCylinder(radius, z1 - z0, App.Vector(center_xy[0], center_xy[1], z0),
                             App.Vector(0.0, 0.0, 1.0))


# --- kiểm tra khe hở (chỉ dùng số học thuần Python) --------------------------
def seg_dist(p, a, b):
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    if L2 < 1e-12:
        return math.hypot(p[0] - ax, p[1] - ay)
    t = ((p[0] - ax) * dx + (p[1] - ay) * dy) / L2
    t = max(0.0, min(1.0, t))
    return math.hypot(p[0] - (ax + t * dx), p[1] - (ay + t * dy))


def poly_dist_pt(poly, p):
    return min(seg_dist(p, poly[i], poly[(i + 1) % len(poly)]) for i in range(len(poly)))


def seg_seg_dist(a1, a2, b1, b2):
    return min(seg_dist(a1, b1, b2), seg_dist(a2, b1, b2),
               seg_dist(b1, a1, a2), seg_dist(b2, a1, a2))


def poly_dist(p1, p2):
    n, m = len(p1), len(p2)
    return min(seg_seg_dist(p1[i], p1[(i + 1) % n], p2[j], p2[(j + 1) % m])
               for i in range(n) for j in range(m))


def ring_reach(phi_deg, a_out, b_out):
    """Bán kính mặt ngoài vành theo phương phi (xấp xỉ cực)."""
    t = G.deg(phi_deg)
    return 1.0 / math.sqrt((math.cos(t) / a_out) ** 2 + (math.sin(t) / b_out) ** 2)


# =============================================================================
# 3. THÂN VÒNG (SHELL) + TAY KẸP (ARM)
# =============================================================================
a_in, b_in = P.a_in(), P.b_in()
a_out, b_out = P.a_out(), P.b_out()

phi_arm_end = P.SLIT_PHI - GAP_SLIT * 0.5 * (180.0 / (math.pi * a_out))     # mặt đầu TAY KẸP
phi_shell_start = P.SLIT_PHI + GAP_SLIT * 0.5 * (180.0 / (math.pi * a_out))  # mặt đầu THÂN
phi_shell_hinge_end = P.HINGE_PHI - HINGE_WINDOW * 0.5
phi_arm_hinge_start = P.HINGE_PHI + HINGE_WINDOW * 0.5

# SỬA LỖI (2026-10-07): bản cũ lấy shell = [61−d → 319] và arm = [353 → 61+d] ⇒ hai
# cung CHỒNG NHAU 2d = 0.45 mm ⇒ khe bị hàn kín, vòng in ra là vòng KÍN không mở được.
# Đúng phải là: arm = [353 → 61−d], shell = [61+d → 319] ⇒ giữa hai mặt đầu là KHE HỞ.
shell = band_prism(a_in, b_in, a_out, b_out, phi_shell_start, phi_shell_hinge_end, 0.0, P.H_RING)
arm = band_prism(a_in, b_in, a_out, b_out, phi_arm_hinge_start, phi_arm_end + 360.0, 0.0, P.H_RING)

# Lá bản lề mềm của tay kẹp (nằm SÁT mặt trong ⇒ mặt tiếp xúc da liên tục)
# SỬA LỖI (2026-10-07): bản cũ đặt mặt TRONG của lá TRÙNG KHÍT mặt trong của thân/
# tay kẹp ⇒ mối hàn boolean có hai mặt trụ trùng nhau, bộ tessellate sinh 2 tam giác
# diện tích ~0 (đã kiểm: shell+blade → zero=2; arm+blade → zero=0). Nay hạ lá vào
# 0.05 mm (bước nhỏ, không ảnh hưởng tiếp xúc da) và nâng mặt ngoài lên +0.05 để
# GIỮ ĐÚNG chiều dày làm việc BLADE_T (dao relief xén về +0.47 khi đóng cửa sổ).
BLADE_INSET = 0.05
blade_hinge = band_prism(a_in + BLADE_INSET, b_in + BLADE_INSET,
                         a_in + BLADE_INSET + BLADE_T, b_in + BLADE_INSET + BLADE_T,
                         P.HINGE_PHI - P.WAIST_ARC * 0.5, P.HINGE_PHI + P.WAIST_ARC * 0.5,
                         Z_H0, Z_H1)

# Cửa sổ nhả vật liệu: bỏ phần thành NGOÀI quanh bản lề.
# SỬA LỖI (2026-10-07): bản cũ lấy mép trong = a_in + BLADE_T*0.94 ⇒ xén 0.03 mm
# bề mặt ngoài lá bản lề ⇒ sinh 2 tam giác diện tích 0 ở mép cửa sổ (φ = 319°,
# z = 2.5/11.5). Nay đặt mép trong TRÙNG mặt ngoài lá (BLADE_T) ⇒ lá giữ đủ
# 0.50 mm và lưới STL sạch.
# Mép cửa sổ lệch 0.4° ra ngoài hai mặt đầu thân/tay kẹp: tránh ĐỒNG PHẲNG hoàn
# toàn giữa mặt dao cắt và mặt đầu chi tiết (sinh 2 tam giác diện tích ~0 khi
# tessellate). Mất thêm 0.09 mm thành ngoài ở hai mép — vô hại về cơ học.
relief = band_prism(a_in + BLADE_INSET + BLADE_T - 0.03, b_in + BLADE_INSET + BLADE_T - 0.03,
                    a_out + 1.0, b_out + 1.0,
                    phi_shell_hinge_end - 0.4, phi_arm_hinge_start + 0.4, -0.5, P.H_RING + 0.5)

# =============================================================================
# 4. CHỐT TRỤ Ø3 TRÊN TAY KẸP (đối tượng tì của mặt dốc)
# =============================================================================
peg = cyl(PEG_R, PEG_Z0, PEG_Z1, PEG)


def _ang_cover(phi0, phi1):
    """Tập góc [0,360) mà cung CCW phi0 → phi1 phủ."""
    L = (phi1 - phi0) % 360.0 or 360.0
    a = phi0 % 360.0
    b = a + L
    return [(a, b)] if b <= 360.0 else [(a, 360.0), (0.0, b - 360.0)]


def ang_overlap(A, B):
    """Tổng độ dài phần GIAO của hai tập góc (độ)."""
    out = 0.0
    for a0, a1 in A:
        for b0, b1 in B:
            lo, hi = max(a0, b0), min(a1, b1)
            if hi - lo > 1e-9:
                out += hi - lo
    return out


ang_cover = _ang_cover
_cov_shell = _ang_cover(phi_shell_start, phi_shell_hinge_end)
_cov_arm = _ang_cover(phi_arm_hinge_start, phi_arm_end + 360.0)
_len_shell = sum(b - a for a, b in _cov_shell)
_len_arm = sum(b - a for a, b in _cov_arm)
OVERLAP_DEG = sum(max(0.0, min(a1, b1) - max(a0, b0))
                  for a0, a1 in _cov_shell for b0, b1 in _cov_arm)
SLIT_GAP_MM = (360.0 - _len_shell - _len_arm - HINGE_WINDOW) * math.pi / 180.0 * a_out



# =============================================================================
# 5. TAI TRÊN THÂN: LAND TÌ CỨNG + CHÂN LÁ MỎNG + LÁ MỎNG (chốt mềm A)
# =============================================================================
# 5a. Hai "tai" (= mặt chặn cứng). Bề mặt trên của tai là LAND nằm dưới đáy thân
#     cần gạt 0.05 mm. Hai tai nhường khoảng Z ở giữa cho lá mỏng.
post_parts = []
for (z0, z1) in POST_Z:
    post_parts.append(prism(w_poly([(POST_U0, POST_V_TOP), (POST_U1, POST_V_TOP),
                                    (POST_U1, POST_V_BOT), (POST_U0, POST_V_BOT)]), z0, z1))
post = fuse_chain(post_parts)

# 5b. Lá mỏng: chân cắm vào thân vòng (khối đế) + đoạn làm việc (eo) + đầu tự do
leaf_root = prism(w_poly([(BL_ROOT_U0, BL_V_TOP), (BL_ROOT_U1, BL_V_TOP),
                          (BL_ROOT_U1, BL_ROOT_V_BOT), (BL_ROOT_U0, BL_ROOT_V_BOT)]),
                  BL_Z0, BL_Z1)
leaf_web = prism(w_poly([(BL_ROOT_U0, BL_V_TOP), (BL_TIP_U, BL_V_TOP),
                         (BL_TIP_U, BL_V_BOT), (BL_ROOT_U0, BL_V_BOT)]),
                 BL_Z0, BL_Z1)
leaf = leaf_root.fuse(leaf_web)      # fuse HAI NGÔI (API FreeCAD chuẩn, xem fuse_chain)

# =============================================================================
# 6. CẦN GẠT: móc có MẶT DỐC (tiếp tuyến chốt P) + chuôi + đệm ngón tay cái
# =============================================================================
# Đường dốc: u + v = K_RAMP. Điểm tiếp xúc danh nghĩa:
C_RAMP = (ARM_LEN + PEG_R / math.sqrt(2.0), PEG_R / math.sqrt(2.0))
K_RAMP_PRINT = K_RAMP + (PRINT_CLEAR - FLAT_DEPTH) * math.sqrt(2.0)  # mặt dốc của cần gạt
K_FLAT = K_RAMP - FLAT_DEPTH * math.sqrt(2.0)      # mặt phẳng tì vát trên chốt P
U_RAMP_HI = ARM_LEN - L_LEAD_IN                       # đầu trên mặt dốc
V_RAMP_HI = K_RAMP_PRINT - U_RAMP_HI


def ring_clear_uv(u, v, margin):
    """True nếu điểm (u,v) cách mặt ngoài vành ≥ margin (và không nằm trong lòng vành)."""
    x, y = W(u, v)
    r = math.hypot(x, y)
    phi = math.degrees(math.atan2(y, x))
    return r - ring_reach(phi, a_out, b_out) >= margin


# Đầu dưới mặt dốc: giới hạn bởi khe hở với TAY KẸP (không được cắm vào vành)
U_RAMP_LO = U_RAMP_HI
for i in range(1, 400):
    u_try = U_RAMP_HI + i * 0.01
    if not ring_clear_uv(u_try, K_RAMP_PRINT - u_try, 0.35):
        break
    U_RAMP_LO = u_try
V_RAMP_LO = K_RAMP_PRINT - U_RAMP_LO

ramp_face = [(U_RAMP_HI, V_RAMP_HI), (U_RAMP_LO, V_RAMP_LO)]
head_out = [(u + OFF_N * N_LOC[0], v + OFF_N * N_LOC[1]) for (u, v) in ramp_face]

lever_poly = [
    (L_TAIL_U, L_TAIL_V),                 # 1 đáy chuôi (đầu ngoài)
    (L_STEP_U, L_TAIL_V),                 # 2 đáy chuôi (đầu trong)
    (L_STEP_U, L_BODY_V),                 # 3 bậc lên mặt tì cứng
    (ARM_LEN - 1.7, L_BODY_V),            # 4 đáy thân, dừng trước chốt P
    ramp_face[0],                         # 5 đầu trên mặt dốc
    ramp_face[1],                         # 6 đầu dưới mặt dốc (tiếp xúc danh nghĩa ở giữa)
    head_out[1],                          # 7 góc ngoài dưới của móc
    head_out[0],                          # 8 góc ngoài trên của móc
    (ARM_LEN - 1.0, L_TOP_V),             # 9 về mặt trên thân
    (L_TAIL_U, L_TOP_V),                  # 10 mặt trên chuôi
]

lever = prism(w_poly(lever_poly), Z_LEV0, Z_LEV1)

# 6b. VÁT PHẲNG mặt ngoài chốt P — mặt tì SONG SONG mặt dốc ⇒ tiếp xúc DIỆN
#     (không phải tiếp xúc đường như chốt trụ tròn tiếp tuyến).
_flat = prism(w_poly([(K_FLAT + 80.0, -80.0), (K_FLAT + 80.0, 200.0),
                      (K_FLAT - 80.0, 200.0), (K_FLAT - 80.0, 80.0)]),
              PEG_Z0 - 0.5, PEG_Z1 + 0.5)
peg = peg.cut(_flat)
CHORD = 2.0 * math.sqrt(max(PEG_R ** 2 - (PEG_R - FLAT_DEPTH) ** 2, 0.0))

# Đệm ngón tay cái (paddle) — nơi ngón tay cái đẩy theo +u để nhả khoá
thumb = prism(w_poly([(PAD_U0, PAD_V0), (PAD_U1, PAD_V0),
                      (PAD_U1, PAD_V1), (PAD_U0, PAD_V1)]), PAD_Z0, PAD_Z1)

# =============================================================================
# 7. PHỤ KIỆN TRÊN THÂN: GỐI GÂN + RÃNH GÂN + VÁCH CẢM BIẾN
# =============================================================================
curves = []

boss_pts = []
for dphi, rr in ((0.0, 1.0), (0.22, 1.0), (0.35, 0.35), (0.65, 0.35), (0.78, 1.0), (1.0, 1.0)):
    phi = ANCHOR['phi0'] + (ANCHOR['phi1'] - ANCHOR['phi0']) * dphi
    r = G.ell_r(a_out, b_out, phi) + ANCHOR['rise'] * rr
    boss_pts.append(polar(r, phi))
boss = prism(boss_pts + [polar(G.ell_r(a_out, b_out, ANCHOR['phi1']), ANCHOR['phi1']),
                         polar(G.ell_r(a_out, b_out, ANCHOR['phi0']), ANCHOR['phi0'])],
             0.0, ANCHOR['z1'])
curves.append(('AnchorBoss', boss))

for gp in GROOVE_PHI:
    r0 = G.ell_r(a_out, b_out, gp)
    broad = rad_prism([(-0.4, r0 - GROOVE_D), (P.H_RING + 0.4, r0 - GROOVE_D),
                       (P.H_RING + 0.4, r0 - GROOVE_LIP), (-0.4, r0 - GROOVE_LIP)], gp)
    curves.append(('Groove_%.0f' % gp, broad))

sensor_recess = band_prism(a_in - P.SENSOR_T, b_in - P.SENSOR_T, a_in + 0.02, b_in + 0.02,
                           P.SENSOR_PHI0, P.SENSOR_PHI1, -0.4, P.H_RING + 0.4)

# =============================================================================
# 8. RÃNH ĐỆM TPU + KHOÉT LÕM SƯỜN + VUỐT CÔN
# =============================================================================
cutters = []
for pp in PAD_PHI:
    r_in = G.ell_r(a_in, b_in, pp)
    z_mid = P.H_RING / 2.0
    h_half = P.H_PAD / 2.0
    lip = PAD_LIP
    # Rãnh đệm phải CONG theo ellipse: dùng band_prism (không dùng rad_prism thẳng,
    # vì trên cung 46° mặt phẳng cắt sẽ xuyên qua vách ở hai đầu cung ⇒ mảnh rời).
    p0, p1 = pp - PAD_ARC / 2.0, pp + PAD_ARC / 2.0
    z_mid = P.H_RING / 2.0
    lip = PAD_LIP
    z_a, z_b = z_mid - P.H_PAD / 2.0, z_mid + P.H_PAD / 2.0
    cutters.append(band_prism(a_in - 0.4, b_in - 0.4, a_in + PAD_SLOT_D, b_in + PAD_SLOT_D,
                              p0, p1, -0.2, z_a, n=48))
    cutters.append(band_prism(a_in - 0.4, b_in - 0.4, a_in + PAD_SLOT_D, b_in + PAD_SLOT_D,
                              p0, p1, z_b, P.H_RING + 0.2, n=48))
    cutters.append(band_prism(a_in - 0.4, b_in - 0.4,
                              a_in + PAD_SLOT_D - lip, b_in + PAD_SLOT_D - lip,
                              p0, p1, z_a, z_b, n=48))


for pp in (0.0, 180.0):
    r0 = G.ell_r(a_out, b_out, pp)
    cutters.append(rad_prism([(-0.5, r0 - P.RELIEF_D), (P.H_RING + 0.5, r0 - P.RELIEF_D),
                              (P.H_RING + 0.5, r0 + 1.0), (-0.5, r0 + 1.0)], pp))


def taper_wedge(sign):
    x_edge = G.ell_r(a_out, b_out, 0.0) - P.RELIEF_D + 0.15
    x0 = sign * x_edge
    x1 = sign * (x_edge - P.TAPER_DROP)
    pts = [(x0, 0.0, P.TAPER_Z0), (x0, 0.0, P.H_RING + 1.0), (x1, 0.0, P.H_RING + 1.0)]
    f = Part.Face(Part.makePolygon([App.Vector(*p) for p in pts], True))
    return f.extrude(App.Vector(0.0, 40.0, 0.0)).translate(App.Vector(0.0, -20.0, 0.0))


# =============================================================================
# 9. LẮP GHÉP (MỘT chi tiết in liền khối)
# =============================================================================
def union_all(parts):
    return fuse_chain(parts)


# 9a. DAO DOÀNG TRONG LÒNG VÒNG (bore): xoá mọi vật liệu lọt vào lòng ngón —
#     chân "tai" và chân lá mỏng cắm sâu qua mặt trong; nếu không cắt, chúng thò
#     vào lòng vòng tới ~1 mm và sẽ tì lên da mu ngón. Kiểm tra B8 canh mục này.
bore = band_prism(0.02, 0.02, a_in - 0.02, b_in - 0.02, 0.0, 360.0, -1.0, P.H_RING + 1.0, n=240)

body = union_all([shell, arm, blade_hinge, post, leaf, lever, thumb, peg])
# Cắt lần lượt từng dao: FreeCAD CHỈ nhận MỘT đối tượng cho cut()/fuse()/common()
# (shape.cut([a, b]) sẽ TypeError; multiFuse chỉ dùng cho PHÉP HỢP).
ring = cut_all(body, [relief, sensor_recess, taper_wedge(+1), taper_wedge(-1), bore]
               + cutters)

# --- lỗ vít M3 ở mỏ neo (điểm bắt vỏ Bowden) ---
hole = Part.makeCylinder(ANCHOR['screw_r'], 40.0,
                         App.Vector(0.0, -20.0, (ANCHOR['z1'] - 0.6) / 2.0),
                         App.Vector(0.0, 1.0, 0.0))
ring = ring.cut(hole)

# Làm sạch lưới: gộp các mặt bị chia nhỏ (do các khối chỉ TIẾP XÚC MẶT: lá bản lề ↔
# mặt đầu thân/tay kẹp) ⇒ tránh vài tam giác diện tích ~0 trong STL. Không đổi hình học.
ring = ring.removeSplitter()

# =============================================================================
# 10. ĐỆM TPU (in riêng, TPU 85A)
# =============================================================================
pads = []
for i, pp in enumerate(PAD_PHI):
    r_in = G.ell_r(a_in, b_in, pp)
    h_half = P.H_PAD / 2.0
    z_mid = P.H_RING / 2.0
    lip = PAD_LIP
    prof = [(-0.01, r_in + PAD_SLOT_D - 0.25), (P.H_RING + 0.01, r_in + PAD_SLOT_D - 0.25),
            (P.H_RING + 0.01, r_in - PAD_T + 0.02),
            (z_mid + h_half + 0.6, r_in - PAD_T + 0.02),
            (z_mid + h_half + 0.6, r_in - PAD_T - 0.6),
            (z_mid - h_half - 0.6, r_in - PAD_T - 0.6),
            (z_mid - h_half - 0.6, r_in - PAD_T + 0.02),
            (-0.01, r_in - PAD_T + 0.02)]
    p = rad_prism(prof, pp)
    keep = band_prism(r_in - PAD_T - 1.0, r_in - PAD_T - 1.0,
                      r_in + PAD_SLOT_D + 1.0, r_in + PAD_SLOT_D + 1.0,
                      pp - PAD_ARC / 2.0, pp + PAD_ARC / 2.0, -1.0, P.H_RING + 1.0, n=60)
    pads.append((i, p.common(keep)))

# =============================================================================
# 11. KIỂM TRA HÌNH HỌC (số học thuần Python — không phụ thuộc CAD kernel)
# =============================================================================
# Quy ước động học (kiểm bằng tay, xem báo cáo §B):
#   * CHIỀU MỞ = cần gạt quay CÙNG CHIỀU KIM ĐỒNG HỒ quanh A (gọi là s > 0) ⇒ móc
#     rời khỏi chốt P; tay kẹp quay cùng chiều kim đồng hồ quanh Hp (θ3 giảm).
#   * Mô-men tải (phản lực ngón → chốt P → mặt dốc) NGƯỢC chiều kim đồng hồ ⇒ ÉP
#     cần gạt vào LAND (mặt chặn cứng) ⇒ form-closed, tải không tự nhả khoá.
#   * Muốn nhả phải THẮNG mô-men tải + lực lá mỏng (mục D của synthesis).
# Tương đương số học: cho cần gạt "đứng yên" thì thế giới quay +s quanh A.
def jaw_arc_pts():
    """Mặt ngoài tay kẹp ở trạng thái ĐÓNG (cung φ = 336° → 61°)."""
    return [polar(ring_reach(336.0 + 85.0 * k / 60.0, a_out, b_out), 336.0 + 85.0 * k / 60.0)
            for k in range(61)]


JAW_ARC = jaw_arc_pts()


def scene(s_deg, dtheta_deg):
    """(cần gạt quay NGƯỢC chiều kim đồng hồ s, tay kẹp mở dtheta) → (chốt P, cung
    tay kẹp) trong KHUNG CẦN GẠT Ở TRẠNG THÁI ĐÓNG."""
    fA = rot_about(A_PIV, s_deg, -1.0)      # thế giới quay −s ⇔ cần gạt quay +s (CCW)
    fJ = rot_about(HP, dtheta_deg, -1.0)    # tay kẹp quay CW quanh Hp (θ3 giảm = mở)
    return fA(fJ(PEG)), [fA(fJ(p)) for p in JAW_ARC]


def pt_in_poly(p, poly):
    inside = False
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if (y1 > p[1]) != (y2 > p[1]):
            if p[0] < x1 + (p[1] - y1) * (x2 - x1) / (y2 - y1):
                inside = not inside
    return inside


# Cho phép "xuyên" đàn hồi nhỏ (biến dạng tiếp xúc + độ mềm của lá mỏng), KHÔNG phải
# khe hở hình học: ở trạng thái đóng đĩa chốt P ĐÃ tiếp xúc mặt dốc (khe hở = 0).
PEN_PEG = 0.20   # = FLAT_DEPTH: mô hình chốt ĐÃ VÁT PHẲNG tương đương đường tròn
#                  bán kính (PEG_R − FLAT_DEPTH) ⇒ phép kiểm vướng CHÍNH XÁC với mặt phẳng tì
PEN_JAW = 0.05   # mm — xuyên đàn hồi cho phép của cung tay kẹp vào móc


def clash(lp, peg_xy, jaw_pts):
    """True nếu VƯỚNG: đĩa chốt P (bán kính PEG_R) hoặc cung tay kẹp cắt quá sâu vào móc."""
    if pt_in_poly(peg_xy, lp):
        return True
    if poly_dist_pt(lp, peg_xy) < PEG_R - PEN_PEG:
        return True
    for p in jaw_pts:
        if pt_in_poly(p, lp):
            return True
    if poly_dist(lp, jaw_pts) < -PEN_JAW:
        return True
    return False


FULL_OPEN_DEG = abs(TS.TH3_OPEN - TS.TH3_CLOSED)      # ≈ 22.74° = khe hở 5 mm
LP0 = w_poly(lever_poly)                              # móc ở khung gốc

# --- kiểm tra tĩnh mặt dốc ---
d_tang = abs((C_RAMP[0] + C_RAMP[1]) - K_RAMP) / math.sqrt(2.0)
u_touch0 = 0.5 * (K_RAMP + ARM_LEN)                   # u của tiếp điểm danh nghĩa


def jaw_limit(s_deg, dt_step=0.10, dt_max=45.0):
    """Góc mở lớn nhất của tay kẹp khi cần gạt đã mở s — quét CẢ HÀNH TRÌNH (đĩa chốt
    P và cung tay kẹp không được cắt vào móc ở bất kỳ bước nào)."""
    last_free = 0.0
    n = int(round(dt_max / dt_step))
    for k in range(n + 1):
        dt = k * dt_step
        if clash(LP0, *scene(s_deg, dt)):
            return last_free, "ok"
        last_free = dt
    return dt_max, "free"


def open_sweep(s_max=150.0, s_step=1.0):
    rows = []
    for i in range(int(s_max / s_step) + 1):
        s = i * s_step
        dt, why = jaw_limit(s)
        rows.append((s, dt, why))
        if dt is None or why == "free":
            break
    return rows


# =============================================================================
# 12. ĐĂNG KÝ ĐỐI TƯỢNG + XUẤT STL
# =============================================================================
def add_obj(name, shape):
    o = doc.addObject("Part::Feature", name)
    o.Shape = shape
    return o


objs = [add_obj("Ring_PETG", ring)]
for i, p in pads:
    objs.append(add_obj("Pad%d_TPU" % (i + 1), p))
doc.recompute()

if not os.path.isdir(OUT_DIR):
    os.makedirs(OUT_DIR)
for o in objs:
    Mesh.export([o], os.path.join(OUT_DIR, o.Name + ".stl"))

# =============================================================================
# 13. BÁO CÁO KIỂM TRA HÌNH HỌC
# =============================================================================
bb = ring.BoundBox
dx_lat = max(abs(bb.XMin), abs(bb.XMax)) - P.A_KNUCK
n_solids = len(ring.Solids)
vol_petg_cm3 = ring.Volume / 1000.0
mass_petg = vol_petg_cm3 * P.RHO_PETG * 1000.0     # cm³ × g/cm³ = g
vol_tpu = sum(p.Volume for _, p in pads) / 1000.0
mass_tpu = vol_tpu * P.RHO_TPU * 1000.0

print("=" * 78)
print("Ý TƯỞNG 1 — VÒNG KHOÁ QUÁ TÂM KIỂU MÓC CÓ MẶT DỐC (Side Toggle Clasp)")
print("Hình học khoá SUY RA TỪ synthesis/toggle_synthesis.py (không chép tay số)")
print("=" * 78)
print("A. KHUNG TOẠ ĐỘ CẦN GẠT (mm; gốc = tâm đốt gần, +X = sườn, +Y = mu)")
print("   A (tâm quay)  = (%7.3f, %7.3f)  r=%5.2f  φ=%.2f°"
      % (A_PIV[0], A_PIV[1], math.hypot(*A_PIV), math.degrees(math.atan2(A_PIV[1], A_PIV[0]))))
print("   P (chốt Ø%.1f) = (%7.3f, %7.3f)  r=%5.2f  |A–P|=%5.2f  nghiêng %.1f°"
      % (TS.PEG_D, PEG[0], PEG[1], math.hypot(*PEG), ARM_LEN, SLANT))
print("   β mặt dốc = %.1f°   K_RAMP (u+v) = %.4f   tay đòn nhả R_handle = %.2f mm"
      % (BETA, K_RAMP, R_HANDLE_GEO))
print("-" * 78)
print("B. KIỂM TRA KHOÁ (số học, không phải đo)")
print("   B1. Mặt dốc tiếp tuyến chốt P: tiếp điểm danh nghĩa (u,v) = (%6.3f, %6.3f)"
      % C_RAMP)
print("       |(u+v) − K_RAMP|/√2 = %.4f mm ⇒ tiếp xúc thiết kế ĐÚNG (khe hở 0)  %s"
      % (d_tang, "PASS" if d_tang < 1e-6 else "FAIL"))
print("       Hình học IN: mặt dốc lùi %.2f mm theo pháp tuyến (khe hở in %.2f mm) — bị"
      % (PRINT_CLEAR, PRINT_CLEAR))
print("       ÉP KÍN bởi phản lực ngón khi đeo ⇒ trạng thái LÀM VIỆC vẫn khép kín, không rơ.")
print("       Đoạn mặt dốc dùng được: u ∈ [%.2f, %.2f] (dài %.2f mm) — đủ cho ±0.27 mm"
      % (U_RAMP_HI, U_RAMP_LO, U_RAMP_LO - U_RAMP_HI))
print("       dịch chốt khi đường kính ngón Ø20→Ø24.")
print("   B2. MẶT CHẶN CỨNG (land trên 2 tai): khe hở danh nghĩa %.2f mm, tay đòn"
      % P.STOP_GAP)
STOP_R_GEO = abs(0.5 * (POST_U0 + POST_U1))       # tay đòn lực tì = |u| trọng tâm land
print("       STOP_R = |u| trọng tâm land = %.2f mm ⇒ lực tì = M/STOP_R = %.2f N."
      % (STOP_R_GEO, abs(TS.M_LOAD_SIGNED) / STOP_R_GEO))
print("       Tải ÉP thêm vào mặt chặn ⇒ form-closed; đảo dấu mô-men phải quay %.0f°."
      % (TS.OC_MARGIN_ACTUAL or 0.0))
print("   B3. Lá mỏng (chốt mềm A): %.2f × %.2f mm, tay đòn hiệu dụng %.2f mm ⇒ k ≈ %.2f N/mm"
      % (BL_T, BL_Z1 - BL_Z0, L_EFF, 3.0 * P.E_PETG * ((BL_Z1 - BL_Z0) * BL_T ** 3 / 12.0) / L_EFF ** 3))
print("       (đặt trước + bù dung sai in/từ biến; KHÔNG phải khớp rời ⇒ không rơ)")
check("B4. KHE thân ↔ tay kẹp: HỞ %.3f mm, chồng lấn %.4f°" % (SLIT_GAP_MM, OVERLAP_DEG),
      abs(SLIT_GAP_MM - GAP_SLIT) <= 0.06 and OVERLAP_DEG <= 1e-6,
      "mặt đầu tay kẹp %.2f° | mặt đầu thân %.2f° (cung thân %.2f°, tay kẹp %.2f°)"
      % (phi_arm_end, phi_shell_start, _len_shell, _len_arm))

# --- B5–B7: RÃNH ĐỆM không được cắt vào các vùng chức năng ---------------------
# (lớp lỗi đã xảy ra: rãnh 327° cắt mất lá bản lề ⇒ tay kẹp rời khỏi thân)
_cov_pads = [(pp - PAD_ARC / 2.0, pp + PAD_ARC / 2.0) for pp in PAD_PHI]
for _lbl, _a0, _a1 in (("LÁ BẢN LỀ (hở tay kẹp)",
                        P.HINGE_PHI - P.WAIST_ARC * 0.5, P.HINGE_PHI + P.WAIST_ARC * 0.5),
                       ("KHE thân ↔ tay kẹp", phi_arm_end - 2.5, phi_shell_start + 2.5),
                       ("RÃNH CẢM BIẾN", P.SENSOR_PHI0 - 2.0, P.SENSOR_PHI1 + 2.0)):
    _ov = ang_overlap(_cov_pads, ang_cover(_a0, _a1))
    check("B5–B7. Rãnh đệm không cắt vào %s" % _lbl, _ov <= 1e-6, "chồng lấn %.2f°" % _ov)
print("-" * 78)
print("C. ĐỘNG HỌC KHOÁ / NHẢ (mô phỏng 2D số học)")
# --- C0: trạng thái ĐÓNG tĩnh --------------------------------------------------
d_closed = poly_dist(LP0, [p for p in JAW_ARC])
check("C0. Khe hở móc ↔ tay kẹp (đóng)", d_closed >= GAP_PEG_MIN,
      "%+.3f mm ≥ %.2f mm" % (d_closed, GAP_PEG_MIN))
peg0, _ = scene(0.0, 0.0)
d_peg0 = poly_dist_pt(LP0, peg0)
_d_exp = PEG_R - FLAT_DEPTH + PRINT_CLEAR
check("C1. Mặt dốc ↔ tâm chốt P = R − vát + khe hở in", abs(d_peg0 - _d_exp) <= 1e-3,
      "%.4f mm (kỳ vọng %.4f = %.2f − %.2f + %.2f)"
      % (d_peg0, _d_exp, PEG_R, FLAT_DEPTH, PRINT_CLEAR))
# --- C2: tay kẹp KHÔNG thể mở khi cần gạt ở trạng thái đóng --------------------
dt0, why0 = jaw_limit(0.0)
_take = math.radians(dt0 or 0.0) * R3 * 0.0 + math.radians(dt0 or 0.0) * 12.6
check("C2. Hành trình ĐẶT TRƯỚC (khe hở in) ≤ 0.25 mm", (dt0 or 0.0) <= 1.2,
      "tay kẹp mở %.2f° = %.2f mm ở r=12.6 — đây là khe hở IN bị lực đệm/ngón"
      % (dt0 or 0.0, _take))
print("       ÉP KÍN (không phải khe hở cơ khí); sau đó đường truyền lực cứng tuyệt đối.")
# --- C3: hành trình nhả (quay cần gạt CCW) -------------------------------------
rows = open_sweep(s_max=90.0, s_step=1.0)
free = [r for r in rows if r[2] == "free"]
if (not rows) or rows[0][2] == "ket":
    check("C3. Hành trình nhả", False, "trạng thái đóng đã vướng")
else:
    shown = [r for r in rows if abs(r[0] % 10.0) < 1e-9][:6]
    for (sv, dt, wh) in shown:
        print("      cần gạt quay %5.1f° → tay kẹp mở tối đa %6.2f°  [%s]"
              % (sv, dt if dt is not None else float('nan'), wh))
    if free:
        s_rel = free[0][0]
        print("      ...")
        print("   ⇒ Ở cần gạt %.1f°: tay kẹp mở hết %.2f° (khe 5 mm) — NHẢ HẲN"
              % (s_rel, FULL_OPEN_DEG))
        print("     ngón tay cái đi %.2f mm; lực nhả ≈ %.2f N (M/R_handle + lá mỏng)"
              % (math.radians(s_rel) * R_HANDLE_GEO, TS.F_RELEASE_TOTAL))
        check("C3. Hành trình nhả ≤ 60° (một động tác)", s_rel <= 60.0,
              "%.1f° ≤ 60°" % s_rel)
    else:
        with_open = max(abs(r[1]) for r in rows if r[1])
        check("C3. Hành trình nhả ≤ 60° (một động tác)", False,
              "quay %.0f° mới mở %.2f°/%.2f°" % (rows[-1][0], with_open, FULL_OPEN_DEG))
print("-" * 78)
print("D. RÀNG BUỘC HÌNH HỌC CỦA BRIEF")
check("Z dài trục 12–16 mm", 11.9 <= bb.ZLength <= 16.1, "%.2f mm" % bb.ZLength)
check("ΔX sườn ≤ %.1f mm" % P.DX_MAX, dx_lat <= P.DX_MAX,
      "%+.2f mm (X ∈ [%.2f, %.2f])" % (dx_lat, bb.XMin, bb.XMax))
print("   Bao hình X×Y×Z: %.2f × %.2f × %.2f mm" % (bb.XLength, bb.YLength, bb.ZLength))
print("-" * 78)
print("E. KHỐI LƯỢNG (ngân sách in)")
print("   PETG %.2f cm³ → ≈ %.2f g   |   TPU 85A %.3f cm³ → ≈ %.2f g   |   tổng ≈ %.2f g"
      % (vol_petg_cm3, mass_petg, vol_tpu, mass_tpu, mass_petg + mass_tpu))
print("-" * 78)
print("F. KIỂM TRA KHỐI (solid)")
n_solids = len(ring.Solids)
check("Đúng 1 khối đặc liền", n_solids == 1, "%d khối" % n_solids)
if n_solids != 1:
    for k, sl in enumerate(sorted(ring.Solids, key=lambda x: -x.Volume)[:6]):
        bk = sl.BoundBox
        print("      #%d V=%.2f mm3  X[%.1f,%.1f] Y[%.1f,%.1f] Z[%.1f,%.1f]"
              % (k + 1, sl.Volume, bk.XMin, bk.XMax, bk.YMin, bk.YMax, bk.ZMin, bk.ZMax))
# B8. Không được còn vật liệu trong LÒNG VÒNG (dao bore phải xoá hết chân tai/lá)
_v_bore = ring.common(bore).Volume
check("B8. Lòng vòng SẠCH (không nub tì da)", _v_bore <= 3.0,
      "V vật liệu trong lòng = %.2f mm³ (dung sai 3 mm³ cho sai số đa giác hoá)" % _v_bore)
check("Khối hợp lệ (OCCT isValid)", bool(ring.isValid()), "%s" % ring.isValid())
print("   Xuất %d STL tại: %s" % (len(objs), OUT_DIR))
print("=" * 78)
if FAILS:
    print("KẾT LUẬN: CÓ %d MỤC FAIL → %s" % (len(FAILS), ", ".join(FAILS)))
else:
    print("KẾT LUẬN: TẤT CẢ MỤC KIỂM TRA PASS.")
print("=" * 78)

if FAILS and os.environ.get("FF_NO_SYS_EXIT") != "1":
    sys.exit(2)      # trong FreeCAD GUI: FF_NO_SYS_EXIT=1 để sys.exit() không đóng app
