# Rà soát Gate 0 + đề cương A/B/C — 2026-10-19 (lượt tài liệu)

> **Trạng thái:** báo cáo rà soát của agent, **không phải** quyết định dự án và **không phải** bằng chứng thử nghiệm. Mọi đề xuất ở đây chờ chủ dự án duyệt.
> **Ủy quyền:** chỉ đạo chủ dự án ngày 2026-10-19 — *"hoàn thiện đề cương/hồ sơ trước, sau đó mới bắt đầu code"*; phạm vi chọn: tài liệu/hồ sơ (`docs_first`), nhánh thị giác theo kiến trúc OpenCV cổ điển + detector cắm được, **chưa commit GitHub**, **cập nhật sổ tay nhật ký trên Drive**.
> **Căn cứ đọc trước khi sửa (theo `AGENTS.md`):** `CURRENT_SUBMISSION_2026-10-17.md`, `DECISION_LOG.md`, `PROJECT_SNAPSHOT.md`, `CURRENT_DESIGN_BASELINE.md`, `IMPLEMENTATION_PIPELINE.md`, `CLAIM_LEDGER.csv`, `SOURCE_LEDGER.csv`, `protocols/09`, `skills/vietnamese-proposal-writing/SKILL.md`, `tooling/WRITING_STYLE_PROFILE.md`, `docs/01`, `docs/04`, `docs/06`, `research/notebook/*`, `research/notebooklm_sync/experiments/*`, `3d_model` (liệt kê), Drive folder `04_So_tay_nhat_ky_nghien_cuu` + `00_HUONG_DAN.md`.

---

## 1. Đã tạo / đã sửa

### Tạo mới (tất cả ở mức `PROPOSED`)

| Tệp | Nội dung | Vai trò trong pipeline |
|---|---|---|
| `research/protocols/10_gate0_task_state_sheet.md` | thông số tác vụ thìa/vùng đích (mọi ô số `OPEN`), kiểu cầm, định nghĩa `PLACE_OK`/`RELEASE`/`DROP`/`MISPLACE`/`UNKNOWN`, 14 nhãn trạng thái `T_*` kèm nguồn bằng chứng bắt buộc, máy trạng thái chế độ `SAFE_STOP/ASSIST/EVAL/AAN/TASK/INVALID/FAULT`, 5 phương pháp ứng viên phân biệt vận động tự nguyện vs do actuator tạo, must-have vs mở rộng, sơ đồ ngón↔cảm biến↔actuator, danh sách 10 mục `OPEN` + ai chốt, yêu cầu log tối thiểu | Gate 0 artifact #1 và #3 |
| `research/protocols/10a_gate0_channel_map_and_acquisition_budget.md` | ràng buộc đã chốt và hệ quả số học 16 − 3 = 13 (trần, không phải số Velostat), 4 phương án phân bổ PA-1/PA-2/PA-3a/PA-3b kèm bảng đánh đổi và khuyến nghị, bản đồ CH0–CH15, điểm lắp + phương pháp hiệu chuẩn, công thức ngân sách quét + ví dụ `[TÍNH TOÁN]`, đồng bộ thời gian camera↔ESP32↔servo, **8 câu hỏi kỹ thuật phải kiểm tra trước khi cấp nguồn**, khối lượng/chi phí (mục tiêu, chưa cân/chưa kiểm toán), 6 việc để đóng Gate 0 | Gate 0 artifact #2 |
| `research/protocols/10b_channel_map_proposed.csv` | bản đồ kênh dạng máy đọc được (PA-2 + biến thể PA-3a), mỗi dòng có `status` và `evidence_label`; dùng làm đầu vào sinh `channel_map.h` khi bắt đầu code | Gate 0 artifact #2 |
| `docs/07_Vision_TaskState_Architecture.md` | vai trò/ranh giới camera, giả định cảnh, kiến trúc detector cắm được (ClassicCV mặc định; MediaPipe/YOLO/Depth-Anything là ứng viên chưa nhận; RL ngoài phạm vi), schema đầu ra detector, ánh xạ detector → nhãn `T_*` + hysteresis + quy tắc `UNKNOWN`, bản ghi hiệu chuẩn camera/tỷ lệ, yêu cầu phản hồi trực quan, schema serial Orange Pi→ESP32-S3 kèm bất biến an toàn, phiếu benchmark (mọi ô số `OPEN`), 7 bước thực hiện | Gate 3 |
| `docs/08_Software_Firmware_Roadmap.md` | 8 nguyên tắc bất biến khi code (không hardcode ngưỡng; `null` → từ chối chạy chế độ đánh giá; băm phiên bản cấu hình; mô phỏng ≠ số đo; log bất biến; an toàn ở tầng thấp; không KTV; module nào cũng có test), kiến trúc phần mềm, bố trí thư mục đề xuất, 7 pha F0–F7 với đầu vào/đầu ra/exit/điều cấm, đồ thị phụ thuộc, môi trường & công cụ (kèm giới hạn mạng của sandbox), 7 việc cần chủ dự án chốt để bắt đầu code, bảng rủi ro | lộ trình code sau Gate 0 |
| `research/notebook/2026-10-19_NHAT_KY_BO_SUNG_GATE0_VA_KE_HOACH_CODE.md` | mục nhật ký mới theo 5 trường Điều 14 (thời gian — nội dung — phương pháp — kết quả — vai trò thành viên), ô vai trò thành viên và ô xác nhận GVHD **để trống** | sổ tay nghiên cứu |

