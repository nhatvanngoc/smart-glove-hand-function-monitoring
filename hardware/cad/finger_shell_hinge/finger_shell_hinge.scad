// =====================================================================
// Khung ốp 1 đốt ngón tay — cơ chế BẢN LỀ + NGÀM CÀI (mã OpenSCAD)
// =====================================================================
// Tương ứng 1-1 về tham số & hình học với bản CadQuery đã chạy & xuất
// STEP/STL trong repo: hardware/cad/finger_shell_hinge/finger_shell_hinge.py
// (xem out/*.step, out/renders/*.png).
//
// LÝ DO CÓ CẢ 2 BẢN (CadQuery .py VÀ OpenSCAD .scad này):
//   - Sandbox dựng thiết kế này KHÔNG có apt/internet tới kho Debian, nên
//     KHÔNG cài được OpenSCAD lẫn FreeCAD GUI ở đó. Bản .py (CadQuery, cài
//     qua pip, dùng chung lõi hình học Open CASCADE với FreeCAD) là bản ĐÃ
//     CHẠY VÀ KIỂM TRA HÌNH HỌC THẬT trong sandbox đó (xuất STEP/STL, dựng
//     ảnh xem nhanh trong out/renders/).
//   - File .scad này viết tay theo đúng công thức/toạ độ của bản .py, để
//     bạn mở trực tiếp bằng OpenSCAD (miễn phí, https://openscad.org) trên
//     máy mình — KHÔNG cần cài gì thêm, không cần Python/pip.
//   - File .scad này **ĐÃ được chạy qua chính OpenSCAD 2025.01.19 thật**
//     (không phải mô phỏng) ngay trong sandbox, nhờ gói npm
//     openscad-wasm-prebuilt chạy qua Node.js — xem render_scad_wasm.mjs.
//     Cả 5 biến thể PART (top/bottom/pin/assembly_closed/assembly_open)
//     dựng thành khối đa diện hợp lệ ("Simple: yes", không lỗi CGAL) và
//     xuất STL thành công. Thể tích + bounding-box của top/bottom/pin khớp
//     bản .py (CadQuery/OCCT) trong sai số <0.3% (chỉ do rời rạc hoá $fn)
//     — xem cross_check.py và README §5. Đây là bằng chứng 2 lõi hình học
//     ĐỘC LẬP (OCCT vs CGAL) đồng ý với nhau, KHÔNG phải bằng chứng thiết
//     kế đã đúng công thái học/cơ học (vẫn cần in + đo thật, xem README §8).
//
// TRẠNG THÁI: `PROPOSED` — xem CLM-HW-004 / DEC-HW-006 trong
// research/claims/CLAIM_LEDGER.csv và research/context/DECISION_LOG.md.
// Kích thước đốt ngón (W_in/H_in/L) là SỐ GIẢ ĐỊNH, PHẢI đo lại bằng
// thước cặp trước khi in bản dùng thật.
//
// LỖI ĐÃ SỬA 2026-10-07 (phát hiện bởi chủ dự án khi mở file này bằng
// chính OpenSCAD trên máy mình — cảm ơn vì đã bắt lỗi!): tay đòn ngàm cài
// (latch_arm, nửa lòng tay) từng cách thành vỏ ~2.8mm, không chạm vào đâu
// -> xuất STL bị tách thành 2 mảnh RỜI, không in được nguyên khối. Đã vá
// bằng cách thêm "gốc nối" (rib) trong module latch_arm(). Kiểm chứng lại
// bằng check_connectivity.py (đếm connected components qua trimesh) — xem
// README §5a để biết chi tiết đầy đủ. BÀI HỌC: file CAD "chạy được, không
// lỗi CGAL/OCCT" KHÔNG đồng nghĩa là mọi chi tiết đều liền 1 khối in được —
// luôn chạy check_connectivity.py sau khi sửa hình học.
//
// CÁCH DÙNG:
//   1. Cài OpenSCAD: https://openscad.org/downloads.html
//   2. Mở file này. Các biến có khối "/* [Tên nhóm] */" phía trên sẽ hiện
//      thành thanh trượt trong tab Customizer (Window > Customizer).
//   3. Đổi biến PART ở cuối file để chọn xem: "top" | "bottom" | "pin" |
//      "assembly_closed" | "assembly_open"
//   4. Nhấn F5 để xem nhanh (preview), F6 để render đầy đủ CSG (bắt buộc
//      trước khi xuất STL).
//   5. File > Export > Export as STL khi PART đang là chi tiết muốn in
//      ("top" hoặc "bottom" — KHÔNG in "assembly_*", chỉ để xem).
// =====================================================================

