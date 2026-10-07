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
r_in   = 2.5; // bo góc mặt trong
r_out  = 4.0; // bo góc mặt ngoài

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
r_pin           = 1.15;// bán kính lỗ xỏ chốt (lỗ phi ~2.3mm cho chốt phi 2.0-2.2mm)
knuckle_overlap = 0.5; // phần khớp ống "ăn" vào thành vỏ để liền khối

/* [6. Ngàm cài - cạnh Y = +W_out/2] */
catch_h     = 9.0;  // chiều cao khối ngàm cố định (mu tay)
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
OPEN_ANGLE = 150;       // độ, dùng khi PART = "assembly_open"

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

// =====================================================================
// 2) ỐNG CƠ SỞ (vỏ ngoài trừ lòng trong) + CẮT ĐÔI theo mặt Z=0
// =====================================================================
module base_tube() {
    difference() {
        rounded_box_x(L, W_out, H_out, r_out, x0 = 0);
        rounded_box_x(L + 4, W_in, H_in, r_in, x0 = -2);
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
module hinge_knuckles(which) {
    n  = n_knuckle_total();
    sw = seg_width();
    for (i = [0 : n - 1]) {
        is_top = (i % 2 == 0); // thứ tự T B T B T... (bắt đầu & kết thúc bằng top)
        if ((which == "top" && is_top) || (which == "bot" && !is_top)) {
            xs = margin_x + i * (sw + knuckle_gap);
            translate([xs + sw / 2, y_hinge, 0])
                cyl_x(r_knuckle, sw);
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
module latch_catch() {
    y0 = W_out / 2;
    x0 = margin_x; x1 = L - margin_x;
    w  = x1 - x0;
    xc = (x0 + x1) / 2;

    translate([xc, y0 + catch_t / 2 - 0.3, catch_h / 2])
        cube([w, catch_t, catch_h], center = true);

    for (i = [0 : 1]) {
        zt = catch_h * 0.35 + i * tooth_pitch;
        translate([xc, y0 + catch_t - 0.3 + tooth_h * 0.4, zt])
            cube([w, tooth_h * 2, 1.4], center = true);
    }
}

module latch_arm() {
    y0 = W_out / 2;
    x0 = margin_x; x1 = L - margin_x;
    w  = x1 - x0;
    xc = (x0 + x1) / 2;

    translate([xc, y0 + catch_t + arm_t / 2 + 0.6, arm_h / 2])
        cube([w, arm_t, arm_h], center = true);

    translate([xc, y0 + catch_t + arm_t - arm_hook / 2 + 0.2, arm_h - 1.0])
        cube([w, arm_hook + arm_t, 1.6], center = true);
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
module top_shell() {
    difference() {
        union() {
            split_half(+1);
            hinge_knuckles("top");
            latch_catch();
        }
        union() {
            sensor_pocket(+1);
            wire_channel(+1);
            hinge_pinhole();
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

module hinge_pin() {
    hole_len = (L - 2 * margin_x) + 4;
    pin_len  = hole_len + 1;
    translate([margin_x - 2.5 + pin_len / 2, y_hinge, 0])
        cyl_x(r_pin - 0.15, pin_len); // khe hở lắp 0.15mm bán kính
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
}

// Xoay nửa lòng tay quanh trục bản lề (đường thẳng qua (*, y_hinge, 0),
// song song trục X) — minh hoạ thao tác "mở ra để đặt ngón vào".
module assembly_open(angle = OPEN_ANGLE) {
    color("Orange") top_shell();
    color("SteelBlue")
        translate([0, y_hinge, 0])
        rotate([angle, 0, 0])
        translate([0, -y_hinge, 0])
        bottom_shell();
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
