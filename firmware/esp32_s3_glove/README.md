# FIRMWARE ESP32-S3: HỆ THỐNG THU THẬP 21 KÊNH, LỌC SỐ DSP VÀ ĐIỀU KHIỂN TRỢ LỰC AAN
**Vi điều khiển:** ESP32-S3 Dual-Core Xtensa LX7 @ 240MHz  
**Phiên bản cấu hình:** Vòng lặp phát triển 3 (Phê duyệt theo đề cương `LV1_11A2_12A1 ky.signed.pdf`)

---

## 1. CẤU TRÚC PHẦN MỀM NHÚNG

Firmware chạy trên nền tảng ESP-IDF / Arduino-ESP32 với FreeRTOS đa nhiệm:

* **Task 1: Sensor_Acquisition_Task (Core 0, Priority 5, Chu kỳ 30 Hz / 33 ms):**
  - Quét tuần tự 21 kênh tương tự qua 2 bộ MUX 16:1 CD74HC4067 (16 ô Velostat + 3 Flex Sensor ZD10-100 + 2 REF).
  - Trích mẫu qua ADC 16-bit ADS1115 (giao tiếp I2C 400kHz), áp dụng settling delay 300 µs và cơ chế đọc nháp xả dung kháng ký sinh.
* **Task 2: DSP_Processing_Task (Core 0, Priority 4):**
  - **Nhánh Velostat:** Lọc trung vị 3 mẫu $\to$ Lọc IIR thông thấp $f_c = 8\text{ Hz}$ $\to$ Bám đường nền động (Moving baseline tracking) $\to$ Áp vùng chết ngưỡng tiếp xúc để triệt tiêu trôi tĩnh.
  - **Nhánh Flex Sensor:** Lọc trung bình trượt 5 mẫu $\to$ Hàm truyền tuyến tính $V_{ADC} \to \theta^\circ$ (góc uốn liên đốt). Tuyệt đối không áp vùng chết của Velostat.
  - Tính toán bộ ba chỉ số: Chỉ số nỗ lực **EI**, Độ hụt tầm vận động **GAP**, Mức trợ lực cần thiết **RAL**.
* **Task 3: Motor_Control_Task (Core 1, Priority 5, Chu kỳ 20 ms / 50 Hz):**
  - Máy trạng thái 3 pha: Nghỉ (Idle) $\to$ Phát hiện nỗ lực (Effort Detection) $\to$ Trợ lực theo nhu cầu (AAN Action).
  - Xuất 3 kênh tín hiệu PWM điều khiển 3 động cơ servo MG90S kéo/nhả cáp Bowden độc lập.
* **Task 4: Telemetry_Task (Core 1, Priority 2):**
  - Giao tiếp UART tốc độ cao (115200 / 921600 bps) với máy tính nhúng Orange Pi 5 Pro.
  - Nhận nhãn dự đoán thời gian tới tiếp xúc (TTC) và lệnh mở ngón đón trước từ thị giác máy tính Depth Anything V2.
