# Báo cáo kỹ thuật: Tầng tiền khuếch đại INA333, ADC ADS1115 và ESP32-S3 cho cảm biến Velostat

## 1. Thiết kế tầng tiền khuếch đại INA333 (Module CJMCU-333)
* **Hệ số khuếch đại (Gain):** Được xác định theo công thức $G = 1 + \frac{100\text{ k}\Omega}{R_G}$. Biến trở SMD trên bo dùng để vi chỉnh $R_G$.
* **Xử lý điện áp phân cực chế độ chung ($V_{CM}$) và mốc DC ($V_{REF}$):**
  - Mạch hoạt động ở nguồn đơn (3.3V và GND). INA333 không thể xử lý hoặc xuất tín hiệu âm dưới 0V.
  - Chân VREF được duy trì ở mức $\approx 1.65\text{V}$ (half-supply) để thiết lập điểm tĩnh DC (baseline offset).
  - Tín hiệu ngõ ra chuẩn theo công thức: $V_{OUT} = G \cdot (V_{IN+} - V_{IN-}) + V_{REF}$.
  - Khi chưa có lực ép tác động, $V_{OUT}$ giữ cố định ở $\approx 1.500\text{ mV} - 1.650\text{ mV}$. Khi chịu lực ép, trở kháng Velostat giảm, kéo điện áp vi sai thay đổi và nâng $V_{OUT}$ một cách tuyến tính trong dải $0.1\text{V} - 3.2\text{V}$.

## 2. Ghép nối với bộ chuyển đổi tương tự - số (ADC) 16-bit ADS1115
* **Chế độ đọc:** Cấu hình kênh đơn A0 đọc ngõ ra $V_{OUT}$ từ INA333.
* **Tốc độ lấy mẫu & Chế độ hoạt động:** Cấu hình Continuous Conversion Mode đạt tốc độ tối đa $860\text{ SPS}$ ($860\text{ Hz}$).
* **Đồng bộ hóa ngắt phần cứng (Hardware Interrupt via ALRT Pin):**
  - Chân ALRT của ADS1115 kết nối với chân GPIO ngắt (GPIO 10) của ESP32-S3.
  - Sử dụng hàm `ads.startComparator_SingleEnded(0, 0)` trong thư viện Adafruit_ADS1X15 để kích hoạt chế độ Conversion Ready.
  - Mỗi khi hoàn tất chuyển đổi, ADS1115 phát xung hạ mức LOW kích hoạt ngắt phần cứng (Falling Edge ISR) trên ESP32-S3.
  - Triệt tiêu hoàn toàn hiện tượng jitter, trễ giao tiếp I2C và đảm bảo không bị rơi rụng mẫu (Zero stale/dropped samples).

## 3. Sơ đồ đấu nối phần cứng ESP32-S3 - INA333 - ADS1115
* **Nguồn:** Cấp 3.3V từ chân 3V3 của ESP32-S3 đồng thời vào chân 3.3V của INA333 và VDD của ADS1115 (chung GND toàn hệ thống).
* **I2C:** SDA -> GPIO 8, SCL -> GPIO 9, ADDR -> GND (địa chỉ 0x48).
* **Ngắt:** ALRT (ADS1115) -> GPIO 10 (ESP32-S3).
* **Tín hiệu:** VOUT (INA333) -> A0 (ADS1115).

## 4. Thuật toán phần mềm trên ESP32-S3: Tự động cân mốc 0 (Auto-Tare)
Để loại bỏ mức điện áp tĩnh DC ($V_{REF} \approx 1.5\text{V}$) khi chưa có lực tác động, hệ thống thực hiện Auto-Tare khi khởi động:
1. Cho mạch analog ổn định 500 ms.
2. Thu thập chính xác 100 mẫu liên tiếp qua ngắt phần cứng ALRT để tính trung bình cộng baseline:
   $$\text{Baseline} = \frac{1}{100} \sum_{i=1}^{100} V_i$$
3. Giá trị lực hiển thị tức thời:
   $$V_{\text{lực}} = V_{\text{đo}} - \text{Baseline}$$
Tín hiệu sau Tare bắt đầu từ đúng $0.0\text{ mV}$, giúp tối ưu hóa dải đo và hỗ trợ các thuật toán nhận diện mẫu lực ép tay phục hồi chức năng sau đó.
