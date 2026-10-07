# -*- coding: utf-8 -*-
"""
fcgeom.py — Thư viện hình học thuần Python (không phụ thuộc CAD) cho bộ cố định đốt gần P1.

Mọi hàm trả về danh sách điểm 2D [(x, y), ...] đã được "lấy mẫu dày" (dense sampling).
Triết lý thiết kế: KHÔNG dùng fillet/booleans cong của CAD kernel ⇒ script chạy được
trên mọi bản FreeCAD mà không gặp lỗi tangency/fillet (nguồn lỗi phổ biến nhất).
Mọi chi tiết đều là "prism" dựng từ đa giác phẳng + extrude.

Quy ước trục (khớp với docs/04_Hardware_Architecture.md):
    X = ngang (sang hai bên sườn ngón, +X = phía ngón giữa)
    Y = mu–lòng (+Y = mặt mu / dorsal)
    Z = trục ngón (+Z = về phía đầu ngón / distal)
    Góc phi (phi) đo CCW từ +X:  0 deg = sườn phải, 90 = mu, 180 = sườn trái, 270 = lòng.
"""
import math

TAU = 2.0 * math.pi


# ----------------------------------------------------------------------------- helpers
def deg(d):
    return float(d) * math.pi / 180.0


def ell_pt(a, b, phi_deg):
    """Điểm trên ellipse tham số (a, b) tại góc tham số phi (độ)."""
    t = deg(phi_deg)
    return (a * math.cos(t), b * math.sin(t))


def ell_r(a, b, phi_deg):
    """Bán kính (khoảng cách tới gốc) của ellipse tại góc tham số phi."""
    x, y = ell_pt(a, b, phi_deg)
    return math.hypot(x, y)


def arc(a, b, phi0, phi1, n=140, start=True):
    """Cung ellipse từ phi0 -> phi1, trả về n+1 điểm (kể cả 2 đầu)."""
    if n < 2:
        n = 2
    pts = []
    for i in range(n + 1):
        f = i / float(n) if start else (i + 1) / float(n + 1)
        pts.append(ell_pt(a, b, phi0 + (phi1 - phi0) * f))
    return pts


def band(a_in, b_in, a_out, b_out, phi0, phi1, n=140):
    """Vành khuyên ellipse (sector) từ phi0 -> phi1: cung ngoài + cung trong (ngược chiều).

    Chiều dày thành xấp xỉ (a_out - a_in) ở sườn và (b_out - b_in) ở mu/lòng.
    """
    outer = arc(a_out, b_out, phi0, phi1, n)
    inner = arc(a_in, b_in, phi1, phi0, n)
    return outer + inner


def tf(pts, origin=(0.0, 0.0), rot_deg=0.0):
    """Quay (CCW, độ) rồi tịnh tiến một danh sách điểm 2D."""
    c, s = math.cos(deg(rot_deg)), math.sin(deg(rot_deg))
    ox, oy = origin
    out = []
    for (x, y) in pts:
        out.append((ox + c * x - s * y, oy + s * x + c * y))
    return out


def local_frame(phi_deg, r_ref):
    """Trả về (origin, rot_deg) của hệ toạ độ địa phương tại góc phi trên vành bán kính r_ref.

    Trong hệ địa phương: u = tiếp tuyến (chiều +phi), v = hướng kính ra ngoài.
    Gốc đặt tại điểm (r_ref, phi). Dùng kèm tf().
    """
    t = deg(phi_deg)
    origin = (r_ref * math.cos(t), r_ref * math.sin(t))
    return origin, phi_deg - 90.0  # trục u trùng chiều +phi


def rect(w, h, cu=0.0, cv=0.0, rot=0.0):
    """Chữ nhật tâm (cu, cv), kích thước w (u) x h (v), quay rot độ."""
    p = [(cu - w / 2.0, cv - h / 2.0), (cu + w / 2.0, cv - h / 2.0),
         (cu + w / 2.0, cv + h / 2.0), (cu - w / 2.0, cv + h / 2.0)]
    if rot:
        return tf(p, (cu, cv), rot)  # tf quay quanh gốc, nên dịch tạm — xử lý bên dưới
    return p


