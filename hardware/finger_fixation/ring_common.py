# -*- coding: utf-8 -*-
"""
ring_common.py — TIỆN ÍCH DÙNG CHUNG cho các script sinh STL của bộ cố định đốt gần P1
================================================================================
Dùng bởi build_idea2_ratchet_cinch.py và build_idea3_wrap_band.py (Ý tưởng 1 tự chứa
để bảo đảm tính độc lập của bản kiểm tra đã công bố).

Quy ước khung toạ độ (mm):
    gốc = tâm đốt gần;  +X = sườn (về phía ngón giữa);  +Y = mu (dorsal);  +Z = về đốt xa.
    φ đo CCW từ +X:  0° = sườn, 90° = mu, 180° = sườn đối diện, 270° = bụng.

Toàn bộ khối là LĂNG TRỤ theo Z (in không cần support) — đúng tinh thần đã đặt ra
cho cả 3 ý tưởng.
"""
import math
import os
import sys

import FreeCAD as App
import Part
import Mesh

def script_dir():
    """Thư mục chứa script này — hoạt động cả khi được exec() trong FreeCAD GUI.

    Trong FreeCAD GUI, `__file__` không tồn tại nếu người dùng dán lệnh
    exec(open(...).read()) vào cửa sổ Python ⇒ dò tiếp trong thư mục làm việc.
    """
    if "__file__" in globals():
        return os.path.dirname(os.path.abspath(__file__))
    cwd = os.getcwd()
    for d in (cwd, os.path.join(cwd, "hardware", "finger_fixation")):
        if os.path.isfile(os.path.join(d, "params.py")):
            return d
    raise RuntimeError(
        "Không tìm thấy params.py cạnh script. Hãy chạy bằng run_in_freecad.py "
        "(hoặc cd vào hardware/finger_fixation trước khi exec).")


