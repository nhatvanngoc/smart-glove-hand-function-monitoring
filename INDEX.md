# INDEX — Sơ đồ file của dự án

> **Hướng đề tài hiện hành:** găng hỗ trợ tập phục hồi vận động tinh sau đột quỵ; chức năng tiến triển từ gập–duỗi có trợ giúp, tự động chuyển AAN theo ngưỡng, tới phối hợp ba ngón gắp–nhấc–di chuyển–đặt thìa. Tên làm việc chưa phải tên cuối.
> **Cập nhật:** 2026-10-19 · Thẩm quyền: [`research/context/CURRENT_DESIGN_BASELINE.md`](research/context/CURRENT_DESIGN_BASELINE.md), `DEC-REHAB-001` và `DECISION_LOG.md`.
> **Cảm biến/hệ thống:** 3 Flex sensor (mỗi ngón cái–trỏ–giữa một chiếc) theo dõi gập–duỗi; Velostat ghi áp lực/tiếp xúc tương đối; camera theo dõi thìa/vùng đích/kết quả. Nếu cả 3 Flex cùng đi qua MUX 16 kênh thì còn tối đa 13 kênh cho Velostat/ô tham chiếu; map cuối mở. Orange Pi 5 Pro dự kiến xử lý thị giác; chưa benchmark; RL không thuộc phạm vi. Không yêu cầu KTV chuyển mode. Servo cuốn dây trực tiếp trên tang; an toàn, hồi/duỗi và điều khiển độc lập còn mở.
> **Bằng chứng:** bench/phantom trước; không thử bệnh nhân/claim hiệu quả lâm sàng/home use đã xác nhận. Các chỉ số kỹ thuật là mục tiêu tới khi có log; không tuyên bố novelty/“đầu tiên”. Hồ sơ đã nộp giữ nguyên.
> **Drive:** nguồn `11A2.docx` và PDF người dùng cung cấp vẫn nguyên trạng. DOCX review riêng dựa trên draft cũ, hiện không đại diện cho hướng mới.

---

##  Cấu trúc hiện tại

