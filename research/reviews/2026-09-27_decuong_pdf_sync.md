# Đối chiếu bản nộp `docs/DE_CUONG.pdf` (2026-09-26) với repo — 2026-09-27

> **Mục đích:** `docs/DE_CUONG.pdf` là **bản đề cương đã nộp** (mới hơn mọi tài liệu trong repo, vốn dừng ở 2026-09-19).
> File này ghi lại: PDF nói gì, repo đang nói gì khác, chỗ nào vênh trong chính PDF, và chủ dự án cần chốt gì.
> Quy tắc: **bản nộp thắng về mặt sự kiện** (đội hình, thời gian, kiến trúc đã nộp), nhưng **repo thắng về kỷ luật bằng chứng**
> (mọi câu chữ trong PDF vi phạm `AGENTS.md`/`DEC-MSG-001` phải được gắn cờ, không được copy nguyên văn vào tài liệu khác).

---

## 1. Hồ sơ file PDF

| Mục | Giá trị |
|---|---|
| File | `docs/DE_CUONG.pdf` (1,7 MB) + bản trích text `docs/DE_CUONG.txt` (để tra cứu) |
| Độ dài | **15 trang**, 14 hình (Hình 1–14), 1 bảng (Bảng 1: C1.1–C1.10) |
| Tạo lúc | 2026-09-26 23:32 +07:00, bằng Microsoft Word for Microsoft 365 |
| Cấu trúc | 12 mục (§1 thông tin chung → §12 an toàn–đạo đức) + Tài liệu tham khảo [1]–[18] |
| Mật độ trình bày | ~1,0 ô hình/bảng mỗi trang (14 hình + 1 bảng / 15 trang) — **dưới** chuẩn `CLM-MET-004` (≥1,3) |

---

## 2. Sự kiện mới từ bản nộp (repo chưa có → đã cập nhật vào repo ở lần này)

