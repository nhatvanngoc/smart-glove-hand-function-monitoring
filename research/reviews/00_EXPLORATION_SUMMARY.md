# 00 — Tổng kết hành trình săn đề tài (kết luận cuối)

> **Ngày:** 2026-08-26 · File này **thay thế** ~15 báo cáo kill-test rời rạc (đã chuyển vào `research/reviews/archive/`).

## Kết luận cuối cùng

**Đề tài chốt (cho ViSEF):** **Hướng C** — *Lót giày Velostat giá rẻ tự kiểm tra độ tin cậy + theo dõi độ cứng mô khu trú ở gan chân, sàng lọc sớm nguy cơ loét bàn chân đái tháo đường tại nhà.* Xem `docs/01_Topic_Definition.md`.

## Vì sao các hướng khác bị loại (tóm tắt kill-test)

| Hướng | Số phận | Lý do chính |
|---|---|---|
| 3D-GRF/COP + knee OA | Loại | Prior art dày (smart insole + ML/IMU/GCN); cần force plate (không có) |
| Measurement-integrity cho gait (C21–C40) | Loại/lưu dự phòng | Personalized-baseline drift-compensation đã là **patent**; gait-variability-là-biomarker đã thiết lập |
| Assistive control (LifeChair-style) | Loại | **LifeChair** đã có + **patent** (closed-loop haptic posture) |
| Tactile biofeedback glove | Loại | Systematic review **101 bài** về AI smart glove; drift-compensation đã có |
| Adaptive seating (neurodivergent) | Loại | Nhóm sản phẩm thương mại có sẵn; validate khó; IRB nặng |
| PI-SSL cho lực | Loại | **UniForce/PhyDNN** đã học lực không cần nhãn |
| Velostat + audio (contact) | Loại | **MicCheck** + audio-tactile fusion đã trưởng thành |
| Transfer learning socket fitting | Loại | **PhyAug/Cross-Domain HAR** đã chiếm; cần sensor đắt; luẩn quẩn accuracy; quay lại socket |

## Quy luật rút ra (quan trọng cho các lần sau)

1. **Cứ "cảm biến áp lực + con người" là prior art dày.** ML-method và application đều đã bão hòa.
2. **Novelty (nếu còn) nằm ở góc VẬT LÝ/CẢM BIẾN cụ thể**, không phải ở ML-method hay application.
3. **ViSEF/ISEF KHÔNG đòi "phát minh thế giới":** rubric ISEF = Creativity 20 + Execution 35 + Presentation 35 → một đề tài **thực thi tốt + tác động thật + sáng tạo vừa phải** là cạnh tranh được. Đừng tự trói vào bar "tiến sĩ".

## Điểm mới thật của Hướng C (neo vào đây)

> **(1) Dynamic-pressure stiffness proxy** — dùng **đáp ứng áp lực động** của Velostat để suy **độ cứng mô khu trú** (callus/xơ hóa). Đây là phần **vật lý**, chưa bị chiếm.

- (2) Self-validation và (3) longitudinal: **KHÔNG mới** (đã có prior art) → là execution, không claim mới.
- **Sống hay chết do GATE experiment** (`research/protocols/05_velostat_stiffness_GATE_experiment.md`): Velostat có phân biệt được độ cứng mô **vượt trên drift của chính nó** không (tiêu chí PASS-C).

## Prior-art key cần trích dẫn (đã verify, xem SOURCE_LEDGER)

- **Biology đã thiết lập:** độ cứng mô gan chân là biomarker nguy cơ DFU (Sci Rep 2025 phantom; J Biomech 2020; elastography studies).
- **Công cụ đo độ cứng hiện có:** MyotonPRO, IndentoPRO, TCM, Shore Durometer, ultrasound elastography.
- **Cận kề cơ chế:** "substrate stiffness ảnh hưởng output cảm biến áp điện trở" (PMC5676615).
- **Velostat đặc trưng:** Hopkins 2020 (IEEE Sensors J) — accuracy 16–48%, drift, hysteresis.
- **Self-validation/drift:** đã có patent/prior art → không claim mới.

## Trạng thái

- **Gate 1 (prior-art):** Hướng C **không bị kill**; novelty hẹp nhưng thật ở góc vật lý.
- **Gate 2 (khả thi vật lý):** **CHƯA ĐO** — chờ Velostat để chạy GATE.
- Không có kết quả thực nghiệm nào trong repo này. Tất cả là định hướng + prior-art.