```
.
├── README.md                      ← Tóm tắt định hướng và ranh giới hiện hành
├── INDEX.md                       ← File này
├── LICENSE
├── requirements.txt               ← numpy, matplotlib, scikit-learn
├── 3d_model/                          ← [Trọng tâm] Thiết kế cơ cấu cơ khí nẹp ngón tay (CAD & 3D Print)
│   ├── custom_exo/full_finger_modular/ ← Bộ 3 đốt module hóa Print-in-Place + Khớp rãnh trượt 13.5mm (STL/STEP/FCStd)
│   ├── custom_exo/fixation_mechanisms_benchmark/ ← 9 phương án cơ cấu đóng/mở nẹp 1 đốt (Mech 1-9), đã in thử thực tế; Mech 9 (hiện tại) CHƯA có file CAD — xem README trong thư mục
│   ├── generate_full_finger_modular.py ← Script FreeCAD Python sinh tham số toàn bộ ngón tay
│   └── render_full_finger.py          ← Script kết xuất đồ họa trực quan 4 góc nhìn
├── de_cuong/
│   ├── DE_CUONG_NGHIEN_CUU.pdf / .docx (= _BAN_MOI, MD5 trùng) ← bản 2026-10-03, lịch sử; phần AAN/lực/phantom-only superseded bởi baseline 2026-10-19
│   ├── DE_CUONG_NGHIEN_CUU_COBROWSE.docx ← bản rút gọn/khác (40 KB, chưa đọc chi tiết)
│   └── build_docx.py / make_figures.py / make_plots.py / write_section1.py / figures/ / tikz/ ← script dựng bản PDF/docx ở trên
├── docs/
│   ├── DE_CUONG.pdf / DE_CUONG.txt    ← [Trọng tâm] BẢN ĐÃ NỘP TRƯỜNG (15 tr., 2026-09-26) + trích text tra cứu
│   ├── DE_CUONG_NOP_TRUONG.md         ← Đề cương nộp trường (bản md; danh tính đã điền từ PDF)
│   ├── 01_Topic_Definition.md         ← Định nghĩa đề tài hiện hành theo baseline 2026-10-19
│   ├── 02_Theoretical_Foundation.md   ← Lý thuyết tham khảo; định nghĩa project-specific cũ đã superseded
│   ├── 03_Literature_Gap_Analysis_Plan.md ← Hồ sơ prior-art nội bộ; không dùng để tuyên bố novelty trong đề cương
│   ├── 04_Hardware_Architecture.md    ← Kiến trúc cảm biến; mô tả actuator AAN cũ đã superseded
│   ├── 05_De_Cuong_Dang_Ky_DRAFT.md   ← Outline cũ — superseded, giữ để truy vết
│   ├── 06_Co_Cau_Co_Khi_Exoskeleton.md ← Khung/nẹp CAD; không xác nhận actuator AAN
│   ├── DE_CUONG_A_B_C_DRAFT_2026-10-19.md ← Bản A/B/C đang cập nhật theo lộ trình rehab + AAN tự động + bài tập thìa; chưa duyệt/nộp
│   ├── 11A2_CAP_NHAT_DU_THAO_2026-10-19.docx ← Bản Word review cũ; chưa đồng bộ hướng mới, không phải bản nộp
│   ├── OUTLINE_BAOCAO_VISEFD.md       ← Outline cũ — superseded
│   └── bao_cao/
│       ├── A1_ly_do_chon_de_tai.md    ← Tiêu chí A của ViSEF
│       ├── A2_muc_tieu.md
│       ├── A3_tieu_chi.md
│       ├── A4_doi_tuong_pham_vi.md
│       ├── A5_dia_diem.md
│       ├── A6_phuong_phap.md
│       └── GLOSSARY.md                ← Phân cấp thuật ngữ cảm biến + tuyên bố bị cấm
├── firmware/
│   └── mega_link_diagnostics/     ← Lưu ý: DI SẢN đề tài cũ (Mega ↔ Orange Pi bring-up). Xem ghi chú trong file
├── research/
│   ├── README.md                  ← Quy trình làm việc trong research/
│   ├── claims/CLAIM_LEDGER.csv    ← Claim + cấp bằng chứng + trạng thái
│   ├── evidence/SOURCE_LEDGER.csv ← Nguồn thật/candidate + trạng thái xác minh
│   ├── context/
│   │   ├── CURRENT_DESIGN_BASELINE.md ← Hướng chức năng hiện hành, AAN tự động, cảm biến/camera và ranh giới bằng chứng
│   │   ├── IMPLEMENTATION_PIPELINE.md   ← Pipeline triển khai/kiểm chứng đề xuất, thresholds vẫn mở
│   │   ├── DECISION_LOG.md        ← Quyết định chính thức (DEC-*), gồm lịch sử và supersession
│   │   ├── PROJECT_SNAPSHOT.md    ← Bản nén ngữ cảnh với cập nhật hiện hành đầu trang
│   │   ├── CONVERSATION_2026-08-25.md     ← Bản nén hội thoại (đề tài cũ, lịch sử)
│   │   └── CONVERSATION_2026-09-13.md     ← Bản nén hội thoại (pivot sang găng tay)
│   ├── protocols/
│   │   ├── 06_glove_hand_GATE_experiment.md   ← GATE đo; AAN cũ superseded, các GATE cần rà soát
│   │   ├── 09_AAN_spool_phantom_and_conditional_volunteer.md ← AAN hiện hành; khung thử có điều kiện
│   │   ├── ISEF_REVIEW_ORCHESTRATION.md       ← Phản biện 6-lane + adjudication
│   │   ├── 04_orangepi5pro_mega2560_bringup_tests.md ← Lưu ý: DI SẢN (Mega), giữ làm tham khảo
│   │   └── 05_velostat_stiffness_GATE_experiment.md  ← Lưu ý: SUPERSEDED (DFU) — không dùng
│   ├── prompts/REVIEWER_DISPATCH_TEMPLATE.md ← Template dispatch reviewer
│   ├── queries/QUERY_LOG.jsonl    ← Log truy vấn (auditable)
│   ├── bench/templates/           ← Template log đo bench
│   ├── reviews/00_EXPLORATION_SUMMARY.md ← Tổng kết hành trình săn đề tài
│   ├── reviews/2026-09-27_decuong_pdf_sync.md ← [Trọng tâm] ĐỐI CHIẾU BẢN NỘP với repo (F1–F14, G0↔C1, sổ I/L/R, 6 QĐ chờ chốt)
│   ├── reviews/2026-09-19_prior_art_novelty_gate1.md ← [Trọng tâm] KẾT QUẢ RÀ SOÁT PRIOR ART lượt 1 (ma trận + quyết định hạ/nâng novelty)
│   ├── reviews/archive/           ← ~20 báo cáo kill-test (đề tài cũ, lưu lịch sử)
│   ├── notebooklm_sync/           ← Lưu ý: Đồng bộ từ Google NotebookLM. `experiments/01-05` = log bring-up phần cứng thật (`DEC-PHASE-002`, chưa chính thức hoá GATE 0); `chat_transcripts/`, `studio/` = bản ghi chú nháp ban đầu, chỉ dùng để tham khảo nội bộ — không trích trực tiếp vào hồ sơ nộp
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

*(`.tools/sources/`, `.venv/`, `research/{cache,downloads,generated,queries/private}/` là thư mục cục bộ, bị Git ignore.)*

---

## Nội dung chính từng nhóm

### `docs/` — Tài liệu đề tài
- **01_Topic_Definition** [Trọng tâm cao]: tên đề tài, vấn đề, khoảng trống, novelty trung thực, RQ 2 tầng, pipeline, killer experiment, phần cứng.
- **02_Theoretical_Foundation** [Trọng tâm cao]: phục hồi vận động sau đột quỵ, thang đo lâm sàng (FMA/ARAT/BBT), cơ sinh học bàn tay & lực ngón, vật lý piezoresistive của Velostat, hysteresis/creep/drift, phép đo vi sai, lượng tử hóa INT8, tuyên bố an toàn. Nhãn [Khả thi] chuẩn / [Chờ xử lý] giả thuyết / [Thông tin] cần kiểm chứng.
- **03_Literature_Gap_Analysis_Plan** [Trọng tâm vừa]: 10 nhóm chủ đề cần rà soát + ma trận theo dõi.
- **04_Hardware_Architecture** [Trọng tâm cao]: bố trí 12–24 kênh, MUX, ngân sách độ phân giải ADC, tốc độ khung hình, đường ống dữ liệu.

### `docs/bao_cao/` — Báo cáo theo mẫu ViSEF
- **A.1–A.6**: lý do chọn đề tài, mục tiêu, tiêu chí, đối tượng & phạm vi, địa điểm, phương pháp.
- **GLOSSARY**: phân cấp vật liệu → sensing element → mảng → hệ thống; danh sách **tuyên bố bị cấm**.

### `research/` — Hạ tầng nghiên cứu có kiểm chứng
- **Ledgers**: mọi tuyên bố, nguồn, quyết định, truy vấn đều có vết. Sau lượt rà soát 1 (2026-09-19): SOURCE_LEDGER 114 dòng (24 nguồn mới), QUERY_LOG +13 bản ghi, CLAIM_LEDGER 15 dòng (CLM-NOV-003 → `CONFLICTED`, thêm CLM-NOV-005 + CLM-MET-002).
- **Protocols**: GATE experiment cho đề tài hiện tại + phản biện ISEF 6-lane.
- **Context**: snapshot + nhật ký quyết định + bản nén hội thoại.

---

## Lưu ý: Lịch sử quan trọng (đã xử lý)

- **HISTORICAL — 2026-10-11 (phần phạm vi đã superseded 2026-10-19):** đồng bộ bản đề cương `de_cuong/DE_CUONG_NGHIEN_CUU.pdf` và ghi nhận AAN là trụ cột kỹ thuật (`DEC-SCOPE-006`), khi đó còn giới hạn phantom-only. Phạm vi thử hiện hành được thay bằng `DEC-SCOPE-007`/`DEC-AAN-002`: AAN là mục tiêu chính, servo cuốn dây trực tiếp, phantom trước và tình nguyện viên chỉ sau đánh giá an toàn/phê duyệt. Các ghi nhận khác về bring-up (`DEC-PHASE-002`) và hồ sơ/tên vẫn cần đọc trong decision log theo ngày. Cập nhật README (§1, §6.1 mới, §8, §10, §11, lịch sử), quy định an toàn (§2 ranh giới AAN + cảnh báo cấp bằng chứng của notebooklm_sync), DECISION_LOG (+5), CLAIM_LEDGER (+3), SOURCE_LEDGER (+6).
- **2026-08-25:** đề tài "đệm khí thích ứng + AAC" bị **xóa toàn bộ** theo DEC-TOPIC-003 (lịch sử còn trong git).
- **2026-08-26:** chốt Hướng C — lót giày Velostat theo dõi độ cứng mô gan chân (sàng lọc DFU).
- **2026-08-28:** **PIVOT** — bỏ DFU vì GATE 3 (Usefulness) yếu; chuyển sang **găng tay theo dõi chức năng bàn tay sau đột quỵ** (DEC-TOPIC-018).
- **2026-09-13:** chốt **tên đề tài chính thức** (DEC-TOPIC-019), chuyển phần cứng từ Arduino Mega 2560 sang **ESP32-S3 + CD74HC4067** (DEC-HW-003), chốt **bố trí kênh** (DEC-HW-004), cập nhật đồng bộ toàn repo + push GitHub.
- **2026-09-27:** đồng bộ **bản đã nộp `docs/DE_CUONG.pdf`** (15 tr., tạo 2026-09-26) → `research/reviews/2026-09-27_decuong_pdf_sync.md`: đội hình 2 người + GVHD Lê Công Long, lĩnh vực Nhúng, timeline 09/2026–01/2027; tên quay về `DEC-TOPIC-019` (README cũ ghi `DEC-TITLE-001` "chốt" là quá thẩm quyền — chưa từng vào log); `GAP = PROM − AROM`; ngưỡng C1.x; kiến trúc ADS1115+INA333; môi trường cài lại (10/11 check). 6 quyết định + 7 nguồn + 3 claim chờ nhóm thống nhất.
- **2026-09-19 (11):** `docs/DE_CUONG_NOP_TRUONG.md` = **bản đề cương nộp nhà trường** (13 mục + Phụ lục A): tính mới theo tiêu chí ViSEF/ISEF với bảng đối chiếu 8 công trình/sản phẩm, ảnh hưởng chia 3 loại, cơ sở lý thuyết + nguyên lý hoạt động, 10 ngưỡng đăng ký trước khi đo, ngân sách dự toán theo 4 lớp. `docs/05` thành outline nội bộ. Thêm `SRC-VN-STROKE-EPI-2025`, `SRC-COCHRANE-UE-2014`, `SRC-HENDRICKS-2002-MOTORRECOVER` (UNVERIFIED — ghi lại một chỗ **trích sai nguồn** trong A.1) và `CLM-BIO-003/-004`. *(2026-09-27: đã điền 4 ô danh tính từ bản PDF đã nộp.)*
- **2026-09-19 (10):** nhóm nghiên cứu chốt 2 việc — **`DEC-ROLE-001`: không nêu danh tính KTV trong hồ sơ nộp** (đã sửa `docs/05` §9.6, `protocols/07` §7; `A.5` còn nợ 1 chỗ) và **`DEC-PHASE-001`: vẫn pha lý thuyết** (không firmware, không script). Để GATE 0 vẫn chạy được: **`research/protocols/08a_gate0_bench_sheets.md`** — phiếu đo in được dùng toàn số nguyên + checklist 8 ảnh, và `protocols/08` thêm **G0.0** (chọn định nghĩa nhiễu A/B trước khi đo).
- **2026-09-19 (9):** nhóm nghiên cứu khai báo **đã có** Velostat + ESP32-S3 + Orange Pi 5 Pro + băng đồng và có **chị là KTV VLTL-PHCN 10 năm** → `DEC-RESOURCE-001` + `SRC-OWNER-2026-09-19-RESOURCES/-KTV10Y` + kiểm kê `research/context/EQUIPMENT_AND_ACCESS.md` + ranh giới sử dụng KTV ở `research/protocols/07` §7. Verdict đầu tư: **giải ngân được Lớp 0–1 về tiền**, nhưng **ngưỡng vẫn phải chốt trước khi đo** và **không đo trên người nhà**.
- **2026-09-19 (8):** đọc **toàn văn** báo cáo dự thi "Xe lăn tự hành ALS" (QG 2024–2025, lĩnh vực **Hệ thống nhúng**, 15 trang) do nhóm nghiên cứu cung cấp → `research/reviews/2026-09-19_benchmark_xe_lan_ALS_QG2025.md` + `SRC-XELAN-ALS-QG2025-REPORT` (READ_FULL) + `CLM-MET-004` (ngân sách hình thức). Kết luận: phương pháp của ta **trên** chuẩn thắng cuộc; vật thật + con số **dưới** (bằng 0). Khuyến nghị đổi lĩnh vực dự thi sang **Hệ thống nhúng**.
- **2026-09-19 (7):** nhóm nghiên cứu: thời gian **đủ** → lên kế hoạch cho cả 7 cổng (`DEC-PLAN-001`). Viết **`research/protocols/08_gate0_execution_plan.md`**: GATE 0 tách thành Q1 (độ nhạy `γ`) + Q2 (cửa sổ đọc được `R₀ ≤ R_max`), thêm thí nghiệm quét trở nguồn đo `R_max` + ENOB thật, log trôi ≥10 ngày, 9 ngưỡng **ĐỀ XUẤT — chờ nhóm nghiên cứu chốt**, cây quyết định khi fail, schema log. **Không viết script** theo chỉ thị.
- **2026-09-19 (6):** trả lời câu "đi xa được tới đâu" → **`research/reviews/2026-09-19_project_ceiling.md`** (trần theo 3 trục: hội thi / xuất bản / sản phẩm, 5 đòn bẩy, 5 rủi ro; 3 mục đã đưa vào `docs/05` §8c). Toàn bộ phán đoán ở đó là **judgment, không phải số đo**.
- **2026-09-19 (5):** làm mục (1)+(4) nhóm nghiên cứu yêu cầu → `docs/02` §5.5 (mô hình chuỗi đo + cửa sổ preload) và `GAP1 review §6` (sửa 3 lỗi danh tính nguồn, thêm `SRC-TW-SPASTICITY-2022` là đối thủ trực tiếp); tra bằng sáng chế theo phân loại = **bất khả thi** (ghi `docs/03` §7). Soạn **`docs/05_De_Cuong_Dang_Ky_DRAFT.md`** để nộp trường (chờ `DEC-SCOPE-004`).
- **2026-09-19 (4):** nhóm nghiên cứu chốt phạm vi **E4+E5+E6** (`DEC-SCOPE-003`) nhưng chỉ đạo *giai đoạn này tập trung vào cơ sở lý thuyết*: đã viết `docs/02` §1.4–§1.6/§3.4/§5.4/§7.3/§8.3; **hoãn** chốt ngưỡng GATE A′/RAL và **hoãn** viết script; không trích dự án tham chiếu ISEF 2025 vào hồ sơ nộp.
- **2026-09-19 (3):** xác minh chuẩn tham chiếu hội thi: `SRC-ISEF-2025-ROBO065T` (ISEF 2025, giải Tư, THPT thị xã Quảng Trị, thuần tích hợp YOLO11+Nav2+Gemma2+Telegram, 4 con số tự đo) → hiệu chỉnh khuyến nghị: **E5 nâng lên nên làm**, E3 bỏ vì đạo đức/thời gian chứ không phải vì novelty (`review §11–§13`, `DEC-SCOPE-002c`).
- **2026-09-19 (2):** nhóm nghiên cứu đề xuất hướng "tập chủ động có trợ lực (AAT)". Phân tích phạm vi + kiểm toán 12 tuyên bố + ma trận va chạm prior art (16 dòng nguồn mới, chưa đọc toàn văn) → `research/reviews/2026-09-19_active_assisted_scope_options.md`; bản nháp lý thuyết đã viết lại an toàn cho báo cáo → `docs/bao_cao/A7_AAT_rationale_DRAFT.md`. **Chờ `DEC-SCOPE-002`** (E1/E2-lite/E3).
- **2026-09-19:** **lượt rà soát prior art 1 (Gap 1)** — 3 nguồn `UNVERIFIED` đã xác minh danh tính; 24 nguồn mới vào ledger; kết quả: **hạ bậc novelty A** (nguyên lý vách→hướng đã có 2015; ART-Glove 2026 làm vỏ cứng + da áp điện trở), **nâng C lên trọng tâm**; thêm mốc y văn (STEF MDC 12,7; Manumeter MDC ~31%) vào GATE B/C **không đổi ngưỡng**. Chờ `DEC-NOV-001`. Chi tiết: `research/reviews/2026-09-19_prior_art_novelty_gate1.md`.

Các file trong `research/reviews/archive/`, `research/protocols/04-05`, `firmware/mega_link_diagnostics/` là **di sản** của các đề tài đã bị loại. **Không dùng làm cơ sở cho đề tài hiện tại.**