### Sửa (nhỏ, có chủ đích)

| Tệp | Sửa gì |
|---|---|
| `docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md` | header: ghi rõ "cập nhật lần 2", thêm liên kết 5 hồ sơ kỹ thuật mới, thêm `DEC-SENSE-001`; §B.2: thay câu chung về phân bổ kênh bằng 4 phương án + trần 13 kênh; §B.3: thêm đoạn về máy trạng thái và 5 phương pháp tách vận động tự nguyện; **thêm §C.4** bảng đăng ký trước 14 chỉ số (cột ngưỡng `OPEN` + cột căn cứ để chốt) và 4 quy tắc đi kèm; **thêm §C.5** thứ tự triển khai công cụ, nói rõ chưa viết code. Giữ nguyên cấu trúc A/B/C + Tài liệu tham khảo |
| `research/context/IMPLEMENTATION_PIPELINE.md` | Gate 0/Gate 3/Gate 4: thêm khối "Drafted 2026-10-19 (PROPOSED)" trỏ tới artifact mới, ghi rõ chưa pass gate; §4: thêm dòng trạng thái lượt tài liệu |
| `research/protocols/09_...md` | §7: thêm ghi chú cập nhật; 9 dòng `OPEN` nay trỏ tới bản đề xuất tương ứng — **vẫn `OPEN`**, không dòng nào chuyển thành "đã chốt" |
| `research/context/DECISION_LOG.md` | thêm 6 dòng đề xuất `DEC-TASK-001`, `DEC-TASK-002`, `DEC-CHMAP-001`, `DEC-ACQ-001`, `DEC-VIS-001`, `DEC-IMPL-001`, `DEC-IMPL-002` (7 mã, đều `PROPOSED`) và 5 mục checklist mới trong khối open decisions |
| `research/claims/CLAIM_LEDGER.csv` | thêm 6 claim (`CLM-TASK-001`, `CLM-ACQ-001`, `CLM-ACQ-002`, `CLM-HW-006`, `CLM-VIS-002`, `CLM-IMPL-001`); cập nhật `next_action` của `CLM-SENSE-001`, `CLM-FLEX-001`, `CLM-VISION-001` để trỏ tới bản đề xuất |
| `research/context/PROJECT_SNAPSHOT.md`, `README.md`, `INDEX.md`, `research/README.md`, `research/context/CURRENT_SUBMISSION_2026-10-17.md`, `research/tooling/SETUP_STATUS.md` | đăng ký tệp mới, ghi trạng thái triển khai 2026-10-19, ghi chú lượt chỉ-sửa-tài-liệu và giới hạn mạng của sandbox cho pha code |

---

## 2. Kết quả rà soát đề cương A/B/C trước khi sửa

