# Golden-filter hunt — round 2 (Velostat + thứ khác) — 2026-08-26

Ràng buộc mới của owner: **không** đụng đề tài xe lăn (file PDF), và candidate phải là **Velostat + một thứ khác**. Vẫn problem-first, system-novelty, prototype-first, kill-test sớm.

## Kill-test 3 hướng

| # | Pain point / beneficiary | Hiện có gì | Vì sao thất bại (bằng chứng) | Sống? |
|---|---|---|---|---|
| **F. Chất lượng ép tim CPR** (người tập/bystander) | Manikin QCPR (Resusci Anne), TrueCPR (điện từ), thiết bị phản hồi dùng **accelerometer** | Thiết bị accelerometer **sai trên nền mềm (giường/đệm)** vì cộng cả lún đệm; **không phát hiện leaning** (thiếu hồi vị lồng ngực); TrueCPR đúng nhưng **đắt**. ~28% ép đúng độ sâu | **SỐNG (hẹp)** — gap thật: đo **độ sâu/ép trực tiếp bằng áp lực, đúng cả trên nền mềm, phát hiệnleaning, giá rẻ**. Nhưng manikin phản hồi là mảng **rất chật** |
| **G. Tư thế ngủ nguy hiểm ở trẻ (SIDS)** (trẻ sơ sinh) | **ĐÃ có bài dùng pressure mat + CNN + Velostat** (Technologies 13(10):427, 2025) phát hiện nằm sấp/ngửa; camera (Nanit, Cubo Ai); wearable | Cảm biến đeo → báo động giả nhiều; **FDA: không thiết bị nào được duyệt phòng SIDS** | **CHẾT** — ý "pressure mat + CNN + Velostat cho infant posture" **đã được công bố đúng như vậy** |
| **H. Lực cầm nắm thể thao** (VĐV golf/tenis) | FPPS 7 môn + KNN (Sci Rep 2024); DeChambeau/Microsoft grip 8 cảm biến; strain-gauge golf | Đã có cả academic lẫn thương mại; FSR bị trôi; **tác động con người thấp** (hiệu suất, không khẩn cấp) | **CHẾT** — đã chiếm + ít nhân văn |

## Ứng viên tốt nhất round 2: **F (CPR)** — nhưng phải nói thật

**Câu vàng:**
> "Tôi giải quyết vấn đề **ép tim ngoài lồng ngực sai độ sâu/nhịp/hồi vị** cho **người tập CPR và người cấp cứu tại hiện trường**, vì **thiết bị phản hồi hiện nay (accelerometer) đo sai trên nền mềm như giường/đệm và không phát hiện được leaning, còn TrueCPR chính xác thì quá đắt**; hệ thống của tôi là **tấm đệm cảm biến áp lực Velostat + AI biên**, đo **độ sâu/nhịp/hồi vị/vị trí tay trực tiếp bằng áp lực, đúng cả trên nền mềm**, huấn luyện thời gian thực; tôi chứng minh bằng **độ chính xác đo độ sâu so với cảm biến lực chuẩn, trên cả nền cứng và nền mềm, so với baseline accelerometer**."

- **Velostat + thứ khác:** Velostat (đo áp lực ép) + edge-AI coaching (Orange Pi) + phantom ngực.
- **Prototype-first:** bench hoàn toàn (phantom ngực + nền cứng/mềm + cảm biến lực chuẩn) — **không cần người/IRB**.
- **Điểm mạnh ViSEF:** cứu người (tác động rõ), demo trực quan, "làm được trên giường" là điểm khác biệt dễ hiểu.

## Nói thẳng với owner (trung thực)
- Cả 3 hướng round 2 **đều có prior art**. Infant posture **đã bị công bố đúng ý Velostat** → loại. Sports grip đã chiếm + ít nhân văn → loại.
- **CPR sống được** vì có **gap kỹ thuật thật** (accelerometer sai trên nền mềm + không đo được leaning; TrueCPR đắt) và **rất nhân văn + bench được**. Nhưng mảng "manikin phản hồi CPR" **rất đông**, nên novelty chỉ nằm ở **cơ chế đo áp lực trên nền mềm**, không phải ở ý tưởng "CPR feedback".
- Đây vẫn là đóng góp kiểu **cơ chế/đo-lường** — mạnh về Execution + Human impact cho ViSEF, nhưng **không phải "cơ chế mới đập vào mắt"** cho bar quốc tế khắt khe.

## Nếu owner muốn tiếp
- **Phương án 1:** đào sâu F (CPR) — kill-test vòng 3 (đã có ai làm pressure-based CPR depth trên nền mềm chưa) rồi khóa.
- **Phương án 2:** cào beneficiary khác (người chăm sóc / công nhân / bệnh nhân cụ thể) để tìm pain point có gap "sạch" hơn — vì áp lực-sensing ở đâu prior art cũng dày.
