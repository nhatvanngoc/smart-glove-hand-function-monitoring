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

def test_full_redesign(r_in=11.8, length_z=16.0):
    shell_thick = 2.0
    
    # -------------------------------------------------------------------------
    # 1. BẢN LỀ PRINT-IN-PLACE DUNG SAI VÀNG FDM (RADIAL GAP 0.6mm, Z-GAP 0.8mm)
    # -------------------------------------------------------------------------
    hx = -(r_in + shell_thick + 0.8)
    hy = -2.2
    pin_r = 1.6 # Tăng đường kính chốt lên 3.2mm chịu lực cắt cao
    gap_radial = 0.60 # Khe hở hướng kính 0.6mm đảm bảo FDM không dính
    hole_r = pin_r + gap_radial # Bán kính lỗ = 2.2mm
    gap_z = 0.80 # Khe hở dọc trục Z 0.8mm (4 lớp in 0.2mm)
    
    knuckle_z_min = 2.6
    knuckle_z_max = length_z - 2.6
    knuckle_height = knuckle_z_max - knuckle_z_min # Chiều cao đốt gài bụng
    
    # Khối máng mu ngón
    outer_cyl = Part.makeCylinder(r_in + shell_thick, length_z, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1))
    inner_cyl = Part.makeCylinder(r_in, length_z + 4.0, FreeCAD.Vector(0,0,-2.0), FreeCAD.Vector(0,0,1))
    dorsal_tube = outer_cyl.cut(inner_cyl)
    cutter_bottom = Part.makeBox(60.0, 30.0, length_z + 4.0, FreeCAD.Vector(-30.0, -30.0, -2.0))
    dorsal_base = dorsal_tube.cut(cutter_bottom)
    
    # Khe khoét cho tai bản lề bụng xoay (rộng rãi, Z-gap = 0.8mm mỗi đầu)
    arm_swing_cut = Part.makeBox(14.0, 12.0, knuckle_height + 2 * gap_z, 
                                 FreeCAD.Vector(hx - 6.0, hy - 5.0, knuckle_z_min - gap_z))
    dorsal_base = dorsal_base.cut(arm_swing_cut)
    
    # Tai bản lề máng mu (Lug fork)
    lug_outer = Part.makeCylinder(pin_r + 1.5, length_z, FreeCAD.Vector(hx, hy, 0.0), FreeCAD.Vector(0,0,1))
    lug_slot_cut = Part.makeBox(16.0, 16.0, knuckle_height + 2 * gap_z, 
                                FreeCAD.Vector(hx - 8.0, hy - 8.0, knuckle_z_min - gap_z))
    lug_fork = lug_outer.cut(lug_slot_cut)
    lug_bridge = Part.makeBox(5.0, 4.0, length_z, FreeCAD.Vector(hx, hy - 2.0, 0.0)).cut(lug_slot_cut)
    
    # Chốt xoay vát nón 45 độ 2 đầu để giảm tiếp xúc và dễ bẻ lách
    pin_cyl = Part.makeCylinder(pin_r, length_z, FreeCAD.Vector(hx, hy, 0.0), FreeCAD.Vector(0,0,1))
    # Vát nón côn tại hai điểm chuyển tiếp giữa tai và đốt xoay
    cone_cut_b = Part.makeCone(pin_r + 0.6, pin_r, 0.6, FreeCAD.Vector(hx, hy, knuckle_z_min - gap_z), FreeCAD.Vector(0,0,1))
    cone_cut_t = Part.makeCone(pin_r, pin_r + 0.6, 0.6, FreeCAD.Vector(hx, hy, knuckle_z_max + gap_z - 0.6), FreeCAD.Vector(0,0,1))
    hinge_pin = pin_cyl.cut(cone_cut_b).cut(cone_cut_t)
    
    # -------------------------------------------------------------------------
    # 2. HỌNG KHÓA CƠ CẤU BẬP BÊNH (SEESAW ROCKER BUCKLE)
    # -------------------------------------------------------------------------
    # Rãnh trượt thông suốt: rộng 2.6mm cho dải răng 1.8mm -> clearance 0.8mm cực kỳ êm!
    rx_chute = r_in + 1.0
    slot_w_x = 2.6
    wall_inner = 1.4
    chute_len_y = 12.0
    chute_y_start = -2.5
    
    # Khung vỏ hầm
    chute_w_total = wall_inner + slot_w_x + 1.5
    chute_box = Part.makeBox(chute_w_total, chute_len_y, knuckle_height,
                             FreeCAD.Vector(rx_chute, chute_y_start, knuckle_z_min))
    
    # Hầm rỗng thông suốt hai đầu
    tunnel_cut = Part.makeBox(slot_w_x, chute_len_y + 4.0, knuckle_height - 1.6,
                              FreeCAD.Vector(rx_chute + wall_inner, chute_y_start - 2.0, knuckle_z_min + 0.8))
    chute_frame = chute_box.cut(tunnel_cut)
    
    # CƠ CẤU LẪY BẬP BÊNH (SEESAW ROCKER LEVER):
    # Trục bản lề đàn hồi ở giữa: Y = chute_y_start + 6.0
    # Đầu trước (Y < 6.0): Mang răng khóa ăn vào dải răng
    # Đuôi sau (Y > 6.0): Cánh tay đòn ấn xả (nhô ra ngoài có khía nhám)
    x_pivot = rx_chute + wall_inner + slot_w_x
    
    # Bản lề đàn hồi dầm mỏng 1.0mm
    flex_hinge = Part.makeBox(1.0, 1.4, knuckle_height - 1.6,
                             FreeCAD.Vector(x_pivot, chute_y_start + 5.5, knuckle_z_min + 0.8))
                             
    # Cánh đòn bập bênh:
    # Đầu trước mang răng khóa:
    front_arm = Part.makeBox(1.2, 4.0, knuckle_height - 1.6,
                            FreeCAD.Vector(x_pivot, chute_y_start + 1.5, knuckle_z_min + 0.8))
    # Răng khóa tam giác một chiều 90°/45° nhô vào rãnh 0.7mm
    pt1 = FreeCAD.Vector(x_pivot + 0.1, chute_y_start + 3.0, knuckle_z_min + 0.8)
    pt2 = FreeCAD.Vector(x_pivot - 0.7, chute_y_start + 3.0, knuckle_z_min + 0.8)
    pt3 = FreeCAD.Vector(x_pivot + 0.1, chute_y_start + 4.5, knuckle_z_min + 0.8)
    pawl_tooth = Part.Face(Part.makePolygon([pt1, pt2, pt3, pt1])).extrude(FreeCAD.Vector(0,0,knuckle_height - 1.6))
    
    # Đuôi sau: Cánh tay ấn nhả (Rocker Rear Paddle) nghiêng ra ngoài để ngón tay ấn xuống
    rear_arm = Part.makeBox(2.8, 4.5, knuckle_height - 1.6,
                           FreeCAD.Vector(x_pivot + 0.4, chute_y_start + 7.0, knuckle_z_min + 0.8))
    # Khía nhám chống trượt trên đuôi ấn
    g1 = Part.makeBox(0.6, 0.8, knuckle_height - 1.6, FreeCAD.Vector(x_pivot + 3.2, chute_y_start + 7.8, knuckle_z_min + 0.8))
    g2 = Part.makeBox(0.6, 0.8, knuckle_height - 1.6, FreeCAD.Vector(x_pivot + 3.2, chute_y_start + 9.8, knuckle_z_min + 0.8))
    
    rocker_lever = front_arm.fuse(pawl_tooth).fuse(flex_hinge).fuse(rear_arm).fuse(g1).fuse(g2)
    
    # Cắt rãnh thoát cho lẫy bập bênh dao động tự do không chạm vách
    rocker_slit = Part.makeBox(4.5, 11.0, knuckle_height - 1.6,
                              FreeCAD.Vector(x_pivot + 0.1, chute_y_start + 0.5, knuckle_z_min + 0.8))
    chute_frame = chute_frame.cut(rocker_slit)
    
    chute_assembled = chute_frame.fuse(rocker_lever).removeSplitter()
    
    # Cầu gắn họng vào thân mu ngón
    bridge_box = Part.makeBox(wall_inner + 1.2, 4.5, length_z, FreeCAD.Vector(rx_chute - 0.6, 0.0, 0.0))
    
    dorsal_all = dorsal_base.fuse(lug_fork).fuse(lug_bridge).fuse(hinge_pin).fuse(chute_assembled).fuse(bridge_box).removeSplitter()
    
    # -------------------------------------------------------------------------
    # 3. TAY ĐÒN LIÊN KẾT GIA CƯỜNG DÀI VƯƠN 18.0mm + GÂN TAM GIÁC CHỐNG GÃY
    # -------------------------------------------------------------------------
    arm_reach = 18.0 # Tăng vươn từ 10.5mm lên 18.0mm (chuẩn giải phẫu gập 90 độ)
    arm_thick = 3.2  # Dày 3.2mm
    arm_width_y = 7.0 # Rộng 7.0mm
    x_outer = r_in + shell_thick
    x_arm_l = -(x_outer + 0.3 + arm_thick)
    x_arm_r = x_outer + 0.3
    
    arm_box_l = Part.makeBox(arm_thick, arm_width_y, arm_reach + 3.0, 
                             FreeCAD.Vector(x_arm_l, -arm_width_y/2.0, length_z - 3.0))
    arm_box_r = Part.makeBox(arm_thick, arm_width_y, arm_reach + 3.0, 
                             FreeCAD.Vector(x_arm_r, -arm_width_y/2.0, length_z - 3.0))
                             
    # GÂN TAM GIÁC GIA CƯỜNG CHỐNG GÃY GỐC (Triangular Gusset Ribs)
    # Gân vát góc 45 độ dài 5.0mm nối từ lưng máng mu ra sườn tay đòn
    p_g1 = FreeCAD.Vector(x_arm_l, -arm_width_y/2.0, length_z - 4.5)
    p_g2 = FreeCAD.Vector(x_arm_l, -arm_width_y/2.0, length_z + 4.0)
    p_g3 = FreeCAD.Vector(x_arm_l + arm_thick + 1.5, -arm_width_y/2.0, length_z - 4.5)
    gusset_l = Part.Face(Part.makePolygon([p_g1, p_g2, p_g3, p_g1])).extrude(FreeCAD.Vector(0, arm_width_y, 0))
    
    p_gr1 = FreeCAD.Vector(x_arm_r + arm_thick, -arm_width_y/2.0, length_z - 4.5)
    p_gr2 = FreeCAD.Vector(x_arm_r + arm_thick, -arm_width_y/2.0, length_z + 4.0)
    p_gr3 = FreeCAD.Vector(x_arm_r - 1.5, -arm_width_y/2.0, length_z - 4.5)
    gusset_r = Part.Face(Part.makePolygon([p_gr1, p_gr2, p_gr3, p_gr1])).extrude(FreeCAD.Vector(0, arm_width_y, 0))
    
    # 3 Lỗ định vị phi 3.4mm cách nhau 2.5mm
    for i in range(3):
        z_hole = length_z + 3.0 + i * 2.5
        h_l = Part.makeCylinder(1.7, arm_thick + 2.0, FreeCAD.Vector(x_arm_l - 1.0, 0, z_hole), FreeCAD.Vector(1, 0, 0))
        h_r = Part.makeCylinder(1.7, arm_thick + 2.0, FreeCAD.Vector(x_arm_r - 1.0, 0, z_hole), FreeCAD.Vector(1, 0, 0))
        arm_box_l = arm_box_l.cut(h_l)
        arm_box_r = arm_box_r.cut(h_r)
        
    dorsal_all = dorsal_all.fuse(arm_box_l).fuse(arm_box_r).fuse(gusset_l).fuse(gusset_r).removeSplitter()
    
    # -------------------------------------------------------------------------
    # 4. DẢI ÔM BỤNG (PALMAR STRAP) MANG DẢI RĂNG THU GỌN VÀ KHỚP VÁT NÓN
    # -------------------------------------------------------------------------
    # Khối xoay knuckle
    knuckle_out = Part.makeCylinder(hole_r + 1.4, knuckle_height, FreeCAD.Vector(hx, hy, knuckle_z_min), FreeCAD.Vector(0,0,1))
    p_k1 = FreeCAD.Vector(hx, hy - hole_r - 1.4, knuckle_z_min)
    p_k2 = FreeCAD.Vector(hx, hy + hole_r + 1.4, knuckle_z_min)
    p_k3 = FreeCAD.Vector(-r_in + 0.2, -0.2, knuckle_z_min)
    p_k4 = FreeCAD.Vector(-r_in - 1.2, -2.5, knuckle_z_min)
    f_k = Part.Face(Part.makePolygon([p_k1, p_k2, p_k3, p_k4, p_k1])).extrude(FreeCAD.Vector(0,0,knuckle_height))
    knuckle_piece = knuckle_out.fuse(f_k).removeSplitter()
    
    # Cánh cung dẻo dày 1.3mm
    strap_t = 1.3
    strap_out = Part.makeCylinder(r_in + strap_t, knuckle_height, FreeCAD.Vector(0,0,knuckle_z_min), FreeCAD.Vector(0,0,1))
    strap_in = Part.makeCylinder(r_in, knuckle_height + 4.0, FreeCAD.Vector(0,0,knuckle_z_min - 2.0), FreeCAD.Vector(0,0,1))
    strap_arch = strap_out.cut(strap_in).cut(Part.makeBox(60.0, 30.0, 30.0, FreeCAD.Vector(-30.0, 0.0, 0.0)))
    
    # Đế cảm biến Velostat 11.4 x 3.2mm
    pad_w = 11.4; pad_t = 3.2
    pad_box = Part.makeBox(pad_w, pad_t, knuckle_height, FreeCAD.Vector(-pad_w/2.0, -r_in - pad_t, knuckle_z_min))
    
    # DẢI RĂNG ĐỰC THU GỌN (THÂN 1.2mm, RĂNG 0.6mm -> TỔNG 1.8mm, lọt thỏm trong hầm 2.6mm)
    rack_x = rx_chute + wall_inner + 0.35 # Căn giữa khe 2.6mm
    rack_w = 1.2
    rack_len = 13.5
    rack_y_start = -2.0
    rack_base = Part.makeBox(rack_w, rack_len, knuckle_height, FreeCAD.Vector(rack_x, rack_y_start, knuckle_z_min))
    
    # 6 Răng tam giác bước 1.5mm, sâu 0.6mm
    P = 1.5
    d_tooth = 0.6
    for i in range(6):
        y_lock = rack_y_start + 2.0 + i * P
        y_ramp_tip = y_lock + 1.1
        pt1 = FreeCAD.Vector(rack_x + rack_w - 0.05, y_lock, knuckle_z_min)
        pt2 = FreeCAD.Vector(rack_x + rack_w + d_tooth, y_lock, knuckle_z_min)
        pt3 = FreeCAD.Vector(rack_x + rack_w - 0.05, y_ramp_tip, knuckle_z_min)
        w_t = Part.makePolygon([pt1, pt2, pt3, pt1])
        rack_base = rack_base.fuse(Part.Face(w_t).extrude(FreeCAD.Vector(0,0,knuckle_height)))
        
    # Cầu gắn dải răng vào dải bụng
    bridge_w = (rack_x + rack_w) - (r_in - 1.0)
    rack_bridge = Part.makeBox(bridge_w, 2.5, knuckle_height, FreeCAD.Vector(r_in - 1.0, rack_y_start, knuckle_z_min))
    
    palmar_raw = knuckle_piece.fuse(strap_arch).fuse(pad_box).fuse(rack_base).fuse(rack_bridge).removeSplitter()
    
    # Khoang Velostat 9.8 x 7.1 x 1.4mm
    velo_w = 9.8; velo_h = min(7.1, knuckle_height - 0.4); velo_depth = 1.4
    velo_cut = Part.makeBox(velo_w, velo_depth + 0.5, velo_h,
                            FreeCAD.Vector(-velo_w/2.0, -r_in - velo_depth, knuckle_z_min + (knuckle_height - velo_h)/2.0))
    palmar_hollow = palmar_raw.cut(velo_cut)
    
    # Khoan lỗ trục xoay phi 4.4mm (chốt phi 3.2mm + khe hở radial 0.6mm)
    knuckle_hole = Part.makeCylinder(hole_r, knuckle_height + 4.0, FreeCAD.Vector(hx, hy, knuckle_z_min - 2.0), FreeCAD.Vector(0, 0, 1))
    # Vát nón côn 45 độ 2 đầu lỗ để chống dính lớp giáp mí
    chamfer_b = Part.makeCone(hole_r + 0.8, hole_r, 0.8, FreeCAD.Vector(hx, hy, knuckle_z_min), FreeCAD.Vector(0, 0, 1))
    chamfer_t = Part.makeCone(hole_r, hole_r + 0.8, 0.8, FreeCAD.Vector(hx, hy, knuckle_z_max - 0.8), FreeCAD.Vector(0, 0, 1))
    
    palmar_final = palmar_hollow.cut(knuckle_hole).cut(chamfer_b).cut(chamfer_t).removeSplitter()
    
    print('Dorsal Solids:', len(dorsal_all.Solids), 'Volume:', dorsal_all.Volume)
    print('Palmar Solids:', len(palmar_final.Solids), 'Volume:', palmar_final.Volume)
    
    # Xoay -100 độ cho Print-in-Place
    palmar_open = palmar_final.copy()
    palmar_open.rotate(FreeCAD.Vector(hx, hy, 0), FreeCAD.Vector(0, 0, 1), -100.0)
    
    comp = Part.Compound([dorsal_all, palmar_open])
    m = MeshPart.meshFromShape(comp, LinearDeflection=0.08, AngularDeflection=0.35)
    print('Mesh: Facets =', len(m.Facets), 'Points =', len(m.Points), 'isSolid =', m.isSolid(), 'hasNonManifolds =', m.hasNonManifolds())

test_full_redesign()
