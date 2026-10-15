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
> 
> *Chi tiết triển khai cơ cấu cơ khí nẹp ngón, khoang âm preload $9.5 \times 6.8 \times 1.2\,\text{mm}$, bản lề Print-in-Place và khớp rãnh trượt tự lựa bù 13.5mm: xem tài liệu chuyên sâu [`docs/06_Co_Cau_Co_Khi_Exoskeleton.md`](06_Co_Cau_Co_Khi_Exoskeleton.md) và thư mục CAD 3D [`3d_model/custom_exo/full_finger_modular/`](../3d_model/custom_exo/full_finger_modular/). Riêng bài toán đóng/mở vỏ nẹp quanh một đốt ngón (để bệnh nhân tự đeo/tháo một tay) đang được thử nghiệm song song, chưa tích hợp chính thức — xem [`3d_model/custom_exo/fixation_mechanisms_benchmark/README.md`](../3d_model/custom_exo/fixation_mechanisms_benchmark/README.md).*

---

## 4. Ngân sách độ phân giải

### 4.1 Chuỗi tín hiệu
```
Velostat (R_sensor thay đổi theo lực)
   → cầu phân áp với R_f
   → CD74HC4067 (R_on ~ 50–70 Ω ở 5 V, thấp hơn nhiều so với R_sensor)
   → ADC1 của ESP32-S3
```

**Chọn R_f:** độ nhạy `dV/dR` cực đại khi `R_f ≈ R_sensor`. Vì R_sensor của sensing element tự chế **chưa được đo** [Thông tin], quy trình bắt buộc là:
1. Đo R_sensor ở các mức tải khác nhau (bench, có load cell tham chiếu).
2. Chọn R_f nằm giữa dải làm việc (dự kiến hàng chục kΩ — [Thông tin] phải đo).
3. Ghi lại đường cong `ADC ↔ lực` cho từng sensing element (không dùng chung một đường cong cho mọi kênh).

### 4.2 Ngân sách nhiễu (dự kiến — phải đo lại)

| Nguồn | Ảnh hưởng dự kiến | Cách xử lý |
|---|---|---|
| Lượng tử hóa ADC 12-bit | ~1 LSB ≈ 0,8 mV trên dải 3,3 V | — |
| Nhiễu ADC ESP32-S3 (ENOB thực ~9–10 bit) | vài LSB | Lấy trung bình N mẫu |
| Nhiễu nguồn/đường dẫn | phụ thuộc layout | Tụ lọc, dây ngắn, mass chung chắc chắn |
| Điện trở tiếp xúc copper–Velostat | có thể lớn, thay đổi theo tải | Preload + kẹp cơ khí ổn định |

> **Xác nhận độc lập từ y văn (2026-10-11, `CLM-HW-005`):** hạn chế độ chính xác của Velostat trong bảng trên không phải suy đoán — 2 nguồn thực nghiệm độc lập đo được sai số **16–48% trên toàn thang đo** khi dùng Velostat làm cảm biến áp lực (`SRC-VELOSTAT-HOPKINS-2020`: ổ khớp chi giả; `SRC-VELOSTAT-INSOLE-DEFAZIO-2021`: lót giày đo dáng đi), kèm hiện tượng trễ (hysteresis). Đây là lý do `docs/02` §7.3 định nghĩa EI/GAP/RAL là chỉ số **tương đối, trong-cùng-một-người**, không phải lực tuyệt đối theo N — khớp đúng với giới hạn vật liệu đã biết, không phải né tránh.

**Lấy trung bình:** nhiễu ngẫu nhiên giảm theo `√N`.
- N = 16 → giảm ~4 lần (~2 bit hiệu dụng) → **~11 bit hiệu dụng**.
- N = 64 → giảm ~8 lần (~3 bit) → đổi lại tốc độ khung giảm.

> Đây là **ước lượng lý thuyết**. Giá trị thật của ENOB **phải đo bằng log** (đo với đầu vào cố định rồi tính độ lệch chuẩn).

---

## 5. Ngân sách tốc độ khung

Giả định mỗi kênh cần **thời gian ổn định (settling) + lấy mẫu**: `t_ch ≈ 100–300 µs` khi đã lấy trung bình nhiều mẫu ([Thông tin] đo lại thực tế).

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