| # | Sự kiện trong PDF | Vị trí | Cập nhật vào |
|---|---|---|---|
| F1 | **Đội hình 2 người:** Văn Ngọc Nhật Anh (11A2) + **Nguyễn Duy Quân (12A1)**, THPT Quảng Trị | §1.4 | `README.md`, `INDEX.md`, `PROJECT_SNAPSHOT.md`, `DE_CUONG_NOP_TRUONG.md` (ô danh tính) |
| F2 | **GVHD: Lê Công Long** | §1.5 | như trên |
| F3 | **Lĩnh vực dự thi: Hệ thống nhúng** (Embedded Systems) | §1.2 | `README.md`, `PROJECT_SNAPSHOT.md` — khớp khuyến nghị ở `docs/05` §1 |
| F4 | **Thời gian: 09/2026 → 01/2027**; địa điểm: phòng sáng tạo trường + nhà riêng | §7.3 | `PROJECT_SNAPSHOT.md`, `DECISION_LOG.md` (bổ sung `DEC-PLAN-001`: đã có mốc) |
| F5 | **Tên đề tài đã nộp = tên cũ** `DEC-TOPIC-019` (*"…găng tay thông minh hỗ trợ đánh giá và theo dõi…"*), **không** phải tên mới `DEC-TITLE-001` mà README 2026-09-19 ghi là "chốt" | §1.1 | `README.md` (sửa), `DECISION_LOG.md` (ghi nhận `DEC-TITLE-001` chưa từng tồn tại trong log) |
| F6 | Chuỗi tín hiệu đã nộp: **Velostat → cầu vi sai → INA333 (G=10) → ADS1115 16-bit (62,5 µV/LSB) → ESP32-S3 (IIR bậc 2 fc=10 Hz + Notch 50 Hz) → BLE → Orange Pi 5 Pro**; `R_ref = 10 kΩ` 0,1 %; đệm MCP6001; **1 IMU LSM6DS3** ở mu tay (bù nghiêng trọng trường); cảm biến **SHT30** bù trôi nhiệt–ẩm | §8–§9 | `docs/04` §8 (mới), `PROJECT_SNAPSHOT.md` §5, `CLAIM_LEDGER.csv` (`CLM-HW-003`) |
| F7 | Bộ ngưỡng nghiệm thu đã nộp: **M1–M6 + C1.1–C1.10** (bảng đối chiếu với G0.x ở §4 dưới) | §5.2, §11.1 | `README.md` §6, `PROJECT_SNAPSHOT.md` §6, `protocols/08` §7 (ghi chú, **chưa** tự chốt), `CLM-MET-005` |
| F8 | Định nghĩa đã nộp: **GAP = PROM − AROM (≥ 0°, theo giao thức, không suy nguyên nhân)**; **RAL = nấc tải nhỏ nhất (g) đạt P_complete ≥ 80 %** qua 10 chu kỳ/nấc, 120 g → 0 g; **EI** = trung vị biến thiên phổ tín hiệu vi sai chuẩn hóa theo vận tốc góc, công thức/cửa sổ/ngưỡng **cố định trước khi đo** | §8.2, §9.3, §10.3 | `CLM-DEF-001`, ghi chú ở `docs/02` §11 (mới) |
| F9 | Quy tắc vận hành đã nộp: auto-zero 3 s đầu phiên; cảnh báo khi trôi tĩnh vượt **±5 %** dải đo so với ô tham chiếu; 2 vòng lặp kín (V_base → chỉnh găng; phương sai → nhãn **"Nghi vấn"** + loại khỏi xu hướng) | §9.3, §11.2 | `PROJECT_SNAPSHOT.md`, `docs/04` §8 |
| F10 | Rig + phantom đã nộp: khung nhôm 2020, trượt tuyến tính ổ bi, vít me bước đôi + phanh từ, lò xo tải chuẩn; phantom silicone y tế **Shore A 25–30** (PDF tự ghi: *cần đối chiếu tài liệu mô mềm trước khi chốt*); load cell + **HX711 24-bit** kiểm định độc lập | §10.1 | `docs/04` §8, `research/protocols/07` (ghi chú), `EQUIPMENT_AND_ACCESS.md` |
| F11 | AAN đã nộp (chỉ trên phantom/giàn): lò xo thụ động nấc **20–120 g**; servo Bowden `F_assist = max(0, F_target − F_phantom)` + giới hạn lực cài trước; phản hồi thị giác EI + mức hỗ trợ | §10.2 | `PROJECT_SNAPSHOT.md`, `research/protocols/07` (ghi chú) |
| F12 | Ràng buộc mới: giá găng mục tiêu **< 1,5 triệu đ**; khối lượng đeo **< 150 g**; độ trễ toàn hệ thống **≤ 500 ms**; suy luận INT8 **< 15 ms**; phát hiện đeo lỏng **≥ 80 %** (M6) | §3.3, §5 | `README.md` §7, `PROJECT_SNAPSHOT.md` |
| F13 | Phạm vi người: **chỉ tự thử trên chính người thực hiện, chế độ đo, không tác động lực, tự nguyện + quy tắc dừng**; không dữ liệu người khác/bệnh nhân trước phê duyệt đạo đức | §7.2, §12 | `PROJECT_SNAPSHOT.md` §8, `DECISION_LOG.md` (`DEC-ETHICS-001` vẫn OPEN) |
| F14 | Tham khảo KTV ghi dạng ẩn danh [17] — **khớp `DEC-ROLE-001`** (không danh tính) | TLTK [17] | không cần sửa; ghi nhận tuân thủ |

---

## 3. Đối chiếu tài liệu tham khảo [1]–[18] trong PDF với `SOURCE_LEDGER.csv`

