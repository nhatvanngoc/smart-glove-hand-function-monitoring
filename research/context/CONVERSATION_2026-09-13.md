# Bản nén hội thoại — 2026-08-28 → 2026-09-13 (pivot sang găng tay)

> Chỉ ghi **chỉ thị của chủ dự án**, **dữ kiện mới** và **kết luận bền vững**. Không ghi diễn biến trao đổi.
> Bản nén giai đoạn trước: `CONVERSATION_2026-08-25.md` (đề tài cũ — chỉ còn giá trị lịch sử).

---

## 1. Chỉ thị của chủ dự án

| # | Ngày | Chỉ thị | Ghi nhận |
|---|---|---|---|
| D1 | 2026-08-28 | PIVOT: bỏ DFU, chuyển sang **găng tay theo dõi chức năng bàn tay sau đột quỵ** | → DEC-TOPIC-018 |
| D2 | 2026-08-28 | Không làm găng tay **phục hồi chức năng** (máy tập). Chỉ làm **đánh giá + theo dõi** | Định vị sản phẩm |
| D3 | 2026-09-13 | Chốt tên đề tài: *"Nghiên cứu và phát triển găng tay thông minh hỗ trợ đánh giá và theo dõi chức năng vận động bàn tay trong phục hồi chức năng sau đột quỵ"* | → DEC-TOPIC-019 |
| D4 | 2026-09-13 | Nguyên lý cơ học: khung cứng + ngón tay tì vào vách → đo lực hướng → dựng lại bàn tay 3D | → DEC-HW-002 |
| D5 | 2026-09-13 | Đề xuất **ESP32-S3 + MUX 74HC** thay Arduino Mega 2560 | → DEC-HW-003 (đã kiểm chứng kỹ thuật, chấp nhận) |
| D6 | 2026-09-13 | Yêu cầu tính toán sao cho **độ phân giải đủ tốt** cho đánh giá và tái tạo | → `docs/04_Hardware_Architecture.md` |
| D7 | 2026-09-13 | Cập nhật tên mới + đẩy toàn bộ lên GitHub | Phiên này |

## 2. Phỏng vấn KTVVLTL-PHCN — phần 2

**Câu hỏi:** Các găng tay phục hồi chức năng hiện có trên thị trường có dùng được không?

**Trả lời (nén):**
- Giá thường từ khoảng 4.000 USD trở lên — không hợp lý so với thuê một kỹ thuật viên thật.
- Thường chỉ dùng trong phòng khám, dưới giám sát của người vận hành → **không giải quyết được khoảng trống tại nhà**.
- Phần lớn chỉ **thực hiện động tác** mà không **theo dõi và đánh giá** → dễ gây **lệ thuộc máy**, không phải phục hồi chức năng.
- Phân biệt hai mức khó:
  - **Mức thấp (thụ động: co–duỗi):** găng tay hiện có hỗ trợ được, nhưng gây phụ thuộc.
  - **Mức cao (cầm nắm, bấm bàn phím, bóp, xoay cổ tay):** găng tay hiện có **không làm được**, vì không đảm bảo an toàn và trách nhiệm pháp lý — **bắt buộc phải có người có chuyên môn**.
- Phần mềm mô phỏng kiểu "RehabReach" thiếu độ chính xác của **vi cử động** và không tương tác với thực tế. 🔵 *(thông tin do chủ dự án cung cấp — cần xác minh trước khi đưa vào báo cáo)*

**Kết luận rút ra (quan trọng):**
> Xây dựng một găng tay phục hồi chức năng **hoàn chỉnh, không phụ thuộc con người** là hướng **không phù hợp** về an toàn và chuyên môn.
> Hướng phù hợp là một giải pháp **rẻ, theo dõi và đánh giá được tại nhà**: găng tay đánh giá liên tục → phân tích → phát hiện sớm sai động tác → gửi dữ liệu tới chuyên gia → can thiệp sớm → tiếp tục đánh giá.

## 3. Xác nhận độc lập về nhu cầu

- Chủ dự án tham khảo ý kiến **thầy tại phcn-online.com** và **chị là KTV PHCN**; cả hai đều nói đề tài **đáng làm**. → DEC-CLINICAL-002.
- Trang phcn-online có nêu: quá trình luyện tập kéo dài, lặp lại, đòi hỏi người bệnh tham gia tích cực, trong khi **nhiều cơ sở PHCN còn hạn chế về trang thiết bị và nguồn lực**. 🔵 *(phải lấy đúng URL bài và câu nguyên văn trước khi trích dẫn)*

## 4. Nguyên lý cơ học do chủ dự án đặt ra (nguyên văn, nén)

> "Găng tay có một bộ khung cơ khí cứng (exoskeleton) ép sát vào ngón tay. Khi ngón tay muốn nhúc nhích sang phải → nó đụng vào vách bên phải của khung → tạo áp lực lên dải Velostat bên phải. Máy tính đọc lực này và dịch thành vector hướng sang phải. Tôi hoàn toàn có thể dùng dữ liệu này để vẽ lại một bàn tay 3D đang mô phỏng lực bóp gập/duỗi (flexion/extension) của các lóng tay."

→ Ghi thành DEC-HW-002. Đây là **ứng viên novelty chính** của đề tài và **phải qua GATE A/B** trước khi được viết như một kết quả.

## 5. Phân tích kỹ thuật đã thực hiện trong phiên