| # | Phát hiện | Mức độ | Xử lý |
|---|---|---|---|
| 1 | Đề cương liệt kê chỉ số dự kiến ở §C.2 nhưng **không có bảng đăng ký trước** (định nghĩa, đơn vị, cách đo, ngưỡng, căn cứ) → dễ bị hội đồng hỏi "chốt tiêu chí trước hay sau khi đo" | cao (phương pháp luận) | thêm §C.4 với 14 chỉ số, cột ngưỡng để `OPEN` toàn bộ |
| 2 | §B.2 nói "còn tối đa 13 kênh" nhưng không có phương án cụ thể → không thể kiểm tra tính khả thi | cao (kỹ thuật) | liên kết `10a`/`10b`; nêu 4 phương án và đánh đổi ngay trong đề cương |
| 3 | §B.3 nói chuyển mode "tự động theo quy tắc ngưỡng" nhưng **không nói làm sao biết chuyển động là do người tập chứ không do servo** | cao (logic điều khiển) | thêm đoạn dẫn tới `protocols/10` §5 (5 phương pháp ứng viên); nêu trong đề cương rằng đây là điều kiện tiên quyết |
| 4 | Không có phần nào nói **khi nào bắt đầu code, theo thứ tự gì** → người đọc không thấy đường từ đề cương tới sản phẩm | trung bình | thêm §C.5 + `docs/08` |
| 5 | Câu chữ target/result: rà lại toàn bộ §A–§C, các phát biểu đều ở dạng "dự kiến/mục tiêu/chưa đo"; không tìm thấy chỗ nào biến kế hoạch thành kết quả | đạt | giữ nguyên, chỉ bổ sung |
| 6 | Tuyên bố cấm: quét chuỗi `đầu tiên`, `first to`, `5 N`, `F_assist`, `Newton`, `chứng minh hiệu quả`, `an toàn tuyệt đối`, `đã thử nghiệm trên` trong các tệp mới/sửa → mọi lần xuất hiện đều nằm trong câu **cấm/không dùng**, không có chỗ nào khẳng định | đạt | giữ nguyên |
| 7 | Danh tính: đề cương không nêu tên KTV/người được tham khảo (đúng `DEC-ROLE-001`); không có ô danh tính nào được agent tự điền | đạt | giữ nguyên |
| 8 | Tham khảo [1][2] vẫn ở mức "tài liệu tham khảo làm việc" với cảnh báo đối chiếu toàn văn; **chưa** xác minh toàn văn trong lượt này; vấn đề gán sai nguồn `SRC-HENDRICKS-2002-MOTORRECOVER` vẫn còn nợ từ 2026-09-19 | còn nợ | ghi vào mục 5 dưới đây, không tự sửa trích dẫn |
| 9 | Bản DOCX review trên Drive (`11A2_CAP_NHAT_DU_THAO_2026-10-19.docx`) dựng từ draft cũ → **chưa dựng lại** vì bản Markdown chưa được duyệt (đúng `AGENTS.md`) | đúng quy trình | không làm |

---

## 3. Phát hiện kỹ thuật mới cần kiểm tra (không phải tuyên bố lỗi)