| PDF | Nội dung | Ledger | Trạng thái |
|---|---|---|---|
| [1] | Tran et al., Global Epidemiology 2025 (dịch tễ VN) | `SRC-VN-STROKE-EPI-2025` | PARTIAL — khớp |
| [2] | BYT, HD chẩn đoán & điều trị PHCN sau đột quỵ não, QĐ 4039/QĐ-BYT, 2014 | `SRC-MOH-REHAB-GUIDELINE-2014` (**mới**) | **UNVERIFIED** — chưa kiểm số QĐ/năm |
| [3] | Giáo trình PHCN (Cao Minh Châu…), NXB Y học 2020 | `SRC-REHAB-TEXTBOOK-2020` (**mới**) | **UNVERIFIED** — chưa kiểm |
| [4] | PHCN-Online.com 2024 (lượng giá chi trên, co cứng) | `SRC-PHCN-ONLINE-2024` (**mới**) | **UNVERIFIED** — chưa mở URL/bài |
| [5] | Pollock et al., Cochrane 2014 CD010820 | `SRC-COCHRANE-UE-2014` | READ_ABSTRACT — khớp |
| [6] | Langhorne et al., Lancet Neurology 2009 | `SRC-LANGHORNE-2009` (**mới**) | **UNVERIFIED** — repo trước đây chỉ trích gián tiếp qua [5] |
| [7] | Manumeter RCT, Sensors 2022;22(18):6938 | `SRC-MANUMETER-RCT-2022` | READ_ABSTRACT — khớp |
| [8] | Amin et al., IEEE OJEMB 2024 | `SRC-AMIN-2024-SPASTICITY` | READ_ABSTRACT — khớp |
| [9] | Device (Cell Press) 2024 — găng robot từ tính | `SRC-MAG-GLOVE-DEVICE-2024` | READ_ABSTRACT — khớp DOI; ⚠️ PDF §4.1 gọi là "**Gloreha** [9]" là **gán sai** (xem §5.1-I3) |
| [10] | Lin et al., Sensors 2022;22(19):7212 | `SRC-TW-SPASTICITY-2022` | READ_ABSTRACT — khớp |
| [11] | ART-Glove, arXiv:2606.16370, 2026 | `SRC-ARTGLOVE-2026` | READ_ABSTRACT — khớp ID |
| [12] | Liu et al., Engineering 2024;32:202–216 | `SRC-RECONFIG-GLOVE-2023` | VERIFIED — ⚠️ PDF §4.1 ghi "**IROS 2017** [12]" là **gán sai nhãn** (xem §5.1-I2); bài IROS 2017 thật là `SRC-ZHU-2017-GLOVE`, **không có trong TLTK của PDF** |
| [13]–[14] | ironHand 2016 + JRM 2018 | `SRC-IRONHAND-2018`, `SRC-IRONHAND-JRM-2018` | PARTIAL / READ_ABSTRACT — khớp |
| [15] | "A Systematic Review on Custom Data Gloves", *IEEE Access* 2024;12:71245–71268 | `SRC-CUSTOMGLOVE-REVIEW-2024` | READ_ABSTRACT — ⚠️ **không xác minh được locator**: bài đúng tên này tìm thấy ở *IEEE Trans. Human-Machine Systems* 54 (2024), không phải *IEEE Access* 12:71245–71268 (xem `QUERY_LOG.jsonl` Q-20260927) → ghi `UNVERIFIED` cho locator trong PDF |
| [16] | Sensors 2015;15(10):25463–25478 (vách áp điện trở) | `SRC-SIDEWALL-PIEZO-2015` | READ_ABSTRACT — khớp |
| [17] | Phỏng vấn tham khảo ẩn danh KTV VLTL–PHCN, 2026 | `SRC-KTV-INTERVIEW-2026` (**mới**, project_artifact) | OWNER_DIRECTIVE — khớp `DEC-ROLE-001` |
| [18] | "Piezoresistive characteristics of carbon-black…" *Sensors and Actuators A* 2018;279:412–421 | `SRC-VELOSTAT-CB-2018` (**mới**) | **UNVERIFIED** — tập 279 (15/08/2018) tồn tại nhưng truy vấn 2026-09-27 không tìm thấy bài khớp tên/trang (xem `QUERY_LOG.jsonl`) |

---

## 4. Bảng đối chiếu ngưỡng: repo (G0.x/M1–M6) ↔ bản nộp (C1.x/M1–M6)

> Ký hiệu: ✅ khớp · 🔀 đổi ngưỡng/định nghĩa (cần chủ dự án phê chuẩn `DEC-METRIC-002`) · ➕ mới trong PDF.

