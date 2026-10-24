# Đọc `11A2.pdf` và đề xuất hướng cải thiện trước hạn nộp — 2026-10-20

> **Nguồn đọc:** `11A2.pdf` trên Google Drive, ID `1uJDGpTx_sR1P1VCsHM1fv6hrnCzMgDaJ`, 779.014 B, md5 `aa846313e3631803de34e296fd095b8b`, modifiedTime `2026-10-19T01:27:30Z`, 12 trang. **Tệp nguồn không bị chỉnh sửa.**
> **Loại tài liệu:** đề xuất cải thiện của agent theo yêu cầu chủ dự án. **Không phải** phản biện y khoa độc lập, **không** xác nhận tính đúng của bất kỳ số đo nào, **không** phải bản duyệt.
> **Căn cứ đối chiếu:** `CURRENT_DESIGN_BASELINE.md`, `DECISION_LOG.md` (đến `DEC-MECH-007` ngày 2026-10-20), `docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md` (lần 3), `research/protocols/10`–`10a`–`10b`, `docs/04` §4–§9, `docs/06`, `3d_model/custom_exo/fixation_mechanisms_benchmark/`, `research/notebooklm_sync/experiments/05,07`, `research/reviews/2026-10-17_11A2_docx_audit.md`.

---

## 0. Độ phủ trích xuất (khai báo trung thực)

Công cụ đọc Drive trả về toàn bộ chữ trong PDF nhưng kết quả bị cắt ở giữa do giới hạn dung lượng; tôi đã đọc lại bằng nhiều lát cắt để phủ phần lớn văn bản.

| Vùng | Trạng thái đọc |
|---|---|
| Mục lục, A.1–A.4, B.1, B.2 (đầu), B.4, B.5, B.6 (tiêu đề), C.1 (bảng Mech), C.2, Bảng 3, C.3 (câu mở đầu + chỉ tiêu 1), C.5 (phần thân), C.6, Tài liệu tham khảo [1]–[12] | **Đọc nguyên văn** |
| B.2 (phần còn lại), B.3 (thiết kế khung nẹp + cấu trúc cảm biến vi sai hai vách), B.6 (nội dung AAN/RL), C.1 (đoạn mở đầu), C.3 (chỉ tiêu 2–10), C.4, C.5 (câu mở đầu), chú thích Hình 1–10 | **Không trích xuất được** — mọi nhận định về các vùng này dựa trên mục lục của PDF và bản audit DOCX 2026-10-17, **phải mở PDF kiểm tra trực tiếp trước khi sửa** |
| Hình ảnh, công thức dạng ảnh, bố cục trang | Không đọc được (chỉ đọc chữ). PDF có Hình 1–10 và công thức EI dạng toán học |

Vì vậy: các mục dưới đây ghi rõ **câu trích nguyên văn** (tin được) và **suy ra từ bản DOCX cũ** (cần kiểm tra lại).

---

## 1. Kết luận chính

1. **Vấn đề lớn nhất không phải câu chữ, mà là trục đề tài.** `11A2.pdf` vẫn được viết quanh trục **"thiết bị đo lường"**: câu hỏi nghiên cứu là *tín hiệu áp trở có đủ lặp lại không*, bộ ba chỉ số **EI/GAP/RAL** là sản phẩm chính, cảm biến là **ma trận 16 phần tử Velostat vi sai hai vách**, và có hẳn một mục cho **Học tăng cường (RL)**. Hướng hiện hành (`DEC-REHAB-001`, Giai đoạn 7, và ba quyết định ngày 2026-10-20) là **"găng hỗ trợ tập vận động tinh"**: 3 bước *hỗ trợ gập–duỗi → tự động chuyển AAN → bài tập gắp thìa bằng ba ngón*, **3 Flex + 6 Velostat (PA-2, 11 kênh)**, có **camera**, **không RL**, **không Newton**. Vá câu chữ trên trục cũ sẽ không ra bản nộp nhất quán.
2. **Cùng một bộ số đang được dùng vừa làm mục tiêu vừa làm kết quả đã đạt.** A.4 gọi SNR ≥ 18 dB, R² ≥ 0,90, f_s ≥ 20 Hz là *"ngưỡng mục tiêu kỹ thuật dự kiến"*; Bảng 3 ở C.2 ghi **SNR = 21,4 dB, R² = 0,93, 25 Hz, 0,00 mV** ở cột "Vòng lặp 2" đặt cạnh cột "Mục tiêu đề ra"; C.5 kết luận đã **"triệt tiêu hoàn toàn"**; trong khi C.3 nói sẽ **"kiểm định 10 chỉ tiêu kỹ thuật… từ tháng 10/2026 đến tháng 01/2027"**. Bốn con số đó **không có log/biên bản nào trong repo** (`research/bench/logs/` chỉ có `README.md`; quét toàn repo không thấy `21,4`/`0,93`/`25 Hz` ở đâu ngoài bản audit 17/10).
3. **Phần A đã tốt hơn hẳn bản DOCX 17/10 và nên giữ nguyên.** Penfield có nguồn riêng [11], Hebb [12], GAP = PROM − AROM đúng chiều và ghi rõ "đo bằng công cụ ngoài", Manumeter ~31% đã diễn giải đúng đại lượng, và có câu chặn *"đề tài không đo hoạt động vỏ não hay chứng minh sự tái tổ chức thần kinh"*. Danh mục [1]–[12] khớp với `SOURCE_LEDGER.csv`.

---

## 2. Bảng đối chiếu PDF ↔ hướng hiện hành

