# -*- coding: utf-8 -*-
"""
run_in_freecad.py — CHẠY CẢ 3 BỘ SINH STL NGAY TRONG FREECAD
================================================================================
Đây là "nút bấm duy nhất" để tạo 5 STL của Ý tưởng 1 (bộ ưu tiên: Cơ cấu đòn bẩy
kẹp bên sườn — Side Toggle Clasp) và 3 + 3 STL của Ý tưởng 2, 3.

CÁCH DÙNG
---------
A) FreeCAD GUI (bản có cửa sổ):
     View → Panels → Python console, rồi dán 1 dòng (thay <ĐƯỜNG_DẪN>):

         exec(open(r"<ĐƯỜNG_DẪN>/hardware/finger_fixation/run_in_freecad.py").read())

     hoặc: Macro → Macros… → Create → dán nội dung file này → Execute.

B) Dòng lệnh (không cần GUI — dùng cho CI/máy chủ có FreeCAD):

         freecadcmd hardware/finger_fixation/run_in_freecad.py

KẾT QUẢ
-------
   hardware/finger_fixation/stl/idea1/{Ring_PETG, Pad1..4_TPU}.stl
   hardware/finger_fixation/stl/idea2/{Ring_PETG, Pad1..4_TPU}.stl
   hardware/finger_fixation/stl/idea3/{Ring_PETG, Band_TPU, Wedge_PETG}.stl
   + bảng PASS/FAIL y như headless/run_verify.py

GHI CHÚ KỸ THUẬT
----------------
* Script ĐẶT FF_NO_SYS_EXIT=1 trước khi exec các script build: trong FreeCAD GUI,
  sys.exit() ném SystemExit và có thể ĐÓNG ứng dụng — biến này chặn điều đó, đồng
  thời KHÔNG thay đổi kết quả hình học (chỉ bỏ lệnh thoát).
* Ba script build KHÔNG phụ thuộc lớp tương thích headless: chúng chỉ dùng API
  FreeCAD chuẩn (App.Vector, Part.makePolygon/Face/makeCylinder, Shape.cut/fuse/
  common/extrude/removeSplitter, Shape.Volume/BoundBox/Solids/isValid, Mesh.export).
  Bộ rà soát API: python headless/freecad_api_audit.py (chạy được cả hai chế độ).
"""
import io
import os
import re
import sys
import traceback

_HERE = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else None
if _HERE is None:                       # dán trực tiếp vào console FreeCAD
    _cwd = os.getcwd()
    for _d in (_cwd, os.path.join(_cwd, "hardware", "finger_fixation")):
        if os.path.isfile(os.path.join(_d, "build_idea1_toggle_clasp.py")):
            _HERE = _d
            break
if _HERE is None or not os.path.isdir(_HERE):
    raise RuntimeError("Không xác định được thư mục hardware/finger_fixation — "
                       "hãy chạy: freecadcmd <đường_dẫn>/run_in_freecad.py")

SCRIPTS = [("Ý TƯỞNG 1 — Side Toggle Clasp (đòn bẩy quá tâm)", "build_idea1_toggle_clasp.py"),
           ("Ý TƯỞNG 2 — Ratchet Cinch (cóc một chiều)",           "build_idea2_ratchet_cinch.py"),
           ("Ý TƯỞNG 3 — Wrap Band + chêm tự cưỡng hoá",           "build_idea3_wrap_band.py")]

RE_PASS = re.compile(r"\[PASS\]")
RE_FAIL = re.compile(r"\[FAIL\]")

os.environ["FF_NO_SYS_EXIT"] = "1"      # xem GHI CHÚ KỸ THUẬT ở đầu file


class _Tee(io.TextIOBase):
    """Vừa in ra màn hình vừa gom vào buffer để đếm [PASS]/[FAIL]."""

    def __init__(self, real):
        self._real = real
        self.buf = io.StringIO()

    def write(self, s):
        self.buf.write(s)
        try:
            self._real.write(s)
        except Exception:
            pass
        return len(s)

    def flush(self):
        try:
            self._real.flush()
        except Exception:
            pass


def _run(path):
    src = open(path, "r", encoding="utf-8").read()
    g = {"__name__": "__main__", "__file__": path}
    tee = _Tee(sys.stdout)
    old = sys.stdout
    sys.stdout = tee
    try:
        exec(compile(src, path, "exec"), g)
        code = 0
    except SystemExit as e:
        code = int(e.code or 0)
    except Exception:
        code = 1
        traceback.print_exc()
    finally:
        sys.stdout = old
    txt = tee.buf.getvalue()
    return code, len(RE_PASS.findall(txt)), len(RE_FAIL.findall(txt)), txt


def main():
    print("=" * 78)
    print("CHẠY TRONG FREECAD — BỘ SINH STL CỐ ĐỊNH ĐỐT GẦN P1 (Ø20–24 mm)")
    try:
        import FreeCAD as App
        ver = App.Version() if hasattr(App, "Version") else ["?"]
        print("   FreeCAD: %s | GUI đang bật: %s"
              % (".".join(str(x) for x in ver[:3]), bool(getattr(App, "GuiUp", 0))))
    except Exception as e:                       # pragma: no cover
        print("   Không import được FreeCAD: %s" % e)
    print("   Thư mục làm việc: %s" % _HERE)
    print("=" * 78)

    rows = []
    hard_fail = False
    for title, name in SCRIPTS:
        path = os.path.join(_HERE, name)
        print("\n" + "#" * 78)
        print("# %s\n# %s" % (title, name))
        print("#" * 78)
        if not os.path.isfile(path):
            print("   [FAIL] thiếu file: %s" % path)
            rows.append((name, "THIẾU FILE", 0, 0, 1))
            hard_fail = True
            continue
        code, n_pass, n_fail, txt = _run(path)
        ket = "CÓ MỤC FAIL" if n_fail else ("PASS" if code == 0 else "LỖI")
        if "KẾT LUẬN: TẤT CẢ MỤC KIỂM TRA PASS" in txt and n_fail == 0:
            ket = "PASS"
        rows.append((name, ket, n_pass, n_fail, code))
        if ket != "PASS":
            hard_fail = True

    print("\n" + "=" * 78)
    print("BẢNG TỔNG HỢP — CHẠY TRONG FREECAD")
    print("=" * 78)
    print("  %-34s %-10s %5s %5s %5s" % ("file", "kết quả", "PASS", "FAIL", "mã"))
    for name, ket, p, f, c in rows:
        print("  %-34s %-10s %5d %5d %5d" % (name, ket, p, f, c))
    n_ok = sum(1 for r in rows if r[1] == "PASS")
    print("-" * 78)
    print("  %d/%d script PASS | tổng %d mục PASS, %d mục FAIL"
          % (n_ok, len(rows), sum(r[2] for r in rows), sum(r[3] for r in rows)))
    print("  STL: %s" % os.path.join(_HERE, "stl", "{idea1,idea2,idea3}"))
    print("=" * 78)

    if not bool(getattr(sys.modules.get("FreeCAD"), "GuiUp", 0)) and hard_fail:
        sys.exit(2)      # chỉ thoát bằng mã lỗi khi KHÔNG ở GUI (freecadcmd/CI)


main()
