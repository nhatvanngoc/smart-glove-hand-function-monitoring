# Conversation archive — 2026-08-25 (đổi hướng đề tài)

> **Mục đích:** bản nén (lossy) hội thoại ra quyết định đổi hướng đề tài, lưu trữ bền vững trên GitHub để khôi phục ngữ cảnh mà không phụ thuộc trí nhớ hội thoại.
> **Phương pháp nén:** tóm tắt có cấu trúc + phụ lục chứa **nguyên văn** chỉ thị của chủ dự án (làm provenance). Bản tóm tắt là **hỗ trợ điều hướng**, không phải bằng chứng; nguồn chuẩn là `DECISION_LOG.md`, `PROJECT_SNAPSHOT.md` và các artifact gốc được trỏ tới.
> **Trạng thái:** chủ dự án cho biết sẽ gửi **thêm thông tin** sau — các mục "mở" dưới đây chờ cập nhật tiếp theo.

---

## 1. Tóm tắt nén (compressed)

### 1.1 Yêu cầu của chủ dự án (8 mục)

1. Vai trò AI: context lớn, điều phối sub-agent, **phản biện**.
2. Chuẩn bị & clone repo: academic-research-skills, PlotNeuralNet, Caffe, PGF/TikZ, MiKTeX.
3. Công cụ **tìm kiếm** + **sub-agent phản biện**.
4. **Nén token** cho ngữ cảnh lớn, **lưu truy vấn vào file**.
5. Kỹ năng nghiên cứu khoa học & phản biện **ngang tầm ISEF**, **giảm thiểu ảo giác**.
6. **Đổi hướng đề tài** (từ "đệm khí thích ứng" sang Smart Insole) — cập nhật lên GitHub.
7. **Nén hội thoại này** và lưu vào GitHub.
8. **Đổi tên repo GitHub**.

### 1.2 Đổi hướng đề tài (tóm tắt quyết định)

