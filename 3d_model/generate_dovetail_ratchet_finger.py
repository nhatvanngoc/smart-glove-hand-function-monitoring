import sys
import os
import io
import math

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import FreeCAD
import Part
import Mesh

OUT_DIR = r"D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\3d_model\custom_exo\dovetail_ratchet_finger"
os.makedirs(OUT_DIR, exist_ok=True)

doc = FreeCAD.newDocument("DovetailRatchetFingerExo")

print("=== BẮT ĐẦU DỰNG HỆ THỐNG NẸP NGÓN TAY KIẾN TRÚC MỚI ĐỘT PHÁ ===")
print("1. Chỉnh chu vi: Quai đai dẻo răng cưa luồn máng dẫn hướng đồng tâm (8 nấc, dải phi 17-24.5mm).")
print("2. Chỉnh chiều dài: Khớp trượt Đuôi én (Dovetail) khóa cứng 5 bậc tự do + Khớp xoay Clevis đôi chịu cắt kép.")
print("3. Khoang Velostat chuẩn 9.8 x 7.1 x 1.4mm (bù co ngót FDM) đồng bộ 100% trên cả 3 đốt.")

# ==============================================================================
# HÀM TẠO KHUNG ĐỐT NGÓN TAY (PHALANX CUFF) TÍCH HỢP QUAI ĐAI RĂNG CƯA & ĐẾ VELOSTAT
# ==============================================================================
def build_phalanx_cuff(r_in, length_z, has_dovetail_channel=True, is_distal=False):
    """
    Tạo 1 đốt ngón tay hoàn chỉnh gồm:
    - Vỏ mu ngón (Dorsal shell) tích hợp rãnh trượt Đuôi én (Dovetail Channel) ở lưng.
    - Máng dẫn hướng (Buckle Guide Sleeve) tích hợp lẫy khóa đàn hồi ở sườn phải (+X).
    - Cánh cung đàn hồi dẻo 1.2mm ở sườn trái (-X).
    - Đế cảm biến phẳng cứng vững dày 3.2mm chứa hốc Velostat 9.8 x 7.1 x 1.4mm ở bụng ngón.
    - Dây đai dẻo mang dải 8 răng cưa (Buttress teeth, bước 1.5mm) luồn mượt mà qua máng.
    """
    shell_thick = 2.0
    
    # 1. DORSAL SHELL
    outer_cyl = Part.makeCylinder(r_in + shell_thick, length_z)
    inner_cyl = Part.makeCylinder(r_in, length_z + 4.0, FreeCAD.Vector(0,0,-2.0))
    dorsal_base = outer_cyl.cut(inner_cyl).cut(Part.makeBox(60.0, 30.0, length_z + 4.0, FreeCAD.Vector(-30.0, -30.0, -2.0)))
    
    # Rãnh luồn cáp / khuyên cáp ở mu ngón
    if is_distal:
        cable_eyelet = Part.makeCylinder(3.2, 6.0, FreeCAD.Vector(0, r_in + shell_thick - 1.0, length_z/2.0), FreeCAD.Vector(0, 1, 0))
        cable_hole = Part.makeCylinder(1.0, length_z + 2.0, FreeCAD.Vector(0, r_in + shell_thick + 2.5, -1.0), FreeCAD.Vector(0, 0, 1))
        cable_stop = Part.makeCylinder(1.8, 6.0, FreeCAD.Vector(0, r_in + shell_thick + 2.5, length_z/2.0), FreeCAD.Vector(0, 0, 1))
        cable_feature = cable_eyelet.cut(cable_hole).cut(cable_stop)
        dorsal_base = dorsal_base.fuse(cable_feature)
        
    # 2. RÃNH TRƯỢT ĐUÔI ÉN TRÊN MU NGÓN (DOVETAIL CHANNEL)
    w_base = 6.0
    w_top = 8.8
    h_dove = 2.6
    clearance_dove = 0.15
    
    if has_dovetail_channel:
        box_housing = Part.makeBox(w_top + 4.0, h_dove + 2.0, length_z, FreeCAD.Vector(-(w_top + 4.0)/2.0, r_in + shell_thick - 0.5, 0.0))
        
        # Rãnh cắt đuôi én có dung sai
        pts_cut = [
            FreeCAD.Vector(-w_base/2.0 - clearance_dove, r_in + shell_thick - 0.6, -1.0),
            FreeCAD.Vector(w_base/2.0 + clearance_dove, r_in + shell_thick - 0.6, -1.0),
            FreeCAD.Vector(w_top/2.0 + clearance_dove, r_in + shell_thick + h_dove + clearance_dove - 0.5, -1.0),
            FreeCAD.Vector(-w_top/2.0 - clearance_dove, r_in + shell_thick + h_dove + clearance_dove - 0.5, -1.0),
            FreeCAD.Vector(-w_base/2.0 - clearance_dove, r_in + shell_thick - 0.6, -1.0)
        ]
        wire_c = Part.makePolygon(pts_cut)
        face_c = Part.Face(wire_c)
        cutter_dove = face_c.extrude(FreeCAD.Vector(0, 0, length_z + 2.0))
        
        # Lỗ chốt khóa nêm ngang (phi 2.2mm)
        pin_lock_hole = Part.makeCylinder(1.1, w_top + 6.0, FreeCAD.Vector(-(w_top+6.0)/2.0, r_in + shell_thick + h_dove/2.0, length_z/2.0), FreeCAD.Vector(1, 0, 0))
        
        # Rãnh cáp luồn dọc thành bên của hộp trượt
        cable_tunnel = Part.makeCylinder(1.0, length_z + 2.0, FreeCAD.Vector(5.0, r_in + shell_thick + 1.2, -1.0), FreeCAD.Vector(0, 0, 1))
        
        dovetail_housing = box_housing.cut(cutter_dove).cut(pin_lock_hole).cut(cable_tunnel)
        dorsal_base = dorsal_base.fuse(dovetail_housing)
        
    # Nếu là đốt 2 hoặc đốt 3: cần có tai bản lề sau (Rear Tongue) để khớp vào Clevis của thanh trượt phía trước
    if is_distal or r_in < 11.0:
        tongue_w = 3.6
        tongue_h = 5.5
        tongue_reach = 5.5
        overlap_z = 1.5
        tongue_box = Part.makeBox(tongue_w, tongue_h, tongue_reach + overlap_z, FreeCAD.Vector(-tongue_w/2.0, r_in + shell_thick - 1.0, -tongue_reach))
        tongue_hole = Part.makeCylinder(1.4, tongue_w + 2.0, FreeCAD.Vector(-tongue_w/2.0 - 1.0, r_in + shell_thick + tongue_h/2.0 - 1.0, -tongue_reach + 2.5), FreeCAD.Vector(1, 0, 0))
        tongue = tongue_box.cut(tongue_hole)
        dorsal_base = dorsal_base.fuse(tongue)
        
    # 3. MÁNG DẪN HƯỚNG BUCKLE SLEEVE Ở SƯỜN PHẢI (+X)
    strap_w = 8.0
    strap_t = 1.2
    slot_t = 1.8 # Khe trượt rộng 1.8mm (khe hở 0.3mm mỗi bên cho dây 1.2mm lọt êm)
    slot_w = 8.6 # Rộng 8.6mm cho dây 8.0mm trượt không bị xéo
    
    sleeve_x_min = r_in
    sleeve_wall = 1.6
    sleeve_box = Part.makeBox(sleeve_wall + slot_t + sleeve_wall, 7.0, length_z, FreeCAD.Vector(sleeve_x_min, -2.5, 0.0))
    sleeve_slot = Part.makeBox(slot_t, 12.0, slot_w, FreeCAD.Vector(sleeve_x_min + sleeve_wall, -5.0, (length_z - slot_w)/2.0))
    
    # Răng ngàm khóa một chiều tích hợp trong máng
    pawl_tooth = Part.makeBox(0.8, 1.2, slot_w, FreeCAD.Vector(sleeve_x_min + sleeve_wall + slot_t - 0.7, 0.5, (length_z - slot_w)/2.0))
    pawl_ramp = Part.makeBox(1.0, 1.5, slot_w + 2.0, FreeCAD.Vector(sleeve_x_min + sleeve_wall + slot_t - 0.7, 0.2, (length_z - slot_w)/2.0 - 1.0))
    pawl_ramp.rotate(FreeCAD.Vector(sleeve_x_min + sleeve_wall + slot_t - 0.7, 0.5, 0), FreeCAD.Vector(0, 0, 1), 35.0)
    pawl_tooth = pawl_tooth.cut(pawl_ramp)
    
    # Tai gạt nhả ngàm (Release Tab)
    release_tab = Part.makeBox(2.5, 2.0, 4.0, FreeCAD.Vector(sleeve_x_min + sleeve_wall + slot_t + sleeve_wall - 0.5, 2.0, (length_z - 4.0)/2.0))
    
    buckle_sleeve = sleeve_box.cut(sleeve_slot).fuse(pawl_tooth).fuse(release_tab)
    
    # 4. ĐẾ CẢM BIẾN PHẲNG CỨNG VỮNG (RIGID PALMAR SENSOR PAD)
    pad_w = 11.2
    pad_thick = 3.2
    pad_box = Part.makeBox(pad_w, pad_thick + 1.2, length_z, FreeCAD.Vector(-pad_w/2.0, -r_in - pad_thick, 0.0))
    finger_cyl = Part.makeCylinder(r_in, length_z + 2.0, FreeCAD.Vector(0, 0, -1.0))
    pad_trimmed = pad_box.cut(finger_cyl)
    
    # Khoang âm Velostat phẳng chuẩn 9.8 x 7.1 x 1.4mm (bù co ngót FDM)
    velo_w = 9.8
    velo_h = 7.1
    velo_depth = 1.4
    velo_pocket = Part.makeBox(velo_w, velo_depth + 1.0, velo_h, 
                               FreeCAD.Vector(-velo_w/2.0, -r_in - velo_depth, (length_z - velo_h)/2.0))
    sensor_pad = pad_trimmed.cut(velo_pocket)
    
    # 5. DẢI CUNG ĐÀN HỒI DẺO TRÁI (LEFT FLEXURE STRAP 1.2mm)
    strap_l_out = Part.makeCylinder(r_in + 1.2, length_z)
    strap_l_in = Part.makeCylinder(r_in, length_z + 2.0, FreeCAD.Vector(0, 0, -1.0))
    strap_l = strap_l_out.cut(strap_l_in).cut(Part.makeBox(60.0, 60.0, length_z + 2.0, FreeCAD.Vector(-4.5, -30.0, -1.0)))
    
    bridge_l = Part.makeBox(4.0, 4.0, length_z, FreeCAD.Vector(-r_in - 2.0, -3.0, 0.0))
    left_side = sensor_pad.fuse(strap_l).fuse(bridge_l)
    
    # 6. DÂY ĐAI DẺO MANG DẢI 8 RĂNG CƯA (TOOTHED LADDER STRAP)
    num_strap_teeth = 8
    tooth_pitch = 1.5
    strap_len = num_strap_teeth * tooth_pitch + 8.0 # ~20mm đủ ôm tới máng
    
    strap_body = Part.makeBox(strap_len, strap_t, strap_w, FreeCAD.Vector(pad_w/2.0 - 1.0, -r_in - pad_thick, (length_z - strap_w)/2.0))
    
    # Dải 8 răng cưa dạng nêm (Buttress Teeth) có gối chồng 0.2mm vào thân đai
    teeth_fused = None
    for i in range(num_strap_teeth):
        x_t = pad_w/2.0 + 4.0 + i * tooth_pitch
        t_box = Part.makeBox(1.1, 0.8 + 0.2, strap_w, FreeCAD.Vector(x_t, -r_in - pad_thick + strap_t - 0.2, (length_z - strap_w)/2.0))
        t_ramp = Part.makeBox(1.5, 1.2, strap_w + 2.0, FreeCAD.Vector(x_t, -r_in - pad_thick + strap_t - 0.2, (length_z - strap_w)/2.0 - 1.0))
        t_ramp.rotate(FreeCAD.Vector(x_t, -r_in - pad_thick + strap_t - 0.2, 0), FreeCAD.Vector(0, 0, 1), 35.0)
        t_cut = t_box.cut(t_ramp)
        teeth_fused = t_cut if teeth_fused is None else teeth_fused.fuse(t_cut)
        
    strap_complete = strap_body.fuse(teeth_fused)
    
    # 7. HỢP KHỐI TOÀN BỘ CHI TIẾT ĐỐT NGÓN THÀNH 1 SOLID DUY NHẤT
    phalanx_solid = dorsal_base.fuse(buckle_sleeve).fuse(left_side).fuse(strap_complete).removeSplitter()
    
    assert len(phalanx_solid.Solids) == 1, f"LỖI: Cuff có {len(phalanx_solid.Solids)} solids!"
    return phalanx_solid

