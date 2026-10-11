import sys
import os
import io
import math

# Đảm bảo UTF-8 cho console Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import FreeCAD
import Part
import Mesh

OUT_DIR = r"D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\3d_model\custom_exo\full_finger_modular"
os.makedirs(OUT_DIR, exist_ok=True)

doc = FreeCAD.newDocument("FullFingerMultiStepModular")

print("=== BẮT ĐẦU DỰNG BỘ 3 ĐỐT NGÓN TAY ĐA NẤC TO/NHỎ (5 NẤC) & DÀI/NGẮN (4 NẤC) ===")

# ==============================================================================
# HÀM TẠO RÃNH TRƯỢT ĐA NẤC ĐỊNH VỊ (MULTI-POSITION DETENT SLOT CUTTER)
# ==============================================================================
def make_detent_slot_cutter(r_detent, r_waist, num_steps, step_pitch, p_start, dir_slot, dir_pin):
    """
    Tạo rãnh trượt 4 nấc định vị:
    - Tại mỗi nấc có hốc tròn bán kính r_detent (phi 2.7mm cho chốt phi 2.4mm)
    - Giữa các nấc có eo thắt bán kính r_waist (phi 2.2mm) tạo cảm giác khấc chuyển nấc
    """
    total_len = (num_steps - 1) * step_pitch
    b_waist = Part.makeBox(24.0, 2 * r_waist, total_len, p_start - dir_pin * 12.0 - FreeCAD.Vector(0, r_waist, 0))
    cutter = b_waist
    for i in range(num_steps):
        p_step = p_start + dir_slot * (i * step_pitch)
        c = Part.makeCylinder(r_detent, 24.0, p_step - dir_pin * 12.0, dir_pin)
        cutter = cutter.fuse(c)
    return cutter.removeSplitter()

