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

## Literature-gap checkpoint (initial scan, 2026-08-25)

- Đã rà soát sơ bộ các nhóm **#2 3D-GRF, #4 drift/hysteresis, #5 cross-session, #7 longitudinal**; query provenance ở `research/queries/QUERY_LOG.jsonl`, nguồn đã đọc có scope ở `research/evidence/SOURCE_LEDGER.csv`, và phản biện G5 ở `research/reviews/2026-08-25_gap_groups_2_4_5_7_and_devil_advocate.md`.
- Kết quả bảo thủ: generic low-cost smart-insole + ML 3D-GRF đã có close prior art (Zhang et al., 2025); generic correction/đặc trưng cảm biến cũng đã có. Longitudinal wearable monitoring tồn tại ở mức khái quát. **E (biology-vs-sensor separation) và cross-session pressure-insole 3D-GRF vẫn UNRESOLVED, không phải gap đã xác nhận.**
- Devil's Advocate (sequential role review, không độc lập đa-agent) kết luận **BLOCK**: force plate/reference đa trục, thiết kế nhận diện biology-vs-sensor, ablation cross-session, và baseline/hardware lock phải có trước bất kỳ claim mạnh nào.
- Chỉ thị chiến lược mới của chủ dự án: săn **golden novelty** bằng reverse-engineering literature (failure mechanism → hidden variable → mechanism → killer experiment), không brainstorm implementation novelty. Seed cards và protocol ở `research/reviews/2026-08-25_golden_novelty_hunt.md`.
- Đã dựng checkpoint đầu tiên của **Gap Matrix 20 paper**: `research/reviews/2026-08-25_golden_novelty_gap_matrix.csv` (18 nguồn đã đọc theo scope ledger; 2 candidate vẫn cần bibliographic/full-text verification). Close prior art Olugbon et al. là **preprint arXiv 2025**, không phải paper 2021; nó dùng IMU + center-of-pressed-sensor cho vGRF nhưng chưa xác minh tách biology-vs-sensor qua nhiều session.
- Interim decision (`research/reviews/2026-08-25_golden_novelty_interim_decision.md`): candidate tốt nhất hiện nay là **intervention-calibrated measurement-integrity monitoring** — phát hiện/flag measurement-system state để giảm false longitudinal gait-change alerts. Điểm triage bảo thủ 8.0/10, nhưng **UNRESOLVED**, không được claim novelty cho đến khi hoàn tất near-neighbor screening và killer experiment với force-plate/reference.

## Engineering continuity and owner-provided background

- **Transport baseline:** owner reports direct GPIO UART/serial communication between Orange Pi 5 Pro and Arduino Mega is already working. The next action is to characterize integrity, timing, GPIO/UART electrical-interface documentation, ADC scan behavior and raw-log provenance — not re-establish basic communication. `research/protocols/04_orangepi5pro_mega2560_bringup_tests.md` reflects this.
- **Owner-reported diagnostic run (not independently reprocessed):** Mega at ADC prescaler 64 reported 11,511 sent frames, 0 errors and a 16-channel/100-Hz target. Orange Pi reported 11,510 received frames, 0 CRC failures, 0 sequence gaps, one expected disconnect/reconnect, CPU 47.153 C, and a 54.13-Hz whole-runtime average. The owner explains that firmware deliberately alternated 60-s send and 60-s no-send states; 11,510 frames over 212.6 s is consistent with approximately 54.1 Hz whole-runtime throughput. This is a fault/reconnect test, not a continuous 100-Hz transport validation or sensor/ADC-quality result. Next transport test: a 10-min uninterrupted CONNECTED run must report `connected_interval_rate`, frame-interval p50/p95, CRC failures, gaps and the one-frame sent/received boundary difference.
- **Owner-provided experience:** Văn Ngọc Nhật Anh reports participation in **2** prior Vietnamese science-and-engineering competitions (KHKT) and **5** engineering competitions. This is background for planning/communication, not evidence of this prototype’s validation or competition readiness.

## Hypothesis-lock checkpoint

- Owner has locked the next-phase RQ: **Can controlled measurement perturbations estimate measurement integrity in a low-cost plantar sensing system and reduce false longitudinal gait-change alerts without substantially increasing missed true changes?** This does not confirm novelty; status remains **CANDIDATE — NOT YET CONFIRMED**.
- The three pre-model artifacts are now present: `research/reviews/01_prior_art_matrix.md` (30-paper kill matrix, with 20 read-scope entries and 10 candidates), `research/protocols/02_perturbation_protocol.md`, and `research/protocols/03_falsification_plan.md`.
- Bench/reference-load work is the first permitted experimental phase. Any work involving other human participants remains paused pending applicable ISEF/affiliated-fair IRB/SRC pre-approval.

## Immediate next actions

1. ~~Complete the **prior-art kill test** for C21–C30~~ — **DONE 2026-08-26**: all C21–C29 identity-verified and read; C30 mapped; adversarial searches run. No kill paper found; no GAP CONFIRMED (bounded screen). Novelty framing narrowed per `CLM-NOV-003`. **C31–C40 conceptual near-neighbour attack also DONE 2026-08-26** (sensor quality, fault diagnosis, measurement validity, context/distribution shift, longitudinal alerting): no paper kills `CLM-NOV-003`; it survives. Extra constraints recorded: **MDC/SDC is the mandatory static baseline to beat**, and injected *measurement* perturbation must be distinguished from *biological* gait change (cf. `SRC-ACM-2025-GAITCHANGE`). Gate 1 stays **OPEN**.
2. Lock **force plate/load cell** access, axes, timing/synchronization and reference-load rig before kinetic/COP claims.
3. Execute only the Phase-A **bench metrology** protocol first; evaluate perturbation viability before model development.
4. Continue remaining literature groups (#1, #3, #6, #8, #9, #10) only insofar as they can kill/refine the locked hypothesis; a residual targeted adversarial re-search is still owed before any novelty claim is upgraded to SUPPORTED.
3. Đặc trưng Velostat (drift/hysteresis/creep theo nhiệt/tải/thời gian) trên bench.
4. Baseline tuyến tính/CNN/LSTM trước ST-GNN; leave-one-subject/session-out.
5. Benchmark NPU INT8 (latency/throughput/công suất).
6. Giữ nguyên tắc: không kết luận y khoa; IRB/SRC trước mọi thử nghiệm có người.
