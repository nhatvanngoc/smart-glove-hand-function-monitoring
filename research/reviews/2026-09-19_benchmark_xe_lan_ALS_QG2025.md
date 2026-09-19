# Benchmark: báo cáo toàn văn "Xe lăn tự hành hỗ trợ bệnh ALS trong di chuyển và giao tiếp" (Cuộc thi KHKT cấp quốc gia 2024–2025, lĩnh vực HỆ THỐNG NHÚNG)

> **Nguồn:** `BCTT - QG.pdf` do chủ dự án cung cấp qua liên kết Google Drive (`drive.google.com/file/d/1H4TLHMIEwgDnas9XEzxrrRzbiZ7b4nM2`), **đã đọc 5/5 chunk = toàn văn 15 trang**, ngày 2026-09-19.
> **Dòng ledger:** `SRC-XELAN-ALS-QG2025-REPORT` (`READ_FULL`).
> **⛔ QUY tắc sử dụng (chỉ thị chủ dự án 2026-09-19):** tài liệu này là **benchmark nội bộ**. **Không** trích, **không** nêu tên, **không** dẫn số liệu của nó trong bất kỳ file nào của hồ sơ nộp (`docs/05`, `docs/bao_cao/*`, báo cáo toàn văn, poster, slide).
> **Chuẩn đánh giá ở đây = ⚑ chuẩn hội thi học sinh** (không phải chuẩn tạp chí). Mọi nhận định là **phán đoán**, không phải số đo.

---

## 1. Báo cáo đó *thực sự* dài và chặt đến đâu (đếm được, không cảm tính)

| Hạng mục | Giá trị đếm từ bản toàn văn |
|---|---|
| Độ dài | **15 trang** (A: tr. 3–4 · B: tr. 5–9 · C: tr. 10–14 · TLTK: tr. 15) |
| Cấu trúc | A. 7 mục (lý do / xác định vấn đề / mục tiêu / **tiêu chí dự án** / đối tượng & phạm vi / địa điểm / phương pháp) — B. 7 mục — C. 5 mục — TLTK |
| Hình + Bảng | **17 "Hình" + 3 "Bảng"** ≈ **1,33 mục trình bày / trang**. Phần lớn là sơ đồ khối nguyên lý + ảnh chụp thật + ảnh chụp màn hình app/đồ thị |
| Bảng vật liệu | `Bảng 1` liệt kê 6 nhóm thiết bị (Arduino Uno R3, 2× DAC MCP4725, RealSense D435i, RPLidar A1, 2× encoder 600 xung, 2× webcam) — **không có giá tiền, không có tổng chi phí** |
| Số lượng phép đo | gaze: **1000 ảnh** (dataset Kaggle, không phải dữ liệu tự thu) · sai số tọa độ: **5 điểm, mỗi điểm 1 lần** · DAC: **1 bảng 9 hướng** đo bằng đồng hồ vạn năng · PID: **bảng log 167 dòng** (input/setpoint/output) · tự hành: **0 số** (chỉ có ảnh bản đồ + ảnh app) · LLM: **310 mẫu câu** (300 train / 10 test), loss 2,6 → 0,2, **bảng so sánh 2 prompt** |
| Kiểm định thống kê | **0** (không SD, không CI, không p, không ICC, không kiểm định phân phối) |
| Cỡ mẫu người dùng | **0** — không có thử nghiệm trên bệnh nhân; ảnh "vận hành trong môi trường thực nghiệm" là nhóm tự vận hành |
| Tuyên bố đạo đức / IRB | **không có dòng nào** |
| Prior art | **2** đối thủ nêu trong văn bản ("Xe lăn điều khiển bằng mắt" giải nhì ISEF 2016; WHILL) — **không có bảng differentiate**, không có mức-đã-đọc |
| Tài liệu tham khảo | **9** mục; phần lớn là **blog / Wikipedia / trang hãng / trang ROS wiki / trang Kaggle**; **0 DOI**, **0 bài báo phản biện** |
| Tiêu chí PASS | nêu dạng số ("sai số dưới 2 cm", "8 hướng", "2 ngôn ngữ", "3 câu văn") nhưng **không có quy trình chốt trước khi đo**, không có cổng nào bị fail được báo cáo |
| Giới hạn | §C.5 "Hướng phát triển" = **1 đoạn**, nội dung: "các module điện tử đều đang sử dụng sẵn có trên thị trường, chưa chủ động thiết kế nên một số thông số chưa tối ưu" |
| Kết quả | giải **Nhất** Cuộc thi KHKT cấp quốc gia 2025 (19–21/3/2025, TP.HCM), lĩnh vực **Hệ thống nhúng**; sau đó **giải Tư ISEF 2025**, ISEF xếp vào **Robotics and Intelligent Machines** (theo báo chí + trang isef.net, đã verify ở lượt trước) |

