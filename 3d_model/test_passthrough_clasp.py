import sys
import os
import io
import math

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import FreeCAD
import Part
import MeshPart

print("=== KIỂM TRA THỬ NGHIỆM CƠ CẤU HỌNG THOÁT XUYÊN THÂU (PASS-THROUGH CHUTE) ===")

r_in = 11.8
shell_thick = 2.0
length_z = 16.0
knuckle_z_min = 2.4
knuckle_z_max = length_z - 2.4
knuckle_height = knuckle_z_max - knuckle_z_min # 11.2mm

# 1. DỰNG THANH RĂNG CÁI (DORSAL RACK) DÀI ĐỂ ĐÂM XUYÊN QUA HỌNG
rx = r_in + 1.4 # 13.2
rack_thick_x = 2.0
rack_len_y = 14.0 # Dài 14mm để đâm xuyên qua nhiều nấc
rack_w_z = knuckle_height

# Thanh răng phôi
rack_base = Part.makeBox(rack_thick_x, rack_len_y, rack_w_z, FreeCAD.Vector(rx, -rack_len_y + 4.0, knuckle_z_min))

# Vát nhọn đầu dẫn hướng 45 độ
tip_wedge = Part.makeBox(3.0, 3.0, rack_w_z + 2.0, FreeCAD.Vector(rx - 0.5, -rack_len_y + 4.0 - 1.5, knuckle_z_min - 1.0))
tip_wedge.rotate(FreeCAD.Vector(rx, -rack_len_y + 4.0, knuckle_z_min), FreeCAD.Vector(0,0,1), 45.0)
rack_solid = rack_base.cut(tip_wedge)

# Cắt 6 rãnh răng cưa tam giác (Pitch = 1.8mm, depth = 1.0mm)
P = 1.8
depth_tooth = 1.0
ramp_len = 1.25
num_teeth = 6

cutter_list = []
for i in range(num_teeth):
    y_lock = -rack_len_y + 6.0 + i * P
    y_ramp_end = y_lock + ramp_len
    p1 = FreeCAD.Vector(rx + rack_thick_x + 0.5, y_lock, knuckle_z_min - 1.0)
    p2 = FreeCAD.Vector(rx + rack_thick_x - depth_tooth, y_lock, knuckle_z_min - 1.0)
    p3 = FreeCAD.Vector(rx + rack_thick_x + 0.5, y_ramp_end, knuckle_z_min - 1.0)
    w_cut = Part.makePolygon([p1, p2, p3, p1])
    f_cut = Part.Face(w_cut)
    cutter_list.append(f_cut.extrude(FreeCAD.Vector(0, 0, rack_w_z + 2.0)))

for c in cutter_list:
    rack_solid = rack_solid.cut(c)

print(f"Thanh răng cái (Dorsal Rack) valid: {rack_solid.isValid()}, Solids: {len(rack_solid.Solids)}")

# 2. DỰNG HỌNG THOÁT RỖNG 2 ĐẦU (PASS-THROUGH CHUTE) TRÊN THANH GÀI
# Kích thước khe lọt: Khe rộng theo X là 2.5mm (rộng hơn rack 2.0mm là 0.5mm), cao theo Z là 11.8mm
chute_in_x = 2.5
chute_in_y = 12.0
chute_wall = 1.4

chute_x0 = rx - 0.25 # Canh giữa rack
chute_y0 = -rack_len_y + 2.0
chute_outer = Part.makeBox(chute_in_x + chute_wall * 2, chute_in_y, rack_w_z + 0.8, 
                           FreeCAD.Vector(chute_x0 - chute_wall, chute_y0, knuckle_z_min - 0.4))

# Khoét rỗng thông suốt 2 đầu dọc theo trục Y (KHÔNG CÓ VÁCH CHẶN ĐÁY!)
tunnel_cutter = Part.makeBox(chute_in_x, chute_in_y + 4.0, rack_w_z + 0.6,
                             FreeCAD.Vector(chute_x0, chute_y0 - 2.0, knuckle_z_min - 0.3))
chute_sleeve = chute_outer.cut(tunnel_cutter)

# 3. DẦM ĐÀN HỒI MANG RĂNG ĐỰC (CANTILEVER BEAM + PAWL TEETH)
# Cắt rãnh thoát dầm đàn hồi trên vách ngoài (+X) của họng
x_beam = chute_x0 + chute_in_x
beam_thick = 1.3
beam_len = 8.5
beam_box = Part.makeBox(beam_thick, beam_len, rack_w_z - 0.6,
                        FreeCAD.Vector(x_beam, chute_y0 + 2.0, knuckle_z_min + 0.3))

# Răng đực nhô vào lòng họng (-X) ăn khớp với rack
num_pawl_teeth = 2
pawl_list = []
for i in range(num_pawl_teeth):
    y_lock = chute_y0 + 4.0 + i * P
    y_ramp_end = y_lock + ramp_len
    p1 = FreeCAD.Vector(x_beam + 0.2, y_lock, knuckle_z_min + 0.3)
    p2 = FreeCAD.Vector(x_beam - (depth_tooth - 0.15), y_lock, knuckle_z_min + 0.3)
    p3 = FreeCAD.Vector(x_beam + 0.2, y_ramp_end, knuckle_z_min + 0.3)
    w_t = Part.makePolygon([p1, p2, p3, p1])
    f_t = Part.Face(w_t)
    pawl_list.append(f_t.extrude(FreeCAD.Vector(0,0,rack_w_z - 0.6)))

for t in pawl_list:
    beam_box = beam_box.fuse(t)

# Tai mở nhanh (Quick release tab)
release_tab = Part.makeBox(2.6, 2.6, rack_w_z - 0.6,
                          FreeCAD.Vector(x_beam + beam_thick, chute_y0 + 2.0 + beam_len - 2.6, knuckle_z_min + 0.3))
compliant_pawl = beam_box.fuse(release_tab)

# Gộp họng thoát với dầm đàn hồi
chute_complete = chute_sleeve.fuse(compliant_pawl).removeSplitter()
print(f"Họng thoát (Pass-through Chute) valid: {chute_complete.isValid()}, Solids: {len(chute_complete.Solids)}")

# 4. KIỂM TRA MÔ PHỎNG ĐÂM XUYÊN CÁC NẤC (NOTCH 1 -> 5)
print("\n--> Kiểm tra thanh răng cái đâm xuyên tự do qua họng thoát:")
for step in range(num_teeth):
    r_pos = rack_solid.copy()
    r_pos.translate(FreeCAD.Vector(0, step * P, 0))
    vol = chute_complete.common(r_pos).Volume
    print(f"    Nấc {step + 1} (Ăn sâu thêm {step * P:.1f}mm): Thể tích giao thoa = {vol:.4f} mm3")

# 5. XUẤT LƯỚI FDM VÀ KIỂM TRA TÍNH TOÀN VẸN MANIFOLD
mesh = MeshPart.meshFromShape(chute_complete, MaxLength=0.5)
print(f"\n--> Tạo lưới FDM thành công: {len(mesh.Facets)} tam giác.")
print(f"    Lưới khép kín (isSolid): {mesh.isSolid()}")
print(f"    Lưới không có đa giác trùng (hasNonManifolds): {mesh.hasNonManifolds()}")
assert mesh.isSolid() and not mesh.hasNonManifolds(), "LỖI LƯỚI NON-MANIFOLD!"
print("=== THÀNH CÔNG RỰC RỠ: LƯỚI HOÀN TOÀN SOLID VÀ KHÔNG LỖI MANIFOLD! ===")
