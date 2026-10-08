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
    # 2026-10-07 (theo yêu cầu "đổi sang hình trụ, bớt vuông cứng"): bỏ cách bo góc
    # chữ nhật kiểu cũ (r_in/r_out, góc bo nhỏ ~2.5-4mm). Tiết diện giờ là 1 lăng trụ
    # "viên thuốc dẹt": 2 mặt mu tay/lòng tay có 1 đoạn THẲNG ở giữa (đủ rộng để dán
    # cảm biến phẳng), còn 2 CẠNH HÔNG (nơi gắn bản lề + ngàm cài) được bo tròn HẾT
    # MỨC có thể bằng 1 cung ELIP lớn (gần giống nửa hình trụ tròn, không còn góc
    # vuông). Xem rounded_prism()/README mục "Tiết diện (2026-10-07)".
    flat_w = 12.0      # bề rộng đoạn thẳng còn lại ở giữa mặt mu/lòng tay (mm) —
                       # mặc định = pocket_w + 2*2mm biên, đủ chứa hốc cảm biến.

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
    PIN_INTEGRATED = True  # 2026-10-07, theo yêu cầu chủ dự án: True = HÀN
    # LIỀN trục chốt vào nửa mu tay (in top_shell + trục thành 1 khối duy
    # nhất, không cần lắp chốt rời — chỉ nửa lòng tay vẫn tách riêng vì
    # phải xoay quanh trục). False = thiết kế cũ: chốt là 1 chi tiết RỜI
    # (hinge_pin.stl), xỏ qua lỗ xuyên cả 2 nửa sau khi in (xem README §5b
    # để biết đánh đổi: tích hợp -> ít chi tiết rời hơn, nhưng KHÔNG còn
    # thay được bằng que kim loại cứng nếu trục in bị gãy).
    r_knuckle = 3.0      # bán kính ngoài khớp ống (mm)
    # 2026-10-07 (theo yêu cầu "in tại chỗ, tự do xoay ngay sau khi in"):
    # r_pin = bán kính LỖ trên khớp ống nửa lòng tay (hole). Khi PIN_INTEGRATED=True,
    # bán kính trục đặc hàn vào nửa mu tay = r_pin - pin_clearance. Trước đây
    # pin_clearance là số viết tay 0.15mm ngay trong build_pin() — QUÁ CHẶT cho
    # kiểu in "print-in-place" (in liền 1 lần, khớp ống bọc quanh trục trong lúc
    # in, không lắp tay sau) theo đúng nghĩa đen câu yêu cầu của chủ dự án.
    # Các nguồn hướng dẫn in FDM (Snapmaker, FastPreci, QIDI 3D — xem README §5e)
    # đều khuyến nghị khe hở bán kính 0.2-0.4mm cho bản lề in-tại-chỗ (0.15mm dễ
    # bị dính liền 2 khối khi máy in chưa hiệu chỉnh hoàn hảo). Đã tăng lỗ lên
    # 1.3mm để giữ nguyên bán kính trục đặc ~1.0mm (không đổi độ cứng trục) mà
    # vẫn đạt khe hở 0.3mm/bán kính theo khuyến nghị.
    r_pin = 1.3           # bán kính lỗ xỏ chốt/khớp xoay (mm) -> lỗ phi 2.6mm
    pin_clearance = 0.3   # khe hở BÁN KÍNH giữa trục đặc và lỗ (mm) — ĐÂY LÀ
                           # THAM SỐ CẦN HIỆU CHỈNH THEO TỪNG MÁY IN/VẬT LIỆU
                           # THẬT (xem README §5e) — 0.3mm chỉ là điểm khởi đầu
                           # phổ biến, CHƯA kiểm chứng bằng mẫu in thật.
    # 2026-10-08 (theo yêu cầu chủ dự án: "đảm bảo không dễ rơi ra ngoài"):
    # LỖI PHÁT HIỆN — trục cũ là hình trụ ĐỀU bán kính không đổi suốt chiều
    # dài, 2 đầu chỉ bo tròn (fillet) chứ KHÔNG có vai/mũ chặn lớn hơn lỗ
    # khớp ống -> KHÔNG CÓ GÌ ngăn nửa lòng tay trượt dọc trục (X) và tuột
    # hẳn ra khỏi trục. Khắc phục: thêm 2 "vai chặn" (retention shoulder,
    # hình trụ đồng trục bán kính pin_retain_r > r_pin) ở giữa khớp ống ĐẦU
    # và CUỐI thuộc nửa mu tay.
    #
    # SỬA LẠI GHI CHÚ 2026-10-08 (phát hiện khi làm QA bằng ảnh render +
    # đo thể tích chính xác, theo yêu cầu "dùng vision kiểm tra tới khi hết
    # lỗi"): ghi chú CŨ ở đây từng viết sai là vai chặn "ẩn gọn trong boss có
    # sẵn, KHÔNG tạo gờ nhô mới ra ngoài vỏ" — ĐÃ KIỂM CHỨNG ĐIỀU NÀY SAI.
    # Đo bằng boolean cut(top_shell CÓ vai chặn, top_shell KHÔNG có vai
    # chặn) ra ~24mm3 vật liệu MỚI, nằm hoàn toàn ở Z<0 (nửa không gian của
    # lòng tay) — vì boss của nửa mu tay (add_hinge_knuckles) chỉ là NỬA
    # hình trụ (intersect half_space Z>=0, xem add_hinge_knuckles()), trong
    # khi vai chặn là hình trụ TRÒN ĐỦ (cả 2 nửa Z). Vậy mỗi vai chặn thực
    # tế lộ ra thành 1 "cục u" nửa-hình-trụ nhỏ (bán kính 2.2mm, dài 2mm)
    # nhô vào đúng khe hở (knuckle_gap) giữa 2 khớp ống, phía lòng tay.
    # ĐÂY LÀ CHỦ Ý CẦN THIẾT, KHÔNG PHẢI LỖI: vai chặn PHẢI có vật liệu ở
    # đúng nửa Z<0 thì mới thực sự "chặn" được khớp ống lòng tay (có lỗ nằm
    # ở Z<0) khi nó cố trượt dọc trục tới đúng vị trí X này — nếu giới hạn
    # vai chặn về chỉ Z>=0 (giống boss) thì sẽ MẤT TÁC DỤNG chặn hoàn toàn.
    # Đã xác nhận cục u này KHÔNG gây va chạm khi xoay bản lề (vẫn PASS
    # check_hinge_sweep.py, xem README §5f) và KHÔNG vượt quá bán kính
    # ngoài lớn nhất của vỏ (2.2mm < r_knuckle=3.0mm) nên không ảnh hưởng
    # kích thước bao ngoài tổng thể — nhưng về mặt thẩm mỹ nó CÓ lộ ra một
    # chút trong khe hở giữa các khớp ống, không "ẩn hoàn toàn" như ghi chú
    # cũ từng nói. Xem README §5f (mục cập nhật) để biết chi tiết + ảnh.
    pin_retain_r = 2.2     # bán kính "vai chặn" (mm) — phải > r_pin (lỗ khớp
                           # ống, hiện 1.3mm) để chặn tuột. LƯU Ý: KHÔNG ẩn
                           # hoàn toàn — xem ghi chú 2026-10-08 ở trên, tạo 1
                           # cục u nhỏ lộ ra ở khe hở giữa các khớp ống (đã
                           # xác nhận không va chạm, không vượt quá bán kính
                           # ngoài lớn nhất r_knuckle=3.0mm của vỏ).
    knuckle_overlap = 0.5  # phần khớp ống "ăn" vào thành vỏ để union liền khối

    # --- Ngàm cài (snap latch) — cạnh Y = +W_out/2 ---
    catch_h = 14.0       # chiều cao khối ngàm (mu tay, cố định) tính từ mặt phân (mm)
                         # PHẢI >= (arm_h - 1.0 + 1.5) để chứa hết nấc răng gần điểm
                         # nghỉ của móc (xem add_latch_catch(), README §5c)
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
# 2) KHỐI ỐNG CƠ SỞ — tiết diện "viên thuốc dẹt" (flat-top capsule), cắt đôi
#    theo mặt Z=0
# =====================================================================
def rounded_prism(length_x, w, h, flat_w, x_off=0.0, length_margin=0.0):
    """Lăng trụ dọc theo X, mặt cắt (YZ) là 1 "viên thuốc dẹt":
      - 2 mặt mu tay/lòng tay (Z=+-h/2): có 1 đoạn THẲNG ở giữa, rộng `flat_w`
        (chỗ áp cảm biến phẳng + rãnh dây đai) — y chạy từ -flat_w/2 đến +flat_w/2.
      - 2 cạnh hông (Y=+-w/2, nơi gắn bản lề + ngàm cài): bo tròn bằng 1 cung
        ELIP lớn (bán trục Y = w/2 - flat_w/2, bán trục Z = h/2), nối tiếp
        tuyến (tangent) với đoạn thẳng — không còn góc vuông, "tròn hết mức
        có thể" trong khi vẫn giữ đủ mặt phẳng ở giữa để dán cảm biến.
    (2026-10-07, thay cho `rect().fillet(r)` kiểu cũ — xem README mục
    "Tiết diện": r_in/r_out góc bo nhỏ (2.5-4mm) làm tiết diện trông "vuông,
    cứng ngắc"; yêu cầu đổi sang "hình trụ" -> dùng cấu trúc flat-top + elip
    lớn này để vừa tròn trịa ở 2 cạnh hông, vừa giữ mặt phẳng cần thiết cho
    cảm biến/rãnh dây ở 2 mặt mu/lòng tay.)
    """
    half_flat = flat_w / 2.0
    a = w / 2.0 - half_flat  # bán trục elip theo Y (phải > 0)
    b = h / 2.0              # bán trục elip theo Z
    assert a > 0.1, (
        "flat_w qua lon so voi w (%.1f) -- khong con cho de bo tron canh hong" % w
    )
    profile = (
        cq.Workplane("YZ")
        .moveTo(half_flat, h / 2.0)
        .lineTo(-half_flat, h / 2.0)                              # mặt mu/lòng tay (thẳng)
        .ellipseArc(a, b, angle1=90, angle2=180, startAtCurrent=True)   # cạnh hông trái, nửa trên
        .ellipseArc(a, b, angle1=180, angle2=270, startAtCurrent=True)  # cạnh hông trái, nửa dưới
        .lineTo(half_flat, -h / 2.0)                               # mặt lòng/mu tay (thẳng)
        .ellipseArc(a, b, angle1=270, angle2=360, startAtCurrent=True)  # cạnh hông phải, nửa dưới
        .ellipseArc(a, b, angle1=0, angle2=90, startAtCurrent=True)     # cạnh hông phải, nửa trên
        .close()
    )
    wp = profile.extrude(length_x + length_margin)
    wp = wp.translate((x_off, 0, 0))
    return wp