### 1.1 Cái họ **bắt buộc phải có** để thắng (theo quan sát)
1. Một **vật thật chạy được** + ảnh chụp nó đang chạy (Hình 12–17).
2. **Vài con số** tự đo, mỗi mục tiêu 1 con số, đặt cạnh mục tiêu (2 cm, 99,2 %, 1 m/s, loss 0,2).
3. Sơ đồ nguyên lý cho **từng** module (Hình 1–7) — người đọc không cần chạy được cũng hiểu hệ thống ghép kiểu gì.
4. Một chuỗi "lần đầu tiên / chưa ai làm đồng thời" **cụ thể** (chưa tích hợp theo dõi đồng tử **vào** xe lăn tự hành + chưa dùng NLP cho giao tiếp) — không cần bảo vệ bằng tra cứu.
5. Chi phí tự chế / phần cứng dùng sẵn nêu bằng **tên linh kiện**, không cần giá.

### 1.2 Cái họ **không cần** mà vẫn thắng (thông tin đắt giá nhất cho ta)
Bảng prior art · mức-đã-đọc của nguồn · kiểm định thống kê · protocol chốt trước khi đo · cỡ mẫu người dùng · tuyên bố IRB · danh sách "anti-claims" · log công khai · báo cáo kết quả fail. **Tám thứ này đều là thứ đề tài ta đã có hoặc đã lên kế hoạch có.**

---

## 2. Ba điểm mà nếu chỉ đọc báo cáo cấp quốc gia thì **không** thấy (đối chiếu ISEF abstract)

| Đại lượng | Bản QG (15 tr.) | Bản ISEF (abstract) | Bài học cho ta |
|---|---|---|---|
| Độ chính xác gaze | "99,2 %" = **992/1000 ảnh** đúng *hình dạng + tâm đồng tử* | "97,11 %" accuracy of **gaze point** | cùng một chữ "accuracy" cho hai construct khác nhau. Ta đã có quy tắc cấm loại lẫn lộn này (`AGENTS.md`: không ADC→N/độ) → **giữ và nêu thẳng trong báo cáo** |
| Chất lượng điều hướng | **không có số** (chỉ ảnh bản đồ + ảnh app) | **0,12 m** sai lệch bám quỹ đạo, **93,33 %** phiên tự hành đến đích | vòng sau **đòi số ở cấp hệ thống**, không chấp nhận "chạy được". → chính là GATE B + GATE D của ta |
| Giao tiếp | "3 câu văn, 2 ngôn ngữ, Telegram" (định tính) | "**< 5,33 s**/câu" | độ trễ là con số rẻ nhất để thêm → `fps_meas` + độ trễ đầu–cuối đã nằm trong `protocols/08` G0.9 |

**Suy luận (phán đoán, ⚑):** họ phải *chèn thêm* 4 chỉ số định lượng để đi thi quốc tế. Nghĩa là ban tổ chức/quốc tế chấm bằng **số đo hệ thống**, không bằng sơ đồ. Đề tài ta nên **làm luôn từ vòng quốc gia** phần mà họ phải làm ở vòng quốc tế — đó là chỗ rẻ nhất để vượt.

---

## 3. Đối chiếu trực tiếp: cùng một "ô" trong báo cáo, ai hơn ai

