# Project snapshot — 2026-09-13

> Bản nén ngữ cảnh để phiên sau khôi phục trạng thái **bằng artifact**, không dựa vào trí nhớ hội thoại.
> Chỉ chứa **sự kiện bền vững**. Quyết định đầy đủ: `DECISION_LOG.md`. Đề tài: `docs/01_Topic_Definition.md`.

---

## 1. Đề tài (CHỐT — DEC-TOPIC-019)

**Tiếng Việt:**

> **Nghiên cứu và phát triển găng tay thông minh hỗ trợ đánh giá và theo dõi chức năng vận động bàn tay trong phục hồi chức năng sau đột quỵ**

**Tiếng Anh:**

> A low-cost smart glove with directional piezoresistive sensing for quantitative hand motor-function assessment and longitudinal monitoring in post-stroke rehabilitation.

**"Viên đạn" — 1 câu:**

> Theo dõi định lượng chức năng bàn tay **tại nhà**, liên tục **giữa các lần tái khám lâm sàng**.

**Loại sản phẩm:** thiết bị **đánh giá & theo dõi**. **KHÔNG** phải robot/găng tập phục hồi chức năng. **KHÔNG** chẩn đoán, **KHÔNG** thay thế đánh giá lâm sàng.

---

## 2. Vấn đề & khoảng trống

- Sau đột quỵ, phục hồi bàn tay phụ thuộc luyện tập chủ động tại nhà; kỹ thuật viên chỉ gặp bệnh nhân mỗi **1–3 tháng**.
- Khoảng giữa hai lần tái khám là **"hộp đen"** (nguyên văn KTVVLTL-PHCN): không biết tập đúng không, đủ không, có tiến triển không.
- Tập sai/không duy trì trong thời gian dài → co cứng, đau, chững lại; nặng hơn: biến dạng khớp, co rút, chèn ép thần kinh ngoại vi.
- Công cụ hiện tại (FMA, ARAT, Box and Block, Jamar, E-Link) = **ảnh chụp tại một thời điểm**, tại cơ sở y tế, chi phí cao.

## 3. Bằng chứng xác nhận khoảng trống

| Nguồn | Vai trò |
|---|---|
| Amin K.R. et al., *Remote Monitoring for the Management of Spasticity*, IEEE OJEMB (2024), DOI 10.1109/OJEMB.2024.3523442 | Hội đồng chuyên gia: công cụ đánh giá hiện tại chỉ dùng được ở phòng khám; theo dõi định lượng giữa các lần tái khám "có ý nghĩa thay đổi cuộc sống và tiết kiệm chi phí"; là bài toán chung của nhiều lĩnh vực PHCN. **Lưu ý:** đối tượng là *spasticity* → chỉ dùng để chứng minh khoảng trống chung |
| OTHER study (2026), DOI 10.1080/09638288.2026.2643929, PMID 41918405 | Theo dõi hoạt động tại nhà + coaching từ xa cải thiện chức năng sinh hoạt và tự quản lý sau đột quỵ |
| DEC-CLINICAL-001 (phỏng vấn KTVVLTL-PHCN, 2026-08-28) | Xác nhận pain point: ảnh chụp rời rạc; "hộp đen"; thiết bị tại nhà chỉ hữu ích nếu chỉ số có ý nghĩa lâm sàng + đủ tin cậy + đơn giản + **bổ sung chứ không thay thế** |
| DEC-CLINICAL-002 (chuyên gia PHCN tại phcn-online.com) | Xác nhận độc lập thứ hai: đề tài đáng nghiên cứu |
| Phỏng vấn KTV phần 2 (2026-09-13) | KTV nêu rõ: giải pháp cần là **đánh giá**, không phải phục hồi chức năng trực tiếp; và lưu ý mức độ khó của bài tập (thụ động dễ → cầm nắm/bấm/xoay cổ tay khó, không đảm bảo an toàn nếu làm tự động) |

## 4. Novelty (trung thực — mức ViSEF)

- **KHÔNG** claim "găng tay + AI/TinyML" là mới; **KHÔNG** claim "đo lực bóp" là mới.
- **Ứng viên chính:** cảm biến **hướng** qua **vách khung cứng** — mã hóa hướng chuyển động của lóng ngón bằng áp lực lên vách, **không dùng IMU/flex sensor**, đồng thời lấy được **độ lớn lực**.
- **Ứng viên ứng dụng:** theo dõi dọc tại nhà + tái tạo bàn tay 3D để chuyên gia xem từ xa.
- **KHÔNG mới (phải trích dẫn prior art):** đọc vi sai/ô tham chiếu để bù drift; INT8 quantization.
- Prior art gần nhất phải differentiate: Zhu lab IROS 2017 (15 IMU + 6 Velostat lực tiếp xúc); Reconfigurable Data Glove 2023 (IMU + Velostat).
- **Chưa hoàn tất rà soát prior art** → xem `docs/03_Literature_Gap_Analysis_Plan.md`. Mức novelty chỉ được chốt sau khi rà soát xong.

## 5. Phần cứng (CHỐT — DEC-HW-002/003/004)

```
Sensing element : Velostat + copper tape + cấu trúc sandwich + lớp cơ khí (tự chế tạo)
Khung           : găng in 3D (PLA/PETG + TPU), vách ép tạo hướng
Cấu hình 1      : 12 kênh (11 đo + 1 tham chiếu) — 1× CD74HC4067 — bring-up, GATE 0/A
Cấu hình 2      : 24 kênh, mỗi khớp 1 CẶP đối xứng → đọc vi sai — 2× CD74HC4067 — GATE A/B/C/D/E
MCU             : ESP32-S3 (ADC1 12-bit + trung bình N mẫu, BLE 5, logic 3.3 V)
                  [thay Arduino Mega 2560 — DEC-HW-003]
Edge            : Orange Pi 5 Pro RK3588 (NPU ~6 TOPS), mô hình INT8 (RKNN)
Tham chiếu bench: load cell + HX711
```

