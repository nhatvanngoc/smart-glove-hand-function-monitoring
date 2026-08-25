# Project snapshot — 2026-08-25 (đổi hướng đề tài)

## Purpose and epistemic state

Đề tài đã **chuyển hướng** (2026-08-25) từ "đệm khí thích ứng + AAC" sang **Smart Insole Edge-AI: ước lượng 3D-GRF (Fx, Fy, Fz) và quỹ đạo COP** từ ma trận Velostat giá rẻ, suy luận trên Orange Pi 5 Pro. Repository hiện ở giai đoạn **định hướng + chuẩn bị hạ tầng**: chưa có đo đạc phần cứng, chưa có chuẩn vàng, chưa có bộ dữ liệu. Mọi ý tưởng dP/dt, ST-GNN và "khoảng trống nghiên cứu" là **giả thuyết cần kiểm chứng**.

## Quyết định chính (đã ghi DECISION_LOG)

- **DEC-TOPIC-001:** bỏ "đệm khí + AAC", chuyển sang Smart Insole (owner, 2026-08-25). Đóng/supersede các quyết định kiến trúc cũ (matrix 5×9, Jetson vs Orange Pi, robot arm, SOFA/Gazebo).
- **DEC-INSOLE-001:** phần cứng cơ sở = Arduino Mega (16 kênh ADC) + Orange Pi 5 Pro (NPU ~6 TOPS, suy luận biên). 6 TOPS là spec nhà sản xuất, chưa đo.
- **DEC-INSOLE-002:** chiến lược dP/dt (giảm drift) + ST-GNN (đồ thị giải phẫu bàn chân → Fx/Fy từ Fz) là **giả thuyết nghiên cứu**, chưa được chấp nhận làm kết quả.
- **DEC-INSOLE-003:** hoãn mọi module AAC/eye-tracking/khí nén; giữ tài liệu cũ làm archive.

## Baseline artifacts already read (đề tài cũ — lịch sử)

- `input baseline report/ĐỀ CƯƠNG NGHIÊN CỨU KHOA HỌC KỸ THUẬT final.pdf` và `Sổ tay khoa học.docx`: thuộc đề tài "đệm khí"; mô tả 8×8/64 ô, Jetson Orin Nano, robot arm. Không còn là baseline của đề tài mới.
- `docs/01`–`29`, `cad/`, `simulation/`: kiến trúc đệm khí/Velostat patch 50 mm/SOFA — giữ làm archive; không hợp nhất vào kiến trúc mới.

## Khoảng trống nghiên cứu & novelty (GIẢ THUYẾT)

1. Chưa có giải pháp **giá rẻ** xử lý triệt để **drift qua nhiều phiên** cho Velostat → cần systematic review có lưu vết trước khi ghi claim.
2. Suy **Fx/Fy từ cảm biến chỉ đo áp lực pháp tuyến** là bài toán ngược nhiễu cao → cần xác định prior art.
3. Triển khai mô hình không–thời gian lượng tử hoá trên **NPU giá rẻ** với độ trễ thấp → cần benchmark thực tế.

Lĩnh vực smart insole rất đông (thương mại: Nurvv, Sensoria, Moticon, Digitsole, Plantiga…; hàn lâm: GRF-from-insoles). Tính mới phải **thu hẹp rõ ràng** và được chứng minh, không suy từ "chưa tìm thấy".

## Blocker & rủi ro đã xác định (từ red-team 2026-08-25)

- **F1 (BLOCKER):** chưa có chuẩn vàng (force plate/load cell đa trục) cho Fx, Fy, Fz, COP.
- **F2 (MAJOR):** "dP/dt triệt tiêu drift" là phát biểu quá mạnh — chỉ được nói "giảm" với biên định lượng.
- **F3 (MAJOR):** novelty chưa được chứng minh.
- **F4 (MAJOR):** ST-GNN chưa có baseline so sánh.
- **F5/F6 (MAJOR):** hiệu năng phần cứng chưa đo; ma trận >16 ô cần multiplexing → đánh đổi tần số lấy mẫu.
- **F7 (BLOCKER có điều kiện):** không kết luận y khoa; IRB/SRC trước khi thử người.

Chi tiết: `research/reviews/2026-08-25_smart_insole_redteam.md`.

## Tooling state (2026-08-25)

- 5 nguồn đã clone + ghim commit vào `.tools/sources/` (gitignored): academic-research-skills `6837b4d`, PlotNeuralNet `e96bc85`, Caffe `9b89154`, PGF `0a859c8`, MiKTeX `76d1b3d`. Bootstrap `--check` PASS toàn bộ.
- Skill links `.claude/skills/` (deep-research, academic-paper, academic-paper-reviewer, academic-pipeline) đã tạo.
- Caffe/PGF/MiKTeX là **source reference**, không build. MiKTeX runtime cần installer chính thức trên máy thật (`scripts/install_miktex_debian.sh`); `pdflatex` chưa có trong sandbox.
- Python deps (numpy/matplotlib/scikit-learn) chưa cài trong checkout này — tạo `.venv` theo README.
- Search provenance: `scripts/tinyfish_search.py` + `research/queries/QUERY_LOG.jsonl`; context packet: `scripts/build_context_bundle.py`.

## Immediate next decisions/actions (chờ chủ dự án)

1. Chốt **chuẩn vàng** Fx/Fy/Fz/COP (force plate/load cell) — blocker số 1.
2. Chốt số ô cảm biến + layout điện cực + chiến lược ADC/multiplexing.
3. Chạy systematic review novelty có lưu vết (drift cross-session, GRF-from-insoles).
4. Chạy baseline tuyến tính/CNN/LSTM trước ST-GNN, báo uncertainty, chống leakage theo người tham gia.
5. Benchmark latency/throughput/năng lượng sau lượng tử hoá INT8 trên Orange Pi 5 Pro.
6. Giữ nguyên tắc: không kết luận y khoa; IRB/SRC trước mọi thử nghiệm có người.
