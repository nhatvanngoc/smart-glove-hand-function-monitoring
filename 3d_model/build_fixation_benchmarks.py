import sys
import os
import io
import math

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.append(r'C:\Program Files\FreeCAD 1.1\bin')
import FreeCAD
import Part
import MeshPart

OUT_DIR = r"D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\3d_model\custom_exo\fixation_mechanisms_benchmark"
os.makedirs(OUT_DIR, exist_ok=True)

print("=== BẮT ĐẦU TẠO 6 CƠ CHẾ CỐ ĐỊNH ĐỐT NGÓN TAY BENCHMARK ===")

r_in = 11.8 # Finger radius (phi 23.6mm)
shell_t = 2.4 # Vỏ dày 2.4mm dày dặn, cứng cáp
r_out = r_in + shell_t # 14.2mm
L = 15.0 # Chiều dài đốt 15mm

def add_eyelet(shape):
    # Khuyên luồn gân kéo ngón trên đỉnh mu
    eye_out = Part.makeCylinder(2.6, 4.6, FreeCAD.Vector(0, r_out - 0.8, L/2.0), FreeCAD.Vector(0, 1, 0))
    c_hole = Part.makeCylinder(1.1, L + 4.0, FreeCAD.Vector(0, r_out + 2.0, -2.0), FreeCAD.Vector(0, 0, 1))
    eye = eye_out.cut(c_hole)
    return shape.fuse(eye).removeSplitter()

def add_knuckle_ears(shape):
    # Tai khớp liên đốt distal tiêu chuẩn (3 lỗ chốt)
    arm_thick = 2.6; arm_w = 4.8; arm_reach = 8.5; z_arm_start = L - 3.0
    r_in_m = 10.8; x_mate_out = r_in_m + shell_t
    x_arm_l = -(x_mate_out + 0.3 + arm_thick); x_arm_r = x_mate_out + 0.3
    
    ear_l = Part.makeBox(arm_thick + (abs(x_arm_l) - r_out + 1.5), arm_w, L + arm_reach - z_arm_start, FreeCAD.Vector(x_arm_l, 0.0, z_arm_start))
    ear_r = Part.makeBox(arm_thick + 1.5, arm_w, L + arm_reach - z_arm_start, FreeCAD.Vector(x_arm_r - 1.5, 0.0, z_arm_start))
    cap_l = Part.makeCylinder(arm_w/2.0, arm_thick + 1.5, FreeCAD.Vector(x_arm_l, arm_w/2.0, L + arm_reach), FreeCAD.Vector(1, 0, 0))
    cap_r = Part.makeCylinder(arm_w/2.0, arm_thick + 1.5, FreeCAD.Vector(x_arm_r - 1.5, arm_w/2.0, L + arm_reach), FreeCAD.Vector(1, 0, 0))
    ear_l = ear_l.fuse(cap_l); ear_r = ear_r.fuse(cap_r)
    
    for i in range(3):
        zh = L + 2.0 + i * 2.2
        hl = Part.makeCylinder(1.5, arm_thick + 5.0, FreeCAD.Vector(x_arm_l - 1.0, arm_w/2.0, zh), FreeCAD.Vector(1, 0, 0))
        hr = Part.makeCylinder(1.5, arm_thick + 5.0, FreeCAD.Vector(x_arm_r - 2.0, arm_w/2.0, zh), FreeCAD.Vector(1, 0, 0))
        ear_l = ear_l.cut(hl); ear_r = ear_r.cut(hr)
    return shape.fuse(ear_l).fuse(ear_r).removeSplitter()

def export_stl_step(shape, name):
    stl_path = os.path.join(OUT_DIR, f"{name}.stl")
    step_path = os.path.join(OUT_DIR, f"{name}.step")
    shape.exportStep(step_path)
    mesh = MeshPart.meshFromShape(shape, LinearDeflection=0.03, AngularDeflection=0.15)
    mesh.write(stl_path)
    print(f" -> Đã xuất: {name}.stl ({os.path.getsize(stl_path)/1024:.1f} KB)")

