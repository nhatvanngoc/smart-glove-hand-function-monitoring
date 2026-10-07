#!/usr/bin/env python3
"""
Khung ốp 1 đốt ngón tay — cơ chế BẢN LỀ (hinge) + CÀI NGÀM (snap latch)
=======================================================================

MỤC ĐÍCH (xem hardware/cad/finger_shell_hinge/README.md để biết đầy đủ bối cảnh):
  Thay thế kiểu "ống kín phải xỏ ngón tay vào" (đau, khó với bệnh nhân liệt/co cứng)
  bằng kiểu VỎ SÒ (clam-shell) mở ra được:
    - 1 cạnh bên   = BẢN LỀ (hinge trục in 3D + chốt rời) -> mở ra như nắp hộp
    - cạnh bên kia = NGÀM CÀI (snap latch, có 2 nấc)      -> gập xuống là khóa lại
  Người chăm sóc đặt đốt ngón vào nửa trên (mu tay) đang mở, gập nửa dưới (lòng
  tay) xuống và bấm ngàm — KHÔNG cần luồn/ép ngón tay qua một vòng kín.

TRẠNG THÁI: bản vẽ CAD **thiết kế trên giấy / in thử lần 1**, các kích thước
đốt ngón tay (W_in, H_in, L) là SỐ GIẢ ĐỊNH tạm thời, PHẢI đo lại bằng thước
cặp trên người dùng thật trước khi in bản dùng thật (xem docs/04 nguyên tắc
"ngân sách thiết kế, không phải kết quả đo").

Công cụ: CadQuery 2.x (chạy trên OCP/Open CASCADE lấy từ PyPI) — môi trường
sandbox này không có apt/FreeCAD GUI lẫn OpenSCAD, nên dùng CadQuery làm công
cụ CAD tham số (parametric, scriptable, xuất STEP/STL chuẩn) thay thế.
Xem README.md mục "Môi trường dựng CAD" để cài lại từ đầu.

Chạy:
    python3 finger_shell_hinge.py            # xuất toàn bộ STEP/STL vào out/
"""
import os
import cadquery as cq

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT_DIR, exist_ok=True)


# =====================================================================
# 1) THAM SỐ THIẾT KẾ (đổi ở đây để chỉnh theo size ngón tay thật)
# =====================================================================
class P:
    # --- Kích thước đốt ngón tay (TẠM ĐỊNH, phải đo lại bằng thước cặp) ---
    L = 24.0          # chiều dài khung dọc theo ngón (mm) — đặt giữa thân đốt,
                       # tránh 2 khớp MCP/PIP (đốt gần ngón trỏ dài ~40-45mm)
    W_in = 19.0        # bề rộng trong, hướng trụ-quay (mm) — đặt tạm theo đốt gần
    H_in = 16.0        # bề dày trong, hướng mu-lòng (mm)

    # --- Vỏ cứng ---
    t_wall = 2.2       # bề dày thành khung (mm), PETG, >=2 lớp tường 0.4mm nozzle
    r_in = 2.5         # bo góc mặt trong (thoải mái da)
    r_out = 4.0        # bo góc mặt ngoài

    # --- Hốc cảm biến (Velostat + đồng tự dính, theo docs/04 §6) ---
    pocket_w = 8.0     # bề rộng hốc áp cảm biến (mm)
    pocket_len = 16.0  # chiều dài hốc dọc theo ngón (mm)
    pocket_depth = 1.3 # độ sâu khoét vào vách (mm) — chứa sandwich Velostat+đồng

    # --- Rãnh luồn dây tín hiệu ra khỏi hốc, dọc theo mu bàn tay ---
    wire_w = 2.2
    wire_depth = 1.2

    # --- Bản lề (hinge) — cạnh Y = -W_out/2 ---
    margin_x = 2.0       # chừa 2 đầu trục X không có khớp, cho cứng vững
    n_knuckle_top = 3    # số "khớp ống" thuộc nửa mu tay (A)
    n_knuckle_bot = 2    # số "khớp ống" thuộc nửa lòng tay (B), xen kẽ với A
    knuckle_gap = 0.5    # khe hở in 3D giữa các khớp ống (mm)
    r_knuckle = 3.0      # bán kính ngoài khớp ống (mm)
    r_pin = 1.15         # bán kính lỗ xỏ chốt (mm) -> lỗ phi 2.3mm cho chốt phi 2.0-2.2mm
    knuckle_overlap = 0.5  # phần khớp ống "ăn" vào thành vỏ để union liền khối

    # --- Ngàm cài (snap latch) — cạnh Y = +W_out/2 ---
    catch_h = 9.0        # chiều cao khối ngàm (mu tay, cố định) tính từ mặt phân (mm)
    catch_t = 2.2        # bề dày khối ngàm
    tooth_h = 0.9        # độ nhô của mỗi nấc răng ngàm
    tooth_pitch = 2.6    # khoảng cách giữa 2 nấc (mm)
    arm_h = 13.0          # chiều dài tay đòn ngàm (lòng tay, đàn hồi) (mm)
    arm_t = 1.1           # bề dày tay đòn đàn hồi (mm) — PETG mỏng để tự đàn hồi
    arm_hook = 1.1         # độ sâu móc ở đầu tay đòn, ăn vào nấc răng

    # --- Dây đai phụ (Velcro/thun) — khóa an toàn lớp 2 ---
    strap_slot_w = 3.2
    strap_slot_h = 6.0

    @property
    def W_out(self):
        return self.W_in + 2 * self.t_wall

    @property
    def H_out(self):
        return self.H_in + 2 * self.t_wall


