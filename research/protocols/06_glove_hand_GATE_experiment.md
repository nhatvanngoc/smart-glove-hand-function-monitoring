# 06 — GATE experiment: Găng tay đánh giá, theo dõi & hỗ trợ (AAN) chức năng bàn tay sau đột quỵ

> **Ngày soạn:** 2026-09-13 · **Cập nhật cấu trúc lớn: 2026-10-13** (owner, qua `ask_user`, xem `DEC-GATE-002` ở `DECISION_LOG.md`).
> **Trạng thái:** CHỜ vật liệu + phần cứng (Velostat, khung in 3D, ESP32-S3, CD74HC4067, load cell).
> **Đây là thí nghiệm quyết định đề tài sống hay chết.** Không có GATE pass ⇒ không viết kết luận.
>
> **Lý do tái cấu trúc (2026-10-13):** `DEC-SCOPE-006` (2026-10-11) đã chốt AAN là **trụ cột kỹ thuật thứ 4**, ngang hàng với mảng cảm biến/bộ ba chỉ số/lớp tự kiểm chuẩn — nhưng bảng GATE ở bản cũ của file này **chỉ kiểm chứng nhánh ĐO** (0/A/B/C), còn phần AAN chỉ nằm rải rác dưới tên phụ "GATE A′"/"GATE RAL" trong `07_ral_phantom_and_ktv_interview.md`, không có vị thế ngang hàng. Từ bản này: **hai nhánh song song**, mỗi nhánh có cổng sống còn (⭐) riêng. Đồng thời, **GATE F (INT8/NPU) bị tạm hoãn** — xem §4 — cho tới khi chốt được nhiệm vụ phù hợp nhất cho Orange Pi 5 Pro.
>
> **Nguyên tắc bắt buộc (không đổi):**
> - Toàn bộ GATE ở cả hai nhánh chạy trên **bench/phantom**, **không cần người tham gia** ⇒ không cần IRB cho các cổng này (`DEC-SCOPE-003`/`DEC-SCOPE-006` — ranh giới an toàn phantom-only không có ngoại lệ).
> - Mọi log phải lưu thô, có timestamp, có mã phiên, vào `research/bench/` (và bản gốc không bị sửa).
> - Ngưỡng PASS/FAIL phải **chốt trước khi đo** và ghi vào file này; cấm chỉnh ngưỡng sau khi thấy kết quả. Các ngưỡng đánh dấu **ĐỀ XUẤT — CHƯA CHỐT** là kế thừa nguyên trạng từ `07_ral_phantom_and_ktv_interview.md` (chủ dự án hoãn chốt từ 2026-09-19), không phải số liệu agent tự bịa ra ở bản cập nhật này.

---

## 0. Bảng tổng hợp — hai nhánh song song

### Nhánh ĐO (assessment) — GATE 0 → A → C⭐

| Cổng | Câu hỏi | Nếu FAIL |
|---|---|---|
| **GATE 0** | Sensing element tự chế có lặp lại được không? | Dừng — chưa làm được cảm biến thì không có gì để nghiên cứu |
| **GATE A** | Mảng áp trở vi sai có phân biệt được **chiều gập/duỗi** VÀ lượng hóa **mức kích hoạt nỗ lực** (Bản đồ động học) không? | Bỏ tính năng "hướng lực & kích hoạt"; lùi về đo lực một chiều đơn thuần |
| **GATE C** ⭐ | Thay đổi chức năng thật có **lớn hơn** drift/nhiễu không? | **DỪNG ĐỀ TÀI** hoặc đổi trục nghiên cứu |

### Nhánh TRỢ LỰC — AAN (trụ cột thứ 4, `DEC-SCOPE-006`) — GATE AAN-1 → AAN-2⭐

| Cổng | Câu hỏi | Nếu FAIL |
|---|---|---|
| **GATE AAN-1** | Có phát hiện được **nỗ lực** khi ngón **chưa** di chuyển không? (Effort Index) | Bỏ Effort Index khỏi đề tài; AAN chỉ còn là lò xo trợ lực cố định, không "theo nhu cầu" |
| **GATE AAN-2** ⭐ | Đường cong tải–hoàn thành (RAL) có đơn điệu + ổn định không, **và** mức tham gia chủ động (participation ratio) có được giữ/tăng qua các lần thử, không bị xói mòn về 0 (chống ỷ lại)? | RAL chỉ là thông số bench, **không** được gọi là "trợ lực thích ứng"; AAN bị hạ xuống "trợ lực cố định phân bậc" |

### Cổng Trạm Y Sinh Biên (Edge Intelligence Station) — GATE EDGE (`DEC-ARCH-001`)

