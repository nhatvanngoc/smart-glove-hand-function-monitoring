# GATE experiment — Hướng C: Velostat dynamic-pressure có đo được độ cứng mô không?

> ⚠️ **SUPERSEDED — KHÔNG DÙNG (2026-09-13).**
> File này là GATE experiment của Hướng C (**theo dõi độ cứng mô gan chân / sàng lọc DFU**), đã bị bỏ ngày 2026-08-28 vì GATE 3 (Usefulness) yếu.
> GATE experiment hiện hành: `research/protocols/06_glove_hand_GATE_experiment.md`.


**Ngày soạn:** 2026-08-26 · **Trạng thái:** CHỜ vật liệu (Velostat). Đây là thí nghiệm **quyết định** Hướng C sống hay chết.

## Câu hỏi gate (duy nhất)
> Một cảm biến/mảng Velostat giá rẻ, dùng **đáp ứng ĐỘNG** (nén lặp, tải ngắn), có **phân biệt được các mức độ cứng mô khác nhau** (mô phỏng: mô khỏe → callus → mô xơ tiểu đường) **VƯỢT LÊN TRÊN độ trôi/trễ của chính nó** không?

Nếu KHÔNG → Hướng C sụp về vật lý → bỏ hoặc đổi trục.

## Giả thuyết nền (đã có bằng chứng y văn)
- Độ cứng mô gan chân **tăng** ở bàn chân tiểu đường/callus và **là biomarker nguy cơ loét** (đã thiết lập — không cần chứng minh lại).
- Vật liệu cứng hơn → **biến dạng ít hơn ở cùng lực**, và **đáp ứng động (tốc độ hồi, diện tích vòng trễ chuẩn hóa) khác** → Velostat đọc được.

## Dụng cụ (rẻ, bench, không cần người/IRB)
1. **Phantom độ cứng biết trước** (ground truth): silicone/polyurethane nhiều mức Shore (mềm ~ mô khỏe; trung bình ~ callus; cứng ~ mô xơ). Hoặc hydrogel điều chỉnh cross-linking (như bạn đề xuất).
2. **1 mảng Velostat** (hoặc 1–2 ô) + điện cực + **Arduino Mega** đọc ADC.
3. **Jig nén** cố định: 1 đầu ấn phẳng gắn vào trục (in 3D / kẹp), nén vuông góc, độ sâu/lực lặp lại.
4. **Cảm biến lực tham chiếu** (load cell rẻ + HX711) để biết lực thật đặt vào (làm chuẩn, KHÔNG phải force plate).
5. **Bệ cứng** đặt phantom (để lực truyền qua phantom, không qua nền mềm).

## Quy trình
**A. Đo đáp ứng động theo độ cứng (core):**
- Đặt phantom lên bệ cứng → Velostat ở trên → jig nén **lặp** (vd 20 chu kỳ, cùng biên độ lực, cùng tốc độ), ghi tín hiệu Velostat + load cell.
- Lặp với **từng mức Shore** (mỗi mức ≥3 mẫu, ≥3 vị trí để giảm nhiễu).

**B. Tách tín hiệu mô khỏi drift của cảm biến (self-validation):**
- **Ô tham chiếu / đo trên bệ cứng:** nhấn Velostat lên **bề mặt cứng đã biết** (không có phantom) → đây là **drift thuần của cảm biến** theo thời gian/chu kỳ.
- Trừ phần drift này khỏi tín hiệu đo trên phantom → phần còn lại = **đáp ứng của phantom (mô)**.

**C. Ổn định dài ngày (mô phỏng longitudinal):**
- Đo lại **cùng 1 phantom** mỗi ngày trong 5–7 ngày → kiểm tra hệ **không báo động giả** khi độ cứng không đổi (dù cảm biến trôi).

## Feature cần trích (chống drift — theo đúng ý bạn)
- **Tỷ lệ slope**: slope nhánh nén / slope nhánh nhả.
- **Vòng trễ chuẩn hóa**: diện tích vòng trễ / (đỉnh lực × đỉnh chuyển vị).
- **Độ cứng động proxy**: Δlực/Δbiến dạng ở pha nén (sau khi trừ drift).
- **Đạo hàm theo ngày**: tốc độ đổi của các metric trên (cho phần longitudinal).

## Tiêu chí PASS / FAIL (định lượng, quyết định)
- **PASS-A (phân biệt):** 3 mức Shore tách biệt rõ — vd effect size lớn / phân loại 3 lớp accuracy cao / chồng lấn phân bố thấp.
- **PASS-B (tương quan):** metric (đã trừ drift) **tương quan đơn điệu** với Shore đã biết (R² khá, vd ≥0.7).
- **PASS-C (tín hiệu > drift) — QUAN TRỌNG NHẤT:** biên độ tín hiệu do **đổi độ cứng** phải **lớn hơn** biên độ drift của cảm biến trong cùng khung thời gian (vd tỷ lệ ≥2:1). **Nếu FAIL-C → Hướng C chết.**
- **PASS-D (longitudinal):** đo lại cùng phantom nhiều ngày → không có "cảnh báo giả" vượt ngưỡng.

## Đọc kết quả
- **PASS hết** → Hướng C khả thi → viết proposal đầy đủ; novelty neo vào **(1) dynamic-pressure stiffness proxy** (vật lý), các phần (2)(3) là execution/hỗ trợ, KHÔNG claim là mới.
- **FAIL-C** (drift lấn át) → Hướng C sụp → báo thẳng, đổi trục (bỏ Velostat hoặc bỏ ràng buộc human-pressure).
- **FAIL-A/B nhưng PASS-C** → tín hiệu có nhưng yếu/ồn → cân nhắc cải thiện jig/feature hoặc hạ tham vọng.

## Ghi chú trung thực
- Gate này **không** chứng minh giá trị lâm sàng (cần bệnh nhân + theo dõi dài, ngoài phạm vi học sinh). Nó chỉ chứng minh **tính khả thi vật lý** của cảm biến — đủ để làm đề tài proof-of-concept bench cho ViSEF/ISEF.
- Không claim chẩn đoán; chỉ "sàng lọc/theo dõi nguy cơ".
