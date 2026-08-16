# Project snapshot — 2026-08-16

## Purpose and epistemic state

Dự án hướng đến một research prototype đệm khí thích ứng + AAC cho người hạn chế vận động. Repository hiện chứng minh được rằng có tài liệu thiết kế, CAD/reference code, mô phỏng và smoke experiments synthetic. Chưa có artifact đủ để kết luận đã chế tạo toàn hệ thống, hiệu chuẩn Velostat ra mmHg, đạt hiệu quả trên người, đạt clinical-grade, hoặc sẵn sàng sử dụng như medical device.

## Baseline artifacts already read

- `input baseline report/ĐỀ CƯƠNG NGHIÊN CỨU KHOA HỌC KỸ THUẬT final.pdf`: 7 trang. Mô tả kiến trúc 8×8/64 ô, Jetson Orin Nano, stereo camera và robot arm 3 DOF. Phần kết quả/chế tạo, kết luận và tài liệu tham khảo còn trống, nên đây là đề cương chứ không phải báo cáo kết quả hoàn tất.
- `input baseline report/Sổ tay khoa học.docx`: 9 đoạn/entry được đọc sơ bộ. Ghi ý tưởng 8×4; ngày 2026-05-01 bỏ robot arm để giảm chi phí; ngày 2026-05-05 chọn Orange Pi 5 + STM32F4; ngày 2026-05-10 mới mô phỏng cell 1×1 bằng NumPy/Matplotlib/Gazebo.
- `docs/`: 30 tài liệu. Nhóm `docs/00`–`13` chủ yếu giữ kiến trúc 8×8 + Jetson + robot arm; nhóm `docs/15`–`29` chuyển sang 5×9/45 cell, Velostat patch 50×50 mm và SOFA. `docs/19_Final_Matrix_Lock_5x9_50mm.md` ghi “đã chốt” ngày 2026-07-27 nhưng chưa có owner approval được truy vết ngoài chính tài liệu đó.

## Architecture conflicts that block silent editing

| Topic | Baseline/report and older docs | Notebook/later docs | State |
|---|---|---|---|
| Cell matrix | 8×8, 64 independent cells | notebook 8×4; later lock 5×9, 45 cells | owner decision required |
| Edge computer | Jetson Orin Nano | Orange Pi 5 | owner decision required |
| Camera positioning | robot arm 3 DOF included | robot arm removed 2026-05-01 | owner decision required |
| Simulation | Gazebo/ROS2 | later docs choose SOFA; notebook only notes early NumPy/Matplotlib/Gazebo cell | reconcile history vs target |
| Prototype state | report has empty “fabricated successfully” section | repo review admits no hardware validation | do not claim fabricated |

Do not create a hybrid architecture by assumption. The next architecture edit needs an explicit answer covering matrix, compute board, robot arm, and primary simulator.

## Evidence risks already identified

1. All seven experiment scripts are synthetic/reference experiments. `docs/11_Academic_Review.md` itself says no hardware validation, while also displaying green PASS values and an “Accept with minor revisions” verdict. The synthetic values cannot support hardware/clinical claims, and the verdict is an internal review artifact, not external acceptance.
2. `docs/10_References.md` says all sources passed Tier-0 verification, but its own table labels one source Tier-1/needs DOI and no complete provenance ledger is present. Initial exact-title searches did not retrieve the stated Saadeh 2018, Khan 2021, or Mahmood 2023 records. They remain quarantined as `UNVERIFIED`; search misses are not proof of nonexistence.
3. Velostat/Linqstat behavior is nonlinear and affected by hysteresis, creep/drift, geometry, substrate and environmental conditions. Any mmHg output is a calibration result, not a material constant.
4. `32 mmHg` is a historical/reference value with strong limitations; do not use it as an absolute harm, diagnostic, pass/fail, or universal safety threshold.
5. The proposed protocol includes other human participants and up to four-hour exposure. Current ISEF rules require properly constituted IRB review/pre-approval before recruitment or interaction; a mentor-only approval is insufficient.

## Tooling state

- Pinned shallow/partial checkouts exist under `.tools/sources/` for Academic Research Skills, PlotNeuralNet, Caffe, PGF and MiKTeX; versions are in `tools/research_sources.lock.json`.
- Academic Research Skills is linked locally under `.claude/skills/`; all four links and all five pinned, clean source trees pass bootstrap/environment checks. Third-party prompts remain untrusted inputs.
- Caffe, PGF, and MiKTeX source trees are intentionally not built. Caffe is legacy/reference-only unless a concrete experiment requires it. Normal TikZ rendering should use the PGF package from the TeX distribution.
- An ignored `.venv` has NumPy, Matplotlib and scikit-learn. All seven synthetic experiment scripts execute, but four expose failed/non-estimable criteria and the remaining PASS values still are not empirical evidence; details are in `research/tooling/SMOKE_TESTS.md`.
- PlotNeuralNet Python → TeX generation passed. MiKTeX runtime/`pdflatex` installation is still blocked in this sandbox by outbound APT/TLS failures, so PDF rendering remains untested. The official Debian installer script is prepared at `scripts/install_miktex_debian.sh`.
- Environment readiness is 10/11 required/target checks, with only `pdflatex` failing; `miktexsetup` is an optional warning.
- Search provenance is persisted in `research/queries/QUERY_LOG.jsonl`; TinyFish now logs complete/failed/blocked attempts automatically without storing its API key. Claim/source ledgers and a hard-budget context bundle provide continuation state.

## Immediate next decisions/actions

1. Owner locks the actual 2026 baseline: matrix, SBC, robot arm, simulator and minimal ISEF demo scope.
2. Quarantine or re-verify every reference used by a consequential claim, beginning with the three exact-title misses and the epidemiology/cost figures.
3. Replace synthetic “PASS” framing with a results table split into simulation, bench, hardware, human and clinical evidence levels.
4. Define mannequin/bench MVP and acceptance criteria that do not rely on `32 mmHg` as a universal cutoff.
5. Before any human testing, obtain applicable affiliated-fair guidance, IRB/SRC pre-approval, risk determination, and consent/assent documentation.