1. [ ] Chốt cấu hình 1 hay 2 (hoặc lộ trình 1 → 2) — và chốt `DEC-SCOPE-005` (3 ngón như bản nộp hay giữ lộ trình 5 ngón).
2. [ ] Đo `R_sensor` theo tải cho ≥ 5 mẫu sensing element tự chế.
3. [ ] Đo ENOB thực của chuỗi ADC + MUX.
4. [ ] Đo tốc độ khung và độ trễ end-to-end thực tế.
5. [ ] Ghi toàn bộ vào `research/bench/` và `research/evidence/SOURCE_LEDGER.csv` (loại `raw_measurement`).
6. [ ] Sau đó mới chạy `research/protocols/06_glove_hand_GATE_experiment.md`.

---

## 8. Cấu hình ĐÃ NỘP (`docs/DE_CUONG.pdf` §8–§9, 2026-09-26) — chờ `DEC-HW-005`

> Các §1–§7 ở trên là **ngân sách thiết kế trên giấy** (ESP32-S3 ADC 12-bit, `V_EX = 3,1 V`, 6 IMU, lộ trình 5 ngón).
> Bản nộp dùng chuỗi khác. **Không xóa §1–§7** (lịch sử thiết kế); khi `DEC-HW-005` được chốt thì §8 này thành cấu hình hiện hành
> và `protocols/08` §3 + `docs/02` §5.5 phải tính lại theo LSB mới. Chi tiết: `CLM-HW-003`, sync review §2-F6.

```
[Tầng 1 — tay]  12 sensing element Velostat (khung ốp ngón PETG in 3D, điện cực đồng 0,05 mm,
                bu-lông kẹp vi chỉnh preload F_p) + 1 ô tham chiếu không tải
                + 1 IMU 6-DOF LSM6DS3 ở mu tay (bù góc nghiêng trọng trường)
[Tầng 2 — cổ tay] 2× CD74HC4067 (chuyển mạch 1 kHz) → MCP6001 đệm
                → cầu vi sai ΔV = V(lòng) − V(mu), R_ref = 10 kΩ (0,1 %, 25 ppm/°C)
                → INA333 G = 10 (CMRR ≥ 100 dB) → ADS1115 16-bit (±2,048 V, 62,5 µV/LSB, 860 SPS)
                → ESP32-S3 (lọc IIR bậc 2 fc = 10 Hz, Notch 50 Hz, BLE 5.0)
                → nguồn LiPo 3,7 V qua TP4056 + LDO HT7333 (cách ly lưới điện)
                + SHT30 bù trôi nhiệt–ẩm
[Tầng 3 — biên] Orange Pi 5 Pro (RK3588, NPU 6 TOPS): suy luận INT8 < 15 ms,
                tính EI/GAP/RAL + dashboard
```

**Bảng delta so với ngân sách §1–§5:**

| Hạng mục | Ngân sách cũ (§1–§5) | Bản nộp (§8–§9 PDF) |
|---|---|---|
| ADC | ESP32-S3 ADC1 12-bit (~1,51 mV/LSB danh định) | **ADS1115 16-bit rời** (62,5 µV/LSB, dải ±2,048 V) |
| Khuếch đại | không có (cầu phân áp thụ động, `R_f ≈ R_sensor`) | **INA333 G = 10**, `R_ref = 10 kΩ` 0,1 % |
| Đệm / bù môi trường | chưa có | MCP6001 + **SHT30** |
| IMU | 6 IMU (góc AROM/PROM + tốc độ kéo) | **1 IMU LSM6DS3** (bù nghiêng) — Lưu ý: nguồn đo góc cho GAP còn mở (**I7**) |
| Lấy mẫu | mục tiêu 45–100 Hz, sàn 20 Hz | Lưu ý: PDF ghi **cả 50 Hz** (§8.1/§9.1) **và 20 Hz** (M5/C1.10) — **I1** |
| Lọc số | chưa định | IIR bậc 2 fc = 10 Hz + Notch 50 Hz |
| Ngón | lộ trình 5 ngón (cấu hình 1/2) | **3 ngón** (cái/trỏ/giữa) — `DEC-SCOPE-005` |
| Kênh vi sai | 24 kênh vi sai (cấu hình 2) | "**12 kênh vi sai**" trên 6 khớp — Lưu ý: chưa rõ 12 cặp hay 12 phần tử (**I6**) |
| Nguồn | chưa định | LiPo 3,7 V + TP4056 + HT7333 |

