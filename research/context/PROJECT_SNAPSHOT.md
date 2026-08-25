# Project snapshot — 2026-08-25 (tinh chỉnh đề tài lần 2)

## Purpose and epistemic state

Đề tài đã được **tinh chỉnh** (chỉ thị phần 2): từ "Smart Insole ước lượng 3D-GRF/COP" thành đề tài có trọng tâm novelty rõ ràng hơn — **longitudinal drift-robust kinetic monitoring**:

- Mục tiêu khoa học: continuous **drift-robust** 3D kinetic estimation from wearable plantar sensing.
- Mục tiêu ứng dụng: longitudinal detection of abnormal gait changes.
- Mục tiêu y sinh: hỗ trợ theo dõi thay đổi chức năng vận động & đáp ứng phục hồi ở người nguy cơ/mắc knee OA.
- **Bị cấm:** chẩn đoán/điều trị OA, thay thế bác sĩ/X-ray/MRI/force plate, "GRF ⇒ OA".

Repository hiện ở giai đoạn **định hướng + chuẩn bị hạ tầng**: chưa có đo đạc, chưa có chuẩn vàng, chưa có bộ dữ liệu, **chưa có kết quả gap analysis**. Toàn bộ file đề tài cũ (đệm khí/AAC) đã bị **xóa** theo DEC-TOPIC-003 (lịch sử còn trong git).

## Quyết định chính (xem DECISION_LOG)

- **DEC-TOPIC-001/002/003:** đổi hướng + tinh chỉnh + xóa file cũ.
- **DEC-INSOLE-004:** novelty = E (biology-vs-sensor) + D (longitudinal change detection); GRF regression không đủ.
- **DEC-INSOLE-006:** force plate = chuẩn vàng bắt buộc (blocker nếu thiếu).
- **DEC-INSOLE-008:** không vội build hardware — gap analysis trước.

## Insight cốt lõi (từ chỉ thị)

- Không bắt đầu từ "người yếu thế cần gì" mà từ: **bottleneck khó → biến ẩn khó đo → phương pháp mới → benchmark định lượng → impact**.
- Literature 2025–2026 đã có 3D-GRF estimation bằng smart insole + ML/IMU/GCN → **"Velostat + GNN → 3D-GRF" không đủ mới**.
- Tách nguồn biến thiên: `Δ = Δ_biology + Δ_sensor + Δ_environment`; cô lập Δ_biology là contribution chính.
- Killer experiment: drift correction → cross-session error ≈ hằng số + false change detection ↓.

## Blocker & rủi ro (red-team)

1. **BLOCKER:** chưa có force plate/load cell đa trục (chuẩn vàng 3D-GRF).
2. **MAJOR:** novelty chưa được xác minh bằng gap analysis (E/D/A/B/C).
3. **MAJOR:** dP/dt chỉ giảm offset drift (không triệt tiêu); gain drift/hysteresis/creep vẫn còn.
4. **MAJOR:** ST-GNN phải thắng baseline (tuyến tính/CNN/LSTM) trên cùng split; chống leakage theo người/phiên.
5. **MAJOR:** hiệu năng phần cứng chưa đo (16 chân ADC vs số ô; 6 TOPS là spec).
6. **BLOCKER (có điều kiện):** IRB/SRC trước mọi thử nghiệm có người; nghiên cứu theo tầng để giảm rủi ro.

## Tooling state

- 5 nguồn đã clone + ghim commit trong `.tools/sources/` (academic-research-skills `6837b4d`, PlotNeuralNet `e96bc85`, Caffe `9b89154`, PGF `0a859c8`, MiKTeX `76d1b3d`).
- Skill links `.claude/skills/` đã tạo; bootstrap `--check` PASS.
- Python deps (numpy/matplotlib/scikit-learn) cài trong `.venv`; readiness 10/11 — chỉ thiếu `pdflatex` (cài MiKTeX installer trên máy thật).
- Search/log: `scripts/tinyfish_search.py`, `research/queries/QUERY_LOG.jsonl`; context packet: `scripts/build_context_bundle.py`.

## Immediate next actions

1. Chạy **literature gap analysis 2025–2026** (10 nhóm) — `docs/03`.
2. Chốt **force plate/load cell** làm chuẩn vàng (mượn/thuê).
3. Đặc trưng Velostat (drift/hysteresis/creep theo nhiệt/tải/thời gian) trên bench.
4. Baseline tuyến tính/CNN/LSTM trước ST-GNN; leave-one-subject/session-out.
5. Benchmark NPU INT8 (latency/throughput/công suất).
6. Giữ nguyên tắc: không kết luận y khoa; IRB/SRC trước mọi thử nghiệm có người.
