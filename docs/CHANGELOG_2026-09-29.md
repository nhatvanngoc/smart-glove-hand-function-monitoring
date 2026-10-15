# NHẬT KÝ ĐỒNG BỘ HỒ SƠ NGHIÊN CỨU — 2026-09-29

> **Phạm vi:** mọi thay đổi / bổ sung / loại bỏ từ khi hoàn thiện bản dự thảo (báo cáo mới nhất) tới nay.
> **Ký hiệu trạng thái:** [Đã cập nhật repo] = đã vào repo · [Chờ cập nhật bản Word] = nhóm đang cập nhật bản Word ·
> [Nhóm đang thực hiện] = nhóm đang đo/mua/thu thập số liệu · [giữ] = quyết định giữ nguyên.
> Tham chiếu: checklist M-01..M-27 (`research/notebook/2026-09-29_measurability_M-checklist.md`),
> outline v3.0 (`docs/OUTLINE_BAOCAO_VISEFD.md`).

---

## I. [Cập nhật] THAY ĐỔI (15 mục)

| # | Nội dung thống nhất | Trạng thái |
|---|---|---|
| T-01 | Tần số quét: 50 Hz → **20 Hz danh định** (M-02) | [Đã cập nhật repo] outline v3.0 A.3/C.3 · [Chờ cập nhật bản Word] sửa §8.1/Hình 7 |
| T-02 | Định nghĩa kênh: "12 kênh vi sai" → **kênh = phần tử đơn; 12 + 1 chuẩn = 13 đầu vào; 6 cặp vi sai** (M-04) | [Đã cập nhật repo] B.1/B.4 · [Chờ cập nhật bản Word] sửa §5.2/§7.1 |
| T-03 | "INA128 / INA333" → **INA333 duy nhất** (M-16) | [Đã cập nhật repo] B.1/B.3 · [Chờ cập nhật bản Word] sửa Hình 9/10 |
| T-04 | Vex/G/S: số cũ chưa công nhận → **đo R(F) thật rồi tính lại toàn chuỗi** (M-01/M-17) | [Nhóm đang thực hiện] đo DMM + quả cân |
| T-05 | Số §8.2 "qua thực nghiệm" → **dán "minh họa" hoặc ghi xuất xứ máy/người/ngày/N/log** (M-06/M-07) | [Chờ cập nhật bản Word] §8.2 + caption Hình 4/5/13 |
| T-06 | Hằng số AAN (1,2 s / 5 N / EI_th) → **"giá trị đặt trước, chờ kiểm định trên giàn"** (M-09) | [Chờ cập nhật bản Word] §10.2 |
| T-07 | M6 "phổ V_base" → **bản thu nhỏ: cửa sổ V_base + 20–30 lần tháo/đeo, giữ target 80%** | [Đã cập nhật repo] A.3/C.2 · [Chờ cập nhật bản Word] §5.2-M6/§11.2 |
| T-08 | AI "xử lý dữ liệu" → **dự đoán + cảnh báo, thà báo nhầm còn hơn bỏ sót (recall-oriented), KTV duyệt** → chốt cuối: **luật thường gánh chính + 1 thực nghiệm đối chứng rules-vs-ML** (không phải AI trang trí) | [Đã cập nhật repo] B.5/C.5 · [Chờ cập nhật bản Word] sửa §9.1/Hình 7/10 |
| T-09 | Nhiệt độ: **giữ nhưng thu hẹp** — log T/RH mọi phiên + 1 đồ thị trôi-vs-T + hệ số r từ dữ liệu C1.8, không chương riêng | [Đã cập nhật repo] B.4 · [Chờ cập nhật bản Word] sửa §8.3/Hình 6 |
| T-10 | M6: ~~bỏ~~ → **RÚT LẠI, GIỮ** (quyết định bỏ đã hủy) | [Đã cập nhật repo] giữ 2 vòng lặp · bản Drive giữ nguyên M6 |
| T-11 | Ngân sách: "<1,5M cả hệ thống" → **tách "thiết bị đeo <1,5M" vs "trạm dùng chung"** (M-21) | [Đã cập nhật repo] B.8 · [Chờ cập nhật bản Word] sửa §5.1/Tóm tắt |
| T-12 | Dẫn động giàn: cáp Bowden → **khớp cứng (rig/phantom only)**; **1 servo/ngón, MCP+PIP liên động**; kiểm định xong 1 ngón trước | [Đã cập nhật repo] B.3 · [Nhóm đang thực hiện] ngân sách mô-men + test nhiệt (M-19) |
| T-13 | DMM chính = **FNIRSI 2C23T theo datasheet** (10k count, 0,5%); DMM rời = máy phụ, **không tra model** (DEC-INST-001) | [Đã cập nhật repo] sổ tay L1–L6/PB-2 |
| T-14 | Orange Pi 5 Pro = **trạm dùng chung (trường đã có, 0 đồng)**; đã test INT8 + xử lý ảnh OK (chờ 5 số để viết claim — M-08) | [Đã cập nhật repo] B.1/B.3 · [Nhóm đang thực hiện] gửi model/input/latency/RKNN/log |
| T-15 | E2E vận hành theo **trần <10M, chỉ ghi sổ tay, không vào báo cáo** (DEC-BUDGET-002) | [Đã cập nhật repo] notebook §5 (~5,5M) |

