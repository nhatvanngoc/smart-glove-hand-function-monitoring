#!/usr/bin/env python3
"""Kiểm tra RIÊNG cho cơ chế ngàm cài (snap latch): móc (hook, ở tay đòn nửa
lòng tay) và ít nhất 1 nấc răng (ở khối ngàm nửa mu tay) có thực sự GIAO
NHAU về mặt hình học (chồng lấn cả 2 trục Y và Z) hay không.

TẠI SAO SCRIPT NÀY TỒN TẠI (bối cảnh — xem README §5c):
    2026-10-07, khi chủ dự án yêu cầu "check lại cơ chế chính xác", việc rà
    soát thủ công phát hiện: móc nằm ở Z=[11.2,12.8]mm trong khi CẢ HAI nấc
    răng nằm ở Z=[2.45,3.85]mm và [5.05,6.45]mm — lệch nhau 5-9mm, KHÔNG BAO
    GIỜ chạm được vào nhau. Ngàm cài NHƯ VẬY hoàn toàn không khóa được.

    Lỗi này đã tồn tại ở CẢ `finger_shell_hinge.py` VÀ `finger_shell_hinge.scad`
    (cùng 1 nguyên nhân gốc: công thức vị trí răng được tính ĐỘC LẬP với công
    thức vị trí móc, không có tham chiếu chéo, nên trôi lệch nhau qua một lần
    sửa trước đó) — vì vậy:
      - `cross_check.py` (so khớp 2 bản CAD VỚI NHAU) KHÔNG phát hiện được,
        vì lỗi giống hệt nhau ở cả 2 bản.
      - `check_connectivity.py` (đếm số mảnh rời) KHÔNG phát hiện được, vì
        răng và móc đều LÀ một phần liền của khối chính (không rời ra),
        chỉ đơn giản là không bao giờ chạm được NHAU khi lắp.

    Đây là một LỚP lỗi hoàn toàn khác: đúng kết nối (connectivity), đúng thể
    tích/bbox (cross-check), nhưng SAI chức năng cơ khí (2 chi tiết phải ăn
    khớp với nhau thì không ăn khớp). Script này bổ sung một phép kiểm tra
    THỨ BA, độc lập với 2 cái trên: kiểm tra TƯƠNG TÁC HÌNH HỌC giữa các chi
    tiết có vai trò ăn khớp với nhau, không chỉ kiểm tra bản thân từng chi
    tiết có liền khối/đúng kích thước hay không.

LƯU Ý QUAN TRỌNG: Script này CHỈ kiểm tra bounding-box 3D của từng "nấc răng"
và "móc" có giao nhau hay không — đây là điều kiện CẦN (nếu không giao nhau ở
trạng thái nghỉ thì chắc chắn không khóa được), nhưng KHÔNG PHẢI điều kiện ĐỦ
để khẳng định cơ chế lò xo/đàn hồi hoạt động đúng trong thực tế (lực cài, độ
đàn hồi của tay đòn PETG mỏng, góc nghiêng khi xoay qua bản lề... vẫn CHƯA
được kiểm chứng bằng mẫu in thật). Xem README §5c.

Chạy:
    python3 check_latch_engagement.py
"""
import sys

import cadquery as cq

import finger_shell_hinge as fsh

p = fsh.p


def bbox_of(shape):
    bb = shape.val().BoundingBox()
    return (bb.xmin, bb.xmax), (bb.ymin, bb.ymax), (bb.zmin, bb.zmax)


def overlap(range_a, range_b):
    lo = max(range_a[0], range_b[0])
    hi = min(range_a[1], range_b[1])
    return max(0.0, hi - lo)


def build_hook_only():
    """Trích riêng khối móc (hook) từ add_latch_arm(), không union vào shell,
    để đo bounding-box ĐỘC LẬP (không bị shell khác che/ảnh hưởng)."""
    y0 = p.W_out / 2.0
    x0, x1 = p.margin_x, p.L - p.margin_x
    w = x1 - x0
    xc = (x0 + x1) / 2.0
    r_hook = min(0.3, (p.arm_hook + p.arm_t) / 2.0 - 0.2, 1.6 / 2.0 - 0.2)
    hook = (
        cq.Workplane("XY")
        .box(w, p.arm_hook + p.arm_t, 1.6)
        .edges("|X")
        .fillet(r_hook)
        .translate((xc, y0 + p.catch_t + p.arm_t - p.arm_hook / 2.0 + 0.2, p.arm_h - 1.0))
    )
    return hook


def build_teeth_only():
    """Trích riêng từng nấc răng từ add_latch_catch(), không union vào shell."""
    y0 = p.W_out / 2.0
    x0, x1 = p.margin_x, p.L - p.margin_x
    w = x1 - x0
    xc = (x0 + x1) / 2.0
    hook_rest_z = p.arm_h - 1.0
    r_tooth = min(0.3, p.tooth_h - 0.1, 1.4 / 2.0 - 0.1)
    teeth = []
    for i in range(2):
        z_t = hook_rest_z - i * p.tooth_pitch
        tooth = (
            cq.Workplane("XY")
            .box(w, p.tooth_h * 2, 1.4)
            .edges("|X")
            .fillet(r_tooth)
            .translate((xc, y0 + p.catch_t - 0.3 + p.tooth_h * 0.4, z_t))
        )
        teeth.append(tooth)
    return teeth


def main():
    hook = build_hook_only()
    hx, hy, hz = bbox_of(hook)
    print("Moc (hook):  X=%.2f..%.2f  Y=%.2f..%.2f  Z=%.2f..%.2f" % (hx[0], hx[1], hy[0], hy[1], hz[0], hz[1]))

    teeth = build_teeth_only()
    any_engage = False
    for i, tooth in enumerate(teeth):
        tx, ty, tz = bbox_of(tooth)
        oy = overlap(hy, ty)
        oz = overlap(hz, tz)
        engages = oy > 0.05 and oz > 0.05
        any_engage = any_engage or engages
        status = "AN KHOP" if engages else "khong giao nhau"
        print(
            "Nac rang %d: X=%.2f..%.2f  Y=%.2f..%.2f  Z=%.2f..%.2f"
            "  | chong lan voi moc: Y=%.2fmm Z=%.2fmm -> %s"
            % (i, tx[0], tx[1], ty[0], ty[1], tz[0], tz[1], oy, oz, status)
        )

    print()
    if any_engage:
        print("KET LUAN: OK -- moc va it nhat 1 nac rang CO giao nhau hinh hoc"
              " (dieu kien CAN de ngam cai khoa duoc). CHUA kiem chung bang"
              " mau in that (luc cai, do dan hoi) -- xem README SS5c.")
        return 0
    else:
        print("KET LUAN: LOI -- moc KHONG giao voi bat ky nac rang nao."
              " Ngam cai se KHONG the khoa duoc. Can sua lai vi tri"
              " tooth_z / hook_rest_z trong finger_shell_hinge.py va"
              " finger_shell_hinge.scad cho khop nhau.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