| Ô trong báo cáo (form quốc gia) | Họ (QG 2025) | Ta **hôm nay** | Ta **sau GATE 0 + GATE C** | Phán đoán ⚑ |
|---|---|---|---|---|
| Vật thật | Xe lăn + 6 module, chạy được, có ảnh | **0** — jig chưa chế tạo | phần tử áp trở + 1 ngón trên jig + ảnh log | **họ hơn hẳn** cho tới khi ta có ảnh thứ nhất |
| Con số cho từng mục tiêu | 5 số | **0** | 6 con số tự đo (review `…_scope_options.md` §12) | ngang, rồi hơn |
| Cơ sở của con số | 1 lần đo/điểm | protocol + ngưỡng **chốt trước** | CV, ICC, MDC, ENOB, `fps_meas` | **ta hơn rõ** |
| "Độ tin cậy của dữ liệu" | không đề cập | cờ `UNRELIABLE` + GATE E (bơm lỗi) | phát hiện lỗi ≥ 90 %, báo động giả ≤ 5 % | **ta hơn** (và giải thích được bằng 1 ảnh: đồ thị có 2 đường, một đường bị đánh dấu loại) |
| Theo dõi theo thời gian | không có | — | ≥ 10 ngày drift-only + đường cong theo tuần | **ta hơn đúng chỗ họ trống** |
| Vấn đề người dùng / tính cấp thiết | số ALS của Mỹ (1 trang mạng) | dịch tễ VN: 1.541/100.000 *(verify)* + 80 % *(verify)* | + **10 phiếu phỏng vấn KTV** (chị tác giả làm nghề) | **ta hơn về độ địa phương**, nếu lấy được phỏng vấn |
| An toàn | chọn 1 m/s "để đảm bảo an toàn" | rig chỉ tác động phantom; **cấm** thử trên người; `CLM-SAFE-001` | + bộ 3 chân (moment/vòng dòng/giới hạn thời gian) | ngang ở câu chữ, **ta hơn ở bằng chứng** (log dòng thô 2026-09-05) |
| Giới hạn | 1 đoạn mơ hồ | Phụ lục A `docs/05` (liệt kê cái **không** nói) | + cổng nào fail thì nói fail | **ta hơn**, nhưng phải *trình bày ngắn* — họ chỉ dành 3 dòng |
| Đạo đức/IRB | không có dòng nào | 5 điều + quy trình | — | **ta hơn, và không mất gì**; nhưng đừng biến thành 2 trang (hội đồng không quen đọc) |

---

## 4. Đánh giá lại đề tài của bạn sau khi đọc benchmark (thay đổi so với `2026-09-19_project_ceiling.md`)

### 4.1 Trần ⚑: **nâng một bậc có điều kiện** — và có một quyết định chiến thuật mới
- **Cao hơn:** chuẩn thực tế của hội đồng **không phải** "độ chặt khoa học" (họ cho một báo cáo 15 trang, **0 kiểm định thống kê, 0 prior art table, 0 IRB, 0 số đo điều hướng** đạt giải Nhất quốc gia + giải Tư ISEF). Mọi thứ ta đã làm (134 nguồn có mức đọc, 7 cổng, ngưỡng chốt trước, anti-claims) **nằm trên** mặt bằng đó, không phải "quá mức cần thiết". ⇒ **giữ toàn bộ**, nhưng **đừng để nó phình thành 40 trang**.
- **Điều kiện:** toàn bộ lợi thế trên là **hứa hẹn**. Lợi thế của họ là **đã có**. Ở vòng chấm, 1 ảnh chụp thiết bị đang chạy + 1 bảng số thắng 5 trang phương pháp luận.
- **Quyết định chiến thuật mới — chọn lĩnh vực:** họ thắng ở **HỆ THỐNG NHÚNG** với một thiết bị y tế-trợ năng, và **ISEF lại xếp** cùng dự án đó vào Robotics. ⇒ đề xuất cho ta (chủ dự án quyết): **chính = Hệ thống nhúng (Embedded Systems)**, **phụ = Y sinh – Khoa học sức khỏe**. Lý do: bằng chứng của ta là *độ lặp, nhiễu, độ trễ, cổng pass/fail* — đúng ngôn ngữ của giám khảo kỹ thuật; đưa vào ô Y sinh sẽ mời câu hỏi "bệnh nhân đâu?" mà ta **không có quyền** trả lời trước IRB.

