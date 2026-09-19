# 📑 INDEX — Sơ đồ file của dự án

> **Đề tài:** Nghiên cứu và phát triển **găng tay thông minh hỗ trợ đánh giá và theo dõi chức năng vận động bàn tay trong phục hồi chức năng sau đột quỵ**
> **Học sinh:** Văn Ngọc Nhật Anh — THPT Quảng Trị
> **Cập nhật:** 2026-09-19 (lượt rà soát prior art 1; novelty dịch từ A sang C — chờ `DEC-NOV-001`)
> **Trạng thái:** định hướng + thiết kế + **prior art lượt 1 chưa hoàn tất**. **Chưa có kết quả thực nghiệm.**

---

## 🗂️ Cấu trúc hiện tại

```
.
├── README.md                      ← Giới thiệu, vấn đề, novelty, kiến trúc, setup
├── AGENTS.md                      ← Quy tắc vận hành cho mọi AI/agent (bằng chứng, an toàn, IRB)
├── INDEX.md                       ← File này
├── LICENSE
├── requirements.txt               ← numpy, matplotlib, scikit-learn
├── docs/
│   ├── 01_Topic_Definition.md         ← Đề tài, RQ 2 tầng, novelty, pipeline, killer experiment
│   ├── 02_Theoretical_Foundation.md   ← CƠ SỞ LÝ THUYẾT (phục hồi vận động, thang đo, Velostat, drift, edge-AI)
│   ├── 03_Literature_Gap_Analysis_Plan.md ← Kế hoạch rà soát khoảng trống 2011–2026
│   ├── 04_Hardware_Architecture.md    ← Bố trí kênh, MUX, ngân sách nhiễu, tốc độ khung
│   ├── OUTLINE_BAOCAO_VISEFD.md       ← Khung báo cáo toàn văn A/B/C theo mẫu ViSEF
│   └── bao_cao/
│       ├── A1_ly_do_chon_de_tai.md    ← Tiêu chí A của ViSEF
│       ├── A2_muc_tieu.md
│       ├── A3_tieu_chi.md
│       ├── A4_doi_tuong_pham_vi.md
│       ├── A5_dia_diem.md
│       ├── A6_phuong_phap.md
│       └── GLOSSARY.md                ← Phân cấp thuật ngữ cảm biến + tuyên bố bị cấm
├── firmware/
│   └── mega_link_diagnostics/     ← ⚠️ DI SẢN đề tài cũ (Mega ↔ Orange Pi bring-up). Xem ghi chú trong file
├── research/
│   ├── README.md                  ← Quy trình làm việc trong research/
│   ├── claims/CLAIM_LEDGER.csv    ← Claim + cấp bằng chứng + trạng thái
│   ├── evidence/SOURCE_LEDGER.csv ← Nguồn thật/candidate + trạng thái xác minh
│   ├── context/
│   │   ├── DECISION_LOG.md        ← Quyết định chính thức (DEC-*)
│   │   ├── PROJECT_SNAPSHOT.md    ← Bản nén ngữ cảnh hiện tại
│   │   ├── CONVERSATION_2026-08-25.md     ← Bản nén hội thoại (đề tài cũ, lịch sử)
│   │   └── CONVERSATION_2026-09-13.md     ← Bản nén hội thoại (pivot sang găng tay)
│   ├── protocols/
│   │   ├── 06_glove_hand_GATE_experiment.md   ← ⭐ GATE experiment CHO ĐỀ TÀI HIỆN TẠI
│   │   ├── ISEF_REVIEW_ORCHESTRATION.md       ← Phản biện 6-lane + adjudication
│   │   ├── 04_orangepi5pro_mega2560_bringup_tests.md ← ⚠️ DI SẢN (Mega), giữ làm tham khảo
│   │   └── 05_velostat_stiffness_GATE_experiment.md  ← ⚠️ SUPERSEDED (DFU) — không dùng
│   ├── prompts/REVIEWER_DISPATCH_TEMPLATE.md ← Template dispatch reviewer
│   ├── queries/QUERY_LOG.jsonl    ← Log truy vấn (auditable)
│   ├── bench/templates/           ← Template log đo bench
│   ├── reviews/00_EXPLORATION_SUMMARY.md ← Tổng kết hành trình săn đề tài
│   ├── reviews/2026-09-19_prior_art_novelty_gate1.md ← ⭐ KẾT QUẢ RÀ SOÁT PRIOR ART lượt 1 (ma trận + quyết định hạ/nâng novelty)
│   ├── reviews/archive/           ← ~20 báo cáo kill-test (đề tài cũ, lưu lịch sử)
│   └── tooling/SETUP_STATUS.md    ← Trạng thái runtime/tooling
├── scripts/
│   ├── bootstrap_research_tooling.sh
│   ├── check_research_environment.py
│   ├── research_log.py
│   ├── tinyfish_search.py
│   ├── build_context_bundle.py
│   └── install_miktex_debian.sh
└── tools/research_sources.lock.json
```

*(`.tools/sources/`, `.claude/skills/`, `.venv/`, `research/{cache,downloads,generated,queries/private}/` là thư mục cục bộ, bị Git ignore.)*

