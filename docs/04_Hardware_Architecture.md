# 04 — Kiến trúc phần cứng

> **Ngày:** 2026-09-13 · **Quyết định liên quan:** DEC-HW-003 (ESP32-S3 thay Mega 2560), DEC-HW-004 (bố trí kênh).
> **Trạng thái:** **thiết kế trên giấy**. Mọi con số về nhiễu/độ phân giải/tốc độ khung dưới đây là **ngân sách dự kiến (design budget)**, phải **đo lại trên bench** trước khi đưa vào báo cáo.
> **Không** được trích các số trong tài liệu này như kết quả thực nghiệm.

---

## 1. Sơ đồ tổng thể

```
        ┌──────────── Mảng sensing element (12–24 kênh) ────────────┐
        │  Velostat + copper tape, dán trên vách khung in 3D        │
        └───────────────────────────┬───────────────────────────────┘
                                    │ tín hiệu tương tự
                        ┌───────────▼───────────┐
                        │  CD74HC4067 (16:1)     │  ×1 (cấu hình 12 kênh)
                        │  chọn kênh bằng 4 GPIO │  ×2 (cấu hình 24 kênh,
                        └───────────┬───────────┘   chọn chip bằng chân EN)
                                    │ 1 đường analog
                        ┌───────────▼───────────────────────────┐
                        │  ESP32-S3                             │
                        │  · ADC1 12-bit + lấy trung bình N mẫu │
                        │  · quét kênh → frame + CRC            │
                        │  · BLE 5 (không dây) / UART (bench)   │
                        └───────────┬───────────────────────────┘
                                    │
                        ┌───────────▼───────────────────────────┐
                        │  Orange Pi 5 Pro (RK3588)             │
                        │  · bù ảnh hưởng drift                 │
                        │  · trích đặc trưng → vector lực       │
                        │  · suy luận hướng khớp → bàn tay 3D   │
                        │  · mô hình INT8 (RKNN) trên NPU       │
                        └───────────┬───────────────────────────┘
                                    │
                        Dashboard theo tuần (KTV/bác sĩ)
```

---

## 2. Vì sao ESP32-S3 thay Arduino Mega 2560 (DEC-HW-003)

| Tiêu chí | Arduino Mega 2560 | **ESP32-S3** | Kết luận |
|---|---|---|---|
| ADC | 10-bit, 16 kênh | 12-bit danh định (ADC1), 2 khối SAR | ESP32-S3 |
| Tốc độ | 16 MHz, 8-bit AVR | 240 MHz, dual-core, có gia tốc vector cho NN | ESP32-S3 |
| Truyền dữ liệu | UART/USB có dây | BLE 5 + Wi-Fi + USB-OTG | ESP32-S3 (bắt buộc cho thiết bị đeo tại nhà) |
| Mức logic | 5 V → **cần level shifter** sang Orange Pi 3.3 V | **3.3 V** → khớp trực tiếp | ESP32-S3 (bớt một rủi ro điện) |
| Kích thước/tiêu thụ | To, tốn điện | Nhỏ, có chế độ ngủ | ESP32-S3 |
| Số chân analog | 16 chân ADC rời | **ít chân ADC** (ADC1 dùng được ~7–8 chân trên nhiều board) → **cần MUX** | Hoà, nhưng MUX là bắt buộc |

**Đánh đổi phải ghi nhận trung thực:** ADC của ESP32-S3 **không tuyến tính hoàn hảo** và nhạy với cấu hình (suy giảm khi bật Wi-Fi). Vì vậy:
- chỉ dùng **ADC1**; nếu cần truyền không dây thì ưu tiên **BLE**, tránh Wi-Fi trong lúc đo;
- phải **hiệu chuẩn ADC** (đường cong hiệu chỉnh theo điện áp chuẩn) trước khi dùng;
- phải ghi lại nhiệt độ/điện áp nguồn trong log để truy vết.

---

## 3. Bố trí kênh

### 3.1 Cấu hình 1 — Tối thiểu khả thi (12 kênh, 1 MUX) — *dùng cho bring-up và GATE 0/A*