| Cổng | Câu hỏi | Nếu FAIL |
|---|---|---|
| **GATE EDGE** | Orange Pi 5 Pro (RK3588, NPU 6 TOPS) có chạy suy luận chính sách AAN & mô hình RL bù trôi/trễ Velostat (MDP) thời gian thực ($\le 20\text{ ms}$) và đối chứng góc ArUco không? | Hạ mức xử lý biên; lùi về các thuật toán lọc tuyến tính cổ điển trên vi điều khiển |

> **Ghi chú quyết định `DEC-GATE-003` (2026-10-13):** Đã chính thức loại bỏ **GATE D** (False Alarm), **GATE E** (Fault Injection) và **GATE AAN-3** (An toàn cơ học chấp hành) khỏi phạm vi tự nghiệm thu của học sinh. Các tiêu chuẩn an toàn thiết bị y sinh và chứng nhận kiểm định độ tin cậy thuộc thẩm quyền của cơ quan thử nghiệm lâm sàng độc lập / phòng đo lường có thẩm quyền, học sinh không tự cấp chứng nhận kiểm định.

**Vì sao đặt ⭐ ở cả hai nhánh:** GATE C trả lời "nhánh Đo có còn lý do tồn tại không" (nếu không nhạy hơn nhiễu thì đo để làm gì); GATE AAN-2 trả lời đúng câu hỏi tương đương cho nhánh Trợ lực — "AAN có thực sự khác gì một lò xo trợ lực cố định không, hay chỉ là trợ lực cố định được gọi tên hoa mỹ". Nếu AAN-2 fail, đề tài **không bị dừng** (khác GATE C) nhưng **bắt buộc đổi nhãn**, không được gọi là "theo nhu cầu"/"thích ứng".

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

## GATE A — Nhận diện Hướng vận động & Bản đồ kích hoạt nỗ lực động (`DEC-GATE-004`)

> **Cập nhật 2026-10-13 (`DEC-GATE-004`):** Đã loại bỏ hoàn toàn khái niệm "tái tạo góc bàn tay 3D" (GATE B cũ) vì mâu thuẫn vật lý: cảm biến áp trở chỉ đo lực nỗ lực tiếp xúc, không có quan hệ đơn ánh với góc khớp sinh học và không thể đổi trực tiếp sang độ ($^\circ$). Toàn bộ việc đánh giá không gian và lực được hợp nhất vào **GATE A mới**: kết hợp suy luận chiều vận động (gập vs duỗi) với lượng hóa các mức nỗ lực (Bản đồ kích hoạt động học).

**Câu hỏi khoa học:** Với mảng sensing element đối xứng trên hai vách cứng (lòng – mu) của khung nẹp, hệ thống có: (1) Xác định đúng **chiều** gập/duỗi từ dấu vector vi sai $S_{palmar} - S_{dorsal}$; và (2) Lượng hóa được các **mức kích hoạt nỗ lực** để hiển thị trực quan bản đồ động học (Kinetic Activation Map) cho kỹ thuật viên theo dõi không?

**Phantom thử nghiệm:** Khung găng in 3D gắn trên bàn tay giả (phantom) có thể tác động lực theo hướng biết trước bằng quả cân/lò xo chuẩn.

**Quy trình:**
1. Tác động lực theo 2 chiều (gập, duỗi) ở 3 mức lực nỗ lực chuẩn ($1\text{ N}, 3\text{ N}, 5\text{ N}$) $\times$ mỗi mức 20 lần lặp.
2. Ghi đồng thời: nhãn chiều nỗ lực + mức lực chuẩn (ground truth) + vector vi sai nội tại.
3. Kiểm tra tính độc lập điểm đặt lực: lặp lại ở các vị trí tiếp xúc khác nhau trên cùng lóng ngón.
4. Trực quan hóa dữ liệu thời gian thực trên Dashboard: hiển thị thanh mức nỗ lực (Activation Bar / Heatmap).

**Thước đo:**
- Độ chính xác phân loại chiều gập/duỗi (Accuracy, %).
- Tỷ lệ phân tách đúng 3 dải nỗ lực ($< 1,5\text{ N}$; $1,5–3,5\text{ N}$; $> 3,5\text{ N}$).
- Độ tương phản tín hiệu giữa hai trạng thái đối lập (SNR vi sai).

**Tiêu chí PASS (chốt trước):**
- Phân biệt cặp đối lập (gập vs. duỗi): Accuracy $\ge \mathbf{90\%}$ trên phantom. Vector trung bình của hai chiều phải **ngược dấu tuyệt đối**.
- Phân tách mức kích hoạt nỗ lực: Accuracy phân cấp 3 dải lực $\ge \mathbf{85\%}$.
- Trực quan hóa bản đồ áp lực: Kỹ thuật viên xem giao diện thời gian thực và phân biệt chính xác trạng thái kích hoạt của từng ngón mà không cần nhìn tay thật.

