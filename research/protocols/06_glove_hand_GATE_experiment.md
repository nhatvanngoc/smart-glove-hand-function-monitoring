# 06 — GATE experiment: Găng tay đánh giá & theo dõi chức năng bàn tay sau đột quỵ

> **Ngày soạn:** 2026-09-13 · **Trạng thái:** CHỜ vật liệu + phần cứng (Velostat, khung in 3D, ESP32-S3, CD74HC4067, load cell).
> **Đây là thí nghiệm quyết định đề tài sống hay chết.** Không có GATE pass ⇒ không viết kết luận.
>
> **Nguyên tắc bắt buộc:**
> - Toàn bộ GATE 0–F chạy trên **bench/phantom**, **không cần người tham gia** ⇒ không cần IRB cho các cổng này.
> - Mọi log phải lưu thô, có timestamp, có mã phiên, vào `research/bench/` (và bản gốc không bị sửa).
> - Ngưỡng PASS/FAIL phải **chốt trước khi đo** và ghi vào file này; cấm chỉnh ngưỡng sau khi thấy kết quả.

---

## 0. Bảng tổng hợp

| Cổng | Câu hỏi | Nếu FAIL |
|---|---|---|
| **GATE 0** | Sensing element tự chế có lặp lại được không? | Dừng — chưa làm được cảm biến thì không có gì để nghiên cứu |
| **GATE A** | Hệ thống có phân biệt được **hướng** tác động không? | Bỏ tính năng "cảm biến hướng"; lùi về đo lực đơn thuần |
| **GATE B** | Có tái tạo được bàn tay 3D đủ trung thực không? | Bỏ mục tiêu 3D, chỉ báo cáo chỉ số lực |
| **GATE C** ⭐ | Thay đổi chức năng thật có **lớn hơn** drift/nhiễu không? | **DỪNG ĐỀ TÀI** hoặc đổi trục nghiên cứu |
| **GATE D** | Chạy nhiều ngày có báo động giả không? | Phải tăng ngưỡng hoặc bỏ tính năng cảnh báo |
| **GATE E** | Có tự phát hiện được sensing element lỗi không? | Bỏ tính năng self-validation |
| **GATE F** | INT8 trên NPU có đủ nhanh/chính xác không? | Chạy trên CPU, ghi rõ là chưa dùng NPU |

---

## GATE 0 — Độ lặp lại của sensing element

**Câu hỏi:** Cùng một sensing element, dưới cùng một tải lặp lại, có cho cùng tín hiệu không?

**Dụng cụ:** jig nén cơ khí (in 3D/kẹp), load cell + HX711 làm tham chiếu lực, ESP32-S3 + 1 sensing element, bệ cứng.

**Quy trình:**
1. Đo `R_sensor` theo tải tăng dần rồi giảm dần (đường cong tăng/giảm) → xác định **hysteresis**.
2. Giữ tải không đổi trong ≥ 60 giây → đo **creep**.
3. Lặp chu kỳ tải ≥ 100 lần → đo **thay đổi điểm làm việc theo chu kỳ**.
4. Lặp toàn bộ ở 3 ngày khác nhau → đo biến thiên giữa các phiên.
5. Lặp với ≥ 5 sensing element khác nhau (đánh giá chế tạo có nhất quán không).

**Thước đo:** hệ số biến thiên CV (%), độ trễ chuẩn hóa, độ trôi trong 60 s, hệ số tương quan giữa hai lần đo.

**Tiêu chí PASS (chốt trước):**
- CV trong một phiên ≤ 5% ở mức tải làm việc.
- ICC giữa các phiên ≥ 0,75.
- Ghi nhận được đường cong tăng/giảm để **định lượng** hysteresis (không yêu cầu nhỏ, chỉ yêu cầu biết được).

**Nếu FAIL:** quay lại thiết kế cơ khí/electric cực trước, không chạy tiếp.

