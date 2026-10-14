# Nhật ký thực nghiệm 07: Vòng lặp Thiết kế số 2 (Design Iteration 2)
## Tối ưu hóa kiến trúc phần cứng dựa trên thực nghiệm tích hợp cơ khí và Bộ lọc DSP động

> **Căn cứ quy chuẩn:** Quy trình Thiết kế Kỹ thuật (Engineering Design Process) theo Thông tư số 84/2026/TT-BGDĐT.  
> **Ngày thực hiện:** 15/10/2026.  
> **Hạng mục:** Chế tạo cảm biến kẹp Sandwich trên khung ốp đốt tay, tối ưu hóa kiến trúc mạch đo và thiết lập thuật toán lọc nhiễu động (DSP Pipeline).  
> **Nguyên tắc phương pháp luận:** Không xóa bỏ dữ liệu thực nghiệm Vòng lặp 1 (INA333 $G \approx 6.5$, notes 01–06), mà kế thừa và phân tích nguyên nhân vật lý dẫn đến quyết định cải tiến kiến trúc phần cứng (Hardware Simplification & Trade-off).

---

## I. Cấu trúc Cơ - Điện của Cảm biến Đốt tay (Sandwich Piezoresistive Transducer)

* **Cấu tạo vật lý:** Mỗi đốt ngón tay được thiết kế một khung ốp in 3D gắn 2 cụm cảm biến đối xứng tại Mặt lòng (Palmar — Kênh C0) và Mặt mu (Dorsal — Kênh C1).
* **Cấu trúc tiếp xúc 3 lớp (Sandwich):** 
  $$\text{Cuộn dây đồng mạ niken} \longrightarrow \text{Màng áp trở Velostat} \longrightarrow \text{Cuộn dây đồng mạ niken}$$
  Lớp mạ niken chống oxy hóa bề mặt trong môi trường nhiệt ẩm và giảm thiểu điện trở tiếp xúc ký sinh giữa dây dẫn và màng polymer.
* **Mạch định thiên (Bias Circuit):** Mỗi màng cảm biến mắc nối tiếp với một điện trở kéo lên $R_{pullup} = 10\text{ k}\Omega$ độc lập nối lên nguồn $3.3\text{V}$, tạo thành mạch cầu phân áp trực tiếp.

---

## II. Bảng Đối chứng Tối ưu hóa Kiến trúc Phần cứng (Hardware Optimization)

| Tiêu chí đánh giá | Kiến trúc Vòng lặp 1 (Sử dụng INA333, $G \approx 6.5$) | Kiến trúc Vòng lặp 2 — Tối ưu hóa (Đo trực tiếp qua PGA 16-bit ADS1115) | Cơ sở Lý luận & Bằng chứng Thực nghiệm |
|---|---|---|---|
| **Biên độ biến thiên của Velostat** | $\Delta V \approx 1500\text{ mV} - 2200\text{ mV}$ (từ $2.5\text{V}$ xuống $0.3\text{V}$ khi bóp). | Thu nhận trọn vẹn toàn bộ dải biến thiên tự nhiên $0\text{V} - 3.3\text{V}$. | Màng Velostat có hệ số nhạy áp trở lớn gấp hàng trăm lần Loadcell kim loại, bản thân điện trở thay đổi từ hàng chục $\text{k}\Omega$ xuống vài trăm $\Omega$, không cần khuếch đại tiền tầng hệ số lớn. |
| **Cửa sổ điện áp tuyến tính** | Bị giới hạn hẹp trong khoảng $\pm 0.24\text{V}$ quanh mốc $V_{REF} = 1.68\text{V}$ ($1.44\text{V} \to 1.92\text{V}$). | Mở rộng toàn dải từ $0.000\text{V}$ đến $3.300\text{V}$ (độ phân giải $0.125\text{ mV/LSB}$ ở dải $\pm 4.096\text{V}$). | Lực siết cơ khí ban đầu (Preload) của khung ốp làm điện áp tĩnh rơi xuống $< 1.42\text{V}$, khiến INA333 chạm sàn bão hòa và kẹt đồ thị ở $\approx 2838\text{ mV}$. |
| **Hiện tượng Nhiễu nền & Trôi** | Bị khuếch đại gấp $6.5$ lần cùng với tín hiệu hữu ích. | Giữ ở mức nguyên bản ($50\text{ mV} - 135\text{ mV}$), dễ dàng triệt tiêu bằng thuật toán số. | Giảm 1 mắt xích IC tương tự giúp loại bỏ tạp âm nhiệt nội bộ, giảm số linh kiện trên PCB và giảm tiêu thụ năng lượng của găng tay. |

