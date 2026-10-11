# Báo cáo thực nghiệm: Quét đa kênh CD74HC4067 kết hợp INA333 và ADS1115

## 1. Kết quả kiểm tra trên Serial Plotter
* **Hệ thống phần cứng:** ESP32-S3 điều khiển chuyển kênh CD74HC4067 ($S_0 - S_3$), tín hiệu sau dồn kênh đưa vào tầng khuếch đại vi sai INA333, chuyển đổi ADC 16-bit qua ADS1115 (giao tiếp I2C 400kHz, kênh đơn A0).
* **Hiện trạng các kênh:**
  - Kênh 0 (Xanh dương): Nối cố định GND -> Điện áp hiển thị phẳng tuyệt đối tại $0\text{ mV}$. Hoàn toàn không bị dính nhiễu từ các kênh lân cận.
  - Kênh 2 (Xanh lá): Dao động tuần hoàn từ $\approx 600\text{ mV}$ lên kịch trần nguồn $3250\text{ mV}$ ($3.25\text{V}$, tương đương thanh nguồn Rail-to-Rail của INA333 và ADS1115 ở mức nguồn 3.3V).
  - Kênh 1 (Cam): Dao động tuần hoàn từ $0\text{ mV}$ lên đỉnh $\approx 1700\text{ mV}$ ($1.7\text{V}$).
  - Đồ thị xuất hiện dạng zíc-zắc gãy khúc do tốc độ lấy mẫu trên mỗi kênh bị chia 4 (quét tuần tự qua 4 kênh kèm thời gian trễ delay).

## 2. Kết luận kỹ thuật
* Bộ dồn kênh tương tự CD74HC4067 hoạt động chính xác: chuyển mạch đúng địa chỉ, cách ly kênh tốt, không xảy ra hiện tượng rò kênh sang Kênh 0.
* Chuỗi tín hiệu Analog -> Multiplexer -> Instrumentation Amplifier -> ADC 16-bit I2C -> ESP32-S3 đã thông suốt hoàn toàn về mặt phần cứng và firmware.