---

## 📁 Nội dung chính từng nhóm

### `docs/` — Tài liệu đề tài
- **01_Topic_Definition** ⭐⭐⭐: tên đề tài, vấn đề, khoảng trống, novelty trung thực, RQ 2 tầng, pipeline, killer experiment, phần cứng.
- **02_Theoretical_Foundation** ⭐⭐⭐: phục hồi vận động sau đột quỵ, thang đo lâm sàng (FMA/ARAT/BBT), cơ sinh học bàn tay & lực ngón, vật lý piezoresistive của Velostat, hysteresis/creep/drift, phép đo vi sai, lượng tử hóa INT8, tuyên bố an toàn. Nhãn 🟢 chuẩn / 🟡 giả thuyết / 🔵 cần kiểm chứng.
- **03_Literature_Gap_Analysis_Plan** ⭐⭐: 10 nhóm chủ đề cần rà soát + ma trận theo dõi.
- **04_Hardware_Architecture** ⭐⭐⭐: bố trí 12–24 kênh, MUX, ngân sách độ phân giải ADC, tốc độ khung hình, đường ống dữ liệu.

### `docs/bao_cao/` — Báo cáo theo mẫu ViSEF
- **A.1–A.6**: lý do chọn đề tài, mục tiêu, tiêu chí, đối tượng & phạm vi, địa điểm, phương pháp.
- **GLOSSARY**: phân cấp vật liệu → sensing element → mảng → hệ thống; danh sách **tuyên bố bị cấm**.

### `research/` — Hạ tầng nghiên cứu có kiểm chứng
- **Ledgers**: mọi tuyên bố, nguồn, quyết định, truy vấn đều có vết. Sau lượt rà soát 1 (2026-09-19): SOURCE_LEDGER 114 dòng (24 nguồn mới), QUERY_LOG +13 bản ghi, CLAIM_LEDGER 15 dòng (CLM-NOV-003 → `CONFLICTED`, thêm CLM-NOV-005 + CLM-MET-002).
- **Protocols**: GATE experiment cho đề tài hiện tại + phản biện ISEF 6-lane.
- **Context**: snapshot + nhật ký quyết định + bản nén hội thoại.

---

## ⚠️ Lịch sử quan trọng (đã xử lý)

