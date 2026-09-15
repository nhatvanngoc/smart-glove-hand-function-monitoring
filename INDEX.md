# 📑 INDEX — Sơ đồ file của dự án

> **Đề tài:** Nghiên cứu và phát triển **găng tay thông minh hỗ trợ đánh giá và theo dõi chức năng vận động bàn tay trong phục hồi chức năng sau đột quỵ**
> **Học sinh:** Văn Ngọc Nhật Anh — THPT Quảng Trị
> **Cập nhật:** 2026-09-13 (chốt đề tài găng tay; phần cứng ESP32-S3 + CD74HC4067)
> **Trạng thái:** định hướng + thiết kế + prior art. **Chưa có kết quả thực nghiệm.**

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
- **Ledgers**: mọi tuyên bố, nguồn, quyết định, truy vấn đều có vết.
- **Protocols**: GATE experiment cho đề tài hiện tại + phản biện ISEF 6-lane.
- **Context**: snapshot + nhật ký quyết định + bản nén hội thoại.

---

## ⚠️ Lịch sử quan trọng (đã xử lý)

- **2026-08-25:** đề tài "đệm khí thích ứng + AAC" bị **xóa toàn bộ** theo DEC-TOPIC-003 (lịch sử còn trong git).
- **2026-08-26:** chốt Hướng C — lót giày Velostat theo dõi độ cứng mô gan chân (sàng lọc DFU).
- **2026-08-28:** **PIVOT** — bỏ DFU vì GATE 3 (Usefulness) yếu; chuyển sang **găng tay theo dõi chức năng bàn tay sau đột quỵ** (DEC-TOPIC-018).
- **2026-09-13:** chốt **tên đề tài chính thức** (DEC-TOPIC-019), chuyển phần cứng từ Arduino Mega 2560 sang **ESP32-S3 + CD74HC4067** (DEC-HW-003), chốt **bố trí kênh** (DEC-HW-004), cập nhật đồng bộ toàn repo + push GitHub.

Các file trong `research/reviews/archive/`, `research/protocols/04-05`, `firmware/mega_link_diagnostics/` là **di sản** của các đề tài đã bị loại. **Không dùng làm cơ sở cho đề tài hiện tại.**