def base_tube():
    outer = rounded_prism(p.L, p.W_out, p.H_out, p.flat_w)
    inner = rounded_prism(p.L, p.W_in, p.H_in, p.flat_w, x_off=-2.0, length_margin=4.0)
    return outer.cut(inner)


def half_space(sign):
    """Khối hộp khổng lồ chiếm trọn nửa không gian Z>0 (sign=+1) hoặc Z<0
    (sign=-1), dùng để CẮT/GIAO bất kỳ khối nào về đúng 1 nửa mu/lòng tay.
    Dùng chung cho split_half() (cắt vỏ) VÀ add_hinge_knuckles() (cắt khớp
    ống bản lề — xem SỬA LỖI 2026-10-07 §5e: khớp ống trước đây là 1 hình
    trụ TRÒN ĐỦ, tâm đúng tại mặt phân Z=0, nên PHẦN NỬA của nó luôn tràn
    sang phía đối diện — ví dụ khớp ống của top_shell (should chỉ ở Z>=0)
    thực ra có một nửa khối nằm ở Z<0, đè lên đúng vùng của bottom_shell,
    tạo ra ~9.4mm3 chồng lấn KHÔNG ĐỔI dù xoay bản lề góc nào (vì chồng lấn
    nằm sát trục quay, không phụ thuộc góc xoay) — phát hiện bằng
    check_hinge_sweep.py.).
    """
    big = max(p.W_out, p.H_out, p.L) * 6
    return cq.Workplane("XY").box(big, big, big).translate((0, 0, sign * big / 2))