/* [1. Kích thước đốt ngón tay — PHẢI ĐO LẠI BẰNG THƯỚC CẶP] */
L    = 24.0; // chiều dài khung dọc theo ngón (mm)
W_in = 19.0; // bề rộng trong, hướng trụ-quay (mm)
H_in = 16.0; // bề dày trong, hướng mu-lòng (mm)

/* [2. Vỏ cứng] */
t_wall = 2.2; // bề dày thành khung (mm)
// 2026-10-07 (theo yêu cầu "đổi sang hình trụ, bớt vuông cứng"): bỏ bo góc
// chữ nhật kiểu cũ (r_in/r_out). Tiết diện giờ là "viên thuốc dẹt": 2 mặt
// mu/lòng tay có 1 đoạn THẲNG rộng flat_w (chỗ dán cảm biến), 2 cạnh hông
// (bản lề + ngàm cài) bo tròn HẾT MỨC bằng 1 cung ELIP lớn. Xem capsule_prism().
flat_w = 12.0; // bề rộng đoạn thẳng ở giữa mặt mu/lòng tay (mm)

/* [3. Hốc cảm biến Velostat + đồng tự dính] */
pocket_w     = 8.0;  // bề rộng hốc
pocket_len   = 16.0; // chiều dài hốc dọc theo ngón
pocket_depth = 1.3;  // độ sâu khoét vào vách

/* [4. Rãnh luồn dây tín hiệu] */
wire_w     = 2.2;
wire_depth = 1.2;

/* [5. Bản lề - cạnh Y = -W_out/2] */
margin_x        = 2.0; // chừa 2 đầu trục X không có khớp
n_knuckle_top   = 3;   // số khớp ống thuộc nửa mu tay — PHẢI = n_knuckle_bot + 1
n_knuckle_bot   = 2;   // số khớp ống thuộc nửa lòng tay
knuckle_gap     = 0.5; // khe hở in 3D giữa các khớp ống
r_knuckle       = 3.0; // bán kính ngoài khớp ống
// 2026-10-07 (theo yêu cầu "in tại chỗ, tự do xoay ngay sau khi in" — xem
// README §5e): r_pin = bán kính LỖ trên khớp ống nửa lòng tay; khi
// PIN_INTEGRATED=true, trục đặc hàn vào nửa mu tay có bán kính =
// r_pin - pin_clearance. Trước đây khe hở là số viết tay 0.15mm, QUÁ CHẶT
// cho kiểu in-tại-chỗ (dễ dính liền 2 khối nếu máy in chưa hiệu chỉnh hoàn
// hảo) — các nguồn hướng dẫn in FDM khuyến nghị 0.2-0.4mm. Tăng lỗ lên
// 1.3mm để giữ nguyên bán kính trục đặc ~1.0mm mà đạt khe hở 0.3mm.
r_pin           = 1.3; // bán kính lỗ xỏ chốt/khớp xoay (lỗ phi ~2.6mm)
pin_clearance   = 0.3; // khe hở BÁN KÍNH trục-lỗ (mm) -- CẦN HIỆU CHỈNH
                        // theo máy in/vật liệu thật, xem README §5e