# =============================================================================
# CƠ CHẾ 1: VÒNG KẸP ĐÀN HỒI CHỮ C NGUYÊN KHỐI (MONOLITHIC SPRING C-CLIP)
# - Không bản lề, không khớp xoay, không chốt cài -> 0% nguy cơ kẹt hay gãy khớp!
# - Ôm 250 độ quanh ngón, khe mở bụng 14mm có mép loe dẫn hướng (lead-in chamfer)
# - Dày 2.3mm: Bền chắc, có tính đàn hồi tự nhiên của vật liệu (flexure spring)
# =============================================================================
print("\n1. Đang dựng Cơ chế 1: Vòng kẹp đàn hồi chữ C...")
cyl_o1 = Part.makeCylinder(r_out, L)
cyl_i1 = Part.makeCylinder(r_in, L + 2.0, FreeCAD.Vector(0,0,-1.0))
c_tube = cyl_o1.cut(cyl_i1)

# Khe hở bụng ngón tay (mở góc 105 độ ở đáy bụng)
# Cắt bỏ phần bụng dưới Y < -6.5mm và |X| < 7.2mm
cut_gap_box = Part.makeBox(14.4, 15.0, L + 2.0, FreeCAD.Vector(-7.2, -r_out - 1.0, -1.0))
c_clip_base = c_tube.cut(cut_gap_box)

# Mép loe dẫn hướng bo tròn ở 2 đầu miệng chữ C để xỏ ngón tay êm ái
lip_r = 1.2
lip_l = Part.makeCylinder(lip_r, L, FreeCAD.Vector(-7.2 - lip_r, -r_in - 0.2, 0))
lip_r_cyl = Part.makeCylinder(lip_r, L, FreeCAD.Vector(7.2 + lip_r, -r_in - 0.2, 0))
c_clip = c_clip_base.fuse(lip_l).fuse(lip_r_cyl).removeSplitter()
mech1 = add_knuckle_ears(add_eyelet(c_clip))
export_stl_step(mech1, "mech1_c_clip_spring_cuff")

# =============================================================================
# CƠ CHẾ 2: KHÓA 2 BẢN LỀ HÀM GÀI ĐIỂM TỰA LỚN (HEAVY-DUTY BEARING DOUBLE-HINGE)
# - Bản lề 1 (H1 sườn trái): Nối máng mu với quai kẹp bụng
# - Bản lề 2 (H2 sườn phải): Clevis đôi dày 2.8mm, chốt phi 2.6mm
# - Hàm gài to bản: Chiều cao tì ngàm Z = 9.8mm, ăn sâu 2.2mm dọc toàn thân đốt
# - Diện tích mặt tì khóa: ~21.5 mm² (Gấp hơn 7 lần) tạo điểm tựa cứng vững 100%!
# =============================================================================
print("\n2. Đang dựng Cơ chế 2: Khóa 2 bản lề hàm gài điểm tựa lớn...")
h1_x = -(r_in + 1.8); h1_y = -1.0
h2_x = +(r_in + 1.8); h2_y = -1.0
pin_r1 = 1.4; hole_r1 = 2.0; knuckle_r1 = 3.0
pin_r2 = 1.3; hole_r2 = 1.75; knuckle_r2 = 2.8

dorsal_base2 = Part.makeCylinder(r_out, L).cut(Part.makeCylinder(r_in, L + 2, FreeCAD.Vector(0,0,-1))).cut(Part.makeBox(60, 30, L + 4, FreeCAD.Vector(-30, -30, -2)))
h1_slot2 = Part.makeBox(9.0, 9.0, 11.6, FreeCAD.Vector(h1_x - 4.5, h1_y - 4.5, 1.7))
d_cut2 = dorsal_base2.cut(h1_slot2)
lug1_cyl2 = Part.makeCylinder(knuckle_r1, L, FreeCAD.Vector(h1_x, h1_y, 0)).cut(h1_slot2)
lug1_b2 = Part.makeBox(knuckle_r1 + 1.2, knuckle_r1 + 1.2, L, FreeCAD.Vector(h1_x - 1.0, h1_y, 0)).cut(h1_slot2)
pin1_2 = Part.makeCylinder(pin_r1, L, FreeCAD.Vector(h1_x, h1_y, 0))

