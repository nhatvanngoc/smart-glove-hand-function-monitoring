# GLOSSARY — Định nghĩa thuật ngữ dùng nhất quán trong báo cáo
# (Cập nhật 2026-09-13 — Găng tay theo dõi chức năng bàn tay sau đột quỵ; phần cứng ESP32-S3)

---

## Hệ thống phân cấp cảm biến

| Cấp | Tên gọi trong báo cáo | Thành phần | Ghi chú |
|---|---|---|---|
| Vật liệu | **vật liệu piezoresistive Velostat** | Film polyolefin tẩm carbon | KHÔNG gọi là "cảm biến Velostat" |
| Điện cực | **điện cực copper tape** | Băng đồng dẫn điện | Tạo tiếp xúc điện |
| Phần tử cảm biến | **sensing element** | Velostat + copper tape + cấu trúc sandwich + lớp cơ khí giữ hình học | Do tác giả chế tạo |
| Cặp phần tử | **cặp sensing element đối xứng** | 2 sensing element trên 2 vách đối diện của cùng khung | Dùng để đọc vi sai (hiệu), triệt thành phần drift đồng pha |
| Hệ thống đo | **mảng sensing element** | 12–24 sensing element trên khung găng in 3D | Bố trí theo bảng trong `docs/04_Hardware_Architecture.md` |
| Hệ thống hoàn chỉnh | **hệ thống cảm biến áp lực bàn tay** | Mảng + CD74HC4067 + ESP32-S3 + firmware | Toàn bộ phần đo, chưa gồm xử lý biên |

## Nguyên lý cơ học — thiết kế khung cứng

**Cơ chế chuyển đổi hướng chuyển động → tín hiệu áp lực:**

```
Ngón tay chuyển động hướng X
        ↓
Đụng vào vách khung exoskeleton hướng X
        ↓
Tạo áp lực lên dải Velostat tại vách hướng X
        ↓
ADC đọc điện trở thay đổi → lực hướng X
        ↓
Dịch thành vector hướng → tái tạo flexion/extension
```

**Điểm khác biệt so với găng tay Velostat thông thường:**
- Thông thường: Velostat đo **lực tiếp xúc trực tiếp** (fingertip pressure khi cầm vật)
- Thiết kế này: Velostat đo **lực hướng qua vách khung** → mã hóa được **hướng chuyển động** của từng lóng ngón tay

**Prior art gần nhất cần differentiate:**
- Glove-based system (Zhu lab, IROS 2017): Velostat đo lực + IMU đo pose → tái tạo bàn tay. Dùng IMU riêng để đo góc khớp.
- Reconfigurable Data Glove (Science China 2023): Velostat tại ngón + 4×4 grid ở lòng bàn tay + IMU.
- **Đề tài này:** KHÔNG dùng IMU — dùng chính Velostat trên khung cứng để suy ra hướng chuyển động → rẻ hơn, đơn giản hơn, nhưng cần validate độ chính xác.

## Output chính của hệ thống

| Thuật ngữ | Định nghĩa | Ghi chú |
|---|---|---|
| **Đường cong chức năng theo tuần** *(digital trajectory)* | Chuỗi chỉ số chức năng tay định lượng theo tuần | Output chính — "viên đạn" của đề tài |
| **Chỉ số chức năng vận động** | Vector đặc trưng từ mảng sensing element sau khi xử lý | Đầu vào của mô hình |
| **Đường nền (baseline)** | Giá trị chỉ số ở tuần 0 | Cá nhân hóa cho từng người dùng |
| **Suy luận hướng khớp** | Ước lượng hướng gập/duỗi của khớp từ mẫu kích hoạt trên các vách khung | **Suy luận (infer)**, KHÔNG phải "đo góc khớp" |
| **Đọc vi sai** | Hiệu hai sensing element trên hai vách đối diện | Giảm ảnh hưởng drift đồng pha |
| **Ô tham chiếu** | Sensing element ở vị trí không chịu tải người dùng | Đo biến thiên thuần của hệ đo → cờ "UNRELIABLE" |
| **Cờ không đáng tin (UNRELIABLE)** | Trạng thái hệ thống khi dữ liệu không đủ điều kiện kết luận | Nguyên tắc: **thà báo lỗi còn hơn báo sai** |

