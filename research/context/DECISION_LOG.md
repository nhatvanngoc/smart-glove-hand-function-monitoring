# Decision log

Only an explicit project-owner or authorized review decision may close an architecture/safety item. Agents may propose but must not self-approve project-scope decisions.

| ID | Date | Decision | Authority | Status | Evidence / consequence |
|---|---|---|---|---|---|
| DEC-PROC-001 | 2026-08-16 | Pin third-party research/tooling by commit under `.tools/sources/`. | repository setup task | IMPLEMENTED | `tools/research_sources.lock.json` |
| DEC-PROC-002 | 2026-08-16 | Store durable context, searches, claims and review dissent in tracked ledgers. | repository setup task | IMPLEMENTED | `research/`; `AGENTS.md` |
| DEC-PROC-003 | 2026-08-16 | Treat synthetic outputs as simulation only. | safety/evidence protocol | IMPLEMENTED | `AGENTS.md` |
| DEC-TOPIC-001 | 2026-08-25 | Abandon "adaptive air cushion + AAC"; redirect to Smart Insole Edge-AI (3D-GRF & COP). | project owner | SUPERSEDED by DEC-TOPIC-017 |  |
| DEC-TOPIC-002 | 2026-08-25 | Refine topic: novelty = longitudinal drift-robust kinetic monitoring. | project owner | SUPERSEDED |  |
| DEC-TOPIC-003 | 2026-08-25 | Delete all air-cushion/AAC old-topic files. | project owner | IMPLEMENTED | git history |
| DEC-TOPIC-017 | 2026-08-26 | Chốt Hướng C (DFU tissue stiffness monitoring). | project owner | SUPERSEDED by DEC-TOPIC-018 | |
| DEC-TOPIC-018 | 2026-08-28 | **PIVOT: Drop Hướng C (DFU). Chốt đề tài mới: Găng tay cảm biến áp lực Velostat + TinyML INT8 theo dõi định lượng chức năng bàn tay sau đột quỵ tại nhà (longitudinal hand motor function monitoring).** Lý do drop DFU: GATE 3 (Usefulness) yếu — stiffness proxy chưa có bằng chứng RCT lâm sàng cho longitudinal monitoring. Gap mới được xác nhận bởi expert panel quốc tế (Remote Monitoring Spasticity 2024, Birmingham) và OTHER study 2026. | project owner | ADOPTED | `research/context/PROJECT_SNAPSHOT.md` |
| DEC-HW-001 | 2026-08-28 | Phần cứng (phiên bản đầu): Velostat + copper tape sensing element (6 vùng: 5 ngón + lòng bàn tay) + găng tay in 3D + Arduino Mega 2560 + Orange Pi 5 Pro RK3588 (INT8 NPU). | project owner | SUPERSEDED by DEC-HW-003 (phần Mega 2560; phần Velostat/OPi giữ nguyên) | |
| DEC-HW-002 | 2026-08-28 | **Nguyên lý cơ học thiết kế:** Khung cứng exoskeleton ép sát ngón tay. Khi ngón tay chuyển động theo hướng X → đụng vào vách khung hướng X → tạo áp lực lên dải Velostat hướng X → ADC đọc lực → dịch thành vector hướng X. Cho phép tái tạo flexion/extension từng lóng tay dưới dạng mô hình bàn tay 3D. Khác biệt so với găng tay Velostat thông thường (đo lực tiếp xúc trực tiếp): đây đo **lực hướng** qua vách khung → mã hóa được hướng chuyển động. | project owner | ADOPTED | |
| DEC-ETHICS-001 | OPEN | Determine human-participant route with affiliated fair/IRB before any recruitment. | qualified IRB/SRC | PENDING | |