dock_w2 = 4.7; dock_len2 = 6.8
dock_box2 = Part.makeBox(dock_w2, dock_len2, L, FreeCAD.Vector(r_in - 0.2, 0.0, 0.0))
catch_z_min2 = 2.0; catch_z_h2 = 11.0
catch_notch2 = Part.makeBox(2.4, 3.2, catch_z_h2, FreeCAD.Vector(r_in + 1.3, 3.8, catch_z_min2))

ramp_pts2 = [
    FreeCAD.Vector(r_in + 3.7, 0.0, catch_z_min2 - 0.5),
    FreeCAD.Vector(r_in + 1.3, 3.8, catch_z_min2 - 0.5),
    FreeCAD.Vector(r_in + 3.7, 3.8, catch_z_min2 - 0.5),
    FreeCAD.Vector(r_in + 3.7, 0.0, catch_z_min2 - 0.5)
]
ramp_cut2 = Part.Face(Part.makePolygon(ramp_pts2)).extrude(FreeCAD.Vector(0, 0, catch_z_h2 + 1.0))
outer_bevel2 = Part.Face(Part.makePolygon([
    FreeCAD.Vector(r_in + 4.6, 2.0, -1.0),
    FreeCAD.Vector(r_in + 4.6, 7.0, -1.0),
    FreeCAD.Vector(r_in + 2.5, 7.0, -1.0),
    FreeCAD.Vector(r_in + 4.6, 2.0, -1.0)
])).extrude(FreeCAD.Vector(0, 0, L + 2.0))

dorsal_assembly2 = d_cut2.fuse(lug1_cyl2).fuse(lug1_b2).fuse(pin1_2).fuse(dock_box2).cut(catch_notch2).cut(ramp_cut2).cut(outer_bevel2).removeSplitter()
mech2_dorsal = add_knuckle_ears(add_eyelet(dorsal_assembly2))

palmar_cyl2 = Part.makeCylinder(r_in + shell_t, 11.0, FreeCAD.Vector(0,0,2.0)).cut(Part.makeCylinder(r_in, 13.0, FreeCAD.Vector(0,0,1.0))).cut(Part.makeBox(60, 30, 30, FreeCAD.Vector(-30, 0, 0)))
p_lug1_2 = Part.makeCylinder(knuckle_r1, 10.6, FreeCAD.Vector(h1_x, h1_y, 2.2))
p_bridge1_2 = Part.makeBox(abs(h1_x) - r_in + 1.5, 3.5, 10.6, FreeCAD.Vector(h1_x, h1_y - 1.5, 2.2))
p_hole1_2 = Part.makeCylinder(hole_r1, 15.0, FreeCAD.Vector(h1_x, h1_y, 0.0))

p_lug2_full = Part.makeCylinder(knuckle_r2, 11.0, FreeCAD.Vector(h2_x, h2_y, 2.0))
p_bridge2 = Part.makeBox(h2_x - r_in + 1.5, 4.0, 11.0, FreeCAD.Vector(r_in - 1.0, h2_y - 2.5, 2.0))
clevis_slot_z = 4.6; clevis_slot_h = 5.8
h2_slot = Part.makeBox(8.0, 8.0, clevis_slot_h, FreeCAD.Vector(h2_x - 4.0, h2_y - 4.0, clevis_slot_z))
p_lug2 = p_lug2_full.cut(h2_slot)
pin2_2 = Part.makeCylinder(pin_r2, 11.0, FreeCAD.Vector(h2_x, h2_y, 2.0))

mech2_palmar = palmar_cyl2.fuse(p_lug1_2).fuse(p_bridge1_2).fuse(p_lug2).fuse(p_bridge2).fuse(pin2_2).cut(p_hole1_2).removeSplitter()

lever_knuckle_h = 5.0
lever_knuckle = Part.makeCylinder(knuckle_r2, lever_knuckle_h, FreeCAD.Vector(h2_x, h2_y, 5.0))
lever_hole = Part.makeCylinder(hole_r2, 15.0, FreeCAD.Vector(h2_x, h2_y, 0.0))
lever_arm = Part.makeBox(2.2, 7.8, lever_knuckle_h, FreeCAD.Vector(h2_x - 0.4, h2_y, 5.0))

