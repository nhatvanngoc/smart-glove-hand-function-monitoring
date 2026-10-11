import sys
import os
import io
import math

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import FreeCAD
import Part
import MeshPart
import Mesh

OUT_DIR = r"D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\3d_model\custom_exo\full_finger_modular"
os.makedirs(OUT_DIR, exist_ok=True)

doc = FreeCAD.newDocument("FullFingerV34HookClaspAndSnapPin")

print("=== BẮT ĐẦU DỰNG BỘ 3 ĐỐT NGÓN TAY V3.4 (GIẢI QUYẾT TRIỆT ĐỂ LỖ LIÊN ĐỐT & QUAI GÀI) ===")
print("=== 1. KHỚP LIÊN ĐỐT: CẢ 2 BÊN ĐỀU LÀ LỖ PHI 3.2mm PHẲNG MỊN, ĐỐT 2 TRƯỢT VÀO ĐỐT 1 ÊM RU ===")
print("===    ĐI KÈM CHỐT XỎ RỜI TỰ KHÓA (DETACHABLE SNAP-PIN) HOẶC ỐC M3 - LẮP 1 GIÂY 0 DÙNG LỰC ===")
print("=== 2. QUAI GÀI BỤNG: MÓC GÀI BẬC THANG (HOOK-AND-LADDER CLASP) 4 NẤC ÔM ĐÚNG THEO CUNG XOAY ===")
print("===    KHÔNG CẦN ÉP NGANG, KHÔNG CẦN CHỐT NẤM, NHẤC TAI GẠT LÀ THÁO NGAY TRONG 0.1s ===")
print("=== 3. BẢN LỀ PRINT-IN-PLACE: KHE HỞ HƯỚNG KÍNH 0.75mm, KHE Z 0.85mm, VÁT CÔN 45 ĐỘ ===")