| # | `11A2.pdf` nói (trích/ý) | Hướng hiện hành + căn cứ | Mức |
|---|---|---|---|
| 1 | A.3: vấn đề nghiên cứu = *"mảng cảm biến áp trở trên khung nẹp có tạo được tín hiệu đủ lặp lại… và tự động phát hiện phiên đo lỗi do lỏng nẹp hay không"* | `DEC-REHAB-001`: chức năng là **hỗ trợ tập vận động tinh** (3 bước, bài tập thìa), đo lường là phương tiện | P0 |
| 2 | B.1/C.5: *"ma trận 16 phần tử cảm biến áp trở Velostat… hai vách lòng–mu"*, *"chế tạo thành công"* | `DEC-SENSE-001` (3 Flex) + **`DEC-CHMAP-001` ADOPTED 2026-10-20 = PA-2**: 3 Flex + **6** Velostat + 2 ô tham chiếu = **11 kênh quét**. Chưa chế tạo cấu hình này | P0 |
| 3 | A.4: *"Trợ lực AAN giới hạn lực an toàn ≤ 5 N trên mô hình silicone"*; B.1: *"chỉ bù đúng phần lực thiếu hụt"*; B.5: EI dùng `F_net`/`F_target` | Baseline: **đã rút** luật Newton `F_assist` và tiêu chí 5 N; Velostat **không quy đổi Newton** (`CLM-HW-005`: 16–48 % FS + trễ đàn hồi) | P0 |
| 4 | B.6 (tiêu đề): *"Cơ chế trợ lực theo nhu cầu (AAN) và mô hình Học tăng cường (RL)"* | `DEC-RL-001/002`: **RL ngoài phạm vi**; `DEC-REHAB-001` + A/B/C §B.2: "Không đưa RL vào phạm vi hiện hành" | P0 |
| 5 | Không có camera, không có bài tập thìa, không có chuyển chế độ tự động | `DEC-REHAB-001`; `docs/07` (nhánh thị giác); `DEC-TASK-001` (tờ yêu cầu tác vụ); **`DEC-TASK-002` ADOPTED = M3** | P0 |
| 6 | Không có cơ cấu ba tang / nhả dây chủ động; AAN "truyền động qua dây cáp" chung chung | **`DEC-MECH-007` ADOPTED 2026-10-20**: ba tang riêng + servo nhả dây chủ động, không lò xo/khớp 4 khâu | P0 |
| 7 | Bảng 3 + C.2 + C.5: SNR 21,4 dB, R² 0,93, 25 Hz, 0,00 mV, "triệt tiêu hoàn toàn", "phẳng tuyệt đối" | `DEC-PHASE-002`: bring-up là **ghi nhận thật nhưng chưa chính thức hoá GATE** (thiếu `session_manifest`/`perturbation_log`/`reference_check` theo `protocols/08a`); `research/bench/logs/` **rỗng**; `DEC-METRIC-001`: ngưỡng chốt trước khi đo | P0 |
| 8 | C.1: Mech 9 *"Đạt tối ưu"*, 22 s, sau 50 chu kỳ; C.5 *"hỗ trợ người bệnh tự thao tác… bằng một tay"* | `DEC-MECH-006`: Mech 9 **chưa có CAD trong repo, chưa xác nhận in thử/đo độ bền**; checklist 2026-10-12 còn nợ xuất `.step`/`.stl` + in thử | P0 |
| 9 | C.6: *"thử nghiệm đối chứng lâm sàng với thang đo FMA-UE và ARAT trên người bệnh thực tế"* sau IRB | Baseline: **bench/phantom trước**; thử có cấp nguồn trên **người khỏe** chỉ **có điều kiện** sau rà an toàn + phê duyệt; **không thử bệnh nhân** trong phạm vi hiện tại; không tuyên bố hiệu quả lâm sàng | P0 |
| 10 | A.4: *"Quét 16 kênh với tần số tối thiểu 20 Hz/kênh"* | Nhập nhằng **Hz/kênh** vs **Hz/khung**. `10a` §5 `[TÍNH TOÁN]`: 16 kênh + đọc nháp ≈ **24 Hz toàn khung**; PA-2 (11 kênh) ≈ **35 Hz toàn khung**. `DEC-ACQ-001` **chưa đo** | P1 |
| 11 | B.2: găng robot thương mại *"dễ gây phản xạ co cứng chống đối và tạo tâm lý ỷ lại"* (không có citation tại câu) | `CLM-*`/ledger: nhận định lâm sàng khái quát cần nguồn trực tiếp hoặc hạ thành ví dụ có dẫn nguồn | P1 |
| 12 | Không có **đăng ký trước chỉ số**, không có khối lượng/chi phí, không nhắc nhật ký nghiên cứu/minh chứng quá trình; khuôn **A/B/C + Tài liệu tham khảo** thì đúng | Khuôn đã chốt: **`DEC-PROP-004` (ADOPTED 2026-10-19) = A/B/C + Tài liệu tham khảo, do giới hạn trang** → PDF đúng khuôn, không phải lỗi. Thiếu: A/B/C §C.4 đã soạn bảng đăng ký trước 14 chỉ số; `DEC-MASS-001`/`DEC-COST-002` (**chưa cập nhật cho ba tang**); Điều 14 nhật ký nghiên cứu | P1 |

---

## 3. P0 — sáu việc phải làm trước khi nộp

### P0-1. Chọn lại trục đề tài, rồi mới sửa câu chữ

Giữ trục "thiết bị đo" thì mọi mục sau sẽ lệch nhau (A.3 hỏi về độ lặp lại tín hiệu, nhưng C.5 kết luận về AAN và EI/GAP/RAL, còn hướng hiện hành nói về bài tập thìa). Đề xuất trục mới, đúng ba bước của `DEC-REHAB-001`:

> *Găng tay ba ngón hỗ trợ người tập sau đột quỵ đi từ vận động gập–duỗi cơ bản đến một thao tác vận động tinh có mục đích (gắp thìa → di chuyển → đặt vào vùng đích), trong đó bộ điều khiển tự động giảm dần trợ lực khi phát hiện vận động chủ động; toàn bộ chức năng được kiểm chứng trên bàn thử và mô hình tay giả trước.*

Kèm theo, câu hỏi nghiên cứu nên đổi từ *"tín hiệu có đủ lặp lại không"* thành hai tầng: (a) tín hiệu Flex/Velostat có đủ tin cậy để **làm đặc trưng chuyển chế độ** không; (b) cơ cấu ba tang + nhả dây chủ động có tạo được **dạng kẹp ba chấu** và **duỗi chủ động** không. Đây là hai câu hỏi mà dự án thật sự phải trả lời ở Gate 1/Gate 2.

### P0-2. Tách bạch "đã đo — ghi nhận sơ bộ — mục tiêu chưa đo" (bảng 3 cột)

Đây là lỗi nặng nhất về mặt bằng chứng và cũng dễ sửa nhất. Đề xuất thay cách trình bày Bảng 3 bằng bảng 3 cột, áp dụng cho từng con số đang có:

| Con số trong PDF | Xếp loại đúng theo bằng chứng repo | Cách viết đề xuất |
|---|---|---|
| Bão hòa ngõ ra INA333 ≈ 2838 mV khi siết nẹp; cầu phân áp sụt < 1,42 V | **Ghi nhận dự án** (`experiments/05,07`; `DEC-PHASE-002`) | "Quan sát trên bàn đo: … (ghi nhận bring-up, chưa formal hoá thành log GATE)" |
| Nhiễu nền 50–135 mV khi giãn màng | **Ghi nhận dự án** | như trên |
| Đọc nháp + 300 µs khử bóng ma kênh; dead-band 180 mV; EMA α = 0,20 | **Tham số thiết kế đã áp dụng** | "Tham số xử lý tín hiệu đang dùng: …" |
| **0,00 mV "phẳng tuyệt đối"** | **Hệ quả của ngưỡng hoá**, không phải nhiễu vật lý biến mất | "Sau vùng chết 180 mV, đầu ra ở trạng thái nghỉ bị ghim về 0; **điều này không có nghĩa nhiễu nền đã mất** — nhiễu thô 50–135 mV vẫn còn trước lọc" |
| **SNR = 21,4 dB; R² = 0,93** | **Không có artifact truy vết trong repo** | Hoặc nộp kèm log/biên bản + định nghĩa phép tính (cửa sổ tín hiệu/nhiễu, số điểm tải, số lần lặp, tải chuẩn tạo bằng gì), hoặc **bỏ khỏi bản nộp** và chuyển thành "chưa đo, sẽ đo ở Gate 1" |
| **25 Hz toàn khung 16 kênh** | Khớp phép tính `[TÍNH TOÁN]` của `10a` §5 (≈24 Hz) nhưng **chưa đo** | "Ước tính từ thời gian chuyển kênh + đọc nháp: ≈24–25 Hz toàn khung 16 kênh; **phải đo lại** với cấu hình PA-2 11 kênh" |
| **"Triệt tiêu hoàn toàn"** bão hòa/nhiễu xuyên kênh/trôi đàn hồi | Vượt bằng chứng | "Giảm đáng kể hiện tượng X trong các lần thử trên bàn đo; chưa kiểm chứng dài hạn/nhiều mẫu" |
| SNR ≥ 18 dB, R² ≥ 0,90, CV ≤ 5 %/8 %, h ≤ 18 %, creep ≤ 8 % | **Mục tiêu đăng ký trước** (`DEC-METRIC-002` vẫn PROPOSED) | Giữ ở cột "mục tiêu", ghi rõ "chưa đo" |

Nguyên tắc: **một con số chỉ được xuất hiện ở một cột**. Nếu vừa là mục tiêu vừa là kết quả thì người chấm có quyền hiểu là đã đạt.

### P0-3. Gỡ ngôn ngữ Newton và ngưỡng 5 N

Ba chỗ phải sửa: A.4 (*"giới hạn lực an toàn ≤ 5 N"*), B.1 (*"chỉ bù đúng phần lực thiếu hụt"*), B.5 (EI có `F_target` ở mẫu số). Hướng sửa:

- Đổi đơn vị: dùng **"đáp ứng áp trở tương đối (ΔV/đơn vị ADC sau hiệu chuẩn)"** hoặc **chỉ số trong-người**; nói rõ Velostat có sai số 16–48 % FS và trễ đàn hồi theo y văn nên **không quy đổi Newton** khi chưa hiệu chuẩn từng kênh bằng tải chuẩn.
- Giới hạn an toàn nên phát biểu bằng **đại lượng kiểm soát được**: giới hạn hành trình, giới hạn góc kéo, giới hạn dòng/mô-men servo, cơ cấu nhả khi mất nguồn, và nút dừng — thay vì một con số lực mà dự án **không có thiết bị đo độc lập** để kiểm chứng (`10` §8 mục 9 còn `OPEN`).
- EI: hoặc định nghĩa lại **không dùng lực** (ví dụ tỷ lệ giữa tích phân đáp ứng trong pha chủ động và mức tham chiếu của chính phiên đó), hoặc ghi rõ đây là **chỉ số đề xuất chưa kiểm chứng** và `F_target` lấy từ đâu.

### P0-4. Bỏ RL khỏi tiêu đề/nội dung B.6, thay bằng quy tắc chuyển chế độ đã duyệt

`DEC-RL-001/002` đặt RL ngoài phạm vi; A/B/C §B.2 ghi "Không đưa RL vào phạm vi hiện hành". Đề xuất đổi B.6 thành **"Cơ chế trợ lực theo nhu cầu (AAN) và quy tắc tự động chuyển chế độ"**, nội dung:

- servo cuốn dây câu cá trực tiếp lên **ba tang riêng** (`DEC-MECH-007`), duỗi bằng **nhả dây chủ động**;
- chuyển `ASSIST → AAN` **tự động**, không cần kỹ thuật viên nhấn nút;
- phương pháp phân biệt vận động tự nguyện với chuyển động do máy tạo: **M3** — cửa sổ thăm dò tự nguyện (`DEC-TASK-002`), kèm ghi chú trung thực *"đã chọn phương pháp, chưa kiểm chứng; độ dài cửa sổ và tiêu chí dừng còn trống; bắt buộc rà an toàn trước khi chạy có cấp nguồn"*;
- máy trạng thái chế độ `SAFE_STOP/ASSIST/EVAL/AAN/TASK/INVALID/FAULT` (`protocols/10` §4) — đây là nội dung "an toàn" cụ thể mà bản PDF hiện thiếu.

Nếu nhóm muốn giữ RL như hướng tương lai, chỉ đặt ở **C.6 Hướng phát triển**, một câu, không kèm tuyên bố năng lực.

### P0-5. Sửa phần cảm biến cho khớp PA-2 và thêm nhánh camera + bài tập thìa

- Thay "ma trận 16 phần tử Velostat" bằng **3 Flex (cái/trỏ/giữa) + 6 Velostat cặp lòng–mu + 2 ô tham chiếu = 11 kênh quét trên CD74HC4067 → ADS1115** (PA-2, đã duyệt 2026-10-20), 5 kênh dự phòng. Ghi rõ **vị trí lắp và dải điện trở Flex thật còn phải đo**.
- Sửa A.4 *"20 Hz/kênh"* thành **tốc độ khung** (toàn bộ 11 kênh/giây) và ghi là **mục tiêu chưa đo** (`DEC-ACQ-001`).
- Thêm một mục ngắn về **camera**: nhận biết thìa + vùng đích, nhãn trạng thái tác vụ, phản hồi trực quan; kiến trúc detector cắm được, xử lý ảnh cổ điển chạy trước trên Orange Pi 5 Pro (`docs/07`); **mọi chỉ số độ đúng/độ trễ/fps để trống** vì chưa benchmark.
- Thêm **bài tập thìa** như một tác vụ đánh giá chức năng (tỷ lệ hoàn thành, thời gian, số lần rơi) — lấy từ `protocols/10`, với các ô kích thước/khoảng cách/thời gian **còn `OPEN` chờ đo vật thật**.

### P0-6. Hạ mức khẳng định ở C.1/C.5 và siết ranh giới con người ở C.6