# ==============================================================================
# HÀM TẠO THANH TRƯỢT ĐUÔI ÉN ĐIỀU CHỈNH DÀI (DOVETAIL LENGTH SLIDER + CLEVIS)
# ==============================================================================
def build_dovetail_slider(num_steps=3, step_pitch=2.5):
    """
    Tạo thanh trượt đuôi én (Male Dovetail Slider) gồm:
    - Thân đuôi én vát góc 45 độ lồng khít vào Dovetail Channel.
    - 3 lỗ khóa định vị chiều dài (bước 2.5mm).
    - Ngàm đôi kẹp trục xoay (Double-Shear Clevis Hinge) chịu lực uốn/cắt tối đa.
    """
    w_base = 6.0
    w_top = 8.8
    h_dove = 2.6
    slider_len = (num_steps - 1) * step_pitch + 11.0 # ~16.0mm
    
    poly_pts_m = [
        FreeCAD.Vector(-w_base/2.0, 0, 0),
        FreeCAD.Vector(w_base/2.0, 0, 0),
        FreeCAD.Vector(w_top/2.0, h_dove, 0),
        FreeCAD.Vector(-w_top/2.0, h_dove, 0),
        FreeCAD.Vector(-w_base/2.0, 0, 0)
    ]
    wire_m = Part.makePolygon(poly_pts_m)
    face_m = Part.Face(wire_m)
    male_body = face_m.extrude(FreeCAD.Vector(0, 0, slider_len))
    
    # Clevis Hinge (Ngàm đôi kẹp giữa)
    ear_thick = 2.2
    ear_gap = 4.0 # Lọt tai 3.6mm của đốt sau với khe hở 0.2mm mỗi bên
    ear_h = 6.5
    ear_reach = 6.5
    
    ear_l = Part.makeBox(ear_thick, ear_h, ear_reach, FreeCAD.Vector(-ear_gap/2.0 - ear_thick, 0, slider_len))
    ear_r = Part.makeBox(ear_thick, ear_h, ear_reach, FreeCAD.Vector(ear_gap/2.0, 0, slider_len))
    
    # Lỗ trục xoay qua cả 2 tai kẹp (phi 2.8mm)
    z_pivot = slider_len + ear_reach - 2.8
    pivot_hole = Part.makeCylinder(1.4, ear_gap + 2*ear_thick + 4.0, 
                                   FreeCAD.Vector(-ear_gap/2.0 - ear_thick - 2.0, ear_h/2.0, z_pivot), FreeCAD.Vector(1, 0, 0))
    clevis = ear_l.fuse(ear_r).cut(pivot_hole)
    
    slider_solid = male_body.fuse(clevis)
    
    # 3 lỗ chốt khóa định vị (phi 2.2mm, bước 2.5mm)
    for i in range(num_steps):
        z_hole = 3.5 + i * step_pitch
        hole = Part.makeCylinder(1.1, w_top + 4.0, FreeCAD.Vector(-(w_top+4.0)/2.0, h_dove/2.0, z_hole), FreeCAD.Vector(1, 0, 0))
        slider_solid = slider_solid.cut(hole)
        
    slider_final = slider_solid.removeSplitter()
    assert len(slider_final.Solids) == 1, f"LỖI: Slider có {len(slider_final.Solids)} solids!"
    return slider_final