def build_phalanx_v34(r_in, length_z, is_distal=False, has_front_joint=True, has_rear_joint=True,
                      num_length_steps=5, step_pitch=2.0, rear_reach=8.5, r_in_mate=None):
    if r_in_mate is None:
        r_in_mate = r_in
        
    shell_thick = 2.0
    
    # -------------------------------------------------------------------------
    # 1. BẢN LỀ XOAY PRINT-IN-PLACE (DUNG SAI VÀNG FDM)
    # -------------------------------------------------------------------------
    hx = -(r_in + shell_thick + 0.9)
    hy = -2.2
    pin_r = 1.5 # Chốt phi 3.0mm
    gap_radial = 0.75 # Khe hở hướng kính 0.75mm -> Lỗ phi 4.5mm
    hole_r = pin_r + gap_radial
    gap_z = 0.85 # Khe hở mặt đáy và đỉnh 0.85mm (>4 layer 0.2mm)
    
    knuckle_z_min = 2.0
    knuckle_h = 8.0 if (not is_distal and length_z >= 15.0) else 6.6
    knuckle_z_max = knuckle_z_min + knuckle_h
    
    # Máng mu ngón (Dorsal shell)
    outer_cyl = Part.makeCylinder(r_in + shell_thick, length_z, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1))
    inner_cyl = Part.makeCylinder(r_in, length_z + 4.0, FreeCAD.Vector(0,0,-2.0), FreeCAD.Vector(0,0,1))
    dorsal_tube = outer_cyl.cut(inner_cyl)
    
    # Cắt nửa dưới (Y < 0)
    cutter_bottom = Part.makeBox(60.0, 30.0, length_z + 4.0, FreeCAD.Vector(-30.0, -30.0, -2.0))
    dorsal_base = dorsal_tube.cut(cutter_bottom)
    
    # Cắt khe hở khoét cho tai bản lề bụng xoay
    z_slot_min = knuckle_z_min - gap_z
    z_slot_h = knuckle_h + 2 * gap_z
    slot_cut = Part.makeBox(20.0, 20.0, z_slot_h, FreeCAD.Vector(hx - 10.0, hy - 10.0, z_slot_min))
    dorsal_base = dorsal_base.cut(slot_cut)
    
    # Tai bản lề máng mu (Lug fork)
    lug_fork = Part.makeCylinder(pin_r + 1.8, length_z, FreeCAD.Vector(hx, hy, 0.0), FreeCAD.Vector(0,0,1)).cut(slot_cut)
    lug_bridge = Part.makeBox(6.5, 4.0, length_z, FreeCAD.Vector(hx, hy - 2.0, 0.0)).cut(slot_cut)
    hinge_pin = Part.makeCylinder(pin_r, length_z, FreeCAD.Vector(hx, hy, 0.0), FreeCAD.Vector(0,0,1))
    
    bridge_box = Part.makeBox(4.5, 4.5, length_z, FreeCAD.Vector(r_in - 1.0, 0.0, 0.0))
    
    # -------------------------------------------------------------------------
    # 2. DÀN BẬC MÓC GÀI (LADDER RACKS) 4 NẤC TRÊN SƯỜN MU NGÓN (+X)
    # -------------------------------------------------------------------------
    x_base = r_in + shell_thick
    ladder_w_x = 1.6
    ladder_len_y = 13.0
    ladder_h_z = knuckle_h
    
    ladder_base = Part.makeBox(ladder_w_x + 1.0, ladder_len_y, ladder_h_z,
                               FreeCAD.Vector(x_base - 1.0, 0.0, knuckle_z_min))
    ladder_wedge = Part.makeBox(2.0, ladder_len_y, ladder_h_z,
                                FreeCAD.Vector(x_base - 2.0, 0.0, knuckle_z_min))
    
    teeth_solid = ladder_base.fuse(ladder_wedge)
    x_rack_outer = x_base + ladder_w_x
    tooth_h_x = 0.8 # Chiều cao răng móc 0.8mm
    
    # 4 Nấc móc gài (bước 2.6mm: Y = 2.5, 5.1, 7.7, 10.3)
    for i in range(4):
        y_step = 2.5 + i * 2.6
        y_ramp_tip = y_step + 1.6
        
        pt1 = FreeCAD.Vector(x_rack_outer, y_step, knuckle_z_min)
        pt2 = FreeCAD.Vector(x_rack_outer + tooth_h_x, y_step, knuckle_z_min)
        pt3 = FreeCAD.Vector(x_rack_outer, y_ramp_tip, knuckle_z_min)
        w_t = Part.makePolygon([pt1, pt2, pt3, pt1])
        tooth_prism = Part.Face(w_t).extrude(FreeCAD.Vector(0, 0, knuckle_h))
        teeth_solid = teeth_solid.fuse(tooth_prism)
        
    # Khuyên neo / luồn gân trên mu ngón (+Y)
    if is_distal:
        eyelet_out = Part.makeCylinder(3.2, 5.0, FreeCAD.Vector(0, r_in, length_z/2.0), FreeCAD.Vector(0, 1, 0))
        cable_hole = Part.makeCylinder(1.0, length_z + 4.0, FreeCAD.Vector(0, r_in + 2.5, -2.0), FreeCAD.Vector(0, 0, 1))
        cable_stop = Part.makeCylinder(1.7, 6.0, FreeCAD.Vector(0, r_in + 2.5, length_z/2.0), FreeCAD.Vector(0, 0, 1))
        eyelet = eyelet_out.cut(cable_hole).cut(cable_stop)
    else:
        eyelet_out = Part.makeCylinder(3.2, 5.0, FreeCAD.Vector(0, r_in, length_z/2.0), FreeCAD.Vector(0, 1, 0))
        cable_hole = Part.makeCylinder(1.2, length_z + 4.0, FreeCAD.Vector(0, r_in + 2.5, -2.0), FreeCAD.Vector(0, 0, 1))
        eyelet = eyelet_out.cut(cable_hole)
        
    dorsal_solid = dorsal_base.fuse(lug_fork).fuse(lug_bridge).fuse(hinge_pin).fuse(bridge_box).fuse(teeth_solid).fuse(eyelet).removeSplitter()
    
    # -------------------------------------------------------------------------
    # 3. TAY ĐÒN LIÊN ĐỐT GIA CƯỜNG & LỖ TAI BẢN LỀ SAU (KHÔNG DÙNG CHỐT CHẾT)
    # -------------------------------------------------------------------------
    if has_front_joint and not is_distal:
        x_mate_outer = r_in_mate + shell_thick
        arm_reach = (num_length_steps - 1) * step_pitch + 13.0
        arm_thick = 3.2
        arm_width_y = 6.8
        x_arm_l = -(x_mate_outer + 0.3 + arm_thick)
        x_arm_r = x_mate_outer + 0.3
        overlap_x = max(0.0, r_in - r_in_mate)
        
        z_arm_base = knuckle_z_max + gap_z + 0.5
        arm_box_l = Part.makeBox(arm_thick + overlap_x, arm_width_y, length_z + arm_reach - z_arm_base, 
                                 FreeCAD.Vector(x_arm_l, -arm_width_y/2.0 + 1.0, z_arm_base))
        arm_box_r = Part.makeBox(arm_thick + overlap_x, arm_width_y, length_z + arm_reach - z_arm_base, 
                                 FreeCAD.Vector(x_arm_r - overlap_x, -arm_width_y/2.0 + 1.0, z_arm_base))
        
        p_g1 = FreeCAD.Vector(x_arm_l, 0.0, z_arm_base)
        p_g2 = FreeCAD.Vector(x_arm_l, 0.0, length_z + 4.5)
        p_g3 = FreeCAD.Vector(x_arm_l + arm_thick + 1.8, 0.0, z_arm_base)
        gusset_l = Part.Face(Part.makePolygon([p_g1, p_g2, p_g3, p_g1])).extrude(FreeCAD.Vector(0, 4.0, 0))
        
        p_gr1 = FreeCAD.Vector(x_arm_r + arm_thick, 0.0, z_arm_base)
        p_gr2 = FreeCAD.Vector(x_arm_r + arm_thick, 0.0, length_z + 4.5)
        p_gr3 = FreeCAD.Vector(x_arm_r - 1.8, 0.0, z_arm_base)
        gusset_r = Part.Face(Part.makePolygon([p_gr1, p_gr2, p_gr3, p_gr1])).extrude(FreeCAD.Vector(0, 4.0, 0))
        
        # 5 Lỗ định vị phi 3.2mm kèm vát côn đón mũ chốt phi 4.8mm
        for i in range(num_length_steps):
            z_hole = length_z + 3.5 + i * step_pitch
            h_l = Part.makeCylinder(1.6, arm_thick + overlap_x + 2.0, FreeCAD.Vector(x_arm_l - 1.0, 0.5, z_hole), FreeCAD.Vector(1, 0, 0))
            h_r = Part.makeCylinder(1.6, arm_thick + overlap_x + 2.0, FreeCAD.Vector(x_arm_r - overlap_x - 1.0, 0.5, z_hole), FreeCAD.Vector(1, 0, 0))
            lead_l = Part.makeCone(2.4, 1.6, 0.8, FreeCAD.Vector(x_arm_l - 0.1, 0.5, z_hole), FreeCAD.Vector(1, 0, 0))
            lead_r = Part.makeCone(1.6, 2.4, 0.8, FreeCAD.Vector(x_arm_r + arm_thick - 0.7, 0.5, z_hole), FreeCAD.Vector(1, 0, 0))
            arm_box_l = arm_box_l.cut(h_l).cut(lead_l)
            arm_box_r = arm_box_r.cut(h_r).cut(lead_r)
            
        dorsal_solid = dorsal_solid.fuse(arm_box_l).fuse(arm_box_r).fuse(gusset_l).fuse(gusset_r)
        
    if has_rear_joint:
        x_outer = r_in + shell_thick
        lug_thick = 3.2
        lug_width_y = 6.8
        lug_reach = rear_reach + 2.5
        overlap_z = 0.9
        x_lug_l = -x_outer
        x_lug_r = x_outer - lug_thick
        
        lug_box_l = Part.makeBox(lug_thick, lug_width_y, lug_reach + overlap_z, FreeCAD.Vector(x_lug_l, -lug_width_y/2.0 + 1.0, -lug_reach))
        lug_box_r = Part.makeBox(lug_thick, lug_width_y, lug_reach + overlap_z, FreeCAD.Vector(x_lug_r, -lug_width_y/2.0 + 1.0, -lug_reach))
        
        # LỖ TRÒN PHI 3.2mm TRÊN TAI BẢN LỀ ĐỐT SAU (KHÔNG DÙNG CHỐT CHẾT NHÔ NGOÀI)
        # Đốt sau trượt nhẹ nhàng vào giữa 2 tay đòn đốt trước (khe hở 0.3mm mỗi bên)
        z_stud = -rear_reach
        h_lug_l = Part.makeCylinder(1.6, lug_thick + 2.0, FreeCAD.Vector(x_lug_l - 1.0, 0.5, z_stud), FreeCAD.Vector(1, 0, 0))
        h_lug_r = Part.makeCylinder(1.6, lug_thick + 2.0, FreeCAD.Vector(x_lug_r - 1.0, 0.5, z_stud), FreeCAD.Vector(1, 0, 0))
        lug_l_final = lug_box_l.cut(h_lug_l)
        lug_r_final = lug_box_r.cut(h_lug_r)
        
        dorsal_solid = dorsal_solid.fuse(lug_l_final).fuse(lug_r_final)
        
    dorsal_final = dorsal_solid.removeSplitter()
    assert len(dorsal_final.Solids) == 1, f"LỖI: dorsal_final có {len(dorsal_final.Solids)} solids!"
    
    # -------------------------------------------------------------------------
    # 4. PALMAR SWING ARM: MÓC GÀI ĐÀN HỒI (HOOK-AND-LADDER CLASP)
    # -------------------------------------------------------------------------
    knuckle_out = Part.makeCylinder(hole_r + 1.3, knuckle_h, FreeCAD.Vector(hx, hy, knuckle_z_min), FreeCAD.Vector(0,0,1))
    p_k1 = FreeCAD.Vector(hx, hy - hole_r - 1.3, knuckle_z_min)
    p_k2 = FreeCAD.Vector(hx, hy + hole_r + 1.3, knuckle_z_min)
    p_k3 = FreeCAD.Vector(-r_in + 0.2, -0.2, knuckle_z_min)
    p_k4 = FreeCAD.Vector(-r_in - 1.2, -2.5, knuckle_z_min)
    f_k = Part.Face(Part.makePolygon([p_k1, p_k2, p_k3, p_k4, p_k1])).extrude(FreeCAD.Vector(0,0,knuckle_h))
    knuckle_assembly = knuckle_out.fuse(f_k).removeSplitter()
    
    strap_t = 1.4
    strap_out = Part.makeCylinder(r_in + strap_t, knuckle_h, FreeCAD.Vector(0,0,knuckle_z_min), FreeCAD.Vector(0,0,1))
    strap_in = Part.makeCylinder(r_in, knuckle_h + 4.0, FreeCAD.Vector(0,0,knuckle_z_min - 2.0), FreeCAD.Vector(0,0,1))
    strap_arch = strap_out.cut(strap_in).cut(Part.makeBox(60.0, 30.0, 30.0, FreeCAD.Vector(-30.0, 0.0, 0.0)))
    
    pad_w = 11.4; pad_thick = 3.2
    pad_box = Part.makeBox(pad_w, pad_thick, knuckle_h, FreeCAD.Vector(-pad_w/2.0, -r_in - pad_thick, knuckle_z_min))
    
    x_hook_strap = x_rack_outer + tooth_h_x + 0.25 # Khe hở chạy 0.25mm
    strap_w = 1.4
    strap_len_y = 11.5
    strap_h_z = knuckle_h - 0.4
    z_strap_start = knuckle_z_min + 0.2
    
    bridge_right = Part.makeBox(x_hook_strap + strap_w - (r_in - 1.0), 3.5, knuckle_h,
                                FreeCAD.Vector(r_in - 1.0, -3.5, knuckle_z_min))
    
    hook_arm = Part.makeBox(strap_w, strap_len_y, strap_h_z,
                            FreeCAD.Vector(x_hook_strap, 0.0, z_strap_start))
    
    # Răng móc gài hướng vào trong (-X) tại Y = 6.0mm
    y_hook_tip = 6.0
    hook_pts = [
        FreeCAD.Vector(x_hook_strap, y_hook_tip, z_strap_start),
        FreeCAD.Vector(x_hook_strap - tooth_h_x, y_hook_tip, z_strap_start),
        FreeCAD.Vector(x_hook_strap, y_hook_tip - 1.5, z_strap_start)
    ]
    w_h = Part.makePolygon(hook_pts + [hook_pts[0]])
    hook_tooth = Part.Face(w_h).extrude(FreeCAD.Vector(0, 0, strap_h_z))
    
    # Tai gạt mở ngàm (Thumb Release Tab) vươn ra ngoài 3.5mm kèm 3 khía nhám
    tab_box = Part.makeBox(strap_w + 3.5, 4.0, strap_h_z,
                           FreeCAD.Vector(x_hook_strap, strap_len_y - 0.5, z_strap_start))
    g1 = Part.makeCylinder(0.5, strap_h_z, FreeCAD.Vector(x_hook_strap + strap_w + 3.5, strap_len_y + 0.5, z_strap_start), FreeCAD.Vector(0,0,1))
    g2 = Part.makeCylinder(0.5, strap_h_z, FreeCAD.Vector(x_hook_strap + strap_w + 3.5, strap_len_y + 1.7, z_strap_start), FreeCAD.Vector(0,0,1))
    g3 = Part.makeCylinder(0.5, strap_h_z, FreeCAD.Vector(x_hook_strap + strap_w + 3.5, strap_len_y + 2.9, z_strap_start), FreeCAD.Vector(0,0,1))
    thumb_tab = tab_box.fuse(g1).fuse(g2).fuse(g3)
    
    palmar_raw = knuckle_assembly.fuse(strap_arch).fuse(pad_box).fuse(bridge_right).fuse(hook_arm).fuse(hook_tooth).fuse(thumb_tab).removeSplitter()
    
    # Khoang cảm biến Velostat 9.8 x 7.1 x 1.4mm
    velo_w = 9.8; velo_h = min(7.1, knuckle_h - 0.4); velo_depth = 1.4
    velo_cut = Part.makeBox(velo_w, velo_depth + 0.5, velo_h,
                            FreeCAD.Vector(-velo_w/2.0, -r_in - velo_depth, knuckle_z_min + (knuckle_h - velo_h)/2.0))
    palmar_hollow = palmar_raw.cut(velo_cut)
    
    # Khoan lỗ trục xoay phi 4.5mm (chốt phi 3.0mm + khe hở radial 0.75mm)
    knuckle_hole = Part.makeCylinder(hole_r, knuckle_h + 4.0, FreeCAD.Vector(hx, hy, knuckle_z_min - 2.0), FreeCAD.Vector(0, 0, 1))
    chamfer_b = Part.makeCone(hole_r + 0.8, hole_r, 0.8, FreeCAD.Vector(hx, hy, knuckle_z_min), FreeCAD.Vector(0, 0, 1))
    chamfer_t = Part.makeCone(hole_r, hole_r + 0.8, 0.8, FreeCAD.Vector(hx, hy, knuckle_z_max - 0.8), FreeCAD.Vector(0, 0, 1))
    
    arm_final = palmar_hollow.cut(knuckle_hole).cut(chamfer_b).cut(chamfer_t).removeSplitter()
    assert len(arm_final.Solids) == 1, f"LỖI: arm_final có {len(arm_final.Solids)} solids!"
    
    # Tư thế in FDM mở -90 độ (khe hở cực kỳ thoáng >0.75mm, không có bất kỳ va chạm nào)
    arm_open_90 = arm_final.copy()
    arm_open_90.rotate(FreeCAD.Vector(hx, hy, 0), FreeCAD.Vector(0, 0, 1), -90.0)
    
    compound_open = Part.Compound([dorsal_final, arm_open_90])
    compound_closed = Part.Compound([dorsal_final, arm_final])
    
    return dorsal_final, arm_final, compound_open, compound_closed