| Bản nộp | Ngưỡng trong PDF | Tương ứng repo | Kết luận |
|---|---|---|---|
| C1.1 | Nhiễu đỉnh-đỉnh `Vpp ≤ 5 mV` / 5.000 mẫu tĩnh | G0.0 bản B (`σ` / ≥5.000 mẫu) | 🔀 PDF **chốt luôn định nghĩa B** + ngưỡng tuyệt đối 5 mV (với ADS1115 62,5 µV/LSB ≈ 80 LSB — thang đo khác hẳn ngân sách ESP32-S3 trong `docs/04`) |
| C1.2 | `SNR ≥ 18 dB` (≈8×) tại ΔF=1 N, ≥10/12 kênh | G0.1 (`SNR ≥ 8 LSB`) + M1 | ✅ khớp về tỉ số (≈8×); 🔀 đơn vị đổi từ LSB sang dB, phạm vi **10/12 kênh** (repo: tồn tại `F_p`) |
| C1.3 | `γ ≥ 0,25` (≥10/12 kênh); `R² ≥ 0,90` | G0.2 (`γ ≥ 0,25` ở ≥4/5 mảng; `R² ≥ 0,95`) + M2 | 🔀 **R² hạ 0,95 → 0,90**; mẫu số đổi sang kênh |
| C1.4 | CV nội phiên ≤ 5 % (giàn cơ học) | G0.3 (`CV ≤ 5 %`) + M3 | ✅ khớp |
| C1.5 | CV liên ngày ≤ 8 % (3 ngày, tháo/đeo lại, trên phantom) | G0.4 (`ICC(3 ngày) ≥ 0,75`) + M3 | 🔀 **đổi metric ICC → CV**, nới 5 %→8 %, gắn điều kiện phantom |
| C1.6 | Hysteresis `h ≤ 18 %` | G0.5 (`hys_norm ≤ 15 %`) | 🔀 **nới 15 % → 18 %** |
| C1.7 | Creep ≤ 8 % (giữ 60 s @ 5 N) | G0.6 (`creep_2dec ≤ 3 %`, mốc 10 s→100 s) | 🔀 **đổi cả định nghĩa lẫn ngưỡng** (thang thời gian + tải khác; dễ đo tay hơn) |
| C1.8 | Trôi/tín hiệu ≤ 2,0 sau 10 ngày (qua auto-zero) | G0.7 (`drift_ratio ≤ 2` **và** trôi 10 ngày < ΔV@1N) | 🔀 **bỏ điều kiện thứ hai** (so với ΔV@1N) |
| C1.9 | Rải γ giữa mảng ≤ ±40 % (+ bảng chuẩn hóa) | G0.8 (±40 %) | ✅ khớp |
| C1.10 | `fs ≥ 20 Hz` đồng thời 12 kênh | G0.9 (`fps ≥ 20 Hz`) + M5 | ✅ khớp (⚠️ nhưng PDF §8.1/§9.1 ghi **50 Hz** — xem §5.1-I1) |
| M4 | Trôi/tín hiệu ≤ 2,0 sau 10 ngày | M4 repo (`drift/ΔV@1N < 1` + `drift_ratio ≤ 2`) | 🔀 nới theo C1.8 |
| M5 | `fs ≥ 20 Hz` + trễ toàn hệ thống ≤ 500 ms | M5 repo (`fps ≥ 20 Hz` + `latency_p95 ≤ 500 ms`) | ✅ khớp |
| M6 | Phát hiện đeo lỏng ≥ 80 % (qua phổ `V_base`) | M6 repo (bắt ≥4/5 lỗi tiêm) + GATE E (≥90 %, báo giả ≤5 %) | 🔀 **đổi metric**: repo = fault-injection; PDF = phát hiện đeo lỏng qua `V_base` |
| M2 (dải) | Dải tiền tải khả dụng **0,5–10 N**; §8.2 giả thuyết cửa sổ `Fp ∈ [0,5; 2,0] N` chờ Giai đoạn 1 xác định | `docs/02` §5.5: `F_p ≤ 68·γ·ΔF` (≈34 N với γ=0,5) | 🔀 khung khác nhau (dải vận hành/hypothesis vs cận trên lý thuyết) — tương thích được nếu đọc §8.2 là "vùng tìm kiếm", nhưng repo chưa từng nêu 0,5–10 N |

**Nguyên tắc áp dụng:** `DEC-METRIC-001` cấm đổi ngưỡng sau khi thấy số — hiện **chưa có số nào** nên việc bản nộp dùng C1.x là hợp lệ **khi và chỉ khi** chủ dự án phê chuẩn `DEC-METRIC-002`
(xem §6). `research/protocols/08` §7 giữ nguyên 10 ô chờ chốt; đã thêm ghi chú trỏ sang bảng này.