| DEC-TOPIC-019 | 2026-09-13 | **Chốt TÊN ĐỀ TÀI CHÍNH THỨC:** *"Nghiên cứu và phát triển găng tay thông minh hỗ trợ đánh giá và theo dõi chức năng vận động bàn tay trong phục hồi chức năng sau đột quỵ"*. Tên cũ có cụm "hệ thống … TinyML … giá thấp" bị bỏ vì dài, và vì "TinyML/giá thấp" là **phương tiện**, không phải đối tượng nghiên cứu. | project owner | ADOPTED | `README.md`; `docs/01_Topic_Definition.md`; `docs/bao_cao/A1_ly_do_chon_de_tai.md` |
| DEC-HW-003 | 2026-09-13 | **Đổi vi điều khiển thu thập: Arduino Mega 2560 → ESP32-S3**, kết hợp **CD74HC4067** (MUX 16:1). Lý do: Mega chỉ ADC 10-bit, cồng kềnh, không có truyền không dây, và **mức logic 5 V buộc phải có level shifter** sang Orange Pi 3.3 V. ESP32-S3: ADC1 12-bit, 240 MHz, BLE 5, logic 3.3 V khớp trực tiếp Orange Pi. **Đánh đổi phải ghi nhận:** ADC ESP32-S3 kém tuyến tính hơn danh định → bắt buộc hiệu chuẩn ADC và chỉ dùng ADC1; số chân ADC ít nên MUX là bắt buộc. | project owner (đề xuất) + phân tích kỹ thuật | ADOPTED | `docs/04_Hardware_Architecture.md` |
| DEC-HW-004 | 2026-09-13 | **Chốt bố trí kênh 2 giai đoạn.** *Cấu hình 1 (12 kênh, bring-up + GATE 0/A):* 4 ngón dài × 2 khớp (MCP, PIP) + ngón cái × 2 khớp + lòng bàn tay × 1 + ô tham chiếu × 1 = 11 kênh đo + 1 tham chiếu; 1× CD74HC4067. *Cấu hình 2 (24 kênh, GATE A/B/C/D/E):* mỗi khớp có **cặp sensing element đối xứng trên hai vách đối diện** → **đọc vi sai** (`d = S_palmar − S_dorsal`) để lấy dấu gập/duỗi và triệt thành phần drift đồng pha; 4 ngón dài × 2 khớp × 2 vách = 16, ngón cái × 2 khớp × 2 vách = 4, lòng bàn tay × 2, ô tham chiếu × 2; 2× CD74HC4067 dùng chung 1 chân ADC1, chọn chip bằng chân EN (không dùng ADC2 vì xung đột với Wi-Fi). | project owner + phân tích kỹ thuật | ADOPTED | `docs/04_Hardware_Architecture.md` |
| DEC-METRIC-001 | 2026-09-13 | **Ngưỡng PASS/FAIL của GATE phải chốt TRƯỚC khi đo**, ghi vào `research/protocols/06_glove_hand_GATE_experiment.md`; cấm chỉnh ngưỡng sau khi xem kết quả. GATE C (độ nhạy phát hiện thay đổi) là **cổng sống còn**: nếu không đạt thì dừng đề tài, không viết báo cáo như thể thành công. | project owner | ADOPTED | `research/protocols/06_glove_hand_GATE_experiment.md` |
| DEC-MSG-001 | 2026-09-13 | **Ngôn ngữ bắt buộc:** dùng "**suy luận** hướng gập/duỗi" — không dùng "đo góc khớp"; "**giảm ảnh hưởng** drift" — không dùng "loại bỏ drift"; hệ thống là "**găng tay đánh giá và theo dõi**" — không phải robot/găng tập phục hồi chức năng. | project owner | ADOPTED | `docs/bao_cao/GLOSSARY.md` |
| DEC-REPO-001 | 2026-09-13 | **Đề nghị đổi tên repo GitHub** `velostat-smart-insole-dfu` → `smart-glove-stroke-hand-rehab` cho khớp đề tài. Agent **không thực hiện được**: token của phiên không có quyền Administration (HTTP 403). Cần chủ dự án chạy `gh repo rename`. | project owner | PENDING (chờ chủ dự án) | `README.md` mục 9 |
| DEC-CLINICAL-001 | 2026-08-28 | **KTVVLTL-PHCN xác nhận pain point** (3 câu hỏi thực địa). Kết quả: (1) FMA/ARAT/Box and Block chỉ cho "ảnh chụp tại thời điểm", không longitudinal. (2) Khoảng giữa hai lần tái khám là **"hộp đen"** — không biết bệnh nhân tập đúng không, tiến triển thế nào. (3) Thiết bị tại nhà HỮU ÍCH nếu: chỉ số có ý nghĩa lâm sàng + đủ tin cậy + đơn giản + bổ sung cho đánh giá lâm sàng chứ không thay thế KTV. | KTVVLTL-PHCN (chị tác giả) | CONFIRMED | Ghi chép phỏng vấn thực địa 2026-08-28 |
| DEC-CLINICAL-002 | 2026-08-28 | **Xác nhận độc lập thứ hai:** Chuyên gia PHCN tại phcn-online.com và chị KTV (hai nguồn độc lập trong nghề) đều đánh giá đề tài *"đáng đặt chân và nghiên cứu"*. Xác nhận tính cấp thiết và hướng tiếp cận phù hợp thực tiễn lâm sàng. | Chuyên gia PHCN (phcn-online.com) + KTVVLTL-PHCN | CONFIRMED | Tham khảo 2026-08-28 |

## Open decisions (owner response required)

```
[X] Tên đề tài tiếng Việt chính thức  -> CHỐT 2026-09-13 (DEC-TOPIC-019)
[X] Số sensing element và layout      -> CHỐT 2026-09-13 (DEC-HW-004): 12 kênh (tối thiểu) / 24 kênh (vi sai)
[X] Vi điều khiển thu thập            -> CHỐT 2026-09-13 (DEC-HW-003): ESP32-S3 + CD74HC4067
[ ] Chốt dùng Cấu hình 1 trước rồi mới lên Cấu hình 2, hay làm thẳng Cấu hình 2?
[ ] Giao thức bài tập chuẩn: thứ tự, số lần, thời gian giữ, thời gian nghỉ (cần chốt cùng KTVVLTL-PHCN)
[ ] Chỉ số chính cho đường cong theo tuần: biên độ lực / thời gian / phân bố / độ mượt?
[ ] Baseline so sánh chính: Box and Block / lực kế / ARAT?
[ ] Giá trị R_f và dải R_sensor làm việc (phải đo trước)
[ ] Đổi tên repo GitHub (chờ chủ dự án chạy gh repo rename)
```