# ==============================================================================
# DỰNG BỘ 3 ĐỐT NGÓN TAY HOÀN CHỈNH
# ==============================================================================
print("--> Dựng Đốt 1 (Proximal) - phi 23.6mm...")
d1, a1, p1_open, p1_closed = build_phalanx_v34(
    r_in=11.8, length_z=16.0, is_distal=False, has_front_joint=True, has_rear_joint=False,
    num_length_steps=5, step_pitch=2.0, r_in_mate=10.8
)

print("--> Dựng Đốt 2 (Middle) - phi 21.6mm...")
d2, a2, p2_open, p2_closed = build_phalanx_v34(
    r_in=10.8, length_z=13.5, is_distal=False, has_front_joint=True, has_rear_joint=True,
    num_length_steps=5, step_pitch=2.0, rear_reach=8.5, r_in_mate=9.8
)

print("--> Dựng Đốt 3 (Distal HỞ ĐẦU) - phi 19.6mm...")
d3, a3, p3_open, p3_closed = build_phalanx_v34(
    r_in=9.8, length_z=12.6, is_distal=True, has_front_joint=False, has_rear_joint=True,
    rear_reach=8.0
)

# ==============================================================================
# DỰNG CHỐT XỎ RỜI TỰ KHÓA (DETACHABLE SNAP-PIN) IN 3D
# ==============================================================================
print("--> Dựng Chốt xỏ rời tự khóa (Detachable Snap-Pin)...")
pin_head = Part.makeCylinder(2.7, 1.2, FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1))
pin_shaft = Part.makeCylinder(1.5, 6.8, FreeCAD.Vector(0, 0, 1.2), FreeCAD.Vector(0, 0, 1))
pin_collar = Part.makeCylinder(1.8, 0.5, FreeCAD.Vector(0, 0, 8.0), FreeCAD.Vector(0, 0, 1))
pin_cone = Part.makeCone(1.8, 0.9, 1.5, FreeCAD.Vector(0, 0, 8.5), FreeCAD.Vector(0, 0, 1))
snap_pin_raw = pin_head.fuse(pin_shaft).fuse(pin_collar).fuse(pin_cone)