// 2026-10-08 (§5f, theo yêu cầu "đảm bảo không dễ rơi ra ngoài"): LỖI PHÁT
// HIỆN -- trục cũ (hinge_pin() dưới đây) là hình trụ bán kính KHÔNG ĐỔI
// suốt chiều dài, 2 đầu chỉ bo tròn (capsule) chứ KHÔNG có vai/mũ chặn lớn
// hơn lỗ khớp ống -> KHÔNG CÓ GÌ ngăn nửa lòng tay trượt dọc trục X và
// tuột hẳn ra khỏi trục. Khắc phục: thêm 2 "vai chặn" hình TRỤ ĐỒNG TRỤC
// (collar, bán kính pin_retain_r > r_pin) ở GIỮA khớp ống ĐẦU và CUỐI
// thuộc nửa mu tay (đã có sẵn vật liệu boss r_knuckle=3.0mm bao quanh ở
// đó) -- vai chặn ẩn gọn trong boss có sẵn, KHÔNG tạo gờ nhô mới. Mọi khớp
// ống nửa lòng tay (lỗ bán kính r_pin) đều nằm GIỮA 2 vai chặn này theo
// trục X nên không thể trượt dọc trục để tuột ra ngoài (kiểm chứng bằng
// check_axial_retention.py). Dùng hình TRỤ (không phải hình CẦU) vì hình
// cầu tạo điểm cực kỳ dị khi xuất STL -> check_connectivity.py báo nhầm
// "mảnh rời". Chỉ áp dụng khi PIN_INTEGRATED=true.
pin_retain_r    = 2.2; // bán kính vai chặn (mm) -- phải > r_pin (1.3mm) để
                        // chặn tuột, và < r_knuckle (3.0mm) để ẩn gọn
pin_retain_len  = 2.0;  // chiều dài mỗi vai chặn (mm)
knuckle_overlap = 0.5; // phần khớp ống "ăn" vào thành vỏ để liền khối

/* [6. Ngàm cài - cạnh Y = +W_out/2] */
catch_h     = 14.0; // chiều cao khối ngàm cố định (mu tay) -- PHẢI >= (arm_h - 1.0 + 1.5)
                     // để chứa hết nấc răng gần điểm nghỉ của móc (xem latch_catch(), §5c)
catch_t     = 2.2;  // bề dày khối ngàm
tooth_h     = 0.9;  // độ nhô mỗi nấc răng
tooth_pitch = 2.6;  // khoảng cách giữa 2 nấc
arm_h       = 13.0; // chiều dài tay đòn đàn hồi (lòng tay)
arm_t       = 1.1;  // bề dày tay đòn
arm_hook    = 1.1;  // độ sâu móc ở đầu tay đòn

/* [7. Dây đai phụ - khoá an toàn lớp 2] */
strap_slot_w = 3.2;
strap_slot_h = 6.0;

/* [8. Xem trước / xuất file] */
PART = "assembly_open"; // "top" | "bottom" | "pin" | "assembly_closed" | "assembly_open"
// LỖI NGHIÊM TRỌNG ĐÃ SỬA 2026-10-07 (§5e): dấu CŨ của OPEN_ANGLE (+150) là
// HƯỚNG XOAY SAI -- 2 nửa vỏ ĐÂM XUYÊN NHAU thật (giao nhau hình học tới
// ~600mm3 ở bản .py tương đương) trong khoảng góc +5..+100°, chỉ "trông ổn"
// ở ảnh render vì ảnh cũ CHỈ xem ở đúng 1 góc cuối (150°, nơi 2 nửa tình cờ
// tách rời). Đã quét toàn bộ dải góc bằng CadQuery (check_hinge_sweep.py,
// bản .py) và xác nhận chiều ÂM (-150°) mới là hướng xoay KHÔNG va chạm.
// assembly_open() bên dưới đã đổi dấu cho đúng.
OPEN_ANGLE = 150;       // độ (giá trị DƯƠNG, độ lớn góc mở) -- dùng khi PART = "assembly_open"

// 2026-10-07, theo yêu cầu chủ dự án: true = HÀN LIỀN trục chốt vào nửa mu
// tay (in top_shell + trục thành 1 khối duy nhất, không cần lắp chốt rời —
// chỉ nửa lòng tay vẫn tách riêng vì phải xoay quanh trục). false = thiết
// kế cũ: chốt là 1 chi tiết RỜI (PART="pin"), xỏ qua lỗ xuyên cả 2 nửa sau
// khi in (xem README §5b: đánh đổi — tích hợp thì gọn hơn, nhưng KHÔNG còn
// thay được bằng que kim loại cứng nếu trục in bị gãy).
PIN_INTEGRATED = true;

$fn = 48; // độ mịn hình tròn (giảm còn ~24 nếu máy chạy preview chậm)

