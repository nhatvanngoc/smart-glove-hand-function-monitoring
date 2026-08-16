# RQ BRIEF — Research Question Brief (ARS Stage 1)
## Đề tài: Hệ thống đệm khí thích ứng tích hợp giao tiếp bằng ánh mắt phòng ngừa loét tì đè

**Học sinh:** Văn Ngọc Nhật Anh — Lớp 11A2, THPT Quảng Trị
**Lĩnh vực:** Hệ thống nhúng (Embedded Systems)
**Cuộc thi:** Khoa học Kỹ thuật dành cho học sinh Trung học — Năm học 2026–2027
**Phiên bản ARS-Codex:** academic-pipeline v3.12.0 + academic-research-suite
**Ngày:** 2026-06-14

---

## 1. Vấn đề nghiên cứu (Research Problem)

### 1.1 Bối cảnh y tế
- **Loét tì đè** (Pressure Injuries, PI) là biến chứng y khoa nghiêm trọng với nhóm bệnh nhân hạn chế vận động (GBD ~2,46 triệu ca/năm; Hoa Kỳ ~26,8 tỷ USD/năm, ~60.000 ca tử vong).
- Bệnh nhân liệt nặng (ALS, locked-in syndrome, chấn thương tủy sống, đột quỵ) đồng thời **mất khả năng giao tiếp bằng lời**, cần giải pháp AAC (Augmentative and Alternative Communication).

### 1.2 Bất cập của giải pháp hiện tại
| Vấn đề | Hiện trạng | Hệ quả |
|---------|-----------|---------|
| Đệm chống loét | Bơm xả luân phiên theo chu kỳ cố định, không dựa trên áp suất thực | Không phân tán tải theo risk map; dễ tổn thương cục bộ |
| Cảm biến áp suất | Velostat dễ drift, hysteresis, phi tuyến khi đo dài hạn | Sai số tích lũy → cảnh báo trễ |
| Mô hình đánh giá | Dùng ngưỡng áp suất tĩnh | Không tính quan hệ **Áp suất – Thời gian – Tư thế (PTI)** |
| Eye-tracking AAC | Camera cố định, đắt tiền, menu tĩnh, không hiểu ngữ cảnh | Lệch khỏi khuôn mặt; câu sinh thiếu tự nhiên |

### 1.3 Câu hỏi nghiên cứu (RQ)
**RQ chính:** *Có thể thiết kế một hệ thống đệm khí thích ứng tích hợp giao tiếp bằng ánh mắt, dựa trên mô hình Áp suất – Thời gian (PTI), để vừa phòng ngừa loét tì đè vừa hỗ trợ giao tiếp cho người hạn chế vận động không?*

**RQ phụ (sub-questions):**
- **SQ1.** Ma trận cảm biến lai (Velostat 8×8 + piezocapacitive nodes) kết hợp cơ chế cross-calibration có giảm được sai số tích lũy so với ma trận Velostat thuần không?
- **SQ2.** Mô hình PTI thích ứng (Pressure-Time-Intensity) kết hợp dự báo CNN-LSTM có cảnh báo sớm hơn ngưỡng áp suất tĩnh trong bao lâu?
- **SQ3.** Hệ đệm khí 64 ô điều khiển PID độc lập có duy trì được áp suất vùng sacrum dưới 32 mmHg khi phân tán tải theo risk map không?
- **SQ4.** Hệ stereo eye-tracking với cụm camera điều khiển bằng robot arm có đạt độ chính xác >80% trong điều kiện xác định không?
- **SQ5.** Mô hình ngôn ngữ Qwen-0.5B fine-tuned bằng LoRA có sinh được câu AAC ngắn đúng ngữ cảnh với độ trễ chấp nhận được không?

---

## 2. Mục tiêu nghiên cứu (Objectives)

### 2.1 Mục tiêu tổng quát
Xây dựng **hệ thống tích hợp hai chức năng** (phòng loét + giao tiếp) cho bệnh nhân hạn chế vận động, có khả năng **tự cải tiến** theo từng người dùng.