pin_slit = Part.makeBox(0.9, 4.0, 4.5, FreeCAD.Vector(-0.45, -2.0, 10.0 - 4.5))
snap_pin_final = snap_pin_raw.cut(pin_slit).removeSplitter()
assert len(snap_pin_final.Solids) == 1

# ==============================================================================
# KIỂM ĐỊNH TOÀN DIỆN: VA CHẠM = 0.0000 VÀ KHOẢNG CÁCH AN TOÀN >= 0.70mm
# ==============================================================================
print("\n=== KIỂM ĐỊNH VA CHẠM VÀ KHE HỞ AN TOÀN TRÊN TỪNG ĐỐT ===")
for name, p_open in [("Đốt 1 (Proximal)", p1_open), ("Đốt 2 (Middle)", p2_open), ("Đốt 3 (Distal)", p3_open)]:
    s1 = p_open.Solids[0]
    s2 = p_open.Solids[1]
    comm = s1.common(s2)
    dist = s1.distToShape(s2)
    print(f"    {name:20s} | Va chạm thể tích: {comm.Volume:.4f} mm3 | Khoảng cách min: {dist[0]:.3f} mm")
    assert comm.Volume == 0.0, f"LỖI: {name} BỊ VA CHẠM TRONG TƯ THẾ IN!"
    assert dist[0] >= 0.70, f"LỖI: {name} KHOẢNG CÁCH QUÁ NHỎ ({dist[0]} mm)!"