- Mech 9: đổi **"Đạt tối ưu"** → *"phương án triển vọng nhất trong 9 phương án đã in thử; **chưa có bản vẽ CAD trong kho dự án và chưa đo độ bền chu kỳ theo biên bản**"* (đúng `DEC-MECH-006`). Bảng C.1 nên thêm cột **"Ngày thử / số lần lặp / người thử"** — hiện bảng có thời gian đeo (55–80 s, 40–65 s, 28 s, 22 s) và "sau 50 chu kỳ" mà không có ngày, không có số lần lặp, không nói đo bằng gì.
- C.5: đổi *"chế tạo thành công ma trận 16 phần tử"* → *"đã lắp và thử trên bàn đo các phần tử Velostat theo cấu trúc vi sai hai vách; cấu hình PA-2 (3 Flex + 6 Velostat) **chưa chế tạo**"*; đổi *"xây dựng hoàn chỉnh mô hình toán học"* → *"đã viết định nghĩa toán học của ba chỉ số; **chưa kiểm chứng bằng dữ liệu**"*.
- C.6: giữ IRB nhưng viết lại theo đúng ranh giới hiện hành: **(1)** bench/phantom trước; **(2)** thử có cấp nguồn trên **người trưởng thành khỏe mạnh** chỉ **sau khi** rà an toàn đạt và có phê duyệt/chấp thuận phù hợp; **(3)** nghiên cứu trên **người bệnh** và đối chứng lâm sàng FMA-UE/ARAT là **hướng dài hạn ngoài phạm vi đề tài này**, không phải bước kế tiếp tự động; **(4)** không tuyên bố hiệu quả phục hồi, không tuyên bố dùng tại nhà đã xác nhận, không tuyên bố an toàn đã chứng nhận, không tuyên bố "đầu tiên"/tính mới.

---

## 4. P1 — nên sửa nếu còn thời gian

1. **Khuôn nộp đã chốt, không cần bàn lại:** `DEC-PROP-004` (ADOPTED 2026-10-19) chấp nhận **A/B/C + Tài liệu tham khảo do giới hạn trang**, thay cho khuôn 6 mục của thông báo trường (`DEC-PROP-003`). PDF hiện đã đúng khuôn này → **không đổi khuôn**. Hệ quả thực tế: vì bị giới hạn trang, mọi nội dung thêm vào (PA-2, M3, ba tang, camera, bài tập thìa) phải đi kèm một danh sách **cắt bớt**, xem mục 4a.
2. **4a. Đề xuất ưu tiên trang (nếu bản nộp bị giới hạn độ dài):**
   - **Giữ nguyên/ưu tiên cao:** câu chuyện hai vòng lặp phần cứng ở C.2 (điểm mạnh nhất); bảng 3 cột "đã đo – sơ bộ – mục tiêu"; bảng đăng ký trước chỉ số (nén còn 8–10 dòng, cột ngưỡng để trống); ranh giới con người ở C.6; danh mục tài liệu tham khảo.
   - **Nén mạnh:** A.2.1 (vỏ não/Hebbian) rút còn 3–4 câu + câu chặn hiện có; B.4 (DSP 4 bước) chuyển công thức thành một bảng tham số 4 dòng; C.1 giữ bảng, bỏ mô tả từng phương án.
   - **Cắt hẳn:** nội dung RL (chỉ để 1 câu ở C.6 nếu muốn); các nhận định thị trường không dẫn nguồn ở B.2; mọi con số không có artifact truy vết (P0-2).
3. **Thêm bảng đăng ký trước chỉ số** (14 chỉ số, cột ngưỡng để trống) — đã soạn sẵn ở A/B/C §C.4, chỉ việc đưa vào; đây là điểm cộng lớn với người chấm vì chống "chọn ngưỡng sau khi thấy kết quả".
4. **Thêm khối lượng và chi phí (1–2 câu):** `DEC-MASS-001` (80–120 g cụm đeo, **chưa cân**) và `DEC-COST-002` (1,0–1,3 triệu / ~5,5 triệu, **dự toán chưa kiểm toán**) — và ghi rõ cả hai **chưa cập nhật cho phương án ba tang** (`DEC-MECH-007`).
5. **Citation:** [1] khớp `SRC-VN-STROKE-EPI-2025` (VERIFIED, đối chiếu toàn văn qua PMC); [5] khớp `SRC-COCHRANE-UE-2014`; [7] khớp `SRC-MANUMETER-RCT-2022` (READ_FULL); [11] `SRC-PENFIELD-1937-HOMUNCULUS` (VERIFIED gián tiếp, chưa đọc bản scan 1937); [12] `SRC-HEBB-1949-ORGANIZATION` (READ_SECONDARY_CONFIRMED); [4] `SRC-GORDON-2023-SCAN` (mới đối chiếu abstract). **Đề xuất:** thêm DOI cho [5], [7], [9], [10]; với [11]/[12] giữ mức xác minh gián tiếp trong hồ sơ nội bộ — không cần nói trong bản nộp, nhưng không được nâng cấp thành "đã đọc toàn văn".
6. **Giữ ý "tự động phát hiện phiên đo lỗi do lỏng nẹp"** (A.3): đây là ý hay và **nối thẳng vào 2 ô tham chiếu `REF_1/REF_2` của PA-2** — nên giữ và gắn vào thiết kế kênh thay vì bỏ đi khi viết lại A.3 (P0-1).
7. **B.2:** nhận định về CPM/sEMG/"tâm lý ỷ lại" cần nguồn tại câu hoặc hạ thành ví dụ có dẫn nguồn ([9] là một găng robot cụ thể, không chứng minh cho cả thị trường).
8. **Hình:** Hình 1–10 và công thức EI là tài sản của bản PDF; bản Word dựng từ Markdown hiện **không có hình**. Nếu nộp bản mới, cần quyết định chèn lại hình nào (đặc biệt Hình 10 Serial Plotter và bảng Mech) và kiểm tra công thức/đơn vị/chú thích khi xuất PDF — công cụ đọc của tôi chỉ trích xuất chữ nên **chưa xác nhận** nội dung chú thích từng hình.

---

## 5. Điểm mạnh cần GIỮ (đã tốt hơn bản DOCX 17/10)

