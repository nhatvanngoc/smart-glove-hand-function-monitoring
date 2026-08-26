# Phản biện 5 ghế — Smart Insole Edge-AI (3D-GRF & COP)

> **Ngày:** 2026-08-25 · **Áp dụng cho:** đề tài Smart Insole (`docs/01_Topic_Definition.md`).
> **Bổ sung cho:** `research/protocols/ISEF_REVIEW_ORCHESTRATION.md` (6-lane tổng quát). Giao thức 5 ghế này chuyên cho đề tài hiện tại.
> **Cập nhật lần 2 (tinh chỉnh novelty):** trọng tâm phản biện là **longitudinal drift-robust kinetic monitoring** (tách Δ_biology khỏi Δ_sensor/Δ_environment) và **killer experiment** (drift correction → cross-session error ≈ const + false-change rate ↓). Phản biện "chỉ đo GRF" không còn là đích — đích là **giữ ổn định qua phiên**.
> **Quy tắc độc lập (bắt buộc):** nếu host không tách được sub-agent/model độc lập thật sự thì các ghế chạy **tuần tự trong cùng context** và phải ghi rõ **"sequential role review; không phải independent multi-agent verification"**. Không được gọi là xác minh đa agent độc lập.

---

## 1. Năm ghế chuyên gia

| Ghế | Nhiệm vụ phản biện | Phải tấn công | Không được mặc định |
|---|---|---|---|
| **G1 — Cơ sinh học (Biomechanics)** | Đúng về lý thuyết GRF/COP, pha bước chân, giải phẫu bàn chân, khả năng suy Fx/Fy từ Fz | Tính hợp lệ cơ sinh học của đồ thị bàn chân; COP định nghĩa & đơn vị; giả định đế không trượt; biên độ Fx/Fy thực tế nhỏ và nhiễu | rằng mô hình đồ thị giải phẫu tự nó làm tăng độ chính xác |
| **G2 — Nhúng (Embedded)** | Khả thi về phần cứng, ADC, tần số lấy mẫu, multiplexing, nguồn, NPU, độ trễ | 16 kênh ADC vs số ô cảm biến; tần số lấy mẫu thực; 6 TOPS chỉ là spec; latency/năng lượng; độ bền đế khi gập | rằng "tốc độ cao" là đủ hoặc đã đo được |
| **G3 — AI/ML** | Hợp lệ về học máy: data split, leakage, baseline, uncertainty, overfitting, suy luận | thiếu baseline; rò rỉ dữ liệu (cùng người/cùng phiên ở train+test); ST-GNN quá sức với lượng dữ liệu nhỏ; không báo uncertainty | rằng ST-GNN tốt hơn baseline khi chưa chạy baseline |
| **G4 — Đạo đức & ISEF** | Tuân thủ quy tắc người tham gia, an toàn, phạm vi tuyên bố y khoa | IRB/SRC timing; gọi thiết bị y tế; thu thập dữ liệu sinh trắc; an toàn điện | rằng "người khoẻ mạnh" = không rủi ro, hoặc mentor = IRB |
| **G5 — Devil's Advocate** | Tấn công tiền đề & phạm vi (frame challenge) | vì sao không mua insole thương mại; novelty bị prior art đè; dP/dt không triệt tiêu drift; toàn bộ hướng đi có đáng không | rằng hệ thống đề xuất là giải pháp đúng |

---

## 2. Năm câu hỏi "chí mạng" và chiến lược trả lời

> Nguyên tắc trả lời: **không giả vờ đã có kết quả**. Với mỗi câu, đưa ra (a) phạm vi tuyên bố trung thực, (b) bằng chứng/thí nghiệm sẽ giải quyết, (c) phương án dự phòng nếu thất bại.

### Q1. "Bạn khẳng định kháng trôi dạt, nhưng drift cũng làm nhiễu chính dP/dt — sao chứng minh loại được drift?"

- **Trả lời trung thực:** Chỉ tuyên bố **giảm (attenuation) thành phần trôi dạt chậm kiểu offset**, không tuyên bố **triệt tiêu**. dP/dt giảm offset drift nhưng không loại được gain/sensitivity drift.
- **Bằng chứng giải quyết:** thí nghiệm ghế đo có kiểm soát nhiệt + tải tĩnh dài (hàng giờ) + chu kỳ nén; đo residual drift trong miền dP/dt so với chuẩn vàng; báo cáo **biên trôi dạt định lượng**, không dùng từ "loại bỏ".
- **Dự phòng:** thêm hiệu chuẩn định kỳ, bù nhiệt (tham chiếu cảm biến không tải), hoặc giới hạn thời lượng phiên đo đã được đặc trưng.

### Q2. "ST-GNN trên NPU 6 TOPS của Orange Pi có chạy nổi real-time với 16 kênh ADC tần số cao không? Độ trễ, năng lượng?"

- **Trả lời trung thực:** 6 TOPS là **thông số nhà sản xuất**, chưa phải throughput đo được. Mục tiêu là suy luận **mỗi bước chân/cửa sổ**, không nhất thiết per-sample.
- **Bằng chứng giải quyết:** xuất ONNX → lượng tử hoá INT8 → đo latency/throughput/công suất thực trên Orange Pi 5 Pro; công bố số đo, không ước lượng.
- **Dự phòng:** thu nhỏ mô hình (cắt tỉa, kiến trúc nhẹ hơn, LSTM/CNN gọn); nếu không đạt, chấp nhận mô hình đơn giản hơn có sai số tương đương — hiệu quả phần cứng là kết quả hợp lệ, không phải thất bại.