> **Bản chạy chi tiết (2026-09-19):** [`08_gate0_execution_plan.md`](08_gate0_execution_plan.md) — tách GATE 0 thành **Q1** (độ nhạy: `γ`, `ΔV/σ`) và **Q2** (mạch đọc thật có nghe thấy không: `R₀(F_p) ≤ R_max`), thêm **thí nghiệm quét trở nguồn** để đo `R_max` thay vì đi mượn 100 kΩ, thêm log trôi ≥10 ngày, và **cây quyết định khi fail**. Ngưỡng ở đó là **ĐỀ XUẤT — chủ dự án chốt trước khi đo** (`DEC-SCOPE-003` vẫn hiệu lực).

---

## GATE A — Phân biệt HƯỚNG (điểm kỹ thuật trung tâm của đề tài)

**Câu hỏi:** Với nhiều sensing element trên các vách của khung, hệ thống có xác định đúng **chiều** của lực/phản lực tác động không?

**Phantom:** khung găng in 3D gắn trên **cánh tay phantom** (hoặc bàn tay giả in 3D) có thể gây lực theo hướng biết trước bằng quả nặng/lò xo.

**Quy trình:**
1. Gây lực theo 4 hướng chuẩn trên mặt phẳng (gập, duỗi, trái, phải) ở 3 mức lực (nhỏ/vừa/lớn) × mỗi mức 20 lần.
2. Ghi đồng thời: nhãn hướng (ground truth do người đặt lực gán) + vector kênh thô.
3. Lặp ở **3 vị trí đặt lực khác nhau** trên cùng lóng ngón để kiểm tra hệ thống có phụ thuộc điểm đặt lực không.
4. Phân tích: ma trận nhầm lẫn (confusion matrix) + độ chính xác phân loại hướng.

**Thước đo:** accuracy phân loại hướng, tỷ lệ nhầm lẫn giữa cặp hướng đối diện, khoảng cách Euclid giữa vector trung bình của hai hướng đối lập.

> 📚 **Mốc tham chiếu từ y văn** (thêm 2026-09-19 sau lượt rà soát prior art; **không** đổi ngưỡng — DEC-METRIC-001): các găng đo góc khớp không-IMU đã công bố precision ~1,67% FS / RMS < 3,29° (`SRC-GRATING-GLOVE-2021`), sai số góc ±6° cho găng bend+force dùng để đánh giá chức năng tay (`SRC-FUNCASSESS-2016`), ART-Glove dùng encoder cho 22 DoF (`SRC-ARTGLOVE-2026`). **Nếu GATE A/B chỉ đạt mức "phân loại được hướng" mà sai số lớn hơn hẳn các mốc đó, phải trình bày là bước proof-of-concept và nêu rõ khoảng cách**, không so sánh một chiều với "không dùng IMU".

**Tiêu chí PASS (chốt trước):**
- Phân loại 4 hướng: accuracy ≥ **85%** trên phantom.
- Phân biệt **cặp đối lập** (gập vs duỗi): accuracy ≥ **90%**.
- Vector trung bình của hai hướng đối lập phải **ngược dấu** một cách hệ thống.

**Nếu FAIL:** loại bỏ claim "cảm biến hướng"; chuyển sang báo cáo chỉ số lực đơn hướng và ghi rõ lý do.

---

## GATE B — Tái tạo bàn tay 3D

**Câu hỏi:** Từ trường lực-hướng rời rạc, hệ thống suy luận được hướng gập/duỗi từng khớp và dựng lại bàn tay 3D ở mức chuyên gia đọc hiểu được không?

**Ground truth:** phantom có **khớp đặt được góc biết trước** (in 3D với chốt hãm ở các góc 0°, 30°, 60°, 90°) hoặc goniometer trên phantom.

**Quy trình:**
1. Đặt phantom ở từng tổ hợp góc đã biết (bắt đầu đơn khớp, sau đó đa khớp).
2. Thu dữ liệu, chạy mô hình suy luận, xuất mô hình bàn tay 3D.
3. So sánh **góc suy luận** với **góc đặt thật**.
4. Lặp lại 3 lần mỗi tổ hợp để đánh giá độ ổn định.

**Thước đo:** MAE (độ) theo khớp; RMSE; tương quan giữa góc suy luận và góc thật; đánh giá định tính của KTV (có đọc được động tác không).

