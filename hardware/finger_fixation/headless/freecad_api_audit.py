# -*- coding: utf-8 -*-
"""
freecad_api_audit.py — RÀ SOÁT API: bảo đảm 3 script build CHỈ dùng API FreeCAD thật
================================================================================
Vì sao có script này: bộ kiểm headless (headless/freecad_compat.py) giả lập API
FreeCAD trên nhân OCCT. Nếu script build lỡ dùng một hàm CHỈ CÓ ở lớp giả lập
(ví dụ `cutMany`) thì bản headless vẫn PASS nhưng khi chạy trong FreeCAD thật sẽ
lỗi AttributeError. Script này rà mã nguồn để bắt đúng loại lỗi đó.

HAI CHẾ ĐỘ
----------
1) Ngoài FreeCAD:      python headless/freecad_api_audit.py
   → đối chiếu mọi tên API dùng trong mã nguồn với DANH SÁCH TRẮNG (API FreeCAD
     0.20+/1.0) + DANH SÁCH ĐEN (tên chỉ có ở lớp giả lập headless).
2) TRONG FreeCAD:      freecadcmd headless/freecad_api_audit.py
   → kiểm tra THẬT bằng hasattr() trên Part / App / Mesh / Part.Shape của chính
     bản FreeCAD đang chạy (bằng chứng mạnh nhất).

Thêm --write để ghi reports/freecad_api_audit.txt
"""
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)

SOURCES = ["build_idea1_toggle_clasp.py", "build_idea2_ratchet_cinch.py",
           "build_idea3_wrap_band.py", "ring_common.py"]

# ---------------------------------------------------------------- danh sách ---
# API cấp MODULE của FreeCAD (wiki.freecad.org: Part API / Mesh API / App API).
WHITELIST_MODULE = {
    "App.Vector", "App.newDocument", "App.Version", "App.GuiUp", "App.ActiveDocument",
    "Part.makePolygon", "Part.Face", "Part.makeCylinder", "Part.makeLine", "Part.Wire",
    "Part.show", "Part.Shape", "Part.makeBox",
    "Mesh.export", "Mesh.show",
}

# Phương thức/thuộc tính của Part.Shape (TopoShape) — đều có trong FreeCAD 0.20+.
WHITELIST_SHAPE = {
    "cut", "fuse", "common", "multiFuse", "extrude", "removeSplitter", "translate",
    "rotate", "isValid", "isNull", "isClosed", "Volume", "Area", "BoundBox",
    "Solids", "Faces", "Edges", "Wires", "Shells", "Vertexes", "Shape",
    "exportStl", "tessellate", "optimalBoundingBox",
}

# Tên CHỈ có ở lớp giả lập headless — không được xuất hiện trong script build.
BLACKLIST = ["cutMany", "_binop", "_binop_many", "freecad_compat"]

# Hàm sinh/đổi khối CAD của bộ mã này (để nhận diện biến nào là "biến CAD").
CAD_PRODUCERS = re.compile(
    r"(\bPart\.|\bRC\.(prism|band_prism|local_prism|rad_prism|cyl|union_all|"
    r"fuse_chain|common|make_pads|shell_arm_hinge|body_features|pad_cutters)\b|"
    r"\bG\.(band|spiral_ribbon|ratchet_rack)\b|\b(prism|band_prism|local_prism|rad_prism|"
    r"cyl|union_all|fuse_chain|make_pads|w_poly|taper_wedge)\s*\(|"
    r"\.(cut|fuse|common|extrude|removeSplitter)\s*\()")


def _strip_comments_strings(src):
    src = re.sub(r'"""(?:.|\n)*?"""', "", src)
    src = re.sub(r"'''(?:.|\n)*?'''", "", src)
    src = re.sub(r"#.*", "", src)
    return src


# ------------------------------------------------------- bẫy CÚ PHÁP (đã gặp) ---
# Mỗi mục: (regex, mô tả, mức độ) — mức "FAIL" nghĩa là FreeCAD thật sẽ lỗi/ sai.
TRAPS = [
    (r"\.(cut|fuse|common)\s*\(\s*\[",
     "truyền DANH SÁCH cho cut/fuse/common — FreeCAD chỉ nhận 1 đối tượng "
     "(TopoShapePyImp.cpp: PyArg_ParseTuple \"O!\") ⇒ TypeError; dùng cut_all()/fuse_chain()",
     "FAIL"),
    (r"makePolygon\s*\([^()]*\bclosed\s*=",
     "makePolygon(..., closed=True) — makePolygon là varargs-method, KHÔNG nhận keyword "
     "⇒ TypeError; phải truyền tham số thứ hai THEO VỊ TRÍ: makePolygon(pts, True)",
     "FAIL"),
    (r"\.multiFuse\s*\(",
     "multiFuse() = GENERAL FUSE trong FreeCAD ⇒ có thể trả về compound NHIỀU mảnh rời; "
     "không dùng cho chi tiết cần '1 khối liền' — dùng fuse_chain()",
     "FAIL"),
    (r"\bcutMany\s*\(",
     "cutMany() KHÔNG tồn tại trong FreeCAD (chỉ là hàm của lớp mô phỏng cũ)",
     "FAIL"),
    (r"\bsys\.exit\s*\(",
     "sys.exit() trong script build: trong FreeCAD GUI sẽ ném SystemExit và ĐÓNG app "
     "⇒ bọc bằng FF_NO_SYS_EXIT (xem ring_common.exit_code)",
     "WARN"),
]