- A.2.1 đã có câu chặn đúng: *"đề tài không đo hoạt động vỏ não hay chứng minh sự tái tổ chức thần kinh"*.
- A.2.2: **GAP = PROM − AROM** đúng chiều (`DEC-DEF-001`), kèm *"đo bằng công cụ ngoài"* và *"không xem riêng nó là phép chẩn đoán"* — đúng hai điểm mà bản DOCX từng sai.
- A.1: Manumeter ~31 % đã diễn giải đúng đại lượng (mức thay đổi cường độ sử dụng ngày) và tách riêng 100–200 lần đếm dương tính giả/giờ — bản DOCX từng gọi sai là "sai số đếm".
- A.4 đã gọi các con số là *"ngưỡng mục tiêu kỹ thuật dự kiến"* và đã có câu *"theo quy trình an toàn được phê duyệt trước khi đo"* cho thử nghiệm trên người khỏe.
- C.2 kể **hai vòng lặp thiết kế phần cứng** (INA333 G≈6,5 → sụt áp < 1,42 V → bão hòa ≈2838 mV → bỏ INA333, đọc trực tiếp PGA ADS1115): đây là **câu chuyện kỹ thuật đắt giá nhất** của hồ sơ, khớp với ghi nhận bring-up thật. Nên giữ nguyên mạch kể, chỉ đổi cách dán nhãn bằng chứng (P0-2) — kể một kết quả âm rồi quyết định đổi kiến trúc là điểm cộng, miễn là không gọi nó là GATE đã đạt.
- C.6 có nhắc IRB và phantom; danh mục tài liệu tham khảo [1]–[12] khớp `SOURCE_LEDGER.csv`.

---

## 6. Ba phương án bản nền (cần chủ dự án chọn)

| Phương án | Làm gì | Ưu | Nhược |
|---|---|---|---|
| **A — Dựng bản mới từ `docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md` (lần 3)** *(agent khuyến nghị → **chủ dự án đã chọn, 2026-10-20**)* | Bản Markdown này **đã khớp hướng hiện hành**, đã có §C.4 đăng ký trước chỉ số, §C.5 lộ trình công cụ, và ba quyết định 2026-10-20. Dựng DOCX bằng `scripts/build_abc_review_docx.py` (đã có, `--check` PASS), rồi chèn lại Hình 1–10 từ PDF nếu muốn | Nhất quán 100 % với sổ quyết định; không phải rà lại từng câu cũ; công cụ dựng đã sẵn | Mất phần văn phong/hình của bản PDF; cần duyệt toàn văn Markdown trước |
| **B — Dựng bản theo 6 mục từ `docs/DE_CUONG_NOP_BAN_KHKT_2026-10-18.md`** | Bản này viết theo thông báo của trường và đã có đoạn *Tính khả thi* viết trung thực về tiến độ GATE | Có sẵn `exports/*.docx/.pdf`; đoạn *Tính khả thi* dùng lại được | **Không khuyến nghị làm bản nền:** `DEC-PROP-004` đã chốt khuôn A/B/C do giới hạn trang. Chỉ nên **lấy lại đoạn Tính khả thi** để chèn 2–3 câu vào §C của Phương án A |
| **C — Vá trực tiếp `11A2.pdf`/`11A2.docx`** | Sửa tại chỗ 9 điểm P0 | Giữ nguyên hình ảnh, bố cục, văn phong đã có | **Không khuyến nghị:** phải sửa tận gốc trục đề tài (A.3, A.4, B.1, B.5, B.6, C.3, C.5) — thực chất là viết lại phần lớn; và tệp nguồn trên Drive là bản chỉ đọc, không được ghi đè |

---

## 7. Kế hoạch theo quỹ thời gian (chờ xác nhận hạn nộp thật)

Ghi chú: `DEC-PROP-003` ghi hạn theo thông báo của trường là **17h 18/10/2026** — đã qua. Hạn mà chủ dự án nói "sắp đến" **chưa có trong hồ sơ repo** (có thể là mốc thi dự kiến cuối tháng 11/2026 hoặc một vòng nộp bổ sung), nên cần xác nhận trước khi lập lịch. Đồng thời `DEC-PROP-004` ghi rõ khuôn A/B/C được chọn **do giới hạn trang** → trước khi viết lại phải chốt **số trang tối đa**, vì nó quyết định làm được bao nhiêu mục P0/P1.

- **Nếu còn ≤ 2 ngày:** chỉ làm P0-2 (bảng 3 cột), P0-3 (gỡ 5 N/Newton), P0-6 (hạ mức khẳng định + ranh giới con người). Đây là ba lỗi có thể khiến hồ sơ bị đánh giá là "nói quá bằng chứng". Chưa kịp đổi trục đề tài thì **không** thêm tính năng mới vào bản nộp.
- **Nếu còn 3–5 ngày:** thêm P0-1 (đổi trục + câu hỏi nghiên cứu), P0-4 (B.6 bỏ RL, đưa M3 + máy trạng thái vào), P0-5 (PA-2 + camera + bài tập thìa). Nên đi theo **Phương án A**.
- **Nếu còn ≥ 1 tuần:** làm toàn bộ P0 + P1, cộng thêm: đo **vật thật** để điền thông số bài tập thìa (`DEC-TASK-001`), cân cụm đeo nếu đã in (`DEC-MASS-001`), và chuyển số liệu bring-up tháng 10 thành **phiếu buổi đo đúng mẫu** (`protocols/08a`) để hai con số SNR/R² có thể ở lại bản nộp một cách hợp lệ.

---

## 8. Tài liệu này KHÔNG kết luận

- Không khẳng định bất kỳ con số nào trong `11A2.pdf` là sai về mặt vật lý; chỉ nói rằng **chúng thiếu artifact truy vết trong kho dự án** và **cách trình bày đang nhập mục tiêu với kết quả**.
- Không đánh giá y khoa/lâm sàng, không xác nhận thiết bị an toàn, không xác nhận hiệu quả phục hồi.
- Không kết luận về bố cục/hình ảnh/công thức trong PDF vì công cụ chỉ trích xuất chữ.
- Không tự sửa `11A2.pdf`/`11A2.docx` trên Drive; không dựng bản nộp mới cho tới khi chủ dự án chọn phương án và xác nhận khuôn/hạn nộp.
- Không điền bất kỳ ngưỡng hay thông số tác vụ nào; mọi ô `OPEN` vẫn `OPEN`.

## 9. Mã quyết định đề xuất

**`DEC-PROP-005` — ĐÃ DUYỆT 2026-10-20 (chủ dự án chọn Phương án A):** bản nền là A/B/C draft lần 3, B (lấy đoạn *Tính khả thi* từ bản 6 mục 18/10) hay C (vá `11A2.pdf`, không khuyến nghị); kèm xác nhận **hạn nộp thật** và **số trang tối đa**. Khuôn nộp không cần hỏi lại — đã chốt A/B/C + Tài liệu tham khảo bởi `DEC-PROP-004`. **Đã dựng bản nộp theo lựa chọn này** — xem §10. `DEC-PROP-006` (ADOPTED cùng ngày) chốt thêm: ≤14 trang nội dung + 1 bìa, và nguyên tắc *"đề cương không phải báo cáo toàn văn: có kết quả gì báo cáo kết quả đó và đưa ra các mục tiêu định lượng"*.

