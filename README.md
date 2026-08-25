# Smart Insole Edge-AI — Ước lượng 3D-GRF & quỹ đạo COP

Nghiên cứu hệ thống **lót giày thông minh (Smart Insole)** dùng **Edge-AI** để ước lượng **lực phản lực mặt đất 3 chiều (3D-GRF: Fx, Fy, Fz)** và **quỹ đạo tâm áp lực (COP)** từ ma trận cảm biến áp lực giá rẻ **Velostat**, chạy suy luận trực tiếp trên **Orange Pi 5 Pro**.

> **Trạng thái bằng chứng:** đây là giai đoạn **định hướng + chuẩn bị hạ tầng**. Repository chưa có kết quả phần cứng/lâm sàng. Các ý tưởng về dP/dt, ST-GNN và "khoảng trống nghiên cứu" đang ở mức **giả thuyết** — phải được kiểm chứng trước khi ghi thành claim `SUPPORTED`. Xem `research/context/PROJECT_SNAPSHOT.md`.

## Chuyển hướng chiến lược (2026-08-25)

Dự án đã **từ bỏ** ý tưởng "đệm khí thích ứng (adaptive air cushion) + AAC" do rủi ro cơ khí, cảm biến và kiểm chứng lâm sàng quá cao, chuyển sang đề tài Smart Insole. Chi tiết: [`docs/30_TOPIC_PIVOT_Smart_Insole.md`](docs/30_TOPIC_PIVOT_Smart_Insole.md). Toàn bộ tài liệu/hình vẽ CAD của đề tài cũ được giữ làm **kho lưu trữ lịch sử**, không hợp nhất vào kiến trúc mới.

## Thiết lập nhanh

Yêu cầu: Git, Python 3.10+, và Bash.

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

MiKTeX (để render sơ đồ PlotNeuralNet/TikZ) không phải Git repo — cài **installer chính thức** trên máy làm việc (https://miktex.org/download). Trên Debian 12 có thể thử:

```bash
bash scripts/install_miktex_debian.sh
```

Clone source MiKTeX trong `.tools/sources/miktex` **không phải** MiKTeX runtime.

## Quy trình nghiên cứu có kiểm chứng

- Tổng quan và lệnh: [`research/README.md`](research/README.md)
- Snapshot ngữ cảnh: [`research/context/PROJECT_SNAPSHOT.md`](research/context/PROJECT_SNAPSHOT.md)
- Nhật ký quyết định: [`research/context/DECISION_LOG.md`](research/context/DECISION_LOG.md)
- Claim ledger: [`research/claims/CLAIM_LEDGER.csv`](research/claims/CLAIM_LEDGER.csv)
- Chuyển hướng đề tài: [`docs/30_TOPIC_PIVOT_Smart_Insole.md`](docs/30_TOPIC_PIVOT_Smart_Insole.md)
- Phản biện 5 ghế (Cơ sinh học, Nhúng, AI, Đạo đức, Devil's Advocate): [`research/protocols/SMART_INSOLE_CRITIQUE_5_SEATS.md`](research/protocols/SMART_INSOLE_CRITIQUE_5_SEATS.md)
- Điều phối phản biện ISEF (6-lane + adjudication): [`research/protocols/ISEF_REVIEW_ORCHESTRATION.md`](research/protocols/ISEF_REVIEW_ORCHESTRATION.md)
- Red-team đề tài mới: [`research/reviews/2026-08-25_smart_insole_redteam.md`](research/reviews/2026-08-25_smart_insole_redteam.md)
- Bản nén hội thoại đổi hướng: [`research/context/CONVERSATION_2026-08-25.md`](research/context/CONVERSATION_2026-08-25.md)

Mọi agent phải tuân thủ [`AGENTS.md`](AGENTS.md): phân biệt dữ liệu synthetic với đo đạc thực, không tự nâng cấp độ bằng chứng, và yêu cầu IRB/SRC trước thử nghiệm có người tham gia.

## Chạy smoke experiments

```bash
. .venv/bin/activate
for f in experiments/exp0*.py; do PYTHONPATH=. python "$f"; done
```

Các script trên là smoke/reference experiments; kết quả mặc định là **synthetic**, không phải clinical/hardware validation.

## Lưu ý về đổi tên repo

Đã **chuẩn bị đổi tên** repo `nhatvanngoc/adaptive_cushion_aac` → `nhatvanngoc/smart-insole-edge-ai` (2026-08-25), nhưng token GitHub của phiên agent **không có quyền Administration** nên chưa thực hiện được. Chủ dự án tự đổi tên bằng một trong hai cách:

```bash
# Cách 1: dùng gh với tài khoản có quyền admin trên repo
gh repo rename smart-insole-edge-ai --repo nhatvanngoc/adaptive_cushion_aac --yes
```

Cách 2: GitHub web → repo → **Settings** → mục **Repository name** → đổi thành `smart-insole-edge-ai` → Rename.

Sau khi đổi tên, cập nhật remote cục bộ (nếu cần):

```bash
git remote set-url origin https://github.com/nhatvanngoc/smart-insole-edge-ai.git
```

Branch làm việc của phiên giữ nguyên tên `arena/01a0372f-adaptive-cushion-aac` do ràng buộc nền tảng.