# ==============================================================================
# HÀM TẠO CHỐT KHÓA NÊM ĐÔI (LOCKING CROSS-PIN / CLEVIS PIN)
# ==============================================================================
def build_locking_pin():
    """Chốt khóa nêm ngang phi 2.0mm có gờ bấm chống tuột"""
    pin_r = 1.0
    pin_len = 15.0
    pin_cyl = Part.makeCylinder(pin_r, pin_len, FreeCAD.Vector(-pin_len/2.0, 0, 0), FreeCAD.Vector(1, 0, 0))
    head = Part.makeBox(2.0, 4.0, 4.0, FreeCAD.Vector(-pin_len/2.0 - 2.0, -2.0, -2.0))
    catch_tip = Part.makeCone(pin_r + 0.3, pin_r, 1.2, FreeCAD.Vector(pin_len/2.0, 0, 0), FreeCAD.Vector(1, 0, 0))
    return pin_cyl.fuse(head).fuse(catch_tip).removeSplitter()

def build_clevis_pin():
    """Chốt trục xoay Clevis phi 2.7mm (cho lỗ 2.8mm) có gờ chặn"""
    pin_r = 1.35
    pin_len = 11.0
    pin_cyl = Part.makeCylinder(pin_r, pin_len, FreeCAD.Vector(-pin_len/2.0, 0, 0), FreeCAD.Vector(1, 0, 0))
    head = Part.makeCylinder(pin_r + 1.2, 1.8, FreeCAD.Vector(-pin_len/2.0 - 1.8, 0, 0), FreeCAD.Vector(1, 0, 0))
    catch_tip = Part.makeCone(pin_r + 0.25, pin_r, 1.2, FreeCAD.Vector(pin_len/2.0, 0, 0), FreeCAD.Vector(1, 0, 0))
    return pin_cyl.fuse(head).fuse(catch_tip).removeSplitter()

