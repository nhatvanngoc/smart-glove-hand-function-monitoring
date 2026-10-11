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

def test_cuff(r_in=11.8, length_z=16.0):
    shell_thick = 2.0
    hx = -(r_in + shell_thick + 0.5)
    hy = -2.2
    pin_r = 1.4
    gap_radial = 0.35
    hole_r = pin_r + gap_radial
    
    knuckle_z_min = 2.4
    knuckle_z_max = length_z - 2.4
    knuckle_height = knuckle_z_max - knuckle_z_min
    
    # -------------------------------------------------------------------------
    # 1. DORSAL SHELL
    # -------------------------------------------------------------------------
    outer_cyl = Part.makeCylinder(r_in + shell_thick, length_z, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1))
    inner_cyl = Part.makeCylinder(r_in, length_z + 4.0, FreeCAD.Vector(0,0,-2.0), FreeCAD.Vector(0,0,1))
    dorsal_tube = outer_cyl.cut(inner_cyl)
    
    # Cắt nửa dưới (Y < 0)
    cutter_bottom = Part.makeBox(60.0, 30.0, length_z + 4.0, FreeCAD.Vector(-30.0, -30.0, -2.0))
    dorsal_base = dorsal_tube.cut(cutter_bottom)
    
    # Khe xoay bản lề sườn trái
    arm_swing_cut = Part.makeBox(12.0, 10.0, knuckle_height + 0.8, FreeCAD.Vector(hx - 5.0, hy - 4.0, knuckle_z_min - 0.4))
    dorsal_base = dorsal_base.cut(arm_swing_cut)
    
    # Tai bản lề Print-in-Place bên trái
    lug_outer = Part.makeCylinder(pin_r + 1.2, length_z, FreeCAD.Vector(hx, hy, 0.0), FreeCAD.Vector(0,0,1))
    lug_slot_cut = Part.makeBox(14.0, 14.0, knuckle_height + 0.8, FreeCAD.Vector(hx - 7.0, hy - 7.0, knuckle_z_min - 0.4))
    lug_fork = lug_outer.cut(lug_slot_cut)
    lug_bridge = Part.makeBox(4.5, 3.5, length_z, FreeCAD.Vector(hx, hy - 2.0, 0.0)).cut(lug_slot_cut)
    hinge_pin_int = Part.makeCylinder(pin_r, length_z, FreeCAD.Vector(hx, hy, 0.0), FreeCAD.Vector(0,0,1))
    
    # -------------------------------------------------------------------------
    # 2. HỌNG KHÓA THÔNG SUỐT TRÊN MU NGÓN (THRU-CHUTE BUCKLE AT SƯỜN PHẢI)
    # -------------------------------------------------------------------------
    # Họng khóa nằm ở sườn phải (X ~ r_in + 1.2 đến r_in + 4.5)
    # Rãnh trượt thông suốt theo trục Y từ Y = -2.0 đến Y = +8.0
    rx_chute = r_in + 1.0
    slot_w_x = 1.8 # Khe lọt cho dải răng dày 1.3mm (khe rộng 1.8mm)
    wall_inner = 1.4 # Vách trong gắn vào thân máng mu
    wall_outer = 1.4 # Vách ngoài
    chute_len_y = 9.0 # Chiều dài ống hầm
    chute_y_start = -1.5
    
    # Khối vỏ hầm khóa
    chute_total_x = wall_inner + slot_w_x + wall_outer # 1.4 + 1.8 + 1.4 = 4.6mm
    chute_box = Part.makeBox(chute_total_x, chute_len_y, knuckle_height, 
                             FreeCAD.Vector(rx_chute, chute_y_start, knuckle_z_min))
    
    # Đường hầm thông suốt 2 đầu (Subtractive Overshoot 2.0mm mỗi đầu)
    tunnel_slot = Part.makeBox(slot_w_x, chute_len_y + 4.0, knuckle_height + 2.0,
                               FreeCAD.Vector(rx_chute + wall_inner, chute_y_start - 2.0, knuckle_z_min - 1.0))
    chute_tunnel = chute_box.cut(tunnel_slot)
    
    # Lẫy đàn hồi bên vách ngoài với răng khóa cái (Internal locking tooth)
    # Răng khóa lồi vào trong đường hầm ở vách ngoài (X = rx_chute + wall_inner + slot_w_x)
    # Răng ăn khớp theo chiều: trượt từ -Y lên +Y (dốc 45 độ), khóa lại chiều ngược lại (90 độ)
    x_pawl_root = rx_chute + wall_inner + slot_w_x
    p_t1 = FreeCAD.Vector(x_pawl_root + 0.1, chute_y_start + 4.0, knuckle_z_min)
    p_t2 = FreeCAD.Vector(x_pawl_root - 0.75, chute_y_start + 4.0, knuckle_z_min) # Răng nhô vào hầm 0.75mm
    p_t3 = FreeCAD.Vector(x_pawl_root + 0.1, chute_y_start + 5.5, knuckle_z_min) # Dốc dài 1.5mm
    w_pawl = Part.makePolygon([p_t1, p_t2, p_t3, p_t1])
    f_pawl = Part.Face(w_pawl).extrude(FreeCAD.Vector(0,0,knuckle_height))
    
    # Khe rãnh đàn hồi giúp vách ngoài nhún được (Slot slit)
    slit_cut = Part.makeBox(wall_outer + 1.0, 0.8, knuckle_height + 2.0,
                            FreeCAD.Vector(x_pawl_root - 0.2, chute_y_start + 6.5, knuckle_z_min - 1.0))
    
    # Tai gạt mở nhanh (Quick-Release tab) ở vách ngoài
    release_tab = Part.makeBox(2.2, 2.8, knuckle_height,
                              FreeCAD.Vector(rx_chute + chute_total_x, chute_y_start + 3.5, knuckle_z_min))
    
    chute_solid = chute_tunnel.fuse(f_pawl).cut(slit_cut).fuse(release_tab).removeSplitter()
    
    # Cầu nối gắn chắc họng khóa vào vỏ mu ngón (gối sâu 0.5mm vào thân)
    bridge_box = Part.makeBox(wall_inner + 1.0, 4.0, length_z,
                             FreeCAD.Vector(rx_chute - 0.5, 0.0, 0.0))
    
    dorsal_solid = dorsal_base.fuse(lug_fork).fuse(lug_bridge).fuse(hinge_pin_int).fuse(chute_solid).fuse(bridge_box).removeSplitter()
    
    # -------------------------------------------------------------------------
    # 3. DẢI ÔM BỤNG (PALMAR STRAP) MANG DẢI RĂNG ĐỰC DÀI 6 NẤC
    # -------------------------------------------------------------------------
    # Knuckle bên trái
    knuckle_out = Part.makeCylinder(hole_r + 1.2, knuckle_height, FreeCAD.Vector(hx, hy, knuckle_z_min), FreeCAD.Vector(0,0,1))
    # Nối bản lề
    p_k1 = FreeCAD.Vector(hx, hy - hole_r - 1.2, knuckle_z_min)
    p_k2 = FreeCAD.Vector(hx, hy + hole_r + 1.2, knuckle_z_min)
    p_k3 = FreeCAD.Vector(-r_in + 0.2, -0.2, knuckle_z_min)
    p_k4 = FreeCAD.Vector(-r_in - 1.2, -2.5, knuckle_z_min)
    w_k = Part.makePolygon([p_k1, p_k2, p_k3, p_k4, p_k1])
    f_k = Part.Face(w_k).extrude(FreeCAD.Vector(0,0,knuckle_height))
    knuckle_piece = knuckle_out.fuse(f_k).removeSplitter()
    
    # Cánh cung dẻo ôm bụng: Dày 1.4mm
    strap_t = 1.4
    strap_out = Part.makeCylinder(r_in + strap_t, knuckle_height, FreeCAD.Vector(0,0,knuckle_z_min), FreeCAD.Vector(0,0,1))
    strap_in = Part.makeCylinder(r_in, knuckle_height + 4.0, FreeCAD.Vector(0,0,knuckle_z_min - 2.0), FreeCAD.Vector(0,0,1))
    strap_tube = strap_out.cut(strap_in)
    
    # Cắt lấy nửa dưới (Y < 0) và sườn phải (X <= rx_chute + wall_inner + 0.2)
    cut_top = Part.makeBox(60.0, 30.0, 30.0, FreeCAD.Vector(-30.0, 0.0, 0.0))
    cut_far_right = Part.makeBox(30.0, 60.0, 30.0, FreeCAD.Vector(rx_chute + wall_inner + 0.2, -30.0, 0.0))
    strap_arch = strap_tube.cut(cut_top).cut(cut_far_right)
    
    # Đế cảm biến phẳng 11.4 x 3.2mm ở đáy ngón tay
    pad_w = 11.4
    pad_t = 3.2
    pad_box = Part.makeBox(pad_w, pad_t, knuckle_height, FreeCAD.Vector(-pad_w/2.0, -r_in - pad_t, knuckle_z_min))
    
    # DẢI RĂNG ĐỰC (MALE RATCHET STRIP): Nằm ở đầu tự do bên phải của cánh cung!
    # Thanh răng vươn thẳng lên theo hướng +Y để đút thẳng vào họng khóa
    rack_x = rx_chute + wall_inner + 0.2 # Căn chính giữa khe hở đường hầm!
    rack_w = 1.3 # Bề dày thanh răng 1.3mm (khe rộng 1.8mm -> clearance 0.25mm mỗi bên)
    rack_len = 13.0 # Dài 13mm chứa 6 nấc răng cưa
    rack_y_start = -2.0
    
    rack_base = Part.makeBox(rack_w, rack_len, knuckle_height,
                             FreeCAD.Vector(rack_x, rack_y_start, knuckle_z_min))
    
    # Vát nhọn đầu thanh răng 45 độ để đút trúng họng khóa
    p_tip1 = FreeCAD.Vector(rack_x - 0.2, rack_y_start + rack_len, knuckle_z_min - 1.0)
    p_tip2 = FreeCAD.Vector(rack_x + rack_w + 0.2, rack_y_start + rack_len - 1.8, knuckle_z_min - 1.0)
    p_tip3 = FreeCAD.Vector(rack_x + rack_w + 0.2, rack_y_start + rack_len, knuckle_z_min - 1.0)
    w_tip = Part.makePolygon([p_tip1, p_tip2, p_tip3, p_tip1])
    f_tip = Part.Face(w_tip).extrude(FreeCAD.Vector(0,0,knuckle_height + 2.0))
    rack_beveled = rack_base.cut(f_tip)
    
    # Tạo 6 răng cưa đực hình tam giác một chiều trên mặt ngoài của thanh (+X)
    # Bước răng P = 1.6mm, sâu 0.75mm, góc dốc 45 độ hướng về đỉnh (+Y), góc khóa 90 độ hướng về gốc (-Y)
    P = 1.6
    d_tooth = 0.75
    teeth_compound = []
    for i in range(6):
        y_lock = rack_y_start + 2.0 + i * P
        y_ramp_tip = y_lock + 1.2
        pt1 = FreeCAD.Vector(rack_x + rack_w - 0.05, y_lock, knuckle_z_min)
        pt2 = FreeCAD.Vector(rack_x + rack_w + d_tooth, y_lock, knuckle_z_min) # Đỉnh răng đực
        pt3 = FreeCAD.Vector(rack_x + rack_w - 0.05, y_ramp_tip, knuckle_z_min)
        w_t = Part.makePolygon([pt1, pt2, pt3, pt1])
        f_t = Part.Face(w_t).extrude(FreeCAD.Vector(0,0,knuckle_height))
        rack_beveled = rack_beveled.fuse(f_t)
        
    # Cầu nối gắn chắc thanh răng vào đầu cánh cung dẻo
    rack_root = Part.makeBox(rack_w + 1.2, 2.5, knuckle_height,
                            FreeCAD.Vector(rack_x - 1.2, rack_y_start, knuckle_z_min))
    
    # FUSE toàn bộ cụm bụng ngón
    palmar_raw = knuckle_piece.fuse(strap_arch).fuse(pad_box).fuse(rack_beveled).fuse(rack_root).removeSplitter()
    
    # Khoét khoang phẳng Velostat 9.8 x 7.1 x 1.4mm
    velo_w = 9.8
    velo_h = min(7.1, knuckle_height - 0.4)
    velo_depth = 1.4
    velo_cut = Part.makeBox(velo_w, velo_depth + 0.5, velo_h,
                            FreeCAD.Vector(-velo_w/2.0, -r_in - velo_depth, knuckle_z_min + (knuckle_height - velo_h)/2.0))
    palmar_hollow = palmar_raw.cut(velo_cut)
    
    # Khoan lỗ trục xoay
    knuckle_hole = Part.makeCylinder(hole_r, knuckle_height + 4.0, FreeCAD.Vector(hx, hy, knuckle_z_min - 2.0), FreeCAD.Vector(0,0,1))
    chamfer_b = Part.makeCone(hole_r + 0.6, hole_r, 0.6, FreeCAD.Vector(hx, hy, knuckle_z_min), FreeCAD.Vector(0,0,1))
    chamfer_t = Part.makeCone(hole_r, hole_r + 0.6, 0.6, FreeCAD.Vector(hx, hy, knuckle_z_max - 0.6), FreeCAD.Vector(0,0,1))
    
    palmar_final = palmar_hollow.cut(knuckle_hole).cut(chamfer_b).cut(chamfer_t).removeSplitter()
    
    print("Dorsal Solids:", len(dorsal_solid.Solids), "Volume:", dorsal_solid.Volume)
    print("Palmar Solids:", len(palmar_final.Solids), "Volume:", palmar_final.Volume)
    
    # Kiểm tra xoay mở -100 độ cho Print-in-Place
    palmar_open = palmar_final.copy()
    palmar_open.rotate(FreeCAD.Vector(hx, hy, 0), FreeCAD.Vector(0, 0, 1), -100.0)
    
    comp = Part.Compound([dorsal_solid, palmar_open])
    
    # Xuất STL bằng MeshPart tiêu chuẩn
    stl_test = r"D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\3d_model\test_new_cuff.stl"
    m = MeshPart.meshFromShape(comp, LinearDeflection=0.08, AngularDeflection=0.35)
    print("Mesh: Facets =", len(m.Facets), "Points =", len(m.Points), "isSolid =", m.isSolid(), "hasNonManifolds =", m.hasNonManifolds())
    m.write(stl_test)
    print("Đã xuất STL thành công vào:", stl_test)

test_cuff()