### 4.2 Ngân sách hình thức phải bắt chước (đây là chuẩn thắng, không phải chuẩn ta tự đặt)
| Chỉ tiêu hình thức | Ngưỡng nên tự đặt cho ta |
|---|---|
| Độ dài báo cáo toàn văn | **15–20 trang** (không phải 40). `docs/02` 387 dòng là **tài liệu nội bộ**, nén xuống còn **~2 trang** trong hồ sơ |
| Mật độ mục trình bày | **≥ 1,3 hình/bảng trên trang** → 15 trang ⇒ **≥ 20 ô**; mỗi GATE **được dành trước 1 ô** (ảnh + bảng số) |
| Ảnh bắt buộc | phần tử cảm biến trên tay; jig + tải treo; oscilloscope/log; dashboard; **1 ảnh "thử nghiệm"** (trên **phantom**, chú thích rõ "chưa thử trên người") |
| TLTK | 12–15 mục, **có DOI cho ≥ 8** — chỉ cần dùng danh sách must-cite `docs/02` §10 + ledger. Đây là chỗ rẻ nhất để **hơn hẳn** benchmark (họ: 0 DOI, 9 link blog) |

### 4.3 Bốn việc nên làm, theo thứ tự tác dụng
1. **Chạy `protocols/08` GATE 0** (blocker duy nhất: bạn điền 9 ô "Chốt?" ở §7) → đổi "hứa hẹn" thành "đã có", và có **ảnh + bảng số đầu tiên**.
2. **Bỏ hết ảnh chỉ để minh hoạ** khỏi hồ sơ nộp; mỗi sơ đồ phải kèm 1 số đo hoặc 1 kết luận pass/fail.
3. **Sửa `docs/05` §1**: chốt lĩnh vực (đã gắn khuyến nghị ở trên) — việc này ảnh hưởng tới *cả danh sách đối thủ bị chấm cùng*.
4. **Chỉ báo cáo phần đã đo** theo đúng kiểu họ làm: 1 mục tiêu = 1 con số = 1 ô trình bày; phần ta *hơn* (MDC/ICC/UNRELIABLE) đặt ở **Bảng C.4** (bảng đối chiếu tiêu chí A.3 ↔ số đo), không đặt ở phần lý thuyết.

### 4.4 Năm thứ **không** nên bắt chước (để ta không tự hạ mình xuống benchmark)
1. Đo **1 lần** cho mỗi điều kiện rồi tuyên bố "đạt" (bảng 5 điểm gaze của họ) — của ta mỗi điểm ≥ 3 lần, nêu CV.
2. Trộn construct trong một chữ "accuracy" (99,2 % mức ảnh ≠ 97,11 % mức tọa độ).
3. Paste nguyên bảng log 167 dòng vào báo cáo mà **không** rút thành 1 thước đo (hình 11 của họ) — của ta: log thô để trong repo, báo cáo chỉ lấy thống kê + 1 đồ thị.
4. Đánh giá mô hình học bằng **2 ví dụ minh hoạ** (bảng 3 của họ) — nếu ta lượng tử hoá INT8 thì phải nêu **độ chính xác trên tập kiểm tra + độ trễ**, không kể chuyện "câu trả lời hay hơn".
5. TLTK toàn blog/Wikipedia. Không bắt buộc phải trích tạp chí ở vòng quốc gia, nhưng **nó rẻ** và không có lỗi gì khi làm.

---

## 5. Kết luận một câu

**Đọc xong benchmark, vị thế của đề tài bạn tốt hơn tôi đoán: về phương pháp, bạn đang ở trên mức của một báo cáo đã đoạt giải Nhất quốc gia + giải Tư ISEF; về vật thật và con số, bạn đang ở 0.** Toàn bộ khoảng cách còn lại nằm ở đúng một chỗ — `GATE 0` chưa chạy vì chưa có 9 ngưỡng được chốt — và đó là việc của chủ dự án, không phải việc của tôi.