- **Bỏ** "đệm khí thích ứng + AAC" (rủi ro cơ khí, cảm biến, kiểm chứng lâm sàng quá cao).
- **Chuyển sang** "Smart Insole dùng Edge-AI ước lượng **3D-GRF** và quỹ đạo **COP**".
- **Trọng tâm đột phá:** khắc phục điểm yếu của Velostat giá rẻ (trôi dạt, trễ) bằng **dP/dt** (đạo hàm áp lực theo thời gian) + mô hình **ST-GNN** (bàn chân = đồ thị giải phẫu), suy Fx/Fy từ Fz.
- **Phần cứng:** Arduino Mega (16 kênh ADC, tần số cao) + Orange Pi 5 Pro (NPU ~6 TOPS, suy luận tại biên).
- **Khoảng trống:** giả thuyết "chưa có giải pháp giá rẻ xử lý triệt để drift qua nhiều phiên cho Velostat" — **cần kiểm chứng** bằng rà soát có lưu vết.
- **Phản biện:** 5 ghế (Cơ sinh học, Nhúng, AI, Đạo đức, Devil's Advocate) + chiến lược trả lời 5 câu hỏi "chí mạng".

### 1.3 Việc đã thực hiện trong phiên này

- Clone + ghim 5 nguồn vào `.tools/sources/` (không commit, đúng lock file): academic-research-skills `6837b4d`, PlotNeuralNet `e96bc85`, Caffe `9b89154`, PGF `0a859c8`, MiKTeX `76d1b3d`.
- Tạo skill links `.claude/skills/` (deep-research, academic-paper, academic-paper-reviewer, academic-pipeline).
- Environment check: 7/11 — `pdflatex`/`miktexsetup` chưa cài (cần installer MiKTeX trên máy thật), numpy/matplotlib/scikit-learn chưa cài (cần `.venv`).
- Ghi quyết định đổi hướng vào `DECISION_LOG.md` (DEC-TOPIC-001; đóng các quyết định kiến trúc cũ).
- Tạo `docs/30_TOPIC_PIVOT_Smart_Insole.md`, `research/protocols/SMART_INSOLE_CRITIQUE_5_SEATS.md`, `research/reviews/2026-08-25_smart_insole_redteam.md`.
- Cập nhật `README.md`, `AGENTS.md`, `PROJECT_SNAPSHOT.md`, `INDEX.md`, `research/README.md`, `build_context_bundle.py`.
- **Đổi tên repo GitHub** → đã **thử** với tên `smart-insole-edge-ai` nhưng bị GitHub từ chối (HTTP 403: token agent không có quyền Administration). Chờ chủ dự án tự đổi tên; xem mục 1.4.

### 1.4 Đổi tên GitHub (CHỜ CHỦ DỰ ÁN THỰC HIỆN)

- Tên cũ: `nhatvanngoc/adaptive_cushion_aac`.
- Tên đề xuất mới: `nhatvanngoc/smart-insole-edge-ai`.
- **Trạng thái:** đổi tên bị **chặn** — token GitHub của agent không có quyền Administration (HTTP 403 "Resource not accessible by integration"). Repo hiện vẫn là `adaptive_cushion_aac`.
- **Cách thực hiện (chủ dự án):** `gh repo rename smart-insole-edge-ai --repo nhatvanngoc/adaptive_cushion_aac --yes`, hoặc GitHub web → Settings → Repository name.
- Branch làm việc của phiên giữ nguyên: `arena/01a0372f-adaptive-cushion-aac` (ràng buộc nền tảng; không đổi tên branch).

### 1.5 Mở — chờ thông tin tiếp theo từ chủ dự án

- Số ô cảm biến/layout điện cực Velostat trong đế giày (và cách vượt giới hạn 16 kênh ADC).
- Chuẩn vàng (force plate/load cell) cho Fx, Fy, Fz, COP — blocker số 1.
- Phạm vi novelty chốt cuối (sau systematic review).
- Quyết định ST-GNN vs baseline sau khi có dữ liệu.
- Tên repo cuối cùng (nếu muốn đổi khác) và bất kỳ thông tin bổ sung nào.

---

## 2. Phụ lục — nguyên văn chỉ thị của chủ dự án (provenance)

<details>
<summary>Raw owner message (2026-08-25)</summary>

```
Để chuẩn bị cho 1 large project, tôi cần bạn là 1 ai có context windows lớn, có khả năng điều phối sub agent làm việc, và phản biện. Sau đó clone cho tôi 1 số repo để chuẩn bị và triển khai, setup.

1. https://github.com/Imbad0202/academic-research-skills.git
2. https://github.com/HarisIqbal88/PlotNeuralNet.git
3. https://github.com/BVLC/caffe.git
4. https://github.com/pgf-tikz/pgf.git
5. MiKTeX
6. Tool search, sub agent phản biện
7. Nén token để chứa lượng ngữ cảnh lớn, lưu truy vấn vào file.
8. Kĩ năng nghiên cứu khoa học, phản biện ngang tầm cuộc thi ISEF. Giảm tính ảo giác nhất có thể.

Có sự thay đổi về đề tài, bạn cập nhật ở github. Cụ thể như sau:

Quá trình nghiên cứu đã chuyển hướng từ một dự án "Đệm khí thích ứng" quá tham vọng và rủi ro cao sang một đề tài có chiều sâu khoa học và tính khả thi cao hơn: "Hệ thống lót giày thông minh (Smart Insole) sử dụng Edge-AI để ước lượng lực phản lực mặt đất 3 chiều (3D-GRF) và quỹ đạo tâm áp lực (COP)". Trọng tâm đột phá của đề tài là giải quyết điểm yếu cố hữu của cảm biến giá rẻ Velostat (trôi dạt, trễ) bằng các thuật toán toán học và mô hình AI tiên tiến, chạy trực tiếp trên thiết bị nhúng (Orange Pi 5 Pro). Một kế hoạch chi tiết đã được xây dựng để người dùng tận dụng tối đa thời gian chờ vật liệu, nhằm thuần thục phần cứng (Arduino Mega, Orange Pi) và chuẩn bị hạ tầng kỹ thuật sẵn sàng cho việc phát triển và kiểm chứng đề tài.

Các điểm chính:
- Chuyển hướng chiến lược: từ bỏ "đệm khí" do quá nhiều rủi ro về cơ khí, cảm biến và kiểm chứng lâm sàng; chuyển sang "lót giày thông minh".
- Trọng tâm "kháng trôi dạt" (Drift-Resistant): dùng đạo hàm biến thiên áp lực theo thời gian (dP/dt) để triệt tiêu ảnh hưởng của trôi dạt do nhiệt độ và biến dạng vật liệu của Velostat.
- Ứng dụng mô hình AI tiên tiến: ST-GNN mô hình hoá bàn chân như đồ thị giải phẫu, suy ra lực trượt ngang (Fx, Fy) từ dữ liệu áp lực dọc (Fz).
- Phần cứng + phần mềm phối hợp: Arduino Mega thu 16 kênh ADC tần số cao; Orange Pi 5 Pro (NPU 6 TOPS) suy luận AI tại biên.
- Đã xác định khoảng trống nghiên cứu: chưa có giải pháp giá rẻ nào giải quyết triệt để drift qua nhiều phiên đo cho Velostat.
- Chuẩn bị phản biện: quy trình 5 "ghế" (Cơ sinh học, Nhúng, AI, Đạo đức, Devil's Advocate) + chiến lược trả lời 5 câu hỏi "chí mạng".

Sau đó nén cuộc trò chuyện này, lưu trữ vào github. Rồi đổi tên github như nào luôn. Bạn cứ làm đi còn thông tin nữa mà tôi sẽ gửi sau.
```

</details>

---

## 3. Cách dùng tệp này

- **Khôi phục ngữ cảnh:** đọc mục 1, sau đó mở `DECISION_LOG.md` + `PROJECT_SNAPSHOT.md`.
- **Truy xuất nguồn gốc:** mục 2 (nguyên văn) là nguồn chuẩn cho mọi diễn giải ở mục 1; nếu khác nhau, nguyên văn thắng.
- **Cập nhật:** khi chủ dự án gửi thông tin mới, append tệp hội thoại mới `CONVERSATION_YYYY-MM-DD.md` và cập nhật DECISION_LOG/SNAPSHOT, không sửa ngược lịch sử.

---

## 4. Phần 2 — thông tin bổ sung (cùng ngày 2026-08-25)

> **Lưu ý định danh tài liệu:** phần 1 dẫn tới `docs/30_TOPIC_PIVOT_Smart_Insole.md`; file đó đã được thay thế bằng `docs/01_Topic_Definition.md` (tinh chỉnh). Mọi tài liệu đề tài cũ đã bị xóa theo DEC-TOPIC-003.

### 4.1 Tóm tắt nén (compressed)

1. **Định nghĩa đề tài (tinh chỉnh):** "Lót giày Edge-AI ước lượng liên tục 3D-GRF & COP, drift-robust, để phát hiện sớm thay đổi động học dáng đi & theo dõi đáp ứng phục hồi ở người nguy cơ/mắc knee OA."
2. **Novelty (insight quan trọng nhất):** KHÔNG coi "3D-GRF estimation" là novelty chính — literature 2025–2026 đã có. Trọng tâm mới = **longitudinal, drift-robust kinetic monitoring** (tách Δ_biology khỏi Δ_sensor/Δ_environment).
3. **Chuyển hướng mục tiêu:** không "chẩn đoán OA bằng AI" mà "theo dõi dọc sự thay đổi động học dáng đi của một cá nhân, phân biệt thay đổi sinh học thật với drift cảm biến & biến thiên giữa các ngày".
4. **Mục tiêu tối thượng:** biến phép đo force-plate trong lab thành **wearable liên tục ổn định theo thời gian** ("mang phòng lab đi cùng người bệnh").
5. **Liên hệ knee OA:** chuỗi `Gait → GRF/COP → Knee loading pattern`; KHÔNG claim `GRF ⇒ OA`, không chẩn đoán/điều trị/thay thế bác sĩ/X-ray/MRI/force plate.
6. **RQ 2 tầng:** (1) duy trì 3D-GRF/COP đủ ổn định qua nhiều phiên để phân biệt thay đổi động học thật với drift & biến thiên? (2) thay đổi phát hiện có theo dõi được suy giảm/cải thiện chức năng liên quan knee OA?
7. **Killer experiment:** không drift correction → error↑; có → error≈const; **false change detection↓**.
8. **Ứng viên novelty A–E; chọn E (biology-vs-sensor) + D (longitudinal change detection).**
9. **Phần cứng tái sử dụng:** Velostat (ma trận cảm biến) + Arduino Mega (acquisition/scanning/sampling) + Orange Pi 5 Pro/RK3588 (edge GNN, INT8).
10. **Nghiên cứu theo tầng (giảm IRB):** healthy/phantom → force-plate validation → gait patterns → (nếu đủ điều kiện) knee OA.
11. **Bước tiếp theo bắt buộc:** literature gap analysis 2025–2026 (10 nhóm chủ đề) — ĐỪNG vội build hardware.
12. **Yêu cầu thao tác:** đọc, cập nhật, viết cơ sở lí thuyết, xóa file đề tài cũ.

### 4.2 Nguyên văn chỉ thị (provenance)

<details>
<summary>Raw owner message — phần 2 (2026-08-25)</summary>

```
Hệ thống lót giày Edge-AI ước lượng liên tục 3D-GRF và COP có khả năng chống trôi dạt để phát hiện sớm sự thay đổi động học dáng đi và theo dõi đáp ứng phục hồi ở người có nguy cơ hoặc mắc thoái hóa khớp gối.

Trong đó:

3D-GRF — Continuous 3D Ground Reaction Forces: Fx: lực trước–sau; Fy: lực trái–phải; Fz: lực thẳng đứng.
COP — Center of Pressure trajectory: quỹ đạo tâm áp lực dưới bàn chân.
Edge-AI: xử lý/suy luận ngay trên thiết bị, hướng tới RK3588/Orange Pi 5 Pro.
Drift-resistant: giải quyết hiện tượng trôi cảm biến, đặc biệt quan trọng với Velostat.
Ultimate application: theo dõi thay đổi cơ học của dáng đi theo thời gian; hỗ trợ phát hiện sớm thay đổi bất thường liên quan đến knee OA; theo dõi đáp ứng phục hồi.

2. Vì sao đề tài này xuất hiện?
Trước đó đã thử rất nhiều hướng: phantom hồi sức sơ sinh; cầm máu cấp cứu; hỗ trợ giao tiếp người hạn chế vận động; hỗ trợ nuôi ăn; tactile sensing; orthosis; rehabilitation; smart phantom. Vấn đề chung: human impact tốt nhưng novelty chưa đủ mạnh, hoặc clinical proxy khó, IRB/participant khó, mechanical complexity, direct neighbors trong literature quá nhiều, khó chứng minh "cái này tốt hơn cái đang có".
Sau khi reverse-engineer các dự án ISEF/ViSEF, thống nhất không nên bắt đầu bằng "người yếu thế cần gì?" mà bằng: bottleneck khó → biến ẩn khó đo → phương pháp mới → benchmark định lượng → impact.

3. Insight quan trọng nhất: không nên coi "3D-GRF estimation" là novelty chính. Literature 2025–2026 đã có: smart insole + ML ước lượng 3D-GRF; pressure insole + IMU + ML; spatiotemporal GCN cho continuous 3D-GRF; GRF liên quan knee OA. "Em dùng Velostat + GNN để dự đoán 3D-GRF" chưa đủ mới — nguy cơ rơi về ~70–80 điểm.

4. Cú chuyển hướng quan trọng: thay vì "chẩn đoán thoái hóa khớp gối bằng AI" → "theo dõi liên tục sự thay đổi động học dáng đi của một cá nhân trong thời gian dài, đồng thời phân biệt thay đổi sinh học thật với drift của cảm biến và biến thiên giữa các ngày." Trọng tâm khoa học = Longitudinal, drift-robust kinetic monitoring.

5. Mục tiêu tối thượng: không phải đo GRF (GRF là phương tiện) mà biến phép đo động học trong phòng lab (force plate) thành wearable liên tục, đủ ổn định theo thời gian để phát hiện thay đổi thật trong dáng đi của từng cá nhân — "mang phòng lab đi cùng người bệnh": smart insole → GRF + COP → hàng nghìn bước → nhiều ngày/tuần → gait trajectory theo thời gian.

6. Tại sao liên quan knee OA: knee OA liên quan cách chịu tải, phân bố lực, braking/propulsion, bất đối xứng hai chân, biến đổi COP, gait mechanics. Chuỗi: Gait → GRF/COP → Knee loading pattern. KHÔNG claim GRF⇒OA hay "hệ thống chẩn đoán thoái hóa khớp".

7. Cách đặt mục tiêu y sinh an toàn: khoa học = continuous drift-robust 3D kinetic estimation from wearable plantar sensing; ứng dụng = longitudinal detection of abnormal gait changes; y sinh = hỗ trợ theo dõi thay đổi chức năng vận động & đáp ứng phục hồi ở người nguy cơ/mắc knee OA. Không tuyên bố: chẩn đoán/điều trị OA, thay thế bác sĩ/X-ray/MRI/force plate.

8. Tại sao force plate quan trọng: so sánh predicted 3D-GRF ↔ force plate ground truth; predicted COP ↔ force plate COP; báo RMSE/MAE/NRMSE/R²/COP error/temporal alignment/drift/cross-session error — ground truth sạch cho Embedded/Engineering.

9. "Drift" có thể trở thành contribution chính: baseline drift, hysteresis, sensitivity change, calibration drift, fitting change, nhiệt/tải change, session variation. ΔCOP = Δ_biology + Δ_sensor + Δ_environment — tách Δ_biology khỏi Δ_sensor là bài toán thú vị nhất.

10. Pipeline dự kiến: Velostat pressure → ADC/Arduino → spatial pressure map → spatio-temporal graph → Edge-AI/GNN → 3D-GRF + COP → drift correction → personal baseline → longitudinal deviation → gait change detection → rehabilitation monitoring.

11. Có thể phát triển closed-loop: Measure→Detect→Intervene→Measure (baseline gait → phát hiện bất thường → can thiệp phục hồi → đi lại bằng insole → GRF/COP thay đổi? → đánh giá đáp ứng). Không tự claim "điều trị" — hỗ trợ theo dõi & đánh giá đáp ứng can thiệp.

12. Beneficiary: ưu tiên người nguy cơ/mắc knee OA trong theo dõi phục hồi. Nghiên cứu theo tầng: GĐ1 healthy/phantom/controlled loading; GĐ2 validation force plate; GĐ3 gait patterns; GĐ4 (nếu đủ điều kiện đạo đức & đối tác) người knee OA — giảm đáng kể rủi ro IRB.

13. Điểm mạnh: ground truth tốt (force plate); embedded tự nhiên (sensor/acquisition/signal processing/edge inference/real-time); ML thật (P(x,y,t) phù hợp graph/spatiotemporal); có biomechanics; human impact; mở rộng (stroke, Parkinson, gait asymmetry, sports, fall-risk).

14. Điểm yếu lớn nhất: novelty chưa đủ nếu chỉ Velostat→GNN→3D-GRF→OA. Ứng viên mạnh: A drift-resistant estimation; B cross-session generalization; C personal baseline; D longitudinal change detection; E biology-vs-sensor separation. E + D hấp dẫn nhất.

15. Killer experiment: không drift correction → error↑; có → error≈constant; false change detection↓. Giả thuyết: sau 30 ngày, phương pháp giảm sai lệch liên-session và giảm false gait-change detection đáng kể so với calibration thường.

16. Điểm dự kiến (heuristic chiến lược, không phải điểm ban giám khảo): Smart insole 3D-GRF/COP + drift robustness: tốt 78–82, ceiling 90–93+; các đề tài cũ 58–89.

17. DNA: wearable pressure sensing → 3D-GRF+COP → drift-aware estimation → personal baseline → longitudinal kinetic change → early functional warning → rehabilitation monitoring.

18. Phần cứng sẵn có tái sử dụng: Velostat (pressure sensing matrix), Arduino Mega (acquisition/scanning/sampling/preprocessing), Orange Pi 5 Pro/RK3588 (signal processing, GNN inference, INT8, real-time edge, logging).

19. RQ cuối nên hướng tới: (1) hệ thống lót giày cảm nhận áp lực có duy trì 3D-GRF/COP đủ ổn định qua nhiều phiên để phân biệt thay đổi động học thật với drift & biến thiên? (2) thay đổi phát hiện có dùng để theo dõi suy giảm/cải thiện chức năng liên quan knee OA?

20. Pitch ngắn nhất (cho giáo viên) + nguyên tắc quan trọng nhất: ĐỪNG vội build hardware — bước tiếp theo là literature gap analysis 2025–2026 quanh: Velostat+plantar pressure, 3D-GRF, COP, drift/hysteresis, cross-session generalization, personal calibration, longitudinal gait monitoring, knee OA biomechanics, GNN/ST-GCN gait, Edge/INT8 deployment.
```

</details>

---

## 5. Chỉ thị chiến lược bổ sung — săn “golden novelty” (2026-08-25)

### Tóm tắt bền vững

Chủ dự án yêu cầu đổi cách tìm novelty: **reverse-engineering literature**, không brainstorm tính năng/phần cứng. Định nghĩa làm việc:

`important unsolved bottleneck + reason existing methods fail + plausible new mechanism + killer experiment`.

Quy trình bắt buộc: vẽ technology landscape; đọc Limitations/Discussion/Future Work/Methods/Dataset; chuyển từng failure thành Gap Card; tìm contradiction “works / fails under condition B”; xác định hidden variable; chỉ sau đó xét Velostat/Mega/RK3588 có phục vụ hypothesis không.

Trọng tâm ưu tiên: **measurement reliability/fidelity under time, condition and person variation**, đặc biệt câu hỏi liệu hệ thống có thể phân biệt thay đổi gait với thay đổi measurement system. Không coi “Velostat + RK3588 + GNN” là novelty.

Yêu cầu đầu ra kế tiếp: **Gap Matrix 20–30 paper (2020–2026)**; mỗi paper bóc: đã làm gì, failure, limitation tác giả tự nêu, ai đã giải tiếp, gap còn lại, và độ khớp hardware. Chỉ giữ gap có điểm cao theo importance/novelty/depth/measurability/ground truth/feasibility/ISEF impact/ceiling.

### Kiểm chứng ban đầu từ dẫn liệu chủ dự án

- Lead “Reliable Vertical Ground Reaction Force Estimation with Smart Insole During Walking” được xác minh là **arXiv preprint 2025** (`arXiv:2501.07748`), không phải paper năm 2021. Nó là close prior art cho IMU + contact-geometry (center of pressed sensors) + ML để giảm lệ thuộc magnitude pressure trong vGRF; chưa phải bằng chứng separation biology-vs-sensor nhiều session.
- CoP paper 2022 xác minh calibration task-match, vertical force, và số pressure cells ảnh hưởng accuracy; benchmark 2019 xác minh placement/stacking insole ảnh hưởng accuracy. Đây là candidate hidden variables/controlled interventions, chưa phải novelty confirmed.

### Artifact liên quan

`research/reviews/2026-08-25_golden_novelty_hunt.md`; `research/evidence/SOURCE_LEDGER.csv`; `research/queries/QUERY_LOG.jsonl`.

---

## 6. Hypothesis lock and pre-model gates (2026-08-25)

Owner directed that the project stop brainstorming and test one hypothesis:

> Can controlled measurement perturbations estimate measurement integrity in a low-cost plantar sensing system and reduce false longitudinal gait-change alerts without substantially increasing missed true changes?

Owner required three pre-model artifacts: a 30–50-paper prior-art kill matrix; a precise perturbation protocol (placement, loading history, calibration mismatch, footwear/context); and a falsification plan. The primary endpoint is false longitudinal gait-change alert rate; missed changes, coverage, selective risk, session error and abstention are secondary/guardrail metrics. Abstention cannot be treated as success without a coverage–risk analysis.

GO/NO-GO gates: no full near-neighbor; 2–3 bench perturbations cause reproducible degradation beyond noise; simple baseline produces false alerts; proposed method improves false alerts without unacceptable missed alerts/low coverage. No full system/GNN work before these gates. Human testing remains subject to ISEF/IRB/SRC requirements.

Artifacts: `research/reviews/01_prior_art_matrix.md`, `research/protocols/02_perturbation_protocol.md`, `research/protocols/03_falsification_plan.md`.

---

## 7. Engineering baseline and owner experience (2026-08-25)

Owner reports that direct GPIO UART/serial between Orange Pi 5 Pro and Arduino Mega is already functioning. The plan must not treat basic communication as unresolved; it must document the actual UART device/pins, voltage-interface/level-shifting method, common ground, baud rate and measured logic levels before research acquisition. USB remains an optional diagnostic fallback.

Owner also reports prior participation in 2 Vietnamese science-and-engineering (KHKT) competitions and 5 engineering competitions. This is planning/background context only and is not evidence for prototype readiness, validation, or future competition outcome.

---

## 8. Owner-reported Mega ↔ Orange Pi diagnostic run (2026-08-25)

Owner reports a GPIO UART diagnostic run: Mega configured at 115200 baud, 16 channels × 100-Hz frame target, ADC prescaler 64, 11,511 sent frames and no reported Mega errors. Orange Pi reports 11,510 received frames, zero CRC failures/gaps, one disconnect/reconnect, CPU 47.153 C, and 54.13 fps across 212.6 s. Owner explains firmware deliberately alternates 60-s send and 60-s no-send states; 11,510/212.6 ≈ 54.1 frames/s, so the reported whole-runtime average is expected. This is owner-reported status pending raw-log reprocessing; it is a deliberate transport-disconnect test, not continuous 100-Hz validation or sensor/ADC-quality evidence.
