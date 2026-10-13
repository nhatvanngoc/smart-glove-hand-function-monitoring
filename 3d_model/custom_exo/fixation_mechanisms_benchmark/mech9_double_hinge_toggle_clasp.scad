// =============================================================================
// CƠ CẤU "BẢN LỀ KÉP – QUAI GÔNG KẸP NGÀM ĐỰC ĐÔI" (DOUBLE-HINGE TOGGLE CLASP)
// Phiên bản V9.7: TỐI ƯU KHỚP GÀI CÔNG THÁI HỌC (ERGONOMIC TACTILE SNAP)
// 1. Bản lề 1 & 2 xoay trơn tuyệt đối: Trục phi 2.6mm, Lỗ phi 3.7mm (Khe hở 0.55mm, Khe trục 0.7-0.8mm).
// 2. Vát côn tự đỡ 45 độ chống sệ sợi bắc cầu cho toàn bộ các tai bản lề.
// 3. Khớp gài lực vừa vặn: Giảm độ cắn ngàm từ 0.70mm xuống 0.35mm (không bị quá chặt).
// 4. Rãnh khóa ngàm âm có vách thoát vát 45-50 độ (triệt tiêu góc vuông kẹt gờ, gạt mở êm ru).
// 5. Thân quai kẹp dày 1.70mm tạo độ đàn hồi chuẩn (Spring Beam), bấm vào "tách" giòn, bẩy mở nhẹ tay.
// 6. Cần gạt mở thiết kế công thái học đón ngón cái, bẩy nhẹ nhàng không đau tay.
// =============================================================================

/* [CHẾ ĐỘ HIỂN THỊ] */
MODE = "PRINT_READY"; // [ASSEMBLY, SECTION_CUT, PRINT_READY, DORSAL_ONLY, PALMAR_ONLY, CLASP_ONLY]

OPEN_ANGLE_1 = 110; // [0:1:140] - Mở 110 độ triệt tiêu hoàn toàn góc hẹp dính bàn in Z=0
OPEN_ANGLE_2 = 100; // [0:1:140] - Quai kẹp mở quanh Bản lề 2

SHOW_FINGER = false;

/* [THÔNG SỐ HÌNH HỌC CỐT LÕI (mm)] */
D_FINGER    = 23.6;             // Đường kính ngón tay danh nghĩa (mm)
R_IN        = D_FINGER / 2;     // 11.80 mm
R_OUT       = 14.10;            // Bán kính ngoài thân vỏ danh nghĩa (Dày 2.30mm)
L_CUFF      = 15.00;            // Chiều dài đốt ngón tay = 15.00 mm

/* [BẢN LỀ 1 - SƯỜN TRÁI (SIDE A - FREE-SPINNING MAIN HINGE)] */
H1_X        = -14.40;           // Tâm trục bản lề 1 X
H1_Y        = 0.00;             // Tâm trục bản lề 1 Y
PIN_R       = 1.30;             // Chốt xoay phi 2.6 mm
BORE_R      = 1.85;             // Lỗ bạc phi 3.7 mm (Khe hở hướng kính 0.55 mm - PIP XOAY TRƠN)
KNUCKLE_R   = 2.70;             // Bán kính ngoài tai bản lề 2.70 mm (Dày vách 0.85 mm)
Z_CAP       = 2.00;             // Chiều dày tai chặn 2 đầu (mm)
AXIAL_GAP   = 0.80;             // Khe hở dọc trục 0.80 mm CHỐNG DÍNH BẮC CẦU
Z_SLV_S     = Z_CAP + AXIAL_GAP;          // 2.80 mm - Đáy ống bọc
Z_SLV_E     = L_CUFF - Z_CAP - AXIAL_GAP; // 12.20 mm - Đỉnh ống bọc
Z_SLV_H     = Z_SLV_E - Z_SLV_S;          // 9.40 mm - Chiều dài ống bọc

/* [BẢN LỀ 2 - VAI NGÀM MU SƯỜN PHẢI (SIDE B - SECOND HINGE)] */
H2_X        = 16.50;            // Tâm trục bản lề 2 X
H2_Y        = 4.50;             // Tâm trục bản lề 2 Y
PIN2_R      = 1.30;             // Chốt bản lề 2 phi 2.6 mm
BORE2_R     = 1.85;             // Lỗ bản lề 2 phi 3.7 mm (Khe hở 0.55 mm)
KNUCKLE2_R  = 2.55;