def check_traps(src, name):
    """→ (fails, warns) khi rà các bẫy cú pháp đã biết trên mã nguồn (đã bỏ chú thích)."""
    fails, warns = [], []
    for pat, msg, level in TRAPS:
        if re.search(pat, src):
            (fails if level == "FAIL" else warns).append("%s: %s" % (name, msg))
    return fails, warns


def scan(path):
    src = _strip_comments_strings(open(path, "r", encoding="utf-8").read())
    mods = set("%s.%s" % m for m in re.findall(r"\b(App|Part|Mesh)\.([A-Za-z_]\w*)", src))
    black = [b for b in BLACKLIST if re.search(r"\b%s\b" % re.escape(b), src)]

    # dataflow-lite: biến nào được gán từ một "CAD producer" ⇒ là biến CAD
    cad_vars = set()
    for line in src.splitlines():
        if "=" not in line or not CAD_PRODUCERS.search(line.split("=", 1)[1]):
            continue
        lhs = line.split("=", 1)[0].strip()
        for name in re.split(r"[,\s]+", lhs):
            if re.fullmatch(r"[A-Za-z_]\w*", name) and name not in ("import", "from"):
                cad_vars.add(name)
    cad_vars -= {"App", "Part", "Mesh", "RC", "G", "P", "TS", "np", "os", "sys", "math"}

    used_methods = {}
    for line in src.splitlines():
        for recv, meth in re.findall(r"\b([A-Za-z_]\w*)\s*\.\s*([A-Za-z_]\w*)\s*\(", line):
            if recv in cad_vars:
                used_methods.setdefault(meth, set()).add(recv)
    return mods, used_methods, black


def main():
    write = "--write" in sys.argv
    out_lines = []
    def emit(s=""):
        print(s)
        out_lines.append(s)

    emit("=" * 78)
    emit("RÀ SOÁT API FREECAD — script build Ý tưởng 1/2/3 + ring_common.py")
    emit("=" * 78)

    inside = False
    probe = None
    try:
        import FreeCAD as App
        import Part
        import Mesh  # noqa: F401
        inside = True
        ver = App.Version() if hasattr(App, "Version") else ["?"]
        emit("  CHẾ ĐỘ 2 — TRONG FreeCAD %s: kiểm tra bằng hasattr()"
             % ".".join(str(x) for x in ver[:3]))
        probe = Part.makeBox(1, 1, 1) if hasattr(Part, "makeBox") else Part.Shape()
    except Exception:
        emit("  CHẾ ĐỘ 1 — ngoài FreeCAD: đối chiếu danh sách trắng API (0.20+/1.0)")

    fails = []
    for name in SOURCES:
        path = os.path.join(_ROOT, name)
        if not os.path.isfile(path):
            fails.append("%s: KHÔNG tìm thấy file" % name)
            continue
        mods, methods, black = scan(path)
        bad_mod = sorted(m for m in mods if m not in WHITELIST_MODULE)
        bad_meth = sorted(m for m in methods if m not in WHITELIST_SHAPE)
        trap_fails, trap_warns = check_traps(
            _strip_comments_strings(open(path, "r", encoding="utf-8").read()), name)
        fails += trap_fails
        emit("")
        emit("  %-32s API module: %-42s" % (name, ", ".join(sorted(mods))))
        if methods:
            emit("  %-32s phương thức trên biến CAD: %s"
                 % ("", ", ".join(sorted(methods))))
        emit("  %-32s bẫy cú pháp FreeCAD: %s"
             % ("", "KHÔNG có" if not (trap_fails + trap_warns) else
                "; ".join(t.split(": ", 1)[1] for t in trap_fails + trap_warns)))
        if trap_warns:
            emit("  %-32s (cảnh báo: %s)" % ("", len(trap_warns)))
        if bad_mod or bad_meth:
            fails.append("%s: tên ngoài danh sách trắng: %s"
                         % (name, ", ".join(bad_mod + bad_meth)))
        if black:
            fails.append("%s: dùng tên riêng của lớp giả lập headless: %s"
                         % (name, ", ".join(black)))
        if inside:
            miss = [m for m in sorted(mods) if not _module_has(m)]
            miss += [m for m in sorted(methods) if not hasattr(probe, m)]
            if miss:
                fails.append("%s: FreeCAD KHÔNG có: %s" % (name, ", ".join(miss)))
                emit("  %-32s ✘ FreeCAD KHÔNG có: %s" % ("", ", ".join(miss)))
            else:
                emit("  %-32s ✔ hasattr() OK trên bản FreeCAD đang chạy" % "")
        if bad_mod or bad_meth or black:
            emit("  %-32s ✘ có tên không hợp lệ (xem kết luận)" % "")

    emit("")
    emit("-" * 78)
    if fails:
        emit("KẾT LUẬN: %d VẤN ĐỀ" % len(fails))
        for f in fails:
            emit("   - %s" % f)
    else:
        emit("KẾT LUẬN: API HỢP LỆ — script build chỉ dùng API FreeCAD chuẩn.")
        emit("   (headless vẫn dùng được vì freecad_compat.py phủ đúng các API này)")
    emit("=" * 78)

    if write:
        out = os.path.join(_ROOT, "reports", "freecad_api_audit.txt")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as fh:
            fh.write("\n".join(out_lines) + "\n")
        print("   → đã ghi %s" % out)
    return 2 if fails else 0


def _module_has(dotted):
    mod, _, attr = dotted.partition(".")
    py = {"App": "FreeCAD", "Part": "Part", "Mesh": "Mesh"}.get(mod)
    m = sys.modules.get(py) or __import__(py)
    return hasattr(m, attr)


if __name__ == "__main__":
    sys.exit(main())