---

## 5. Sổ vấn đề (issue register)

### 5.1 Vênh *trong chính PDF* (không sửa PDF; ghi để bản sau sửa)

| ID | Vấn đề | Chi tiết |
|---|---|---|
| I1 | **50 Hz vs 20 Hz** | §8.1 lấy mẫu `fs = 50 Hz`, §9.1 BLE 50 Hz, nhưng M5/C1.10 nghiệm thu `≥ 20 Hz`. Chưa rõ 50 Hz là cấu hình chạy còn 20 Hz là sàn nghiệm thu, hay là số sót. |
| I2 | **"[12]" gán nhãn IROS 2017** | §4.1 viết "IROS 2017 [12]" nhưng TLTK [12] là Liu et al., *Engineering* 2024. Bài IROS 2017 thật (Liu et al., DOI 10.1109/IROS.2017.8206575 = `SRC-ZHU-2017-GLOVE`) **không có trong TLTK**. |
| I3 | **"[9]" gán cho Gloreha** | §4.1 viết "Gloreha [9]" nhưng [9] là bài *Device* 2024 về găng robot điều khiển từ tính — không phải sản phẩm Gloreha. |
| I4 | **TLTK [15] sai địa chỉ?** | "IEEE Access 2024;12:71245–71268" không xác minh được; bài đúng tên này thuộc *IEEE Trans. Human-Machine Systems* 54 (2024). Cần đối chiếu lại toàn văn. |
| I5 | **TLTK [18] chưa xác minh** | Không tìm thấy bài khớp tên/trang trong *Sensors and Actuators A* 2018;279:412–421 qua truy vấn 2026-09-27. |
| I6 | **"12 kênh vi sai" mơ hồ** | §7.1: 3 ngón × 2 khớp (MCP, PIP/IP) "tạo thành 12 kênh đo vi sai". 6 khớp × 1 cặp vách = 6 cặp vi sai, không phải 12 — trừ khi mỗi khớp có 2 cặp (PDF không nói). Mâu thuẫn hoặc thiếu định nghĩa với §9.1 ("12 phần tử"). |
| I7 | **Nguồn góc cho GAP/Angular velocity chưa rõ** | GAP (PROM−AROM, đơn vị độ) và "vận tốc góc cùng phiên" (chuẩn hóa EI) cần đo góc, nhưng kiến trúc chỉ còn **1 IMU LSM6DS3 ở mu tay** (bù nghiêng) — không còn 6 IMU đo góc khớp như `DE_CUONG_NOP_TRUONG.md` §4.1. PDF không nêu góc khớp lấy từ đâu (IMU đơn? goniometer thủ công trên giàn? suy từ ADC — điều bị cấm?). |
| I8 | **Dải tiền tải hai số** | M2: 0,5–10 N; §8.2: giả thuyết [0,5; 2,0] N. Cần một câu nối ("vùng tìm kiếm" vs "dải vận hành"). |

### 5.2 Câu chữ trong PDF vi phạm kỷ luật claim của repo (gắn cờ, không copy sang tài liệu khác)

| ID | Câu trong PDF | Vi phạm | Cách nói đúng (đã có trong repo) |
|---|---|---|---|
| L1 | "**triệt tiêu** trôi đồng pha / nhiễu đồng pha" (Tóm tắt, §4.3, §6.2/H1, §8.3, C1.8) | `AGENTS.md` §1 + `DEC-MSG-001`: cấm "triệt tiêu/loại bỏ drift" | "**giảm** thành phần đồng pha; phần dư được định lượng bằng C1.8/GATE C" |
| L2 | H1: "cho phép **đo chính xác lực ép**" | `AGENTS.md` §1: cấm ADC→N khi chưa hiệu chuẩn từng kênh với chuẩn lực | "ghi **tín hiệu vi sai** tỉ lệ với lực ép; chưa quy đổi ra newton" |
| L3 | "xác định **trực tiếp** hướng gập/duỗi" (§4.3) | `DEC-MSG-001`: hướng khớp là **suy luận**, không phải đo | "suy luận dấu gập/duỗi từ hiệu hai vách" |