**Quy tắc vận hành đi kèm (PDF §9.3/§11.2):** auto-zero 3 s duỗi nghỉ đầu phiên (`V_offset` trừ trực tiếp);
cảnh báo kiểm tra cơ khí khi trôi tĩnh vượt **±5 %** dải đo so với ô tham chiếu; vòng lặp 1 (`V_base` → chỉnh găng),
vòng lặp 2 (phương sai → nhãn **"Nghi vấn"** + loại khỏi xu hướng + đo lại).

---

## 9. Vòng lặp thiết kế 2 (15/10/2026, `DEC-HW-006`): Tối ưu hóa mạch đo dựa trên thực nghiệm cơ khí

Ghi nhận quá trình thực nghiệm phát hiện giới hạn bão hòa của tầng khuếch đại INA333 khi siết nẹp ngón tay và giải pháp chuyển đổi sang mạch đo trực tiếp qua ADS1115 kết hợp thuật toán xử lý tín hiệu số.

```
[Mạch ban đầu]
Màng Velostat -> MUX CD74HC4067 -> Tầng INA333 (G ≈ 6.5, V_REF = 1.68V) -> ADS1115 (A0) -> ESP32-S3
==> Hiện tượng lỗi: Lực siết tĩnh của khung ốp ngón tay kéo mốc tĩnh tụt xuống < 1.42V, làm INA333 chạm sàn bão hòa
    (kẹt ở ≈ 2838 mV). Cửa sổ tuyến tính ±0.24V quá hẹp so với biên độ thật (1.5V - 2.2V) của Velostat.

[Mạch cải tiến - DEC-HW-006]
Màng Velostat (kẹp dây đồng mạ niken) + điện trở kéo lên 10 kΩ
   -> MUX CD74HC4067 (thời gian trễ 300 µs và đọc nháp để xả điện tích ký sinh)
   -> Tầng PGA 16-bit tích hợp trong ADS1115 (dải đo mở rộng toàn phần 0V - 3.3V, bước lượng tử 0.125 mV/LSB)
   -> ESP32-S3: Lọc số 4 bước (Đọc nháp -> Khóa vùng chết 180 mV -> Tự động bám mốc tĩnh -> Lọc EMA và tính lực vi sai)
```

**Bảng so sánh tối ưu hóa giữa 2 vòng lặp:**

| Tiêu chí | Vòng lặp 1 (INA333, $G \approx 6.5$) | Vòng lặp 2 (PGA 16-bit ADS1115 + DSP) | Cơ sở lý luận & Bằng chứng thực nghiệm |
|---|---|---|---|
| **Dải động thu nhận** | Bị bão hòa khi $\Delta V > 0.24\text{V}$ | Toàn dải $0.000\text{V} - 3.300\text{V}$ | Màng Velostat có độ nhạy lớn hơn hàng trăm lần strain gauge, tự thân tạo biến thiên $1.5\text{V} - 2.2\text{V}$, không cần khuếch đại tương tự hệ số lớn. |
| **Độ nhạy cơ học tĩnh** | Dễ kẹt sàn khi siết ốc nẹp | Mở rộng biên độ, đo được từ lúc nghỉ có tải tĩnh | Lực siết cơ khí ban đầu không còn làm tê liệt mạch đo. |
| **Nhiễu nền & Trôi** | Bị nhân $6.5$ lần qua INA333 | Giữ nguyên bản ($50 - 135\text{ mV}$), triệt tiêu bằng DSP | Thuật toán Adaptive Drift Tracking ($\gamma = 0.002$) tự thích nghi với dão nhựa và thân nhiệt. |
| **Độ phức tạp phần cứng** | Thêm 1 IC tương tự, cần nguồn tham chiếu ảo $V_{REF}$ | Tối giản phần cứng (Hardware Simplification) | Giảm tiêu thụ năng lượng, giảm kích thước mạch trên ngón tay, tăng độ tin cậy. |