---

## 10. Bản dựng nộp theo Phương án A (thực hiện 2026-10-20, hai lượt)

**Lượt 1 — bản gọn.** Dựng `docs/DE_CUONG_A_B_C_BAN_NHAP_2026-10-20.md` → `exports/DE_CUONG_A_B_C_BAN_NHAP_2026-10-20.docx` với nội dung nén để bám trần 14 trang: 7.023 từ, 128 đoạn, 6 bảng; ước tính ≈ 13 trang chữ + ≈ 2 trang bảng.

**Lượt 2 — bản đầy đủ (theo `DEC-PROP-007`).** Chủ dự án chỉ đạo *"viết hoàn thành B/C luôn đi, phần A tham khảo bản cũ"* và *"cấu trúc này cần tái lại nội dung các mục"* → cùng tệp Markdown đó được **viết lại hoàn chỉnh**, và DOCX được dựng lại: **12.817 từ, 199 đoạn, 8 bảng, 76.078 B**, builder `--check` **PASS**. Bản DOCX rà soát của lượt trước (`exports/11A2_CAP_NHAT_DU_THAO_2026-10-20.docx`) **không bị ghi đè**.

**Lượt 3 — bản cô đọng (theo `DEC-PROP-008`).** Chủ dự án chỉ ra nguyên nhân bản lượt 2 quá dài: *"có quá nhiều câu xã giao"*, và yêu cầu đọc lại bản mẫu. Đã đọc lại toàn bộ mục A + danh mục tài liệu tham khảo của `11A2.pdf` để lấy chuẩn mật độ (A.1 của bản mẫu chỉ ~90 từ; B.1 một đoạn ~90 từ; B.2 một đoạn ~110 từ; A.4 một câu dẫn + 5 gạch đầu dòng). Viết lại theo đúng khung của bản mẫu — **A.1–A.4 · B.1–B.7 · C.1–C.6 · TLTK [1]–[15]** — kết quả **5.718 từ, 101 đoạn, 6 bảng, ~10 trang chữ**, `--check` PASS. Sáu quy tắc mật độ đã ghi thành chuẩn trong `research/tooling/WRITING_STYLE_PROFILE.md`; các câu meta không bị vứt đi mà chuyển thành **nhãn trong ngoặc, cột bảng, hoặc ghi chú nội bộ cuối tệp**.

**Lượt 3b — nén câu, giữ nguyên nội dung.** Chủ dự án yêu cầu làm gấp và *"đừng cắt bớt nội dung"*, nên chỉ nén ở mức câu chữ (bỏ từ đệm, gộp mệnh đề bằng dấu chấm phẩy, thay câu trần thuật bằng tham chiếu chéo): **5.718 → 5.519 từ**, vẫn 101 đoạn, 6 bảng, 7 chỗ chèn hình, `--check` PASS. Ước tính độ dài: 8,0 trang văn xuôi + 2,1 trang bảng + 2,3 trang cho 7 hình = **12,4 trang nội dung**, vừa trần 14 trang, dư ~1,6 trang. Muốn xuống −700 từ như phương án đã chọn thì buộc phải bỏ ý — trái với chỉ đạo *"đừng cắt bớt nội dung"* — nên dừng ở mức không mất ý nào và bù phần còn lại bằng chỗ dư trang.

**Lượt 4 — BẢN NỘP sạch (`DEC-PROP-009`).** Chủ dự án gạch một câu mẫu: *"Khác bản trước: bỏ ngưỡng 'lực an toàn ≤ 5 N'…"* và yêu cầu "một bản đề cương chuẩn để nộp". Nguyên nhân: các bản trước là **tài liệu làm việc**, mang theo cả nhật ký chỉnh sửa và vết kiểm toán. Đã dựng tệp riêng `docs/DE_CUONG_A_B_C_BAN_NOP_2026-10-20.md` (bản nội bộ `…BAN_NHAP…` giữ nguyên). Những gì bị bỏ và thay bằng gì:

| Bỏ khỏi bản nộp | Thay bằng |
|---|---|
| Câu nói về phiên bản trước ("Khác bản trước: bỏ ngưỡng ≤ 5 N…") | bỏ hẳn; ý an toàn đã nằm trong gạch đầu dòng "giới hạn an toàn đặt theo hành trình dây, góc kéo, dòng servo, hành vi nhả khi mất nguồn" |
| "bản trước ghi SNR 21,4 dB, R² 0,93 — không truy vết được" + kế hoạch ba bước hợp thức hóa | hai số chuyển hẳn thành **mục tiêu** (SNR ≥ 18 dB, R² ≥ 0,90) + một câu nói sẽ đo bằng buổi đo có biên bản, nêu định nghĩa phép tính |
| Nhãn `OPEN`, `[SƠ BỘ]`, `[MỤC TIÊU]`, `[TÍNH TOÁN]`, `[ĐÃ ĐO]` | "chưa xác định", "ghi nhận sơ bộ", "mục tiêu dự kiến, chưa đo" — và **nói một lần** ở đầu phần C |
| Mã nội bộ `PA-2`, `M3`, `Gate 0/1/2/3` | "cấu hình 11 kênh đã chọn", "phương pháp cửa sổ thăm dò", "mốc 0/1/2/3" |
| Đường dẫn tệp trong kho (`03_Serial_Plotter_exports`, `research/evidence/…`) | bỏ hẳn; ý "đối chiếu đồ thị đã xuất" gộp vào câu về buổi đo có biên bản |
| Khối banner/status/meta đầu tệp và ghi chú nội bộ cuối tệp | bỏ hẳn (bản dựng không truyền `--banner/--status/--meta`) |
| Ô Mech 7 để `⟨bổ sung hoặc ghi rõ đã bỏ qua⟩` | "không có số liệu trong hồ sơ hiện tại của nhóm" |
| "Học tăng cường không thuộc phạm vi đề tài" (câu phủ định một ý không hề được nêu) | bỏ; phạm vi đã được nói ở C.6 |

Kết quả: **5.627 từ, 100 đoạn, 6 bảng, 7 chỗ chèn hình, `--check` PASS**, ước tính **12,7 trang nội dung** — vừa trần 14 trang. Quét tự động bằng `grep` cho 0 kết quả với các từ khóa nội bộ (`OPEN`, `DEC-`, `PA-2`, `Gate`, `research/`, `Ghi chú nội bộ`, `bản trước`, `SNR 21,4`).

