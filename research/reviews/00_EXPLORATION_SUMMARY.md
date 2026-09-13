# 00 — Tổng kết hành trình săn đề tài

> **Ngày:** 2026-09-13 (cập nhật) · File này **thay thế** ~15 báo cáo kill-test rời rạc (đã chuyển vào `research/reviews/archive/`).

## Kết luận cuối cùng (2026-09-13)

**Đề tài chốt (cho ViSEF):**

> **Nghiên cứu và phát triển găng tay thông minh hỗ trợ đánh giá và theo dõi chức năng vận động bàn tay trong phục hồi chức năng sau đột quỵ.**

Xem `docs/01_Topic_Definition.md` (đề tài), `research/context/DECISION_LOG.md` (DEC-TOPIC-019), `research/protocols/06_glove_hand_GATE_experiment.md` (cổng kiểm chứng).

**Hướng C (DFU tissue stiffness) đã bị bỏ ngày 2026-08-28** — xem bảng bên dưới.

## Vì sao các hướng khác bị loại (tóm tắt kill-test)

| Hướng | Số phận | Lý do chính |
|---|---|---|
| 3D-GRF/COP + knee OA | Loại | Prior art dày (smart insole + ML/IMU/GCN); cần force plate (không có) |
| Measurement-integrity cho gait (C21–C40) | Loại/lưu dự phòng | Personalized-baseline drift-compensation đã là **patent**; gait-variability-là-biomarker đã thiết lập |
| Assistive control (LifeChair-style) | Loại | **LifeChair** đã có + **patent** (closed-loop haptic posture) |
| Tactile biofeedback glove | Loại | Systematic review **101 bài** về AI smart glove; drift-compensation đã có |
| Velostat dynamic-pressure stiffness (DFU) | Loại (2026-08-28) | **GATE 3 (Usefulness) yếu** — stiffness proxy chưa có bằng chứng lâm sàng longitudinal đủ mạnh, không so được với theo dõi nhiệt độ/áp lực |
| Loét tì đè | Loại | Prior art dày hơn DFU; tính khả dụng tại nhà không rõ |
| CPR trên bề mặt mềm | Loại | Đã được giải quyết bằng 2 accelerometer (PMC5143701) |
| Đánh giá spasticity | Loại | Trùng chức năng phụ của đề tài exoskeleton Quảng Trị (giải nhì quốc gia) |
| Adaptive seating (neurodivergent) | Loại | Nhóm sản phẩm thương mại có sẵn; validate khó; IRB nặng |
| PI-SSL cho lực | Loại | **UniForce/PhyDNN** đã học lực không cần nhãn |
| Velostat + audio (contact) | Loại | **MicCheck** + audio-tactile fusion đã trưởng thành |
| Transfer learning socket fitting | Loại | **PhyAug/Cross-Domain HAR** đã chiếm; cần sensor đắt; luẩn quẩn accuracy; quay lại socket |

## Quy luật rút ra (quan trọng cho các lần sau)

1. **Cứ "cảm biến áp lực + con người" là prior art dày.** ML-method và application đều đã bão hòa.
2. **Novelty (nếu còn) nằm ở góc VẬT LÝ/CẢM BIẾN cụ thể**, không phải ở ML-method hay application.
3. **ViSEF/ISEF KHÔNG đòi "phát minh thế giới":** rubric ISEF = Creativity 20 + Execution 35 + Presentation 35 → một đề tài **thực thi tốt + tác động thật + sáng tạo vừa phải** là cạnh tranh được. Đừng tự trói vào bar "tiến sĩ".

## Điểm mới thật của đề tài hiện tại (neo vào đây)

> **(1) Cảm biến HƯỚNG qua vách khung cứng** — dùng áp lực lên **vách cơ khí** để mã hóa **hướng chuyển động của lóng ngón**, không dùng IMU/flex sensor, đồng thời lấy được **độ lớn lực**.

- (2) Đọc vi sai bằng cặp sensing element đối xứng và ô tham chiếu: **KHÔNG mới** (nguyên lý dummy-gauge kinh điển) → là execution, không claim mới.
- (3) Longitudinal tại nhà: **không claim "hệ thống đầu tiên"** khi chưa rà soát xong prior art.
- **Sống hay chết do GATE experiment** (`research/protocols/06_glove_hand_GATE_experiment.md`):
  - GATE A — có phân biệt được **hướng** không?
  - GATE C — thay đổi chức năng thật có **lớn hơn** drift/nhiễu của chính hệ thống không?

## Prior-art key cần trích dẫn (trạng thái từng nguồn ghi ở SOURCE_LEDGER)

- **Gap longitudinal:** Amin K.R. et al., IEEE OJEMB 2024, DOI 10.1109/OJEMB.2024.3523442 (đối tượng là spasticity — dùng để chứng minh khoảng trống chung).
- **Giá trị theo dõi tại nhà:** OTHER study 2026, DOI 10.1080/09638288.2026.2643929.
- **Prior art gần nhất (phải differentiate):** Zhu lab IROS 2017 (15 IMU + 6 Velostat lực tiếp xúc); Reconfigurable Data Glove 2023 (IMU + Velostat).
- **Hạn chế của cách đeo ở cổ tay:** PMC9901039 / medRxiv 2023 (không ghi được chuyển động ngón).
- **Lực ngón có ý nghĩa lâm sàng:** RCT PMC11092254 (2024); PMC10242812 (2023).
- **Đặc tính Velostat:** Hopkins et al., IEEE Sensors J 2020 🔵 verify.
- **Self-validation/drift:** dummy-gauge/reference-cell đã có từ lâu → không claim mới.

## Trạng thái

- **Gate 1 (prior-art):** đề tài găng tay **chưa hoàn tất rà soát** — xem `docs/03_Literature_Gap_Analysis_Plan.md`. Chưa được phép khẳng định "chưa ai làm".
- **Gate 2 (khả thi vật lý):** **CHƯA ĐO** — chờ Velostat + khung in 3D + ESP32-S3 để chạy GATE 0/A/B/C.
- **Chưa có kết quả thực nghiệm nào trong repo này.** Tất cả là định hướng + thiết kế + prior art.
