# BẢN CẬP NHẬT ĐẦY ĐỦ THEO Ý OWNER — 2026-09-29

> **Phạm vi:** mọi thay đổi / bổ sung / loại bỏ do owner nhắn từ khi gửi bản Drive (báo cáo mới nhất) tới nay.
> **Ký hiệu trạng thái:** [repo ✅] = đã vào repo · [Drive ⏳] = chờ bạn sửa trên bản Word ·
> [bạn ⏳] = chờ bạn làm/mua/gửi số · [giữ] = quyết định giữ nguyên.
> Tham chiếu: checklist M-01..M-27 (`research/notebook/2026-09-29_measurability_M-checklist.md`),
> outline v3.0 (`docs/OUTLINE_BAOCAO_VISEFD.md`).

---

## I. 🔄 THAY ĐỔI (15 mục)

| # | Nội dung bạn chốt | Trạng thái |
|---|---|---|
| T-01 | Tần số quét: 50 Hz → **20 Hz danh định** (M-02) | [repo ✅] outline v3.0 A.3/C.3 · [Drive ⏳] sửa §8.1/Hình 7 |
| T-02 | Định nghĩa kênh: "12 kênh vi sai" → **kênh = phần tử đơn; 12 + 1 chuẩn = 13 đầu vào; 6 cặp vi sai** (M-04) | [repo ✅] B.1/B.4 · [Drive ⏳] sửa §5.2/§7.1 |
| T-03 | "INA128 / INA333" → **INA333 duy nhất** (M-16) | [repo ✅] B.1/B.3 · [Drive ⏳] sửa Hình 9/10 |
| T-04 | Vex/G/S: số cũ chưa công nhận → **đo R(F) thật rồi tính lại toàn chuỗi** (M-01/M-17) | [bạn ⏳] đo DMM + quả cân |
| T-05 | Số §8.2 "qua thực nghiệm" → **dán "minh họa" hoặc ghi xuất xứ máy/người/ngày/N/log** (M-06/M-07) | [Drive ⏳] §8.2 + caption Hình 4/5/13 |
| T-06 | Hằng số AAN (1,2 s / 5 N / EI_th) → **"giá trị đặt trước, chờ kiểm định trên giàn"** (M-09) | [Drive ⏳] §10.2 |
| T-07 | M6 "phổ V_base" → **bản thu nhỏ: cửa sổ V_base + 20–30 lần tháo/đeo, giữ target 80%** | [repo ✅] A.3/C.2 · [Drive ⏳] §5.2-M6/§11.2 |
| T-08 | AI "xử lý dữ liệu" → **dự đoán + cảnh báo, thà báo nhầm còn hơn bỏ sót (recall-oriented), KTV duyệt** → chốt cuối: **luật thường gánh chính + 1 thực nghiệm đối chứng rules-vs-ML** (không phải AI trang trí) | [repo ✅] B.5/C.5 · [Drive ⏳] sửa §9.1/Hình 7/10 |
| T-09 | Nhiệt độ: **giữ nhưng thu hẹp** — log T/RH mọi phiên + 1 đồ thị trôi-vs-T + hệ số r từ dữ liệu C1.8, không chương riêng | [repo ✅] B.4 · [Drive ⏳] sửa §8.3/Hình 6 |
| T-10 | M6: ~~bỏ~~ → **RÚT LẠI, GIỮ** (quyết định bỏ đã hủy) | [repo ✅] giữ 2 vòng lặp · bản Drive giữ nguyên M6 |
| T-11 | Ngân sách: "<1,5M cả hệ thống" → **tách "thiết bị đeo <1,5M" vs "trạm dùng chung"** (M-21) | [repo ✅] B.8 · [Drive ⏳] sửa §5.1/Tóm tắt |
| T-12 | Dẫn động giàn: cáp Bowden → **khớp cứng (rig/phantom only)**; **1 servo/ngón, MCP+PIP liên động**; kiểm định xong 1 ngón trước | [repo ✅] B.3 · [bạn ⏳] ngân sách mô-men + test nhiệt (M-19) |
| T-13 | DMM chính = **FNIRSI 2C23T theo datasheet** (10k count, 0,5%); DMM rời = máy phụ, **không tra model** (DEC-INST-001) | [repo ✅] sổ tay L1–L6/PB-2 |
| T-14 | Orange Pi 5 Pro = **trạm dùng chung (trường đã có, 0 đồng)**; đã test INT8 + xử lý ảnh OK (chờ 5 số để viết claim — M-08) | [repo ✅] B.1/B.3 · [bạn ⏳] gửi model/input/latency/RKNN/log |
| T-15 | E2E vận hành theo **trần <10M, chỉ ghi sổ tay, không vào báo cáo** (DEC-BUDGET-002) | [repo ✅] notebook §5 (~5,5M) |