### Q3. "Không có force plate / tấm đo lực thì lấy đâu ground-truth Fx, Fy để huấn luyện và đánh giá?"

- **Trả lời trung thực:** Đây là **blocker số 1**. Không có chuẩn vàng đa trục thì không thể định lượng sai số 3D-GRF.
- **Bằng chứng giải quyết:** thuê/mượn force plate hoặc load cell đa trục; hoặc giới hạn phạm vi ở **Fz + COP** với chuẩn vàng đơn giản hơn; ghi rõ nguồn gốc nhãn.
- **Dự phòng:** nếu chỉ có Fz/COP, thu hẹp đề tài thành "ước lượng Fz và COP ổn định qua phiên" — vẫn có giá trị khoa học và trung thực hơn là tự bịa nhãn Fx/Fy.

### Q4. "Điểm mới thực sự so với insole thương mại (Nurvv, Sensoria, Moticon…) và nghiên cứu GRF-from-insoles?"

- **Trả lời trung thực:** Không tuyên bố mới "toàn bộ hệ thống". Tuyên bố mới **hẹp** và có điều kiện: (a) nền tảng **giá rẻ Velostat**, (b) **hiệu chỉnh drift qua nhiều phiên** (nếu chứng minh được), (c) **suy lực trượt Fx/Fy từ cảm biến chỉ đo áp lực** (nếu chưa có prior art).
- **Bằng chứng giải quyết:** systematic review có lưu vết (query log + source ledger) với từ khoá cụ thể; bảng so sánh prior art (sensor, ground-truth, drift handling, model, cost).
- **Dự phòng:** nếu prior art đã có, chấp nhận và tái định vị đóng góp (reproduction giá rẻ + đặc trưng drift công khai + bộ dữ liệu mở) — không bịa novelty.

### Q5. "Cảm biến giá rẻ có đủ tin cậy để kết luận gì về sức khoẻ? Thử nghiệm trên người có đúng quy trình?"

- **Trả lời trung thực:** **Không** đưa kết luận y khoa/chẩn đoán. Đây là **nguyên mẫu đo lường cơ sinh học** hỗ trợ **theo dõi** thay đổi chức năng & đáp ứng phục hồi. Không thử người trước **IRB/SRC pre-approval** của hội thi trực thuộc; nghiên cứu theo tầng (healthy/phantom → force plate → gait → OA nếu đủ điều kiện).
- **Bằng chứng giải quyết:** hồ sơ IRB/SRC, consent/assent, đánh giá rủi ro; thử nghiệm bench/mannequin trước.
- **Dự phòng:** nếu chưa được duyệt, toàn bộ phần người tham gia giữ nguyên trạng thái "tạm dừng" và dùng dữ liệu bench.

---

## 2b. Killer experiment — mục tiêu phản biện trung tâm (tinh chỉnh lần 2)

Mỗi ghế G1–G5 phải kiểm tra đề tài có chứng minh được chuỗi sau hay không (không chỉ RMSE một phiên):

1. **Không** drift correction → cross-session error **tăng** theo số phiên.
2. **Có** drift correction → cross-session error ≈ hằng số.
3. **False change detection giảm** trên dữ liệu "không có thay đổi sinh học thật".

Nếu đề tài chỉ báo "RMSE 5% trên một phiên" mà không có 3 mục trên, novelty (E + D) **chưa được chứng minh** — G5 phải hạ bậc tuyên bố novelty.

---

## 3. Quy trình chạy 5 ghế

1. **Đóng băng gói bằng chứng** (packet manifest + SHA-256) như trong orchestration 6-lane.
2. Chạy G1→G5 (song song nếu có thể, ngược lại tuần tự có nhãn). Mỗi ghế ghi artifact immutable với các trường chuẩn (review_id, role, verdict PASS/REVISE/BLOCK, confidence, findings có `exact_claim_or_location` + `evidence path`, unresolved_questions, dissent).
3. **Adjudication** (R7 theo orchestration) hoà giải nhưng **không xoá dissent**; khi bất đồng, giữ trạng thái bảo thủ hơn về an toàn/bằng chứng.
4. Mọi BLOCKER/MAJOR thành mục roadmap có liên kết diff/artifact; "đã sửa" chỉ hợp lệ khi reviewer xác nhận thay đổi thực tế.

## 4. Gắn với quality gates

| Gate | Ý nghĩa cho đề tài này | Blocker cứng |
|---|---|---|
| G0 Baseline lock | chốt số ô cảm biến, chuẩn vàng, mô hình baseline | chưa xác định chuẩn vàng Fx/Fy/Fz |
| G1 Evidence integrity | mọi claim novelty/drift có source/measurement | tuyên bố "loại bỏ drift" khi chưa đo |
| G2 Methods | split không rò rỉ, baseline, uncertainty | leakage cùng người/cùng phiên |
| G3 Safety/ethics | IRB/SRC trước khi thử người | thử người khi chưa duyệt |
| G4 Reproducibility | dữ liệu, hiệu chuẩn, mã, môi trường có version | thiếu raw data/provenance |
| G5 Submission | BLOCKER/MAJOR đã đóng hoặc minh bạch ngoài phạm vi | pseudo-verdict nội bộ thay cho review ngoài |

Không có nhãn "ISEF-ready" khi còn blocker cứng. Một đề tài có thể hứa hẹn mà gate vẫn bị chặn — đó là trạng thái trung thực.