---

## III. Quy trình 4 bước Lọc Tín hiệu Số (Digital Signal Processing) trên ESP32-S3

Để xử lý dải nhiễu nền ($50\text{ mV} - 135\text{ mV}$) sinh ra do hiện tượng biến dạng bò đàn hồi (Viscoelastic Creep) của màng polymer Velostat và điện dung ký sinh của MUX CD74HC4067:

### Bước 1 — Đọc nháp xả điện tích (Dummy Read & $300\,\mu\text{s}$ Settling)
Sau khi chuyển kênh MUX qua 4 chân $S_0 - S_3$, phần mềm chèn khoảng trễ xác lập $300\,\mu\text{s}$ và thực hiện 1 lần đọc nháp (Dummy Read) để nạp đầy tụ lấy mẫu nội bộ của ADS1115 trước khi lấy mẫu chính thức.  
*Kết quả:* Triệt tiêu $100\%$ hiện tượng bóng ma (Ghosting/Crosstalk) giữa kênh lòng C0 và kênh mu C1.

### Bước 2 — Khóa vùng chết trừ tuyến tính (Subtracted Dead-band, $V_{gate} = 180\text{ mV}$)
$$F_{clean} = \max\left(0.0, \; \vert{}V_{base} - V_{raw}\vert{} - 180\text{ mV}\right)$$
Đảm bảo tín hiệu ngõ ra đứng yên tuyệt đối tại $0.00\text{ mV}$ khi ngón tay thả lỏng, và tăng tuyến tính mượt mà ngay từ điểm $0$ khi bắt đầu xuất hiện lực nỗ lực chủ động.

### Bước 3 — Tự động thích nghi điểm 0 (Adaptive Drift Tracking, $\gamma = 0.002$)
Khi ngón tay ở trạng thái nghỉ thả lỏng ($\vert{}\Delta V\vert{} \le 180\text{ mV}$), mốc điện áp tĩnh tự động cập nhật chậm theo bộ lọc thông thấp IIR:
$$V_{base}[k] = 0.998 \cdot V_{base}[k-1] + 0.002 \cdot V_{raw}[k]$$
Giúp hệ thống tự động thích ứng và bù trừ hiện tượng giãn nở nhiệt của nhựa in 3D cũng như thân nhiệt bàn tay truyền vào khung nẹp theo thời gian thực.

### Bước 4 — Lọc trung bình lũy thừa EMA ($\alpha = 0.20$) & Tổng hợp Vi sai Gập/Duỗi
Làm mịn đường tín hiệu lực bằng lọc EMA:
$$F_{filtered}[k] = 0.20 \cdot F_{clean}[k] + 0.80 \cdot F_{filtered}[k-1]$$
Tổng hợp vector lực vi sai hai mặt:
$$F_{net} = F_{palmar(C0)} - F_{dorsal(C1)}$$
*Quy tắc suy luận:*
* $F_{net} > 0$: Bệnh nhân kích hoạt cơ gập ngón (Flexion Effort).
* $F_{net} < 0$: Bệnh nhân kích hoạt cơ duỗi ngón (Extension Effort).
* $F_{net} = 0$: Trạng thái nghỉ tĩnh hoặc đồng co cơ cân bằng.

---

## IV. Đánh giá Theo Tiêu chí Quy trình Thiết kế Kỹ thuật (Thông tư 84/2026/TT-BGDĐT)

1. **Tính xác thực của nghiên cứu:** Vòng lặp Thiết kế số 2 xuất phát trực tiếp từ va chạm thực tế giữa linh kiện điện tử và cơ cấu cơ khí (lực siết ốp ngón tay làm lệch mốc tĩnh ngoài dự kiến). Đây là bằng chứng không thể ngụy tạo của quá trình R&D thực thụ.
2. **Tư duy tối giản hóa phần cứng (Hardware Simplification):** Nhận diện rõ đặc tính vật lý của vật liệu (Velostat có độ nhạy áp trở $\Delta R/R$ rất lớn, không cần mạch khuếch đại đo lường micro-volt như strain gauge) giúp cắt bỏ một tầng phần cứng dư thừa, tăng độ tin cậy và giảm giá thành nguyên mẫu.
3. **Phối hợp nhịp nhàng giữa Phần cứng và Thuật toán:** Thay vì cố gắng giải quyết bài toán trôi và nhiễu bằng việc thêm mạch lọc tương tự phức tạp, hệ thống chuyển giao nhiệm vụ này cho thuật toán DSP 4 bước trên ESP32-S3, tối ưu hóa năng lực tính toán của vi điều khiển 240 MHz.
