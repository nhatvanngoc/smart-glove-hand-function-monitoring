# 06 — GATE experiment: Găng tay đánh giá, theo dõi & hỗ trợ (AAN) chức năng bàn tay sau đột quỵ

> **Ngày soạn:** 2026-09-13 · **Cập nhật cấu trúc lớn:** 2026-10-13.
> **CẢNH BÁO HIỆU LỰC (2026-10-19):** toàn bộ GATE trong tài liệu này được thiết kế cho đề tài monitoring/đo cũ và chưa tái ánh xạ sang chức năng mới `DEC-REHAB-001`. Các phần AAN, cơ cấu, luật điều khiển, ngưỡng lực và thử nghiệm người đã lỗi thời khi trái với baseline hiện hành. Không dùng lò xo, khớp 4 khâu, công thức `F_assist`, 5 N hoặc giá trị số AAN cũ. Hiện hành: hỗ trợ gập–duỗi → tự động chuyển AAN theo ngưỡng → tập task thìa, dùng Flex, Velostat và camera theo vai trò riêng. Dùng protocol 09 làm khung AAN/bench-phantom mới; các GATE cảm biến cũ chỉ là tài liệu tham khảo cần thiết kế lại, không phải GATE pass hay protocol hiện hành.
> **Trạng thái:** CHỜ vật liệu + phần cứng (Velostat, khung in 3D, ESP32-S3, CD74HC4067, load cell).
> **Đây là thí nghiệm quyết định đề tài sống hay chết.** Không có GATE pass ⇒ không viết kết luận.
>
> **Lý do tái cấu trúc (2026-10-13):** `DEC-SCOPE-006` (2026-10-11) đã chốt AAN là **trụ cột kỹ thuật thứ 4**, ngang hàng với mảng cảm biến/bộ ba chỉ số/lớp tự kiểm chuẩn — nhưng bảng GATE ở bản cũ của file này **chỉ kiểm chứng nhánh ĐO** (0/A/B/C), còn phần AAN chỉ nằm rải rác dưới tên phụ "GATE A′"/"GATE RAL" trong `07_ral_phantom_and_ktv_interview.md`, không có vị thế ngang hàng. Từ bản này: **hai nhánh song song**, mỗi nhánh có cổng sống còn (trọng tâm) riêng. Đồng thời, **GATE F (INT8/NPU) bị tạm hoãn** — xem §4 — cho tới khi chốt được nhiệm vụ phù hợp nhất cho Orange Pi 5 Pro.
>
> **Nguyên tắc hồ sơ:**
> - GATE bench/phantom là giai đoạn đầu. Thử AAN có tác động lực trên tình nguyện viên chỉ có thể được xem xét sau đánh giá an toàn đạt và đủ phê duyệt/chấp thuận; xem protocol 09. Nội dung cũ trong file này khẳng định phantom-only tuyệt đối đã bị superseded.
> - Mọi log phải lưu thô, có timestamp, có mã phiên, vào `research/bench/` (và bản gốc không bị sửa).
> - Ngưỡng PASS/FAIL phải **chốt trước khi đo** và ghi vào file này; cấm chỉnh ngưỡng sau khi thấy kết quả. Các ngưỡng đánh dấu **ĐỀ XUẤT — CHƯA CHỐT** là kế thừa nguyên trạng từ `07_ral_phantom_and_ktv_interview.md` (nhóm nghiên cứu hoãn chốt từ 2026-09-19), không phải số liệu agent tự bịa ra ở bản cập nhật này.

---

## 0. Bảng tổng hợp — hai nhánh song song

### Nhánh ĐO (assessment) — GATE 0 → A → C

