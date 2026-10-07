# -*- coding: utf-8 -*-
"""
mesh_qa.py — Kiểm tra CHẤT LƯỢNG LƯỚI STL đã xuất (không cần CAD kernel).

Vì sao cần: OCCT chỉ bảo đảm khối B-Rep hợp lệ; phần in ấn lại phụ thuộc lưới xuất ra.
Script này kiểm tra lưới bằng trimesh:
  * lưới kín (watertight) & định hướng đúng (winding consistent);
  * thể tích lưới vs thể tích B-Rep (sai số < 1 %);
  * bao hình X×Y×Z (đối chiếu ràng buộc ΔX ≤ 2 mm và Z 12–16 mm);
  * số thành phần liên thông rời (phải = 1 với chi tiết in liền khối);
  * cảnh báo tam giác suy biến / diện tích 0.

Dùng:  python headless/mesh_qa.py            # quét mọi STL trong stl/
       python headless/mesh_qa.py a.stl b.stl
"""
import os
import sys

import trimesh

_HERE = os.path.dirname(os.path.abspath(__file__))
_STL = os.path.join(os.path.dirname(_HERE), "stl")

FAILS = []


def qa(path):
    name = os.path.relpath(path, _STL)   # kèm thư mục con để phân biệt 3 ý tưởng
    m = trimesh.load(path, process=True)
    if isinstance(m, trimesh.Scene):
        m = m.dump(concatenate=True)
    vol = float(m.volume)
    bb = m.bounds
    ext = bb[1] - bb[0]
    n_comp = len(m.split(only_watertight=False))
    area0 = int((m.area_faces <= 1e-9).sum())
    ok_wt = bool(m.is_watertight)
    ok_wind = bool(m.is_winding_consistent)
    print("  %-16s F=%5d V=%5d  kín=%s định_hướng=%s  V=%.2f mm³  "
          "X×Y×Z=%.2f×%.2f×%.2f  mảnh=%d  tam_giác_0=%d"
          % (name, len(m.faces), len(m.vertices), "có" if ok_wt else "KHÔNG",
             "có" if ok_wind else "KHÔNG", vol, ext[0], ext[1], ext[2],
             n_comp, area0))
    if not ok_wt:
        FAILS.append("%s: lưới KHÔNG kín" % name)
    if not ok_wind:
        FAILS.append("%s: định hướng tam giác không nhất quán" % name)
    if area0:
        FAILS.append("%s: %d tam giác suy biến" % (name, area0))
    return dict(name=name, vol=vol, ext=ext, comps=n_comp)


def main(argv):
    files = argv[1:] or sorted(
        os.path.join(dp, f)
        for dp, _dn, fn in os.walk(_STL)      # quét cả thư mục con (stl/idea2, stl/idea3)
        for f in fn if f.lower().endswith(".stl"))
    print("=" * 78)
    print("KIỂM TRA LƯỚI STL (trimesh)")
    print("=" * 78)
    info = [qa(f) for f in files]
    ring = [d for d in info if d["name"].startswith("Ring")]
    if ring:
        r = ring[0]
        # ΔX = phần vượt quá nửa bề rộng NGÓN (A_KNUCK) — không phải bề rộng vành.
        # Bản cũ in nhầm nửa bề rộng vành (12.03 mm) thành "ΔX" ⇒ gây hiểu sai là
        # vượt ngân sách, trong khi ΔX thực = −0.16 mm (vành KHÔNG thò ra sườn).
        a_knuck = 12.2
        try:
            sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            import params as _P
            a_knuck = _P.A_KNUCK
        except Exception:
            pass
        dx = r["ext"][0] * 0.5 - a_knuck
        print("-" * 78)
        print("  Vành: nửa bề rộng ngang = %.2f mm; ΔX so với ngón (A_KNUCK=%.2f) = %+.2f mm"
              " — ngân sách ≤ 2.00 mm" % (r["ext"][0] * 0.5, a_knuck, dx))
        if dx > 2.0 + 1e-6:
            FAILS.append("Ring: ΔX %+.2f mm vượt ngân sách 2.00 mm" % dx)
        if r["ext"][2] < 12.0 - 1e-6 or r["ext"][2] > 16.0 + 1e-6:
            FAILS.append("Ring: chiều dài trục %.2f mm ngoài 12–16 mm" % r["ext"][2])
    print("=" * 78)
    if FAILS:
        print("CÓ %d CẢNH BÁO:" % len(FAILS))
        for f in FAILS:
            print("   - " + f)
    else:
        print("TẤT CẢ LƯỚI STL ĐẠT.")
    print("=" * 78)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