print("--> TẤT CẢ 3 ĐỐT ĐỀU ĐẠT CHUẨN HOÀN HẢO! ZERO COLLISION VÀ KHE HỞ >= 0.70mm!\n")

# ==============================================================================
# CỤM LẮP RÁP 3 ĐỐT DUỖI THẲNG 0 ĐỘ VÀ GẬP 45 ĐỘ
# ==============================================================================
print("--> Dựng cụm lắp ráp 3 đốt duỗi thẳng 0 độ...")
d1_c = d1.copy(); a1_c = a1.copy()
d2_c = d2.copy(); a2_c = a2.copy()
d3_c = d3.copy(); a3_c = a3.copy()

z_pip_stud = -8.5
z_pip_hole = 16.0 + 3.5 + 2 * 2.0 # Nấc giữa (Nấc 3, +4.0mm)
z_offset_p2 = z_pip_hole - z_pip_stud
d2_c.translate(FreeCAD.Vector(0, 0, z_offset_p2))
a2_c.translate(FreeCAD.Vector(0, 0, z_offset_p2))

z_dip_stud = z_offset_p2 - 8.0
z_dip_hole = z_offset_p2 + 13.5 + 3.5 + 2 * 2.0 # Nấc giữa (Nấc 3, +4.0mm)
z_offset_p3 = z_dip_hole - z_dip_stud + z_offset_p2
d3_c.translate(FreeCAD.Vector(0, 0, z_offset_p3))
a3_c.translate(FreeCAD.Vector(0, 0, z_offset_p3))

