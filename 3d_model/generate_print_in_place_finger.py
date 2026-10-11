import sys
import os
import io

# Đảm bảo UTF-8 cho console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import FreeCAD
import Part
import Mesh

OUT_DIR = r"D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\3d_model\custom_exo\print_in_place_adult"
os.makedirs(OUT_DIR, exist_ok=True)

doc = FreeCAD.newDocument("PrintInPlaceHinge")

print("=== BẮT ĐẦU DỰNG BẢN LỀ IN NGUYÊN KHỐI VỚI KHÓA NGÀM MỎ QUẠ ÔM NGOÀI (EXTERNAL RATCHET CLASP) ===")

# ==========================================
# CÁC THÔNG SỐ CƠ BẢN (Adult Size phi 20mm)
# ==========================================
FINGER_R_IN = 9.8    # Bán kính trong ôm ngón tay (phi ~20mm)
SHELL_THICK = 2.2    # Độ dày vòm máng mu ngón
HEIGHT_Z = 12.0      # Chiều dài đốt ngón tay

# Tọa độ tâm trục bản lề xoay bên sườn trái
HX = -12.5
HY = -2.2
PIN_R = 1.4          # Bán kính trục xoay phi 2.8mm
GAP_RADIAL = 0.35    # Khe hở hướng kính in liền FDM (0.35mm mỗi bên)
HOLE_R = PIN_R + GAP_RADIAL  # 1.75mm (phi 3.5mm)

# Khe hở mặt đầu dọc trục Z (Axial gap)
GAP_AXIAL = 0.4
KNUCKLE_Z_MIN = 3.4
KNUCKLE_Z_MAX = 8.6
KNUCKLE_HEIGHT = KNUCKLE_Z_MAX - KNUCKLE_Z_MIN # 5.2mm

# ==========================================
# 1. CHI TIẾT A: MÁNG MU NGÓN TAY + TRỤC XOAY LIỀN KHỐI
# ==========================================
print("--> Đang dựng Máng mu ngón tay tích hợp trục xoay & Gờ răng khóa ngoài...")
outer_cyl = Part.makeCylinder(FINGER_R_IN + SHELL_THICK, HEIGHT_Z, FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1))
inner_cyl = Part.makeCylinder(FINGER_R_IN, HEIGHT_Z + 4.0, FreeCAD.Vector(0, 0, -2.0), FreeCAD.Vector(0, 0, 1))
shell_tube = outer_cyl.cut(inner_cyl)

# Cắt mở đáy mặt lòng (Y <= 0)
cutter_bottom = Part.makeBox(36.0, 18.0, HEIGHT_Z + 4.0, FreeCAD.Vector(-18.0, -18.0, -2.0))
dorsal_shell_base = shell_tube.cut(cutter_bottom)

# Cắt rãnh cho tai giữa thanh gài xoay tự do trong khoảng Z=3.0 đến 9.0 tại vùng HX, HY
arm_swing_clearance = Part.makeCylinder(HOLE_R + 1.8, 6.0, FreeCAD.Vector(HX, HY, 3.0), FreeCAD.Vector(0, 0, 1))
dorsal_shell_base = dorsal_shell_base.cut(arm_swing_clearance)

# Khuyên dẫn cáp gân trên mu (+Y)
eyelet_out = Part.makeCylinder(3.2, 5.0, FreeCAD.Vector(0, FINGER_R_IN, HEIGHT_Z/2.0), FreeCAD.Vector(0, 1, 0))
cable_hole = Part.makeCylinder(1.2, 16.0, FreeCAD.Vector(0, FINGER_R_IN + 2.5, -2.0), FreeCAD.Vector(0, 0, 1))
eyelet = eyelet_out.cut(cable_hole)

# Tai bản lề chạc đôi bên sườn trái (Z = 0-3mm và Z = 9-12mm)
lug_outer = Part.makeCylinder(PIN_R + 1.2, HEIGHT_Z, FreeCAD.Vector(HX, HY, 0.0), FreeCAD.Vector(0, 0, 1))
lug_slot_cut = Part.makeBox(14.0, 14.0, 6.0, FreeCAD.Vector(HX - 7.0, HY - 7.0, 3.0))
lug_fork = lug_outer.cut(lug_slot_cut)
lug_bridge = Part.makeBox(4.0, 3.5, HEIGHT_Z, FreeCAD.Vector(HX, HY, 0.0)).cut(lug_slot_cut)

# TRỤC XOAY TRÒN ĐÚC LIỀN (Integrated Hinge Pin - phi 2.8mm chạy xuyên suốt Z=0 đến 12mm)
hinge_pin_integrated = Part.makeCylinder(PIN_R, HEIGHT_Z, FreeCAD.Vector(HX, HY, 0.0), FreeCAD.Vector(0, 0, 1))