### 2.2 Mục tiêu cụ thể (SMART)
1. **Cảm biến:** Tạo pressure map thời gian thực từ ma trận lai 8×8 (64 điểm đo).
2. **Hiệu chuẩn:** Cơ chế cross-calibration Velostat ↔ piezocapacitive giảm drift/sai số tích lũy.
3. **Mô hình PTI:** Mô hình Áp suất – Thời gian – Tư thế thích ứng, cảnh báo sớm hơn ngưỡng tĩnh.
4. **Dự báo:** Mô hình CNN-LSTM dự báo nguy cơ ngắn hạn theo vùng.
5. **Đệm khí:** 64 ô khí điều khiển PID độc lập, giảm peak pressure, duy trì sacrum < 32 mmHg.
6. **Eye-tracking:** Dual global-shutter camera stereo + robot arm 3 DOF, độ chính xác > 80%.
7. **AAC:** Qwen-0.5B + LoRA sinh câu ngắn đúng ngữ cảnh.
8. **Tích hợp:** Vòng lặp tự đánh giá–cải tiến nhằm cá nhân hóa vận hành.

---

## 3. Đối tượng và phạm vi (Scope)

### 3.1 Đối tượng nghiên cứu
- **Con người:** Bệnh nhân liệt (đột quỵ, tủy sống, ALS, locked-in, ICU bất động, người cao tuổi suy kiệt).
- **Giải pháp kỹ thuật:**
  - Ma trận cảm biến lai 8×8 + cross-calibration
  - Mô hình PTI thích ứng + CNN-LSTM
  - Đệm khí 64 ô PID
  - Stereo eye-tracking + robot arm 3 DOF
  - Qwen-0.5B + LoRA fine-tune
  - Vòng lặp tự cải tiến
- **Công cụ phát triển:** Python, C++; STM32, Jetson Orin Nano; Gazebo/ROS2 mô phỏng.

### 3.2 Phạm vi
- **Trong phạm vi:** Pressure map, PTI model, đệm 64 ô, eye-tracking stereo, AAC ngắn, self-improving loop.
- **Ngoài phạm vi:** Bơm máu cục bộ (microcirculation), thiết bị y tế cấy ghép, các phương pháp phẫu thuật.

---

## 4. Tiêu chí thành công (Acceptance Criteria)

| # | Tiêu chí | Đo lường | Ngưỡng |
|---|----------|---------|--------|
| 1 | Pressure map thời gian thực | Tần số cập nhật | ≥ 5 Hz |
| 2 | Hybrid sensing giảm sai số | PTI error reduction | ≥ 20% so với Velostat thuần |
| 3 | PTI cảnh báo sớm | Lead-time so với static threshold | ≥ 30 phút trong mô phỏng |
| 4 | Đệm khí 64 ô duy trì áp sacrum | Mean sacrum pressure | < 32 mmHg |
| 5 | Eye-tracking accuracy | Top-1 icon selection | > 80% |
| 6 | AAC sentence quality | BLEU-4 / chrF | ≥ baseline (keyword-only) |
| 7 | Self-improving | Δ reward sau N episodes | ≥ 10% |

---

## 5. Cấu trúc tài liệu (Documentation Map)
```
docs/
├── 01_RQ_Brief.md              ← file này
├── 02_Literature_Review.md     ← Tổng quan tài liệu có hệ thống
├── 03_Methodology_Blueprint.md ← Phương pháp nghiên cứu
├── 04_System_Architecture.md   ← Kiến trúc hệ thống
├── 05_Hardware_Design.md       ← Thiết kế phần cứng
├── 06_Software_Design.md       ← Thiết kế phần mềm
├── 07_ML_Models.md             ← Mô hình PTI, CNN-LSTM, LoRA
├── 08_Experimental_Protocol.md ← Giao thức thực nghiệm
├── 09_Risk_Register.md         ← Sổ rủi ro & giảm thiểu
└── 10_References.md            ← TLTK có xác minh
```

## 6. Status Dashboard (theo ARS v3.12)
- [x] Stage 0 INTAKE → RQ brief & scope
- [x] Stage 1 RESEARCH → RQ brief + Methodology Blueprint
- [ ] Stage 2 WRITE → Outline & draft paper
- [ ] Stage 2.5 INTEGRITY → pre-review integrity gate
- [ ] Stage 3 REVIEW → first-round review
- [ ] Stage 4 REVISE → revision draft
- [ ] Stage 4.5 FINAL INTEGRITY → final integrity gate
- [ ] Stage 5 FINALIZE → submission package
- [ ] Stage 6 PROCESS SUMMARY → collaboration record
