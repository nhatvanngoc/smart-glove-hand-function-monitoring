# THỊ GIÁC KHÔNG GIAN 3D: DEPTH ANYTHING V2 TRÊN ORANGE PI 5 PRO
**Nền tảng nhúng:** Orange Pi 5 Pro (SoC Rockchip RK3588S, NPU 6 TOPS, 8-core CPU)  
**Cảm biến hình ảnh:** Module Camera OV13855 (13MP MIPI-CSI)  
**Mã quyết định kỹ thuật:** `DEC-VIS-002` (Phê duyệt chính thức theo đề cương `LV1_11A2_12A1 ky.signed.pdf`)

---

## 1. MỤC TIÊU VÀ VAI TRÒ CỦA NHÁNH THỊ GIÁC

Khác với các hệ thống găng tay robot truyền thống vốn chỉ thụ động phản ứng lại sau khi người bệnh đã cử động tay, hệ thống tích hợp **thị giác không gian 3D đón trước (feedforward visual anticipation)**:

1. **Ước tính khoảng cách 3D thực tế (Metric Depth Estimation):**
   - Chạy mô hình mạng nơ-ron nền tảng **Depth Anything V2 (Metric Depth)** trực tiếp từ camera đơn RGB.
   - Xuất bản đồ độ sâu hệ mét 3D, tính toán khoảng cách không gian thực tế $d(t)$ (centimet) giữa đầu ngón tay người bệnh và vật thể mục tiêu (cán thìa).
2. **Dự đoán thời gian tới tiếp xúc (Time-to-Contact - TTC):**
   - Tính toán vận tốc tiếp cận $v(t) = \frac{\Delta d}{\Delta t}$ và thời gian tới va chạm $TTC(t) = \frac{d(t)}{v(t)}$.
   - Khi $TTC$ đạt ngưỡng quy định (ví dụ $0.3 - 0.5\text{ s}$ trước khi chạm thìa), hệ thống phát lệnh qua UART sang ESP32-S3 điều khiển servo mở ngón tay đón trước (feedforward aperture).
3. **Lượng hóa và giám sát tiến trình bài tập gắp thìa (Tripod Pinch Task):**
   - Nhận diện 4 pha bài tập: Tiếp cận (Reaching) $\to$ Kẹp giữ (Grasping) $\to$ Nhấc di chuyển (Transporting) $\to$ Đặt vào chén đích (Releasing).
   - Xuất dữ liệu trực quan lên màn hình Dashboard (Visual Biofeedback) giúp bệnh nhân quan sát quỹ đạo và điều chỉnh động tác.

---

## 2. RANH GIỚI AN TOÀN VÀ ĐIỀU PHỐI HỆ THỐNG

* **Tín hiệu thị giác chỉ dùng cho mở ngón đón trước và đánh giá tác vụ:** Tuyệt đối không bao giờ kích hoạt kẹp siết ngón tay chỉ dựa trên tín hiệu camera. Lệnh kẹp trợ lực chỉ được kích hoạt khi cả 2 điều kiện sau thỏa mãn:
  1. Cảm biến áp trở Velostat xác nhận có áp lực tiếp xúc vật thể.
  2. Cảm biến góc gập Flex Sensor xác nhận ngón tay đã bắt đầu cử động uốn cong theo ý muốn của người bệnh.