| Cổng | Câu hỏi | Nếu FAIL |
|---|---|---|
| **GATE 0** | Sensing element tự chế có lặp lại được không? | Dừng — chưa làm được cảm biến thì không có gì để nghiên cứu |
| **GATE A** | Mảng áp trở vi sai có phân biệt được **chiều gập/duỗi** VÀ lượng hóa **mức kích hoạt nỗ lực** (Bản đồ động học) không? | Bỏ tính năng "hướng lực & kích hoạt"; lùi về đo lực một chiều đơn thuần |
| **GATE C**  | Thay đổi chức năng thật có **lớn hơn** drift/nhiễu không? | **DỪNG ĐỀ TÀI** hoặc đổi trục nghiên cứu |

### Nhánh TRỢ LỰC — AAN (trụ cột thứ 4, `DEC-SCOPE-006`) — GATE AAN-1 → AAN-2

| Cổng | Câu hỏi | Nếu FAIL |
|---|---|---|
| **GATE AAN-1** | Có phát hiện được **nỗ lực** khi ngón **chưa** di chuyển không? (Effort Index) | Bỏ Effort Index khỏi đề tài; AAN chỉ còn là lò xo trợ lực cố định, không "theo nhu cầu" |
| **GATE AAN-2**  | Đường cong tải–hoàn thành (RAL) có đơn điệu + ổn định không, **và** mức tham gia chủ động (participation ratio) có được giữ/tăng qua các lần thử, không bị xói mòn về 0 (chống ỷ lại)? | RAL chỉ là thông số bench, **không** được gọi là "trợ lực thích ứng"; AAN bị hạ xuống "trợ lực cố định phân bậc" |

### Cổng Trạm Y Sinh Biên (Edge Intelligence Station) — GATE EDGE (`DEC-ARCH-001`)

| Cổng | Câu hỏi | Nếu FAIL |
|---|---|---|
| **GATE EDGE** | Orange Pi 5 Pro (RK3588, NPU 6 TOPS) có chạy suy luận chính sách AAN & mô hình RL bù động trôi/trễ Velostat (MDP Inversion) thời gian thực ($\le 20\text{ ms}$) hoàn toàn bằng cảm biến nội tại (không camera) không? | Hạ mức xử lý biên; lùi về thuật toán bù tuyến tính tĩnh trên vi điều khiển |

> **Ghi chú quyết định `DEC-GATE-003`, `DEC-GATE-004`, `DEC-GATE-005` (2026-10-13):**
> 1. Đã chính thức loại bỏ **GATE D** (False Alarm), **GATE E** (Fault Injection) và **GATE AAN-3** (An toàn cơ học chấp hành) khỏi phạm vi tự nghiệm thu của học sinh. Các tiêu chuẩn an toàn thiết bị y sinh và chứng nhận kiểm định độ tin cậy thuộc thẩm quyền của cơ quan kiểm chuẩn/lâm sàng độc lập.
> 2. Đã hủy bỏ GATE B cũ (Tái tạo góc 3D bàn tay) và hợp nhất toàn bộ đánh giá hướng và lực vào **GATE A mới** (Nhận diện Hướng vận động & Bản đồ kích hoạt nỗ lực động).
> 3. Tuyệt đối **không sử dụng camera ngoài hay marker ArUco** (`DEC-GATE-005`). Hệ thống hoạt động 100% bằng mảng cảm biến áp trở nội tại tích hợp trên vách cứng khung nẹp, bảo toàn tính gọn nhẹ và độc lập tại chỗ.

**Vì sao đặt  ở cả hai nhánh:** GATE C trả lời "nhánh Đo có còn lý do tồn tại không" (nếu không nhạy hơn nhiễu thì đo để làm gì); GATE AAN-2 trả lời đúng câu hỏi tương đương cho nhánh Trợ lực — "AAN có thực sự khác gì một lò xo trợ lực cố định không, hay chỉ là trợ lực cố định được gọi tên hoa mỹ". Nếu AAN-2 fail, đề tài **không bị dừng** (khác GATE C) nhưng **bắt buộc đổi nhãn**, không được gọi là "theo nhu cầu"/"thích ứng".

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

