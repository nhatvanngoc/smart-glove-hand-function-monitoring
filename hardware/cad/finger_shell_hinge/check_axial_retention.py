#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kiểm tra bản lề có DỄ BỊ TUỘT RA NGOÀI theo chiều DỌC TRỤC hay không — quét
độ dịch chuyển (translate) dọc theo trục bản lề (X) từ 0 đến một khoảng đủ
xa để nửa lòng tay (bottom_shell) tuột hẳn khỏi trục, và tính thể tích GIAO
NHAU (boolean intersection) thật giữa 2 khớp ống của bottom_shell và trục
(pin) tại mỗi bước dịch, bằng chính lõi hình học OCCT (CadQuery).

LÝ DO CÓ FILE NÀY (2026-10-08, theo yêu cầu chủ dự án "đảm bảo bản lề...
không dễ rơi ra ngoài"): `check_hinge_sweep.py` (2026-10-07) chỉ quét GÓC
XOAY quanh trục, KHÔNG quét chuyển vị DỌC TRỤC — nên đã bỏ sót 1 lỗi thiết
kế thật: trục chốt cũ (trước bản sửa ngày 2026-10-08) là hình trụ bán kính
ĐỀU suốt chiều dài, không có vai/mũ nào lớn hơn lỗ khớp ống của nửa lòng
tay -> KHÔNG CÓ GÌ ngăn nửa lòng tay trượt dọc trục và tuột hẳn ra khỏi
trục (xem README §5f). Đã sửa bằng cách thêm 2 "vai chặn" hình trụ đồng
trục (collar, bán kính pin_retain_r=2.2mm > r_pin=1.3mm) ẩn trong khối vật
liệu có sẵn ở giữa đoạn khớp ống ĐẦU và CUỐI thuộc nửa mu tay. Script này
CHỨNG MINH bằng hình học rằng vai chặn đó THẬT SỰ cản đường trượt (không
chỉ "trên giấy").

Cách kiểm tra: chỉ lấy RIÊNG `build_pin()` (trục, có vai chặn) và RIÊNG
`build_bottom_shell()` (nửa lòng tay, 2 khớp ống BÁM CỨNG vào nhau vì là 1
khối liền) — KHÔNG lấy cả top_shell (vỏ ngoài) để tách bạch rõ: phép thử
này chỉ đo hiệu quả của RIÊNG vai chặn, không trộn lẫn với va chạm ở thành
vỏ (đã có check_hinge_sweep.py lo phần đó).

Ngưỡng diễn giải:
  - Tại độ dịch 0 (vị trí lắp ráp đúng): giao nhau phải ~0 (khe hở in-tại-
    chỗ bình thường, không phải lỗi).
  - Càng dịch xa 0 (2 hướng +X/-X), nửa lòng tay PHẢI đâm xuyên thật vào ít
    nhất 1 vai chặn trước khi có thể đi xa hơn tới mép trục — tức là PHẢI
    tồn tại ít nhất 1 bước dịch có giao nhau > BLOCK_THRESHOLD_MM3 trong
    khoảng [0, ESCAPE_DISTANCE_MM] mỗi hướng. Nếu KHÔNG, nghĩa là nửa lòng
    tay có thể trượt thẳng ra ngoài mà không chạm gì -> LỖI THIẾT KẾ THẬT.
  - Việc giao nhau quay về ~0 ở độ dịch RẤT LỚN (vượt xa ESCAPE_DISTANCE_MM)
    là bình thường — lúc đó nửa lòng tay đã tách rời khỏi trục hoàn toàn
    (không còn gì để chạm), không phải bằng chứng "thoát được vai chặn mà
    không chạm" (xem chi tiết luồng dịch chuyển trong README §5f).

Lưu ý: đây là bằng chứng HÌNH HỌC (bắt buộc phải đâm xuyên vật liệu mới qua
được), CHƯA phải bằng chứng cơ học thật (lực cần để kéo tuột, độ bền PETG
tại vùng vai chặn, dung sai in thật) — xem README §5f và AGENTS.md.

Chạy:
    LD_LIBRARY_PATH=~/.local/stublibs python3 check_axial_retention.py
"""
import sys

import finger_shell_hinge as fsh

# Thể tích giao nhau tối thiểu để coi là "va chạm thật" (không phải sai số
# rời rạc hoá nhỏ của lưới OCCT).
BLOCK_THRESHOLD_MM3 = 0.5

# Quét dịch chuyển dọc trục X từ 0 đến khoảng này (mm) mỗi hướng — đủ xa để
# nửa lòng tay tuột hẳn khỏi 2 đầu trục (pin dài 25mm, margin mỗi đầu ~5mm).
SCAN_RANGE_MM = 25.0
STEP_MM = 1.0


def scan_direction(bot, pin, sign):
    """Quét 1 hướng (sign=+1 hoặc -1), trả về (max_vol, list các (tx, vol))."""
    rows = []
    n = int(SCAN_RANGE_MM / STEP_MM)
    for i in range(n + 1):
        tx = sign * i * STEP_MM
        bot_t = bot.translate((tx, 0, 0))
        inter = bot_t.intersect(pin)
        try:
            v = inter.val().Volume()
        except Exception:
            v = 0.0
        rows.append((tx, v))
    return rows


def main():
    bot = fsh.build_bottom_shell()

    print("=== Bản lề CÓ vai chặn (thiết kế đã sửa, 2026-10-08) ===")
    pin_fixed = fsh.build_pin(with_retention=True)
    rows_pos = scan_direction(bot, pin_fixed, +1)
    rows_neg = scan_direction(bot, pin_fixed, -1)

    print(f"{'Dich chuyen X (mm)':<22}{'The tich giao nhau (mm3)':<28}Ghi chu")
    all_rows = sorted(rows_neg + rows_pos, key=lambda r: r[0])
    for tx, v in all_rows:
        tag = "cham vai chan / truc" if v > BLOCK_THRESHOLD_MM3 else ""
        print(f"{tx:<22.1f}{v:<28.4f}{tag}")

    max_pos = max(v for _, v in rows_pos if _ != 0) if len(rows_pos) > 1 else 0.0
    max_neg = max(v for _, v in rows_neg if _ != 0) if len(rows_neg) > 1 else 0.0
    blocked_pos = any(v > BLOCK_THRESHOLD_MM3 for tx, v in rows_pos)
    blocked_neg = any(v > BLOCK_THRESHOLD_MM3 for tx, v in rows_neg)

    print()
    print(f"Giao nhau LON NHAT khi truot ve huong +X: {max_pos:.2f} mm3 "
          f"({'CO chan' if blocked_pos else 'KHONG chan gi ca -- LOI'})")
    print(f"Giao nhau LON NHAT khi truot ve huong -X: {max_neg:.2f} mm3 "
          f"({'CO chan' if blocked_neg else 'KHONG chan gi ca -- LOI'})")

    print()
    print("=== Doi chung: ban le KHONG co vai chan (thiet ke CU, truoc 2026-10-08) ===")
    pin_old = fsh.build_pin(with_retention=False)
    rows_pos_old = scan_direction(bot, pin_old, +1)
    rows_neg_old = scan_direction(bot, pin_old, -1)
    max_pos_old = max((v for tx, v in rows_pos_old), default=0.0)
    max_neg_old = max((v for tx, v in rows_neg_old), default=0.0)
    print(f"Giao nhau LON NHAT khi truot ve huong +X (truc CU, khong vai chan): {max_pos_old:.4f} mm3")
    print(f"Giao nhau LON NHAT khi truot ve huong -X (truc CU, khong vai chan): {max_neg_old:.4f} mm3")
    print("-> Neu ca 2 gia tri nay ~0, chung minh truc CU khong he can tro gi khi "
          "nua long tay truot doc truc -- DUNG LA CO THE TUOT RA NGOAI DE DANG "
          "(day la ly do phai sua).")

    ok = blocked_pos and blocked_neg
    print()
    if ok:
        print("KET LUAN: OK -- vai chan CHAN DUOC duong truot doc truc o CA 2 huong "
              "(phai dam xuyen vat lieu that moi di qua duoc) -- day la bang chung hinh "
              "hoc rang ban le KHONG DE tuot ra ngoai theo chieu doc truc, CHUA phai bang "
              "chung co hoc that (luc keo, do ben PETG, dung sai in that) -- xem README SS5f.")
        sys.exit(0)
    else:
        print("KET LUAN: LOI -- phat hien it nhat 1 huong truot doc truc KHONG bi can tro "
              "gi -- nua long tay co the tuot thang ra ngoai. PHAI sua truoc khi in.")
        sys.exit(1)


if __name__ == "__main__":
    main()