p = P()


# =====================================================================
# 2) KHỐI ỐNG CƠ SỞ (bo góc chữ nhật) rồi cắt đôi theo mặt Z=0
# =====================================================================
def rounded_prism(length_x, w, h, r, x_off=0.0, length_margin=0.0):
    """Lăng trụ bo góc dọc theo X, mặt cắt (W x H) trên mặt phẳng YZ."""
    wp = (
        cq.Workplane("YZ")
        .rect(w, h)
        .extrude(length_x + length_margin)
    )
    wp = wp.edges("|X").fillet(r)
    wp = wp.translate((x_off, 0, 0))
    return wp


def base_tube():
    outer = rounded_prism(p.L, p.W_out, p.H_out, p.r_out)
    inner = rounded_prism(p.L, p.W_in, p.H_in, p.r_in, x_off=-2.0, length_margin=4.0)
    return outer.cut(inner)


def split_half(solid, sign):
    """sign=+1 -> nửa Z>0 (mu tay/dorsal), sign=-1 -> nửa Z<0 (lòng tay/palmar)."""
    big = max(p.W_out, p.H_out, p.L) * 6
    box = cq.Workplane("XY").box(big, big, big).translate((0, 0, sign * big / 2))
    return solid.intersect(box)


# =====================================================================
# 3) HỐC CẢM BIẾN + RÃNH DÂY
# =====================================================================
def cut_sensor_pocket(shell, sign):
    """sign=+1: khoét ở đỉnh trong (Z=+H_in/2) cho nửa mu tay.
    sign=-1: khoét ở đáy trong (Z=-H_in/2) cho nửa lòng tay."""
    z_face = sign * p.H_in / 2.0
    pocket = (
        cq.Workplane("XY")
        .box(p.pocket_len, p.pocket_w, p.pocket_depth + 0.4)
        .translate((p.L / 2.0, 0, z_face + sign * (p.pocket_depth / 2.0 - 0.2)))
    )
    shell = shell.cut(pocket)

    # rãnh luồn dây tín hiệu: từ mép hốc chạy dọc ra 1 đầu khung (đầu x=0, phía cổ tay)
    wire_len = (p.L / 2.0 - p.pocket_len / 2.0) + 1.0
    wire = (
        cq.Workplane("XY")
        .box(wire_len, p.wire_w, p.wire_depth + 0.4)
        .translate((wire_len / 2.0, 0, z_face + sign * (p.wire_depth / 2.0 - 0.2)))
    )
    shell = shell.cut(wire)
    return shell