---

## II. ➕ BỔ SUNG (12 mục)

| # | Nội dung bạn chốt | Trạng thái |
|---|---|---|
| B-01 | **Phân loại sự kiện E1–E4** (spike/rung/tuột/bão hòa, định nghĩa ở mức tín hiệu) + **timeline sự kiện + báo cáo tuần PDF** + vòng lặp **KTV ngồi nhà duyệt** (AI gắn cờ, người diễn giải — không nói "AI phát hiện co giật") | [repo ✅] B.5/B.7/C.5 · [Drive ⏳] thêm vào §9/§11 |
| B-02 | **Camera đối chứng góc** (ArUco, P1) + **thước đo góc chuẩn chính** (P0) cho GAP (M-13) | [repo ✅] B.6 · [bạn ⏳] mua thước (~50k) |
| B-03 | **Thực nghiệm đối chứng rules-vs-ML** duy nhất (P1): baseline luật ngưỡng → ML chỉ giữ nếu thắng có bằng chứng | [repo ✅] B.5/C.5 |
| B-04 | **Công thức EI tường minh** (công thức + cửa sổ + chuẩn hóa + ngưỡng) viết trước khi thu dữ liệu (M-25) | [bạn ⏳] viết |
| B-05 | **Người đeo + an toàn**: ghi rõ ai đeo (kể cả thành viên nhóm), khi nào, biện pháp an toàn (M-26) | [bạn ⏳] viết → [Drive ⏳] §7.2 |
| B-06 | **Đồ nghề chốt + phương pháp**: C1.1 tách 3 chân (ADS1115 log + scope chứng kiến + shorted-input); chuẩn tĩnh = quả cân; load cell chỉ động + đối chứng | [repo ✅] A.6/notebook §2 |
| B-07 | **3 bẫy thao tác 2C23T**: DMM manual < 0,7 V · gen 100 Ω + dùng square/DC · BNC nhẹ tay | [repo ✅] notebook L2/PB-2 |
| B-08 | **Shopping P0**: HX711 (đầu tiên) · ADS1115/INA333 chính hãng · SHT30 · cân túi/quả cân · thước đo góc · ẩm-nhiệt kế · lò xo · vít · PETG | [bạn ⏳] mua |
| B-09 | **BOM E2E ~5,5M** (găng ~1,2M + giàn-đo ~3,2M + dự phòng ~1M) — sổ tay only | [repo ✅] notebook §5 |
| B-10 | **B.9 bảy nhóm câu cấm** + ma trận kiểm định C + outline v3.0 + A1/A2/A3/A4/A6 viết lại | [repo ✅] |
| B-11 | Điều kiện bỏ phanh: **nghiệm thu vít me tự hãm + 1 khóa cổ thủ công** (M-20) | [bạn ⏳] nghiệm thu |
| B-12 | Sửa cite: 1,5M "ước tính của nhóm" (M-22) · 80% → Cochrane/Langhorne, 85% tìm nguồn hoặc cắt (M-23) · *Engineering* 2024, *Device* 2024, gỡ cite không DOI (M-24) | [repo ✅] A.1 + refs · [Drive ⏳] Tóm tắt/§3/TLTK |