# ==============================================================================
# HÀM DỰNG 1 ĐỐT NGÓN TAY ĐA NẤC HOÀN CHỈNH
# ==============================================================================
def build_phalanx_multistep(r_in, length_z, is_distal=False, has_front_joint=True, has_rear_joint=True,
                            num_length_steps=4, step_pitch=2.0, front_joint_y=12.5, rear_joint_y=12.5,
                            fork_x_gap=8.2, tongue_x_width=5.2, rear_pin_reach=8.0):
    """
    Tạo 1 đốt ngón tay hoàn chỉnh gồm:
    - Máng mu ngón (Dorsal shell)
    - Dải răng cưa Ratchet 5 nấc ở sườn phải (chỉnh độ TO - NHỎ: phi 18mm -> 24.5mm)
    - Thanh gài bụng ngón (Palmar swing arm) in nguyên khối Print-in-Place (-100 độ)
    - Ngàm mỏ quạ ngoạm đa nấc + lẫy tỳ ngón cái mở 1 tay (Thumb release tab)
    - Khoang cảm biến Velostat (9.5 x 6.8 x 1.2mm)
    - Khớp chạc đôi có 4 nấc định vị chiều dài (chỉnh độ DÀI - NGẮN: 0 -> 6.0mm)
    - Đốt ngoài cùng mở hở đầu ngón (Open-tip) cho móng tay thò ra tự do
    """
    shell_thick = 2.2
    hx = -(r_in + shell_thick + 0.5)
    hy = -2.2
    pin_r = 1.4
    gap_radial = 0.35
    hole_r = pin_r + gap_radial
    
    # 1. DORSAL SHELL (Máng mu ngón)
    outer_cyl = Part.makeCylinder(r_in + shell_thick, length_z, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1))
    inner_cyl = Part.makeCylinder(r_in, length_z + 4.0, FreeCAD.Vector(0,0,-2.0), FreeCAD.Vector(0,0,1))
    shell_tube = outer_cyl.cut(inner_cyl)
    
    cutter_bottom = Part.makeBox(60.0, 30.0, length_z + 4.0, FreeCAD.Vector(-30.0, -30.0, -2.0))
    dorsal_base = shell_tube.cut(cutter_bottom)
    
    knuckle_z_min = 2.6
    knuckle_z_max = length_z - 2.6
    knuckle_height = knuckle_z_max - knuckle_z_min
    
    arm_swing_cut = Part.makeCylinder(hole_r + 1.8, knuckle_height + 0.8, FreeCAD.Vector(hx, hy, knuckle_z_min - 0.4), FreeCAD.Vector(0,0,1))
    dorsal_base = dorsal_base.cut(arm_swing_cut)
    
    # Tai bản lề Print-in-Place bên sườn trái
    lug_outer = Part.makeCylinder(pin_r + 1.2, length_z, FreeCAD.Vector(hx, hy, 0.0), FreeCAD.Vector(0,0,1))
    lug_slot_cut = Part.makeBox(14.0, 14.0, knuckle_height + 0.8, FreeCAD.Vector(hx - 7.0, hy - 7.0, knuckle_z_min - 0.4))
    lug_fork = lug_outer.cut(lug_slot_cut)
    lug_bridge = Part.makeBox(4.5, 3.5, length_z, FreeCAD.Vector(hx, hy, 0.0)).cut(lug_slot_cut)
    hinge_pin_int = Part.makeCylinder(pin_r, length_z, FreeCAD.Vector(hx, hy, 0.0), FreeCAD.Vector(0,0,1))
    
    # DẢI RĂNG CƯA RATCHET 5 NẤC Ở SƯỜN PHẢI (CHỈNH ĐỘ TO - NHỎ)
    rx = r_in + 1.7
    num_radial_steps = 5
    radial_pitch = 1.15
    rack_len_y = num_radial_steps * radial_pitch + 1.6
    rack_base = Part.makeBox(2.4, rack_len_y, length_z, FreeCAD.Vector(rx, 0.0, 0.0))
    
    cutter_teeth = None
    for i in range(num_radial_steps):
        y_tooth = 0.5 + i * radial_pitch
        groove = Part.makeBox(2.2, 0.72, length_z + 2.0, FreeCAD.Vector(rx + 0.5, y_tooth, -1.0))
        if cutter_teeth is None:
            cutter_teeth = groove
        else:
            cutter_teeth = cutter_teeth.fuse(groove)
    ratchet_catch = rack_base.cut(cutter_teeth)
    
    # Khuyên neo / luồn gân trên mu ngón (+Y)
    if is_distal:
        # Hở đầu hoàn toàn, khối neo gân mu ngón có lỗ luồn phi 2.0mm và hốc chặn cos phi 3.4mm
        eyelet_out = Part.makeCylinder(3.2, 5.0, FreeCAD.Vector(0, r_in, length_z/2.0), FreeCAD.Vector(0, 1, 0))
        cable_hole = Part.makeCylinder(1.0, length_z + 4.0, FreeCAD.Vector(0, r_in + 2.5, -2.0), FreeCAD.Vector(0, 0, 1))
        cable_stop = Part.makeCylinder(1.7, 6.0, FreeCAD.Vector(0, r_in + 2.5, length_z/2.0), FreeCAD.Vector(0, 0, 1))
        eyelet = eyelet_out.cut(cable_hole).cut(cable_stop)
    else:
        eyelet_out = Part.makeCylinder(3.2, 5.0, FreeCAD.Vector(0, r_in, length_z/2.0), FreeCAD.Vector(0, 1, 0))
        cable_hole = Part.makeCylinder(1.2, length_z + 4.0, FreeCAD.Vector(0, r_in + 2.5, -2.0), FreeCAD.Vector(0, 0, 1))
        eyelet = eyelet_out.cut(cable_hole)
        
    dorsal_solid = dorsal_base.fuse(lug_fork).fuse(lug_bridge).fuse(hinge_pin_int).fuse(ratchet_catch).fuse(eyelet)
    
    # 2. KHỚP LIÊN ĐỐT MU NGÓN CÓ RÃNH 4 NẤC ĐỊNH VỊ (CHỈNH DÀI - NGẮN)
    if has_front_joint and not is_distal:
        detent_span = (num_length_steps - 1) * step_pitch
        fork_reach = 2.5 + detent_span + 2.5  # 11.0mm cho 4 nấc 2.0mm
        half_gap = fork_x_gap / 2.0
        fork_thick = 2.6
        
        f_left = Part.makeBox(fork_thick, 5.4, fork_reach, FreeCAD.Vector(-(half_gap + fork_thick), front_joint_y - 2.7, length_z))
        f_right = Part.makeBox(fork_thick, 5.4, fork_reach, FreeCAD.Vector(half_gap, front_joint_y - 2.7, length_z))
        
        # Cắt rãnh 4 nấc định vị
        z_slot_start = length_z + 2.5
        slot_cutter = make_detent_slot_cutter(
            r_detent=1.35, r_waist=1.1, num_steps=num_length_steps, step_pitch=step_pitch,
            p_start=FreeCAD.Vector(0, front_joint_y, z_slot_start), 
            dir_slot=FreeCAD.Vector(0, 0, 1), dir_pin=FreeCAD.Vector(1, 0, 0)
        )
        
        front_fork = f_left.fuse(f_right).cut(slot_cutter)
        dorsal_solid = dorsal_solid.fuse(front_fork)
        
    # Khớp sau (Tai giữa phía sau vươn dài với đầu trụ tròn ôm chốt phi 2.4mm)
    if has_rear_joint:
        tongue_reach = rear_pin_reach + 2.5
        # Thân tai nối
        t_box = Part.makeBox(tongue_x_width, 5.0, tongue_reach, 
                             FreeCAD.Vector(-tongue_x_width/2.0, rear_joint_y - 2.5, -tongue_reach))
        # Đầu trụ tròn ôm lấy chốt tại Z = -rear_pin_reach
        t_cyl = Part.makeCylinder(2.5, tongue_x_width, FreeCAD.Vector(-tongue_x_width/2.0, rear_joint_y, -rear_pin_reach), FreeCAD.Vector(1, 0, 0))
        # Lỗ chốt tròn phi 2.6mm
        pin_hole = Part.makeCylinder(1.3, 20.0, FreeCAD.Vector(-10.0, rear_joint_y, -rear_pin_reach), FreeCAD.Vector(1, 0, 0))
        rear_tongue = t_box.fuse(t_cyl).cut(pin_hole)
        dorsal_solid = dorsal_solid.fuse(rear_tongue)
        
    dorsal_final = dorsal_solid.removeSplitter()
    
    # 3. PALMAR SWING ARM (Thanh gài bụng ngón đa nấc)
    knuckle_out = Part.makeCylinder(hole_r + 1.2, knuckle_height, FreeCAD.Vector(hx, hy, knuckle_z_min), FreeCAD.Vector(0, 0, 1))
    arm_bridge = Part.makeBox(4.5, 3.5, knuckle_height, FreeCAD.Vector(hx, hy - 2.0, knuckle_z_min))
    
    arm_out_cyl = Part.makeCylinder(r_in + 1.6, knuckle_height, FreeCAD.Vector(0, 0, knuckle_z_min), FreeCAD.Vector(0, 0, 1))
    arm_in_cyl = Part.makeCylinder(r_in - 0.4, knuckle_height + 2.0, FreeCAD.Vector(0, 0, knuckle_z_min - 1.0), FreeCAD.Vector(0, 0, 1))
    arm_slice = arm_out_cyl.cut(arm_in_cyl)
    arm_bottom = arm_slice.cut(Part.makeBox(60.0, 30.0, 20.0, FreeCAD.Vector(-30.0, -0.6, 0.0)))
    
    # Ngàm mỏ quạ ôm ngoài đa nấc (Multi-step Ratchet Snap-Claw)
    snap_arm_out = Part.makeBox(1.6, rack_len_y + 1.8, knuckle_height, FreeCAD.Vector(rx + 2.4, -2.0, knuckle_z_min))
    tooth_claw = Part.makeBox(1.5, 1.0, knuckle_height, FreeCAD.Vector(rx + 0.9, 0.5, knuckle_z_min))
    bridge_r = Part.makeBox(3.0, 1.8, knuckle_height, FreeCAD.Vector(rx - 0.5, -1.8, knuckle_z_min))
    thumb_tab = Part.makeBox(3.8, 2.4, knuckle_height, FreeCAD.Vector(rx + 3.4, rack_len_y - 0.6, knuckle_z_min))
    latch_claw = snap_arm_out.fuse(tooth_claw).fuse(bridge_r).fuse(thumb_tab)
    
    arm_raw = knuckle_out.fuse(arm_bridge).fuse(arm_bottom).fuse(latch_claw)
    
    # Khoan lỗ bản lề xoay
    knuckle_hole = Part.makeCylinder(hole_r, knuckle_height + 4.0, FreeCAD.Vector(hx, hy, knuckle_z_min - 2.0), FreeCAD.Vector(0, 0, 1))
    chamfer_b = Part.makeCone(hole_r + 0.6, hole_r, 0.6, FreeCAD.Vector(hx, hy, knuckle_z_min), FreeCAD.Vector(0, 0, 1))
    chamfer_t = Part.makeCone(hole_r, hole_r + 0.6, 0.6, FreeCAD.Vector(hx, hy, knuckle_z_max - 0.6), FreeCAD.Vector(0, 0, 1))
    
    # Khoang âm đặt cảm biến Velostat: 9.5mm x 6.8mm x 1.2mm
    pocket_len = min(6.8, knuckle_height - 0.6)
    sensor_cut = Part.makeBox(9.5, 1.3, pocket_len, FreeCAD.Vector(-4.75, -r_in + 0.2, knuckle_z_min + 0.3))
    
    arm_final = arm_raw.cut(knuckle_hole).cut(chamfer_b).cut(chamfer_t).cut(sensor_cut).removeSplitter()
    
    # Tạo tư thế in FDM mở -100 độ
    arm_open_100 = arm_final.copy()
    arm_open_100.rotate(FreeCAD.Vector(hx, hy, 0), FreeCAD.Vector(0, 0, 1), -100.0)
    
    compound_open = Part.Compound([dorsal_final, arm_open_100])
    compound_closed = Part.Compound([dorsal_final, arm_final])
    
    return dorsal_final, arm_final, compound_open, compound_closed

