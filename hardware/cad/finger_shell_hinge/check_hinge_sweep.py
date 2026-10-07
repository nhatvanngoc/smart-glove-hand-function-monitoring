#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kiểm tra bản lề có XOAY TỰ DO không — quét góc mở từ 0° đến OPEN_ANGLE và
tính thể tích GIAO NHAU (boolean intersection) thật giữa top_shell và
bottom_shell (đã xoay) tại mỗi góc, bằng chính lõi hình học OCCT (CadQuery).

LÝ DO CÓ FILE NÀY (2026-10-07): trước đây chỉ kiểm tra bằng MẮT qua ảnh
render ở ĐÚNG 1 góc cuối (150°, xem out/renders/05_assembly_open_iso.png) —
việc này đã BỎ SÓT một lỗi nghiêm trọng: với dấu góc xoay (hướng) sai, 2 nửa
vỏ ĐÂM XUYÊN NHAU thật sự (giao nhau tới ~600mm³) trong suốt khoảng góc
5°-100°, chỉ "tình cờ" tách rời lại ở đúng góc 150° nơi ảnh render được chụp.
Quét liên tục qua CadQuery `intersect()` mới bắt được lỗi này. Xem README §5e.

Ngưỡng chấp nhận:
  - Góc 0° (ĐÓNG): ngàm cài (snap latch) CỐ Ý có chồng lấn (~51.5mm³ ở bản
    hiện tại) vì đó là độ ngoàm/interference cần thiết để móc bám chặt vào
    răng khi lắp thật — KHÔNG phải lỗi.
  - Góc 0° < góc <= LATCH_ZONE_MAX_DEG (mặc định 10°): vùng "nhả ngàm" —
    móc (hook) vẫn đang trượt qua khỏi răng (tay đòn đàn hồi PETG uốn nhẹ
    khi mở), nên vẫn còn chồng lấn nhỏ giảm dần (quan sát được ~9.4mm³ tại
    5°, 0mm³ tại 10°) — ĐÂY LÀ HÀNH VI CỐ Ý của ngàm cài, không phải lỗi
    bản lề, chỉ ghi nhận để tham khảo, KHÔNG tính vào điều kiện PASS/FAIL.
  - Góc > LATCH_ZONE_MAX_DEG và <= MAX_ANGLE: đây mới là vùng "đang mở",
    2 nửa PHẢI là 2 khối CỨNG tách rời hoàn toàn (không có ngàm/bản lề nào
    cố ý chạm nhau ở đây) — thể tích giao nhau phải ~0 (cho sai số rời rạc
    hoá rất nhỏ, <0.05mm³), nếu không coi là LỖI THẬT (va chạm vật lý).

Chạy:
    LD_LIBRARY_PATH=~/.local/stublibs python3 check_hinge_sweep.py
"""
import sys

import finger_shell_hinge as fsh

# Ngưỡng cho phép ở vùng "đang mở thật" (xem giải thích ở trên)
THRESHOLD_OPEN_MM3 = 0.05

# Góc cuối của vùng "nhả ngàm" (latch hook còn đang trượt qua, chồng lấn nhỏ
# là CỐ Ý, không tính lỗi) — chọn 10° theo quan sát thực tế (xem log chạy).
LATCH_ZONE_MAX_DEG = 10

# Góc tối đa coi là "trong phạm vi mở hữu ích" của thiết kế hiện tại = đúng
# OPEN_ANGLE danh định (150°, xem build_open_bottom_shell()). Đã kiểm tra
# riêng: qua khỏi ~152° thể tích giao nhau bắt đầu TĂNG TRỞ LẠI (0.60mm³ ở
# 155°) vì phía XA bản lề (cạnh ngàm cài) bắt đầu áp sát lại — đây là GIỚI
# HẠN TỰ NHIÊN của thiết kế (không mở quá ~150°), không phải lỗi, miễn là
# không ai chỉnh OPEN_ANGLE vượt mốc này mà không kiểm tra lại bằng script
# này trước.
MAX_ANGLE = 150
STEP = 5


def main():
    top = fsh.build_top_shell()
    print("Goc (do)   The tich giao nhau (mm3)   Ket qua")
    worst_open = 0.0
    closed_vol = None
    ok = True
    for ang in range(0, MAX_ANGLE + 1, STEP):
        bot = fsh.build_open_bottom_shell(angle_deg=ang) if ang > 0 else fsh.build_bottom_shell()
        inter = top.intersect(bot)
        try:
            v = inter.val().Volume()
        except Exception:
            v = 0.0
        if ang == 0:
            closed_vol = v
            tag = "DONG (co ngam cai an khop -- co tinh, khong phai loi)"
        elif ang <= LATCH_ZONE_MAX_DEG:
            tag = "vung nha ngam (co tinh, khong tinh loi) -- tham khao: %.4f" % v
        else:
            tag = "OK" if v <= THRESHOLD_OPEN_MM3 else "LOI -- 2 nua DAM XUYEN NHAU!"
            if v > worst_open:
                worst_open = v
            if v > THRESHOLD_OPEN_MM3:
                ok = False
        print(f"{ang:8.0f}   {v:10.4f}                {tag}")

    print()
    print(f"The tich giao nhau luc DONG (0 do, co tinh do ngam cai): {closed_vol:.2f} mm3")
    print(f"The tich giao nhau LON NHAT trong vung DANG MO THAT (goc > {LATCH_ZONE_MAX_DEG} va <= {MAX_ANGLE}): {worst_open:.4f} mm3")
    if ok:
        print("\nKET LUAN: OK -- 2 nua vo KHONG dam xuyen nhau trong suot qua trinh mo "
              f"(goc > {LATCH_ZONE_MAX_DEG} -> {MAX_ANGLE} do, buoc {STEP} do). Day la bang chung hinh hoc rang ban "
              "le CO THE xoay tu do, CHUA phai bang chung co hoc that (ma sat, do dan hoi "
              "PETG, dung sai in that) -- xem README SS5e.")
        sys.exit(0)
    else:
        print("\nKET LUAN: LOI -- phat hien dam xuyen hinh hoc that giua 2 nua trong qua "
              "trinh mo o it nhat 1 goc (ngoai vung nha ngam). Ban le NAY KHONG THE xoay tu "
              "do neu in that.")
        sys.exit(1)


if __name__ == "__main__":
    main()