// =====================================================================
// Tham số dẫn xuất
// =====================================================================
W_out   = W_in + 2 * t_wall;
H_out   = H_in + 2 * t_wall;
y_hinge = -(W_out / 2) - r_knuckle + knuckle_overlap; // trục Y của bản lề

assert(n_knuckle_top == n_knuckle_bot + 1,
       "n_knuckle_top phai = n_knuckle_bot + 1 de xen ke deu (T B T B T ...)");

function n_knuckle_total() = n_knuckle_top + n_knuckle_bot;
function seg_width() =
    ((L - 2 * margin_x) - knuckle_gap * (n_knuckle_total() - 1)) / n_knuckle_total();

// =====================================================================
// 1) KHỐI NGUYÊN THỦY
// =====================================================================

// Hình trụ trục dọc theo X, tâm tại gốc cục bộ, dài l, bán kính r.
// (hull của các hình trụ loại này tạo ra hộp bo góc — xem rounded_box_x)
module cyl_x(r, l) {
    rotate([0, 90, 0])
        cylinder(h = l, r = r, center = true, $fn = $fn);
}

// Hộp chữ nhật bo góc, trục dài dọc theo X, trải từ x0 đến x0+len.
// Tương đương fillet() các cạnh song song X của 1 lăng trụ (w x h) trong CadQuery.
module rounded_box_x(len, w, h, r, x0 = 0) {
    translate([x0 + len / 2, 0, 0])
        hull() {
            for (yy = [-(w / 2 - r), (w / 2 - r)])
                for (zz = [-(h / 2 - r), (h / 2 - r)])
                    translate([0, yy, zz])
                        cyl_x(r, len);
        }
}

// "Viên nang" (capsule) trục X, tâm tại gốc cục bộ, dài tổng l (tính cả 2 chỏm
// cầu), bán kính r -- giống cyl_x nhưng 2 đầu được BO TRÒN (chỏm bán cầu) thay
// vì cắt vuông. Dùng cho trục bản lề (hinge_pin) để không còn cạnh sắc ở 2 đầu
// thò ra, dễ lắp/luồn hơn và an toàn hơn khi chạm da. (2026-10-07, yêu cầu "bo
// tròn" của chủ dự án)
module capsule_x(r, l) {
    // Dùng union() của 1 trụ ngắn hơn (dài l - 2r) + 2 chỏm cầu ở 2 đầu,
    // thay vì hull() của 2 hình cầu: cho kết quả HÌNH HỌC giống hệt (cùng
    // là 1 "viên nang") nhưng ổn định hơn với bộ dựng hình CGAL của
    // OpenSCAD khi union() với các khối phức tạp khác trong cùng 1 chi
    // tiết (tránh lỗi "CGAL assertion violation" quan sát được khi dùng
    // hull() trực tiếp trong ngữ cảnh lắp ráp đầy đủ -- xem README §5c).
    rotate([0, 90, 0]) {
        cylinder(h = l - 2 * r, r = r, center = true, $fn = $fn);
        translate([0, 0, -(l / 2 - r)]) sphere(r = r, $fn = $fn);
        translate([0, 0, (l / 2 - r)]) sphere(r = r, $fn = $fn);
    }
}

// Danh sách điểm (Y,Z) của tiết diện "viên thuốc dẹt": PHẲNG ở giữa 2 mặt
// mu/lòng tay (rộng flat_w), BO TRÒN hết mức ở 2 cạnh hông bằng 1 cung ELIP
// lớn (bán trục Y = w/2-flat_w/2, bán trục Z = h/2), nối tiếp tuyến với đoạn
// thẳng (không góc vuông). Tương đương rounded_prism() trong bản .py.
// (2026-10-07, theo yêu cầu "đổi sang hình trụ, bớt vuông cứng")
function capsule_profile_pts(w, h, flat_w, n = 16) =
    let(hf = flat_w / 2, a = w / 2 - hf, b = h / 2)
    concat(
        [[hf, h / 2], [-hf, h / 2]],
        [for (i = [1 : n]) let(t = 90 + i * 90 / n) [-hf + a * cos(t), b * sin(t)]],
        [for (i = [1 : n]) let(t = 180 + i * 90 / n) [-hf + a * cos(t), b * sin(t)]],
        [[hf, -h / 2]],
        [for (i = [1 : n]) let(t = 270 + i * 90 / n) [hf + a * cos(t), b * sin(t)]],
        [for (i = [1 : n]) let(t = 0 + i * 90 / n) [hf + a * cos(t), b * sin(t)]]
    );