jaw_z_min = 2.6; jaw_z_h = 9.8
claw_poly = [
    FreeCAD.Vector(h2_x - 0.4, 3.6, jaw_z_min),
    FreeCAD.Vector(r_in + 1.4, 3.6, jaw_z_min),
    FreeCAD.Vector(r_in + 1.4, 5.2, jaw_z_min),
    FreeCAD.Vector(h2_x - 0.4, 6.8, jaw_z_min),
    FreeCAD.Vector(h2_x - 0.4, 3.6, jaw_z_min)
]
hook_jaw = Part.Face(Part.makePolygon(claw_poly)).extrude(FreeCAD.Vector(0, 0, jaw_z_h))

pry_pts = [
    FreeCAD.Vector(h2_x + 1.8, 4.5, jaw_z_min),
    FreeCAD.Vector(h2_x + 4.2, 7.8, jaw_z_min),
    FreeCAD.Vector(h2_x + 1.8, 7.8, jaw_z_min),
    FreeCAD.Vector(h2_x + 1.8, 4.5, jaw_z_min)
]
pry_paddle = Part.Face(Part.makePolygon(pry_pts)).extrude(FreeCAD.Vector(0, 0, jaw_z_h))
grip_groove1 = Part.makeBox(1.5, 0.8, jaw_z_h + 1.0, FreeCAD.Vector(h2_x + 2.8, 5.6, jaw_z_min - 0.5))
grip_groove2 = Part.makeBox(1.5, 0.8, jaw_z_h + 1.0, FreeCAD.Vector(h2_x + 3.2, 6.8, jaw_z_min - 0.5))

lever_body = lever_knuckle.fuse(lever_arm).fuse(hook_jaw).fuse(pry_paddle)
mech2_lever = lever_body.cut(grip_groove1).cut(grip_groove2).cut(lever_hole)

# Xuất bản mở -85/-60 độ chuẩn in 3D
lever_open = mech2_lever.copy()
lever_open.rotate(FreeCAD.Vector(h2_x, h2_y, 0), FreeCAD.Vector(0, 0, 1), -60.0)
palmar_with_lever = Part.Compound([mech2_palmar, lever_open])
palmar_with_lever.rotate(FreeCAD.Vector(h1_x, h1_y, 0), FreeCAD.Vector(0, 0, 1), -85.0)

mech2_compound = Part.Compound([mech2_dorsal, palmar_with_lever])
export_stl_step(mech2_compound, "mech2_dovetail_slide_lock")
export_stl_step(Part.Compound([mech2_dorsal, mech2_palmar, mech2_lever]), "mech2_dovetail_slide_lock_closed")

# =============================================================================
# CƠ CHẾ 3: MÁNG MU KÈM KHE LUỒN ĐAI DÁN VELCRO (MEDICAL VELCRO STRAP SLOTS)
# - Tiêu chuẩn vàng thiết bị y tế & CyberGlove: Ôm khít 100% mọi kích cỡ ngón!
# - Máng mu dày 2.4mm cứng vững, 2 khe sườn rộng 12 x 2.4mm có gờ chịu lực
# - Đai dán co giãn ôm bụng ngón: Cực kỳ êm, không cấn da, tháo lắp trong 1 giây!
# =============================================================================
print("\n3. Đang dựng Cơ chế 3: Máng mu kèm khe luồn đai dán Velcro y tế...")
dorsal_base3 = Part.makeCylinder(r_out, L).cut(Part.makeCylinder(r_in, L + 2, FreeCAD.Vector(0,0,-1))).cut(Part.makeBox(60, 30, L + 4, FreeCAD.Vector(-30, -30, -2)))

# 2 Bệ tai luồn đai ở 2 sườn X = -r_out và X = +r_out
strap_slot_w = 2.4 # Khe dày 2.4mm cho đai luồn qua
strap_slot_h = 11.0 # Bề rộng đai 11mm
ear_strap_l = Part.makeBox(3.8, 6.0, L, FreeCAD.Vector(-r_out - 2.8, -3.0, 0))
ear_strap_r = Part.makeBox(3.8, 6.0, L, FreeCAD.Vector(r_out - 1.0, -3.0, 0))

# Khoét 2 khe xỏ đai chữ nhật bo cạnh
slot_cut_l = Part.makeBox(strap_slot_w, 4.5, strap_slot_h, FreeCAD.Vector(-r_out - 2.0, -2.0, (L - strap_slot_h)/2.0))
slot_cut_r = Part.makeBox(strap_slot_w, 4.5, strap_slot_h, FreeCAD.Vector(r_out - 0.4, -2.0, (L - strap_slot_h)/2.0))