---

## III. ➖ LOẠI BỎ (14 mục)

| # | Nội dung bạn chốt bỏ | Trạng thái |
|---|---|---|
| R-01 | Claim **"suy luận INT8 < 15 ms"** (chưa đo — chỉ quay lại bằng benchmark thật) (M-08) | [repo ✅] B.5 · [Drive ⏳] xóa §9.1/Hình 7 |
| R-02 | **Phân loại MAS / chẩn đoán / AI-clinical** — từ chối Nâng cấp 1 (M-15) | [không vào báo cáo] |
| R-03 | **AAN trên người / vòng kín lực lên người** — từ chối Nâng cấp 2; AAN chỉ trên phantom (M-12/M-15) | [repo ✅] A.4/B.3 · [Drive ⏳] viết lại §10 |
| R-04 | Chữ **"triệt tiêu hoàn toàn / triệt để"** → "giảm + định lượng phần dư" (M-10) | [repo ✅] B.9 · [Drive ⏳] §8.3/§12.1 |
| R-05 | **Góc "quy đổi từ tín hiệu"** ADC→độ (M-13) | [Drive ⏳] sửa Hình 4 |
| R-06 | **Suy nguyên nhân GAP** ("do yếu cơ/co cứng") (M-14) | [Drive ⏳] sửa §8.2 |
| R-07 | **"RAL giảm = bệnh cải thiện"** → "đặc trưng giao thức kiểm định" (M-11) | [Drive ⏳] sửa §10.3 |
| R-08 | Ngôn ngữ AAN trên người ("tay người bệnh", "bảo vệ khớp") (M-12) | [Drive ⏳] sửa §10.2/Hình 12 |
| R-09 | **200 Hz đa kênh** + 50 Hz danh định (M-02/M-03) | [repo ✅] · [Drive ⏳] |
| R-10 | **ML suy luận gập/duỗi trên NPU** — dấu vi sai đã làm việc đó | [repo ✅] B.5 · [Drive ⏳] sửa Hình 10 |
| R-11 | Mục tiêu **3D/EKF/IMU-từng-đốt** khỏi giai đoạn này → hướng phát triển | [repo ✅] B.6/C.8 · bản Drive §12.2 giữ nguyên |
| R-12 | **Chương "ảnh hưởng nhiệt độ" riêng** (đã thu hẹp ở T-09) | [Drive ⏳] |
| R-13 | **[17] dạng "khảo sát bệnh viện"** → tham khảo ẩn danh trên giấy (M-24) | [repo ✅] A.5 · [Drive ⏳] sửa TLTK [17] |
| R-14 | §12 **"chế tạo thành công… đạt trọn vẹn"** (0 số liệu) → hạ về đúng mức (M-05) | [Drive ⏳] viết lại §12.1 |

**Đã bỏ khỏi danh sách mua:** DMM spare (~500k) — 2 DMM hiện tại đủ · Tra model DMM rời — không làm.

---

## IV. VIỆC CỦA BẠN (gom từ các ⏳ — 8 việc)

1. Đo R(F) thật (DMM + quả cân) → trả lời M-01/M-17 (Vex, G, S, SNR).
2. Viết công thức EI (M-25) + chốt 9 ngưỡng `protocols/08` §7 trước khi đo.
3. Viết mục người đeo + an toàn (M-26).
4. Gửi 5 số INT8 (model/input/latency/RKNN/log) (M-08).
5. Shopping P0 (B-08) — HX711 trước tiên.
6. Ngân sách mô-men + test nhiệt servo (M-19) · nghiệm thu vít me + khóa cổ (M-20).
7. Sửa bản Drive theo các mục [Drive ⏳] (15 chỗ).
8. Xác nhận Pi bản RAM mấy GB + nguồn/thẻ (cho đủ hồ sơ).