/* [KÍCH THƯỚC NGÀM ĐỰC ĐÔI (DUAL PROTRUDING LUGS)] */
LUG_X_OUT   = 18.20;            // Đỉnh ngàm nhô ra X = 18.20 mm
LUG_Y_DOR   = 3.20;             // Bề dày ngàm mu (Y = 0 đến 3.20 mm)
LUG_Y_PAL   = -3.20;            // Bề dày ngàm lòng (Y = -3.20 đến 0 mm)

$fn = $preview ? 45 : 72;

// =============================================================================
// MAIN DISPATCHER
// =============================================================================
if (MODE == "ASSEMBLY") {
    assembly_view(0, 0);
} else if (MODE == "SECTION_CUT") {
    difference() {
        assembly_view(0, 0);
        translate([-50, -50, L_CUFF/2]) cube([100, 100, 50]);
    }
} else if (MODE == "PRINT_READY") {
    assembly_view(OPEN_ANGLE_1, OPEN_ANGLE_2);
} else if (MODE == "DORSAL_ONLY") {
    color([0.25, 0.85, 0.40]) dorsal_shell();
} else if (MODE == "PALMAR_ONLY") {
    color([0.30, 0.65, 1.00]) palmar_shell();
} else if (MODE == "CLASP_ONLY") {
    color([1.00, 0.45, 0.25]) clamping_frame();
}

if (SHOW_FINGER && (MODE == "ASSEMBLY" || MODE == "SECTION_CUT")) {
    %color([0.9, 0.75, 0.65, 0.35])
    cylinder(r = R_IN, h = L_CUFF + 6, center = true);
}

// =============================================================================
// ASSEMBLY VIEW
// =============================================================================
module assembly_view(ang1, ang2) {
    // 1. Nửa vỏ mu cố định
    color([0.25, 0.85, 0.40]) dorsal_shell();
    
    // 2. Nửa vỏ lòng xoay quanh Bản lề 1
    translate([H1_X, H1_Y, 0])
    rotate([0, 0, -ang1])
    translate([-H1_X, -H1_Y, 0])
    color([0.30, 0.65, 1.00]) palmar_shell();
    
    // 3. Quai gông kẹp xoay quanh Bản lề 2
    translate([H2_X, H2_Y, 0])
    rotate([0, 0, ang2])
    translate([-H2_X, -H2_Y, 0])
    color([1.00, 0.45, 0.25]) clamping_frame();
}