# ==============================================================================
# DỰNG BỘ 3 ĐỐT NGÓN TAY ĐA NẤC
# ==============================================================================
print("--> Dựng Đốt 1 (Proximal) - 5 nấc to nhỏ, 4 nấc dài ngắn...")
d1, a1, pip_open1, pip_closed1 = build_phalanx_multistep(
    r_in=11.8, length_z=16.0, is_distal=False, has_front_joint=True, has_rear_joint=True,
    num_length_steps=4, step_pitch=2.0, front_joint_y=12.5, rear_joint_y=12.5,
    fork_x_gap=8.2, tongue_x_width=5.2, rear_pin_reach=7.5
)

print("--> Dựng Đốt 2 (Middle) - 5 nấc to nhỏ, 4 nấc dài ngắn...")
d2, a2, pip_open2, pip_closed2 = build_phalanx_multistep(
    r_in=10.8, length_z=13.5, is_distal=False, has_front_joint=True, has_rear_joint=True,
    num_length_steps=4, step_pitch=2.0, front_joint_y=11.5, rear_joint_y=12.5,
    fork_x_gap=7.8, tongue_x_width=5.2, rear_pin_reach=8.0
)

print("--> Dựng Đốt 3 (Distal HỞ ĐẦU) - 5 nấc to nhỏ, tai sau ôm chốt...")
d3, a3, pip_open3, pip_closed3 = build_phalanx_multistep(
    r_in=9.8, length_z=11.5, is_distal=True, has_front_joint=False, has_rear_joint=True,
    rear_joint_y=11.5, tongue_x_width=4.8, rear_pin_reach=7.5
)