**Lượt 5 — sửa GIỌNG VĂN theo ví dụ chủ dự án tự viết (`DEC-PROP-010`).** Bốn lượt trước đo độ dài bằng **số từ**, nhưng chủ dự án chỉ ra vấn đề nằm ở **giọng văn**: *"Bạn vẫn chưa thấy được phong cách văn phong ngắn gọn"*, rồi đưa nguyên văn hai bản viết cùng mục A.2.1 để đối chiếu. Chẩn đoán: bản của agent nhồi ba ý vào một câu bằng dấu chấm phẩy và lược chủ ngữ kiểu điện tín, nên đọc mệt hơn dù ngắn; bản của chủ dự án **tách mỗi ý một đoạn 1–3 câu** và dùng danh hóa học thuật ("Nghiên cứu của…", "việc cung cấp…", "định hướng cho việc…"). Đã viết lại toàn bộ bản nộp theo sáu khác biệt rút ra từ ví dụ đó (ghi đầy đủ trong `research/tooling/WRITING_STYLE_PROFILE.md` mục "Giọng văn chuẩn"): đoạn ngắn; danh hóa; `[2, 3]` gộp một ngoặc và `Penfield & Boldrey` / `Gordon et al.`; số đếm bằng chữ số; liệt kê trong ngoặc đơn; caveat gắn vào mệnh đề bằng ";" thay vì đứng thành câu phòng thủ. Mục A.2.1 dùng đúng câu chữ của chủ dự án.

Kết quả: **100 → 143 đoạn**, trung bình 43 từ/đoạn (bản sai giọng: 60 từ/đoạn), 5.723 từ, 6 bảng, 7 chỗ chèn hình, ước tính **12,9 trang**, `--check` PASS. **Thước đo mới để tự kiểm:** số đoạn và số từ trung bình mỗi đoạn, không phải tổng số từ.

**Năm chi tiết thư mục được sửa nhờ đọc lại bản mẫu** (lượt 2 ghi sai): [4] *Nature* 617(7960):351–359 (đã ghi 617:359–369); [7] Schwerz de Lucena **D.** (đã ghi L.); [11] *Brain* 60:389–440 (đã ghi 60(4):389–443); [8] Amin **F.**, *Sensors*/PMC11793859 — **mâu thuẫn với `SRC-AMIN-2024-SPASTICITY`** trong sổ nguồn đang ghi *IEEE OJEMB*, phải đối chiếu lại trước khi nộp; [10] Lin B.S., *Design of a Multi-Sensor System for Exploring Upper Limb Spasticity in Stroke Patients* (lượt 2 gán nhầm sang một bài găng vải hai chiều).

**Cấu trúc bản đầy đủ:** A.1 lý do chọn đề tài · A.2 cơ sở y sinh (A.2.1 vỏ não vận động + tập luyện chủ động; A.2.2 trương lực cơ, PROM/AROM/GAP, độ tin cậy phép đo) · A.3 vấn đề nghiên cứu (2 câu hỏi + 6 nội dung + 3 bước thiết kế) · A.4 mục tiêu (tổng quát, cụ thể, **bảng 13 chỉ tiêu định lượng**) · B.1 tổng quan 4 tầng · B.2 hạn chế giải pháp hiện có (3 nhóm, mỗi nhận định có nguồn) · B.3 khung nẹp + bộ truyền ba tang · B.4 cảm biến + bản đồ kênh PA-2 + ngân sách thời gian quét · B.5 mạch thu thập + chuỗi xử lý 4 bước + hiệu chuẩn · B.6 bộ chỉ số EI/GAP/RAL + chỉ số tác vụ · B.7 AAN + M3 + **bảng máy trạng thái 7 trạng thái** · B.8 nhánh thị giác + bài tập thìa · B.9 kiến trúc phần mềm, luồng dữ liệu, nhật ký đo · B.10 khối lượng–chi phí–an toàn · C.1 chín phương án khóa nẹp · C.2 hai vòng lặp mạch + **bảng bằng chứng 3 cột** · C.3 phương pháp kiểm định (**8 quy trình đo** + điều kiện ghi nhận + tiêu chí loại phiên) · C.4 đăng ký trước **17 chỉ số** + 4 quy tắc · C.5 kế hoạch–tiến độ–tính khả thi · C.6 phạm vi thử trên người + đạo đức · C.7 sản phẩm + giới hạn · C.8 kết luận sơ bộ (đã làm / chưa làm) · C.9 hướng phát triển · Tài liệu tham khảo [1]–[16].

**Chín điểm P0 đã áp dụng:** P0-1 đổi trục đề tài sang hỗ trợ tập vận động tinh (A.3); P0-2 bảng bằng chứng 3 cột thay Bảng 3 cũ — SNR 21,4 dB và R² 0,93 được ghi rõ là **kho dự án không truy vết được**, kèm **ba bước để hợp thức hoá số liệu** (đối chiếu đồ thị trong `03_Serial_Plotter_exports`, lập phiếu buổi đo theo mẫu, ghi định nghĩa phép tính SNR/R²) ở C.2; P0-3 gỡ ngưỡng 5 N và ngôn ngữ Newton — EI bỏ `F_target`, giới hạn an toàn phát biểu bằng đại lượng kiểm soát được (A.4, B.6, B.10); P0-4 bỏ RL khỏi phạm vi, đưa M3 + máy trạng thái 7 trạng thái vào (B.7, C.9); P0-5 cập nhật PA-2 11 kênh + camera + bài tập thìa (B.4, B.8); P0-6 hạ mức khẳng định Mech 9 thành *"phương án triển vọng nhất, chưa có CAD trong kho, chưa đo độ bền theo biên bản"* và bổ sung cột truy vết ngày/số lần lặp/người thử (C.1); kết luận sơ bộ tách rõ **đã làm** và **chưa làm** (C.8); ranh giới con người: bàn thử/phantom trước, người khỏe chỉ có điều kiện, IRB là giai đoạn sau (C.6).