def split_half(solid, sign):
    """sign=+1 -> nửa Z>0 (mu tay/dorsal), sign=-1 -> nửa Z<0 (lòng tay/palmar)."""
    return solid.intersect(half_space(sign))


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


def add_hinge_knuckles(shell, which, cut_hole=True):
    """cut_hole=False: KHÔNG khoan lỗ chốt (dùng cho nửa mu tay khi
    PIN_INTEGRATED=True — trục sẽ được HÀN LIỀN thay vì xỏ qua lỗ, xem
    build_top_shell())."""
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
        # SỬA LỖI 2026-10-07 (§5e): boss là 1 hình trụ TRÒN ĐỦ, tâm đúng tại
        # z_axis=0 (mặt phân 2 nửa) -> một nửa khối của nó luôn tràn sang
        # phía NỬA KHÔNG THUỘC VỀ NÓ (vd. khớp ống của top lại có vật liệu ở
        # Z<0, đè lên đúng chỗ bottom_shell cần chiếm) -> gây chồng lấn hình
        # học ~9.4mm3 dù 2 nửa không in dính nhau. Cắt boss về đúng nửa KHÔNG
        # GIAN của chính nó (top -> Z>=0, bot -> Z<=0) trước khi union.
        sign = +1 if which == "top" else -1
        boss = boss.intersect(half_space(sign))
        shell = shell.union(boss)
    if cut_hole:
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
    """Khối ngàm có các nấc răng, gắn vào nửa mu tay (shell trên), cạnh Y=+W_out/2.

    SỬA LỖI #3 2026-10-07 (phát hiện khi "check lại cơ chế chính xác" theo
    yêu cầu chủ dự án): bản cũ đặt vị trí RĂNG theo tỉ lệ ĐỘC LẬP với
    catch_h (`catch_h * 0.35 + i*tooth_pitch` => z~2.45-6.45mm), trong khi
    vị trí nghỉ của MÓC (hook, ở add_latch_arm) tính độc lập theo arm_h
    (`arm_h - 1.0` => z~11.2-12.8mm) — LỆCH NHAU 5-9mm, không bao giờ chạm
    được vào nhau. Ngàm cài NHƯ CŨ KHÔNG THỂ khoá được. Khắc phục: tính vị
    trí răng TRỰC TIẾP từ vị trí nghỉ của móc (cùng công thức `arm_h - 1.0`
    dùng trong add_latch_arm()) để 2 chi tiết LUÔN thẳng hàng."""
    y0 = p.W_out / 2.0
    x0, x1 = p.margin_x, p.L - p.margin_x
    w = x1 - x0
    xc = (x0 + x1) / 2.0

    hook_rest_z = p.arm_h - 1.0  # PHẢI giống hệt công thức trong add_latch_arm()
    assert p.catch_h >= hook_rest_z + 1.5, (
        "catch_h phai >= arm_h - 1.0 + 1.5 de chua het nac rang gan diem nghi cua moc"
    )

    # 2026-10-07 "bo tròn": khối ngàm chính + mỗi nấc răng được bo nhẹ các
    # cạnh dọc theo chiều dài (song song trục X) thay vì cạnh vuông sắc --
    # bán kính nhỏ, an toàn (không ăn vào vùng các răng/mép ăn khớp), giúp
    # giảm tập trung ứng suất khi in 3D và cảm giác cài/mở mượt hơn.
    r_catch = min(0.8, p.catch_t / 2.0 - 0.3, p.catch_h / 2.0 - 0.3)
    block = (
        cq.Workplane("XY")
        .box(w, p.catch_t, p.catch_h)
        .edges("|X")
        .fillet(r_catch)
        .translate((xc, y0 + p.catch_t / 2.0 - 0.3, p.catch_h / 2.0))
    )
    shell = shell.union(block)

    # Nấc 0 (i=0) nằm NGAY TẠI điểm nghỉ tự nhiên của móc -> đây là nấc móc
    # sẽ tự ăn khớp khi gập hẳn xuống (đóng hoàn toàn, không cần giữ). Nấc 1
    # nằm THẤP hơn 1 khoảng tooth_pitch -> móc phải trượt/lướt qua nấc này
    # trước (cảm giác "tách" 2 nấc khi gập), chưa dừng lại ở đó.
    r_tooth = min(0.3, p.tooth_h - 0.1, 1.4 / 2.0 - 0.1)
    n_teeth = 2
    for i in range(n_teeth):
        z_t = hook_rest_z - i * p.tooth_pitch
        tooth = (
            cq.Workplane("XY")
            .box(w, p.tooth_h * 2, 1.4)
            .edges("|X")
            .fillet(r_tooth)
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

    # 2026-10-07 "bo tròn": bo nhẹ cạnh dọc (song song X) của thân tay đòn
    # và móc -- bán kính rất nhỏ vì arm_t/arm_hook khá mỏng; không ảnh
    # hưởng vùng "gốc nối" (root) bên dưới (đã xác nhận lại bằng
    # check_connectivity.py sau khi áp dụng).
    r_arm = min(0.3, p.arm_t / 2.0 - 0.2)
    r_hook = min(0.3, (p.arm_hook + p.arm_t) / 2.0 - 0.2, 1.6 / 2.0 - 0.2)

    arm = (
        cq.Workplane("XY")
        .box(w, p.arm_t, p.arm_h)
        .edges("|X")
        .fillet(r_arm)
        .translate((xc, y_arm_center, p.arm_h / 2.0))
    )
    # móc ở đầu tay đòn, nhô vào phía khối răng (hướng -Y) để ăn khớp
    hook = (
        cq.Workplane("XY")
        .box(w, p.arm_hook + p.arm_t, 1.6)
        .edges("|X")
        .fillet(r_hook)
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
    # PIN_INTEGRATED=True (mặc định, theo yêu cầu 2026-10-07): KHÔNG khoan lỗ
    # chốt ở nửa mu tay — trục sẽ được HÀN LIỀN (union) vào ngay bên dưới,
    # nên top_shell + trục bản lề in ra là MỘT khối duy nhất, không cần lắp
    # chốt rời. Nửa lòng tay (build_bottom_shell) vẫn LUÔN khoan lỗ (có khe
    # hở 0.15mm) để trượt/xoay tự do quanh trục cố định này.
    shell = add_hinge_knuckles(shell, "top", cut_hole=not p.PIN_INTEGRATED)
    shell = add_latch_catch(shell)
    shell = add_strap_slots(shell, +1)
    if p.PIN_INTEGRATED:
        shell = shell.union(build_pin())
    return shell


def build_bottom_shell():
    tube = base_tube()
    shell = split_half(tube, -1)
    shell = cut_sensor_pocket(shell, -1)
    shell = add_hinge_knuckles(shell, "bot")
    shell = add_latch_arm(shell)
    shell = add_strap_slots(shell, -1)
    return shell


def build_pin(with_retention=None):
    """with_retention=None (mặc định): tự quyết theo PIN_INTEGRATED (chỉ thêm
    vai chặn khi trục hàn liền — xem giải thích tham số pin_retain_r ở P)."""
    if with_retention is None:
        with_retention = p.PIN_INTEGRATED
    y_axis = -p.W_out / 2.0 - p.r_knuckle + p.knuckle_overlap
    hole_len = (p.L - 2 * p.margin_x) + 4.0
    pin_len = hole_len + 1.0
    r = p.r_pin - p.pin_clearance  # khe hở BÁN KÍNH = p.pin_clearance (xem P, §5e)
    pin = (
        cq.Workplane("YZ")
        .circle(r)
        .extrude(pin_len)
    )
    # 2026-10-07 "bo tròn": fillet gần hết bán kính trên 2 mặt tròn đầu trục
    # -> tạo chỏm bán cầu (dạng "viên nang"/capsule) thay vì cắt vuông --
    # không còn cạnh sắc ở 2 đầu thò ra, dễ dùng làm mồi luồn qua các khớp
    # ống khi lắp ráp và an toàn hơn khi đầu trục lộ ra ngoài vỏ.
    pin = pin.edges("%CIRCLE").fillet(r * 0.999)
    if with_retention:
        # SỬA LỖI 2026-10-08 (§5f, "đảm bảo không dễ rơi ra ngoài"): thêm 2
        # vai chặn hình TRỤ ĐỒNG TRỤC (collar, bán kính pin_retain_r > r_pin)
        # đặt đúng GIỮA khớp ống ĐẦU và CUỐI thuộc nửa mu tay. Mọi khớp ống
        # nửa lòng tay (lỗ bán kính r_pin=1.3mm) đều nằm GIỮA 2 vai chặn này
        # theo trục X nên không thể trượt dọc trục để tuột ra ngoài. (Thử
        # dùng hình CẦU trước, nhưng cực của hình cầu tạo ra 1 tam giác suy
        # biến thể tích ~0 khi xuất STL -- bị check_connectivity.py báo nhầm
        # thành "mảnh rời"; đổi sang hình TRỤ ĐỒNG TRỤC với trục chính của
        # chốt thì không còn điểm cực kỳ dị nào -> hết lỗi.)
        #
        # ĐÍNH CHÍNH 2026-10-08 (QA bằng ảnh + đo thể tích, xem ghi chú đầy
        # đủ ở định nghĩa `pin_retain_r` trong class P phía trên): vai chặn
        # này KHÔNG "ẩn gọn trong boss có sẵn" như ghi chú cũ từng nói nhầm —
        # vì boss của nửa mu tay chỉ là NỬA hình trụ (Z>=0), còn vai chặn là
        # hình trụ TRÒN ĐỦ nên nửa Z<0 của nó lộ ra thành 1 cục u nhỏ trong
        # khe hở giữa các khớp ống. Đây là CHỦ Ý CẦN THIẾT để vai chặn thực
        # sự chặn được khớp ống lòng tay (đã xác nhận không va chạm khi xoay
        # và không vượt bán kính ngoài lớn nhất của vỏ — xem README §5f).
        segs = knuckle_segments()
        top_segs = [s for s in segs if s[2] == "top"]
        x_first = (top_segs[0][0] + top_segs[0][1]) / 2.0
        x_last = (top_segs[-1][0] + top_segs[-1][1]) / 2.0
        x_origin = p.margin_x - 2.5  # khớp với translate() bên dưới
        collar_len = 2.0  # mm, đủ ngắn để nằm gọn trong 1 doan knuckle (3.6mm)
        for x_global in (x_first, x_last):
            x_local_start = (x_global - x_origin) - collar_len / 2.0
            head = (
                cq.Workplane("YZ")
                .circle(p.pin_retain_r)
                .extrude(collar_len)
                .translate((x_local_start, 0, 0))
            )
            pin = pin.union(head)
    pin = pin.translate((p.margin_x - 2.5, y_axis, 0))
    return pin



def hinge_axis_points():
    y_axis = -p.W_out / 2.0 - p.r_knuckle + p.knuckle_overlap
    p0 = cq.Vector(0, y_axis, 0)
    p1 = cq.Vector(1, y_axis, 0)
    return p0, p1


def build_open_bottom_shell(angle_deg=150.0):
    """Xoay nửa lòng tay quanh trục bản lề để minh họa trạng thái MỞ
    (đặt đốt ngón vào nửa mu tay, rồi gập nửa lòng tay xuống để đóng).

    LỖI NGHIÊM TRỌNG ĐÃ SỪA 2026-10-07 (§5e, phát hiện khi viết
    check_hinge_sweep.py để kiểm tra yêu cầu "xoay tự do quanh trục"): dấu
    của `angle_deg` trước đây là DƯƠNG (+150°) -- hướng này khiến 2 nửa vỏ
    THẬT SỬ ĐÂM XUYÊN NHAU (giao nhau hình học tới ~600mm3, không phải chỉ
    chạm nhẹ) trong suốt khoảng góc +5..+100°, chỉ "trông ổn" ở ảnh render
    cũ vì ảnh cũ CHỈ xuất ở đúng 1 góc cuối (+150°, nơi 2 nửa tình cờ lại
    tách rời) -- việc chỉ xem ảnh ở 1 góc tĩnh đã bỏ sót toàn bộ đường đi va
    chạm ở giữa. Đã quét `top.intersect(bot xoay nhiều góc)` bằng CadQuery và
    phát hiện. Hướng ÂM (-150°) mới là hướng xoay KHÔNG va chạm trong suốt
    hành trình 0 -> -150° (đã quét từng 5-10° xác nhận, xem
    check_hinge_sweep.py). Đổi dấu mặc định thành ÂM để khớp hướng mở thật.
    """
    bot = build_bottom_shell()
    p0, p1 = hinge_axis_points()
    return bot.rotate((p0.x, p0.y, p0.z), (p1.x, p1.y, p1.z), -abs(angle_deg))


def print_ready(shape):
    """Xoay 1 mảnh (top_shell hoặc bottom_shell) sang HƯỚNG ĐẶT LÊN BÀN IN
    sao cho DIỆN TÍCH OVERHANG (bề mặt chúc xuống cần support) là ÍT NHẤT.

    2026-10-08 (theo yêu cầu chủ dự án "xoay chỉnh sửa sao cho khi để lên
    slicer thì support tạo ra sẽ ít nhất đi"): đã viết `check_print_orientation.py`
    để quét 24 hướng đặt theo trục chính (mọi cách úp 1 trong 6 mặt hộp bao
    xuống bàn, có xoay quanh trục đứng) và đo THẬT diện tích tam giác "chúc
    xuống quá 45° so với phương ngang" (đúng tiêu chí slicer FDM dùng để
    quyết định sinh support) bằng lưới tam giác hoá thật (CadQuery
    tessellate()), không phải suy đoán. Kết quả: xoay 90° quanh trục Y
    (đưa trục bản lề — trục X cục bộ — về THẲNG ĐỨNG, trùng trục Z máy in)
    là hướng TỐT NHẤT trong 24 hướng cho CẢ 2 mảnh — giảm overhang từ
    22.7%/24.0% diện tích bề mặt (hướng tệ nhất) xuống còn 8.6%/5.1% (xem
    README §6a để có bảng số đầy đủ). Đây CHÍNH LÀ hướng đã được khuyến
    nghị bằng lời ở README §6 từ trước (để lỗ chốt in theo lớp tròn hoàn
    chỉnh) — nay được XÁC NHẬN BẰNG SỐ là cũng tối ưu cho overhang, và
    được XUẤT SẴN thành file riêng để không cần người dùng tự xoay tay
    trong slicer nữa (giảm rủi ro ai đó in nhầm ở hướng thiết kế gốc, tức
    hướng TỆ nhất, 22-24% overhang).

    QUAN TRỌNG VỀ DẤU GÓC: rotate(+90) quanh Y (không phải -90) — đã kiểm
    chứng cả 2 dấu trong check_print_orientation.py, dấu +90 cho kết quả
    bằng hoặc tốt hơn dấu -90 ở cả 2 mảnh (bottom_shell: 5.06% vs 5.16%).
    """
    rotated = shape.rotate((0, 0, 0), (0, 1, 0), 90)
    bb = rotated.val().BoundingBox()
    return rotated.translate((0, 0, -bb.zmin))  # hạ xuống cho đáy chạm Z=0 (ban in)


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


def export_print_in_place(top, bot, out_name):
    """2026-10-07 (§5e, theo yêu cầu chủ dự án: "phần phụ lồng vào trục khi
    in, in ra là tự do xoay quanh trục tại chỗ"): xuất MỘT file STL DUY NHẤT
    chứa CẢ 2 nửa (top_shell đã hàn sẵn trục + bottom_shell) — để nạp thẳng
    vào slicer làm 1 lần in, khớp ống nửa lòng tay sẽ được in BỌC QUANH trục
    có sẵn với khe hở `P.pin_clearance` (mặc định 0.3mm bán kính, xem README
    §5e) — không cần thao tác lắp ráp nào sau khi in; bản lề quay được NGAY
    khi gỡ khỏi bàn in (nếu máy in đủ chính xác với khe hở này).

    PHẢI gọi với `bot` ở TRẠNG THÁI MỞ (vd. build_open_bottom_shell(150)),
    KHÔNG phải trạng thái đóng — xem ghi chú trong main() để biết lý do
    (ngàm cài sẽ bị in dính liền nếu xuất ở tư thế đóng).

    QUAN TRỌNG: 2 khối (top, bot) KHÔNG được boolean-union — chúng phải ở
    dạng 2 SOLID RIÊNG BIỆT không giao nhau (chỉ cách nhau đúng khe hở) bên
    trong cùng 1 file multi-solid STL, để slicer in chúng như 2 vật thể độc
    lập cùng lúc (kỹ thuật "print-in-place" tiêu chuẩn). Trước khi gọi hàm
    này, main() đã kiểm tra bằng intersect() rằng thể tích giao nhau giữa 2
    khối ở trạng thái truyền vào là ~0 (xem check_hinge_sweep.py).
    """
    compound = cq.Compound.makeCompound([top.val(), bot.val()])
    path = os.path.join(OUT_DIR, f"{out_name}.stl")
    cq.exporters.export(compound, path)
    return path


def main():
    print("Tham số hiện tại: L=%.1f W_in=%.1f H_in=%.1f t_wall=%.1f" % (
        p.L, p.W_in, p.H_in, p.t_wall))

    top = build_top_shell()
    pin_note = "da han lien vao top_shell, in 1 khoi" if p.PIN_INTEGRATED else "chi tiet roi, lap sau"
    print("  top_shell OK, volume=%.1f mm3 (truc ban le: %s)" % (top.val().Volume(), pin_note))
    bot = build_bottom_shell()
    print("  bottom_shell OK, volume=%.1f mm3" % bot.val().Volume())
    pin = build_pin()
    print("  pin OK, volume=%.1f mm3 (xuat rieng hinge_pin.stl de tham khao kich thuoc truc,"
          " du da han lien vao top_shell hay chua)" % pin.val().Volume())

    for name, obj in (("top_shell_dorsal", top), ("bottom_shell_palmar", bot), ("hinge_pin", pin)):
        cq.exporters.export(obj, os.path.join(OUT_DIR, f"{name}.step"))
        cq.exporters.export(obj, os.path.join(OUT_DIR, f"{name}.stl"))
        print("  exported", name)

    # 2026-10-08: file ĐÃ XOAY SẴN về hướng overhang-tối-thiểu (xem print_ready(),
    # README §6a) -- nạp thẳng file "*_print_ready.stl/.step" vào slicer là
    # đúng hướng khuyến nghị ngay, không cần tự xoay tay.
    for name, obj in (("top_shell_dorsal", top), ("bottom_shell_palmar", bot)):
        pr = print_ready(obj)
        cq.exporters.export(pr, os.path.join(OUT_DIR, f"{name}_print_ready.step"))
        cq.exporters.export(pr, os.path.join(OUT_DIR, f"{name}_print_ready.stl"))
        print("  exported", f"{name}_print_ready", "(da xoay san, huong overhang toi thieu)")

    # Trạng thái lắp ráp: ĐÓNG (0°) và MỞ (xoay nửa lòng tay quanh trục bản lề).
    # Nếu PIN_INTEGRATED=True, trục đã NẰM SẴN TRONG top (union ở
    # build_top_shell()) nên KHÔNG truyền pin= nữa (tránh vẽ/xuất trùng lặp);
    # nếu False (thiết kế cũ, chốt rời), vẫn vẽ thêm pin vào cả 2 trạng thái
    # vì chốt nằm đúng trên tâm xoay nên không di chuyển khi mở/đóng.
    asm_pin = None if p.PIN_INTEGRATED else pin
    export_assembly_state(top, bot, "assembly_closed", pin=asm_pin)
    bot_open = build_open_bottom_shell(angle_deg=150.0)
    export_assembly_state(top, bot_open, "assembly_open", pin=asm_pin)
    print("  exported assembly_closed, assembly_open")

    # File IN-TẠI-CHỖ (print-in-place) 2026-10-07: 1 file STL duy nhất, nạp
    # thẳng vào slicer, in top+bottom CÙNG LÚC, khớp ống nửa lòng tay đã bọc
    # sẵn quanh trục — xoay được ngay sau khi in, không cần lắp ráp tay.
    # QUAN TRỌNG: xuất ở trạng thái MỞ (bot_open), KHÔNG phải trạng thái
    # đóng — vì ở trạng thái ĐÓNG, móc ngàm cài CỐ Ý chạm/ngoàm vào răng
    # (giao nhau ~51.5mm3, xem check_hinge_sweep.py); nếu in sẵn ở tư thế đó,
    # slicer sẽ in LIỀN 2 chi tiết ngàm cài thành 1 khối đặc tại đúng chỗ
    # ngoàm, làm mất khả năng tay đòn đàn hồi bật ra/cài vào được -- khác
    # hẳn bản lề (chỉ có khe hở, không bao giờ chạm). Ở trạng thái MỞ 150°,
    # ngàm cài KHÔNG chạm nhau (xa nhau hẳn) nên an toàn để in-tại-chỗ; sau
    # khi in xong, gập tay bằng tay để cài ngàm như thiết kế vốn có.
    if p.PIN_INTEGRATED:
        pip_vol_check = top.intersect(bot_open)
        try:
            pip_overlap = pip_vol_check.val().Volume()
        except Exception:
            pip_overlap = 0.0
        print(f"  [print-in-place] giao nhau top/bottom o TRANG THAI MO = {pip_overlap:.4f} mm3"
              " (phai gan 0 -- xem check_hinge_sweep.py)")
        pip_path = export_print_in_place(top, bot_open, "assembly_open_print_in_place")
        print("  exported", pip_path, "(1 file STL duy nhat, in CA 2 nua CUNG LUC, o tu the MO)")

    print("Xong. File STEP/STL nằm trong:", OUT_DIR)


if __name__ == "__main__":
    main()