- **2026-08-25:** đề tài "đệm khí thích ứng + AAC" bị **xóa toàn bộ** theo DEC-TOPIC-003 (lịch sử còn trong git).
- **2026-08-26:** chốt Hướng C — lót giày Velostat theo dõi độ cứng mô gan chân (sàng lọc DFU).
- **2026-08-28:** **PIVOT** — bỏ DFU vì GATE 3 (Usefulness) yếu; chuyển sang **găng tay theo dõi chức năng bàn tay sau đột quỵ** (DEC-TOPIC-018).
- **2026-09-13:** chốt **tên đề tài chính thức** (DEC-TOPIC-019), chuyển phần cứng từ Arduino Mega 2560 sang **ESP32-S3 + CD74HC4067** (DEC-HW-003), chốt **bố trí kênh** (DEC-HW-004), cập nhật đồng bộ toàn repo + push GitHub.
- **2026-09-19 (11):** `docs/DE_CUONG_NOP_TRUONG.md` = **bản đề cương nộp nhà trường** (13 mục + Phụ lục A): tính mới theo tiêu chí ViSEF/ISEF với bảng đối chiếu 8 công trình/sản phẩm, ảnh hưởng chia 3 loại, cơ sở lý thuyết + nguyên lý hoạt động, 10 ngưỡng đăng ký trước khi đo, ngân sách dự toán theo 4 lớp. `docs/05` thành outline nội bộ. Thêm `SRC-VN-STROKE-EPI-2025`, `SRC-COCHRANE-UE-2014`, `SRC-HENDRICKS-2002-MOTORRECOVER` (UNVERIFIED — ghi lại một chỗ **trích sai nguồn** trong A.1) và `CLM-BIO-003/-004`.
- **2026-09-19 (10):** chủ dự án chốt 2 việc — **`DEC-ROLE-001`: không nêu danh tính KTV trong hồ sơ nộp** (đã sửa `docs/05` §9.6, `protocols/07` §7; `A.5` còn nợ 1 chỗ) và **`DEC-PHASE-001`: vẫn pha lý thuyết** (không firmware, không script). Để GATE 0 vẫn chạy được: **`research/protocols/08a_gate0_bench_sheets.md`** — phiếu đo in được dùng toàn số nguyên + checklist 8 ảnh, và `protocols/08` thêm **G0.0** (chọn định nghĩa nhiễu A/B trước khi đo).
- **2026-09-19 (9):** chủ dự án khai báo **đã có** Velostat + ESP32-S3 + Orange Pi 5 Pro + băng đồng và có **chị là KTV VLTL-PHCN 10 năm** → `DEC-RESOURCE-001` + `SRC-OWNER-2026-09-19-RESOURCES/-KTV10Y` + kiểm kê `research/context/EQUIPMENT_AND_ACCESS.md` + ranh giới sử dụng KTV ở `research/protocols/07` §7. Verdict đầu tư: **giải ngân được Lớp 0–1 về tiền**, nhưng **ngưỡng vẫn phải chốt trước khi đo** và **không đo trên người nhà**.
- **2026-09-19 (8):** đọc **toàn văn** báo cáo dự thi "Xe lăn tự hành ALS" (QG 2024–2025, lĩnh vực **Hệ thống nhúng**, 15 trang) do chủ dự án cung cấp → `research/reviews/2026-09-19_benchmark_xe_lan_ALS_QG2025.md` + `SRC-XELAN-ALS-QG2025-REPORT` (READ_FULL) + `CLM-MET-004` (ngân sách hình thức). Kết luận: phương pháp của ta **trên** chuẩn thắng cuộc; vật thật + con số **dưới** (bằng 0). Khuyến nghị đổi lĩnh vực dự thi sang **Hệ thống nhúng**.
- **2026-09-19 (7):** chủ dự án: thời gian **đủ** → lên kế hoạch cho cả 7 cổng (`DEC-PLAN-001`). Viết **`research/protocols/08_gate0_execution_plan.md`**: GATE 0 tách thành Q1 (độ nhạy `γ`) + Q2 (cửa sổ đọc được `R₀ ≤ R_max`), thêm thí nghiệm quét trở nguồn đo `R_max` + ENOB thật, log trôi ≥10 ngày, 9 ngưỡng **ĐỀ XUẤT — chờ chủ dự án chốt**, cây quyết định khi fail, schema log. **Không viết script** theo chỉ thị.
- **2026-09-19 (6):** trả lời câu "đi xa được tới đâu" → **`research/reviews/2026-09-19_project_ceiling.md`** (trần theo 3 trục: hội thi / xuất bản / sản phẩm, 5 đòn bẩy, 5 rủi ro; 3 mục đã đưa vào `docs/05` §8c). Toàn bộ phán đoán ở đó là **judgment, không phải số đo**.
- **2026-09-19 (5):** làm mục (1)+(4) chủ dự án yêu cầu → `docs/02` §5.5 (mô hình chuỗi đo + cửa sổ preload) và `GAP1 review §6` (sửa 3 lỗi danh tính nguồn, thêm `SRC-TW-SPASTICITY-2022` là đối thủ trực tiếp); tra bằng sáng chế theo phân loại = **bất khả thi** (ghi `docs/03` §7). Soạn **`docs/05_De_Cuong_Dang_Ky_DRAFT.md`** để nộp trường (chờ `DEC-SCOPE-004`).
- **2026-09-19 (4):** chủ dự án chốt phạm vi **E4+E5+E6** (`DEC-SCOPE-003`) nhưng chỉ đạo *giai đoạn này tập trung vào cơ sở lý thuyết*: đã viết `docs/02` §1.4–§1.6/§3.4/§5.4/§7.3/§8.3; **hoãn** chốt ngưỡng GATE A′/RAL và **hoãn** viết script; không trích dự án tham chiếu ISEF 2025 vào hồ sơ nộp.
- **2026-09-19 (3):** xác minh chuẩn tham chiếu hội thi: `SRC-ISEF-2025-ROBO065T` (ISEF 2025, giải Tư, THPT thị xã Quảng Trị, thuần tích hợp YOLO11+Nav2+Gemma2+Telegram, 4 con số tự đo) → hiệu chỉnh khuyến nghị: **E5 nâng lên nên làm**, E3 bỏ vì đạo đức/thời gian chứ không phải vì novelty (`review §11–§13`, `DEC-SCOPE-002c`).
- **2026-09-19 (2):** chủ dự án đề xuất hướng "tập chủ động có trợ lực (AAT)". Phân tích phạm vi + kiểm toán 12 tuyên bố + ma trận va chạm prior art (16 dòng nguồn mới, chưa đọc toàn văn) → `research/reviews/2026-09-19_active_assisted_scope_options.md`; bản nháp lý thuyết đã viết lại an toàn cho báo cáo → `docs/bao_cao/A7_AAT_rationale_DRAFT.md`. **Chờ `DEC-SCOPE-002`** (E1/E2-lite/E3).
- **2026-09-19:** **lượt rà soát prior art 1 (Gap 1)** — 3 nguồn `UNVERIFIED` đã xác minh danh tính; 24 nguồn mới vào ledger; kết quả: **hạ bậc novelty A** (nguyên lý vách→hướng đã có 2015; ART-Glove 2026 làm vỏ cứng + da áp điện trở), **nâng C lên trọng tâm**; thêm mốc y văn (STEF MDC 12,7; Manumeter MDC ~31%) vào GATE B/C **không đổi ngưỡng**. Chờ `DEC-NOV-001`. Chi tiết: `research/reviews/2026-09-19_prior_art_novelty_gate1.md`.

Các file trong `research/reviews/archive/`, `research/protocols/04-05`, `firmware/mega_link_diagnostics/` là **di sản** của các đề tài đã bị loại. **Không dùng làm cơ sở cho đề tài hiện tại.**
