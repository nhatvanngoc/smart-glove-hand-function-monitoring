#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# bootstrap_env.sh — dựng môi trường Python "headless" để CHẠY KIỂM TỰ ĐỘNG
# (headless/run_verify.py, headless/mesh_qa.py) trên máy KHÔNG cài FreeCAD.
#
#   bash headless/bootstrap_env.sh          # → ~/.tooling/venv  + ~/.tooling/py
#   ~/.tooling/py headless/run_verify.py
#
# Vì sao cần gói OCP: lớp tương thích headless/freecad_compat.py giả lập API
# FreeCAD (Part/Mesh/App) TRÊN CHÍNH NHÂN OCCT — cùng nhân hình học mà FreeCAD
# dùng. Nhờ vậy kiểm tra tự động chạy được ở CI/máy chủ, còn script build vẫn
# chạy được nguyên vẹn trong FreeCAD thật (xem README_FREECAD.md).
#
# LƯU Ý libGL: gói OCP liên kết động tới libGL.so.1. Máy chủ headless (không X11)
# không có thư viện này ⇒ `import cadquery` báo "libGL.so.1: cannot open shared
# object file". Script tạo một libGL.so.1 STUB rỗng (chỉ để loader thoả mãn;
# phần dựng hình/boolean/tessellate KHÔNG dùng OpenGL) và bọc lệnh python để
# luôn đặt LD_LIBRARY_PATH đúng.
set -euo pipefail

ROOT="${FINGER_FIXATION_TOOLING:-$HOME/.tooling}"
VENV="$ROOT/venv"
STUB_DIR="$ROOT/libstub"
WRAP="$ROOT/py"

mkdir -p "$ROOT" "$STUB_DIR"

echo "== 1/4 Tạo venv tại $VENV"
python3 -m venv "$VENV"
"$VENV/bin/python" -m pip install -q --upgrade pip

echo "== 2/4 Cài cadquery 2.8.0 + trimesh + numpy (kênh PyPI)"
"$VENV/bin/python" -m pip install -q "cadquery==2.8.0" trimesh numpy

echo "== 3/4 Tạo libGL.so.1 stub (nếu máy chưa có libGL thật)"
if [ ! -e "$STUB_DIR/libGL.so.1" ]; then
    _c="$(mktemp /tmp/glstub_XXXX.c)"
    cat > "$_c" <<'EOF'
/* Stub rỗng cho libGL.so.1 — chỉ để trình nạp động thoả mãn khi import OCP. */
void _gl_stub_anchor(void) {}
EOF
    gcc -shared -fPIC -Wl,-soname,libGL.so.1 "$_c" -o "$STUB_DIR/libGL.so.1"
    rm -f "$_c"
fi
# Bổ sung dần các ký hiệu GL mà OCP tham chiếu TĨNH (undefined symbol khi import).
"$VENV/bin/python" - "$STUB_DIR" <<'PY'
import glob, os, subprocess, sys
stub_dir = sys.argv[1]
libs = glob.glob(os.path.join(os.path.dirname(stub_dir), "venv/lib/python*/site-packages/cadquery_ocp.libs/*.so*"))
libs += glob.glob(os.path.join(os.path.dirname(stub_dir), "venv/lib/python*/site-packages/OCP/*.so*"))
syms = set()
for l in libs:
    out = subprocess.run(["readelf", "--dyn-syms", "-W", l], capture_output=True, text=True).stdout
    for line in out.splitlines():
        p = line.split()
        if len(p) >= 8 and p[6] == "UND" and p[7].startswith(("gl", "glX", "egl", "wgl")):
            syms.add(p[7].split("@")[0])
if not syms:
    print("   (không thấy ký hiệu GL nào — bỏ qua)")
    raise SystemExit(0)
c = "/tmp/_glstub_full.c"
with open(c, "w") as f:
    f.write("/* Stub các entry point OpenGL mà OCP tham chiếu. */\n")
    for s in sorted(syms):
        f.write("void %s(void) {}\n" % s)
    f.write("void _gl_stub_anchor(void) {}\n")
subprocess.run(["gcc", "-shared", "-fPIC", "-Wl,-soname,libGL.so.1", c, "-o",
                os.path.join(stub_dir, "libGL.so.1")], check=True)
print("   → %d ký hiệu GL" % len(syms))
PY

echo "== 4/4 Tạo lệnh bọc $WRAP"
cat > "$WRAP" <<EOF
#!/bin/sh
# Lệnh bọc python của bộ kiểm headless (đặt LD_LIBRARY_PATH cho libGL stub).
export LD_LIBRARY_PATH="$STUB_DIR:\${LD_LIBRARY_PATH:-}"
exec "$VENV/bin/python" "\$@"
EOF
chmod +x "$WRAP"

echo
echo "XONG. Kiểm tra nhanh:"
"$WRAP" -c "import cadquery, trimesh, numpy; print('   cadquery', cadquery.__version__, '| trimesh', trimesh.__version__, '| numpy', numpy.__version__)"
echo "   Chạy kiểm: cd hardware/finger_fixation && $WRAP headless/run_verify.py"
