# A.2 — Mục tiêu nghiên cứu

> **SUPERSEDED 2026-10-19 — draft/archive only.** This text predates `DEC-REHAB-001`; do not reuse as current proposal wording. Current direction: assisted finger flexion/extension → automatic threshold-based AAN → three-digit spoon grasp/lift/transfer/placement; Flex tracks bend/posture, Velostat relative pressure/contact, camera tracks object/target/task outcome and visual feedback. Thresholds, channel map and implementation remain open. See `research/context/CURRENT_DESIGN_BASELINE.md` and `docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md`. Preserve this historical draft and all submitted files unchanged.

- Chế tạo găng tay thông minh 3 ngón (cái/trỏ/giữa) tích hợp khung vách cứng tiền tải và 12 phần tử cảm biến Velostat + 1 ô chuẩn + 1 IMU, ghi nhận lực và hướng chuyển động từng khớp ngón.

- Xây dựng chuỗi đo vi sai hai vách (lòng–mu) kết hợp auto-zero đầu phiên, giảm ảnh hưởng drift đồng pha và định lượng phần dư bằng thực nghiệm.

- Trích xuất bộ ba chỉ số định lượng EI (nỗ lực chủ động), GAP (thiếu hụt tầm vận động), RAL (mức trợ giúp) kèm nhãn độ tin cậy, theo công thức đăng ký trước khi thu dữ liệu.

- Xây dựng trạm biên (Orange Pi 5 Pro): thu log, kiểm soát chất lượng 2 vòng lặp, dashboard + timeline sự kiện, báo cáo tuần tự động phục vụ kỹ thuật viên theo dõi từ xa.

- Kiểm định toàn bộ hệ thống trên giàn cơ khí + mô hình tay giả theo ngưỡng M1–M6/C1.1–C1.10 đăng ký trước, kèm một thực nghiệm đối chứng luật-thường-vs-học-máy trên sự kiện giả lập.
