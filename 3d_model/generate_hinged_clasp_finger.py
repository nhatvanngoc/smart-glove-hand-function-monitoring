import sys
import os
import io

# Đảm bảo UTF-8 cho console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import FreeCAD
import Part
import Mesh

OUT_DIR = r"D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\3d_model\custom_exo\hinged_clasp_adult"
os.makedirs(OUT_DIR, exist_ok=True)

doc = FreeCAD.newDocument("HingedClaspSnapPin")

print("=== BẮT ĐẦU DỰNG HỆ THỐNG GÀI BẢN LỀ KHỚP CHẠC VỚI CHỐT NHỰA SNAP-RIVET ===")

# ==========================================
# 1. CHI TIẾT A: MÁNG MU NGÓN TAY (Dorsal Shell)
# ==========================================
print("--> Đang dựng Chi tiết A: Máng mu ngón tay (Dorsal Shell với bản lề chạc đôi)...")
# Khung mu ngón: Vòm bán nguyệt R_in = 9.8mm, R_out = 12.0mm, Chiều dài Z = 12.0mm
outer_cyl = Part.makeCylinder(12.0, 12.0, FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1))
inner_cyl = Part.makeCylinder(9.8, 14.0, FreeCAD.Vector(0, 0, -1.0), FreeCAD.Vector(0, 0, 1))
shell_tube = outer_cyl.cut(inner_cyl)

# Mở đáy mặt lòng 100% (cắt bỏ phần Y <= 0.0)
bottom_cutter = Part.makeBox(36.0, 18.0, 16.0, FreeCAD.Vector(-18.0, -18.0, -2.0))
dorsal_base = shell_tube.cut(bottom_cutter)

# Khuyên dẫn cáp gân trên mu ngón (Y = +12.0mm, Z = 6.0mm)
eyelet_out = Part.makeCylinder(3.2, 5.0, FreeCAD.Vector(0, 9.5, 6.0), FreeCAD.Vector(0, 1, 0))
cable_hole = Part.makeCylinder(1.2, 16.0, FreeCAD.Vector(0, 12.0, -2.0), FreeCAD.Vector(0, 0, 1))
eyelet = eyelet_out.cut(cable_hole)

# Tai bản lề chạc đôi bên sườn trái (X = -12.5mm, Y = -2.2mm):
# Gồm tai dưới (Z = 0 đến 3.0mm) và tai trên (Z = 9.0 đến 12.0mm)
# Để hở khe giữa (Z = 3.0 đến 9.0mm) cho tai thanh gài lọt vào!
lug_outer = Part.makeCylinder(2.4, 12.0, FreeCAD.Vector(-12.5, -2.2, 0.0), FreeCAD.Vector(0, 0, 1))
lug_hole = Part.makeCylinder(1.05, 16.0, FreeCAD.Vector(-12.5, -2.2, -2.0), FreeCAD.Vector(0, 0, 1))
lug_slot_cutter = Part.makeBox(8.0, 8.0, 6.0, FreeCAD.Vector(-16.0, -6.0, 3.0)) # cắt rãnh giữa Z=3 đến Z=9
fork_hinge = lug_outer.cut(lug_hole).cut(lug_slot_cutter)
fork_bridge = Part.makeBox(4.0, 3.5, 12.0, FreeCAD.Vector(-12.5, -2.2, 0.0)).cut(lug_slot_cutter)

# Ngàm khóa sườn phải (X = +12.0mm, Y = -2.2mm)
# Khối ngàm khóa có 2 nấc gài (Z = 0 đến 12.0mm)
latch_block_out = Part.makeBox(4.0, 5.0, 12.0, FreeCAD.Vector(10.5, -4.5, 0.0))
# Rãnh nấc 1 (cho ngón lớn, chu vi rộng)
catch_step1 = Part.makeBox(2.2, 1.8, 14.0, FreeCAD.Vector(12.2, -3.8, -1.0))
# Rãnh nấc 2 (cho ngón thon, ôm sát)
catch_step2 = Part.makeBox(2.2, 1.8, 14.0, FreeCAD.Vector(12.2, -1.8, -1.0))
latch_block = latch_block_out.cut(catch_step1).cut(catch_step2)