// Lăng trụ dọc theo X, tiết diện (Y,Z) là "viên thuốc dẹt" ở trên.
module capsule_prism(length_x, w, h, flat_w, x0 = 0, length_margin = 0) {
    pts = capsule_profile_pts(w, h, flat_w, 16);
    translate([x0, 0, 0])
        rotate([0, 90, 0])
            linear_extrude(height = length_x + length_margin)
                // polygon() nhận (local_x,local_y); sau rotate([0,90,0]) thì
                // global_y=local_y, global_z=-local_x -- nên truyền [-Z,Y]
                // để bù lại, cho global (Y,Z) đúng như tiết diện mong muốn.
                polygon(points = [for (p = pts) [-p[1], p[0]]]);
}

// =====================================================================
// 2) ỐNG CƠ SỞ (vỏ ngoài trừ lòng trong) + CẮT ĐÔI theo mặt Z=0
// =====================================================================
module base_tube() {
    difference() {
        capsule_prism(L, W_out, H_out, flat_w, x0 = 0);
        capsule_prism(L + 4, W_in, H_in, flat_w, x0 = -2);
    }
}

// sign = +1 -> nửa Z>0 (mu tay/dorsal) ; sign = -1 -> nửa Z<0 (lòng tay/palmar)
module half_space(sign) {
    big = 400;
    translate([-big / 2, -big / 2, sign > 0 ? 0 : -big])
        cube([big, big, big]);
}

module split_half(sign) {
    intersection() {
        base_tube();
        half_space(sign);
    }
}

// =====================================================================
// 3) HỐC CẢM BIẾN + RÃNH DÂY (để TRỪ khỏi vỏ)
// =====================================================================
module sensor_pocket(sign) {
    z_face = sign * H_in / 2;
    translate([L / 2, 0, z_face + sign * (pocket_depth / 2 - 0.2)])
        cube([pocket_len, pocket_w, pocket_depth + 0.4], center = true);
}

module wire_channel(sign) {
    z_face  = sign * H_in / 2;
    wire_len = (L / 2 - pocket_len / 2) + 1.0;
    translate([wire_len / 2, 0, z_face + sign * (wire_depth / 2 - 0.2)])
        cube([wire_len, wire_w, wire_depth + 0.4], center = true);
}

// =====================================================================
// 4) BẢN LỀ — khớp ống so le (để CỘNG vào vỏ) + lỗ chốt (để TRỪ)
// =====================================================================
// SỬA LỖI 2026-10-07 (§5e): cyl_x() là 1 hình trụ TRÒN ĐỦ, tâm đúng tại
// z=0 (mặt phân 2 nửa) -> một nửa khối của nó luôn tràn sang phía NỬA
// KHÔNG THUỘC VỀ NÓ (vd. khớp ống của top lại có vật liệu ở Z<0, đè lên
// đúng chỗ bottom_shell cần chiếm) -> gây chồng lấn hình học ~9.4mm3 dù 2
// nửa không in dính nhau (rotation-invariant nên không phụ thuộc góc
// xoay). Cắt boss về đúng nửa KHÔNG GIAN của chính nó (top -> Z>=0,
// bot -> Z<=0) bằng intersection() với half_space() trước khi thêm vào vỏ.
module hinge_knuckles(which) {
    n    = n_knuckle_total();
    sw   = seg_width();
    sign = (which == "top") ? 1 : -1;
    for (i = [0 : n - 1]) {
        is_top = (i % 2 == 0); // thứ tự T B T B T... (bắt đầu & kết thúc bằng top)
        if ((which == "top" && is_top) || (which == "bot" && !is_top)) {
            xs = margin_x + i * (sw + knuckle_gap);
            intersection() {
                translate([xs + sw / 2, y_hinge, 0])
                    cyl_x(r_knuckle, sw);
                half_space(sign);
            }
        }
    }
}