| Kênh | Vị trí | Vách đo | Ghi chú |
|---|---|---|---|
| CH0 | Ngón trỏ – MCP | phía lòng bàn tay (flexor side) | |
| CH1 | Ngón trỏ – PIP | phía lòng bàn tay | |
| CH2 | Ngón giữa – MCP | phía lòng bàn tay | |
| CH3 | Ngón giữa – PIP | phía lòng bàn tay | |
| CH4 | Ngón áp út – MCP | phía lòng bàn tay | |
| CH5 | Ngón áp út – PIP | phía lòng bàn tay | |
| CH6 | Ngón út – MCP | phía lòng bàn tay | |
| CH7 | Ngón út – PIP | phía lòng bàn tay | |
| CH8 | Ngón cái – MCP | vách đối diện (opposition) | |
| CH9 | Ngón cái – IP | vách đối diện | |
| CH10 | Lòng bàn tay (khối thenar) | pháp tuyến | lực cầm nắm |
| CH11 | **Ô tham chiếu** | trên nẹp cổ tay, không chịu tải người dùng | đo trôi hệ thống |

**Hạn chế của cấu hình 1 (phải nói thẳng):** mỗi khớp chỉ có **một vách** ⇒ chỉ biết *độ lớn*, chưa phân biệt được **dấu** gập/duỗi một cách chắc chắn. Dấu được suy ra từ **so sánh với đường nền (baseline) động**, kém tin cậy hơn đo vi sai.

### 3.2 Cấu hình 2 — Đầy đủ, đo vi sai (24 kênh, 2 MUX) — *dùng cho GATE A/B/C*

Mỗi khớp có **cặp sensing element đối xứng** trên hai vách đối diện:

| Nhóm | Số khớp | Số kênh |
|---|---|---|
| 4 ngón dài × 2 khớp (MCP, PIP) × 2 vách | 8 | 16 |
| Ngón cái × 2 khớp (MCP, IP) × 2 vách | 2 | 4 |
| Lòng bàn tay × 2 vùng | — | 2 |
| Ô tham chiếu | — | 2 (đặt cạnh nhau, kiểm tra chéo) |
| **Tổng** | | **24** |

Với 24 kênh dùng **2 × CD74HC4067**: cả hai MUX đưa tín hiệu về **cùng một chân ADC1**, chọn bằng chân **EN** (chỉ một chip hoạt động tại mỗi thời điểm) → tránh phải dùng ADC2 (ADC2 dùng chung tài nguyên với Wi-Fi).

> **Nguyên tắc thiết kế cơ khí đi kèm:** mỗi sensing element phải được **kéo trước (preload)** một lực nhỏ, xác định, để tín hiệu có cả nhánh dương và nhánh âm quanh điểm làm việc. Không preload thì không đo được chiều.

---

## 4. Ngân sách độ phân giải

### 4.1 Chuỗi tín hiệu
```
Velostat (R_sensor thay đổi theo lực)
   → cầu phân áp với R_f
   → CD74HC4067 (R_on ~ 50–70 Ω ở 5 V, thấp hơn nhiều so với R_sensor)
   → ADC1 của ESP32-S3
```

**Chọn R_f:** độ nhạy `dV/dR` cực đại khi `R_f ≈ R_sensor`. Vì R_sensor của sensing element tự chế **chưa được đo** 🔵, quy trình bắt buộc là:
1. Đo R_sensor ở các mức tải khác nhau (bench, có load cell tham chiếu).
2. Chọn R_f nằm giữa dải làm việc (dự kiến hàng chục kΩ — 🔵 phải đo).
3. Ghi lại đường cong `ADC ↔ lực` cho từng sensing element (không dùng chung một đường cong cho mọi kênh).

### 4.2 Ngân sách nhiễu (dự kiến — phải đo lại)

| Nguồn | Ảnh hưởng dự kiến | Cách xử lý |
|---|---|---|
| Lượng tử hóa ADC 12-bit | ~1 LSB ≈ 0,8 mV trên dải 3,3 V | — |
| Nhiễu ADC ESP32-S3 (ENOB thực ~9–10 bit) | vài LSB | Lấy trung bình N mẫu |
| Nhiễu nguồn/đường dẫn | phụ thuộc layout | Tụ lọc, dây ngắn, mass chung chắc chắn |
| Điện trở tiếp xúc copper–Velostat | có thể lớn, thay đổi theo tải | Preload + kẹp cơ khí ổn định |

