import sys
import os
import io
import math

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import FreeCAD
import Part
import Mesh

OUT_DIR = r"D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\3d_model\custom_exo\full_finger_modular"
os.makedirs(OUT_DIR, exist_ok=True)

doc = FreeCAD.newDocument("FullFingerSlotted")

print("=== KIỂM TRA THIẾT KẾ KHỚP RÃNH TRƯỢT TỰ LỰA (OPTION 1: FLOATING SLOTTED JOINT) ===")

def make_slot_cutter(r_slot, length_slot, p_start, dir_slot, dir_pin):
    c1 = Part.makeCylinder(r_slot, 24.0, p_start - dir_pin * 12.0, dir_pin)
    p_end = p_start + dir_slot * length_slot
    c2 = Part.makeCylinder(r_slot, 24.0, p_end - dir_pin * 12.0, dir_pin)
    b = Part.makeBox(24.0, 2 * r_slot, length_slot, p_start - dir_pin * 12.0 - FreeCAD.Vector(0, r_slot, 0))
    return c1.fuse(c2).fuse(b).removeSplitter()

def build_phalanx_slotted(r_in, length_z, is_distal=False, has_front_joint=True, has_rear_joint=True,
                          front_slot_len=7.0, front_joint_y=12.5, rear_joint_y=12.5,
                          fork_x_gap=6.8, tongue_x_width=5.4):
    shell_thick = 2.2
    hx = -(r_in + shell_thick + 0.5)
    hy = -2.2
    pin_r = 1.4
    gap_radial = 0.35
    hole_r = pin_r + gap_radial
    
    # 1. DORSAL SHELL
    outer_cyl = Part.makeCylinder(r_in + shell_thick, length_z, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1))
    inner_cyl = Part.makeCylinder(r_in, length_z + 4.0, FreeCAD.Vector(0,0,-2.0), FreeCAD.Vector(0,0,1))
    shell_tube = outer_cyl.cut(inner_cyl)
    
    cutter_bottom = Part.makeBox(60.0, 30.0, length_z + 4.0, FreeCAD.Vector(-30.0, -30.0, -2.0))
    dorsal_base = shell_tube.cut(cutter_bottom)
    
    knuckle_z_min = 2.8
    knuckle_z_max = length_z - 2.8
    knuckle_height = knuckle_z_max - knuckle_z_min
    
    arm_swing_cut = Part.makeCylinder(hole_r + 1.8, knuckle_height + 0.8, FreeCAD.Vector(hx, hy, knuckle_z_min - 0.4), FreeCAD.Vector(0,0,1))
    dorsal_base = dorsal_base.cut(arm_swing_cut)
    
    lug_outer = Part.makeCylinder(pin_r + 1.2, length_z, FreeCAD.Vector(hx, hy, 0.0), FreeCAD.Vector(0,0,1))
    lug_slot_cut = Part.makeBox(14.0, 14.0, knuckle_height + 0.8, FreeCAD.Vector(hx - 7.0, hy - 7.0, knuckle_z_min - 0.4))
    lug_fork = lug_outer.cut(lug_slot_cut)
    lug_bridge = Part.makeBox(4.5, 3.5, length_z, FreeCAD.Vector(hx, hy, 0.0)).cut(lug_slot_cut)
    hinge_pin_int = Part.makeCylinder(pin_r, length_z, FreeCAD.Vector(hx, hy, 0.0), FreeCAD.Vector(0,0,1))
    
    rx = r_in + 1.7
    ratchet_base = Part.makeBox(2.2, 4.5, length_z, FreeCAD.Vector(rx, 0.0, 0.0))
    groove_step1 = Part.makeBox(2.0, 1.4, length_z + 2.0, FreeCAD.Vector(rx + 0.4, 0.5, -1.0))
    groove_step2 = Part.makeBox(2.0, 1.4, length_z + 2.0, FreeCAD.Vector(rx + 0.4, 2.5, -1.0))
    ratchet_catch = ratchet_base.cut(groove_step1).cut(groove_step2)
    
    # Khuyên neo / luồn gân trên mu ngón
    if is_distal:
        # Hở đầu hoàn toàn, khối neo gân mu ngón có lỗ luồn + hốc chặn cos
        eyelet_out = Part.makeCylinder(3.2, 5.0, FreeCAD.Vector(0, r_in, length_z/2.0), FreeCAD.Vector(0, 1, 0))
        cable_hole = Part.makeCylinder(1.0, length_z + 4.0, FreeCAD.Vector(0, r_in + 2.5, -2.0), FreeCAD.Vector(0, 0, 1))
        cable_stop = Part.makeCylinder(1.7, 6.0, FreeCAD.Vector(0, r_in + 2.5, length_z/2.0), FreeCAD.Vector(0, 0, 1))
        eyelet = eyelet_out.cut(cable_hole).cut(cable_stop)
    else:
        eyelet_out = Part.makeCylinder(3.2, 5.0, FreeCAD.Vector(0, r_in, length_z/2.0), FreeCAD.Vector(0, 1, 0))
        cable_hole = Part.makeCylinder(1.2, length_z + 4.0, FreeCAD.Vector(0, r_in + 2.5, -2.0), FreeCAD.Vector(0, 0, 1))
        eyelet = eyelet_out.cut(cable_hole)
        
    dorsal_solid = dorsal_base.fuse(lug_fork).fuse(lug_bridge).fuse(hinge_pin_int).fuse(ratchet_catch).fuse(eyelet)
    
    # 2. KHỚP LIÊN ĐỐT MU NGÓN CÓ RÃNH TRƯỢT TỰ LỰA (FLOATING SLOTTED JOINT)
    if has_front_joint and not is_distal:
        # Chạc đôi phía trước: vươn dài ra đón tai đốt kế tiếp
        fork_reach = front_slot_len + 6.0  # Chiều dài chạc đủ bao trọn rãnh trượt + thành chặn 3mm
        half_gap = fork_x_gap / 2.0
        fork_thick = 3.0
        
        # 2 tai chạc 2 bên
        f_left = Part.makeBox(fork_thick, 5.5, fork_reach, FreeCAD.Vector(-(half_gap + fork_thick), front_joint_y - 2.75, length_z))
        f_right = Part.makeBox(fork_thick, 5.5, fork_reach, FreeCAD.Vector(half_gap, front_joint_y - 2.75, length_z))
        
        # Cữ chặn duỗi thẳng 0 độ ở mặt lưng (Hyperextension stop ledge)
        # Nằm ở phía trên (Y cao hơn), ngăn không cho tai đốt sau lật ngửa quá 0 độ
        bridge_stop = Part.makeBox(fork_x_gap + 2*fork_thick, 1.6, fork_reach, FreeCAD.Vector(-(half_gap + fork_thick), front_joint_y + 1.15, length_z))
        
        # Tạo rãnh trượt thuôn dài (Slotted track) theo trục Z
        # Rãnh bắt đầu từ Z = length_z + 2.5 đến length_z + 2.5 + front_slot_len
        z_slot_start = length_z + 2.8
        slot_cut = make_slot_cutter(1.35, front_slot_len, FreeCAD.Vector(0, front_joint_y, z_slot_start), 
                                    FreeCAD.Vector(0, 0, 1), FreeCAD.Vector(1, 0, 0))
        
        front_fork = f_left.fuse(f_right).fuse(bridge_stop).cut(slot_cut)
        dorsal_solid = dorsal_solid.fuse(front_fork)
        
    if has_rear_joint:
        # Tai giữa phía sau vươn về -Z để lọt vào chạc của đốt trước
        tongue_reach = 5.0
        tongue_box = Part.makeBox(tongue_x_width, 5.0, tongue_reach, 
                                  FreeCAD.Vector(-tongue_x_width/2.0, rear_joint_y - 2.5, -tongue_reach))
        # Lỗ chốt tròn phi 2.6mm ở Z = -2.5mm
        pin_hole = Part.makeCylinder(1.3, 20.0, FreeCAD.Vector(-10.0, rear_joint_y, -2.5), FreeCAD.Vector(1, 0, 0))
        rear_tongue = tongue_box.cut(pin_hole)
        dorsal_solid = dorsal_solid.fuse(rear_tongue)
        
    dorsal_final = dorsal_solid.removeSplitter()
    
    # 3. PALMAR SWING ARM (Thanh gài bụng ngón)
    knuckle_out = Part.makeCylinder(hole_r + 1.2, knuckle_height, FreeCAD.Vector(hx, hy, knuckle_z_min), FreeCAD.Vector(0, 0, 1))
    arm_bridge = Part.makeBox(4.5, 3.5, knuckle_height, FreeCAD.Vector(hx, hy - 2.0, knuckle_z_min))
    
    arm_out_cyl = Part.makeCylinder(r_in + 1.6, knuckle_height, FreeCAD.Vector(0, 0, knuckle_z_min), FreeCAD.Vector(0, 0, 1))
    arm_in_cyl = Part.makeCylinder(r_in - 0.4, knuckle_height + 2.0, FreeCAD.Vector(0, 0, knuckle_z_min - 1.0), FreeCAD.Vector(0, 0, 1))
    arm_slice = arm_out_cyl.cut(arm_in_cyl)
    arm_bottom = arm_slice.cut(Part.makeBox(60.0, 30.0, 20.0, FreeCAD.Vector(-30.0, -0.6, 0.0)))
    
    snap_arm_out = Part.makeBox(1.6, 6.2, knuckle_height, FreeCAD.Vector(rx + 2.3, -2.0, knuckle_z_min))
    tooth_claw = Part.makeBox(1.4, 1.2, knuckle_height, FreeCAD.Vector(rx + 0.9, 0.6, knuckle_z_min))
    bridge_r = Part.makeBox(3.0, 1.8, knuckle_height, FreeCAD.Vector(rx - 0.5, -1.8, knuckle_z_min))
    thumb_tab = Part.makeBox(3.5, 2.2, knuckle_height, FreeCAD.Vector(rx + 3.3, 1.8, knuckle_z_min))
    latch_claw = snap_arm_out.fuse(tooth_claw).fuse(bridge_r).fuse(thumb_tab)
    
    arm_raw = knuckle_out.fuse(arm_bridge).fuse(arm_bottom).fuse(latch_claw)
    
    knuckle_hole = Part.makeCylinder(hole_r, knuckle_height + 4.0, FreeCAD.Vector(hx, hy, knuckle_z_min - 2.0), FreeCAD.Vector(0, 0, 1))
    chamfer_b = Part.makeCone(hole_r + 0.6, hole_r, 0.6, FreeCAD.Vector(hx, hy, knuckle_z_min), FreeCAD.Vector(0, 0, 1))
    chamfer_t = Part.makeCone(hole_r, hole_r + 0.6, 0.6, FreeCAD.Vector(hx, hy, knuckle_z_max - 0.6), FreeCAD.Vector(0, 0, 1))
    
    sensor_cut = Part.makeBox(9.5, 1.3, min(6.5, knuckle_height - 0.6), FreeCAD.Vector(-4.75, -r_in + 0.2, knuckle_z_min + 0.3))
    
    arm_final = arm_raw.cut(knuckle_hole).cut(chamfer_b).cut(chamfer_t).cut(sensor_cut).removeSplitter()
    
    arm_open_100 = arm_final.copy()
    arm_open_100.rotate(FreeCAD.Vector(hx, hy, 0), FreeCAD.Vector(0, 0, 1), -100.0)
    
    compound_open = Part.Compound([dorsal_final, arm_open_100])
    compound_closed = Part.Compound([dorsal_final, arm_final])
    
    return dorsal_final, arm_final, compound_open, compound_closed

