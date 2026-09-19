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

**Prior art cần differentiate (cập nhật 2026-09-19, lượt rà soát Gap 1 — chi tiết trong `research/reviews/2026-09-19_prior_art_novelty_gate1.md`):**
- `SRC-ZHU-2017-GLOVE` (đã xác minh): Liu H. et al., *A Glove-based System for Studying Hand-Object Manipulation via Joint Pose and Force Sensing*, IROS 2017, tr. 6617–6624, DOI 10.1109/IROS.2017.8206575 — 15 IMU đo pose + 6 cụm Velostat (26 taxel) đo lực tiếp xúc. **Hướng vector lực ở đó được GÁN theo pose từ IMU**, không suy ra từ vách.
- `SRC-RECONFIG-GLOVE-2023` (đã xác minh): Liu H. et al., **Engineering** 2024;32(1):217-232, DOI 10.1016/j.eng.2023.01.009 — *không phải* "Science China"; pose vẫn dùng backbone IMU.
- `SRC-SIDEWALL-PIEZO-2015` (mới, QUAN TRỌNG): *Piezoresistive Tactile Sensor Discriminating Multidirectional Forces*, Sensors 15(10), DOI 10.3390/s151025463 — **1 lõi + 4 vách**, phần tử CNT/PDMS khóa liên động, phân biệt áp pháp tuyến + shear theo 4 hướng **không cần xử lý tín hiệu phức tạp**. ⇒ ý tưởng "vách mã hóa hướng" đã có từ 2015.
- `SRC-ARTGLOVE-2026` (mới, QUAN TRỌNG): Lin C., Zhao D., *ART-Glove*, arXiv:2606.16370 (15/06/2026) — **găng vỏ cứng khớp nối, 16 bề mặt chức năng, da áp điện trở 2048 taxel @120 Hz**, nhưng 22 DoF đo bằng **encoder**.
- `SRC-GRATING-GLOVE-2021` (mới): găng đo góc khớp **không IMU** bằng dải cách tử + đầu dò quang, precision 1,67% FS.
- **Đề tài này (phát biểu đã thu hẹp, trung thực):** không claim nguyên lý vách là mới; claim là **tổ hợp** *vách có kéo trước + đọc vi sai để lấy DẤU gập/duỗi, không encoder/IMU/camera* + **kiểm chứng MDC/ICC** + **cờ từ chối kết luận**, phục vụ theo dõi dọc tại nhà sau đột quỵ.

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
| "Ý tưởng mới: đo hướng bằng vách áp điện trở" | "áp dụng nguyên lý vách (đã có trong cảm biến xúc giác từ 2015) lên khung lóng ngón để suy DẤU gập/duỗi, không encoder/IMU" |
| "Hệ thống đầu tiên theo dõi chức năng tay tại nhà" | "chưa tìm thấy hệ thống nào kết hợp đủ lực hướng + MDC/ICC + cờ độ tin cậy (tính đến lượt rà soát prior art 2026-09-19)" |
| "Không dùng IMU nên chính xác hơn / rẻ hơn nên tốt hơn" (mệnh đề novelty) | "không dùng IMU là lựa chọn thiết kế; đã có găng grating/quang và stretch không IMU" |
| "Đã triển khai trên NPU" (khi chưa có log) | "đã chạy thử, kết quả log tại …" |
| "Chưa ai làm găng tập có trợ lực / AAN cho ngón tay" | "đề tài dùng lại nguyên lý AAN đã có (iHand 2018, AAN+EMG 2024, găng ngón cái 2026) **ở tầng đo**, không phải ở tầng điều khiển; ở Việt Nam đã có ĐH Bách khoa Đà Nẵng và ĐH Thủy lợi làm găng kéo gập/duỗi" |
| "First to discover/invent [một nguyên lý]" | "First to integrate [A + B] for [một nhóm người dùng cụ thể]" — mẫu câu đã được thưởng ở ISEF (ROBO065T, 2025), **với điều kiện** đi kèm 3–5 con số tự đo; nếu không có số thì không được dùng chữ "first" |

## Câu trả lời mẫu — giám khảo hỏi

**"Cảm biến của em là cái gì?"**
> "Sensing element do em tự chế tạo, gồm lớp vật liệu piezoresistive Velostat kẹp giữa hai lớp điện cực copper tape theo cấu trúc sandwich, có thêm lớp cơ khí giữ hình học ổn định. Các sensing element được dán trên vách của khung cứng in 3D tại các khớp ngón tay: cấu hình tối thiểu 12 kênh, cấu hình đầy đủ 24 kênh đọc vi sai theo cặp."

**"Sao em không dùng IMU như các găng tay khác?"** *(đã siết lại 2026-09-19 — tránh claim "không IMU = mới")*
> "IMU đo góc trực tiếp nhưng đắt theo số trục và bị trôi tích phân. Em chọn cách khác: để ngón tay tì vào vách khung có kéo trước, đọc hiệu giữa hai vách đối diện. Cách này rẻ hơn và cho em cả **dấu** lẫn **độ lớn**. Em không nói 'đo hướng bằng vách' là ý tưởng của em — trong cảm biến xúc giác đã làm thế từ 2015, và năm 2026 đã có găng vỏ cứng phủ da áp điện trở, chỉ khác là họ vẫn dùng encoder để đo góc. Cái em nhắm tới là bỏ được encoder và IMU mà vẫn **chứng minh** được suy luận đó đủ tin bằng GATE A/B và bằng MDC. Đổi lại, em phải chứng minh bằng GATE A/B rằng suy luận hướng là đúng."

**"Em thay thế được Fugl-Meyer không?"**
> "Không. Hệ thống không thay thế đánh giá lâm sàng. Nó cung cấp dữ liệu định lượng liên tục giữa các lần tái khám — thứ hiện tại chưa có công cụ nào làm được tại nhà với chi phí thấp."

**"Làm sao em biết số liệu của mình đúng?"**
> "Em không khẳng định nó đúng. Em chạy 7 cổng kiểm tra (GATE 0 và A–F) từ phantom tới nhiều ngày, trong đó cổng C là cổng sống còn: thay đổi chức năng mô phỏng phải lớn hơn biến thiên drift/nhiễu của chính hệ thống. Nếu cổng đó không đạt, em sẽ báo cáo là hệ thống không dùng được cho theo dõi tiến triển."

**"Tại sao dùng INT8?"**
> "INT8 là kỹ thuật cụ thể để đưa mô hình lên NPU của Orange Pi 5 Pro (RK3588). Nó giảm kích thước mô hình khoảng 4 lần so với FP32 và chạy được tại chỗ, không cần mạng — phù hợp thiết bị dùng tại nhà. Mức giảm độ chính xác sau lượng tử hóa em phải đo, không giả định."
