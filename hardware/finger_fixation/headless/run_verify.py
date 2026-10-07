# -*- coding: utf-8 -*-
"""
run_verify.py — Chạy headless (không cần cài FreeCAD) TẤT CẢ script build_*.py
thông qua lớp tương thích OCCT để:
  1) phát hiện lỗi hình học (solid không hợp lệ, boolean thất bại, đa giác tự cắt);
  2) kiểm tra các ràng buộc cứng của brief (ΔX ≤ 2 mm, chiều dài trục 12–16 mm);
  3) xuất STL + in bảng tổng hợp cho báo cáo.

ĐIỂM QUAN TRỌNG: bản cũ trả về "OK" chỉ vì script con chạy hết (exit 0) — nó KHÔNG
đọc các dòng [FAIL] do script con in ra, và `sys.exit(2)` của script con (SystemExit)
làm chết cả runner. Bản này:
  * bắt SystemExit(code) → coi code != 0 là FAIL;
  * chặn (tee) stdout của script con để ĐẾM [PASS]/[FAIL] và tìm dòng "KẾT LUẬN";
  * tổng hợp thành bảng + mã thoát đúng.

Dùng:
    python headless/run_verify.py                # tất cả build_*.py
    python headless/run_verify.py build_idea1_toggle_clasp.py
"""
import io
import os
import re
import runpy
import sys
import traceback

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
sys.path.insert(0, _HERE)
sys.path.insert(0, _ROOT)

import freecad_compat  # noqa: E402

freecad_compat.install()   # phải gọi TRƯỚC khi exec script build

DEFAULT = ["build_idea1_toggle_clasp.py",
           "build_idea2_ratchet_cinch.py",
           "build_idea3_wrap_band.py"]

RE_PASS = re.compile(r"\[PASS\]")
RE_FAIL = re.compile(r"\[FAIL\]")


class Tee(object):
    """Ghi ra cả stdout thật và buffer để đếm PASS/FAIL."""

    def __init__(self, stream):
        self.stream = stream
        self.buf = io.StringIO()

    def write(self, s):
        self.stream.write(s)
        self.buf.write(s)
        return len(s)

    def flush(self):
        self.stream.flush()

    def isatty(self):
        return False

    def getvalue(self):
        return self.buf.getvalue()


def run_one(fname):
    """→ dict(status, n_pass, n_fail, exit_code, stl)."""
    path = os.path.join(_ROOT, fname)
    print("\n" + "#" * 78)
    print("# %s" % fname)
    print("#" * 78)
    if not os.path.exists(path):
        print("!! CHƯA CÓ FILE — bỏ qua (chưa hoàn thành deliverable)")
        return dict(name=fname, status="MISSING", n_pass=0, n_fail=0,
                    code=None, stl=0)

    tee, saved = Tee(sys.stdout), sys.stdout
    sys.stdout = tee
    code, crashed = 0, False
    try:
        runpy.run_path(path, run_name="__main__")
    except SystemExit as e:
        code = e.code if isinstance(e.code, int) else (0 if e.code is None else 1)
    except BaseException:
        traceback.print_exc()
        crashed = True
        code = 1
    finally:
        sys.stdout = saved

    out = tee.getvalue()
    n_pass, n_fail = len(RE_PASS.findall(out)), len(RE_FAIL.findall(out))
    _stl_dir = os.path.join(_ROOT, "stl")
    n_stl_out = len([f for _dp, _dn, _fn in os.walk(_stl_dir) for f in _fn
                     if f.lower().endswith(".stl")]) if os.path.isdir(_stl_dir) else 0
    status = "FAIL" if (crashed or n_fail or code) else "PASS"
    if "KẾT LUẬN: TẤT CẢ MỤC KIỂM TRA PASS" in out and not n_fail and not code:
        status = "PASS"
    return dict(name=fname, status=status, n_pass=n_pass, n_fail=n_fail,
                code=code, stl=n_stl_out, crashed=crashed)


def main(argv):
    files = argv[1:] or DEFAULT
    rows = [run_one(f) for f in files]
    print("\n" + "=" * 78)
    print("BẢNG TỔNG HỢP HEADLESS VERIFY (giả lập FreeCAD-API trên nhân OCCT)")
    print("=" * 78)
    print("  %-34s %-8s %5s %5s %5s" % ("file", "kết quả", "PASS", "FAIL", "mã"))
    for r in rows:
        print("  %-34s %-8s %5d %5d %5s"
              % (r["name"], r["status"], r["n_pass"], r["n_fail"],
                 r["code"] if r["code"] is not None else "-"))
    n_ok = sum(1 for r in rows if r["status"] == "PASS")
    n_missing = sum(1 for r in rows if r["status"] == "MISSING")
    print("-" * 78)
    print("  %d/%d script PASS%s" % (n_ok, len(rows),
                                     "" if not n_missing else
                                     "   (%d file chưa tồn tại)" % n_missing))
    print("   Tổng STL trong hardware/finger_fixation/stl: %d"
          % (rows[-1]["stl"] if rows else 0))
    print("=" * 78)
    return 0 if (n_ok == len(rows)) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