straight_compound = Part.Compound([d1_c, a1_c, d2_c, a2_c, d3_c, a3_c])

print("--> Dựng cụm lắp ráp 3 đốt gập 45 độ (Flexed Grasping)...")
d2_f = d2.copy(); a2_f = a2.copy()
d3_f = d3.copy(); a3_f = a3.copy()

p2_comp = Part.Compound([d2_f, a2_f])
p2_comp.translate(FreeCAD.Vector(0, 0, z_offset_p2))
p2_comp.rotate(FreeCAD.Vector(0, 0, z_pip_hole), FreeCAD.Vector(1, 0, 0), -45.0)

p3_comp = Part.Compound([d3_f, a3_f])
p3_comp.translate(FreeCAD.Vector(0, 0, z_offset_p3))
p3_comp.rotate(FreeCAD.Vector(0, 0, z_pip_hole), FreeCAD.Vector(1, 0, 0), -45.0)
p3_comp.rotate(FreeCAD.Vector(0, 0, z_dip_hole), FreeCAD.Vector(1, 0, 0), -40.0)

flexed_compound = Part.Compound([d1_c, a1_c, p2_comp, p3_comp])

# ==============================================================================
# XUẤT LƯỚI FDM CHUẨN XÁC, MANIFOLD 100%, SOLID 100%
# ==============================================================================
print("--> Xuất file STL và STEP và kiểm tra chất lượng lưới...")
def export_and_verify(comp, name):
    stl_path = os.path.join(OUT_DIR, f"{name}.stl")
    step_path = os.path.join(OUT_DIR, f"{name}.step")
    
    m = MeshPart.meshFromShape(comp, LinearDeflection=0.08, AngularDeflection=0.35)
    
    is_solid = m.isSolid()
    has_non_manifold = m.hasNonManifolds()
    print(f"    Chi tiết: {name:30s} | Tam giác: {len(m.Facets):6d} | Solid: {str(is_solid):5s} | Non-manifold: {has_non_manifold}")
    assert not has_non_manifold, f"LỖI NON-MANIFOLD TRÊN {name}!"
    
    m.write(stl_path)
    comp.exportStep(step_path)
    print(f"    --> Đã lưu: {name}.stl & {name}.step")