# ==============================================================================
# CHỐT TRỤC NGANG LIÊN KẾT (Hinge Pin phi 2.4mm)
# ==============================================================================
print("--> Dựng Chốt trục ngang liên kết đa nấc (Intersegment Hinge Pin)...")
pin_head = Part.makeCylinder(2.2, 1.4, FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(1, 0, 0))
pin_shaft = Part.makeCylinder(1.2, 17.5, FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(1, 0, 0))
pin_barb = Part.makeCone(1.4, 1.0, 1.5, FreeCAD.Vector(16.0, 0, 0), FreeCAD.Vector(1, 0, 0))
inter_pin = pin_head.fuse(pin_shaft).fuse(pin_barb).removeSplitter()

# ==============================================================================
# TẠO CỤM LẮP RÁP 3 ĐỐT ĐA NẤC (NOMINAL POSITION - NẤC 2 TIÊU CHUẨN)
# ==============================================================================
# Đốt 1 từ Z = 0 đến 16.0mm. Nấc PIP bắt đầu từ Z = 18.5mm, bước 2.0mm.
# Nấc 2 (Medium standard): Z = 18.5 + 1 * 2.0 = 20.5mm
pip_pin_z = 20.5
p2_base_z = pip_pin_z - (-8.0) # Z = 28.5mm

# Đốt 2 từ Z = 28.5 đến 42.0mm. Nấc DIP bắt đầu từ local Z = 16.0mm (global Z = 44.5mm).
# Nấc 2 DIP: global Z = 44.5 + 1 * 2.0 = 46.5mm
dip_pin_z = 46.5
p3_base_z = dip_pin_z - (-7.5) # Z = 54.0mm