// =============================================================================
// 1. NỬA VỎ MU (DORSAL SHELL - Y >= 0)
// =============================================================================
module dorsal_shell() {
    union() {
        difference() {
            union() {
                // A. Vòm mu hình trụ bán nguyệt
                difference() {
                    cylinder(r = R_OUT, h = L_CUFF);
                    translate([0, 0, -1]) cylinder(r = R_IN, h = L_CUFF + 2);
                    translate([-30, -30, -1]) cube([60, 30, L_CUFF + 2]);
                }
                
                // B. NGÀM ĐỰC NỬA MU
                linear_extrude(height = L_CUFF) {
                    polygon([
                        [R_OUT * cos(13.0), R_OUT * sin(13.0)],
                        [R_OUT, 0],
                        [LUG_X_OUT, 0],
                        [LUG_X_OUT, LUG_Y_DOR],
                        [15.50, LUG_Y_DOR + 0.4],
                        [R_OUT * cos(13.0), R_OUT * sin(13.0)]
                    ]);
                }
                
                // C. BẢN LỀ 1 (SIDE A): 2 Tai chặn đầu trục bản lề + Cầu nối
                // Tai chặn dưới Z in [0, 2.0]
                translate([H1_X, H1_Y, 0]) cylinder(r = KNUCKLE_R, h = Z_CAP);
                translate([H1_X, 0.0, 0]) cube([abs(H1_X) - R_IN + 2.0, KNUCKLE_R, Z_CAP]);
                
                // Tai chặn trên Z in [13.0, 15.0] kèm vát côn 45 độ ở mặt dưới
                translate([H1_X, H1_Y, L_CUFF - Z_CAP]) cylinder(r = KNUCKLE_R, h = Z_CAP);
                translate([H1_X, 0.0, L_CUFF - Z_CAP]) cube([abs(H1_X) - R_IN + 2.0, KNUCKLE_R, Z_CAP]);
                
                // D. BẢN LỀ 2 (SIDE B): Ống bọc giữa trên vai ngàm mu (Z in [2.70, 12.30])
                difference() {
                    union() {
                        translate([H2_X, H2_Y, 2.70]) cylinder(r = KNUCKLE2_R, h = 9.60);
                        hull() {
                            translate([H2_X, H2_Y, 2.70]) cylinder(r = KNUCKLE2_R, h = 9.60);
                            translate([15.50, LUG_Y_DOR, 2.70]) cube([2.2, 0.4, 9.60]);
                        }
                    }
                    translate([0, 0, -1]) cylinder(r = R_IN, h = L_CUFF + 2);
                }
                
                // E. Tai gài dây chằng ngoại quan chuẩn
                translate([0, R_OUT - 0.8, L_CUFF/2]) {
                    difference() {
                        rotate([-90, 0, 0]) cylinder(r = 2.6, h = 4.6);
                        translate([0, 2.0, -L_CUFF]) cylinder(r = 1.1, h = L_CUFF*2);
                    }
                }
                ear_w = 4.8; ear_t = 2.6; reach = 9.0; gap_z = 2.5; z_tot = L_CUFF + reach + gap_z;
                translate([11.4, 2.5, 11.0]) difference() { union() { cube([ear_t, ear_w, z_tot - 11.0]); translate([0, ear_w/2, z_tot - 11.0]) rotate([0, 90, 0]) cylinder(r = ear_w/2, h = ear_t); } for (i = [0:2]) translate([-1, ear_w/2, (L_CUFF + gap_z + 1.2 - 11.0) + i * 2.2]) rotate([0, 90, 0]) cylinder(r = 1.5, h = ear_t + 2.0); }
                translate([-14.0, 2.5, 11.0]) difference() { union() { cube([ear_t, ear_w, z_tot - 11.0]); translate([0, ear_w/2, z_tot - 11.0]) rotate([0, 90, 0]) cylinder(r = ear_w/2, h = ear_t); } for (i = [0:2]) translate([-1, ear_w/2, (L_CUFF + gap_z + 1.2 - 11.0) + i * 2.2]) rotate([0, 90, 0]) cylinder(r = 1.5, h = ear_t + 2.0); }
            }
            
            // Khoang xoay ống bọc bản lề 1 (cắt hở từ Z_CAP đến L_CUFF - Z_CAP, khe hở 0.80mm)
            translate([H1_X, H1_Y, Z_CAP]) cylinder(r = KNUCKLE_R + 0.80, h = L_CUFF - 2*Z_CAP);
            
            // Vát côn 45 độ mặt dưới tai chặn trên (Z = 13.0) chống sệ rớt sợi
            translate([H1_X, H1_Y, L_CUFF - Z_CAP - 0.01])
            cylinder(r1 = PIN_R + 0.80, r2 = KNUCKLE_R + 0.80, h = 0.60);
            
            // Lỗ bạc bản lề 2 cho chốt quai kẹp (phi 3.7mm, khe hở 0.55mm)
            translate([H2_X, H2_Y, -1]) cylinder(r = BORE2_R, h = L_CUFF + 2);
            
            // Vát côn tự đỡ 45 độ ở đáy ống bọc H2 (Z = 2.70) chống sệ rớt sợi
            translate([H2_X, H2_Y, 2.70 - 0.01])
            cylinder(r1 = BORE2_R + 0.60, r2 = BORE2_R, h = 0.60);
            
            // Khe thoát dọc trục ở 2 đầu cho tai chặn và tay đòn quai kẹp (khe hở 0.70mm)
            translate([H2_X, H2_Y, -1]) cylinder(r = KNUCKLE2_R + 0.60, h = 3.70);
            translate([H2_X, H2_Y, 12.30]) cylinder(r = KNUCKLE2_R + 0.60, h = 4.70);
            
            // Cắt vát clearance thoát tay đòn xoay ở 2 đầu Z [0, 2.70] và [12.30, 15.0]
            hull() {
                translate([H2_X, H2_Y, -1]) cylinder(r = KNUCKLE2_R + 0.60, h = 3.70);
                translate([18.45, 1.20, -1]) cylinder(r = 1.0, h = 3.70);
            }
            hull() {
                translate([H2_X, H2_Y, 12.30]) cylinder(r = KNUCKLE2_R + 0.60, h = 4.70);
                translate([18.45, 1.20, 12.30]) cylinder(r = 1.0, h = 4.70);
            }
            
            // Hốc cảm biến Velostat trên mu ngón tay
            intersection() {
                cylinder(r = R_IN + 0.7, h = L_CUFF);
                translate([-4.0, 0, (L_CUFF - 10.0)/2]) cube([8.0, 20.0, 10.0]);
            }
            translate([0, R_IN - 1, L_CUFF/2]) rotate([-90, 0, 0]) cylinder(r = 0.8, h = 10);
            
            // Vát chân Elephant's Foot tại Z = 0 trên bàn in
            translate([H1_X, H1_Y, -0.1])
            difference() {
                cylinder(r = KNUCKLE_R + 2.0, h = 0.6);
                cylinder(r1 = KNUCKLE_R - 0.5, r2 = KNUCKLE_R, h = 0.6);
            }
        }
        
