# 📑 INDEX — Sơ đồ file của dự án

> **Dự án:** Smart Insole Edge-AI — Drift-Robust 3D-GRF & COP Monitoring (theo dõi dọc dáng đi, knee OA)
> **Học sinh:** Văn Ngọc Nhật Anh — THPT Quảng Trị
> **Cập nhật:** 2026-08-25 (tinh chỉnh đề tài + xóa toàn bộ file đề tài cũ)

---

## 🗂️ Cấu trúc hiện tại

```
.
├── README.md                      ← Giới thiệu + setup + novelty
├── AGENTS.md                      ← Quy tắc vận hành cho mọi AI/agent
├── INDEX.md                       ← File này
├── LICENSE
├── requirements.txt               ← numpy, matplotlib, scikit-learn
├── docs/
│   ├── 01_Topic_Definition.md     ← Đề tài, RQ, novelty, pipeline, killer experiment
│   ├── 02_Theoretical_Foundation.md ← CƠ SỞ LÍ THUYẾT (cơ sinh học, cảm biến, drift, GNN, metrics)
│   └── 03_Literature_Gap_Analysis_Plan.md ← Kế hoạch rà soát gap 2025–2026
├── research/
│   ├── README.md                  ← Quy trình làm việc trong research/
│   ├── claims/CLAIM_LEDGER.csv    ← Claim + cấp bằng chứng + trạng thái
│   ├── evidence/SOURCE_LEDGER.csv ← Nguồn thật/candidate + trạng thái xác minh
│   ├── context/
│   │   ├── DECISION_LOG.md        ← Quyết định chính thức (DEC-*)
│   │   ├── PROJECT_SNAPSHOT.md    ← Bản nén ngữ cảnh hiện tại
│   │   └── CONVERSATION_2026-08-25.md ← Bản nén hội thoại (phần 1 + 2)
│   ├── protocols/
│   │   ├── ISEF_REVIEW_ORCHESTRATION.md      ← Phản biện 6-lane + adjudication
│   │   └── SMART_INSOLE_CRITIQUE_5_SEATS.md  ← Phản biện 5 ghế cho đề tài này
│   ├── prompts/REVIEWER_DISPATCH_TEMPLATE.md ← Template dispatch reviewer
│   ├── queries/QUERY_LOG.jsonl   ← Log truy vấn (auditable)
│   ├── reviews/2026-08-25_smart_insole_redteam.md ← Red-team phản biện đầu tiên
│   └── tooling/SETUP_STATUS.md   ← Trạng thái runtime/tooling
├── scripts/
│   ├── bootstrap_research_tooling.sh      ← Clone 5 nguồn tooling (ghim commit)
│   ├── check_research_environment.py      ← Kiểm tra readiness
│   ├── research_log.py                    ← Ghi truy vấn vào JSONL
│   ├── tinyfish_search.py                 ← Search + tự log
│   ├── build_context_bundle.py            ← Nén ngữ cảnh thành packet giới hạn
│   └── install_miktex_debian.sh           ← Installer MiKTeX (Debian 12)
└── tools/research_sources.lock.json      ← Ghim commit 5 nguồn tooling
```

*(`.tools/sources/`, `.claude/skills/`, `.venv/`, `research/{cache,downloads,generated,queries/private}/` là thư mục cục bộ, bị Git ignore.)*

---

## 📁 Nội dung chính từng nhóm

### `docs/` — Tài liệu đề tài (3 file)
- **01_Topic_Definition** ⭐⭐⭐: tên đề tài, mục tiêu 3 tầng + tuyên bố cấm, insight novelty, RQ 2 tầng, DNA, pipeline, killer experiment, ứng viên novelty A–E, phần cứng tái sử dụng, lộ trình theo tầng, bước tiếp theo.
- **02_Theoretical_Foundation** ⭐⭐⭐: cơ sinh học dáng đi (GRF/COP/KAM), Velostat & drift (dP/dt), mô hình drift & change detection, GNN/ST-GNN, chuẩn vàng + metrics, edge/INT8, tuyên bố an toàn. Mọi mục được gắn nhãn 🟢 chuẩn / 🟡 giả thuyết / 🔵 cần kiểm chứng.
- **03_Literature_Gap_Analysis_Plan** ⭐⭐: quy trình rà soát 10 nhóm chủ đề + ma trận theo dõi (điền dần).

### `research/` — Hạ tầng nghiên cứu có kiểm chứng
- **Ledgers** (claim/source/decision/query): mọi tuyên bố, nguồn, quyết định, truy vấn đều có vết.
- **Protocols**: phản biện ISEF 6-lane + 5 ghế chuyên đề.
- **Context**: snapshot + nhật ký + bản nén hội thoại — để mỗi phiên khôi phục trạng thái bằng artifact, không dựa vào trí nhớ.

---

## ⚠️ Lịch sử quan trọng (đã xử lý)

- **2026-08-25:** đề tài cũ "đệm khí thích ứng + AAC" bị **xóa toàn bộ** (docs 00–30, cad, diagrams, simulation, pipeline, experiments, outputs, src, input baseline report) theo DEC-TOPIC-003 — lịch sử còn trong git. Đề tài hiện tại là Smart Insole (tinh chỉnh lần 2).