module hinge_pinhole() {
    hole_len = (L - 2 * margin_x) + 4;
    translate([margin_x - 2 + hole_len / 2, y_hinge, 0])
        cyl_x(r_pin, hole_len);
}

// =====================================================================
// 5) NGÀM CÀI — khối răng (mu tay, để CỘNG) + tay đòn đàn hồi (lòng tay, để CỘNG)
// =====================================================================
// SỬA LỖI #3 2026-10-07 (phát hiện khi "check lại cơ chế chính xác" theo
// yêu cầu chủ dự án): bản cũ đặt vị trí RĂNG theo một tỉ lệ ĐỘC LẬP với
// catch_h (`catch_h * 0.35 + i*tooth_pitch` => z~2.45-6.45mm), trong khi
// vị trí nghỉ của MÓC (hook, ở đầu tay đòn) lại tính độc lập theo arm_h
// (`arm_h - 1.0` => z~11.2-12.8mm) — LỆCH NHAU 5-9mm, không bao giờ chạm
// được vào nhau (kiểm chứng bằng toạ độ: xem README §5c). Tức là ngàm cài
// NHƯ CŨ KHÔNG THỂ khoá được — móc vung qua phía trên hẳn các nấc răng.
// Khắc phục: tính vị trí răng TRỰC TIẾP từ vị trí nghỉ của móc (cùng công
// thức `arm_h - 1.0` dùng trong latch_arm()) thay vì một tỉ lệ độc lập,
// để 2 chi tiết LUÔN thẳng hàng dù sau này có đổi arm_h/tooth_pitch.
module latch_catch() {
    y0 = W_out / 2;
    x0 = margin_x; x1 = L - margin_x;
    w  = x1 - x0;
    xc = (x0 + x1) / 2;

    hook_rest_z = arm_h - 1.0; // PHẢI giống hệt công thức trong latch_arm()
    assert(catch_h >= hook_rest_z + 1.5,
           "catch_h phai >= arm_h - 1.0 + 1.5 de chua het nac rang gan diem nghi cua moc");

    // 2026-10-07 "bo tròn": khối ngàm chính giờ bo góc dọc theo chiều dài
    // (giống cách bo r_out của thân ống) thay vì cube() cạnh vuông sắc --
    // r nhỏ, an toàn (không chạm tới vùng các răng chèn vào ở cạnh +Y).
    r_catch = min(0.8, catch_t / 2 - 0.3, catch_h / 2 - 0.3);
    translate([0, y0 + catch_t / 2 - 0.3, catch_h / 2])
        rounded_box_x(w, catch_t, catch_h, r_catch, x0 = x0);

    // Nấc 0 (i=0) nằm NGAY TẠI điểm nghỉ tự nhiên của móc -> đây là nấc
    // móc sẽ tự ăn khớp khi gập hẳn xuống (đóng hoàn toàn, không cần giữ).
    // Nấc 1 nằm THẤP hơn 1 khoảng tooth_pitch -> móc phải trượt/lướt qua
    // nấc này trước (cảm giác "tách" 2 nấc khi gập), chưa dừng lại ở đó.
    // Mỗi nấc cũng được bo nhẹ cạnh (r nhỏ) để giảm ứng suất tập trung khi
    // in 3D và cho cảm giác cài/mở mượt hơn (ít bị vướng cạnh sắc).
    r_tooth = min(0.3, tooth_h - 0.1, 1.4 / 2 - 0.1);
    for (i = [0 : 1]) {
        zt = hook_rest_z - i * tooth_pitch;
        translate([0, y0 + catch_t - 0.3 + tooth_h * 0.4, zt])
            rounded_box_x(w, tooth_h * 2, 1.4, r_tooth, x0 = x0);
    }
}