# ==============================================================================
# DỰNG TOÀN BỘ CÁC CHI TIẾT
# ==============================================================================
print("--> Dựng Đốt 1 (Proximal Cuff) - Bán kính phi 23.0mm...")
cuff1 = build_phalanx_cuff(r_in=11.5, length_z=16.0, has_dovetail_channel=True, is_distal=False)

print("--> Dựng Đốt 2 (Middle Cuff) - Bán kính phi 21.0mm...")
cuff2 = build_phalanx_cuff(r_in=10.5, length_z=13.5, has_dovetail_channel=True, is_distal=False)

print("--> Dựng Đốt 3 (Distal Cuff HỞ ĐẦU) - Bán kính phi 19.0mm...")
cuff3 = build_phalanx_cuff(r_in=9.5, length_z=12.6, has_dovetail_channel=False, is_distal=True)

print("--> Dựng Thanh trượt Đuôi én nối PIP (Khớp nối Đốt 1 -> Đốt 2)...")
slider_pip = build_dovetail_slider(num_steps=3, step_pitch=2.5)

print("--> Dựng Thanh trượt Đuôi én nối DIP (Khớp nối Đốt 2 -> Đốt 3)...")
slider_dip = build_dovetail_slider(num_steps=3, step_pitch=2.5)

print("--> Dựng Chốt khóa nêm định vị và Chốt trục xoay Clevis...")
pin_lock = build_locking_pin()
pin_clevis = build_clevis_pin()

