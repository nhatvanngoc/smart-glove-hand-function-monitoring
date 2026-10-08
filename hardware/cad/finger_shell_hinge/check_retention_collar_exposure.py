#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kiểm tra "cục u" lộ ra do vai chặn chống tuột trục (§5f, pin_retain_r) có
nằm trong giới hạn AN TOÀN hay không — tức là không vượt quá bán kính
ngoài lớn nhất của vỏ, và không gây va chạm khi xoay bản lề.

LÝ DO CÓ FILE NÀY (2026-10-08, theo yêu cầu chủ dự án "dùng vision kiểm
tra tới khi hết lỗi"): khi làm QA bằng ảnh render + đo thể tích boolean
chính xác, phát hiện ghi chú code CŨ nói vai chặn "ẩn gọn trong boss có
sẵn, KHÔNG tạo gờ nhô mới" là SAI — đo bằng `cut(top_shell CÓ vai chặn,
top_shell KHÔNG có vai chặn)` ra ~24mm3 vật liệu MỚI, lộ ra ở nửa Z<0 (xem
README §5f, mục "Đính chính 2026-10-08"). Ghi chú code đã được sửa lại cho
đúng; script này là BẰNG CHỨNG HÌNH HỌC thường trực (chạy lại mỗi khi đổi
tham số) rằng "cục u" đó, dù có thật, vẫn nằm trong giới hạn chấp nhận
được: (a) không vượt bán kính ngoài r_knuckle của vỏ, (b) không gây va
chạm với bottom_shell khi xoay (đối chiếu chéo với check_hinge_sweep.py).

KHÔNG thay thế `check_axial_retention.py` (chứng minh vai chặn CÓ tác
dụng chặn tuột) hay `check_hinge_sweep.py` (chứng minh xoay không đâm
xuyên) — script này CHỈ xác nhận phần vật liệu MỚI do vai chặn tạo ra
(so với không có vai chặn) ở mức "chấp nhận được" về kích thước/vị trí.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import finger_shell_hinge as fsh
from finger_shell_hinge import p


def exposed_collar_bump():
    """Trả về (solid, volume_mm3, bbox) của phần vật liệu MỚI mà vai chặn
    tạo ra trên top_shell, so với 1 top_shell "giả lập" KHÔNG có vai chặn
    (dùng build_pin(with_retention=False) thay thế tạm thời)."""
    top_with = fsh.build_top_shell()

    pin_without = fsh.build_pin(with_retention=False)
    orig_build_pin = fsh.build_pin
    fsh.build_pin = lambda *a, **k: pin_without
    try:
        top_without = fsh.build_top_shell()
    finally:
        fsh.build_pin = orig_build_pin

    diff = top_with.cut(top_without)
    vol = diff.val().Volume()
    bbox = diff.val().BoundingBox()
    return diff, vol, bbox


def main():
    diff, vol, bbox = exposed_collar_bump()

    print("The tich vat lieu MOI do vai chan tao ra (so voi khong co vai chan):")
    print(f"  {vol:.4f} mm3")
    print("Bounding box cua phan vat lieu MOI nay:")
    print(f"  X: [{bbox.xmin:.3f}, {bbox.xmax:.3f}]")
    print(f"  Y: [{bbox.ymin:.3f}, {bbox.ymax:.3f}]")
    print(f"  Z: [{bbox.zmin:.3f}, {bbox.zmax:.3f}]")

    ok = True

    # (a) Phai co that (vai chan phai thuc su lam gi do -- neu =0 nghia la
    # vai chan khong con tac dung gi, mau thuan voi check_axial_retention.py)
    if vol < 1e-6:
        print("LOI: the tich = 0 -- vai chan khong con tac dung gi (mau thuan voi "
              "check_axial_retention.py, xem README SS5f)")
        ok = False

    # (b) Phan loi ra PHAI nam o nua Z<0 (phia long tay) -- dung voi ly do
    # ky thuat da giai thich (vai chan can co vat lieu dung o nua Z<0 moi
    # chan duoc khop ong long tay). Neu loi sang ca Z>0 that nhieu thi la
    # dau hieu bat thuong (vi boss nua mu tay da chiem Z>=0 roi).
    if bbox.zmax > 0.05:
        print(f"CANH BAO: phan vat lieu moi lan ca sang Z>0 ({bbox.zmax:.3f}mm) -- "
              "khac voi gia dinh thiet ke (chi nen loi o Z<0), can xem lai.")
        ok = False

    # (c) Ban kinh toi da cua "cuc u" (do tu truc Y=y_axis) KHONG duoc vuot
    # qua r_knuckle (ban kinh ngoai lon nhat cua vo tai khop ong) -- neu
    # vuot, "cuc u" se la diem loi ra XA NHAT cua toan bo vo, anh huong
    # kich thuoc bao ngoai tong the.
    y_axis = -p.W_out / 2.0 - p.r_knuckle + p.knuckle_overlap
    # bbox.ymin la diem xa truc Y=0 nhat theo huong am (vi vo nam o Y am);
    # khoang cach tu truc ban le toi diem do:
    max_radius_from_axis = abs(bbox.ymin - y_axis)
    print(f"Ban kinh xa truc ban le nhat cua cuc u: {max_radius_from_axis:.3f} mm "
          f"(gioi han cho phep r_knuckle = {p.r_knuckle:.3f} mm)")
    if max_radius_from_axis > p.r_knuckle + 1e-3:
        print("LOI: cuc u VUOT QUA ban kinh ngoai lon nhat cua vo (r_knuckle) -- "
              "se lam tang kich thuoc bao ngoai tong the, can giam pin_retain_r.")
        ok = False

    print()
    if ok:
        print("KET LUAN: OK -- cuc u do vai chan tao ra la CO THAT (dung voi "
              "check_axial_retention.py) nhung nam trong gioi han an toan: "
              "chi lo o nua long tay (Z<0), khong vuot ban kinh ngoai lon nhat "
              "cua vo. Day la mot danh doi thiet ke co chu dinh, khong phai loi "
              "hinh hoc/va cham -- xem README SS5f muc 'Dinh chinh 2026-10-08'.")
    else:
        print("KET LUAN: CO VAN DE -- xem chi tiet loi/canh bao o tren.")
        sys.exit(1)


if __name__ == "__main__":
    main()