pip_closed1_placed = pip_closed1.copy()

pip_closed2_placed = pip_closed2.copy()
pip_closed2_placed.translate(FreeCAD.Vector(0, 0, p2_base_z))

pip_closed3_placed = pip_closed3.copy()
pip_closed3_placed.translate(FreeCAD.Vector(0, 0, p3_base_z))

pin_pip = inter_pin.copy()
pin_pip.translate(FreeCAD.Vector(-8.5, 12.5, pip_pin_z))

pin_dip = inter_pin.copy()
pin_dip.translate(FreeCAD.Vector(-8.5, 11.5, dip_pin_z))

full_finger_straight = Part.Compound([pip_closed1_placed, pip_closed2_placed, pip_closed3_placed, pin_pip, pin_dip])

# CỤM LẮP RÁP GẬP ÔM NẮM (FLEXED GRASPING ASSEMBLY Ở NẤC 2)
pip_closed2_flex = pip_closed2.copy()
pip_closed2_flex.rotate(FreeCAD.Vector(0, 12.5, -8.0), FreeCAD.Vector(1, 0, 0), 35.0)
pip_closed2_flex.translate(FreeCAD.Vector(0, 0, p2_base_z))

# Đốt 3 gập 75 độ tổng cộng
pip_closed3_flex = pip_closed3.copy()
pip_closed3_flex.rotate(FreeCAD.Vector(0, 11.5, -7.5), FreeCAD.Vector(1, 0, 0), 75.0)
pip_closed3_flex.translate(FreeCAD.Vector(0, 0, p3_base_z - 3.5))

full_finger_flexed = Part.Compound([pip_closed1_placed, pip_closed2_flex, pip_closed3_flex])

# ==============================================================================
# XUẤT CÁC FILE STL VÀ STEP
# ==============================================================================
print("--> Xuất file STL và STEP...")

# 1. Từng part ở tư thế mở -100 độ (Sẵn sàng in 3D FDM Print-in-Place)
pip_open1.exportStl(os.path.join(OUT_DIR, "phalanx1_proximal_open.stl"))
pip_open1.exportStep(os.path.join(OUT_DIR, "phalanx1_proximal_open.step"))

pip_open2.exportStl(os.path.join(OUT_DIR, "phalanx2_middle_open.stl"))
pip_open2.exportStep(os.path.join(OUT_DIR, "phalanx2_middle_open.step"))

pip_open3.exportStl(os.path.join(OUT_DIR, "phalanx3_distal_open.stl"))
pip_open3.exportStep(os.path.join(OUT_DIR, "phalanx3_distal_open.step"))

# 2. Chốt trục ngang
inter_pin.exportStl(os.path.join(OUT_DIR, "intersegment_hinge_pin_2_5mm.stl"))
inter_pin.exportStep(os.path.join(OUT_DIR, "intersegment_hinge_pin_2_5mm.step"))

# 3. Cụm lắp ráp hoàn chỉnh duỗi thẳng & gập
full_finger_straight.exportStl(os.path.join(OUT_DIR, "full_finger_assembly_straight.stl"))
full_finger_straight.exportStep(os.path.join(OUT_DIR, "full_finger_assembly_straight.step"))

full_finger_flexed.exportStl(os.path.join(OUT_DIR, "full_finger_assembly_flexed.stl"))
full_finger_flexed.exportStep(os.path.join(OUT_DIR, "full_finger_assembly_flexed.step"))

# 4. Lưu file FreeCAD
doc.addObject("Part::Feature", "Phalanx1_Proximal_Open").Shape = pip_open1
doc.addObject("Part::Feature", "Phalanx2_Middle_Open").Shape = pip_open2
doc.addObject("Part::Feature", "Phalanx3_Distal_Open").Shape = pip_open3
doc.addObject("Part::Feature", "IntersegmentPin").Shape = inter_pin
doc.addObject("Part::Feature", "FullFingerStraight").Shape = full_finger_straight
doc.addObject("Part::Feature", "FullFingerFlexed").Shape = full_finger_flexed
doc.recompute()
doc.saveAs(os.path.join(OUT_DIR, "full_finger_modular.FCStd"))

print("=== HOÀN TẤT TẠO TOÀN BỘ FILE 3D ĐA NẤC THÀNH CÔNG! ===")