| # | Phát hiện | Vì sao quan trọng | Ghi nhận ở đâu |
|---|---|---|---|
| 1 | Ghi nhận dự án nói chuỗi đo đọc **toàn dải 0–3,3 V** qua PGA ADS1115 (0,125 mV/LSB). Giới hạn điện áp đầu vào tuyệt đối của ADS1115 theo datasheet **chưa được tra trong nguồn của dự án** | nếu đầu vào vượt giới hạn tuyệt đối thì có rủi ro hỏng chip/đọc sai; cần tra datasheet + đo thật trước khi cấp nguồn cho găng tích hợp | `CLM-HW-006`, `10a` §7.1 |
| 2 | Bảng tốc độ khung ở `docs/04` §5 (12 kênh → ~415 Hz) giả định **ADC nội ESP32-S3, 200 µs/kênh**; chuỗi hiện hành là MUX → ADS1115 860 SPS + 300 µs settling + đọc nháp. Phép tính lại cho ≈ 24–54 Hz tuỳ số kênh | mục tiêu thiết kế cũ 45–100 Hz có thể **không đạt** với chuỗi 16-bit; ảnh hưởng trễ điều khiển và đồng bộ với camera | `CLM-ACQ-002`, `10a` §5 |
| 3 | PA-3a: ADS1115 có `A1–A3`; chuỗi hiện tại dùng `A0` cho MUX → nếu board đưa `A1–A3` ra chân hàn thì đọc 3 Flex thẳng vào đó, **giải phóng 3 kênh MUX** và tránh ADC1 nội phi tuyến | tăng trần Velostat và giảm rủi ro tuyến tính cho tín hiệu gập–duỗi | `10a` §2 PA-3a, `10b` |
| 4 | `experiments/05` ghi nhận sự cố **ground loop** khi kẹp mass oscilloscope; bản tích hợp sẽ có thêm servo (nguồn đóng cắt) và Orange Pi | nhiễu/mất ổn định khó truy nguyên nếu không có quy tắc nối mass và tách nguồn servo | `10a` §7.5–§7.6 |
| 5 | Flex cần điện trở phân áp riêng; **không** được lấy giá trị datasheet thay phép đo dải điện trở thật | chọn sai điện trở → mất dải đo hoặc mất độ nhạy đúng lúc cần phân biệt gập/duỗi | `10a` §7.3 |
| 6 | Preload Velostat thay đổi theo **nấc kẹp nẹp** (`docs/06` §2.4) → điểm làm việc dịch giữa các lần đeo | nếu không ghi nấc kẹp/preload vào log thì không so sánh được giữa các phiên | `10a` §4 |
| 7 | Một tang kéo cả ba ngón vs ba tang/ba servo: ảnh hưởng trực tiếp tới khả năng tạo dáng cầm tripod và khối lượng cụm đeo (mục tiêu 80–120 g) | quyết định cơ khí phải có **trước** Gate 2, nếu không phải làm lại nẹp | `10` §7, `DECISION_LOG` checklist mới |
| 8 | Servo cuốn dây một chiều **không** tự tạo ra duỗi/hồi dây | đây là phụ thuộc rủi ro cao nhất của chức năng thìa; cần thiết kế + thử không tải trước | `protocols/09` §3.2 (đã có), nhắc lại ở `10` §8 |

---

## 4. Kiểm tra đã chạy trong lượt này

| Kiểm tra | Kết quả |
|---|---|
| Quét chuỗi tuyên bố bị cấm trong tệp mới/sửa | mọi lần xuất hiện đều ở câu cấm — không có khẳng định vi phạm |
| Kiểm tra liên kết tương đối trong 16 tệp mới/sửa | **0 liên kết gãy** |
| Toàn vẹn `CLAIM_LEDGER.csv` | 53 dòng dữ liệu, **đều 11 cột**, `claim_id` không trùng |
| `scripts/check_bench_templates.py` | **PASS** cả 3 template (không sửa header cũ, không tạo log giả) |
| `git diff --check` | không có lỗi khoảng trắng |
| `research/bench/logs/` | vẫn **rỗng** — đúng quy tắc, không tạo dữ liệu giả |
| Quét liên kết gãy trên **93** tệp Markdown của repo | 1 liên kết gãy, **có từ trước lượt này**: `research/reviews/2026-10-17_11A2_docx_audit.md` trỏ tới `docs/11A2_CAP_NHAT_DU_THAO_2026-10-19.docx` — tệp không có trong repo (chỉ tồn tại bản trên Drive, và bản đó đã lỗi thời). Đã xử lý bằng **addendum có ngày** trong tệp audit + chú thích lại `INDEX.md`; không sửa dòng gốc, không dựng lại DOCX |
| Toàn vẹn `SOURCE_LEDGER.csv` | 170 dòng dữ liệu, đều 8 cột, ID không trùng (không thêm nguồn mới trong lượt này) |

Các kiểm tra trên là **kiểm tra cấu trúc/tính nhất quán**, không phải bằng chứng kỹ thuật hay bằng chứng gate đã đạt.

---

## 5. Không làm trong lượt này (nói rõ để khỏi hiểu nhầm)

