# Ảnh chụp minh chứng: Oscilloscope 2C23T (09/10) + Serial Plotter (11/10)

> **Nguồn:** Ảnh chụp thực tế từ màn hình máy đo FNIRSI 2C23T và giao diện Serial Plotter của nhóm nghiên cứu.
> **Trạng thái:** GHI NHẬN THỰC NGHIỆM — đối chiếu cùng `research/protocols/08a` (xem `CLM-EVID-002`).

## 1. Dạng sóng đo trên máy hiện sóng FNIRSI 2C23T (đo ngày **09/10/2026**)

| Kênh | Vai trò (theo xác nhận của nhóm) | Vmax | Vmin | Vavg | Vpp |
|---|---|---|---|---|---|
| CH1 (xanh dương) | Output của INA333 | 1.62 V | 0.06 V | 0.84 V | **1.55 V** |
| CH2 (vàng/cam) | Input từ signal generator, amp cài đặt ≈ 0.1 V | 0.12 V | — | 0.00 V | **0.24 V** |

Timebase 1 ms/div, CH1 Auto trigger, cả 2 kênh thang 500 mV×1 DC.

**Độ lợi đo được:** G = Vpp(CH1)/Vpp(CH2) = 1.55 / 0.24 ≈ **6.46×**.

-> **Khớp gần như chính xác** với con số đã ghi trong
`05_nhat_ky_thuc_nghiem_do_kiem_ina333_ads1115_cd74hc4067.md`:
*"Hệ số khuếch đại đạt G ≈ 6.5 lần (Vpp từ 0.24V khuếch đại lên 1.55V)"*.
→ Kết quả đo thực tế là minh chứng số liệu trực quan cho hệ số khuếch đại đã ghi nhận trong mục 05.

**Nội dung đối chiếu kỹ thuật:** `docs/04_Hardware_Architecture.md`
(dòng 189, 202) ghi thiết kế mục tiêu **"INA333 G = 10"** (`R_ref = 10 kΩ`). Số đo thật
hiện tại là **G ≈ 6,46–6,5×**, thấp hơn mục tiêu thiết kế khoảng 35%. Theo mô tả ở note 05,
đây là do **trim biến trở SMD R_G bằng tay** (không phải điện trở cố định 10 kΩ như dự
kiến ban đầu) để giải quyết lỗi clipping âm khi chạy nguồn đơn. Hai hướng xử lý:
1. Chấp nhận G≈6,5 là giá trị thực tế của thiết kế, cập nhật lại `docs/04` + ngân sách
   nhiễu/độ phân giải LSB cho khớp (vì G ảnh hưởng trực tiếp tới độ phân giải hiệu dụng
   của chuỗi ADS1115 16-bit ±2,048 V).
2. Tiếp tục trim biến trở để kéo G lên gần 10 như thiết kế gốc, rồi đo lại.

## 2. Dạng sóng số hóa trên Serial Plotter qua giao tiếp USB (đo ngày **11/10/2026**)

Đấu nối MUX theo ghi nhận của nhóm:
- **C0** → signal generator, sóng sine 51 Hz, "duty 99", amp 2.1 (đơn vị chưa xác nhận —
  khả năng là Vpp hoặc biên độ đỉnh cài trên máy phát, **chưa chắc là giá trị thực
  nhận được tại điểm đo** do còn tụ AC-coupling + mạch ghim DC mô tả ở note 05).
- **C1** → "1 nguồn khoảng 1,5 mấy volt" (nhóm cần đo lại bằng đồng hồ VOM).
- **C2** → GND.

| Kênh hiển thị | Dải quan sát | Dạng sóng |
|---|---|---|
| Kenh_0 (xanh dương) = C0 | ~600–1750 (đơn vị trục Y: mV quy đổi) | Răng cưa/tam giác đều, chu kỳ ~12–13 mẫu |
| Kenh_1 (cam) = C1 | ~3200–3300 | Gần phẳng, gợn nhẹ |
| Kenh_2 (xanh lá) = C2 | ~100–180 | Gần phẳng, gợn nhẹ |

**Điểm tốt:** Kenh_1 và Kenh_2 không bị dao động "ăn theo" Kenh_0 → gợi ý MUX cách ly
kênh tốt, không crosstalk rõ rệt khi quét — khớp với kết luận đã ghi ở note 02
("CD74HC4067 hoạt động chính xác... không xảy ra hiện tượng rò kênh").

**Hai điểm cần xác minh lại trên bàn đo:**

1. **Đơn vị trục Y của Serial Plotter:** Note 02 (phiên đo trước) đã in giá trị
   trực tiếp bằng **mV** ra Serial Plotter (ví dụ "kịch trần nguồn 3250 mV"). Dải số
   quan sát trong ảnh mới (~3200–3300) giống hệt về độ lớn với con số mV đó của phiên
   trước, cho thấy đây là giá trị mV đã quy đổi trong firmware.
2. **Đối với kênh C1:** Kenh_1 đọc ~3,2–3,3 V — cao hơn mốc 1,5 V dự kiến. Nhóm cần
   kiểm tra lại tiếp điểm dây đo xem có chạm đường nguồn VCC 3,3 V hay không. Kenh_2 (nối GND) đọc ~0,1–0,18 V thay vì 0 V — mức lệch
   này là offset hệ thống cần trừ trong phần mềm.

## 3. Các bước tiếp theo cần triển khai

1. Xác nhận đơn vị trục Y Serial Plotter (mV hay raw count) — nếu mV, cho biết công thức
   quy đổi đang dùng trong firmware (hệ số, offset).
2. Đo lại/kiểm tra điểm nối C1 để làm rõ giá trị ~1,5 V kỳ vọng vs ~3,2–3,3 V đo được.
3. Quyết định hướng xử lý chênh lệch G≈6,5 vs G=10 thiết kế (mục 1 ở trên).
4. Khi đã rõ 3 điểm trên, mới đưa các con số này vào `research/bench/logs/` theo đúng
   schema GATE 0 (`session_manifest.csv` với `bench_session_id` riêng cho từng ngày đo
   09/10 và 11/10) — **hiện tại thư mục đó vẫn phải giữ rỗng** theo đúng quy tắc đã ghi
   trong `research/bench/logs/README.md`.