> **Bản chạy chi tiết (2026-09-19):** [`08_gate0_execution_plan.md`](08_gate0_execution_plan.md) — tách GATE 0 thành **Q1** (độ nhạy: `γ`, `ΔV/σ`) và **Q2** (mạch đọc thật có nghe thấy không: `R₀(F_p) ≤ R_max`), thêm **thí nghiệm quét trở nguồn** để đo `R_max` thay vì đi mượn 100 kΩ, thêm log trôi ≥10 ngày, và **cây quyết định khi fail**. Ngưỡng ở đó là **ĐỀ XUẤT — nhóm nghiên cứu chốt trước khi đo** (`DEC-SCOPE-003` vẫn hiệu lực).

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

## GATE C  — Độ nhạy phát hiện thay đổi (TIÊU CHÍ SỐNG CÒN)

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

>  **Mốc so sánh bắt buộc nêu trong báo cáo** (thêm 2026-09-19; ngưỡng PASS/FAIL **giữ nguyên**): `SRC-STEF-MDC-2026` — công cụ chuẩn STEF có ICC 0,98 và **MDC95 = 12,7 điểm** trên n=53 bán cấp; `SRC-MANUMETER-RCT-2022` — hệ đeo đã kiểm định có **MDC ≈ 31%** mức dùng tay trung bình ngày và 100–200 counting sai/giờ. Hai mốc này trả lời câu hỏi *"'MDC nhỏ' là nhỏ so với cái gì?"*: nếu MDC của chỉ số găng tay không cạnh tranh được với 31% (hoặc không giải thích được vì sao khác), GATE C được tính là FAIL về mặt *utility* dù đạt ngưỡng 2σ.

**Tiêu chí PASS (chốt trước):**
- `Δ_signal` giữa Mức 1 và Mức 3 ≥ **2 × σ_noise** (tức là tách được rõ ràng).
- Cohen's d giữa Mức 1 và Mức 2 ≥ **0,8**.
- MDC của chỉ số chính **nhỏ hơn** mức thay đổi giữa hai mức liền kề.
- **Không** có trường hợp chỉ số đảo chiều giữa các phiên ở cùng một mức.

**Nếu FAIL:** **dừng đề tài**. Phải báo cáo thẳng: *"chỉ số thu được không đủ nhạy để theo dõi tiến triển; không thể dùng cho longitudinal monitoring"*. Không được viết báo cáo như thể thành công.

---

---

## GATE AAN-1 — Nhận diện nỗ lực tĩnh sớm (Effort Index)

**Câu hỏi khoa học:** Khi ngón tay bị giữ chặn cố định (chế độ isometric/isokinetic trên phantom) và có lực nỗ lực co/duỗi tác động lên vách cảm biến, hệ thống có phát hiện được nỗ lực chủ động ($EI$) **trước khi** ngón tay có bất kỳ chuyển động cơ học nào không?

**Phantom thử nghiệm:** Khung nẹp gắn trên bàn tay giả có cơ cấu chặn cứng hành động (khóa ngón cơ học) và cảm biến lực chuẩn (load cell) đối chứng nỗ lực ép vào vách.

**Quy trình:**
1. Khóa cứng ngón tay phantom ở góc duỗi trung tính ($0^\circ$).
2. Tạo 30 chu kỳ nỗ lực ngẫu nhiên (ép gập hoặc ép duỗi với lực $0,5–3\text{ N}$) xen kẽ 30 chu kỳ thả lỏng hoàn toàn ($0\text{ N}$).
3. Đo thời gian trễ từ thời điểm bắt đầu tác dụng lực đến khi thuật toán ngắt phát hiện nỗ lực ($t_{detect}$).
4. Tính chỉ số diện tích dưới đường cong ROC ($AUC$) và tỷ lệ báo động nhầm khi thả lỏng ($FPR$).

