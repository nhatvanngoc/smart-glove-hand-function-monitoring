# 01 — Định nghĩa đề tài (Hướng C — chốt cho ViSEF)

> **Ngày cập nhật:** 2026-08-26
> **Học sinh:** Văn Ngọc Nhật Anh — THPT Quảng Trị
> **Nguồn gốc quyết định:** `research/context/DECISION_LOG.md` (DEC-TOPIC-017) + `research/reviews/00_EXPLORATION_SUMMARY.md`.
> **Trạng thái bằng chứng:** tài liệu **định hướng**. Mọi tuyên bố novelty/hiệu năng/độ chính xác là **giả thuyết** cho đến khi qua GATE experiment. Chưa có gì là kết quả đã đo.

---

## 1. Tên đề tài

**Tiếng Việt:** Lót giày cảm biến áp lực Velostat giá rẻ **tự kiểm tra độ tin cậy** và **theo dõi độ cứng mô khu trú** ở gan chân, hỗ trợ **sàng lọc sớm nguy cơ loét bàn chân đái tháo đường** tại nhà.

**Tiếng Anh:** A low-cost Velostat pressure-insole that **self-validates its own reliability** and **tracks localized plantar tissue stiffness**, toward **early home screening of diabetic-foot-ulcer (DFU) risk**.

**Pitch 1 câu (nói với giám khảo ViSEF):**
> "Người đái tháo đường hay bị loét bàn chân rồi phải cắt cụt, mà mô đệm dưới gan chân **xơ cứng dần trước khi loét xuất hiện**. Em làm một tấm lót giày bằng **Velostat rẻ tiền** vừa **tự phát hiện khi nào cảm biến bị trôi/lão hóa để không báo sai**, vừa **đo độ cứng mô khu trú bằng đáp ứng áp lực động**, giúp **sàng lọc sớm nguy cơ ngay tại nhà** — thay vì phải đến bệnh viện đo bằng máy đàn hồi đắt tiền."

---

## 2. Vấn đề (problem-first)

- Loét bàn chân đái tháo đường (DFU) là biến chứng nặng, thường dẫn đến **đoạn chi**; chi phí điều trị rất lớn.
- **Trước khi loét xuất hiện**, mô đệm gan chân **tăng độ cứng** (do glycation/xơ hóa). **Độ cứng mô là biomarker nguy cơ DFU đã được y văn xác nhận** (không cần chứng minh lại).
- Hiện đo độ cứng mô bằng **ultrasound elastography / MyotonPRO / IndentoPRO / TCM**: **đắt, cồng kềnh, chỉ ở phòng khám, đo một điểm** → không theo dõi tại nhà được.

## 3. Khoảng trống & ý tưởng

- **Khoảng trống:** chưa có công cụ **rẻ, dạng mảng, tại nhà** để theo dõi độ cứng mô gan chân theo thời gian.
- **Ý tưởng:** dùng **Velostat** (rẻ, mềm, làm được dạng mảng) áp vào gan chân, **nén lặp (áp lực động)**; mô cứng hơn → đáp ứng lực–biến dạng/vòng trễ khác → suy ra **độ cứng khu trú**.
- **Hai trụ hỗ trợ (làm đề tài vững, KHÔNG claim là mới):**
  - **Self-validation:** thêm ô tham chiếu/đo trên nền cứng để phát hiện drift/lão hóa cảm biến → **báo lỗi thay vì báo sai**.
  - **Longitudinal:** so sánh theo ngày/tuần; mảng Velostat rẻ cho phép đo liên tục tại nhà.

## 4. Điểm mới (nói trung thực — theo đúng mức ViSEF)

| Thành phần | Mức mới | Ghi chú |
|---|---|---|
| **(1) Dynamic-pressure stiffness proxy** (dùng đáp ứng áp lực **động** để suy độ cứng mô / phát hiện callus) | **Điểm mới chính (vật lý)** | Đây là thứ duy nhất chưa bị chiếm; **GATE experiment phải xác nhận khả thi** |
| (2) Self-validation bằng ô tham chiếu | **KHÔNG mới** | Đã là patent/prior art (personalized-baseline, reference-cell drift). Chỉ là execution tốt |
| (3) Longitudinal tại nhà | **KHÔNG mới** | Đã có (gait/health longitudinal monitoring). Là giá trị ứng dụng, không phải novelty |
| Mảng Velostat đo áp lực thuần | **KHÔNG mới** | Đã có nhiều |

> **Tuyên bố novelty (hẹp, trung thực):** *"Mảng lót giày Velostat tự đánh giá độ tin cậy và giám sát thay đổi cơ học khu trú tại gan chân"* — novelty nằm ở **góc vật lý (1)**; các phần còn lại là **cách kết hợp ở mức thực tiễn** cho ứng dụng DFU. **Đây là mức novelty phù hợp ViSEF** (chấm Creativity 20 + Execution + Presentation), **không** phải "phát minh thế giới".

## 5. Tuyên bố bị cấm (mất điểm + sai khoa học)

- ❌ Chẩn đoán / điều trị / tiên lượng loét; ❌ thay thế bác sĩ, thay thế elastography/lâm sàng.
- ❌ "Velostat đo chính xác độ cứng tuyệt đối" — chỉ **sàng lọc/theo dõi nguy cơ**, và **phải qua GATE**.
- ❌ Claim (2)/(3) là "mới" (đã có prior art).
- ❌ Thử trên bệnh nhân khi chưa có IRB/SRC — giai đoạn đầu **chỉ bench/phantom**.

## 6. Phạm vi & kiểm chứng

- **Giai đoạn 1 (bench, không cần người):** GATE experiment — xem Velostat có phân biệt được độ cứng phantom **vượt trên drift của chính nó** không (`research/protocols/05_velostat_stiffness_GATE_experiment.md`).
- **Giai đoạn 2 (healthy volunteers):** "mô phỏng bệnh" bằng đế/phantom độ cứng khác nhau; chứng minh phân biệt được "thay đổi mô giả" khỏi "drift thật".
- **Giai đoạn 3 (tùy chọn, cần partner + IRB):** pilot 3–5 bệnh nhân, **chỉ feasibility**, không claim giá trị lâm sàng.

## 7. Phần cứng

- **Velostat** (cảm biến áp lực, dạng mảng) + **Arduino Mega** (đọc ADC nhiều kênh) + **Orange Pi 5 Pro** (Edge-AI, xử lý/self-validation). Chi tiết bring-up: `research/protocols/04_orangepi5pro_mega2560_bringup_tests.md`.

## 8. Lịch sử (rút gọn)

Đề tài đã qua nhiều vòng săn novelty (đo 3D-GRF/COP + knee OA; measurement-integrity cho gait; assistive control; transfer learning…). Hầu hết **bị prior art loại**. Hướng C là hướng **sống sót** vì neo vào **góc vật lý** (độ cứng mô) thay vì ML-method. Toàn bộ lịch sử kill-test: `research/reviews/00_EXPLORATION_SUMMARY.md`.