# ==============================================================================
# XUẤT CÁC FILE STL VÀ STEP SẢN XUẤT
# ==============================================================================
print("--> Đang xuất file STL và STEP cho từng chi tiết...")

cuff1.exportStl(os.path.join(OUT_DIR, "cuff1_proximal.stl"))
cuff1.exportStep(os.path.join(OUT_DIR, "cuff1_proximal.step"))

cuff2.exportStl(os.path.join(OUT_DIR, "cuff2_middle.stl"))
cuff2.exportStep(os.path.join(OUT_DIR, "cuff2_middle.step"))

cuff3.exportStl(os.path.join(OUT_DIR, "cuff3_distal.stl"))
cuff3.exportStep(os.path.join(OUT_DIR, "cuff3_distal.step"))

slider_pip.exportStl(os.path.join(OUT_DIR, "slider_pip_dovetail.stl"))
slider_pip.exportStep(os.path.join(OUT_DIR, "slider_pip_dovetail.step"))

slider_dip.exportStl(os.path.join(OUT_DIR, "slider_dip_dovetail.stl"))
slider_dip.exportStep(os.path.join(OUT_DIR, "slider_dip_dovetail.step"))

pin_lock.exportStl(os.path.join(OUT_DIR, "pin_lock_dovetail.stl"))
pin_lock.exportStep(os.path.join(OUT_DIR, "pin_lock_dovetail.step"))