**Lấy trung bình:** nhiễu ngẫu nhiên giảm theo `√N`.
- N = 16 → giảm ~4 lần (~2 bit hiệu dụng) → **~11 bit hiệu dụng**.
- N = 64 → giảm ~8 lần (~3 bit) → đổi lại tốc độ khung giảm.

> Đây là **ước lượng lý thuyết**. Giá trị thật của ENOB **phải đo bằng log** (đo với đầu vào cố định rồi tính độ lệch chuẩn).

---

## 5. Ngân sách tốc độ khung

Giả định mỗi kênh cần **thời gian ổn định (settling) + lấy mẫu**: `t_ch ≈ 100–300 µs` khi đã lấy trung bình nhiều mẫu (🔵 đo lại thực tế).

| Cấu hình | Số kênh | t_ch | Thời gian 1 vòng quét | Tốc độ khung (không nghỉ) |
|---|---|---|---|---|
| 12 kênh | 12 | 200 µs | 2,4 ms | **~415 Hz** |
| 24 kênh | 24 | 200 µs | 4,8 ms | **~208 Hz** |
| 24 kênh | 24 | 300 µs | 7,2 ms | **~139 Hz** |

**Nhu cầu thực tế:** động tác phục hồi chức năng có tần số thấp (khoảng **0,5–2 Hz**). Theo nguyên lý lấy mẫu, tốc độ khung **≥ 20–50 Hz** đã đủ để bắt dạng sóng lực mà không mất thông tin quan trọng. Vì vậy:
- **Mục tiêu thiết kế: 45–100 Hz** (rộng rãi so với yêu cầu), dành phần dư cho lấy trung bình và truyền BLE.
- Có thể **giảm tốc độ khung để tăng độ phân giải** nếu GATE 0 cho thấy nhiễu là yếu tố giới hạn.
- Phải ghi rõ trong log: số mẫu trung bình N, tốc độ khung thực đo, và độ trễ end-to-end.

---

## 6. Đóng gói khung găng

| Thành phần | Vật liệu / cách làm | Rủi ro |
|---|---|---|
| Khung cứng định vị lóng ngón | In 3D (PLA/PETG); khe hở điều chỉnh được | Cứng quá → cấn, không thoải mái; lỏng quá → mất tín hiệu |
| Lớp đệm tiếp xúc | TPU mềm / xốp mỏng | Ảnh hưởng preload |
| Dây dẫn | Dây mảnh dọc mu bàn tay, gom về hộp mạch ở cổ tay | Đứt dây khi gập nhiều lần |
| Hộp mạch | In 3D, gắn ở ngoài cổ tay | Khối lượng/kích thước ảnh hưởng tính khả dụng |
| Chống trượt | Dây đai Velcro quanh cổ tay + đai từng ngón | Xoay/trượt làm sai vị trí kênh |

**Tiêu chí công thái học tối thiểu cần đạt (phải đo, không được nói suông):**
thời gian mang/tháo (don–doff) ở mức người nhà làm được trong ~1 phút; khối lượng tổng; không gây đau khi đeo 15 phút; không cấn khi gập tối đa.

---

## 7. Việc phải làm trước khi viết bất kỳ kết luận nào

1. ☐ Chốt cấu hình 1 hay 2 (hoặc lộ trình 1 → 2).
2. ☐ Đo `R_sensor` theo tải cho ≥ 5 mẫu sensing element tự chế.
3. ☐ Đo ENOB thực của chuỗi ADC + MUX.
4. ☐ Đo tốc độ khung và độ trễ end-to-end thực tế.
5. ☐ Ghi toàn bộ vào `research/bench/` và `research/evidence/SOURCE_LEDGER.csv` (loại `raw_measurement`).
6. ☐ Sau đó mới chạy `research/protocols/06_glove_hand_GATE_experiment.md`.