// SUA LOI 2026-10-07 (phat hien boi chu du an khi mo file nay bang chinh
// OpenSCAD -- xem README Sec.5a "Loi da sua"): ban goc dat `arm` bat dau tu
// y = y0 + catch_t + arm_t/2 + 0.6 ~= 15.05mm, trong khi mep ngoai cung cua
// vo (shell) chi toi y = y0 = W_out/2 ~= 11.7mm -- lech mot khoang trong
// ~2.8mm, KHONG cham vo o bat ky lat cat Z nao. He qua: tay don (+ moc) la
// mot khoi ROI, troi lo lung, khong in duoc. Da kiem chung bang trimesh
// (xem check_connectivity.py): STL cu tach thanh 2 manh roi nhau.
// Khac phuc: them "goc noi" (root/rib) dac, bac cau tu mep vo that (lan
// 0.3mm vao vo, giong add_latch_catch) toi mat trong tay don (lan them
// 0.3mm vao tay don), nam gon trong vung z <= 0 (nua long tay), khong dung
// khoi rang o nua mu tay.
module latch_arm() {
    y0 = W_out / 2;
    x0 = margin_x; x1 = L - margin_x;
    w  = x1 - x0;
    xc = (x0 + x1) / 2;

    y_arm_center = y0 + catch_t + arm_t / 2 + 0.6;
    y_arm_outer  = y_arm_center + arm_t / 2;

    // 2026-10-07 "bo tròn": thân tay đòn + móc bo nhẹ cạnh dọc chiều dài
    // (giống khối ngàm) -- r rất nhỏ vì arm_t/arm_hook khá mỏng, không ảnh
    // hưởng vùng chân (root) nối với vỏ (đã kiểm lại bằng check_connectivity.py).
    r_arm  = min(0.3, arm_t / 2 - 0.2);
    r_hook = min(0.3, (arm_hook + arm_t) / 2 - 0.2, 1.6 / 2 - 0.2);

    translate([0, y_arm_center, arm_h / 2])
        rounded_box_x(w, arm_t, arm_h, r_arm, x0 = x0);

    translate([0, y0 + catch_t + arm_t - arm_hook / 2 + 0.2, arm_h - 1.0])
        rounded_box_x(w, arm_hook + arm_t, 1.6, r_hook, x0 = x0);

    // Goc noi (rib): bac cau khoang trong giua vo that va chan tay don.
    root_h = 3.0;
    eps = 0.2;
    y_root_in  = y0 - 0.3;
    y_root_out = y_arm_outer + 0.3;
    translate([xc, (y_root_in + y_root_out) / 2, -root_h / 2 + eps / 2])
        cube([w, y_root_out - y_root_in, root_h + eps], center = true);
}

// =====================================================================
// 6) KHE DÂY ĐAI PHỤ (để TRỪ khỏi vỏ)
// =====================================================================
module strap_slots(sign) {
    z_mid = sign * H_in / 2;
    for (xc = [margin_x + 1.5, L - margin_x - 1.5])
        translate([xc, 0, z_mid])
            cube([strap_slot_w, W_out * 0.9, strap_slot_h], center = true);
}

// =====================================================================
// 7) LẮP RÁP TỪNG CHI TIẾT
// =====================================================================
// PIN_INTEGRATED=true (mặc định, theo yêu cầu 2026-10-07): KHÔNG khoan lỗ
// chốt ở nửa mu tay, HÀN LIỀN (union) trục ngay vào top_shell -> in top +
// trục thành 1 khối duy nhất. Nửa lòng tay LUÔN khoan lỗ (khe hở 0.15mm)
// để trượt/xoay tự do quanh trục cố định này, dù PIN_INTEGRATED là gì.
module top_shell() {
    difference() {
        union() {
            split_half(+1);
            hinge_knuckles("top");
            latch_catch();
            if (PIN_INTEGRATED) hinge_pin();
        }
        union() {
            sensor_pocket(+1);
            wire_channel(+1);
            if (!PIN_INTEGRATED) hinge_pinhole();
            strap_slots(+1);
        }
    }
}

module bottom_shell() {
    difference() {
        union() {
            split_half(-1);
            hinge_knuckles("bot");
            latch_arm();
        }
        union() {
            sensor_pocket(-1);
            wire_channel(-1);
            hinge_pinhole();
            strap_slots(-1);
        }
    }
}

// Toạ độ X TOÀN CỤC (global) của tâm khớp ống "top" thứ `i` (xem hinge_knuckles()).
function knuckle_center_x(i) = margin_x + i * (seg_width() + knuckle_gap) + seg_width() / 2;