# =====================================================================
# 4) BẢN LỀ — khớp ống (knuckle) so le ở cạnh Y = -W_out/2
# =====================================================================
def knuckle_segments():
    """Trả về danh sách (x_start, x_end, which) which='top' hoặc 'bot',
    so le nhau dọc theo vùng giữa (chừa margin_x ở 2 đầu)."""
    x0 = p.margin_x
    x1 = p.L - p.margin_x
    n_total = p.n_knuckle_top + p.n_knuckle_bot
    total_gap = p.knuckle_gap * (n_total - 1)
    seg_w = ((x1 - x0) - total_gap) / n_total
    segs = []
    x = x0
    # xen kẽ bắt đầu và kết thúc bằng 'top': T B T B T ...
    # (yêu cầu n_knuckle_top == n_knuckle_bot + 1 để xen kẽ đều, bắt-và-kết bằng top)
    assert p.n_knuckle_top == p.n_knuckle_bot + 1, (
        "knuckle_segments() giả định n_knuckle_top = n_knuckle_bot + 1 để xen kẽ đều"
    )
    order = ["top" if i % 2 == 0 else "bot" for i in range(n_total)]
    for which in order:
        segs.append((x, x + seg_w, which))
        x += seg_w + p.knuckle_gap
    return segs


def add_hinge_knuckles(shell, which):
    segs = [s for s in knuckle_segments() if s[2] == which]
    y_flat = -p.W_out / 2.0
    y_axis = y_flat - p.r_knuckle + p.knuckle_overlap
    z_axis = 0.0
    for x_start, x_end, _ in segs:
        w = x_end - x_start
        xc = (x_start + x_end) / 2.0
        # khớp ống (knuckle): hình trụ trục dọc theo X, tiếp xúc mặt bên phẳng
        # của vỏ tại y_flat, nhô ra ngoài (ăn vào vỏ một khoảng knuckle_overlap)
        boss = (
            cq.Workplane("YZ")
            .center(y_axis, z_axis)
            .circle(p.r_knuckle)
            .extrude(w)
            .translate((xc - w / 2.0, 0, 0))
        )
        shell = shell.union(boss)
    # khoan lỗ chốt xuyên suốt toàn bộ vùng bản lề (một lỗ thẳng, đi qua mọi khớp ống)
    hole_len = (p.L - 2 * p.margin_x) + 4.0
    pin_hole = (
        cq.Workplane("YZ")
        .center(y_axis, z_axis)
        .circle(p.r_pin)
        .extrude(hole_len)
        .translate((p.margin_x - 2.0, 0, 0))
    )
    shell = shell.cut(pin_hole)
    return shell


# =====================================================================
# 5) NGÀM CÀI — khối răng (mu tay, cố định) + tay đòn đàn hồi (lòng tay)
# =====================================================================
def add_latch_catch(shell):
    """Khối ngàm có các nấc răng, gắn vào nửa mu tay (shell trên), cạnh Y=+W_out/2."""
    y0 = p.W_out / 2.0
    x0, x1 = p.margin_x, p.L - p.margin_x
    w = x1 - x0
    xc = (x0 + x1) / 2.0

    block = (
        cq.Workplane("XY")
        .box(w, p.catch_t, p.catch_h)
        .translate((xc, y0 + p.catch_t / 2.0 - 0.3, p.catch_h / 2.0))
    )
    shell = shell.union(block)

    n_teeth = 2
    for i in range(n_teeth):
        z_t = p.catch_h * 0.35 + i * p.tooth_pitch
        tooth = (
            cq.Workplane("XY")
            .box(w, p.tooth_h * 2, 1.4)
            .translate((xc, y0 + p.catch_t - 0.3 + p.tooth_h * 0.4, z_t))
        )
        shell = shell.union(tooth)
    return shell