> Ghi chú trung thực: L1–L3 là chữ trong **bản đã nộp** — repo không sửa được quá khứ. Sổ này tồn tại để (a) bản báo cáo sau không lặp lại,
> (b) khi giám khảo hỏi, nhóm trả lời bằng cột "cách nói đúng".

### 5.3 Vênh *trong repo* lộ ra khi đối chiếu (sửa ở lần này hoặc ghi nợ)

| ID | Vấn đề | Xử lý 2026-09-27 |
|---|---|---|
| R1 | README ghi tên mới "`DEC-TITLE-001` chốt 2026-09-19" + link `2026-09-19_title_options.md` — nhưng **quyết định không có trong `DECISION_LOG.md`** và **file không tồn tại**; bản nộp dùng tên cũ | Đã sửa README: tên đã nộp = `DEC-TOPIC-019`; `DEC-TITLE-001` hạ thành đề xuất chưa duyệt, chờ `DEC-TITLE-002` |
| R2 | **GAP ba định nghĩa:** README/`DE_CUONG_NOP_TRUONG` = AROM−PROM (độ IMU); `docs/02` §7.3 = A(PROM)−A(AROM) (mẫu chuẩn hóa ∫\|d\|dt); PDF = PROM−AROM (độ, theo giao thức) | Ghi `CLM-DEF-001` (PROPOSED): lấy định nghĩa PDF làm chuẩn nộp; `docs/02` §11 + README sửa theo; chờ chủ dự án phê chuẩn |
| R3 | **EI ba định nghĩa:** README/`DE_CUONG_NOP_TRUONG` = median\|d\|/(1+κ\|v̂\|); `docs/02` §7.3 = E/(E+E_nền) ∈ (0,1]; `protocols/07` ≈ E/(E+E_nền); PDF = mô tả chữ (trung vị biến thiên phổ, chuẩn hóa vận tốc góc, công thức cố định trước khi đo) | Như R2: PDF thắng về "đã nộp", nhưng PDF chưa cho công thức → công thức tường minh vẫn nợ, gắn vào `DEC-METRIC-002` |
| R4 | **RAL hai định nghĩa:** README/`DE_CUONG_NOP_TRUONG` = hỗ trợ thực/yêu cầu ∈ [0,1]; `docs/02` §7.3 + `protocols/07` + PDF §10.3 = nấc tải nhỏ nhất (g) đạt P_complete ≥ 80 % | Như R2: lấy định nghĩa PDF (gam + giao thức 10 chu kỳ/nấc 120→0 g) |
| R5 | `docs/04` = ADC ESP32-S3 12-bit + R_f≈R_sensor (ngân sách 100 kΩ/10-bit/1,51 mV); PDF = ADS1115 16-bit + INA333 G=10 + R_ref=10 kΩ | Không xóa ngân sách cũ (lịch sử thiết kế); thêm `docs/04` §8 = cấu hình đã nộp + bảng delta; chờ `DEC-HW-005` |
| R6 | README đếm "141 nguồn / 81 truy vấn" nhưng file thật là 140 dòng nguồn / 79 truy vấn (trước lần này) | Đã sửa theo số đếm thật (sau lần này: 146 nguồn, 81 truy vấn) |
| R7 | `docs/05` §2 + §10 còn DOI SSRN preprint và arXiv số cũ cho [Custom Gloves Review]; `A.1` còn gán 80 % cho Hendricks 2002 | Nợ cũ, nhắc lại: `docs/05` là outline nội bộ (không nộp) nên không chặn; A.1 chờ chủ dự án sửa (đã nêu trong `DE_CUONG_NOP_TRUONG.md`) |

---

## 6. Quyết định cần chủ dự án chốt (agent đề xuất, không tự phê)