module hinge_pin() {
    hole_len = (L - 2 * margin_x) + 4;
    pin_len  = hole_len + 1;
    x_origin = margin_x - 2.5; // gốc cục bộ của trục, khớp với translate() bên dưới
    union() {
        translate([x_origin + pin_len / 2, y_hinge, 0])
            // 2026-10-07: bo tròn (capsule) thay vì cắt vuông -- 2 đầu trục giờ
            // là chỏm bán cầu, không còn cạnh sắc, dễ dùng làm mồi luồn qua các
            // khớp ống khi lắp ráp và an toàn hơn khi đầu trục lộ ra ngoài.
            capsule_x(r_pin - pin_clearance, pin_len); // khe hở = pin_clearance (xem §5e)
        // SỬA LỖI 2026-10-08 (§5f): 2 vai chặn chống tuột dọc trục -- xem
        // giải thích đầy đủ ở khai báo pin_retain_r phía trên.
        if (PIN_INTEGRATED) {
            x_first = knuckle_center_x(0);
            x_last  = knuckle_center_x(n_knuckle_total() - 1);
            for (xg = [x_first, x_last])
                translate([xg, y_hinge, 0])
                    cyl_x(pin_retain_r, pin_retain_len);
        }
    }
}

// Đặt mảnh để in: xoay 90° quanh Y để trục bản lề (X cục bộ) nằm DỌC
// (trùng trục Z máy in) — lỗ chốt sẽ in theo từng lớp tròn, không cần support.
// Dùng chức năng "đặt lại lên bàn in / lay flat" của slicer sau khi xuất STL.
module top_shell_print_ready()    { rotate([0, -90, 0]) top_shell(); }
module bottom_shell_print_ready() { rotate([0, -90, 0]) bottom_shell(); }

// =====================================================================
// 8) TRẠNG THÁI LẮP RÁP (chỉ để XEM, KHÔNG xuất STL ở các module này)
// =====================================================================
module assembly_closed() {
    color("Orange")     top_shell();
    color("SteelBlue")  bottom_shell();
    // Neu PIN_INTEGRATED=true, truc da nam san trong top_shell() (union o
    // dinh nghia top_shell ben tren) nen KHONG ve them nua (tranh trung lap).
    if (!PIN_INTEGRATED) color("DimGray") hinge_pin();
}

// Xoay nửa lòng tay quanh trục bản lề (đường thẳng qua (*, y_hinge, 0),
// song song trục X) — minh hoạ thao tác "mở ra để đặt ngón vào".
// LỖI ĐÃ SỬA 2026-10-07 (phát hiện bởi chủ dự án: "thiếu cái trục ở giữa
// bản lề"): trước đây assembly_closed()/assembly_open() chỉ vẽ top_shell()
// + bottom_shell(), QUÊN vẽ hinge_pin() -> nhìn vào thấy 2 nửa khớp ống kề
// nhau nhưng không có chốt xuyên qua, trông như bản lề "rỗng". Trục nằm
// đúng trên đường tâm xoay (y = y_hinge, z = 0, song song trục X) nên vị
// trí KHÔNG đổi giữa đóng/mở — chỉ cần vẽ thêm, không cần xoay theo.
module assembly_open(angle = OPEN_ANGLE) {
    color("Orange") top_shell();
    color("SteelBlue")
        translate([0, y_hinge, 0])
        rotate([-abs(angle), 0, 0]) // xem ghi chú OPEN_ANGLE ở trên -- ÂM mới đúng
        translate([0, -y_hinge, 0])
        bottom_shell();
    if (!PIN_INTEGRATED) color("DimGray") hinge_pin();
}

// =====================================================================
// 9) CHỌN PHẦN CẦN XEM/XUẤT
// =====================================================================
if (PART == "top") {
    top_shell();
} else if (PART == "bottom") {
    bottom_shell();
} else if (PART == "top_print") {
    top_shell_print_ready();
} else if (PART == "bottom_print") {
    bottom_shell_print_ready();
} else if (PART == "pin") {
    hinge_pin();
} else if (PART == "assembly_closed") {
    assembly_closed();
} else if (PART == "assembly_open") {
    assembly_open();
} else {
    echo(str("PART khong hop le: ", PART));
}
