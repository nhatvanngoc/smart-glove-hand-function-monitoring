# Nhật ký thực nghiệm: Đo kiểm INA333, Cấu hình ADS1115 và Thiết kế chuỗi đa kênh CD74HC4067

## 1. Kết quả đo kiểm và giải quyết bài toán tiền khuếch đại INA333 (CJMCU-333)
* **Thiết bị đo kiểm:** Máy hiện sóng cầm tay tích hợp FNIRSI 2C23T.
* **Hiện tượng lỗi ban đầu:**
  - Tín hiệu ngõ ra bị suy hao ($V_{pp}$ vào $0.25\text{V} \to$ ngõ ra chỉ đạt $0.16\text{V}$, tương đương $G \approx 0.64$).
  - Dạng sóng ngõ ra bị méo nấc bậc thang, bẹp đáy (clipping âm xuống $-0.85\text{V}$).
  - Hiện tượng sập nguồn tức thời khi kẹp mass oscillo: do vỏ mass cổng BNC của FNIRSI thông ngầm, gây đoản mạch vòng mass (Ground Loop) khi kẹp vào điểm lệch thế.
* **Bản chất kỹ thuật & Giải pháp:**
  - INA333 chạy nguồn đơn 3.3V và GND (0V), không thể xử lý điện áp âm. Tín hiệu AC từ máy phát xung tụt dưới 0V kích hoạt diode bảo vệ ESD nội, làm tắc nghẽn tầng vi sai.
  - Bổ sung tụ chặn AC 0.47 µF để ngăn dòng một chiều từ nguồn phát.
  - Ghim điện áp phân cực DC tĩnh $V_{REF} \approx 1.5\text{V} - 1.65\text{V}$ (Virtual Ground) vào ngõ vào vi sai.
  - Tinh chỉnh biến trở SMD $R_G$ (loại 1 vòng xoay 270°): Hệ số khuếch đại đạt $G \approx 6.5$ lần ($V_{pp}$ từ 0.24V khuếch đại lên 1.55V), sóng sin trơn mượt, đáy sóng cách GND 60 mV, không còn hiện tượng xén ngọn.
  - Khi tắt máy phát xung AC, $V_{OUT}$ giữ cố định ở $\approx 1.500\text{ mV}$ (chuẩn xác theo mốc $V_{REF}$ tĩnh thiết kế).

## 2. Tối ưu hóa chuỗi chuyển đổi ADC 16-bit ADS1115 với ESP32-S3
* **Lý do phần cứng:** Thay thế ADC nội bộ của ESP32-S3 (vốn bị lỗi phi tuyến nặng ở 2 biên và nhiễu sóng RF) bằng ADS1115 qua I2C.
* **Cấu hình Continuous Conversion Mode & Ngắt phần cứng ALRT:**
  - Tốc độ lấy mẫu: Đặt tối đa 860 SPS (Samples Per Second).
  - Sử dụng chân ngắt phần cứng ALRT của ADS1115 nối vào GPIO 10 (ESP32-S3).
  - Kích hoạt chế độ Conversion Ready bằng hàm `ads.startComparator_SingleEnded(0, 0)` trong thư viện Adafruit_ADS1X15 mới.
  - Phục vụ ngắt sườn xuống (FALLING) lưu trong RAM (IRAM_ATTR): ESP32-S3 chỉ đọc dữ liệu khi phần cứng ADS1115 hoàn tất chuyển đổi (< 0.1 ms).
  - Loại bỏ hoàn toàn trễ giao tiếp I2C, triệt tiêu hiện tượng jitter thời gian thực và tránh đọc trùng/rớt mẫu (Zero Stale Data).

## 3. Kiến trúc chuỗi tín hiệu và Kế hoạch kế tiếp
* Khảo sát phương án: Quét 16 kênh cảm biến -> CD74HC4067 (chọn 1 kênh) -> 1 tầng INA333 -> ADS1115 (A0) -> ESP32-S3. Nội trở dẫn tiếp điểm $R_{ON} \approx 70\,\Omega$ của 4067 không ảnh hưởng đến INA333 do trở kháng ngõ vào của INA333 lên tới $100\text{ G}\Omega$.
* Kiểm soát Settling Time và Crosstalk giữa các đường tín hiệu.
