# THIẾT KẾ PHÂN BỔ 2 CỤM CÔNG THÁI HỌC (ERGONOMIC 2-TIER ALLOCATION)
**Dự án:** Nghiên cứu và phát triển găng tay hỗ trợ đánh giá, theo dõi và hỗ trợ vận động bàn tay trong phục hồi chức năng sau đột quỵ  
**Mã quyết định:** `DEC-HW-008` (Ngày phê duyệt: 24/10/2026)

---

## 1. BÀI TOÁN CÔNG THÁI HỌC VÀ LÝ DO KỸ THUẬT

Ở bệnh nhân sau đột quỵ, trương lực cơ chi trên thường suy giảm nghiêm trọng ở giai đoạn nhão cơ (flaccid stage) hoặc xuất hiện mẫu co cứng gập cổ tay, rủ cổ tay (wrist drop) ở giai đoạn phục hồi sớm. Nếu dồn toàn bộ khối lượng pin nặng (2 cell pin 18650 ~90g), máy tính nhúng Orange Pi 5 Pro (~50g), mạch nguồn và vỏ hộp lên cẳng tay hoặc bàn tay, tổng tải trọng tác động lên chi trên sẽ vượt quá 300–400g. Mức tải này sẽ:
1. Gây mỏi cơ nhanh chóng chỉ sau 3–5 phút luyện tập.
2. Kéo xệ cổ tay, làm sai lệch góc chuyển động cơ sinh học tự nhiên của ngón tay.
3. Kích hoạt phản xạ co cứng gập bệnh lý thứ phát do khớp phải chịu tải quá mức.

---

## 2. KIẾN TRÚC PHÂN BỔ 2 CỤM TỐI ƯU TẢI TRỌNG

Để giải quyết triệt để rào cản trên, hệ thống được thiết kế tách rời thành **2 CỤM CHỨC NĂNG**:

```text
       [ CỤM NẸP TAY ]                             [ HỘP ĐAI HÔNG ]
  (Wearable Splint Unit)                          (Waist Control Box)
    Khối lượng: ~80-90g                           Khối lượng: ~280g
 ┌──────────────────────────┐                    ┌─────────────────────────┐
 │ • Nẹp in 3D 3 ngón tay   │                    │ • Khối Pin Li-ion 2S    │
 │ • 16 ô Velostat vi sai   │                    │   (2x 18650, 7.4V)      │
 │ • 3 Flex Sensor ZD10-100 │                    │ • Mạch Buck XL4005 5A   │
 │ • 3 Servo MG90S kim loại │      Bó cáp mềm    │ • Bo Orange Pi 5 Pro    │
 │ • 3 Tang cáp Bowden      │◄══════════════════►│ • Bo ESP32-S3           │
 │ • 2x MUX CD74HC4067      │     (Dài 50 cm)    │ • Đai đeo thắt lưng     │
 │ • Chốt an toàn mở nhanh  │                    │   thoải mái             │
 └──────────────────────────┘                    └─────────────────────────┘
```

### 2.1. Cụm nẹp tay (Wearable Splint Unit)
* **Vị trí đeo:** Ôm trực tiếp lên mu bàn tay và 3 ngón tay hướng quay (Ngón Cái, Ngón Trỏ, Ngón Giữa).
* **Thành phần bao gồm:**
  - Khung nẹp in 3D bằng nhựa sinh học PLA/PETG nhẹ, thiết kế khoét rỗng dạng tổ ong để thoáng khí.
  - 16 ô cảm biến áp trở Velostat vi sai lòng-mu và 3 dải cảm biến uốn cong Flex ZD10-100.
  - 3 động cơ servo siêu nhỏ MG90S bánh răng kim loại gắn trực tiếp lên sống mu bàn tay.
  - 3 tang cuốn cáp Bowden độc lập kèm cơ cấu chốt cơ khí an toàn mở nhanh (Quick-Release Pin).
  - 2 mạch ghép kênh mini CD74HC4067 để gom 21 kênh tương tự.
* **Tổng khối lượng:** Chỉ đạt **~80 – 90g** (giảm hơn 70% tải trọng so với thiết kế gộp khối).

### 2.2. Hộp điều khiển đai hông (Waist Control Box)
* **Vị trí đeo:** Cố định chắc chắn trên dây đai thắt lưng (vị trí trọng tâm cơ thể người tập).
* **Thành phần bao gồm:**
  - Khối nguồn Pin 2S 18650 (7.4V, ~90g).
  - Mạch hạ áp công suất cao Buck XL4005 (5A / 75W).
  - Bo mạch vi điều khiển ESP32-S3.
  - Máy tính nhúng Orange Pi 5 Pro chạy mô hình Depth Anything V2.
  - Vỏ hộp in 3D có khe tản nhiệt và quạt làm mát mini 5V.
* **Đường dây kết nối:** Toàn bộ tín hiệu điều khiển (I2C, PWM) và nguồn DC 5V cấp cho servo được luồn trong **bó cáp mềm bọc dù dài 50 cm**, dẫn men dọc theo cẳng tay xuống hông, có đai dán Velcro cố định nhẹ nhàng tại cổ tay và khuỷu tay.

---

## 3. HIỆU QUẢ CÔNG THÁI HỌC VÀ AN TOÀN

1. **Giải phóng hoàn toàn cổ tay:** Bệnh nhân thực hiện các bài tập gắp thìa, nhấc tay và di chuyển mà không bị cảm giác nặng nề đè lên khớp cổ tay.
2. **Cách ly nhiệt và điện:** Khối pin công suất lớn và máy tính nhúng tỏa nhiệt được đặt tại hông, cách xa bàn tay người bệnh, đảm bảo an toàn nhiệt tuyệt đối ($\le 37^\circ\text{C}$ tại vùng tiếp xúc da).
3. **Thao tác một tay độc lập:** Dây đai hông dạng khóa bấm cài nhanh (Side-Release Buckle), người bệnh có thể tự cài hoặc tháo bằng một tay khỏe mạnh mà không cần người trợ giúp.