Ngân sách độ phân giải/tốc độ khung (dự kiến, **phải đo lại**): ~11 bit hiệu dụng sau trung bình 16 mẫu; tốc độ khung mục tiêu 45–100 Hz; đủ cho động tác 0,5–2 Hz. Chi tiết: `docs/04_Hardware_Architecture.md`.

## 6. GATE — tiêu chí sống còn

`research/protocols/06_glove_hand_GATE_experiment.md`. Tóm:

- **GATE 0** lặp lại (CV ≤ 5% trong phiên, ICC ≥ 0,75 giữa phiên)
- **GATE A** phân biệt hướng (4 hướng ≥ 85%; cặp đối lập ≥ 90%)
- **GATE B** tái tạo 3D (MAE ≤ 15°, r ≥ 0,8)
- **GATE C ⭐ SỐNG CÒN** Δ giữa các mức chức năng ≥ 2σ_noise; Cohen's d ≥ 0,8; MDC < mức chênh liền kề
- **GATE D** không báo động giả (≤ 10% số phiên qua ≥ 10 ngày)
- **GATE E** tự phát hiện lỗi (≥ 90%, báo động giả ≤ 5%)
- **GATE F** INT8 trên NPU (≤ 50 ms, mất mát ≤ 2%)

**Ngưỡng phải chốt trước khi đo (DEC-METRIC-001).** GATE C fail ⇒ dừng đề tài, báo cáo trung thực.

## 7. Ngôn ngữ bắt buộc (DEC-MSG-001)

| Dùng | Không dùng |
|---|---|
| suy luận hướng gập/duỗi | đo góc khớp |
| giảm ảnh hưởng drift | loại bỏ drift / drift-free |
| găng tay đánh giá và theo dõi | robot/găng tập phục hồi chức năng |
| sensing element chế tạo từ vật liệu Velostat | cảm biến Velostat |
| bổ sung cho đánh giá lâm sàng | thay thế Fugl-Meyer/ARAT |

## 8. Tuyên bố bị cấm

- ❌ Chẩn đoán đột quỵ / mức độ liệt / tiên lượng
- ❌ Thay thế FMA / ARAT / Box and Block / đánh giá của chuyên gia
- ❌ "Đo chính xác lực tuyệt đối" / "đo góc khớp"
- ❌ "Đã kiểm chứng lâm sàng" / "chứng minh hiệu quả"
- ❌ Thử trên người tham gia (kể cả người khỏe) trước khi có IRB/SRC
- ❌ Điền số `[X]` vào A.3 hoặc mục C khi chưa có log đo thật

## 9. Việc tiếp theo (theo thứ tự)

1. ☐ Chốt cấu hình kênh 1 → 2 (hay làm thẳng cấu hình 2).
2. ☐ Chốt giao thức bài tập chuẩn cùng KTVVLTL-PHCN.
3. ☐ Rà soát prior art theo `docs/03` → chốt lại mức novelty.
4. ☐ Chế tạo sensing element → đo `R_sensor`/tải → chọn `R_f`.
5. ☐ Chạy GATE 0 → GATE A/B → **GATE C** → GATE D/E/F.
6. ☐ Điền số thật vào A.3 + mục C của outline.
7. ☐ Chủ dự án đổi tên repo (DEC-REPO-001) và (nếu cần) đổi tên thư mục cục bộ.

## 10. Lịch sử pivot (giữ để không lặp lại sai lầm)

| Đề tài | Số phận | Lý do |
|---|---|---|
| Đệm khí thích ứng + AAC | Bỏ (2026-08-25) | Đã có sản phẩm thương mại; validate khó |
| Smart insole 3D-GRF/COP + knee OA | Bỏ | Prior art dày; cần force plate (không có) |
| Lót giày theo dõi độ cứng mô gan chân (DFU) | Bỏ (2026-08-28) | **GATE 3 (Usefulness) yếu** — stiffness proxy chưa có bằng chứng longitudinal đủ mạnh |
| Loét tì đè | Bỏ | Prior art dày hơn DFU |
| CPR trên bề mặt mềm | Bỏ | Đã được giải quyết bằng 2 accelerometer (PMC5143701) |
| Đánh giá spasticity | Bỏ | Trùng chức năng phụ của đề tài exoskeleton Quảng Trị (giải nhì quốc gia) |
| **Găng tay theo dõi chức năng bàn tay** | **ĐANG LÀM** | Khoảng trống được xác nhận bởi hội đồng chuyên gia 2024 + KTV trong nghề; chưa có đề tài trong tỉnh đụng vào **tay** sau đột quỵ (đề tài exoskeleton Quảng Trị làm **chân**) |

## 11. Điều kiện để đề tài bị coi là thất bại (phải nói thẳng nếu xảy ra)

- GATE C không đạt: chỉ số không đủ nhạy để phân biệt thay đổi chức năng mô phỏng.
- GATE A không đạt: không suy luận được hướng → mất phần "tính mới" chính, chỉ còn là găng đo lực đơn thuần (prior art dày).
- Rà soát prior art tìm ra công bố/sáng chế đã làm đúng cơ chế này.