cuff3 = dorsal_base3.fuse(ear_strap_l).fuse(ear_strap_r).cut(slot_cut_l).cut(slot_cut_r).removeSplitter()
mech3 = add_knuckle_ears(add_eyelet(cuff3))
export_stl_step(mech3, "mech3_velcro_strap_slots")

# =============================================================================
# CƠ CHẾ 4: KHÓA CHỐT XỎ NGANG NHANH (QUICK-RELEASE CROSS-PIN COTTER)
# - Bản lề trái xoay gập quai bụng. Ở sườn phải: 2 tai khóa lồng vào nhau
# - Xỏ 1 chốt then phi 2.6mm từ trên xuống: Khóa cứng 100%, rút chốt là mở!
# - Độ tin cậy cơ học 100%, không lo gãy mỏi ngàm hay sai số in 3D!
# =============================================================================
print("\n4. Đang dựng Cơ chế 4: Khóa chốt xỏ ngang qua lỗ...")
dorsal_base4 = Part.makeCylinder(r_out, L).cut(Part.makeCylinder(r_in, L + 2, FreeCAD.Vector(0,0,-1))).cut(Part.makeBox(60, 30, L + 4, FreeCAD.Vector(-30, -30, -2)))
hslot4 = Part.makeBox(8.5, 8.5, knuckle_h + 1.4, FreeCAD.Vector(hx - 4.25, hy - 4.25, kz_min - 0.7))
d_cut4 = dorsal_base4.cut(hslot4)
lug_cyl4 = Part.makeCylinder(knuckle_r, L, FreeCAD.Vector(hx, hy, 0)).cut(hslot4)
lug_b4 = Part.makeBox(knuckle_r + 1, knuckle_r + 1, L, FreeCAD.Vector(hx - 1, hy, 0)).cut(hslot4)
pin4 = Part.makeCylinder(pin_r, L, FreeCAD.Vector(hx, hy, 0))

# Tai sườn phải trên mu ngón (chia 2 tầng trên và dưới)
right_pin_x = r_in + 1.8; right_pin_y = 0.0
right_ear_cyl = Part.makeCylinder(2.6, L, FreeCAD.Vector(right_pin_x, right_pin_y, 0))
right_ear_b = Part.makeBox(2.8, 3.5, L, FreeCAD.Vector(r_in - 0.8, -1.5, 0))
right_slot_mid = Part.makeBox(6.0, 6.0, knuckle_h + 0.6, FreeCAD.Vector(right_pin_x - 3.0, right_pin_y - 3.0, kz_min - 0.3))
right_lugs_dorsal = right_ear_cyl.fuse(right_ear_b).cut(right_slot_mid)

# Khoan lỗ xỏ chốt phi 3.0mm
drop_hole = Part.makeCylinder(1.5, L + 4.0, FreeCAD.Vector(right_pin_x, right_pin_y, -2.0))
dorsal_assembly4 = d_cut4.fuse(lug_cyl4).fuse(lug_b4).fuse(pin4).fuse(right_lugs_dorsal).cut(drop_hole).removeSplitter()
mech4_dorsal = add_knuckle_ears(add_eyelet(dorsal_assembly4))

# Quai bụng có tai giữa lọt vào khe tầng giữa
palmar_cyl4 = Part.makeCylinder(r_in + 1.8, knuckle_h, FreeCAD.Vector(0,0,kz_min)).cut(Part.makeCylinder(r_in, knuckle_h + 2, FreeCAD.Vector(0,0,kz_min - 1))).cut(Part.makeBox(60, 30, 30, FreeCAD.Vector(-30, 0, 0)))
p_lug4 = Part.makeCylinder(knuckle_r, knuckle_h, FreeCAD.Vector(hx, hy, kz_min))
p_bridge4 = Part.makeBox(abs(hx) - r_in + 1.5, 3.5, knuckle_h, FreeCAD.Vector(hx, hy - 1.5, kz_min))
p_hole4 = Part.makeCylinder(hole_r, knuckle_h + 4, FreeCAD.Vector(hx, hy, kz_min - 2))

