# BẢNG ĐỊNH MỨC VẬT TƯ VÀ LINH KIỆN PHẦN CỨNG CHÍNH THỨC (BOM)
**Dự án:** Nghiên cứu và phát triển găng tay hỗ trợ đánh giá, theo dõi và hỗ trợ vận động bàn tay trong phục hồi chức năng sau đột quỵ  
**Mã quyết định kỹ thuật:** `DEC-HW-008` (Chính thức phê duyệt ngày 24/10/2026)  
**Căn cứ phê duyệt:** Bản đề cương nghiên cứu khoa học kỹ thuật đã ký duyệt `LV1_11A2_12A1 ky.signed.pdf`

---

## 1. DANH MỤC LINH KIỆN ĐÃ CHỐT CHÍNH THỨC

| STT | Tên linh kiện / Mô-đun | Mã hiệu / Quy cách kỹ thuật | Số lượng | Vị trí lắp đặt | Vai trò & Thông số kỹ thuật cốt lõi | Tình trạng |
|:---:|:---|:---|:---:|:---:|:---|:---:|
| 1 | **Cảm biến uốn cong (Flex Sensor)** | **ZD10-100** (Dài 100 mm) | 3 | Dọc mặt mu 3 ngón tay (Cái, Trỏ, Giữa) | Cảm biến màng nano trở áp uốn cong, độ mỏng <0.25 mm, độ bền >1.000.000 chu kỳ. Điện trở giảm từ >10 MΩ (thẳng) về 20–50 kΩ (gập 90°). Dùng cầu phân áp trở chuẩn $R_{ref} = 47\text{ k}\Omega - 100\text{ k}\Omega$ để đo trực tiếp góc gập liên đốt ($\theta^\circ$). | Đã chốt mua mốc 1 |
| 2 | **Cảm biến áp trở màng mỏng** | **Velostat (3M)** vi sai hai mặt | 16 ô + 2 REF | Mặt lòng & mặt mu 3 ngón | Màng polymer dẫn điện nhạy áp lực; bố trí đối xứng lòng-mu để tự triệt tiêu biến dạng nẹp, phân biệt nỗ lực co cơ với lực tì đè thụ động. 2 ô REF đặt trong vỏ cách ly để bù trôi môi trường. | Đã có sẵn |
| 3 | **Động cơ trợ lực ngón (Servo)** | **TowerPro MG90S** (Bánh răng kim loại) | 3 | Cụm nẹp mu bàn tay | Khối lượng 13.4g, kích thước $22.8 \times 12.2 \times 28.5\text{ mm}$, mô-men xoắn $1.8 - 2.2\text{ kg}\cdot\text{cm}$ (ở 4.8–6V). Tang cuốn cáp $D = 14\text{ mm}$ sinh lực kéo ~25 N đáp ứng lực trợ gập ngón. Bánh răng đồng/thép chịu tải cao, không trượt răng. | Đã có sẵn |
| 4 | **Dây truyền động lực** | Dây cáp bện siêu bền Dyneema / Bowden | 1 bộ | Dọc sống lưng nẹp 3 ngón | Dây cáp chịu lực kéo $\ge 150\text{ N}$, trượt êm trong ống dẫn Teflon PTFE, ma sát cực thấp, truyền động từ tang cuốn servo tới các đốt ngón. | Đã có sẵn |
| 5 | **Bộ ghép kênh tương tự (Multiplexer)** | **CD74HC4067** (16:1 MUX) | 2 | Cụm nẹp mu bàn tay | Quét tuần tự 21 kênh tương tự (16 Velostat + 3 Flex + 2 REF) về 1 kênh ADC, tiết kiệm chân vi điều khiển và giảm số lượng dây dẫn về hộp trung tâm. | Đã có sẵn |
| 6 | **Bộ chuyển đổi ADC độ chính xác cao** | **ADS1115** (16-bit Delta-Sigma ADC) | 1 | Bo mạch điều khiển | Độ phân giải 16-bit, giao tiếp I2C tốc độ cao (400 kHz), dải điện áp đo $0 - 3.3\text{ V}$, loại bỏ hiện tượng phi tuyến của ADC nội vi điều khiển. | Đã có sẵn |
| 7 | **Vi điều khiển thời gian thực** | **ESP32-S3** (Dual-core Xtensa 240MHz) | 1 | Hộp đai hông | Thực thi thuật toán DSP 2 nhánh (bám nền động Velostat + ánh xạ góc liên tục Flex), tính toán bộ ba chỉ số EI – GAP – RAL và điều khiển 3 kênh PWM servo trong vòng lặp $\le 20\text{ ms}$. | Đã có sẵn |
| 8 | **Máy tính nhúng xử lý thị giác** | **Orange Pi 5 Pro** (Rockchip RK3588S) | 1 | Hộp đai hông | Chạy mô hình mạng nơ-ron nền tảng **Depth Anything V2 (Metric Depth)**, xử lý bản đồ độ sâu 3D hệ mét thời gian thực, tính thời gian tới tiếp xúc (TTC) và giám sát tiến trình bài tập gắp thìa. | Đã có sẵn |
| 9 | **Cảm biến hình ảnh (Camera)** | **OV13855** (13 Megapixel MIPI-CSI) | 1 | Khung giá đỡ quan sát bài tập | Cảm biến 13MP kết nối trực tiếp qua cổng MIPI-CSI băng thông cao của Orange Pi 5 Pro, cung cấp khung hình RGB độ phân giải cao phục vụ ước lượng độ sâu 3D. | Đã chốt mua mốc 1 |
| 10 | **Khối nguồn lưu động** | **Bộ Pin Li-ion 2S 18650** (7.4V / 2600mAh) | 1 bộ (2 cell) | Hộp đai hông | Cung cấp năng lượng độc lập toàn hệ thống trong thời gian $\ge 2\text{ giờ}$ liên tục, có mạch bảo vệ xả/quá dòng BMS 2S. | Đã có sẵn |
| 11 | **Mạch hạ áp xung công suất (Buck)** | **XL4005** (5A / 75W DC-DC Step-Down) | 1 | Hộp đai hông | Hạ áp từ 7.4V (Pin 2S) xuống 5.0V ổn định, cấp dòng tải đỉnh lên tới 5A cho 3 động cơ servo MG90S và bo mạch Orange Pi 5 Pro, chống sụt áp nguồn xung. | Đã có sẵn |
| 12 | **Cáp kết nối mềm liên cụm** | Bó cáp mềm bọc dù chịu uốn (Chiều dài 50 cm) | 1 sợi | Nối cẳng tay về đai hông | Chứa các đường tín hiệu I2C/SPI/PWM và đường nguồn DC, bọc lớp giáp mềm linh hoạt, không cản trở cử động tay của người bệnh. | Đã có sẵn |

---

## 2. NGUYÊN TẮC QUẢN LÝ VÀ KIỂM CHUẨN VẬT TƯ

1. **Kiểm tra xuất xứ và sai số danh định:** Toàn bộ cảm biến và linh kiện điện tử trước khi hàn lắp vào bo mạch chính thức đều phải qua bước đo kiểm điện trở tĩnh, dòng rò và độ gợn điện áp bằng máy hiện sóng FNIRSI 2C23T.
2. **Nguyên tắc bảo vệ linh kiện:** Các mạch nguồn và vi điều khiển bắt buộc có cầu chì tự phục hồi (PTC) và diode bảo vệ chống cắm ngược cực; đường nguồn cho servo tách riêng cuộn lọc để tránh xung nhiễu motor phản hồi về đường nguồn số.
