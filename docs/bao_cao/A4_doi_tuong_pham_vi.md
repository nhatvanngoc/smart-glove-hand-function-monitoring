# A.4 — Đối tượng và phạm vi nghiên cứu

> **SUPERSEDED 2026-10-19 — draft/archive only.** This text predates `DEC-REHAB-001`; do not reuse as current proposal wording. Current direction: assisted finger flexion/extension → automatic threshold-based AAN → three-digit spoon grasp/lift/transfer/placement; Flex tracks bend/posture, Velostat relative pressure/contact, camera tracks object/target/task outcome and visual feedback. Thresholds, channel map and implementation remain open. See `research/context/CURRENT_DESIGN_BASELINE.md` and `docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md`. Preserve this historical draft and all submitted files unchanged.

- **Đối tượng nghiên cứu:** Di chứng liệt/yếu tay sau đột quỵ và nhu cầu theo dõi chức năng vận động bàn tay tại nhà; hạn chế của các công cụ đánh giá lâm sàng trong theo dõi liên tục; đặc tính kỹ thuật của vật liệu Velostat và phương pháp xây dựng phần tử cảm biến từ vật liệu này.

- **Đối tượng thực nghiệm:** Găng 3 ngón + chuỗi đo vi sai + trạm biên + giàn kiểm định + mô hình tay giả; thu thập, xử lý và phân tích tín hiệu; trích xuất EI/GAP/RAL; thực nghiệm đối chứng luật-thường-vs-học-máy trên sự kiện giả lập.

- **Phạm vi kỹ thuật:** 12 phần tử + ô chuẩn + 1 IMU; cầu vi sai → INA333 → 2×CD74HC4067 → MCP6001 → ADS1115 → ESP32-S3 → BLE → Orange Pi 5 Pro (trạm dùng chung); dashboard + báo cáo tuần; AAN chỉ demo trên phantom.

- **Người đeo (TODO M-26):** ghi rõ ai đeo (kể cả thành viên nhóm), khi nào, biện pháp an toàn (nguồn pin, cách ly lưới, không lực tác động lên người).

- **Giới hạn:** không chẩn đoán; không can thiệp vận động trên người; không thay thế đánh giá lâm sàng; không claim hiệu quả lâm sàng; không thực nghiệm trên bệnh nhân trong giai đoạn này.