**Vấn đề độ dài — ĐÃ XỬ LÝ ở lượt 3, nhưng vẫn phải đếm trang thật.** Trần là **14 trang nội dung + 1 bìa** (`DEC-PROP-006`). Bản lượt 2 ~12.800 từ → ước tính **24–26 trang** ở cỡ 14 pt, giãn dòng 1,35 → **vượt trần**. Bản lượt 3 còn 5.718 từ → ~10 trang chữ, cộng 6 bảng và 7 chỗ chèn hình thì ước tính **13–14 trang, vừa trần**. Máy dựng **không có LibreOffice/pandoc** nên không xuất PDF để đếm trang; mọi con số trang ở đây là ước tính nội bộ, **phải mở trong Word để đếm trang thật**. Nếu vẫn vượt, ba cách xử lý theo thứ tự khuyến nghị (áp dụng cho bản lượt 3; bản lượt 2 giữ làm hồ sơ nội dung):

1. **Dựng bản rút gọn ≤ 14 trang** từ chính bản đầy đủ (giữ bản đầy đủ làm hồ sơ nội dung / bản báo cáo toàn văn sau này) — cần chủ dự án xác nhận để agent làm.
2. **Cắt thủ công theo thứ tự** (đã ghi ở "ghi chú nội bộ" cuối tệp Markdown): bỏ `⟨HÌNH 4⟩`, thu nhỏ `⟨HÌNH 5⟩` → nén ba đoạn B.2 thành một đoạn (giữ citation) → bỏ bảng tiến độ C.5, thay bằng ba câu → nén tám quy trình đo C.3 thành bảng bốn dòng.
3. **Đổi khổ chữ/giãn dòng** bằng cờ dựng bản: `--size=13` và/hoặc `--spacing=1.15` (ước tính còn ~19–21 trang — **vẫn chưa đủ**, nên chỉ dùng kết hợp với cách 2).

**Không cắt** trong mọi trường hợp: bảng bằng chứng 3 cột ở C.2, bảng đăng ký trước chỉ số ở C.4, các điểm giới hạn ở C.6/C.7, và phần "chưa làm được" ở C.8 — đó là những phần bảo vệ hồ sơ khỏi bị đánh giá là nói quá bằng chứng.

**Chỗ nhóm phải tự làm (agent không tự điền):** thông tin bìa (lĩnh vực, trường/CLB, thành viên, người hướng dẫn); chèn hình tại 5 khối `⟨HÌNH 1/3/4/5/6⟩`; bổ sung ngày/số lần lặp/người thử/thông số in cho bảng Mech ở C.1 (và xử lý **Mech 7 đang thiếu** dù tiêu đề nói chín phương án); đối chiếu toàn văn hoặc bỏ ba nguồn `UNVERIFIED` [2] [3] [6]; xóa khối thông tin bản dựng ở đầu tệp Word và "ghi chú nội bộ" ở cuối tệp Markdown.

**Công cụ:** `scripts/build_abc_review_docx.py` nay nhận thêm `--banner=`, `--status=`, `--meta="k=v;k=v"`, `--spacing=`, `--size=`; giá trị mặc định không đổi nên bản dựng cũ vẫn tái tạo y nguyên.

## 11. Bản sao trên Drive (tải lên mới 2026-10-20, không ghi đè tệp nào)

| Tệp trên Drive | Thư mục | ID | Ghi chú |
|---|---|---|---|
| **`DE_CUONG_A_B_C_BAN_NOP_2026-10-20_v2.docx`** (53.360 B) | `01_Cac_file_lam_viec` | **`11UW8oIMmgNtZ87IWMWbxEO5P61UlaKd0`** | **BẢN ĐỂ NỘP hiện hành** — 5.723 từ, 143 đoạn ngắn đúng giọng bản mẫu, ước tính 12,9 trang |
| `DE_CUONG_A_B_C_BAN_NOP_2026-10-20.docx` (52.774 B) | `01_Cac_file_lam_viec` | `1-jBcBMSKeA_a05STGboKMwXn7AMZYTJa` | bản nộp lượt trước, sạch câu meta nhưng **sai giọng văn** — giữ làm vết; bình luận `AAACJEo1aEk` |
| `DE_CUONG_A_B_C_BAN_NOP_CO_DONG_2026-10-20_v2.docx` (54.834 B) | `01_Cac_file_lam_viec` | `19cAEh8g02ruoBsPUOL_cj1ebtlZi9N1t` | bản nội bộ có nhãn kiểm toán — **không dùng để nộp**; bình luận `AAACI37XCmQ` |
| `DE_CUONG_A_B_C_BAN_NOP_CO_DONG_2026-10-20.docx` (55.197 B) | `01_Cac_file_lam_viec` | `176tj3MWVVa6p6tkuw-GCsKzk6GzbdE70` | bản cô đọng v1 (5.718 từ) — bị v2 thay, giữ làm vết; bình luận `AAACJC-ltuc` |
| `DE_CUONG_A_B_C_BAN_DAY_DU_2026-10-20.docx` (76.078 B) | `01_Cac_file_lam_viec` | `1PNVjezxgTSeur_nEdcLXu-BasvFIlLsr` | bản **đầy đủ**, vượt trần trang — **không dùng để nộp**; giữ làm hồ sơ nội dung cho báo cáo toàn văn. Đã để bình luận `AAACI3sp9I4` trên tệp này để không ai nhầm |
| `2026-10-20_11A2_pdf_improvement_plan.md` (32.226 B, bằng bản repo) | `04_So_tay_nhat_ky_nghien_cuu` | `1viIe0njVXkH0TCaCQFlOzDXPwkJopTpw` | chính là tài liệu này |
| bình luận trên sổ tay nhật ký | — | `AAACI4VCoFs` | trỏ tới hai tệp mới + cảnh báo vượt trang |
| bình luận trên bảng tổng hợp | — | `AAACJDB1Y4w` | như trên |
| bình luận **trên chính bản rà đã tải lên** | — | `AAACJE4lxU8` | khai báo rằng bản Drive là **ảnh chụp cũ hơn** bản repo: tệp được tải lên trước khi §10 viết lại (lượt 2) và trước khi thêm §11; **không ghi đè** để sửa, chỉ ghi chú |

`11A2.pdf` (ID `1uJDGpTx_sR1P1VCsHM1fv6hrnCzMgDaJ`) và `11A2.docx` (ID `1VbI9CRPWsx7q0o54h7lAQ4bWq9nz50PO`) **không bị chỉnh sửa**; bản `11A2_CAP_NHAT_DU_THAO_2026-10-19.docx` (ID `1YXvVbi53CPcrzXaJQAPZTQ3ugnsjhErd`) vẫn lỗi thời và không bị ghi đè.

**Chưa làm (chờ chỉ đạo):** điền bìa/thành viên/GVHD; chèn 7 hình rồi đếm trang thật trong Word; chỉnh sửa `11A2.pdf`/`11A2.docx`; commit/push; viết code/firmware; điền bất kỳ ngưỡng hay thông số tác vụ nào.
