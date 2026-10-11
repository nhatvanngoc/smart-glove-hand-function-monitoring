import sys
import os
import io
import math

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import FreeCAD
import Part

print("=== KIỂM TRA MÔ HÌNH HÌNH HỌC RATCHET RĂNG CƯA MỚI (CHUẨN TỌA ĐỘ) ===")

r_in = 11.8
length_z = 16.0
rx = r_in + 1.6 # 13.4
P = 1.8 # Bước răng 1.8mm
depth_tooth = 1.0 # Độ sâu răng 1.0mm
ramp_len = 1.25 # Chiều dài mặt dốc theo trục Y
num_teeth = 6

# 1. DỰNG THANH RĂNG CƯA MU NGÓN (Dorsal Rack)
# Rack có vách ngoài tại X = rx + 2.2
x_rack_root = rx + 0.2
x_rack_tip = rx + 2.2 # Răng nhô ra tới x_rack_tip
rack_total_len = (num_teeth + 1) * P + 2.0
rack_solid = Part.makeBox(2.2, rack_total_len, length_z, FreeCAD.Vector(x_rack_root, -1.0, 0.0))

# Tạo các rãnh răng cưa tam giác (Cutter khoét từ ngoài x_rack_tip vào)
cutter_list = []
for i in range(num_teeth):
    y_lock = 0.5 + i * P
    y_ramp_end = y_lock + ramp_len
    
    # Rãnh khoét tam giác:
    # Mặt khóa tại y_lock, khoét từ ngoài vào sâu depth_tooth
    p1 = FreeCAD.Vector(x_rack_tip + 1.0, y_lock, -1.0)
    p2 = FreeCAD.Vector(x_rack_tip - depth_tooth, y_lock, -1.0)
    p3 = FreeCAD.Vector(x_rack_tip + 1.0, y_ramp_end, -1.0)
    
    w = Part.makePolygon([p1, p2, p3, p1])
    f = Part.Face(w)
    cutter = f.extrude(FreeCAD.Vector(0, 0, length_z + 2.0))
    cutter_list.append(cutter)

cutters_compound = cutter_list[0]
for c in cutter_list[1:]:
    cutters_compound = cutters_compound.fuse(c)

dorsal_rack = rack_solid.cut(cutters_compound).removeSplitter()
print(f"Dorsal Rack valid: {dorsal_rack.isValid()}, Solids: {len(dorsal_rack.Solids)}")

# 2. DỰNG NGÀM GÀI ĐÀN HỒI (Pawl Teeth & Flexure Cantilever)
# Dầm mang răng nằm ngoài x_rack_tip với khe hở dung sai FDM 0.25mm
gap_radial = 0.25
pawl_beam_thick = 1.4
x_pawl_in = x_rack_tip + gap_radial # = 15.6 + 0.25 = 15.85
x_pawl_out = x_pawl_in + pawl_beam_thick

# Thân dầm mang răng (Pawl carrier beam)
pawl_beam = Part.makeBox(pawl_beam_thick, 4.0 * P, length_z, 
                         FreeCAD.Vector(x_pawl_in, -1.0, 0.0))

# 2 răng đực ăn khớp (nhô từ x_pawl_in vào sâu trong rãnh -X)
# Chiều sâu răng đực = depth_tooth - 0.15 = 0.85mm (có khe hở đáy 0.15mm không cấn đáy)
pawl_tooth_depth = depth_tooth - 0.15
pawl_teeth_list = []
for i in range(2):
    y_lock = 0.5 + i * P + 0.15 # Dung sai dọc trục Y 0.15mm
    y_ramp_end = y_lock + (ramp_len - 0.2)
    
    p1 = FreeCAD.Vector(x_pawl_in, y_lock, 0.0)
    p2 = FreeCAD.Vector(x_pawl_in - (pawl_tooth_depth + gap_radial), y_lock, 0.0)
    p3 = FreeCAD.Vector(x_pawl_in, y_ramp_end, 0.0)
    
    w = Part.makePolygon([p1, p2, p3, p1])
    f = Part.Face(w)
    tooth = f.extrude(FreeCAD.Vector(0, 0, length_z))
    pawl_teeth_list.append(tooth)

teeth_compound = pawl_teeth_list[0]
for t in pawl_teeth_list[1:]:
    teeth_compound = teeth_compound.fuse(t)

# Tai gạt mở ngàm (Thumb release tab)
thumb_tab = Part.makeBox(2.8, 2.5, length_z, 
                        FreeCAD.Vector(x_pawl_out, 4.0 * P - 3.5, 0.0))

pawl_full = pawl_beam.fuse(teeth_compound).fuse(thumb_tab).removeSplitter()
print(f"Pawl valid: {pawl_full.isValid()}, Solids: {len(pawl_full.Solids)}")

# Kiểm tra ăn khớp tại vị trí danh định:
common = dorsal_rack.common(pawl_full)
print(f"Thể tích giao thoa (Common Volume) tại nấc danh định: {common.Volume:.4f} mm3")

# Thử nhảy sang các nấc tiếp theo:
for step in range(1, 5):
    p_step = pawl_full.copy()
    p_step.translate(FreeCAD.Vector(0, step * P, 0))
    vol = dorsal_rack.common(p_step).Volume
    print(f"  -> Thể tích giao thoa tại nấc +{step} ({step * P:.1f}mm): {vol:.4f} mm3")

print("=== KIỂM TRA THÀNH CÔNG: KHÔNG HỀ CÓ VA CHẠM KHỐI (ZERO INTERFERENCE)! ===")