        // TRỤC CHỐT XOAY BẢN LỀ 1 ĐÚC LIỀN XUYÊN SUỐT (phi 2.6 mm, Z = 0 đến 15.0 mm ĐẶC 100%)
        translate([H1_X, H1_Y, 0]) cylinder(r = PIN_R, h = L_CUFF);
    }
}

// =============================================================================
// 2. NỬA VỎ LÒNG (PALMAR SHELL - Y <= 0)
// =============================================================================
module palmar_shell() {
    difference() {
        union() {
            // A. Vòm lòng hình trụ bán nguyệt
            difference() {
                cylinder(r = R_OUT, h = L_CUFF);
                translate([0, 0, -1]) cylinder(r = R_IN, h = L_CUFF + 2);
                translate([-30, 0, -1]) cube([60, 30, L_CUFF + 2]);
            }
            
            // B. NGÀM ĐỰC NỬA LÒNG (CÓ VÁT ĐÓN 45 ĐỘ Ở GÓC NGOÀI CHỐNG KẸT)
            linear_extrude(height = L_CUFF) {
                polygon([
                    [R_OUT, 0],
                    [LUG_X_OUT, 0],
                    [LUG_X_OUT, LUG_Y_PAL + 0.80],      // Bắt đầu vát đón 45 độ
                    [LUG_X_OUT - 0.80, LUG_Y_PAL],     // Kết thúc vát đón tại X=17.40, Y=-3.20
                    [15.50, LUG_Y_PAL - 0.4],
                    [R_OUT * cos(-13.0), R_OUT * sin(-13.0)],
                    [R_OUT, 0]
                ]);
            }
            
            // C. BẢN LỀ 1 (SIDE A): Ống bọc giữa trên vỏ lòng (Z in [2.8, 12.2])
            difference() {
                union() {
                    translate([H1_X, H1_Y, Z_SLV_S]) cylinder(r = KNUCKLE_R, h = Z_SLV_H);
                    translate([H1_X, -KNUCKLE_R, Z_SLV_S]) cube([abs(H1_X) - R_IN + 2.0, KNUCKLE_R, Z_SLV_H]);
                }
                translate([0, 0, -1]) cylinder(r = R_IN, h = L_CUFF + 2);
            }
        }
        
        // RÃNH KHÓA GÀI VÁT THOÁT ÊM (SMOOTH DETENT NOTCH, ĐỘ SÂU 0.45MM, VÁCH VÁT 45-50 ĐỘ)
        translate([0, 0, -1])
        linear_extrude(height = L_CUFF + 2) {
            polygon([
                [17.40, LUG_Y_PAL - 0.50],  // Đáy ngoài vát đón
                [17.40, LUG_Y_PAL],         // Bắt đầu dốc đón vào rãnh
                [16.70, LUG_Y_PAL + 0.45],  // Đỉnh rãnh cắn sâu 0.45mm (Y = -2.75mm)
                [16.20, LUG_Y_PAL + 0.45],  // Đáy rãnh tiếp xúc phẳng 0.50mm
                [15.65, LUG_Y_PAL],         // Vách thoát vát 50 độ lướt êm khi mở (Y = -3.20mm)
                [15.65, LUG_Y_PAL - 0.50],  // Đáy trong
                [17.40, LUG_Y_PAL - 0.50]   // Đóng vòng CCW
            ]);
        }
        
        // Lỗ bạc xoay quanh chốt bản lề 1 (phi 3.7 mm, khe hở 0.55 mm)
        translate([H1_X, H1_Y, -1]) cylinder(r = BORE_R, h = L_CUFF + 2);
        
        // Vát côn tự đỡ 45 độ ở đáy ống bọc (Z = 2.80) chống sệ sợi bắc cầu dính tai chặn dưới
        translate([H1_X, H1_Y, Z_SLV_S - 0.01])
        cylinder(r1 = BORE_R + 0.60, r2 = BORE_R, h = 0.60);
        
        // Khe thoát dọc trục cho 2 tai chặn của vỏ mu (khe hở an toàn 0.80 mm)
        translate([H1_X, H1_Y, -1]) cylinder(r = KNUCKLE_R + 0.80, h = Z_SLV_S + 1.0);
        translate([H1_X, H1_Y, Z_SLV_E]) cylinder(r = KNUCKLE_R + 0.80, h = L_CUFF - Z_SLV_E + 2.0);
        
        // Hốc cảm biến Velostat lòng bàn tay
        intersection() {
            cylinder(r = R_IN + 0.7, h = L_CUFF);
            translate([-4.0, -20.0, (L_CUFF - 10.0)/2]) cube([8.0, 20.0, 10.0]);
        }
        translate([0, -(R_IN - 1), L_CUFF/2]) rotate([90, 0, 0]) cylinder(r = 0.8, h = 10);
        
        // Vát chân Elephant's Foot tại Z = 0 trên bàn in cho mép vỏ lòng gần bản lề
        translate([H1_X, H1_Y, -0.1])
        difference() {
            cylinder(r = KNUCKLE_R + 2.0, h = 0.6);
            cylinder(r1 = KNUCKLE_R - 0.5, r2 = KNUCKLE_R, h = 0.6);
        }
    }
}