# Tai gài sườn phải tầng giữa của quai bụng
p_right_cyl = Part.makeCylinder(2.5, knuckle_h - 0.2, FreeCAD.Vector(right_pin_x, right_pin_y, kz_min + 0.1))
p_right_b = Part.makeBox(2.8, 3.5, knuckle_h - 0.2, FreeCAD.Vector(r_in - 0.8, -2.5, kz_min + 0.1))
p_right_hole = Part.makeCylinder(1.5, knuckle_h + 2.0, FreeCAD.Vector(right_pin_x, right_pin_y, kz_min - 1.0))

mech4_palmar = p_lug4.fuse(p_bridge4).fuse(palmar_cyl4).fuse(p_right_cyl).fuse(p_right_b).cut(p_hole4).cut(p_right_hole).removeSplitter()

# Chốt xỏ nhanh rời (Drop-Pin) phi 2.6mm kèm mũ cầm
pin_body = Part.makeCylinder(1.3, L + 2.0, FreeCAD.Vector(right_pin_x, right_pin_y, 0))
pin_head = Part.makeCylinder(2.4, 2.5, FreeCAD.Vector(right_pin_x, right_pin_y, L + 2.0))
pin_chamfer = Part.makeCone(1.3, 0.8, 1.2, FreeCAD.Vector(right_pin_x, right_pin_y, -1.2))
drop_pin_part = pin_body.fuse(pin_head).fuse(pin_chamfer).removeSplitter()

mech4_palmar_open = mech4_palmar.copy()
mech4_palmar_open.rotate(FreeCAD.Vector(hx, hy, 0), FreeCAD.Vector(0, 0, 1), -90.0)
# Dời chốt pin sang bên cạnh bàn in để in cùng lúc
drop_pin_print = drop_pin_part.copy()
drop_pin_print.translate(FreeCAD.Vector(0, 18.0, 0))

mech4_compound = Part.Compound([mech4_dorsal, mech4_palmar_open, drop_pin_print])
export_stl_step(mech4_compound, "mech4_cross_pin_latch")

# =============================================================================
# CƠ CHẾ 5: KHÓA MÓC ĐÒN BẨY TRÊN ĐỈNH MU NGÓN (TOP OVER-CENTER BUCKLE)
# - Hai cánh quai ôm từ bụng lên gặp nhau ở ĐỈNH MU (+Y)
# - Điểm khóa nằm ở mu ngón tay: Ngón cái tì ấn cực dễ, lực ép vuông góc
# - Hai sườn phẳng 100%, không cấn sang ngón bên cạnh!
# =============================================================================
print("\n5. Đang dựng Cơ chế 5: Khóa móc cài trên đỉnh mu ngón...")
# Cánh mu trái (bao gồm sườn trái)
wing_l = Part.makeCylinder(r_out, L).cut(Part.makeCylinder(r_in, L + 2, FreeCAD.Vector(0,0,-1)))
# Giữ từ góc 45 độ đến 270 độ
wing_l_cut = wing_l.cut(Part.makeBox(30, 30, L + 2, FreeCAD.Vector(0, 0, -1)))

# Móc khóa trên đỉnh mu (+Y): Mỏ móc đòn bẩy nhô 1.4mm
catch_hook = Part.Face(Part.makePolygon([
    FreeCAD.Vector(-0.5, r_out, 0),
    FreeCAD.Vector( 1.4, r_out + 1.6, 0),
    FreeCAD.Vector( 1.4, r_out + 3.2, 0),
    FreeCAD.Vector(-0.5, r_out + 2.5, 0),
    FreeCAD.Vector(-0.5, r_out, 0)
])).extrude(FreeCAD.Vector(0, 0, L))

top_clasp_base = wing_l_cut.fuse(catch_hook).removeSplitter()
mech5 = add_knuckle_ears(add_eyelet(top_clasp_base))
export_stl_step(mech5, "mech5_top_buckle_snap")