---

## II. + BỔ SUNG (12 mục)

| # | Nội dung thống nhất | Trạng thái |
|---|---|---|
| B-01 | **Phân loại sự kiện E1–E4** (spike/rung/tuột/bão hòa, định nghĩa ở mức tín hiệu) + **timeline sự kiện + báo cáo tuần PDF** + vòng lặp **KTV ngồi nhà duyệt** (AI gắn cờ, người diễn giải — không nói "AI phát hiện co giật") | [Đã cập nhật repo] B.5/B.7/C.5 · [Chờ cập nhật bản Word] thêm vào §9/§11 |
| B-02 | **Camera đối chứng góc** (ArUco, P1) + **thước đo góc chuẩn chính** (P0) cho GAP (M-13) | [Đã cập nhật repo] B.6 · [Nhóm đang thực hiện] mua thước (~50k) |
| B-03 | **Thực nghiệm đối chứng rules-vs-ML** duy nhất (P1): baseline luật ngưỡng → ML chỉ giữ nếu thắng có bằng chứng | [Đã cập nhật repo] B.5/C.5 |
| B-04 | **Công thức EI tường minh** (công thức + cửa sổ + chuẩn hóa + ngưỡng) viết trước khi thu dữ liệu (M-25) | [Nhóm đang thực hiện] viết |
| B-05 | **Người đeo + an toàn**: ghi rõ ai đeo (kể cả thành viên nhóm), khi nào, biện pháp an toàn (M-26) | [Nhóm đang thực hiện] viết → [Chờ cập nhật bản Word] §7.2 |
| B-06 | **Đồ nghề chốt + phương pháp**: C1.1 tách 3 chân (ADS1115 log + scope chứng kiến + shorted-input); chuẩn tĩnh = quả cân; load cell chỉ động + đối chứng | [Đã cập nhật repo] A.6/notebook §2 |
| B-07 | **3 bẫy thao tác 2C23T**: DMM manual < 0,7 V · gen 100 Ω + dùng square/DC · BNC nhẹ tay | [Đã cập nhật repo] notebook L2/PB-2 |
| B-08 | **Shopping P0**: HX711 (đầu tiên) · ADS1115/INA333 chính hãng · SHT30 · cân túi/quả cân · thước đo góc · ẩm-nhiệt kế · lò xo · vít · PETG | [Nhóm đang thực hiện] mua |
| B-09 | **BOM E2E ~5,5M** (găng ~1,2M + giàn-đo ~3,2M + dự phòng ~1M) — sổ tay only | [Đã cập nhật repo] notebook §5 |
| B-10 | **B.9 bảy nhóm câu cấm** + ma trận kiểm định C + outline v3.0 + A1/A2/A3/A4/A6 viết lại | [Đã cập nhật repo] |
| B-11 | Điều kiện bỏ phanh: **nghiệm thu vít me tự hãm + 1 khóa cổ thủ công** (M-20) | [Nhóm đang thực hiện] nghiệm thu |
| B-12 | Sửa cite: 1,5M "ước tính của nhóm" (M-22) · 80% → Cochrane/Langhorne, 85% tìm nguồn hoặc cắt (M-23) · *Engineering* 2024, *Device* 2024, gỡ cite không DOI (M-24) | [Đã cập nhật repo] A.1 + refs · [Chờ cập nhật bản Word] Tóm tắt/§3/TLTK |