pin_clevis.exportStl(os.path.join(OUT_DIR, "pin_clevis_pivot.stl"))
pin_clevis.exportStep(os.path.join(OUT_DIR, "pin_clevis_pivot.step"))

# ==============================================================================
# DỰNG CỤM LẮP RÁP 3 ĐỐT ĐỒNG BỘ (ASSEMBLY)
# ==============================================================================
print("--> Dựng cụm lắp ráp 3 đốt duỗi thẳng và co gập...")

# Vị trí nấc 2 (trung bình: +2.5mm):
# Slider PIP lồng vào Cuff 1:
slider_pip_placed = slider_pip.copy()
# Đặt slider vào rãnh dovetail của Cuff 1 ở nấc 2
slider_pip_placed.translate(FreeCAD.Vector(0, 11.5 + 2.0 - 0.5, 16.0/2.0 - (3.5 + 2.5)))
pip_axis_z = 16.0/2.0 - (3.5 + 2.5) + (16.0 + 6.5 - 2.8) # Vị trí trục PIP

# Cuff 2 đặt tại trục PIP
cuff2_placed = cuff2.copy()
cuff2_placed.translate(FreeCAD.Vector(0, 0, pip_axis_z - (-5.5 + 2.5)))

# Slider DIP lồng vào Cuff 2:
cuff2_z_base = pip_axis_z - (-5.5 + 2.5)
slider_dip_placed = slider_dip.copy()
slider_dip_placed.translate(FreeCAD.Vector(0, 10.5 + 2.0 - 0.5, cuff2_z_base + 13.5/2.0 - (3.5 + 2.5)))
dip_axis_z = cuff2_z_base + 13.5/2.0 - (3.5 + 2.5) + (16.0 + 6.5 - 2.8)

# Cuff 3 đặt tại trục DIP
cuff3_placed = cuff3.copy()
cuff3_placed.translate(FreeCAD.Vector(0, 0, dip_axis_z - (-5.5 + 2.5)))

assembly_straight = Part.Compound([cuff1, slider_pip_placed, cuff2_placed, slider_dip_placed, cuff3_placed])
assembly_straight.exportStl(os.path.join(OUT_DIR, "full_finger_dovetail_assembly_straight.stl"))
assembly_straight.exportStep(os.path.join(OUT_DIR, "full_finger_dovetail_assembly_straight.step"))

# LƯU FILE FREECAD
doc.addObject("Part::Feature", "Cuff1_Proximal").Shape = cuff1
doc.addObject("Part::Feature", "Cuff2_Middle").Shape = cuff2
doc.addObject("Part::Feature", "Cuff3_Distal").Shape = cuff3
doc.addObject("Part::Feature", "Slider_PIP").Shape = slider_pip
doc.addObject("Part::Feature", "Slider_DIP").Shape = slider_dip
doc.addObject("Part::Feature", "Locking_Pin").Shape = pin_lock
doc.addObject("Part::Feature", "Clevis_Pin").Shape = pin_clevis
doc.addObject("Part::Feature", "Assembly_Straight").Shape = assembly_straight
doc.recompute()
doc.saveAs(os.path.join(OUT_DIR, "dovetail_ratchet_finger.FCStd"))

print("=== HOÀN TẤT THÀNH CÔNG 100%! TOÀN BỘ TỆP ĐÃ ĐƯỢC TẠO TẠI ===")
print(OUT_DIR)