- **Không viết code, không viết firmware, không dựng pipeline thị giác, không làm dashboard.** Theo chỉ đạo chủ dự án, code bắt đầu sau khi đề cương/Gate 0 được duyệt.
- **Không chạy benchmark nào** trên Orange Pi 5 Pro hay bất kỳ phần cứng nào; không có số độ đúng/độ trễ/fps nào được tạo ra.
- **Không đo phần cứng**, không tạo log bench, không "chính thức hoá" dữ liệu bring-up cũ thành log GATE 0 (việc này vẫn còn nợ theo `CLM-EVID-002`).
- **Không điền bất kỳ ngưỡng, thông số tác vụ, kích thước, thời gian hay giá trị an toàn nào.** Mọi ô số để `OPEN`.
- **Không sửa** `docs/DE_CUONG.pdf`, `docs/DE_CUONG_NOP_TRUONG.md`, `de_cuong/*`, `exports/*`, các tệp lịch sử, và **không sửa** `11A2.pdf` / `11A2.docx` / `11A2_CAP_NHAT_DU_THAO_2026-10-19.docx` trên Drive.
- **Chưa dựng lại DOCX review** (chờ duyệt bản Markdown).
- **Chưa commit/push GitHub** theo yêu cầu chủ dự án; thay đổi nằm trên nhánh làm việc của phiên này.
- **Không tra cứu nguồn mới trên mạng** trong lượt này, nên không có `SOURCE_LEDGER` mới; việc đọc toàn văn 5 nguồn hệ trọng và **tra bằng sáng chế theo IPC có hệ thống** vẫn còn nợ từ 2026-09-19 (`DEC-NOV-001`).
- Giới hạn của lượt rà soát: đây là phân tích của **một** agent trong **một** ngữ cảnh, không phải phản biện độc lập đa chiều theo `ISEF_REVIEW_ORCHESTRATION.md`; không được mô tả như "review độc lập". Các nhận định ở mục 3 là **phân tích thiết kế**, không phải số đo.

---

## 6. Cần chủ dự án quyết định (theo thứ tự chặn việc)

| Mã | Việc cần duyệt | Nếu chưa duyệt thì chặn gì |
|---|---|---|
| `DEC-TASK-001` | tờ yêu cầu tác vụ + bộ nhãn `T_*` + máy trạng thái | Gate 1, Gate 3, Gate 5; chưa viết được F0/F1 |
| `DEC-CHMAP-001` | chọn PA-1 / PA-2 / PA-3a / PA-3b và bản đồ CH0–CH15 | firmware F2, schema F0 |
| `DEC-TASK-002` | chọn 1 trong 5 phương pháp tách vận động tự nguyện vs do máy | không được đặt đặc trưng/ngưỡng chuyển mode (F4) |
| `DEC-ACQ-001` | tốc độ khung mục tiêu + SPS + N (sau khi đo) | F2, đồng bộ camera–servo |
| `DEC-VIS-001` | kiến trúc detector cắm được, OpenCV cổ điển trước | F5 |
| `DEC-IMPL-001/002` | lộ trình F0–F6; nơi đặt mode supervisor | toàn bộ pha code |
| — | cơ cấu hồi/nhả + một tang hay ba tang | Gate 2 (rủi ro cao nhất) |
| — | tham chiếu lực/căng dây độc lập + quy trình hiệu chuẩn | mọi phát biểu về lực, và Gate 2 |

---

## 7. Bước tiếp theo đề xuất

1. Chủ dự án duyệt/chỉnh 6 mã quyết định ở mục 6; agent cập nhật `10`/`10a`/`10b`/`docs/07`/`docs/08` thành bản đã duyệt, đổi `status` từng dòng và ghi `layout_revision`.
2. Nhóm kiểm tra 8 điểm ở `10a` §7 trên board thật (một buổi, có ảnh + ghi vào sổ tay), đặc biệt mục ADS1115 và `A1–A3`.
3. Duyệt đề cương A/B/C bản cập nhật lần 2 → dựng lại DOCX review **mới** (không ghi đè bản Drive cũ) nếu chủ dự án yêu cầu.
4. Bắt đầu F0 + F1 + F5 (không cần phần cứng) theo `docs/08`; song song làm Gate 2 về cơ cấu hồi/nhả vì đây là rủi ro cao nhất.
5. Trả nợ cũ còn mở: chính thức hoá dữ liệu bring-up thành log GATE 0 hợp lệ (`CLM-EVID-002`), tra IPC có hệ thống, xác nhận SHT30/AHT20 (`CLM-HW-004`), xuất CAD Mech 9.
