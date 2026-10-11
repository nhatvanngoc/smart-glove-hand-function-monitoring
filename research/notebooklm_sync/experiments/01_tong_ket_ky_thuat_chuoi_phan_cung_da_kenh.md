# Tổng kết kỹ thuật toàn diện: Kiểm thử và xác thực chuỗi phần cứng đa kênh
(ESP32-S3 + ADS1115 + INA333 + CD74HC4067)

## 1. Mục tiêu thử nghiệm
Xác thực toàn bộ chuỗi phần cứng thu thập và tiền xử lý tín hiệu cho mảng cảm biến áp lực bàn tay trong dự án găng tay robot phục hồi chức năng:
`Tín hiệu đầu vào -> MUX 16 kênh CD74HC4067 -> Tầng khuếch đại đo lường INA333 (CJMCU-333) -> Bộ biến đổi tương tự - số ADC 16-bit ADS1115 -> Vi điều khiển ESP32-S3 (qua I2C & Serial Plotter)`.

## 2. Các mốc giải quyết bài toán phần cứng (Milestones)

### 2.1. Cân chỉnh tầng tiền khuếch đại INA333
* **Hiện tượng lỗi ban đầu:** Sóng ngõ ra bị suy hao biên độ ($V_{pp}$ vào 0.25V, ra 0.16V), méo nấc bậc thang, bẹp đáy (xén âm xuống -0.85V) do INA333 chạy nguồn đơn 3.3V bị vi phạm dải điện áp chế độ chung ($V_{CM}$) và thiếu mốc tham chiếu tĩnh $V_{REF}$.
* **Xử lý:**
  - Thêm tụ chặn AC 0.47 µF ngăn dòng DC rò từ nguồn phát xung.
  - Thiết lập điểm tĩnh DC $V_{REF} \approx 1.500\text{ mV} - 1.650\text{ mV}$ (Virtual Ground) tại ngõ vào vi sai.
  - Cân chỉnh biến trở SMD $R_G$ (loại 1 vòng xoay 270°): Đạt hệ số khuếch đại $G \approx 6.5$ lần ($V_{pp}$ đạt 1.55V, $V_{max} = 1.62\text{V}$, $V_{min} = 0.06\text{V}$ cách sàn GND an toàn, sóng sin tròn đều).
  - Khi tắt nguồn phát AC, $V_{OUT}$ giữ cố định tại $\approx 1.500\text{ mV}$ (chuẩn xác theo mốc tĩnh thiết kế).

### 2.2. Tích hợp và cấu hình ADC 16-bit ADS1115
* **Lựa chọn cấu hình:** Sử dụng kênh đơn $A_0$ đọc trực tiếp $V_{OUT}$ từ INA333; chân $A_1$ để trống để tránh sụt áp mốc $V_{REF}$ tĩnh trên bo mạch.
* **Tối ưu chế độ đọc:** Khảo sát chế độ Continuous Conversion kết hợp ngắt phần cứng ALRT (Conversion Ready) trên GPIO 10 ESP32-S3 và cơ chế đọc tuần tự đa kênh qua I2C 400kHz.

### 2.3. Mở rộng đa kênh với CD74HC4067
* **Kết nối điều khiển:** 4 chân GPIO (GPIO 4, 5, 6, 7) điều khiển chọn kênh $S_0 - S_3$, chân EN nối GND kích hoạt liên tục.
* **Tối ưu tốc độ & Settling Time:** Chèn khoảng trễ xác lập điện áp `delayMicroseconds(120)` sau mỗi lần chuyển kênh để xả sạch điện dung ký sinh trên chân SIG, ngăn ngừa hiện tượng nhớ áp giữa các kênh.
* **Kết quả đo kiểm trên Serial Plotter:**
  - Kênh 0 (GND): Ghim phẳng tuyệt đối tại $\approx 0 - 20\text{ mV}$.
  - Kênh 1: Duy trì áp tĩnh cao ổn định tại $\approx 3.046\text{ mV} - 3.100\text{ mV}$.
  - Kênh 2: Bắt trọn dao động tuần hoàn từ 150 mV lên đỉnh 1.650 mV; khi ngắt nguồn phát, kênh lùi về mốc tĩnh đáy $\approx 150\text{ mV}$ dứt khoát.
  - Khả năng cách ly: Không xảy ra hiện tượng rò kênh hay nhiễu xuyên kênh (Crosstalk) giữa các kênh có độ lệch áp lớn (0V, 1.65V, 3.0V).

## 3. Bản chất hiện tượng "Sóng tam giác" trên Serial Plotter
* **Nguyên nhân:** Do phần mềm hiển thị nối các điểm rời rạc bằng đoạn thẳng (Linear Interpolation). Vì ADC phải chia thời gian quét tuần tự qua 4 kênh, số lượng mẫu thu thập trên mỗi chu kỳ sin của máy phát xung chỉ đạt từ 4 đến 6 điểm.
* **Đánh giá mức độ ảnh hưởng:** Hoàn toàn KHÔNG ảnh hưởng đến hệ thống thực tế. Cảm biến màng Velostat là tín hiệu điện trở DC biến thiên chậm theo lực tì/ép của ngón tay người ($0\text{ Hz} - 3\text{ Hz}$), thời gian thao tác kéo dài hàng trăm mili-giây nên mật độ lấy mẫu trên mỗi thao tác là rất dày đặc (hàng chục đến hàng trăm mẫu), cho ra đường đáp ứng lực trơn mượt tự nhiên.

## 4. Trạng thái hệ thống và Kế hoạch bước tiếp theo
* **Trạng thái:** Toàn bộ chuỗi phần cứng và firmware cơ sở đã hoàn thành kiểm chứng, độ tuyến tính và dải động đạt yêu cầu ($0\text{ mV} - 3250\text{ mV}$).
* **Bước kế tiếp:**
  - Tháo nguồn phát xung và tụ lọc AC 0.47 µF ra khỏi bo mạch.
  - Đấu nối các điểm cảm biến màng Velostat (theo cấu hình cầu phân áp) vào các cổng ngõ vào $C_0 - C_{15}$ của CD74HC4067.
  - Kích hoạt lại thuật toán Auto-Tare để tự động đưa mốc lực ban đầu của từng ngón tay về chuẩn $0.0\text{ mV}$.