---

## III. - LOẠI BỎ (14 mục)

| # | Nội dung thống nhất loại bỏ | Trạng thái |
|---|---|---|
| R-01 | Claim **"suy luận INT8 < 15 ms"** (chưa đo — chỉ quay lại bằng benchmark thật) (M-08) | [Đã cập nhật repo] B.5 · [Chờ cập nhật bản Word] xóa §9.1/Hình 7 |
| R-02 | **Phân loại MAS / chẩn đoán / AI-clinical** — từ chối Nâng cấp 1 (M-15) | [không vào báo cáo] |
| R-03 | **AAN trên người / vòng kín lực lên người** — từ chối Nâng cấp 2; AAN chỉ trên phantom (M-12/M-15) | [Đã cập nhật repo] A.4/B.3 · [Chờ cập nhật bản Word] viết lại §10 |
| R-04 | Chữ **"triệt tiêu hoàn toàn / triệt để"** → "giảm + định lượng phần dư" (M-10) | [Đã cập nhật repo] B.9 · [Chờ cập nhật bản Word] §8.3/§12.1 |
| R-05 | **Góc "quy đổi từ tín hiệu"** ADC→độ (M-13) | [Chờ cập nhật bản Word] sửa Hình 4 |
| R-06 | **Suy nguyên nhân GAP** ("do yếu cơ/co cứng") (M-14) | [Chờ cập nhật bản Word] sửa §8.2 |
| R-07 | **"RAL giảm = bệnh cải thiện"** → "đặc trưng giao thức kiểm định" (M-11) | [Chờ cập nhật bản Word] sửa §10.3 |
| R-08 | Ngôn ngữ AAN trên người ("tay người bệnh", "bảo vệ khớp") (M-12) | [Chờ cập nhật bản Word] sửa §10.2/Hình 12 |
| R-09 | **200 Hz đa kênh** + 50 Hz danh định (M-02/M-03) | [Đã cập nhật repo] · [Chờ cập nhật bản Word] |
| R-10 | **ML suy luận gập/duỗi trên NPU** — dấu vi sai đã làm việc đó | [Đã cập nhật repo] B.5 · [Chờ cập nhật bản Word] sửa Hình 10 |
| R-11 | Mục tiêu **3D/EKF/IMU-từng-đốt** khỏi giai đoạn này → hướng phát triển | [Đã cập nhật repo] B.6/C.8 · bản Drive §12.2 giữ nguyên |
| R-12 | **Chương "ảnh hưởng nhiệt độ" riêng** (đã thu hẹp ở T-09) | [Chờ cập nhật bản Word] |
| R-13 | **[17] dạng "khảo sát bệnh viện"** → tham khảo ẩn danh trên giấy (M-24) | [Đã cập nhật repo] A.5 · [Chờ cập nhật bản Word] sửa TLTK [17] |
| R-14 | §12 **"chế tạo thành công… đạt trọn vẹn"** (0 số liệu) → hạ về đúng mức (M-05) | [Chờ cập nhật bản Word] viết lại §12.1 |

**Đã bỏ khỏi danh sách mua:** DMM spare (~500k) — 2 DMM hiện tại đủ · Tra model DMM rời — không làm.

---

## IV. CÁC HẠNG MỤC NHÓM CẦN HOÀN THIỆN (gom từ các [Đang chờ] — 8 việc)

1. Đo R(F) thật (DMM + quả cân) → trả lời M-01/M-17 (Vex, G, S, SNR).
2. Viết công thức EI (M-25) + chốt 9 ngưỡng `protocols/08` §7 trước khi đo.
3. Viết mục người đeo + an toàn (M-26).
4. Gửi 5 số INT8 (model/input/latency/RKNN/log) (M-08).
5. Shopping P0 (B-08) — HX711 trước tiên.
6. Ngân sách mô-men + test nhiệt servo (M-19) · nghiệm thu vít me + khóa cổ (M-20).
7. Sửa bản Drive theo các mục [Chờ cập nhật bản Word] (15 chỗ).
8. Xác nhận Pi bản RAM mấy GB + nguồn/thẻ (cho đủ hồ sơ).