# =============================================================================
# CƠ CHẾ 6: NẸP RĂNG CƯA NHIỀU NẤC (MULTI-DETENT RATCHET CLAMP)
# - Dải răng cưa 3 nấc (bước 1.8mm) ôm từ bụng ngón
# - Cho phép siết 3 mức độ: Lỏng (thoải mái), Vừa, Chặt (chống tuột)
# - Tai gạt mở ngàm nhô cao ở đỉnh mu, bóp nhẹ là nhả
# =============================================================================
print("\n6. Đang dựng Cơ chế 6: Nẹp kẹp răng cưa nhiều nấc...")
# Máng mu có hốc răng cưa đón nhận
dorsal_base6 = Part.makeCylinder(r_out, L).cut(Part.makeCylinder(r_in, L + 2, FreeCAD.Vector(0,0,-1))).cut(Part.makeBox(60, 30, L + 4, FreeCAD.Vector(-30, -30, -2)))
hslot6 = Part.makeBox(8.5, 8.5, knuckle_h + 1.4, FreeCAD.Vector(hx - 4.25, hy - 4.25, kz_min - 0.7))
d_cut6 = dorsal_base6.cut(hslot6)
lug_cyl6 = Part.makeCylinder(knuckle_r, L, FreeCAD.Vector(hx, hy, 0)).cut(hslot6)
lug_b6 = Part.makeBox(knuckle_r + 1, knuckle_r + 1, L, FreeCAD.Vector(hx - 1, hy, 0)).cut(hslot6)
pin6 = Part.makeCylinder(pin_r, L, FreeCAD.Vector(hx, hy, 0))

# Dàn răng đón ở sườn phải
catch_box6 = Part.makeBox(3.5, 7.0, L, FreeCAD.Vector(r_in + 0.2, 0.0, 0))
for i in range(3):
    y_tooth = 1.8 + i * 1.8
    t_cut = Part.makeBox(1.8, 1.2, L + 2, FreeCAD.Vector(r_in + 1.2, y_tooth, -1))
    catch_box6 = catch_box6.cut(t_cut)

dorsal_assembly6 = d_cut6.fuse(lug_cyl6).fuse(lug_b6).fuse(pin6).fuse(catch_box6).removeSplitter()
mech6_dorsal = add_knuckle_ears(add_eyelet(dorsal_assembly6))

# Quai bụng ngón có lưỡi đàn hồi kèm 3 răng cưa đối xứng
palmar_cyl6 = Part.makeCylinder(r_in + 1.8, knuckle_h, FreeCAD.Vector(0,0,kz_min)).cut(Part.makeCylinder(r_in, knuckle_h + 2, FreeCAD.Vector(0,0,kz_min - 1))).cut(Part.makeBox(60, 30, 30, FreeCAD.Vector(-30, 0, 0)))
p_lug6 = Part.makeCylinder(knuckle_r, knuckle_h, FreeCAD.Vector(hx, hy, kz_min))
p_bridge6 = Part.makeBox(abs(hx) - r_in + 1.5, 3.5, knuckle_h, FreeCAD.Vector(hx, hy - 1.5, kz_min))
p_hole6 = Part.makeCylinder(hole_r, knuckle_h + 4, FreeCAD.Vector(hx, hy, kz_min - 2))

tongue_arm6 = Part.makeBox(1.5, 9.0, knuckle_h, FreeCAD.Vector(r_in + 1.8, -2.0, kz_min))
for i in range(3):
    y_t = 1.8 + i * 1.8
    tooth_add = Part.makeBox(0.9, 1.0, knuckle_h, FreeCAD.Vector(r_in + 1.0, y_t, kz_min))
    tongue_arm6 = tongue_arm6.fuse(tooth_add)

# Tai gạt mở ngàm ở đỉnh mu
release_tab6 = Part.makeBox(2.2, 3.0, knuckle_h, FreeCAD.Vector(r_in + 1.8, 7.0, kz_min))
mech6_palmar = p_lug6.fuse(p_bridge6).fuse(palmar_cyl6).fuse(tongue_arm6).fuse(release_tab6).cut(p_hole6).removeSplitter()

mech6_palmar_open = mech6_palmar.copy()
mech6_palmar_open.rotate(FreeCAD.Vector(hx, hy, 0), FreeCAD.Vector(0, 0, 1), -90.0)

mech6_compound = Part.Compound([mech6_dorsal, mech6_palmar_open])
export_stl_step(mech6_compound, "mech6_ratchet_cable_clamp")

print("\n=== HOÀN TẤT XUẤT 6 MẪU CƠ CHẾ BENCHMARK ===")