dorsal_shell = dorsal_base.fuse(eyelet).fuse(fork_hinge).fuse(fork_bridge).fuse(latch_block).removeSplitter()

Part.export([dorsal_shell], os.path.join(OUT_DIR, "indice2_dorsal_shell.step"))
mesh_a = doc.addObject("Mesh::Feature", "indice2_dorsal_shell")
mesh_a.Mesh = Mesh.Mesh(dorsal_shell.tessellate(0.05))
Mesh.export([mesh_a], os.path.join(OUT_DIR, "indice2_dorsal_shell.stl"))

# ==========================================
# 2. CHI TIẾT B: THANH GÀI XOAY BẢN LỀ (Palmar Swing-Arm)
# ==========================================
print("--> Đang dựng Chi tiết B: Thanh gài xoay bản lề (Palmar Swing-Arm)...")
# Khối bản lề tai đơn ở giữa (Z = 3.3 đến 8.7mm, khe hở 0.3mm trên dưới)
arm_knuckle_out = Part.makeCylinder(2.3, 5.4, FreeCAD.Vector(-12.5, -2.2, 3.3), FreeCAD.Vector(0, 0, 1))
arm_knuckle_hole = Part.makeCylinder(1.05, 8.0, FreeCAD.Vector(-12.5, -2.2, 2.0), FreeCAD.Vector(0, 0, 1))
arm_knuckle = arm_knuckle_out.cut(arm_knuckle_hole)

# Thân thanh gài cong ôm bụng ngón: R_in = 9.2mm, R_out = 11.2mm, chiều rộng Z = 5.4mm (Z = 3.3 đến 8.7)
arm_outer = Part.makeCylinder(11.2, 5.4, FreeCAD.Vector(0, 0, 3.3), FreeCAD.Vector(0, 0, 1))
arm_inner = Part.makeCylinder(9.2, 8.0, FreeCAD.Vector(0, 0, 2.0), FreeCAD.Vector(0, 0, 1))
arm_ring = arm_outer.cut(arm_inner)
# Chỉ lấy nửa dưới lòng bàn tay (Y <= -0.5mm)
arm_cutter_top = Part.makeBox(36.0, 18.0, 10.0, FreeCAD.Vector(-18.0, -0.5, 1.0))
arm_arch = arm_ring.cut(arm_cutter_top)

# Cầu nối từ trục xoay vào thân cong
arm_bridge_left = Part.makeBox(4.5, 3.5, 5.4, FreeCAD.Vector(-12.5, -4.2, 3.3))

# Đầu lẫy khóa đàn hồi bên phải (Snap Hook with Thumb Tab)
hook_stem = Part.makeBox(3.0, 4.5, 5.4, FreeCAD.Vector(10.0, -4.2, 3.3))
# Gờ móc (Catch tooth) nhô ra 1.4mm khớp vào rãnh ngàm máng ngón
catch_tooth = Part.makeBox(1.6, 1.5, 5.4, FreeCAD.Vector(11.8, -2.8, 3.3))
# Tai gạt ngón cái (Thumb Tab)
thumb_tab = Part.makeBox(3.5, 2.5, 5.4, FreeCAD.Vector(11.5, -6.5, 3.3))
latch_end = hook_stem.fuse(catch_tooth).fuse(thumb_tab)

swing_arm_solid = arm_knuckle.fuse(arm_bridge_left).fuse(arm_arch).fuse(latch_end)

# HỐC ÂM CẢM BIẾN VELOSTAT (Sensor Pocket: 9.5mm x 7.0mm x 1.2mm)
# Đặt chính giữa bụng ngón tay (X = -4.75 đến +4.75, Z = 2.5 đến 9.5)
sensor_pocket_cutter = Part.makeBox(9.5, 1.3, 8.0, FreeCAD.Vector(-4.75, -9.4, 2.0))
swing_arm_final = swing_arm_solid.cut(sensor_pocket_cutter).removeSplitter()