**Tiêu chí PASS (chốt trước):**
- MAE ≤ **15°** cho các khớp MCP/PIP trên phantom (đây là mức của một hệ thống proof-of-concept, **không** phải mức thiết bị y tế).
- Tương quan góc suy luận vs góc thật `r ≥ 0,8`.
- KTVVLTL-PHCN xem mô hình 3D và xác nhận **phân biệt được** gập/duỗi từng ngón (đánh giá định tính, ghi lại nguyên văn).

**Nếu FAIL:** hạ mục tiêu 3D xuống "trực quan hóa mức độ kích hoạt" thay vì "tái tạo góc".

---

## GATE C ⭐ — Độ nhạy phát hiện thay đổi (TIÊU CHÍ SỐNG CÒN)

**Câu hỏi:** Thay đổi chức năng **thật** (mô phỏng) có tạo ra tín hiệu **lớn hơn** biến thiên drift/nhiễu của hệ đo trong cùng khung thời gian không?

**Thiết kế:**
1. Tạo **các mức chức năng mô phỏng** trên phantom:
   - Mức 1 — "tay khỏe": lực đầy đủ, biên độ lớn.
   - Mức 2 — "yếu vừa": chặn một phần hành trình/lực (ví dụ giới hạn biên độ ~50%).
   - Mức 3 — "yếu nặng": giới hạn ~25% + có thêm ma sát/thay đổi động học.
