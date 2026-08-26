# Project snapshot — 2026-08-26 (chốt Hướng C cho ViSEF)

## Đề tài hiện tại (Direction C)

**Lót giày cảm biến áp lực Velostat giá rẻ, tự kiểm tra độ tin cậy + theo dõi độ cứng mô khu trú ở gan chân, sàng lọc sớm nguy cơ loét bàn chân đái tháo đường (DFU) tại nhà.**

- **Vấn đề:** DFU → đoạn chi; mô đệm gan chân **xơ cứng trước khi loét**; độ cứng mô là **biomarker nguy cơ đã được y văn xác nhận**.
- **Khoảng trống:** công cụ đo độ cứng hiện tại (elastography/MyotonPRO/TCM/durometer) **đắt, cồng kềnh, 1 điểm, chỉ ở phòng khám**.
- **Ý tưởng:** mảng **Velostat** rẻ, **nén lặp (áp lực động)** → suy **độ cứng khu trú**; **self-validation** (ô tham chiếu phát hiện drift) + **longitudinal** tại nhà.
- **Điểm mới thật (vật lý):** dynamic-pressure stiffness proxy. Self-validation & longitudinal **KHÔNG mới** (execution).
- **Mức novelty:** phù hợp **ViSEF** (Creativity+Execution+Presentation), không phải "phát minh thế giới".

## Trạng thái bằng chứng (epistemic state)

- **Chưa có kết quả thực nghiệm nào.** Repo ở mức **định hướng + prior-art**.
- **Gate 1 (prior-art):** Hướng C **không bị kill**; đã loại ~8 hướng khác (xem `research/reviews/00_EXPLORATION_SUMMARY.md`).
- **Gate 2 (khả thi vật lý):** **CHƯA ĐO** — chờ Velostat để chạy GATE (`research/protocols/05_velostat_stiffness_GATE_experiment.md`).

## Tuyên bố bị cấm

- ❌ Chẩn đoán/điều trị/tiên lượng loét; ❌ thay thế bác sĩ/elastography.
- ❌ "Velostat đo chính xác độ cứng tuyệt đối"; chỉ **sàng lọc/theo dõi nguy cơ** và **phải qua GATE**.
- ❌ Claim self-validation/longitudinal là "mới".
- ❌ Thử trên bệnh nhân khi chưa có IRB/SRC (giai đoạn đầu chỉ bench/phantom).

## Blocker & rủi ro

1. **BLOCKER:** chưa có **Velostat** để chạy GATE.
2. **MAJOR (rủi ro vật lý):** drift/hysteresis của Velostat có thể **lấn át** tín hiệu độ cứng mô → GATE PASS-C quyết định.
3. **MAJOR:** phải vượt **durometer rẻ** (đã rẻ + validated) → lợi thế thật là **mảng + tại nhà + longitudinal**.
4. **MAJOR:** confound — tách đáp ứng **mô** khỏi đáp ứng **cảm biến** (dùng ô tham chiếu/nền cứng).
5. **CONDITIONAL BLOCKER:** IRB/SRC trước mọi thử nghiệm có người.

## Quyết định chính (DECISION_LOG)

- **DEC-TOPIC-017 (2026-08-26):** chốt Hướng C; mục tiêu **chinh phục ViSEF trước**; novelty = góc vật lý (dynamic-pressure stiffness proxy).
- Các hướng cũ (3D-GRF/COP knee OA; measurement-integrity gait; assistive control; transfer learning…) đã **loại** qua kill-test.

## Phần cứng & tooling

- **Phần cứng:** Velostat (cảm biến) + Arduino Mega (ADC) + Orange Pi 5 Pro (Edge-AI). Transport GPIO UART Mega↔OPi đã chạy (owner-reported). Bring-up: `research/protocols/04_...bringup_tests.md`.
- **Tooling:** `.tools/sources/` (ghim commit), skill links, `scripts/` (search/log/build_context_bundle/check_env). Readiness 10/11 (thiếu pdflatex).
- **Ledger:** nguồn đã verify ở `research/evidence/SOURCE_LEDGER.csv`; claim ở `research/claims/CLAIM_LEDGER.csv`; query ở `research/queries/QUERY_LOG.jsonl`.

## Việc tiếp theo

1. **Khi có Velostat:** chạy **GATE experiment** (`research/protocols/05_...`). Gửi số liệu để phân tích PASS/FAIL (đặc biệt PASS-C: tín hiệu độ cứng > drift).
2. Nếu GATE PASS → viết proposal đầy đủ + kế hoạch bench Stage 2 (healthy volunteers, mô phỏng bệnh bằng phantom).
3. Nếu GATE FAIL → báo thẳng, đổi trục (bỏ Velostat hoặc bỏ ràng buộc human-pressure).
4. Giữ nguyên tắc: không kết luận y khoa; IRB/SRC trước khi thử trên người.
