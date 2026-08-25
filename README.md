# Smart Insole Edge-AI — Drift-Robust 3D-GRF & COP Monitoring

Hệ thống **lót giày thông minh (Smart Insole)** dùng **Edge-AI** ước lượng **liên tục** lực phản lực mặt đất 3 chiều (**3D-GRF: Fx, Fy, Fz**) và quỹ đạo tâm áp lực (**COP**) từ ma trận cảm biến áp lực giá rẻ **Velostat**, với khả năng **chống trôi dạt (drift-robust)** — để phát hiện sớm thay đổi động học dáng đi và theo dõi đáp ứng phục hồi ở người có nguy cơ/mắc **thoái hóa khớp gối (knee OA)**.

> **Trạng thái bằng chứng:** giai đoạn **định hướng + chuẩn bị hạ tầng**. Chưa có đo đạc phần cứng, chưa có chuẩn vàng, chưa có kết quả rà soát tài liệu. Mọi ý tưởng (dP/dt, ST-GNN, novelty) là **giả thuyết cần kiểm chứng**. Không tuyên bố chẩn đoán/điều trị. Xem `research/context/PROJECT_SNAPSHOT.md`.

## Trọng tâm novelty

> ❌ "Velostat + GNN để dự đoán 3D-GRF" **chưa đủ mới** (literature 2025–2026 đã có).

Trọng tâm thật sự là **longitudinal, drift-robust kinetic monitoring**: tách thay đổi sinh học thật khỏi drift cảm biến —

```
Δ(đo lường dọc) = Δ_biology + Δ_sensor + Δ_environment
```

Chi tiết: [`docs/01_Topic_Definition.md`](docs/01_Topic_Definition.md).

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
