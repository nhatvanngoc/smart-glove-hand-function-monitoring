# Adaptive Cushion AAC

Dự án nghiên cứu hệ thống đệm khí thích ứng dựa trên mô hình áp suất–thời gian, tích hợp giao tiếp hỗ trợ người hạn chế vận động trong phòng ngừa loét tì đè.

> **Trạng thái bằng chứng:** repository hiện chủ yếu chứa thiết kế, mã tham chiếu và kết quả mô phỏng/synthetic. Chưa được diễn giải các kết quả này thành xác nhận phần cứng, hiệu quả lâm sàng hay thiết bị y tế. Baseline kiến trúc cũng đang có các nhánh tài liệu chưa thống nhất; xem `research/context/PROJECT_SNAPSHOT.md`.

## Thiết lập nhanh

Yêu cầu: Git, Python 3.10+, và Bash. Các runtime SOFA/ROS 2 được cài riêng theo `docs/23B_SOFA_WSL_Simplest_Path.md`.

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Clone đúng phiên bản các nguồn nghiên cứu/tooling vào .tools/sources
bash scripts/bootstrap_research_tooling.sh

# Kiểm tra trạng thái; thêm --strict để trả lỗi nếu thiếu dependency/target bắt buộc
python scripts/check_research_environment.py
```

MiKTeX trên Debian 12 có installer riêng:

```bash
bash scripts/install_miktex_debian.sh
```

Nếu mạng/package mirror của môi trường hiện tại chặn APT, dùng installer MiKTeX chính thức trên máy làm việc rồi chạy lại environment check. Clone source MiKTeX trong `.tools/sources/miktex` **không phải** MiKTeX runtime.

## Quy trình nghiên cứu có kiểm chứng

- Tổng quan và lệnh: [`research/README.md`](research/README.md)
- Snapshot ngữ cảnh: [`research/context/PROJECT_SNAPSHOT.md`](research/context/PROJECT_SNAPSHOT.md)
- Claim ledger: [`research/claims/CLAIM_LEDGER.csv`](research/claims/CLAIM_LEDGER.csv)
- Rà soát baseline: [`research/reviews/2026-08-16_baseline_intake.md`](research/reviews/2026-08-16_baseline_intake.md)
- Điều phối phản biện: [`research/protocols/ISEF_REVIEW_ORCHESTRATION.md`](research/protocols/ISEF_REVIEW_ORCHESTRATION.md)

Mọi agent phải tuân thủ [`AGENTS.md`](AGENTS.md), đặc biệt quy tắc phân biệt dữ liệu synthetic với đo đạc thực và yêu cầu IRB/SRC trước thử nghiệm có người tham gia.

## Chạy smoke experiments

```bash
. .venv/bin/activate
for f in experiments/exp0*.py; do PYTHONPATH=. python "$f"; done
```

Các script trên là smoke/reference experiments; kết quả mặc định là synthetic, không phải clinical/hardware validation.