# Dựng 3 đốt:
# Đốt 1 (Proximal): r_in = 11.8, length_z = 18.0, rãnh trượt 7.5mm tại khớp PIP
print('1. Dựng Đốt 1...')
d1, a1, p1_open, p1_closed = build_phalanx_slotted(
    r_in=11.8, length_z=18.0, is_distal=False, has_front_joint=True, has_rear_joint=True,
    front_slot_len=7.5, front_joint_y=12.5, rear_joint_y=12.5, fork_x_gap=6.8, tongue_x_width=5.4
)

# Đốt 2 (Middle): r_in = 10.8, length_z = 15.0, rãnh trượt 6.0mm tại khớp DIP
print('2. Dựng Đốt 2...')
d2, a2, p2_open, p2_closed = build_phalanx_slotted(
    r_in=10.8, length_z=15.0, is_distal=False, has_front_joint=True, has_rear_joint=True,
    front_slot_len=6.0, front_joint_y=11.5, rear_joint_y=12.5, fork_x_gap=6.4, tongue_x_width=5.4
)

# Đốt 3 (Distal): r_in = 9.8, length_z = 12.0, hở đầu
print('3. Dựng Đốt 3...')
d3, a3, p3_open, p3_closed = build_phalanx_slotted(
    r_in=9.8, length_z=12.0, is_distal=True, has_front_joint=False, has_rear_joint=True,
    rear_joint_y=11.5, tongue_x_width=5.0
)

print('Shapes valid:', d1.isValid(), d2.isValid(), d3.isValid(), a1.isValid(), a2.isValid(), a3.isValid())