# KHỐI GỜ RĂNG KHÓA NGOÀI SƯỜN PHẢI (External Ratchet Catch on Dorsal Shell)
# Thiết kế hoàn toàn ở MẶT NGOÀI, KHÔNG CÓ HỐC RỖNG KÍN, in FDM sắc nét 100%
ratchet_base = Part.makeBox(2.2, 4.5, HEIGHT_Z, FreeCAD.Vector(11.5, 0.0, 0.0))
# Rãnh khóa Nấc 1 (cho ngón lớn, chu vi rộng)
groove_step1 = Part.makeBox(2.0, 1.4, HEIGHT_Z + 2.0, FreeCAD.Vector(11.9, 0.5, -1.0))
# Rãnh khóa Nấc 2 (cho ngón thon, ôm sát)
groove_step2 = Part.makeBox(2.0, 1.4, HEIGHT_Z + 2.0, FreeCAD.Vector(11.9, 2.5, -1.0))
ratchet_catch = ratchet_base.cut(groove_step1).cut(groove_step2)

dorsal_full = dorsal_shell_base.fuse(eyelet).fuse(lug_fork).fuse(lug_bridge).fuse(hinge_pin_integrated).fuse(ratchet_catch).removeSplitter()

# ==========================================
# 2. CHI TIẾT B: THANH GÀI BỤNG NGÓN TAY (PALMAR SWING-ARM)
# ==========================================
print("--> Đang dựng Thanh gài bụng ngón tay tích hợp ngàm mỏ quạ ôm ngoài & tai gạt ngón cái...")
knuckle_out = Part.makeCylinder(HOLE_R + 1.2, KNUCKLE_HEIGHT, FreeCAD.Vector(HX, HY, KNUCKLE_Z_MIN), FreeCAD.Vector(0, 0, 1))
arm_bridge = Part.makeBox(4.5, 3.5, KNUCKLE_HEIGHT, FreeCAD.Vector(HX, HY - 2.0, KNUCKLE_Z_MIN))

# Thân cong ôm bụng ngón (Z = 3.4 đến 8.6mm)
arm_out_cyl = Part.makeCylinder(FINGER_R_IN + 1.6, KNUCKLE_HEIGHT, FreeCAD.Vector(0, 0, KNUCKLE_Z_MIN), FreeCAD.Vector(0, 0, 1))
arm_in_cyl = Part.makeCylinder(FINGER_R_IN - 0.4, KNUCKLE_HEIGHT + 2.0, FreeCAD.Vector(0, 0, KNUCKLE_Z_MIN - 1.0), FreeCAD.Vector(0, 0, 1))
arm_slice = arm_out_cyl.cut(arm_in_cyl)
arm_bottom_half = arm_slice.cut(Part.makeBox(36.0, 18.0, 10.0, FreeCAD.Vector(-18.0, -0.6, 2.0)))

# CƠ CẤU KHÓA MỎ QUẠ ĐÀN HỒI ÔM NGOÀI (External Snap-Claw with Ergonomic Thumb Lever):
# Cần đàn hồi vươn dọc sườn ngoài: X = 13.8mm, Y từ -2.0 đến +4.2mm
snap_arm_outer = Part.makeBox(1.6, 6.2, KNUCKLE_HEIGHT, FreeCAD.Vector(13.8, -2.0, KNUCKLE_Z_MIN))
# Mấu răng khóa mỏ quạ móc ngược vào trong (-X) lọt vào rãnh Nấc 1 hoặc Nấc 2
tooth_claw = Part.makeBox(1.4, 1.2, KNUCKLE_HEIGHT, FreeCAD.Vector(12.4, 0.6, KNUCKLE_Z_MIN))
# Cầu nối từ thân cong (X=11.0, Y=-1.8) sang cần đàn hồi ngoài
bridge_right = Part.makeBox(3.0, 1.8, KNUCKLE_HEIGHT, FreeCAD.Vector(11.0, -1.8, KNUCKLE_Z_MIN))
# Tai tì ngón cái (Thumb Release Lever) nhô rộng ra ngoài X = 14.8 đến 18.3mm
# Người bệnh chỉ cần dùng ngón cái gạt nhẹ vào tai này là ngàm nhả ra ngay lập tức
thumb_tab = Part.makeBox(3.5, 2.2, KNUCKLE_HEIGHT, FreeCAD.Vector(14.8, 1.8, KNUCKLE_Z_MIN))