2. Mỗi mức đo **lặp lại** ở **nhiều ngày khác nhau** (≥ 5 phiên, ≥ 3 ngày), mỗi phiên ≥ 10 lần lặp.
3. Tính:
   - `Δ_signal` = khoảng cách giữa các mức (effect size, ví dụ Cohen's d).
   - `σ_noise` = độ lệch chuẩn **trong cùng một mức** qua các phiên (bao gồm cả drift).
4. Tính **MDC** của chỉ số: `MDC ≈ 1,96·√2·SEM`.

> 📚 **Mốc so sánh bắt buộc nêu trong báo cáo** (thêm 2026-09-19; ngưỡng PASS/FAIL **giữ nguyên**): `SRC-STEF-MDC-2026` — công cụ chuẩn STEF có ICC 0,98 và **MDC95 = 12,7 điểm** trên n=53 bán cấp; `SRC-MANUMETER-RCT-2022` — hệ đeo đã kiểm định có **MDC ≈ 31%** mức dùng tay trung bình ngày và 100–200 counting sai/giờ. Hai mốc này trả lời câu hỏi *"'MDC nhỏ' là nhỏ so với cái gì?"*: nếu MDC của chỉ số găng tay không cạnh tranh được với 31% (hoặc không giải thích được vì sao khác), GATE C được tính là FAIL về mặt *utility* dù đạt ngưỡng 2σ.

**Tiêu chí PASS (chốt trước):**
- `Δ_signal` giữa Mức 1 và Mức 3 ≥ **2 × σ_noise** (tức là tách được rõ ràng).
- Cohen's d giữa Mức 1 và Mức 2 ≥ **0,8**.
- MDC của chỉ số chính **nhỏ hơn** mức thay đổi giữa hai mức liền kề.
- **Không** có trường hợp chỉ số đảo chiều giữa các phiên ở cùng một mức.

**Nếu FAIL:** **dừng đề tài**. Phải báo cáo thẳng: *"chỉ số thu được không đủ nhạy để theo dõi tiến triển; không thể dùng cho longitudinal monitoring"*. Không được viết báo cáo như thể thành công.

---

## GATE D — Theo dõi nhiều ngày không báo động giả

**Câu hỏi:** Khi chức năng **không** thay đổi, hệ thống có im lặng không?

**Quy trình:**
1. Giữ **nguyên một mức** trên phantom, chạy ≥ 10 ngày (mỗi ngày 1 phiên, mỗi phiên ≥ 10 lần lặp).
2. Bật logic cảnh báo "có thay đổi" của hệ thống.
3. Đếm số lần hệ thống báo thay đổi **trong khi thực tế không có thay đổi**.
4. Lặp lại với điều kiện thay đổi môi trường nhẹ (nhiệt độ phòng khác nhau, tháo và đeo lại găng).

**Thước đo:** tỷ lệ báo động giả (% trên số phiên), biến thiên của chỉ số theo ngày.

**Tiêu chí PASS (chốt trước):**
- Tỷ lệ báo động giả ≤ **10%** số phiên.
- Không có **xu hướng đơn điệu giả** (chỉ số không tự trôi tăng/giảm một chiều theo ngày dù chức năng không đổi).

**Nếu FAIL:** tăng ngưỡng cảnh báo (và ghi rõ độ nhạy bị giảm), hoặc bỏ tính năng cảnh báo, chỉ báo cáo đường cong cho chuyên gia tự đọc.

---

## GATE E — Tự kiểm tra độ tin cậy (self-validation)

**Câu hỏi:** Hệ thống có phát hiện được khi **chính nó** hỏng/sai, thay vì đưa ra kết quả sai không?

**Lỗi mô phỏng có chủ đích (fault injection):**
| Lỗi | Cách tạo |
|---|---|
| Đứt dây một kênh | Ngắt một chân sensing element |
| Chập/mất tiếp xúc | Nối tắt điện cực |
| Kênh trôi mạnh | Gia nhiệt cục bộ hoặc thay đổi preload |
| Suy giảm độ nhạy | Đặt thêm lớp cản cơ khí |
| Nhiễu tăng vọt | Đưa nguồn nhiễu gần mạch đọc |

Mỗi loại lặp ≥ 20 lần.

**Thước đo:** detection rate (%), false alarm rate (%), thời gian phát hiện (số frame).

**Tiêu chí PASS (chốt trước):**
- Phát hiện ≥ **90%** các lỗi mô phỏng.
- Báo động giả trên hệ thống khỏe ≤ **5%**.
- Thời gian phát hiện ≤ **10 giây** kể từ khi lỗi xuất hiện.

---

## GATE F — Suy luận tại biên (INT8 trên NPU)

**Quy trình:**
1. Huấn luyện mô hình trên PC (baseline trước: hồi quy tuyến tính / rừng ngẫu nhiên; chỉ dùng mạng nơ-ron nếu baseline không đủ).
2. Lượng tử hóa INT8 → chuyển sang RKNN → chạy trên NPU của Orange Pi 5 Pro.
3. Đo: độ trễ trung bình/độ trễ đuôi (p95), mức tiêu thụ điện, mức giảm độ chính xác so với FP32.
4. Đo độ trễ end-to-end (từ lúc kết thúc frame trên ESP32-S3 đến lúc cập nhật mô hình 3D).

**Tiêu chí PASS (chốt trước):**
- Độ trễ suy luận ≤ **50 ms** (đủ để phản hồi gần tức thời cho người dùng).
- Mức giảm độ chính xác sau INT8 so với FP32 ≤ **2%**.
- Chạy liên tục 30 phút không treo, không rò bộ nhớ.

> Nếu NPU không dùng được: chạy trên CPU **và ghi rõ trong báo cáo là chưa triển khai NPU** — không được nói "đã triển khai INT8 trên NPU" khi chưa có log.

---

## Biểu mẫu log tối thiểu

Mỗi phiên đo phải lưu: ngày giờ, mã phiên, nhiệt độ/độ ẩm phòng, mã firmware (git hash), cấu hình kênh, giá trị R_f, số mẫu trung bình N, tốc độ khung thực đo, tải/ground truth, người thực hiện, file log thô, ghi chú bất thường.

Dùng `research/bench/templates/session_manifest.csv` và `research/bench/templates/reference_check.csv`.

---

## Câu chốt dùng khi báo cáo kết quả GATE

> "Chúng tôi không cho rằng hệ thống đo chính xác chức năng bàn tay. Chúng tôi kiểm tra xem **chỉ số thu được có đủ ổn định và đủ nhạy để theo dõi thay đổi theo thời gian hay không**, và chúng tôi công bố cả những trường hợp nó **không** làm được."