def add_latch_arm(shell):
    """Tay đòn đàn hồi gắn vào nửa lòng tay (shell dưới), cạnh Y=+W_out/2,
    vươn lên phía mu tay để móc vào khối răng.

    SỬA LỖI 2026-10-07 (phát hiện bởi chủ dự án khi mở file .scad bằng
    OpenSCAD thật — xem README §5a "Lỗi đã sửa"): bản gốc đặt `arm` bắt đầu
    từ y = y0 + catch_t + arm_t/2 + 0.6 ≈ 15.05mm, trong khi mép ngoài cùng
    của vỏ (shell) chỉ tới y = y0 = W_out/2 ≈ 11.7mm — tức LỆCH một khoảng
    trống ~2.8mm, KHÔNG chạm vào vỏ ở bất kỳ lát cắt Z nào. Hệ quả: tay đòn
    (+ móc) là một khối RỜI, trôi lơ lửng trong không gian, không in được
    (không có gì đỡ nó). Đã kiểm chứng bằng `trimesh` (xem
    check_connectivity.py): STL cũ tách thành 2 mảnh rời nhau.
    Khắc phục: thêm một "gốc nối" (root/rib) đặc, bắc cầu từ mép vỏ thật
    (lấn 0.3mm vào vỏ, giống cách `add_latch_catch` đã làm) tới mặt trong
    của tay đòn (lấn thêm 0.3mm vào tay đòn), nằm gọn trong vùng Z của nửa
    lòng tay (z <= 0, không đụng khối răng ở nửa mu tay)."""
    y0 = p.W_out / 2.0
    x0, x1 = p.margin_x, p.L - p.margin_x
    w = x1 - x0
    xc = (x0 + x1) / 2.0

    y_arm_center = y0 + p.catch_t + p.arm_t / 2.0 + 0.6
    y_arm_outer = y_arm_center + p.arm_t / 2.0

    arm = (
        cq.Workplane("XY")
        .box(w, p.arm_t, p.arm_h)
        .translate((xc, y_arm_center, p.arm_h / 2.0))
    )
    # móc ở đầu tay đòn, nhô vào phía khối răng (hướng -Y) để ăn khớp
    hook = (
        cq.Workplane("XY")
        .box(w, p.arm_hook + p.arm_t, 1.6)
        .translate((xc, y0 + p.catch_t + p.arm_t - p.arm_hook / 2.0 + 0.2, p.arm_h - 1.0))
    )
    # Gốc nối (rib) — bắc cầu khoảng trống giữa vỏ thật và chân tay đòn,
    # nằm trong z <= 0 (nửa lòng tay), KHÔNG tràn sang nửa mu tay.
    root_h = 3.0
    eps = 0.2
    y_root_in = y0 - 0.3
    y_root_out = y_arm_outer + 0.3
    root = (
        cq.Workplane("XY")
        .box(w, y_root_out - y_root_in, root_h + eps)
        .translate((xc, (y_root_in + y_root_out) / 2.0, -root_h / 2.0 + eps / 2.0))
    )
    shell = shell.union(root).union(arm).union(hook)
    return shell


# =====================================================================
# 6) RÃNH DÂY ĐAI PHỤ (Velcro/thun) — khóa an toàn lớp 2
# =====================================================================
def add_strap_slots(shell, sign):
    z_mid = sign * p.H_in / 2.0
    for xc in (p.margin_x + 1.5, p.L - p.margin_x - 1.5):
        slot = (
            cq.Workplane("YZ")
            .center(0, z_mid)
            .rect(p.W_out * 0.9, p.strap_slot_h, centered=(True, True))
            .extrude(p.strap_slot_w)
            .translate((xc - p.strap_slot_w / 2.0, 0, 0))
        )
        shell = shell.cut(slot)
    return shell


# =====================================================================
# 7) LẮP RÁP TOÀN BỘ
# =====================================================================
def build_top_shell():
    tube = base_tube()
    shell = split_half(tube, +1)
    shell = cut_sensor_pocket(shell, +1)
    shell = add_hinge_knuckles(shell, "top")
    shell = add_latch_catch(shell)
    shell = add_strap_slots(shell, +1)
    return shell


def build_bottom_shell():
    tube = base_tube()
    shell = split_half(tube, -1)
    shell = cut_sensor_pocket(shell, -1)
    shell = add_hinge_knuckles(shell, "bot")
    shell = add_latch_arm(shell)
    shell = add_strap_slots(shell, -1)
    return shell


def build_pin():
    y_axis = -p.W_out / 2.0 - p.r_knuckle + p.knuckle_overlap
    hole_len = (p.L - 2 * p.margin_x) + 4.0
    pin_len = hole_len + 1.0
    pin = (
        cq.Workplane("YZ")
        .center(y_axis, 0)
        .circle(p.r_pin - 0.15)  # khe hở lắp 0.15mm bán kính
        .extrude(pin_len)
        .translate((p.margin_x - 2.5, 0, 0))
    )
    return pin