_HERE = script_dir()
for _p in (_HERE, os.path.join(_HERE, "synthesis")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import params as P   # noqa: E402
import fcgeom as G   # noqa: E402

OUT_DIR = os.path.join(_HERE, "stl")
FAILS = []


# ---------------------------------------------------------------- thông báo ---
def check(name, ok, txt):
    if not ok:
        FAILS.append(name)
    print("   [%s] %-38s %s" % ("PASS" if ok else "FAIL", name, txt))


def finish(shape, pads, title, extras, subdir=None, extra_parts=()):
    """Đăng ký đối tượng, xuất STL, in bảng tổng hợp. → mã thoát (0/2).

    subdir: thư mục con trong stl/ (mỗi ý tưởng một thư mục để KHÔNG ghi đè STL
    của nhau — cả 3 ý tưởng đều có Ring_PETG.stl + Pad*_TPU.stl).
    extra_parts: [(tên, khối)] cho các chi tiết in rời khác (đai TPU, chêm...).
    """
    doc = App.newDocument(title.replace(" ", "_")[:40])
    objs = [_add(doc, "Ring_PETG", shape)]
    for i, p in pads:
        objs.append(_add(doc, "Pad%d_TPU" % (i + 1), p))
    for (name, sh) in extra_parts:
        objs.append(_add(doc, name, sh))
    doc.recompute()
    out_dir = os.path.join(OUT_DIR, subdir) if subdir else OUT_DIR
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    for o in objs:
        Mesh.export([o], os.path.join(out_dir, o.Name + ".stl"))
    print("-" * 78)
    for line in extras:
        print(line)
    print("   Xuất %d STL tại: %s" % (len(objs), out_dir))
    if FAILS:
        print("KẾT LUẬN: CÒN %d MỤC CHƯA ĐẠT: %s" % (len(FAILS), ", ".join(FAILS)))
        return 2
    print("KẾT LUẬN: TẤT CẢ MỤC KIỂM TRA PASS.")
    return 0


def _add(doc, name, shape):
    o = doc.addObject("Part::Feature", name)
    o.Shape = shape
    return o


# ------------------------------------------------------------------ dựng 3D ---
def prism(pts2d, z0, z1):
    if len(pts2d) < 3:
        raise ValueError("prism cần >= 3 điểm")
    # LƯU Ý: makePolygon là varargs-method của FreeCAD ⇒ KHÔNG nhận keyword;
    # tham số "closed" phải truyền THEO VỊ TRÍ (closed=True sẽ TypeError).
    w = Part.makePolygon([App.Vector(x, y, z0) for (x, y) in pts2d], True)
    return Part.Face(w).extrude(App.Vector(0.0, 0.0, float(z1) - float(z0)))


def band_prism(a_in, b_in, a_out, b_out, phi0, phi1, z0, z1, n=180):
    return prism(G.band(a_in, b_in, a_out, b_out, phi0, phi1, n), z0, z1)


def local_poly(pts_uv, phi, r_ref):
    origin, rot = G.local_frame(phi, r_ref)
    return G.tf(pts_uv, origin, rot)


def local_prism(pts_uv, phi, r_ref, z0, z1):
    return prism(local_poly(pts_uv, phi, r_ref), z0, z1)


def rad_prism(pts_zv, phi):
    """Khối từ đa giác trong mặt phẳng (Z,v) rồi extrude theo TIẾP TUYẾN (chord)."""
    t = G.deg(phi)
    rhat = (math.cos(t), math.sin(t))
    that = (-math.sin(t), math.cos(t))
    pts3 = [(rhat[0] * v + that[0] * (-60.0), rhat[1] * v + that[1] * (-60.0), z)
            for (z, v) in pts_zv]
    f = Part.Face(Part.makePolygon([App.Vector(*p) for p in pts3], True))
    return f.extrude(App.Vector(that[0] * 120.0, that[1] * 120.0, 0.0))


def polar(r, phi):
    t = G.deg(phi)
    return (r * math.cos(t), r * math.sin(t))


def cyl(radius, z0, z1, center_xy):
    return Part.makeCylinder(radius, z1 - z0, App.Vector(center_xy[0], center_xy[1], z0),
                             App.Vector(0.0, 0.0, 1.0))


def fuse_chain(parts):
    """Hợp nhiều khối bằng CHUỖI fuse HAI NGÔI — API FreeCAD chuẩn, kết quả tất định.

    Vì sao KHÔNG dùng Shape.multiFuse(): trong FreeCAD, multiFuse() chạy
    BRepAlgoAPI_BuilderAlgo (general fuse) và có thể trả về một compound còn NHIỀU
    mảnh rời (đúng thể tích hợp nhưng không phải 1 solid) ⇒ mục kiểm "1 khối liền"
    sẽ báo sai. Chuỗi fuse hai ngôi (Shape.fuse) cho đúng MỘT solid khi các khối
    giao nhau — đúng như thiết kế (các chi tiết đều ngập vào nhau ≥ 0,05 mm).
    """
    parts = [p for p in parts if p is not None]
    acc = parts[0]
    for p in parts[1:]:
        acc = acc.fuse(p)
    return acc


def union_all(parts):
    return fuse_chain(parts)


def cut_all(shape, tools):
    """Cắt LẦN LƯỢT từng dao — API FreeCAD chuẩn (cut() chỉ nhận MỘT đối tượng).

    FreeCAD không có `shape.cut([a, b, c])` (0.19–1.0 đều chỉ parse một TopoShape;
    xem src/Mod/Part/App/TopoShapePyImp.cpp → PyArg_ParseTuple "O!"). Tương tự với
    fuse()/common(); chỉ multiFuse()/generalFuse() nhận danh sách và chỉ dùng cho
    PHÉP HỢP. Vì vậy mọi phép cắt nhiều dao phải lặp ở đây.
    """
    for t in tools:
        shape = shape.cut(t)
    return shape


def exit_code(rc):
    """Kết thúc script với mã rc — TRỪ KHI biến môi trường FF_NO_SYS_EXIT=1.

    Lý do: trong FreeCAD (nhất là bản GUI), sys.exit() ném SystemExit làm ĐÓNG ứng
    dụng. run_in_freecad.py đặt FF_NO_SYS_EXIT=1 trước khi exec các script build.
    """
    if os.environ.get("FF_NO_SYS_EXIT") == "1":
        return rc
    sys.exit(rc)


# ------------------------------------------------------ số học kiểm khe hở ---
def seg_dist(p, a, b):
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    if L2 < 1e-12:
        return math.hypot(p[0] - ax, p[1] - ay)
    t = max(0.0, min(1.0, ((p[0] - ax) * dx + (p[1] - ay) * dy) / L2))
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
    t = G.deg(phi_deg)
    return 1.0 / math.sqrt((math.cos(t) / a_out) ** 2 + (math.sin(t) / b_out) ** 2)


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


def slit_check(meta, gap_slit=0.45, tol=0.06):
    """Kiểm tra KHE thân ↔ tay kẹp: phải HỞ đúng gap_slit mm và hai khối KHÔNG chồng."""
    ok = (abs(meta["slit_gap_mm"] - gap_slit) <= tol) and (meta["overlap_deg"] <= 1e-6)
    check("KHE thân ↔ tay kẹp (đóng)", ok,
          "hở %.3f mm (đặt %.2f mm) | chồng lấn %.4f° | mặt đầu %.2f° / %.2f°"
          % (meta["slit_gap_mm"], gap_slit, meta["overlap_deg"],
             meta["phi_arm_end"], meta["phi_shell_start"]))
    return ok


# ------------------------------------- THÂN VÒNG + TAY KẸP + BẢN LỀ (chung) ---
def geom():
    a_in, b_in = P.a_in(), P.b_in()
    a_out, b_out = P.a_out(), P.b_out()
    return dict(a_in=a_in, b_in=b_in, a_out=a_out, b_out=b_out)


def slit_angles(gap=None):
    gap = P.GAP_FIT if gap is None else gap
    a_out = P.a_out()
    d = gap * 0.5 * (180.0 / (math.pi * a_out))
    return P.SLIT_PHI - d, P.SLIT_PHI + d


def ang_cover(phi0, phi1):
    """Tập góc [0,360) mà cung ĐỊNH HƯỚNG phi0 → phi1 (CCW) phủ, dạng [(a0,a1),…]."""
    L = (phi1 - phi0) % 360.0
    if L == 0.0:
        L = 360.0
    a = phi0 % 360.0
    b = a + L
    return [(a, b)] if b <= 360.0 else [(a, 360.0), (0.0, b - 360.0)]


def ang_overlap(A, B):
    """Tổng độ dài phần GIAO của hai tập góc (độ) ⇒ >0 nghĩa là HAI KHỐI CHỒNG NHAU."""
    out = 0.0
    for a0, a1 in A:
        for b0, b1 in B:
            lo, hi = max(a0, b0), min(a1, b1)
            if hi - lo > 1e-9:
                out += hi - lo
    return out


def ang_measure(A):
    return sum(b - a for a, b in A)


def shell_arm_hinge(gap_slit=0.45, hinge_window=34.0, blade_t=0.50, h_ring=None):
    """→ (shell, arm, blade_hinge, relief, meta) — dùng chung cho cả 3 ý tưởng.

    QUY ƯỚC CUNG (đã sửa lỗi "khe bị lấp"):
      – TAY KẸP (arm)  : cung [HINGE+W/2 → SLIT_PHI − d]  (mặt đầu ĐÚNG tại 61−d).
      – THÂN    (shell): cung [SLIT_PHI + d → HINGE−W/2]  (mặt đầu ĐÚNG tại 61+d).
    ⇒ giữa hai mặt đầu là KHE THẬT dài ≈ gap_slit mm. Bản cũ lấy shell bắt đầu ở
      61−d và arm kết thúc ở 61+d ⇒ hai khối CHỒNG NHAU 2d làm khe bị hàn kín,
      vòng in ra là vòng KÍN không thể mở. meta["slit_gap_mm"] kiểm lại điều này.
    """
    g = geom()
    h_ring = P.H_RING if h_ring is None else h_ring
    a_in, b_in, a_out, b_out = g["a_in"], g["b_in"], g["a_out"], g["b_out"]
    d = gap_slit * 0.5 * (180.0 / (math.pi * a_out))
    phi_arm_end = P.SLIT_PHI - d          # mặt đầu tay kẹp
    phi_shell_start = P.SLIT_PHI + d      # mặt đầu thân
    phi_sh_end = P.HINGE_PHI - hinge_window * 0.5
    phi_ar_start = P.HINGE_PHI + hinge_window * 0.5
    shell = band_prism(a_in, b_in, a_out, b_out, phi_shell_start, phi_sh_end, 0.0, h_ring)
    arm = band_prism(a_in, b_in, a_out, b_out, phi_ar_start, phi_arm_end + 360.0, 0.0, h_ring)
    # Lá bản lề LÙI 0.05 mm khỏi mặt trong (tránh hai mặt trụ TRÙNG NHAU với thân/
    # tay kẹp ⇒ tessellate sinh tam giác diện tích ~0); dao relief xén mép cửa sổ để
    # chiều dày làm việc của lá = blade_t − 0.03 khi đã đóng cửa sổ.
    blade = band_prism(a_in + 0.05, b_in + 0.05, a_in + 0.05 + blade_t, b_in + 0.05 + blade_t,
                       P.HINGE_PHI - P.WAIST_ARC * 0.5, P.HINGE_PHI + P.WAIST_ARC * 0.5,
                       P.Z_HINGE0, P.Z_HINGE1)
    relief = band_prism(a_in + 0.05 + blade_t - 0.03, b_in + 0.05 + blade_t - 0.03,
                        a_out + 1.0, b_out + 1.0,
                        phi_sh_end, phi_ar_start, -0.5, h_ring + 0.5)
    cov_shell, cov_arm = ang_cover(phi_shell_start, phi_sh_end), ang_cover(phi_ar_start, phi_arm_end + 360.0)
    gap_deg = 360.0 - ang_measure(cov_shell) - ang_measure(cov_arm) - hinge_window
    meta = dict(phi_arm_end=phi_arm_end, phi_shell_start=phi_shell_start,
                phi_sh_end=phi_sh_end, phi_ar_start=phi_ar_start,
                overlap_deg=ang_overlap(cov_shell, cov_arm),
                slit_gap_mm=gap_deg * math.pi / 180.0 * a_out)
    return shell, arm, blade, relief, meta


# ------------------------------------------- PHỤ KIỆN THÂN: neo gân + cảm biến ---
ANCHOR = dict(phi0=86.0, phi1=112.0, z0=0.0, z1=4.6, rise=1.7,
              slot_w=3.0, slot_d=2.6, screw_r=1.6)


def body_features(h_ring=None):
    """→ (anchor_boss, sensor_recess, anchor_hole) — giống Ý tưởng 1."""
    h_ring = P.H_RING if h_ring is None else h_ring
    a_in, b_in = P.a_in(), P.b_in()
    a_out, b_out = P.a_out(), P.b_out()
    boss_pts = []
    for dphi, rr in ((0.0, 1.0), (0.22, 1.0), (0.35, 0.35), (0.65, 0.35), (0.78, 1.0), (1.0, 1.0)):
        phi = ANCHOR['phi0'] + (ANCHOR['phi1'] - ANCHOR['phi0']) * dphi
        r = G.ell_r(a_out, b_out, phi) + ANCHOR['rise'] * rr
        boss_pts.append(polar(r, phi))
    boss_pts += [polar(G.ell_r(a_out, b_out, ANCHOR['phi1']), ANCHOR['phi1']),
                 polar(G.ell_r(a_out, b_out, ANCHOR['phi0']), ANCHOR['phi0'])]
    boss = prism(boss_pts, ANCHOR['z0'], ANCHOR['z1'])
    recess = band_prism(a_in - P.SENSOR_T, b_in - P.SENSOR_T, a_in + 0.02, b_in + 0.02,
                        P.SENSOR_PHI0, P.SENSOR_PHI1, -0.4, h_ring + 0.4)
    hole = Part.makeCylinder(ANCHOR['screw_r'], 40.0,
                             App.Vector(0.0, -20.0, (ANCHOR['z1'] - 0.6) / 2.0),
                             App.Vector(0.0, 1.0, 0.0))
    return boss, recess, hole


# --------------------------------------------------------- RÃNH + ĐỆM TPU ---
def pad_cutters(pad_phi, pad_arc, pad_slot_d, pad_lip, h_ring=None):
    h_ring = P.H_RING if h_ring is None else h_ring
    a_in, b_in = P.a_in(), P.b_in()
    out = []
    z_mid = h_ring / 2.0
    z_a, z_b = z_mid - P.H_PAD / 2.0, z_mid + P.H_PAD / 2.0
    for pp in pad_phi:
        p0, p1 = pp - pad_arc / 2.0, pp + pad_arc / 2.0
        out.append(band_prism(a_in - 0.4, b_in - 0.4, a_in + pad_slot_d, b_in + pad_slot_d,
                              p0, p1, -0.2, z_a, n=48))
        out.append(band_prism(a_in - 0.4, b_in - 0.4, a_in + pad_slot_d, b_in + pad_slot_d,
                              p0, p1, z_b, h_ring + 0.2, n=48))
        out.append(band_prism(a_in - 0.4, b_in - 0.4,
                              a_in + pad_slot_d - pad_lip, b_in + pad_slot_d - pad_lip,
                              p0, p1, z_a, z_b, n=48))
    return out


def make_pads(pad_phi, pad_arc, pad_slot_d, pad_t, h_ring=None):
    h_ring = P.H_RING if h_ring is None else h_ring
    a_in, b_in = P.a_in(), P.b_in()
    pads = []
    for i, pp in enumerate(pad_phi):
        r_in = G.ell_r(a_in, b_in, pp)
        z_mid = h_ring / 2.0
        h_half = P.H_PAD / 2.0
        prof = [(-0.01, r_in + pad_slot_d - 0.25), (h_ring + 0.01, r_in + pad_slot_d - 0.25),
                (h_ring + 0.01, r_in - pad_t + 0.02),
                (z_mid + h_half + 0.6, r_in - pad_t + 0.02),
                (z_mid + h_half + 0.6, r_in - pad_t - 0.6),
                (z_mid - h_half - 0.6, r_in - pad_t - 0.6),
                (z_mid - h_half - 0.6, r_in - pad_t + 0.02),
                (-0.01, r_in - pad_t + 0.02)]
        p = rad_prism(prof, pp)
        keep = band_prism(r_in - pad_t - 1.0, r_in - pad_t - 1.0,
                          r_in + pad_slot_d + 1.0, r_in + pad_slot_d + 1.0,
                          pp - pad_arc / 2.0, pp + pad_arc / 2.0, -1.0, h_ring + 1.0, n=60)
        pads.append((i, p.common(keep)))
    return pads


# --------------------------------------------------------------- thống kê ---
def stats(shape, pads, ref_lat=None):
    a_knuck = P.A_KNUCK if ref_lat is None else ref_lat
    bb = shape.BoundBox
    out = dict(x_max=max(abs(bb.XMin), abs(bb.XMax)),
               dx_lat=max(abs(bb.XMin), abs(bb.XMax)) - a_knuck,
               z_len=bb.ZMax - bb.ZMin, n_solids=len(shape.Solids),
               ok=bool(shape.isValid()),
               vol_petg_cm3=shape.Volume / 1000.0,
               mass_petg=shape.Volume / 1000.0 * P.RHO_PETG * 1000.0,
               vol_tpu_cm3=sum(p.Volume for _, p in pads) / 1000.0)
    out["mass_tpu"] = out["vol_tpu_cm3"] * P.RHO_TPU * 1000.0
    return out