**Tiêu chí PASS (chốt trước):**
- $AUC \ge \mathbf{0,85}$ trong việc phân biệt giữa trạng thái cố gắng vận động và trạng thái nghỉ tĩnh.
- Thời gian trễ phát hiện $t_{detect} \le \mathbf{300\text{ ms}}$ (đủ nhanh để kích hoạt servo hỗ trợ trước khi phản xạ ỷ lại xuất hiện).
- Tỷ lệ báo động giả khi thả lỏng tĩnh $FPR \le \mathbf{5\%}$.

**Nếu FAIL:** Bỏ chỉ số Effort Index khỏi danh mục tính năng; cơ cấu AAN chỉ hoạt động như một lò xo trợ lực thụ động cố định, không phải trợ lực kích hoạt theo nhu cầu.

---

## GATE AAN-2  — Tính đơn điệu RAL & Chống ỷ lại vận động (TIÊU CHÍ SỐNG CÒN NHÁNH TRỢ LỰC)

**Câu hỏi khoa học:** Đường cong tải–hoàn thành (RAL) có đơn điệu, lặp lại ổn định giữa các phiên ($ICC \ge 0,75$) **và** mức độ tham gia lực chủ động của người dùng (Participation Ratio) có được duy trì/tăng lên qua các chu kỳ thử, không bị sụt giảm về 0 (triệt tiêu hiện tượng ỷ lại vận động - Motor Slacking) không?

**Thiết kế thử nghiệm:**
1. Đặt phantom ở 3 mức suy giảm lực chủ động giả lập (Mức Yếu, Mức Vừa, Mức Khỏe).
2. Chạy thuật toán tìm nấc trợ lực tối ưu (Multi-Armed Bandit / Policy Gradient) qua 50 chu kỳ cử động liên tục.
3. Ghi nhận: nấc tải cơ khí kích hoạt, mức lực chủ động phantom tự sinh, công sinh bởi cơ cấu servo/lò xo.
4. Lặp lại qua 3 phiên độc lập ở các ngày khác nhau để đánh giá độ tin cậy tái lập.

**Tiêu chí PASS (chốt trước):**
- **Độ ổn định đường cong RAL:** Hệ số tương quan nội lớp $ICC \ge \mathbf{0,75}$ giữa các phiên đo khác nhau.
- **Triệt tiêu hiện tượng ỷ lại (Motor Slacking Mitigation):** Tỷ lệ tham gia chủ động $PR = \frac{F_{chủ\_động}}{F_{tổng}} \ge \mathbf{50\%}$ trên các chu kỳ thành công; hệ thống tự giảm nấc hỗ trợ khi phát hiện lực chủ động tăng.
- **Hiệu quả hội tụ:** Thuật toán Multi-Armed Bandit giảm $\ge \mathbf{40\%}$ số chu kỳ cần thử để tìm nấc tải tối ưu so với phương pháp quét lưới tuần tự.

**Nếu FAIL:** Đề tài **không dừng**, nhưng cơ cấu trợ lực bắt buộc phải đổi nhãn trung thực thành "trợ lực cơ học cố định phân bậc", tuyệt đối không được gọi là "hỗ trợ thích ứng theo nhu cầu (AAN)".

---

## §4. Nhiệm vụ cho Orange Pi 5 Pro — Trạm Y Sinh Biên (Edge Medical Intelligence Station) & GATE EDGE (`DEC-ARCH-001`, `DEC-GATE-005`)