def hinge_axis_points():
    y_axis = -p.W_out / 2.0 - p.r_knuckle + p.knuckle_overlap
    p0 = cq.Vector(0, y_axis, 0)
    p1 = cq.Vector(1, y_axis, 0)
    return p0, p1


def build_open_bottom_shell(angle_deg=150.0):
    """Xoay nửa lòng tay quanh trục bản lề để minh họa trạng thái MỞ
    (đặt đốt ngón vào nửa mu tay, rồi gập nửa lòng tay xuống để đóng)."""
    bot = build_bottom_shell()
    p0, p1 = hinge_axis_points()
    return bot.rotate((p0.x, p0.y, p0.z), (p1.x, p1.y, p1.z), angle_deg)


def export_assembly_state(top, bot, name, pin=None):
    asm = cq.Assembly()
    asm.add(top, name="top_shell_dorsal", color=cq.Color(0.85, 0.63, 0.40, 1.0))
    asm.add(bot, name="bottom_shell_palmar", color=cq.Color(0.40, 0.60, 0.80, 1.0))
    if pin is not None:
        # Trục bản lề (hinge_pin) — SỬA LỖI 2026-10-07 (phát hiện bởi chủ dự
        # án: "thiếu cái trục ở giữa bản lề"): trục nằm đúng trên đường tâm
        # xoay (hinge_axis_points()) nên vị trí KHÔNG đổi giữa đóng/mở, chỉ
        # cần thêm vào assembly để nhìn thấy chốt xuyên qua các khớp ống.
        asm.add(pin, name="hinge_pin", color=cq.Color(0.25, 0.25, 0.25, 1.0))
    asm.save(os.path.join(OUT_DIR, f"{name}.step"))
    # Xuất riêng từng mảnh dạng STL (ở đúng vị trí/góc xoay của trạng thái này)
    # để xem nhanh bằng render_preview.py — KHÔNG hợp nhất 2 khối (chỉ để xem, không in).
    cq.exporters.export(top, os.path.join(OUT_DIR, f"{name}__top.stl"))
    cq.exporters.export(bot, os.path.join(OUT_DIR, f"{name}__bottom.stl"))
    if pin is not None:
        cq.exporters.export(pin, os.path.join(OUT_DIR, f"{name}__pin.stl"))


def main():
    print("Tham số hiện tại: L=%.1f W_in=%.1f H_in=%.1f t_wall=%.1f" % (
        p.L, p.W_in, p.H_in, p.t_wall))

    top = build_top_shell()
    print("  top_shell OK, volume=%.1f mm3" % top.val().Volume())
    bot = build_bottom_shell()
    print("  bottom_shell OK, volume=%.1f mm3" % bot.val().Volume())
    pin = build_pin()
    print("  pin OK, volume=%.1f mm3" % pin.val().Volume())

    for name, obj in (("top_shell_dorsal", top), ("bottom_shell_palmar", bot), ("hinge_pin", pin)):
        cq.exporters.export(obj, os.path.join(OUT_DIR, f"{name}.step"))
        cq.exporters.export(obj, os.path.join(OUT_DIR, f"{name}.stl"))
        print("  exported", name)

    # Trạng thái lắp ráp: ĐÓNG (0°) và MỞ (xoay nửa lòng tay quanh trục bản lề)
    # — CẢ 2 trạng thái đều kèm hinge_pin (trục chốt) vì chốt nằm đúng trên
    # tâm xoay nên không di chuyển khi mở/đóng (xem hinge_axis_points()).
    export_assembly_state(top, bot, "assembly_closed", pin=pin)
    bot_open = build_open_bottom_shell(angle_deg=150.0)
    export_assembly_state(top, bot_open, "assembly_open", pin=pin)
    print("  exported assembly_closed, assembly_open (kem hinge_pin)")

    print("Xong. File STEP/STL nằm trong:", OUT_DIR)


if __name__ == "__main__":
    main()