// =============================================================================
// 3. QUAI GÔNG KẸP CỐ ĐỊNH LIỀN KHỐI (CLAMPING FRAME - ERGONOMIC TACTILE SNAP)
// =============================================================================
module clamping_frame() {
    union() {
        // A. TAI CHẶN DƯỚI & TAY ĐÒN XOAY (Z in [0, 2.0mm])
        hull() {
            translate([H2_X, H2_Y, 0]) cylinder(r = KNUCKLE2_R, h = 2.00);
            translate([18.45, 1.00, 0]) cube([1.70, 1.00, 2.00]);
        }
        
        // B. TAI CHẶN TRÊN & TAY ĐÒN XOAY (Z in [13.0, 15.0mm])
        hull() {
            translate([H2_X, H2_Y, 13.00]) cylinder(r = KNUCKLE2_R, h = 2.00);
            translate([18.45, 1.00, 13.00]) cube([1.70, 1.00, 2.00]);
        }
        
        // Vát côn tự đỡ 45 độ mặt dưới tai chặn trên H2 (Z = 13.0) chống sệ rớt sợi
        translate([H2_X, H2_Y, 12.40])
        cylinder(r1 = PIN2_R, r2 = PIN2_R + 0.60, h = 0.60);
        
        // C. CHỐT XOAY BẢN LỀ 2 ĐÚC LIỀN (phi 2.6 mm, Z = 0 đến 15.0 mm)
        translate([H2_X, H2_Y, 0]) cylinder(r = PIN2_R, h = L_CUFF);
        
        // D. THÂN QUAI KẸP ĐÀN HỒI (SPRING BEAM) + MẤU GÀI VÁT 45 ĐỘ + CẦN GẠT MỞ CÔNG THÁI HỌC
        linear_extrude(height = L_CUFF) {
            polygon([
                [18.45,  2.00],  // Đỉnh mặt trong thân quai (khe hở X = 0.25mm)
                [18.45, -3.40],  // Đáy mặt trong thân quai (khe hở Y = 0.20mm)
                [17.50, -3.40],  // Bắt đầu dốc đón vào ngàm (khe hở thoải mái)
                [16.75, -2.85],  // Đỉnh mấu khóa bắt đầu (nhô cao Y = -2.85mm, ăn sâu 0.35mm vào rãnh!)
                [16.35, -2.85],  // Đỉnh mấu khóa kết thúc (rộng 0.40mm)
                [15.75, -3.40],  // Vách thoát vát 45 độ lướt êm khi gạt mở (Y = -3.40mm)
                [15.10, -3.40],  // Đáy trong vòm ôm dưới ngàm
                [15.10, -4.70],  // Đáy ngoài vòm ngàm
                [18.45, -4.70],  // Đáy ngoài thân quai
                [19.50, -5.40],  // Gốc cần gạt mở ngón tay
                [22.00, -6.80],  // Đáy mũi cần gạt mở
                [22.80, -5.80],  // Đỉnh mũi cần gạt mở
                [20.15, -3.50],  // Lưng cần gạt chuyển tiếp vào sống quai kẹp
                [20.15,  2.00],  // Sống lưng thân quai kẹp dày 1.70mm đàn hồi hoàn hảo
                [18.45,  2.00]   // Đóng vòng CCW
            ]);
        }
    }
}