Part.export([swing_arm_final], os.path.join(OUT_DIR, "indice2_palmar_swing_arm.step"))
mesh_b = doc.addObject("Mesh::Feature", "indice2_palmar_swing_arm")
mesh_b.Mesh = Mesh.Mesh(swing_arm_final.tessellate(0.05))
Mesh.export([mesh_b], os.path.join(OUT_DIR, "indice2_palmar_swing_arm.stl"))

# ==========================================
# 3. CHI TIẾT C: CHỐT NHỰA SNAP-RIVET TỰ KHÓA (All-Plastic Snap-Pin)
# ==========================================
print("--> Đang dựng Chi tiết C: Chốt nhựa Snap-Rivet tự khóa (Plastic Snap-Pin)...")
# Tọa độ chốt nằm dọc trục Z từ Z = -1.8 đến Z = +14.5mm tại vị trí (-12.5, -2.2)

# Mũ chốt (Head): đường kính 4.4mm, dày 1.6mm (Z = -1.6 đến 0.0)
pin_head = Part.makeCylinder(2.2, 1.6, FreeCAD.Vector(-12.5, -2.2, -1.6), FreeCAD.Vector(0, 0, 1))

# Thân chốt hình trụ (Shaft): đường kính 1.95mm (vừa vặn lỗ 2.1mm), dài 12.2mm (Z = 0.0 đến 12.2)
pin_shaft = Part.makeCylinder(0.975, 12.2, FreeCAD.Vector(-12.5, -2.2, 0.0), FreeCAD.Vector(0, 0, 1))

# Đầu ngàm nón tự khóa (Conical Snap Barb):
# Bắt đầu tại Z = 12.1 (ngay trên mép tai bản lề Z = 12.0)
# Gờ khóa hình nón mở rộng từ bán kính thân 0.975 lên 1.3mm (đường kính 2.6mm)
barb_lip = Part.makeCone(1.3, 1.3, 0.4, FreeCAD.Vector(-12.5, -2.2, 12.1), FreeCAD.Vector(0, 0, 1)) if False else Part.makeCylinder(1.3, 0.4, FreeCAD.Vector(-12.5, -2.2, 12.1), FreeCAD.Vector(0, 0, 1))
# Mũi vát côn dẫn hướng 30 độ từ bán kính 1.3mm thu nhỏ dần về 0.6mm ở đỉnh (Z = 12.5 đến 14.3)
barb_tip = Part.makeCone(1.3, 0.6, 1.8, FreeCAD.Vector(-12.5, -2.2, 12.5), FreeCAD.Vector(0, 0, 1))
pin_barb = barb_lip.fuse(barb_tip)

pin_solid_unsplit = pin_head.fuse(pin_shaft).fuse(pin_barb)

# Rãnh xẻ đàn hồi (Expansion Slit): rộng 0.55mm, sâu 4.2mm từ đỉnh chốt xuống (Z = 10.3 đến 14.8)
# Rãnh xẻ này cho phép 2 nửa đầu nón ép lại khi đẩy qua lỗ 2.1mm, rồi tự bung khóa ở mặt trên
slit_cutter = Part.makeBox(4.0, 0.55, 4.8, FreeCAD.Vector(-14.5, -2.475, 10.2))
snap_pin_final = pin_solid_unsplit.cut(slit_cutter).removeSplitter()

Part.export([snap_pin_final], os.path.join(OUT_DIR, "clasp_hinge_pin_2mm.step"))
mesh_c = doc.addObject("Mesh::Feature", "clasp_hinge_pin_2mm")
mesh_c.Mesh = Mesh.Mesh(snap_pin_final.tessellate(0.05))
Mesh.export([mesh_c], os.path.join(OUT_DIR, "clasp_hinge_pin_2mm.stl"))

doc.saveAs(os.path.join(OUT_DIR, "hinged_clasp_finger.FCStd"))

print("\n=== TOÀN BỘ FILE CAD & STL HÀM GÀI + CHỐT NHỰA SNAP-RIVET ĐÃ XUẤT THÀNH CÔNG! ===")