def rect_at(w, h, cu=0.0, cv=0.0):
    """Chữ nhật tâm (cu, cv) — không quay (đơn giản, ít lỗi)."""
    return [(cu - w / 2.0, cv - h / 2.0), (cu + w / 2.0, cv - h / 2.0),
            (cu + w / 2.0, cv + h / 2.0), (cu - w / 2.0, cv + h / 2.0)]


def trapezoid(w_bot, w_top, h, cu=0.0, cv=0.0):
    """Hình thang đáy dưới w_bot, đáy trên w_top, cao h, tâm đáy tại (cu, cv)."""
    return [(cu - w_bot / 2.0, cv), (cu + w_bot / 2.0, cv),
            (cu + w_top / 2.0, cv + h), (cu - w_top / 2.0, cv + h)]


def waisted_blade(length, t_end, t_mid, cu=0.0, cv=0.0, n=24, along='u'):
    """Lá đàn hồi ("living hinge") có eo thắt ở giữa: dày t_mid ở giữa, t_end ở 2 đầu.

    Dùng cho mọi khớp mềm: biên dạng cosine để giảm tập trung ứng suất.
    along='u': lá chạy dọc trục u (dài `length`), chiều dày theo v (v = ±t/2).
    """
    pts_top, pts_bot = [], []
    for i in range(n + 1):
        u = -length / 2.0 + length * i / float(n)
        f = 2.0 * abs(u) / length            # 0 ở giữa, 1 ở đầu
        t = t_mid + (t_end - t_mid) * (f ** 2)
        pts_top.append((cu + u, cv + t / 2.0))
        pts_bot.append((cu + u, cv - t / 2.0))
    pts = pts_top + pts_bot[::-1]
    if along == 'u':
        return pts
    return [(y, x) for (x, y) in pts]        # lá chạy dọc v


def spiral_ribbon(r_start, r_end, phi_start, phi_end_extra, thickness, n=220):
    """Băng xoắn ốc phẳng (Archimedes) — dùng cho Ý tưởng 3 (băng quấn tự siết).

    r(phi) = r_start + (r_end - r_start) * phi / phi_total ;  phi in [0, phi_total]
    Trả về đa giác: cung ngoài (r + t/2) rồi cung trong (r - t/2) ngược lại.
    """
    pts_out, pts_in = [], []
    for i in range(n + 1):
        phi = phi_start + (deg(phi_end_extra)) * i / float(n)
        r = r_start + (r_end - r_start) * i / float(n)
        pts_out.append(((r + thickness / 2.0) * math.cos(phi), (r + thickness / 2.0) * math.sin(phi)))
        pts_in.append(((r - thickness / 2.0) * math.cos(phi), (r - thickness / 2.0) * math.sin(phi)))
    return pts_out + pts_in[::-1]


def ratchet_rack(phi0, phi1, r_base, pitch_deg, tooth_h, n_teeth, ramp_frac=0.72):
    """Thanh răng cưa (prism) trên cung bán kính r_base: răng nhọn một chiều.

    ramp_frac = 0 -> 1 : phần chiều dài răng dành cho mặt dốc (ramp);
    phần còn lại là "sườn đứng" (shoulder) — bề mặt chịu lực form-closed.
    """
    pts = []
    step = (phi1 - phi0) / float(n_teeth)
    for k in range(n_teeth):
        a0 = phi0 + k * step
        a_ramp = a0 + step * ramp_frac
        a1 = a0 + step
        pts.append(((r_base) * math.cos(deg(a0)), (r_base) * math.sin(deg(a0))))
        pts.append(((r_base + tooth_h) * math.cos(deg(a_ramp)), (r_base + tooth_h) * math.sin(deg(a_ramp))))
        pts.append(((r_base) * math.cos(deg(a1)), (r_base) * math.sin(deg(a1))))
    return pts


def poly_bbox(pts):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)


def poly_area(pts):
    """Diện tích đa giác (shoelace) — dùng để kiểm tra định hướng/độ lớn."""
    s = 0.0
    n = len(pts)
    for i in range(n):
        x0, y0 = pts[i]
        x1, y1 = pts[(i + 1) % n]
        s += x0 * y1 - x1 * y0
    return s / 2.0
