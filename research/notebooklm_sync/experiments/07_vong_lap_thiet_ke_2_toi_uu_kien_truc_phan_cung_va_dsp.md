# Nhật ký thử nghiệm phần cứng #02 — Ngày 15/10/2026

**Phân hệ:** Mạch thu thập tín hiệu cảm biến lực & góc khớp  
**Mục tiêu đo kiểm:** Đo kiểm tra độ trễ và nhiễu của chuỗi mạch CD74HC4067 -> INA333 -> ADS1115 -> ESP32-S3 bằng cách so sánh trực tiếp dạng sóng trên máy hiện sóng FNIRSI 2C23T (CH1, CH2) với dữ liệu đọc về qua cổng USB Serial Plotter.

---

## I. Cấu tạo cụm cảm biến trên đốt ngón tay

* **Vị trí lắp đặt:** Mỗi đốt ngón tay trên khung nẹp in 3D được bố trí 2 cụm cảm biến đối xứng tại mặt lòng (kênh C0) và mặt mu (kênh C1).
* **Cấu trúc điện cực:** Kẹp màng Velostat ở giữa 2 lớp dây đồng mạ niken (cố định trên khung in 3D ở mặt lòng C0 và mặt mu C1). Chọn dây mạ niken thay vì đồng trần để tránh mặt đồng bị xỉn màu hoặc oxy hóa khi tiếp xúc với lớp carbon của Velostat, giúp hạn chế hiện tượng trôi điện trở nền R0 sau vài ngày đo.
* **Mạch phân áp:** Mỗi màng cảm biến mắc nối tiếp với một điện trở kéo lên 10 kΩ lên nguồn 3.3V của ESP32-S3.

---

## II. Kết quả đo kiểm và lý do thay đổi kiến trúc mạch đo

| Nội dung so sánh | Mạch ban đầu (dùng tầng khuếch đại INA333, G ≈ 6.5) | Mạch cải tiến (đo trực tiếp qua ADS1115) | Hiện tượng thực tế trên bàn đo |
|---|---|---|---|
| **Dải điện áp của màng Velostat** | Đo được biên độ biến thiên rất lớn từ 2.5V xuống 0.3V khi bóp chặt (chênh lệch > 1800 mV). | Thu nhận trọn vẹn dải điện áp từ 0V đến 3.3V. | Màng Velostat có độ nhạy áp trở lớn, điện trở tụt từ hàng chục kΩ xuống vài trăm Ω khi có lực ép, tín hiệu đủ lớn nên không cần tầng tiền khuếch đại vi sai. |
| **Cửa sổ điện áp tuyến tính** | Dải đo hiệu dụng rất hẹp quanh mốc 1.68V (từ 1.44V đến 1.92V). | Toàn dải từ 0.000V đến 3.300V (bước lượng tử 0.125 mV ở dải đo ±4.096V của ADS1115). | Khi siết ốc cố định khung nẹp vào ngón tay, lực nén cơ khí ban đầu làm điện áp tĩnh rơi xuống dưới 1.42V. Khi ngón tay gập nhẹ, INA333 lập tức chạm ngưỡng bão hòa và đồ thị Serial Plotter bị kẹt cứng ở mức khoảng 2838 mV. |
| **Nhiễu nền và độ trôi** | Nhiễu nền 50 - 135 mV bị khuếch đại lên hơn 6 lần cùng tín hiệu. | Giữ nguyên biên độ nhiễu gốc 50 - 135 mV, xử lý triệt để bằng phần mềm. | Bớt 1 IC khuếch đại tương tự giúp giảm nhiễu nhiệt nội bộ, bớt linh kiện hàn trên bo mạch và giảm dòng tiêu thụ của găng tay. |

---

## III. Xử lý tín hiệu số trên vi điều khiển ESP32-S3

Để lọc dải nhiễu nền và hiện tượng trôi mốc tĩnh do tính chất đàn hồi trễ của màng polymer Velostat:

### Bước 1: Đọc nháp và trễ xác lập 300 µs
Sau khi chuyển kênh MUX qua các chân điều khiển S0 - S3, chương trình chờ 300 µs và thực hiện một lần đọc nháp trước khi lấy mẫu chính thức nhằm xả hết điện tích ký sinh trên đường dẫn. Cách này giúp triệt tiêu hiện tượng đọc lẫn tín hiệu giữa kênh mặt lòng C0 và kênh mặt mu C1.

### Bước 2: Khóa vùng chết trừ tuyến tính (ngưỡng 180 mV)
$$F_{clean} = \max\left(0.0, \; \vert{}V_{base} - V_{raw}\vert{} - 180\text{ mV}\right)$$
Khi ngón tay thả lỏng, điện áp dao động nhỏ dưới 180 mV được ghim về đúng 0.0 mV. Khi lực ép vượt ngưỡng, tín hiệu tăng tuyến tính liên tục bắt đầu từ mốc 0.

### Bước 3: Tự động bám mốc tĩnh bù trôi nhiệt
Khi ngón tay ở trạng thái nghỉ thả lỏng (độ lệch dưới 180 mV), mốc điện áp tĩnh được cập nhật chậm theo bộ lọc số:
$$V_{base}[k] = 0.998 \cdot V_{base}[k-1] + 0.002 \cdot V_{raw}[k]$$
Cơ chế này giúp hệ thống tự động bù trừ sự co giãn nhẹ của khung nhựa in 3D và nhiệt độ bàn tay truyền vào cảm biến theo thời gian.

### Bước 4: Lọc trung bình động EMA và tính vi sai gập duỗi
Làm mịn đường tín hiệu bằng bộ lọc EMA với hệ số 0.20:
$$F_{filtered}[k] = 0.20 \cdot F_{clean}[k] + 0.80 \cdot F_{filtered}[k-1]$$
Tổng hợp lực vi sai giữa hai mặt đốt ngón:
$$F_{net} = F_{long(C0)} - F_{mu(C1)}$$
* Nếu $F_{net} > 0$: ngón tay đang kích hoạt cơ gập.
* Nếu $F_{net} < 0$: ngón tay đang kích hoạt cơ duỗi.
* Nếu $F_{net} \approx 0$: ngón tay đang ở trạng thái thả lỏng hoặc lực hai mặt cân bằng.

---

## IV. Kết luận phiên thử nghiệm và việc cần làm tiếp

1. Việc bỏ tầng khuếch đại INA333 và nối trực tiếp cảm biến vào ADS1115 đã loại bỏ hoàn toàn hiện tượng kẹt áp bão hòa ở mức 2.8V, mở rộng cửa sổ đo bao trọn dải biến thiên 0V - 3.3V khi gập duỗi ngón tay.
2. Thuật toán lọc số 4 bước chạy tốt trên ESP32-S3, đưa giá trị tĩnh khi thả lỏng về ổn định tại 0 mV và phân tách rõ ràng hướng lực gập/duỗi.
3. Việc cần làm tiếp: Tiếp tục lắp ráp cảm biến lên các đốt ngón tay còn lại trên khung in 3D và theo dõi độ ổn định tín hiệu liên tục trong phiên đo 30 phút.
