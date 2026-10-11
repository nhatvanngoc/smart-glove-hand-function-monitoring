# Báo cáo thực nghiệm: Đánh giá dạng sóng quét đa kênh sau tối ưu tốc độ

## 1. Phân tích kết quả đo trên Serial Plotter
* **Tốc độ Baudrate:** 115200 baud.
* **Kênh 0 (Trắng xám):** Duy trì sát mức $0\text{ mV}$ (dao động nhỏ $\approx 0 - 20\text{ mV}$). Không bị nhiễu chéo từ các kênh điện áp cao.
* **Kênh 1 (Xanh lam):** Ổn định ở mức cao $\approx 3.046\text{ mV} - 3.100\text{ mV}$, biến thiên nhẹ mượt mà.
* **Kênh 2 (Vàng):** Dao động tuần hoàn dạng tam giác từ $\approx 150\text{ mV}$ lên đỉnh $\approx 1.650\text{ mV}$. Đến mẫu thứ 55364, kênh 2 chuyển trạng thái tụt về mức nền $\approx 150\text{ mV}$ (khi ngừng kích xung hoặc tín hiệu dừng).

## 2. Kết luận
* CD74HC4067 chuyển mạch hoàn toàn ổn định và tin cậy giữa các kênh có độ lệch điện áp lớn (0V, 1.65V, 3.0V).
* Kênh 1 giữ điện áp cao ổn định mà không kéo theo Kênh 0 hay làm sụt Kênh 2.
* Hệ thống sẵn sàng cho bước tích hợp ma trận cảm biến Velostat.