| Vấn đề | Kết luận |
|---|---|
| Mega 2560 hay ESP32-S3? | **ESP32-S3 + CD74HC4067.** Mega: ADC 10-bit, 5 V (buộc level shifter), không wireless. ESP32-S3: 12-bit, 240 MHz, BLE 5, 3.3 V khớp Orange Pi. **Đánh đổi:** ADC S3 kém tuyến tính → phải hiệu chuẩn, chỉ dùng ADC1 |
| MUX nào? | **CD74HC4067** (16:1) chứ không phải 74HC4051 (8:1) — 12–24 kênh cần 16 kênh/MUX |
| Bao nhiêu kênh? | **12 kênh** tối thiểu (11 đo + 1 tham chiếu) cho bring-up; **24 kênh** cho bản đầy đủ có **cặp đối xứng đọc vi sai** |
| Vì sao cần cặp đối xứng? | Một vách chỉ cho độ lớn, **không cho dấu** gập/duỗi. Hiệu hai vách cho dấu + triệt thành phần drift đồng pha |
| 12-bit có đủ? | Danh định 12-bit nhưng ENOB thực thấp hơn; trung bình 16 mẫu → **~11 bit hiệu dụng** (ước lượng, phải đo) |
| Tốc độ khung? | 12 kênh ≈ 415 Hz, 24 kênh ≈ 208 Hz khi `t_ch` = 200 µs → **mục tiêu 45–100 Hz** là rộng rãi cho động tác 0,5–2 Hz |
| Vì sao không cần mạng? | Bệnh nhân lớn tuổi; dữ liệu sức khỏe; phản hồi tức thời → xử lý tại biên, mô hình INT8 trên NPU RK3588 |

## 6. Bảy câu hỏi chủ dự án đặt ra và câu trả lời đã chốt

| # | Câu hỏi | Câu trả lời chốt |
|---|---|---|
| ① | Tính mới ở đâu? | **Cơ chế**: cảm biến **hướng** qua vách khung cứng (không IMU) + **đọc vi sai** + **tự kiểm tra độ tin cậy**. Không phải "găng tay + AI" |
| ② | Tại sao cần? | Khoảng 1–3 tháng giữa các lần tái khám là **hộp đen**; công cụ hiện tại là ảnh chụp rời rạc; không phát hiện được chững lại/tập sai |
| ③ | Ai thực sự dùng? | **Người đeo:** bệnh nhân (người nhà hỗ trợ mang/tháo). **Người đọc dữ liệu (người dùng chính):** KTV VLTL-PHCN. **Người dùng thứ cấp:** bác sĩ PHCN |
| ④ | "Vector 3D" đại diện cho cái gì? | Hướng và độ lớn **phản lực của lóng ngón lên vách khung**. Là proxy cho hướng gập/duỗi, biên độ vận động, độ mượt, lực cầm nắm — **không** phải góc khớp tuyệt đối, **không** phải hoạt động cơ |
| ⑤ | Làm sao chứng minh đúng? | GATE 0 (lặp lại) → A (hướng) → B (tái tạo 3D so với góc biết trước) → **C (độ nhạy, sống còn)** → D (không báo giả) → E (tự phát hiện lỗi) → F (INT8). Ngưỡng chốt trước |
| ⑥ | Nếu thành công thì xã hội được gì? | Rút ngắn điểm mù theo dõi từ ~90 ngày xuống ~1 tuần; phát hiện chững lại/suy giảm sớm; giảm số lần phải đến cơ sở; KTV theo dõi được nhiều bệnh nhân hơn |
| ⑦ | Nếu đánh giá được lực thì sao? | Lực ngón/cầm nắm là đại lượng **có tiền lệ lâm sàng** (tương quan với FMA-UE/ARAT/BBT trong y văn — 🔵 phải verify số). Cho phép phân biệt mẫu **yếu** với mẫu **co cứng**, và dựng **đường cong hồi phục** theo tuần |

## 7. Kiến thức ngoài dự án đã thu thập (chưa đọc toàn văn — 🔵)

- Systematic review *AI-based smart glove…* (2026, 101 bài): phần lớn nguyên mẫu chưa được kiểm chứng lâm sàng; tồn tại drift, suy giảm tín hiệu, cần tự hiệu chỉnh và mô hình nhẹ lượng tử hóa.
- *Wearable technology to capture arm use of stroke survivors* (2023): 87,6% ngày đo hợp lệ; **hạn chế:** cảm biến cổ tay không ghi được chuyển động ngón, không phân biệt vận động có mục đích.
- *Quantitative measurement of finger usage using ring-shaped wearables* (2023): tỷ lệ sử dụng ngón tương quan với FMA-UE/ARAT/STEF.
- RCT *force feedback hand rehabilitation robot* (2024, PMC11092254): lực bóp, AROM, FMA-Hand, ARAT cải thiện → lực ngón có ý nghĩa lâm sàng.
- Ngưỡng MDC của ARAT (~4 điểm) 🔵 cần đối chiếu bảng gốc.
- Đề tài exoskeleton Quảng Trị (giải nhì quốc gia) làm **chi dưới** + có phát hiện co cứng → không trùng, nhưng **phải tránh** mọi phần liên quan đến chi dưới/spasticity.

## 8. Việc chưa giải quyết

- Chưa rà soát xong prior art (`docs/03`) → mức novelty chưa được chốt.
- Chưa có số liệu thực nghiệm nào.
- Chưa verify: nguồn "80% bệnh nhân yếu tay"; nguồn giá Jamar/E-Link; câu trích phcn-online; "RehabReach"; các số tương quan lấy từ y văn.
- Chưa đổi được tên repo GitHub (token phiên không có quyền Administration — HTTP 403).
