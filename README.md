# Smart Insole Edge-AI — Velostat tự kiểm tra & theo dõi độ cứng mô gan chân (sàng lọc DFU)

**Lót giày cảm biến áp lực Velostat giá rẻ**, dùng **Edge-AI**, **tự kiểm tra độ tin cậy của cảm biến** và **theo dõi độ cứng mô khu trú** ở gan chân — hỗ trợ **sàng lọc sớm nguy cơ loét bàn chân đái tháo đường (DFU) tại nhà**.

> **Trạng thái bằng chứng:** giai đoạn **định hướng + prior-art**. **Chưa có kết quả thực nghiệm.** Đề tài **sống hay chết do GATE experiment** (chờ Velostat). Không tuyên bố chẩn đoán/điều trị; chỉ "sàng lọc/theo dõi nguy cơ". Xem `research/context/PROJECT_SNAPSHOT.md`.

## Vấn đề & ý tưởng

- Người đái tháo đường hay bị **loét bàn chân → đoạn chi**; **mô đệm gan chân xơ cứng trước khi loét**. **Độ cứng mô là biomarker nguy cơ DFU đã được y văn xác nhận.**
- Công cụ đo độ cứng hiện tại (elastography/MyotonPRO/TCM) **đắt, cồng kềnh, 1 điểm, chỉ ở phòng khám**.
- **Ý tưởng:** mảng **Velostat** rẻ, **nén lặp (áp lực động)** → suy **độ cứng khu trú**; **self-validation** (ô tham chiếu phát hiện drift → báo lỗi thay vì báo sai) + **theo dõi dọc tại nhà**.

## Trọng tâm novelty (trung thực)

> Điểm mới chính = **góc vật lý**: dùng **đáp ứng áp lực động** của Velostat để suy **độ cứng mô** (dynamic-pressure stiffness proxy). **Self-validation & longitudinal KHÔNG mới** (đã có prior art) — là execution. Đây là mức novelty **phù hợp ViSEF** (không phải "phát minh thế giới").

Hành trình săn đề tài + lý do các hướng khác bị loại: [`research/reviews/00_EXPLORATION_SUMMARY.md`](research/reviews/00_EXPLORATION_SUMMARY.md). Chi tiết đề tài: [`docs/01_Topic_Definition.md`](docs/01_Topic_Definition.md). GATE experiment: [`research/protocols/05_velostat_stiffness_GATE_experiment.md`](research/protocols/05_velostat_stiffness_GATE_experiment.md).

## Tài liệu

| Tài liệu | Nội dung |
|---|---|
| [`docs/01_Topic_Definition.md`](docs/01_Topic_Definition.md) | Đề tài, RQ 2 tầng, novelty, pipeline, killer experiment, lộ trình theo tầng |
| [`docs/02_Theoretical_Foundation.md`](docs/02_Theoretical_Foundation.md) | **Cơ sở lí thuyết**: cơ sinh học, Velostat, drift, dP/dt, GNN, metrics, edge |
| [`docs/03_Literature_Gap_Analysis_Plan.md`](docs/03_Literature_Gap_Analysis_Plan.md) | Kế hoạch rà soát khoảng trống 2025–2026 (10 nhóm chủ đề) |
| [`research/protocols/SMART_INSOLE_CRITIQUE_5_SEATS.md`](research/protocols/SMART_INSOLE_CRITIQUE_5_SEATS.md) | Phản biện 5 ghế + 5 câu hỏi chí mạng |
| [`research/protocols/ISEF_REVIEW_ORCHESTRATION.md`](research/protocols/ISEF_REVIEW_ORCHESTRATION.md) | Điều phối phản biện 6-lane + adjudication |
| [`research/context/DECISION_LOG.md`](research/context/DECISION_LOG.md) | Nhật ký quyết định chính thức |
| [`research/context/PROJECT_SNAPSHOT.md`](research/context/PROJECT_SNAPSHOT.md) | Snapshot ngữ cảnh hiện tại |
| [`research/context/CONVERSATION_2026-08-25.md`](research/context/CONVERSATION_2026-08-25.md) | Bản nén hội thoại (đổi hướng + tinh chỉnh) |

## Thiết lập nhanh

Yêu cầu: Git, Python 3.10+, Bash.

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Clone đúng phiên bản các nguồn nghiên cứu/tooling vào .tools/sources (đã ghim commit)
bash scripts/bootstrap_research_tooling.sh

# Kiểm tra trạng thái; thêm --strict để trả lỗi nếu thiếu dependency/target bắt buộc
python scripts/check_research_environment.py
```

MiKTeX (render sơ đồ PlotNeuralNet/TikZ) cần **installer chính thức** trên máy làm việc (https://miktex.org/download); trên Debian 12 có thể thử `bash scripts/install_miktex_debian.sh`. Clone source MiKTeX trong `.tools/sources/miktex` **không phải** MiKTeX runtime.

## Quy trình nghiên cứu có kiểm chứng

Mọi agent tuân thủ [`AGENTS.md`](AGENTS.md). Quy trình mỗi phiên: đọc snapshot → log truy vấn (`scripts/research_log.py`, `scripts/tinyfish_search.py`) → cập nhật claim/source ledger → chạy review protocol khi có thay đổi lớn → cập nhật snapshot → `python scripts/build_context_bundle.py`.

**Bước tiếp theo bắt buộc (trước khi build hardware):** literature gap analysis 2025–2026 theo `docs/03`.

## Lưu ý đổi tên repo

Đã **chuẩn bị đổi tên** `nhatvanngoc/adaptive_cushion_aac` → `nhatvanngoc/smart-insole-edge-ai`, nhưng token GitHub của phiên agent **không có quyền Administration** (HTTP 403) nên chưa thực hiện được. Chủ dự án tự đổi:

```bash
gh repo rename smart-insole-edge-ai --repo nhatvanngoc/adaptive_cushion_aac --yes
```

hoặc GitHub web → **Settings → Repository name**. Sau đó (nếu cần):

```bash
git remote set-url origin https://github.com/nhatvanngoc/smart-insole-edge-ai.git
```

Branch làm việc của phiên giữ nguyên `arena/01a0372f-adaptive-cushion-aac` (ràng buộc nền tảng).