| ID đề xuất | Nội dung | Vì sao cần |
|---|---|---|
| `DEC-SYNC-001` | Công nhận `docs/DE_CUONG.pdf` (2026-09-26) là **baseline đã nộp**; mọi tài liệu repo sau này đối chiếu về nó | Chặn drift giữa "đã nộp" và "đang viết" |
| `DEC-TEAM-001` | Ghi nhận đội hình 2 người + GVHD Lê Công Long + timeline 09/2026–01/2027 + địa điểm (từ §1/§7.3 PDF) | Điền nốt danh tính còn thiếu trong repo |
| `DEC-TITLE-002` | Tên chính thức = tên trong PDF (tức giữ `DEC-TOPIC-019`); `DEC-TITLE-001` (README 2026-09-19) **hủy** vì chưa từng được duyệt | Dọn mâu thuẫn R1 |
| `DEC-HW-005` | Chốt chuỗi đo đã nộp (ADS1115 + INA333 + MCP6001 + SHT30 + 1 IMU + R_ref=10 kΩ) thay ngân sách `docs/04` cũ; đồng thời trả lời I6/I7 (12 kênh là gì; góc khớp lấy từ đâu) | Nếu không chốt, `GATE 0` §3 (đo R_max của ESP32-S3+Mux) lạc khỏi kiến trúc đã nộp |
| `DEC-METRIC-002` | Phê chuẩn bộ C1.1–C1.10 + M1–M6 trong PDF làm ngưỡng chốt trước khi đo (thay các giá trị G0.x cũ ở §4); chốt nốt công thức EI tường minh + định nghĩa GAP/RAL theo `CLM-DEF-001` | `DEC-METRIC-001` yêu cầu ngưỡng chốt trước khi đo — PDF đã chứa ngưỡng nhưng chưa có quyết định phê chuẩn trong log |
| `DEC-SCOPE-005` | Phạm vi ngón: 3 ngón (cái/trỏ/giữa) như PDF, hay giữ lộ trình 5 ngón trong `docs/04` cấu hình 1/2? | Ảnh hưởng số kênh, ngân sách, jig GATE 0 |

---

## 7. Việc đã làm trong lần đồng bộ này (2026-09-27)

1. Cài đặt lại môi trường theo `README.md` §12: `.venv` (numpy/matplotlib/scikit-learn + pypdf để trích PDF), `bootstrap_research_tooling.sh`
   (5 checkout + 4 skill links OK), `check_research_environment.py` = **10/11** (thiếu `pdflatex` như mọi khi — xem `research/tooling/SETUP_STATUS.md`).
2. Trích text PDF → `docs/DE_CUONG.txt`; viết file đối chiếu này.
3. `SOURCE_LEDGER.csv` +7 dòng (`SRC-DECUONG-PDF-2026-09-26`, `SRC-MOH-REHAB-GUIDELINE-2014`, `SRC-REHAB-TEXTBOOK-2020`,
   `SRC-PHCN-ONLINE-2024`, `SRC-LANGHORNE-2009`, `SRC-KTV-INTERVIEW-2026`, `SRC-VELOSTAT-CB-2018`) — trừ dòng PDF, còn lại đều `UNVERIFIED`.
4. `CLAIM_LEDGER.csv` +3 dòng (`CLM-HW-003`, `CLM-MET-005`, `CLM-DEF-001`), trạng thái `PROPOSED`, chờ §6.
5. `DECISION_LOG.md`: ghi nhận §6 (6 ID đề xuất) + trạng thái các quyết định liên quan.
6. `README.md` / `INDEX.md` / `PROJECT_SNAPSHOT.md`: đội hình, GVHD, timeline, lĩnh vực, tên đã nộp, ngưỡng C1.x, kiến trúc đã nộp, số đếm ledger.
7. `docs/04` +§8 (cấu hình đã nộp), `docs/02` +§11 (ghi chú định nghĩa), `DE_CUONG_NOP_TRUONG.md` (điền 4 ô danh tính từ PDF),
   `protocols/08` §7 (ghi chú trỏ sang bảng §4 — **không** tự chốt ô nào), `protocols/07` + `EQUIPMENT_AND_ACCESS.md` (rig/phantom theo PDF).
8. Log 2 truy vấn xác minh [15]/[18] vào `QUERY_LOG.jsonl` (kết quả: `UNVERIFIED`).
9. Chạy `build_context_bundle.py` (bundle ở `research/generated/`, không commit).

**Không làm (vượt quyền agent):** chốt ngưỡng, chốt kiến trúc, đổi tên đề tài/repo, đo đạc, viết firmware/script phân tích (`DEC-PHASE-001` vẫn hiệu lực),
sửa chữ trong PDF, trích nguồn `UNVERIFIED` vào văn bản nộp.
