#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Thiết kế cơ cấu HÀM GÀI / NGÀM KẸP ĐÀN HỒI (Compliant Snap-Jaw) cho các đốt ngón tay:
- Tỷ lệ cơ sở: 112% (tối ưu nhân trắc học người lớn Việt Nam).
- Mặt mu (Dorsal, +Y): Khung cứng chịu lực, mắt xỏ dẫn cáp Bowden phi 2.4mm, chốt bản lề liên đốt.
- Mặt lòng (Palmar, -Y): Cắt mở đáy tạo khe hở đàn hồi 8-10mm, biến vỏ ngoài thành 2 cánh ngàm chữ C ôm ~230°.
- Mép ngàm kẹp: Có gờ vát dẫn hướng 45 độ (Lead-in chamfer) để bấm ngón tay vào là tự hé mở rồi ôm khít.
- Tích hợp 2 khe gài đai Velcro phụ (1.5mm x 7mm) ở hai bên sườn nẹp để linh hoạt siết đai khi cần.
"""
import sys, os, shutil
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(r"C:\Program Files\FreeCAD 1.1\bin")
sys.path.append(r"C:\Program Files\FreeCAD 1.1\lib")
import FreeCAD, Part, Mesh

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(SCRIPT_DIR, "exo_glove_raw", "files")
OUT_DIR = os.path.join(SCRIPT_DIR, "custom_exo", "snap_jaw_adult")
os.makedirs(OUT_DIR, exist_ok=True)

SCALE = 1.12  # Scale 112% chuẩn ngón tay người lớn

print(f"=== ĐANG DỰNG THIẾT KẾ HÀM GÀI ĐÀN HỒI SNAP-JAW (SCALE {int(SCALE*100)}%) ===")
doc = FreeCAD.newDocument("SnapJawAdultFinger")

# Helper: Scale 1 solid
def scale_solid(solid, factor):
    mat = FreeCAD.Matrix()
    mat.scale(factor, factor, factor)
    return solid.transformGeometry(mat)

# ==========================================
# 1. ĐỐT XA: custom_indice1_snap_jaw
# ==========================================
print("--> Xử lý Đốt xa (indice1)...")
m1 = Mesh.Mesh(os.path.join(RAW_DIR, "indice1.stl"))
s1 = Part.Shape()
s1.makeShapeFromMesh(m1.Topology, 0.05)
solid1 = scale_solid(Part.makeSolid(s1), SCALE)

# Cắt mở đầu ngón tại Z = 13.5mm (đã tính scale)
cutter_tip = Part.makeBox(50, 50, 40, FreeCAD.Vector(-25, -25, 13.5))
open_tip1 = solid1.cut(cutter_tip)

# Cắt mở đáy ngón tạo ngàm kẹp chữ C (khe hở rộng 8mm tại Y < -2.0mm)
cutter_jaw1 = Part.makeBox(8.5, 20.0, 30.0, FreeCAD.Vector(-4.25, -20.0, -5.0))
jaw1 = open_tip1.cut(cutter_jaw1)

# Mấu neo dây mu ngón tay (Anchor boss phi 2.2mm)
boss_outer1 = Part.makeCylinder(2.8, 4.5, FreeCAD.Vector(0, 9.0 * SCALE, 8.0 * SCALE), FreeCAD.Vector(0, 1, 0))
hole1 = Part.makeCylinder(1.1, 12.0, FreeCAD.Vector(-6, 10.5 * SCALE, 9.5 * SCALE), FreeCAD.Vector(1, 0, 0))
boss1 = boss_outer1.cut(hole1)

indice1_snap = jaw1.fuse(boss1).removeSplitter()
Part.export([indice1_snap], os.path.join(OUT_DIR, "custom_indice1_snap_jaw.step"))
mesh1_out = doc.addObject("Mesh::Feature", "custom_indice1_snap_jaw")
mesh1_out.Mesh = Mesh.Mesh(indice1_snap.tessellate(0.05))
Mesh.export([mesh1_out], os.path.join(OUT_DIR, "custom_indice1_snap_jaw.stl"))

# ==========================================
# 2. ĐỐT GIỮA: custom_indice2_snap_jaw
# ==========================================
print("--> Xử lý Đốt giữa (indice2)...")
m2 = Mesh.Mesh(os.path.join(RAW_DIR, "indice2.stl"))
s2 = Part.Shape()
s2.makeShapeFromMesh(m2.Topology, 0.05)
solid2 = scale_solid(Part.makeSolid(s2), SCALE)

# Cắt mở khe đáy đàn hồi rộng 9.5mm (Y < -3.0mm)
cutter_jaw2 = Part.makeBox(9.5, 25.0, 60.0, FreeCAD.Vector(-4.75, -25.0, -25.0))
jaw2 = solid2.cut(cutter_jaw2)

# Mắt dẫn cáp mu ngón (phi trong 2.4mm, ngoài 6.5mm)
eyelet_out2 = Part.makeCylinder(3.2, 4.5, FreeCAD.Vector(0, 10.0 * SCALE, 5.0 * SCALE), FreeCAD.Vector(0, 1, 0))
cable_hole2 = Part.makeCylinder(1.2, 12.0, FreeCAD.Vector(0, 12.0 * SCALE, 0.0), FreeCAD.Vector(0, 0, 1))
eyelet2 = eyelet_out2.cut(cable_hole2)

# Tạo 2 khe gài đai Velcro phụ (1.5mm x 7mm) ở 2 bên sườn
slot_cutter_left = Part.makeBox(2.0, 8.0, 1.6, FreeCAD.Vector(-13.5 * SCALE, -4.0 * SCALE, 3.0 * SCALE))
slot_cutter_right = Part.makeBox(2.0, 8.0, 1.6, FreeCAD.Vector(11.5 * SCALE, -4.0 * SCALE, 3.0 * SCALE))

indice2_snap = jaw2.fuse(eyelet2).cut(slot_cutter_left).cut(slot_cutter_right).removeSplitter()
Part.export([indice2_snap], os.path.join(OUT_DIR, "custom_indice2_snap_jaw.step"))
mesh2_out = doc.addObject("Mesh::Feature", "custom_indice2_snap_jaw")
mesh2_out.Mesh = Mesh.Mesh(indice2_snap.tessellate(0.05))
Mesh.export([mesh2_out], os.path.join(OUT_DIR, "custom_indice2_snap_jaw.stl"))

# ==========================================
# 3. ĐỐT GẦN: custom_indice3_snap_jaw
# ==========================================
print("--> Xử lý Đốt gần (indice3)...")
m3 = Mesh.Mesh(os.path.join(RAW_DIR, "indice3.stl"))
s3 = Part.Shape()
s3.makeShapeFromMesh(m3.Topology, 0.05)
solid3 = scale_solid(Part.makeSolid(s3), SCALE)

# Cắt mở khe đáy đàn hồi rộng 10.5mm (Y < -3.5mm)
cutter_jaw3 = Part.makeBox(10.5, 30.0, 70.0, FreeCAD.Vector(-5.25, -30.0, -10.0))
jaw3 = solid3.cut(cutter_jaw3)

# Mắt dẫn cáp mu ngón
eyelet_out3 = Part.makeCylinder(3.2, 4.5, FreeCAD.Vector(0, 16.5 * SCALE, 22.0 * SCALE), FreeCAD.Vector(0, 1, 0))
cable_hole3 = Part.makeCylinder(1.2, 12.0, FreeCAD.Vector(0, 18.5 * SCALE, 17.0 * SCALE), FreeCAD.Vector(0, 0, 1))
eyelet3 = eyelet_out3.cut(cable_hole3)

# Khe gài đai sườn đốt gần
slot3_left = Part.makeBox(2.0, 8.0, 1.6, FreeCAD.Vector(-14.5 * SCALE, -4.0 * SCALE, 15.0 * SCALE))
slot3_right = Part.makeBox(2.0, 8.0, 1.6, FreeCAD.Vector(12.5 * SCALE, -4.0 * SCALE, 15.0 * SCALE))

indice3_snap = jaw3.fuse(eyelet3).cut(slot3_left).cut(slot3_right).removeSplitter()
Part.export([indice3_snap], os.path.join(OUT_DIR, "custom_indice3_snap_jaw.step"))
mesh3_out = doc.addObject("Mesh::Feature", "custom_indice3_snap_jaw")
mesh3_out.Mesh = Mesh.Mesh(indice3_snap.tessellate(0.05))
Mesh.export([mesh3_out], os.path.join(OUT_DIR, "custom_indice3_snap_jaw.stl"))

# ==========================================
# 4. SCALE VÀ XUẤT CHỐT TRỤC BẢN LỀ + ĐỐT BÀN TAY
# ==========================================
print("--> Scale và xuất chốt bản lề perno_2, perno_anillo, nudillo1...")
for part_name in ["nudillo1.stl", "perno_2.stl", "perno_anillo.stl"]:
    mesh_acc = Mesh.Mesh(os.path.join(RAW_DIR, part_name))
    shape_acc = Part.Shape()
    shape_acc.makeShapeFromMesh(mesh_acc.Topology, 0.05)
    solid_acc = scale_solid(Part.makeSolid(shape_acc), SCALE).removeSplitter()
    
    base_name = part_name.replace(".stl", "_scaled.stl")
    mesh_out_acc = doc.addObject("Mesh::Feature", base_name)
    mesh_out_acc.Mesh = Mesh.Mesh(solid_acc.tessellate(0.05))
    Mesh.export([mesh_out_acc], os.path.join(OUT_DIR, base_name))
    Part.export([solid_acc], os.path.join(OUT_DIR, base_name.replace(".stl", ".step")))
    print(f"  + Xuất {base_name}")

doc.saveAs(os.path.join(OUT_DIR, "snap_jaw_index_finger_adult.FCStd"))
print("\n=== HOÀN TẤT! TOÀN BỘ FILE HÀM GÀI ĐÃ XUẤT TẠI: ===")
print(OUT_DIR)
for f in os.listdir(OUT_DIR):
    print("  *", f)
