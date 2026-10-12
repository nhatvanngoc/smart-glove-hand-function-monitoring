# Ảnh chụp minh chứng: Oscilloscope 2C23T (09/10) + Serial Plotter (11/10)

> **Nguồn:** chủ dự án gửi trực tiếp qua chat 2026-10-11 (2 ảnh, không phải file do agent tạo).
> **Trạng thái:** GHI NHẬN THAM KHẢO — chưa chính thức hoá qua `research/protocols/08a` (xem `CLM-EVID-002`).
> File gốc **chưa có bản lưu ngoài chat** — chủ dự án cần tự tải lên Google Drive
> (`02_Hinh_anh_2C23T/` và `03_Serial_Plotter_exports/`, folder đã tạo 2026-10-11) để có
> bản lưu trữ không phụ thuộc lịch sử chat.

## 1. Ảnh oscilloscope FNIRSI 2C23T — Analog Domain Verification (đo ngày **09/10/2026**)

| Kênh | Vai trò (theo xác nhận của chủ dự án) | Vmax | Vmin | Vavg | Vpp |
|---|---|---|---|---|---|
| CH1 (xanh dương) | Output của INA333 | 1.62 V | 0.06 V | 0.84 V | **1.55 V** |
| CH2 (vàng/cam) | Input từ signal generator, amp cài đặt ≈ 0.1 V | 0.12 V | — | 0.00 V | **0.24 V** |

Timebase 1 ms/div, CH1 Auto trigger, cả 2 kênh thang 500 mV×1 DC.

**Độ lợi đo được:** G = Vpp(CH1)/Vpp(CH2) = 1.55 / 0.24 ≈ **6.46×**.

➡️ **Khớp gần như chính xác** với con số đã ghi trong
`05_nhat_ky_thuc_nghiem_do_kiem_ina333_ads1115_cd74hc4067.md`:
*"Hệ số khuếch đại đạt G ≈ 6.5 lần (Vpp từ 0.24V khuếch đại lên 1.55V)"*.
→ **Ảnh này rất có thể chính là bằng chứng hình ảnh (photographic evidence) đứng sau
câu chữ đã ghi trong note 05** — lần đầu tiên con số G≈6,5 có ảnh gốc đi kèm thay vì chỉ
là mô tả bằng lời.

**Mâu thuẫn cần chủ dự án xử lý (chưa tự sửa):** `docs/04_Hardware_Architecture.md`
(dòng 189, 202) ghi thiết kế mục tiêu **"INA333 G = 10"** (`R_ref = 10 kΩ`). Số đo thật
hiện tại là **G ≈ 6,46–6,5×**, thấp hơn mục tiêu thiết kế khoảng 35%. Theo mô tả ở note 05,
đây là do **trim biến trở SMD R_G bằng tay** (không phải điện trở cố định 10 kΩ như dự
kiến ban đầu) để giải quyết lỗi clipping âm khi chạy nguồn đơn. Hai hướng xử lý khả dĩ
(chủ dự án quyết định, agent không tự chọn):
1. Chấp nhận G≈6,5 là giá trị thực tế của thiết kế, cập nhật lại `docs/04` + ngân sách
   nhiễu/độ phân giải LSB cho khớp (vì G ảnh hưởng trực tiếp tới độ phân giải hiệu dụng
   của chuỗi ADS1115 16-bit ±2,048 V).
2. Tiếp tục trim biến trở để kéo G lên gần 10 như thiết kế gốc, rồi đo lại.

## 2. Ảnh Serial Plotter — Digital Domain Verification (đo ngày **11/10/2026**)

Đấu nối MUX theo xác nhận của chủ dự án:
- **C0** → signal generator, sóng sine 51 Hz, "duty 99", amp 2.1 (đơn vị chưa xác nhận —
  khả năng là Vpp hoặc biên độ đỉnh cài trên máy phát, **chưa chắc là giá trị thực
  nhận được tại điểm đo** do còn tụ AC-coupling + mạch ghim DC mô tả ở note 05).
- **C1** → "1 nguồn khoảng 1,5 mấy volt" (chủ dự án không nhớ chính xác).
- **C2** → GND.

| Kênh hiển thị | Dải quan sát | Dạng sóng |
|---|---|---|
| Kenh_0 (xanh dương) = C0 | ~600–1750 (đơn vị trục Y **chưa xác nhận**: mV hay raw ADC count) | Răng cưa/tam giác đều, chu kỳ ~12–13 mẫu |
| Kenh_1 (cam) = C1 | ~3200–3300 | Gần phẳng, gợn nhẹ |
| Kenh_2 (xanh lá) = C2 | ~100–180 | Gần phẳng, gợn nhẹ |

**Điểm tốt:** Kenh_1 và Kenh_2 không bị dao động "ăn theo" Kenh_0 → gợi ý MUX cách ly
kênh tốt, không crosstalk rõ rệt khi quét — khớp với kết luận đã ghi ở note 02
("CD74HC4067 hoạt động chính xác... không xảy ra hiện tượng rò kênh").

**Hai nghi vấn cần xác minh trước khi chính thức hoá (KHÔNG tự suy diễn thêm):**

1. **Đơn vị trục Y của Serial Plotter là gì?** Note 02 (phiên đo trước) đã in giá trị
   trực tiếp bằng **mV** ra Serial Plotter (ví dụ "kịch trần nguồn 3250 mV"). Dải số
   quan sát trong ảnh mới (~3200–3300) **giống hệt về độ lớn** với con số mV đó của phiên
   trước — gợi ý khả năng cao đây **cũng là mV đã quy đổi trong firmware**, không phải
   raw ADC count 12-bit/16-bit. Nhưng đây là suy luận, **chưa được chủ dự án xác nhận**.
2. **Nếu trục Y là mV:** Kenh_1 đọc ~3,2–3,3 V — **không khớp** với "nguồn khoảng 1,5 V"
   mà chủ dự án nhớ (chênh lệch gần gấp đôi). 3,2–3,3 V gần sát mức thanh nguồn VCC (3,3 V)
   — nghi vấn: dây đo có đang thực sự chạm đúng nguồn ~1,5 V hay đang nổi (floating) hoặc
   vô tình chạm VCC/một điểm khác? Kenh_2 (nối GND) đọc ~0,1–0,18 V thay vì 0 V — mức lệch
   này hợp lý coi là **offset hệ thống cần hiệu chỉnh**, không phải lỗi nối dây.

## 3. Việc cần làm tiếp (owner quyết định, agent không tự chọn hướng)

1. Xác nhận đơn vị trục Y Serial Plotter (mV hay raw count) — nếu mV, cho biết công thức
   quy đổi đang dùng trong firmware (hệ số, offset).
2. Đo lại/kiểm tra điểm nối C1 để làm rõ giá trị ~1,5 V kỳ vọng vs ~3,2–3,3 V đo được.
3. Quyết định hướng xử lý chênh lệch G≈6,5 vs G=10 thiết kế (mục 1 ở trên).
4. Khi đã rõ 3 điểm trên, mới đưa các con số này vào `research/bench/logs/` theo đúng
   schema GATE 0 (`session_manifest.csv` với `bench_session_id` riêng cho từng ngày đo
   09/10 và 11/10) — **hiện tại thư mục đó vẫn phải giữ rỗng** theo đúng quy tắc đã ghi
   trong `research/bench/logs/README.md`.