latch_claw = snap_arm_outer.fuse(tooth_claw).fuse(bridge_right).fuse(thumb_tab)
arm_raw = knuckle_out.fuse(arm_bridge).fuse(arm_bottom_half).fuse(latch_claw)

# KHOAN LỖ BẢN LỀ XUYÊN QUA TOÀN BỘ ARM (Đảm bảo rỗng 100%, không bị bridge lấn)
knuckle_hole = Part.makeCylinder(HOLE_R, KNUCKLE_HEIGHT + 4.0, FreeCAD.Vector(HX, HY, KNUCKLE_Z_MIN - 2.0), FreeCAD.Vector(0, 0, 1))
chamfer_bot = Part.makeCone(HOLE_R + 0.6, HOLE_R, 0.6, FreeCAD.Vector(HX, HY, KNUCKLE_Z_MIN), FreeCAD.Vector(0, 0, 1))
chamfer_top = Part.makeCone(HOLE_R, HOLE_R + 0.6, 0.6, FreeCAD.Vector(HX, HY, KNUCKLE_Z_MAX - 0.6), FreeCAD.Vector(0, 0, 1))

# Khoang âm cảm biến Velostat: 9.5mm x 7.0mm x 1.2mm
sensor_cutter = Part.makeBox(9.5, 1.3, 7.0, FreeCAD.Vector(-4.75, -FINGER_R_IN + 0.2, 2.5))
arm_closed_final = arm_raw.cut(knuckle_hole).cut(chamfer_bot).cut(chamfer_top).cut(sensor_cutter).removeSplitter()

# ==========================================
# 3. TẠO TRẠNG THÁI IN NGUYÊN KHỐI MỞ XOAY RA NGOÀI (Print-in-Place Ready)
# ==========================================
OPEN_ANGLE = -100.0
print(f"--> Tạo phiên bản Print-in-Place mở góc xoay {OPEN_ANGLE} độ ra ngoài...")
arm_open = arm_closed_final.copy()
arm_open.rotate(FreeCAD.Vector(HX, HY, 0), FreeCAD.Vector(0, 0, 1), OPEN_ANGLE)

# Cụm in nguyên khối (Print-in-Place Compound):
pip_compound_open = Part.Compound([dorsal_full, arm_open])
pip_compound_closed = Part.Compound([dorsal_full, arm_closed_final])

# Xuất các file CAD và STL
print("--> Đang xuất các file STL và STEP...")

# 1. File in 3D nguyên khối (Mở góc xoay ra ngoài - FILE CHÍNH ĐỂ NẠP SLICER)
Part.export([pip_compound_open], os.path.join(OUT_DIR, "finger_print_in_place_open90.step"))
mesh_pip_open = doc.addObject("Mesh::Feature", "pip_open")
mesh_pip_open.Mesh = Mesh.Mesh(pip_compound_open.tessellate(0.05))
Mesh.export([mesh_pip_open], os.path.join(OUT_DIR, "finger_print_in_place_open90.stl"))

# 2. File mô phỏng trạng thái đóng
Part.export([pip_compound_closed], os.path.join(OUT_DIR, "finger_print_in_place_closed.step"))
mesh_pip_closed = doc.addObject("Mesh::Feature", "pip_closed")
mesh_pip_closed.Mesh = Mesh.Mesh(pip_compound_closed.tessellate(0.05))
Mesh.export([mesh_pip_closed], os.path.join(OUT_DIR, "finger_print_in_place_closed.stl"))

# 3. Xuất riêng từng chi tiết để kiểm tra CAD
Part.export([dorsal_full], os.path.join(OUT_DIR, "pip_dorsal_shell_integrated_pin.step"))
mesh_d = doc.addObject("Mesh::Feature", "dorsal")
mesh_d.Mesh = Mesh.Mesh(dorsal_full.tessellate(0.05))
Mesh.export([mesh_d], os.path.join(OUT_DIR, "pip_dorsal_shell_integrated_pin.stl"))

Part.export([arm_closed_final], os.path.join(OUT_DIR, "pip_palmar_arm_closed.step"))
mesh_a = doc.addObject("Mesh::Feature", "palmar")
mesh_a.Mesh = Mesh.Mesh(arm_closed_final.tessellate(0.05))
Mesh.export([mesh_a], os.path.join(OUT_DIR, "pip_palmar_arm_closed.stl"))

doc.saveAs(os.path.join(OUT_DIR, "finger_print_in_place.FCStd"))

print("\n=== ĐÃ XUẤT THÀNH CÔNG TOÀN BỘ FILE BẢN LỀ IN LIỀN KHỐI VỚI KHÓA MỎ QUẠ NGOÀI! ===")
print("Thư mục lưu:", OUT_DIR)
