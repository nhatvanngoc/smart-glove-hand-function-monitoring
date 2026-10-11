import sys
import os
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import FreeCAD
import Part

print("=== KIỂM TRA ĐOẠN CODE CỦA GEMINI-ROBOTICS ===")

def build_phalanx_lateral_snap(r_in, length_z, is_distal=False, has_front_joint=True, has_rear_joint=True,
                               num_length_steps=3, step_pitch=2.5,
                               rear_reach=7.0):
    shell_thick = 2.0
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
    lug_bridge = Part.makeBox(4.5, 3.5, length_z, FreeCAD.Vector(hx, hy - 2.0, 0.0)).cut(lug_slot_cut)
    hinge_pin_int = Part.makeCylinder(pin_r, length_z, FreeCAD.Vector(hx, hy, 0.0), FreeCAD.Vector(0,0,1))
    
    # Dải răng cưa Ratchet 5 nấc sườn phải (+X)
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
    
    # Khuyên luồn gân / rãnh dây điện mu ngón (+Y)
    if is_distal:
        eyelet_out = Part.makeCylinder(3.2, 5.0, FreeCAD.Vector(0, r_in, length_z/2.0), FreeCAD.Vector(0, 1, 0))
        cable_hole = Part.makeCylinder(1.0, length_z + 4.0, FreeCAD.Vector(0, r_in + 2.5, -2.0), FreeCAD.Vector(0, 0, 1))
        cable_stop = Part.makeCylinder(1.7, 6.0, FreeCAD.Vector(0, r_in + 2.5, length_z/2.0), FreeCAD.Vector(0, 0, 1))
        eyelet = eyelet_out.cut(cable_hole).cut(cable_stop)
    else:
        eyelet_out = Part.makeCylinder(3.2, 5.0, FreeCAD.Vector(0, r_in, length_z/2.0), FreeCAD.Vector(0, 1, 0))
        cable_hole = Part.makeCylinder(1.2, length_z + 4.0, FreeCAD.Vector(0, r_in + 2.5, -2.0), FreeCAD.Vector(0, 0, 1))
        eyelet = eyelet_out.cut(cable_hole)
        
    dorsal_solid = dorsal_base.fuse(lug_fork).fuse(lug_bridge).fuse(hinge_pin_int).fuse(ratchet_catch).fuse(eyelet)
    
    # 2. KHỚP BẤM NGÀM BÊN HÔNG (LATERAL SNAP-PIVOT)
    x_outer = r_in + shell_thick
    
    # KHỚP PHÍA TRƯỚC (2 TAY ĐÒN BÊN HÔNG VƯƠN RA ĐÓN ĐỐT SAU)
    if has_front_joint and not is_distal:
        arm_reach = (num_length_steps - 1) * step_pitch + 5.0
        arm_thick = 2.0
        arm_width_y = 5.6
        x_arm_l = -(x_outer + 0.3 + arm_thick)
        x_arm_r = x_outer + 0.3
        
        arm_box_l = Part.makeBox(arm_thick, arm_width_y, arm_reach, FreeCAD.Vector(x_arm_l, -arm_width_y/2.0, length_z))
        arm_box_r = Part.makeBox(arm_thick, arm_width_y, arm_reach, FreeCAD.Vector(x_arm_r, -arm_width_y/2.0, length_z))
        
        for i in range(num_length_steps):
            z_hole = length_z + 2.5 + i * step_pitch
            h_l = Part.makeCylinder(1.6, arm_thick + 2.0, FreeCAD.Vector(x_arm_l - 1.0, 0, z_hole), FreeCAD.Vector(1, 0, 0))
            h_r = Part.makeCylinder(1.6, arm_thick + 2.0, FreeCAD.Vector(x_arm_r - 1.0, 0, z_hole), FreeCAD.Vector(1, 0, 0))
            lead_l = Part.makeCone(1.6, 2.3, 0.8, FreeCAD.Vector(x_arm_l + arm_thick + 0.1, 0, z_hole), FreeCAD.Vector(-1, 0, 0))
            lead_r = Part.makeCone(1.6, 2.3, 0.8, FreeCAD.Vector(x_arm_r - 0.1, 0, z_hole), FreeCAD.Vector(1, 0, 0))
            
            arm_box_l = arm_box_l.cut(h_l).cut(lead_l)
            arm_box_r = arm_box_r.cut(h_r).cut(lead_r)
            
        dorsal_solid = dorsal_solid.fuse(arm_box_l).fuse(arm_box_r)
        
    # KHỚP PHÍA SAU (2 CHỐT TRÒN LỒI HƯỚNG RA NGOÀI)
    if has_rear_joint:
        lug_thick = 2.0
        lug_width_y = 5.2
        lug_reach = rear_reach + 2.5
        x_lug_l = -x_outer
        x_lug_r = x_outer - lug_thick
        
        lug_box_l = Part.makeBox(lug_thick, lug_width_y, lug_reach, FreeCAD.Vector(x_lug_l, -lug_width_y/2.0, -lug_reach))
        lug_box_r = Part.makeBox(lug_thick, lug_width_y, lug_reach, FreeCAD.Vector(x_lug_r, -lug_width_y/2.0, -lug_reach))
        
        z_stud = -rear_reach
        stud_l = Part.makeCylinder(1.5, 1.8, FreeCAD.Vector(x_lug_l, 0, z_stud), FreeCAD.Vector(-1, 0, 0))
        stud_r = Part.makeCylinder(1.5, 1.8, FreeCAD.Vector(x_lug_r + lug_thick, 0, z_stud), FreeCAD.Vector(1, 0, 0))
        
        cone_l = Part.makeCone(1.5, 1.0, 0.6, FreeCAD.Vector(x_lug_l - 1.2, 0, z_stud), FreeCAD.Vector(-1, 0, 0))
        cone_r = Part.makeCone(1.5, 1.0, 0.6, FreeCAD.Vector(x_lug_r + lug_thick + 1.2, 0, z_stud), FreeCAD.Vector(1, 0, 0))
        stud_l = stud_l.cut(cone_l)
        stud_r = stud_r.cut(cone_r)
        
        dorsal_solid = dorsal_solid.fuse(lug_box_l).fuse(lug_box_r).fuse(stud_l).fuse(stud_r)
        
    dorsal_final = dorsal_solid.removeSplitter()
    
    # ==============================================================================
    # 3. COMPLIANT PALMAR SWING ARM (Thanh gài bụng ngón cánh cung 2 khớp dẻo)
    # ==============================================================================
    knuckle_out = Part.makeCylinder(hole_r + 1.2, knuckle_height, FreeCAD.Vector(hx, hy, knuckle_z_min), FreeCAD.Vector(0, 0, 1))
    arm_bridge = Part.makeBox(4.5, 3.5, knuckle_height, FreeCAD.Vector(hx, hy - 2.0, knuckle_z_min))
    
    # 3.1 ĐẾ CẢM BIẾN CỨNG VỮNG (Rigid Sensor Pad): Phẳng, chịu tải lực tì cảm biến ổn định
    pad_w = 10.0
    pad_thick = 2.4
    sensor_pad = Part.makeBox(pad_w, pad_thick, knuckle_height, FreeCAD.Vector(-pad_w/2.0, -r_in - pad_thick, knuckle_z_min))
    
    # 3.2 CÁNH CUNG ĐÀN HỒI TRÁI (Left Flexure Strap - dày 1.1mm): Giúp tịnh tiến thu hẹp bán kính
    strap_l_out = Part.makeCylinder(r_in + 1.1, knuckle_height, FreeCAD.Vector(0, 0, knuckle_z_min), FreeCAD.Vector(0, 0, 1))
    strap_l_in = Part.makeCylinder(r_in, knuckle_height + 2.0, FreeCAD.Vector(0, 0, knuckle_z_min - 1.0), FreeCAD.Vector(0, 0, 1))
    strap_l_slice = strap_l_out.cut(strap_l_in)
    strap_l = strap_l_slice.cut(Part.makeBox(60.0, 60.0, 20.0, FreeCAD.Vector(-4.8, -30.0, 0.0))) # Cắt giữ bên trái
    
    # 3.3 CÁNH CUNG ĐÀN HỒI PHẢI (Right Flexure Strap - dày 1.1mm): Đàn hồi cho ngàm sập bám răng cưa
    strap_r_out = Part.makeCylinder(r_in + 1.1, knuckle_height, FreeCAD.Vector(0, 0, knuckle_z_min), FreeCAD.Vector(0, 0, 1))
    strap_r_in = Part.makeCylinder(r_in, knuckle_height + 2.0, FreeCAD.Vector(0, 0, knuckle_z_min - 1.0), FreeCAD.Vector(0, 0, 1))
    strap_r_slice = strap_r_out.cut(strap_r_in)
    strap_r = strap_r_slice.cut(Part.makeBox(60.0, 60.0, 20.0, FreeCAD.Vector(-60.0 - 4.8, -30.0, 0.0))) # Cắt giữ bên phải
    
    # 3.4 NGÀM MỎ QUẠ ĐA NẤC (Ratchet Claw Block)
    snap_arm_out = Part.makeBox(1.6, rack_len_y + 1.8, knuckle_height, FreeCAD.Vector(rx + 2.4, -2.0, knuckle_z_min))
    tooth_claw = Part.makeBox(1.5, 1.0, knuckle_height, FreeCAD.Vector(rx + 0.9, 0.5, knuckle_z_min))
    thumb_tab = Part.makeBox(3.8, 2.4, knuckle_height, FreeCAD.Vector(rx + 3.4, rack_len_y - 0.6, knuckle_z_min))
    
    # Gộp toàn bộ thanh gài dẻo nguyên khối
    print("Fusing arm pieces...")
    arm_raw = knuckle_out.fuse(arm_bridge).fuse(strap_l).fuse(sensor_pad).fuse(strap_r).fuse(snap_arm_out).fuse(tooth_claw).fuse(thumb_tab)
    print("Arm pieces fused successfully, Volume =", arm_raw.Volume)
    
    # Khoan lỗ bản lề xoay
    knuckle_hole = Part.makeCylinder(hole_r, knuckle_height + 4.0, FreeCAD.Vector(hx, hy, knuckle_z_min - 2.0), FreeCAD.Vector(0, 0, 1))
    chamfer_b = Part.makeCone(hole_r + 0.6, hole_r, 0.6, FreeCAD.Vector(hx, hy, knuckle_z_min), FreeCAD.Vector(0, 0, 1))
    chamfer_t = Part.makeCone(hole_r, hole_r + 0.6, 0.6, FreeCAD.Vector(hx, hy, knuckle_z_max - 0.6), FreeCAD.Vector(0, 0, 1))
    
    # Khoang âm đặt cảm biến Velostat: Phẳng, sạch 100% trong lòng búp ngón tay
    pocket_len = min(6.8, knuckle_height - 0.6)
    sensor_cut = Part.makeBox(9.5, 1.3, pocket_len, FreeCAD.Vector(-4.75, -r_in - 1.2, knuckle_z_min + 0.3))
    
    arm_final = arm_raw.cut(knuckle_hole).cut(chamfer_b).cut(chamfer_t).cut(sensor_cut).removeSplitter()
    print("Arm final Volume =", arm_final.Volume)
    
    # Tư thế in FDM mở -100 độ
    arm_open_100 = arm_final.copy()
    arm_open_100.rotate(FreeCAD.Vector(hx, hy, 0), FreeCAD.Vector(0, 0, 1), -100.0)
    
    compound_open = Part.Compound([dorsal_final, arm_open_100])
    compound_closed = Part.Compound([dorsal_final, arm_final])
    
    return dorsal_final, arm_final, compound_open, compound_closed

doc = FreeCAD.newDocument("TestGeminiCode")
d, a, co, cc = build_phalanx_lateral_snap(r_in=11.8, length_z=16.0)
print("SUCCESS: Model built with volume dorsal =", d.Volume, ", arm =", a.Volume)