**Nếu FAIL:** Loại bỏ tính năng "suy luận hướng lực & bản đồ kích hoạt"; lùi về báo cáo chỉ số lực nén một chiều đơn thuần.

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

## §4. Nhiệm vụ cho Orange Pi 5 Pro — Trạm Y Sinh Biên (Edge Medical Intelligence Station) & GATE EDGE (`DEC-ARCH-001`)

> **Cập nhật kiến trúc 2026-10-13 (`DEC-ARCH-001`):** Chốt vai trò của Orange Pi 5 Pro (RK3588, NPU tri-core 6 TOPS) thành **Trạm Y Sinh Biên (Edge Medical Intelligence Station)**, phân tầng rõ ràng với vi điều khiển ESP32-S3:
> - **ESP32-S3 (Tầng chấp hành & An toàn cứng - Hard Real-Time):** Thu thập ADC đa kênh, đọc cảm biến vi sai, giám sát dòng động cơ, ngắt khẩn cấp cơ khí nếu lực vượt $5\text{ N}$. Không chạy mô hình AI nặng để tránh trễ ngắt.
> - **Orange Pi 5 Pro (Tầng trí tuệ biên đa nhân - Edge AI):** Tận dụng kiến trúc 3 nhân NPU và năng lực RKNN INT8 để chạy 3 nhiệm vụ song song, giải quyết trực tiếp các bài toán kỹ thuật chuyên sâu:
>   1. **Nhân NPU 1 — Bù trừ phi tuyến động cho Velostat (RL Sensor Inversion):** Chạy chính sách bù trễ (hysteresis), từ biến (creep) và trôi nhiệt/lão hóa thời gian thực dạng mô hình nơ-ron hồi quy/MDP được lượng tử hóa sang `.rknn`. Chuyển hóa tín hiệu áp trở phi tuyến thành đại lượng lực tuyến tính ổn định qua hàng trăm giờ làm việc.
>   2. **Nhân NPU 2 — Suy luận chính sách thích ứng AAN (Anti-Slacking Actor-Critic):** Tiếp nhận nỗ lực $EI$ và chuyển động ngón tay, suy luận lực bù $F_{assist}$ theo thời gian thực (trễ $< 20\text{ ms}$) nhằm tối ưu hóa phục hồi theo nguyên lý Hebbian và triệt tiêu hiện tượng ỷ lại (Motor Slacking).
>   3. **Nhân NPU 3 + CPU — Kênh thẩm định thị giác độc lập (Camera + Marker ArUco) & Edge Gateway:** Đối chứng chéo quang học góc gập/duỗi với tín hiệu suy luận từ cảm biến vách để kích hoạt cờ tự kiểm chuẩn (GATE E); lưu trữ bảo mật dữ liệu y tế nội bộ không phụ thuộc đám mây (Air-gapped Edge Privacy).

### Tiêu chí nghiệm thu GATE EDGE (Thay thế GATE F cũ):
- **Độ trễ suy luận chính sách (Latency):** $\le 20\text{ ms}$ trên NPU RK3588 (INT8 `.rknn`).
- **Hiệu quả bù trừ vật liệu Velostat:** Sai số trôi (drift) và trễ (hysteresis) sau bù giảm $\ge 60\%$ so với tín hiệu thô trên cùng một chu kỳ tải 100 lần.
- **Tính độc lập thời gian thực:** ESP32-S3 duy trì tần số ngắt an toàn $\ge 100\text{ Hz}$ không bị nghẽn bởi truyền thông dữ liệu với Orange Pi.

---

## Biểu mẫu log tối thiểu

Mỗi phiên đo phải lưu: ngày giờ, mã phiên, nhiệt độ/độ ẩm phòng, mã firmware (git hash), cấu hình kênh, giá trị R_f, số mẫu trung bình N, tốc độ khung thực đo, tải/ground truth, người thực hiện, file log thô, ghi chú bất thường.

Dùng `research/bench/templates/session_manifest.csv` và `research/bench/templates/reference_check.csv`.

---

## Câu chốt dùng khi báo cáo kết quả GATE

> "Chúng tôi không cho rằng hệ thống đo chính xác chức năng bàn tay. Chúng tôi kiểm tra xem **chỉ số thu được có đủ ổn định và đủ nhạy để theo dõi thay đổi theo thời gian hay không**, và chúng tôi công bố cả những trường hợp nó **không** làm được."