## Tuyên bố bị cấm

| Sai | Đúng |
|---|---|
| "Cảm biến Velostat" | "sensing element chế tạo từ vật liệu Velostat" |
| "Chẩn đoán đột quỵ / mức độ liệt" | "hỗ trợ theo dõi chức năng vận động bàn tay" |
| "Thay thế Fugl-Meyer / ARAT / Box and Block" | "bổ sung thông tin giữa các lần đánh giá lâm sàng" |
| "Đo chính xác lực tuyệt đối" | "theo dõi thay đổi tương đối so với đường nền cá nhân" |
| "Đo góc khớp" | "suy luận hướng gập/duỗi của khớp" |
| "Robot / găng tay phục hồi chức năng" | "găng tay đánh giá và theo dõi" |
| "TinyML" (chung chung) | "mô hình lượng tử hóa INT8 triển khai trên NPU RK3588" |
| "Loại bỏ drift" / "drift-free" | "giảm ảnh hưởng drift ở tầng đồng pha, phần còn lại được định lượng" |
| "Chứng minh hiệu quả lâm sàng" | "kiểm tra độ ổn định và độ nhạy trên phantom/người tình nguyện khỏe" |
| "Đã triển khai trên NPU" (khi chưa có log) | "đã chạy thử, kết quả log tại …" |

## Câu trả lời mẫu — giám khảo hỏi

**"Cảm biến của em là cái gì?"**
> "Sensing element do em tự chế tạo, gồm lớp vật liệu piezoresistive Velostat kẹp giữa hai lớp điện cực copper tape theo cấu trúc sandwich, có thêm lớp cơ khí giữ hình học ổn định. Các sensing element được dán trên vách của khung cứng in 3D tại các khớp ngón tay: cấu hình tối thiểu 12 kênh, cấu hình đầy đủ 24 kênh đọc vi sai theo cặp."

**"Sao em không dùng IMU như các găng tay khác?"**
> "IMU đo góc trực tiếp nhưng đắt theo số trục và bị trôi tích phân. Em chọn cách khác: để ngón tay tì vào vách khung, đo lực ở vách đó. Cách này rẻ hơn, và quan trọng hơn là em đo được cả **hướng** lẫn **độ lớn** của lực — thứ mà găng tay đo lực tiếp xúc thông thường không có. Đổi lại, em phải chứng minh bằng GATE A/B rằng suy luận hướng là đúng."

**"Em thay thế được Fugl-Meyer không?"**
> "Không. Hệ thống không thay thế đánh giá lâm sàng. Nó cung cấp dữ liệu định lượng liên tục giữa các lần tái khám — thứ hiện tại chưa có công cụ nào làm được tại nhà với chi phí thấp."

**"Làm sao em biết số liệu của mình đúng?"**
> "Em không khẳng định nó đúng. Em chạy 6 cổng kiểm tra từ phantom tới nhiều ngày, trong đó cổng C là cổng sống còn: thay đổi chức năng mô phỏng phải lớn hơn biến thiên drift/nhiễu của chính hệ thống. Nếu cổng đó không đạt, em sẽ báo cáo là hệ thống không dùng được cho theo dõi tiến triển."

**"Tại sao dùng INT8?"**
> "INT8 là kỹ thuật cụ thể để đưa mô hình lên NPU của Orange Pi 5 Pro (RK3588). Nó giảm kích thước mô hình khoảng 4 lần so với FP32 và chạy được tại chỗ, không cần mạng — phù hợp thiết bị dùng tại nhà. Mức giảm độ chính xác sau lượng tử hóa em phải đo, không giả định."