> **Cập nhật kiến trúc 2026-10-13 (`DEC-ARCH-001`, `DEC-GATE-005`):** Chốt vai trò của Orange Pi 5 Pro (RK3588, NPU tri-core 6 TOPS) thành **Trạm Y Sinh Biên (Edge Medical Intelligence Station)**, phân tầng xử lý rõ rệt với vi điều khiển ESP32-S3 và tuân thủ tuyệt đối quy tắc **Zero-Camera Policy** (không dùng camera ngoài hay marker ArUco; 100% xử lý dựa trên mảng cảm biến áp trở nội tại):
> - **ESP32-S3 (Tầng chấp hành & An toàn cứng - Hard Real-Time):** Thu thập tín hiệu ADC đa kênh qua CD74HC4067 + ADS1115, quản lý ngắt mẫu, đọc cảm biến vi sai hai vách, giám sát dòng tải động cơ và ngắt khẩn cấp cơ khí nếu lực vượt $5\text{ N}$. Tần số lấy mẫu duy trì $\ge 100\text{ Hz}$.
> - **Orange Pi 5 Pro (Tầng trí tuệ biên đa nhân - Edge AI & Inversion Layer):** Tận dụng kiến trúc 3 nhân NPU và công cụ lượng tử hóa RKNN INT8 để chạy 3 nhiệm vụ song song:
>   1. **Nhân NPU 1 — Bù trừ phi tuyến động cho Velostat (RL Sensor Inversion qua MDP):** Tiếp nhận dữ liệu điện trở thô từ M1/GATE 0, mô hình hóa các trạng thái quá khứ để chạy chính sách bù trễ (hysteresis), từ biến (creep) và trôi dạt nhiệt theo thời gian thực dưới dạng mô hình nơ-ron hồi quy lượng tử hóa sang `.rknn`. Chuyển hóa tín hiệu áp trở phi tuyến thành đường lực tuyến tính ổn định qua hàng trăm giờ làm việc liên tục.
>   2. **Nhân NPU 2 — Suy luận chính sách thích ứng AAN (Anti-Slacking Actor-Critic):** Tiếp nhận chỉ số nỗ lực $EI$ và vector vi sai, suy luận mức lực trợ lực bù $F_{assist}$ theo thời gian thực (đáp ứng trễ $\le 20\text{ ms}$) nhằm tối ưu hóa phục hồi theo nguyên lý Hebbian và triệt tiêu hiện tượng ỷ lại cơ học.
>   3. **Nhân NPU 3 + CPU — Trạm Y Sinh Biên & Quản trị dữ liệu cục bộ an toàn (Air-gapped Edge Medical Station):** Tính toán bộ chỉ số lâm sàng (EI, GAP, RAL), tổng hợp bản đồ kích hoạt nỗ lực động thời gian thực (Kinetic Activation Map) hiển thị lên Local Telemetry Dashboard; lưu trữ bảo mật hồ sơ tiến trình phục hồi hoàn toàn nội bộ (Air-gapped Edge Privacy), không phụ thuộc đám mây.

### Tiêu chí nghiệm thu GATE EDGE (Thay thế GATE F cũ):
- **Độ trễ suy luận chính sách (Latency):** $\le \mathbf{20\text{ ms}}$ trên NPU RK3588 (INT8 `.rknn`).
- **Hiệu quả bù trừ vật liệu Velostat:** Sai số trôi (drift) và trễ (hysteresis) sau bù bằng RL giảm $\ge \mathbf{60\%}$ so với tín hiệu thô trên cùng một chu kỳ tải 100 lần.
- **Tính độc lập thời gian thực:** ESP32-S3 duy trì tần số ngắt an toàn $\ge 100\text{ Hz}$ không bị nghẽn bởi truyền thông dữ liệu hai chiều với Orange Pi.

---

## Biểu mẫu log tối thiểu

Mỗi phiên đo phải lưu: ngày giờ, mã phiên, nhiệt độ/độ ẩm phòng, mã firmware (git hash), cấu hình kênh, giá trị R_f, số mẫu trung bình N, tốc độ khung thực đo, tải/ground truth, người thực hiện, file log thô, ghi chú bất thường.

Dùng `research/bench/templates/session_manifest.csv` và `research/bench/templates/reference_check.csv`.

---

## Câu chốt dùng khi báo cáo kết quả GATE

> "Chúng tôi không cho rằng hệ thống đo chính xác chức năng bàn tay. Chúng tôi kiểm tra xem **chỉ số thu được có đủ ổn định và đủ nhạy để theo dõi thay đổi theo thời gian hay không**, và chúng tôi công bố cả những trường hợp nó **không** làm được."
