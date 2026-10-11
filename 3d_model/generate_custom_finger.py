#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tự động tùy biến các đốt nẹp ngón trỏ (Index Finger) từ mẫu gốc Thing:2394197 sang cơ cấu kéo dây gân:
1. custom_indice1: Cắt mở đầu ngón (Open-tip) tại Z=12mm + Thêm mấu neo dây cáp (Anchor boss phi 2.0mm).
2. custom_indice2: Thêm mắt xỏ dẫn cáp (Cable Guide Eyelet phi 2.2mm) trên sống mu ngón tay.
3. custom_indice3: Thêm mắt xỏ dẫn cáp (Cable Guide Eyelet phi 2.2mm) đồng trục với đốt 2.
4. Sao chép các chốt bản lề perno_2.stl, perno_anillo.stl, nudillo1.stl vào thư mục assembly.
5. Xuất các định dạng chuẩn: .STL, .STEP và dự án FreeCAD .FCStd.
"""
import sys, os, shutil
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(r"C:\Program Files\FreeCAD 1.1\bin")
sys.path.append(r"C:\Program Files\FreeCAD 1.1\lib")
import FreeCAD, Part, Mesh

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(SCRIPT_DIR, "exo_glove_raw", "files")
OUT_DIR = os.path.join(SCRIPT_DIR, "custom_exo", "index_finger")
os.makedirs(OUT_DIR, exist_ok=True)

doc = FreeCAD.newDocument("IndexFingerCustom")

# ==========================================
# 1. TÙY BIẾN ĐỐT XA: custom_indice1
# ==========================================
print("--> Đang tùy biến custom_indice1 (Open-tip + Anchor)...")
mesh1 = Mesh.Mesh(os.path.join(RAW_DIR, "indice1.stl"))
shape1 = Part.Shape()
shape1.makeShapeFromMesh(mesh1.Topology, 0.05)
solid1 = Part.makeSolid(shape1)

# Cắt mở đầu ngón tại Z = 12.0 mm
cutter = Part.makeBox(40, 40, 30, FreeCAD.Vector(-20, -20, 12.0))
open_tip = solid1.cut(cutter)

# Tạo mấu neo dây mu ngón tay (Anchor boss) tại Z = 8.0 mm, Y = 8.5 mm
# Trụ boss ngoài đường kính 5mm, cao 4mm
boss_outer = Part.makeCylinder(2.5, 4.0, FreeCAD.Vector(0, 8.0, 7.0), FreeCAD.Vector(0, 1, 0))
# Lỗ xỏ dây xuyên ngang qua boss (song song trục X) phi 2.0mm
hole = Part.makeCylinder(1.0, 10.0, FreeCAD.Vector(-5, 9.5, 8.5), FreeCAD.Vector(1, 0, 0))
boss = boss_outer.cut(hole)

indice1_custom = open_tip.fuse(boss)
indice1_custom = indice1_custom.removeSplitter()

# Xuất indice1
Part.export([indice1_custom], os.path.join(OUT_DIR, "custom_indice1_open_tip_anchor.step"))
mesh_out1 = doc.addObject("Mesh::Feature", "custom_indice1")
mesh_out1.Mesh = Mesh.Mesh(indice1_custom.tessellate(0.05))
Mesh.export([mesh_out1], os.path.join(OUT_DIR, "custom_indice1_open_tip_anchor.stl"))

# ==========================================
# 2. TÙY BIẾN ĐỐT GIỮA: custom_indice2
# ==========================================
print("--> Đang tùy biến custom_indice2 (Cable Guide)...")
mesh2 = Mesh.Mesh(os.path.join(RAW_DIR, "indice2.stl"))
shape2 = Part.Shape()
shape2.makeShapeFromMesh(mesh2.Topology, 0.05)
solid2 = Part.makeSolid(shape2)

# Mắt dẫn cáp (Cable Guide Eyelet) tại mu đốt ngón (Y = 11.0, Z = 5.0)
eyelet_outer2 = Part.makeCylinder(3.0, 4.0, FreeCAD.Vector(0, 9.0, 5.0), FreeCAD.Vector(0, 1, 0))
# Lỗ dẫn dây dọc trục Z (hướng cáp chạy từ đốt 3 sang đốt 1)
cable_hole2 = Part.makeCylinder(1.1, 10.0, FreeCAD.Vector(0, 11.0, 1.0), FreeCAD.Vector(0, 0, 1))
eyelet2 = eyelet_outer2.cut(cable_hole2)

indice2_custom = solid2.fuse(eyelet2)
indice2_custom = indice2_custom.removeSplitter()

Part.export([indice2_custom], os.path.join(OUT_DIR, "custom_indice2_guide.step"))
mesh_out2 = doc.addObject("Mesh::Feature", "custom_indice2")
mesh_out2.Mesh = Mesh.Mesh(indice2_custom.tessellate(0.05))
Mesh.export([mesh_out2], os.path.join(OUT_DIR, "custom_indice2_guide.stl"))

# ==========================================
# 3. TÙY BIẾN ĐỐT GẦN: custom_indice3
# ==========================================
print("--> Đang tùy biến custom_indice3 (Cable Guide)...")
mesh3 = Mesh.Mesh(os.path.join(RAW_DIR, "indice3.stl"))
shape3 = Part.Shape()
shape3.makeShapeFromMesh(mesh3.Topology, 0.05)
solid3 = Part.makeSolid(shape3)

# Mắt dẫn cáp mu ngón đốt 3 (Y = 16.5, Z = 22.0)
eyelet_outer3 = Part.makeCylinder(3.0, 4.0, FreeCAD.Vector(0, 15.0, 22.0), FreeCAD.Vector(0, 1, 0))
cable_hole3 = Part.makeCylinder(1.1, 10.0, FreeCAD.Vector(0, 17.0, 18.0), FreeCAD.Vector(0, 0, 1))
eyelet3 = eyelet_outer3.cut(cable_hole3)

indice3_custom = solid3.fuse(eyelet3)
indice3_custom = indice3_custom.removeSplitter()

Part.export([indice3_custom], os.path.join(OUT_DIR, "custom_indice3_guide.step"))
mesh_out3 = doc.addObject("Mesh::Feature", "custom_indice3")
mesh_out3.Mesh = Mesh.Mesh(indice3_custom.tessellate(0.05))
Mesh.export([mesh_out3], os.path.join(OUT_DIR, "custom_indice3_guide.stl"))

# Lưu dự án FreeCAD
doc.saveAs(os.path.join(OUT_DIR, "index_finger_custom.FCStd"))

# ==========================================
# 4. SAO CHÉP CÁC PHỤ KIỆN LẮP RÁP (PINS & KNUCKLE)
# ==========================================
for accessory in ["perno_2.stl", "perno_anillo.stl", "nudillo1.stl"]:
    src = os.path.join(RAW_DIR, accessory)
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(OUT_DIR, accessory))
        print(f"Copied: {accessory}")

print("\n--> TOÀN BỘ FILE TÙY BIẾN ĐÃ XUẤT THÀNH CÔNG VÀO:")
print(OUT_DIR)
for f in os.listdir(OUT_DIR):
    print("  *", f)
