# Kill-test 3 hướng do owner đề xuất (2026-08-26)

Owner đề xuất 3 hướng (Smart Foam Interface / Tactile Biofeedback Glove / Adaptive Seating neurodivergent), mỗi hướng kèm tuyên bố novelty "chưa có trên IEEE". Đã tra prior art cho từng tuyên bố. Kết quả: **cả 3 tuyên bố đều KHÔNG đứng vững.**

## Direction 1 — Smart Foam Interface (posture/ergonomics + closed-loop haptic)
Tuyên bố: "chưa có closed-loop haptic guidance dựa trên phân bố áp lực động."
**BỊ PHỦ GẦN TRỌN:**
- **LifeChair** (Sensors 18(7):2261, 2018; **bằng sáng chế AU2017101323B4**): đệm cảm biến áp lực vải dẫn + **closed-loop vibrotactile feedback** phân loại tư thế và **rung định hướng để chỉ cách sửa** ("vibration on the left side, encouraging to correct"). Tăng 68.1% thời gian ngồi thẳng. → Đây CHÍNH XÁC là Direction 1, và đã patent.
- **Smart Cushion vibrotactile** (Ishac, Springer 2018): 9 cảm biến áp lực + rung định vị theo vùng cần sửa, 94.1%.
- **Upright Go** (thương mại), **ErgoTac** (IEEE Trans Haptics, hướng dẫn tư thế công thái học), wearable VTI cho công nhân.
- ⚠️ Phần "dự đoán lực nén đĩa đệm L4-L5 +30%" = **overclaim nguy hiểm**: suy ra tải trong cơ thể từ áp lực mặt ghế cần mocap/force-plate/mô hình cơ sinh học; giám khảo biomech sẽ bác (đúng cảnh báo "misuse of GRF to infer internal load").
→ Chỉ còn khe rất hẹp: "spatial pressure guidance cho tương tác tay–dụng cụ", không phải posture chung.

## Direction 2 — Tactile Biofeedback Glove (post-stroke grasp)
Tuyên bố: "relative pattern chống drift là chưa phổ biến."
**BỊ PHỦ:**
- **Systematic review 101 bài (2026)** về AI smart glove (flex+IMU+FSR) cho nhận diện cử chỉ + giám sát phục hồi → mảng găng rehab **cực đông**.
- Chính review đó nêu drift-compensation là **hướng mở đang được làm** → KHÔNG mới; và đã có "physics-informed calibrator + **HMM-based drift correction**" trong găng.
- **Grasp-quality estimation** đã có (Bayesian-network data glove; Tekscan Grip; Pliance Hand).
- **Detecting compensatory movements từ pressure distribution** (JNER 2019, F1 0.98).
→ Không mới. Điểm cộng thật: **bench-testable bằng dynamometer** + human (stroke). Nhưng găng = đông.

## Direction 3 — Adaptive Seating for neurodivergent (autism/ADHD)
Tuyên bố: "human-centered AI vừa nhận diện vừa hành động — rất hiếm."
**BỊ PHỦ:**
- **Hàng loạt sản phẩm thương mại**: Wiggle Seat, Physioworx Inflatable Sensory Cushion, inflatable PeaPod, vibrating FocusPad — đều cho autism/ADHD, deep-pressure/calming.
- **Smart Seat Cushion (UTA)**: đệm **khí tự động điều chỉnh** áp lực (closed-loop, cho wheelchair) → adaptive air-cell cushion **đã có**.
- ⚠️ Validate "giảm lo âu/cải thiện tập trung" ở trẻ neurodivergent = **chủ quan + cần IRB** (dễ sai đạo đức nghiên cứu); engineering (bơm khí vi mô + cảm biến + điều khiển) **quá tải**.
→ Đây gần như là **một nhóm sản phẩm có sẵn**; chỉ "tự động" là mới nhưng khó validate + quá tải.

## Kết luận & quy luật (lặp lại lần nữa, giờ có bằng chứng ở cả 3 hướng)
> **Stack "cảm biến áp lực + feedback + ML" KHÔNG phải nguồn novelty.** Nó đã có ở mọi hướng. Novelty thật (nếu có) chỉ đến từ **một failure mode CỤ THỂ + một nhóm người CHƯA được phục vụ**, không phải từ việc ghép cảm biến/hồi tiếp/AI.

## Xếp hạng khả năng salvage (nếu owner muốn đi tiếp 1 trong 3)
1. **Direction 2** — bench-testable (dynamometer), human thật; nhưng phải thu hẹp thành một khe chưa làm (vd: theo dõi **chất lượng** cầm nắm tại nhà, drift-robust, giá rẻ, so với dynamometer phòng khám). Rủi ro: găng rất đông.
2. **Direction 1** — phải bỏ hẳn posture chung (LifeChair patent) và bỏ dự đoán đĩa đệm; chỉ còn khe hẹp "guidance tương tác tay–dụng cụ".
3. **Direction 3** — yếu nhất: nhóm sản phẩm có sẵn + validate khó + quá tải.