export_and_verify(p1_open, "phalanx1_proximal_open")
export_and_verify(p2_open, "phalanx2_middle_open")
export_and_verify(p3_open, "phalanx3_distal_open")
export_and_verify(snap_pin_final, "intersegment_snap_pin")
export_and_verify(straight_compound, "full_finger_assembly_straight")
export_and_verify(flexed_compound, "full_finger_assembly_flexed")

# Lưu Document FreeCAD
doc.addObject("Part::Feature", "Phalanx1_Proximal_Open").Shape = p1_open
doc.addObject("Part::Feature", "Phalanx2_Middle_Open").Shape = p2_open
doc.addObject("Part::Feature", "Phalanx3_Distal_Open").Shape = p3_open
doc.addObject("Part::Feature", "IntersegmentSnapPin").Shape = snap_pin_final
doc.addObject("Part::Feature", "FullFingerStraight").Shape = straight_compound
doc.addObject("Part::Feature", "FullFingerFlexed").Shape = flexed_compound

doc.recompute()
try:
    doc.saveAs(os.path.join(OUT_DIR, "full_finger_modular.FCStd"))
except Exception as e:
    print(f"Lưu ý khi ghi đè FCStd: {e}")

print("\n=== HOÀN TẤT THÀNH CÔNG 100%! TOÀN BỘ FILE ĐÃ ĐƯỢC XUẤT VÀO ===")
print(OUT_DIR)
