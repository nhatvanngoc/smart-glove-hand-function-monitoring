# ĐỀ CƯƠNG NGHIÊN CỨU KHOA HỌC KỸ THUẬT (BẢN NGẮN — NỘP TRƯỜNG)

> **Trạng thái: DỰ THẢO, đề xuất 2026-10-12 — chưa chốt, chờ chủ dự án duyệt.** Mục đích file này là
> một bản đề cương **thật ngắn (5–7 trang)** đúng khuôn khổ phiếu đăng ký đề tài cấp trường, khác với
> báo cáo khoa học toàn văn (15–16 trang, `de_cuong/DE_CUONG_NGHIEN_CUU.pdf`) và bản nộp trước đó
> (`docs/DE_CUONG_NOP_TRUONG.md`, đã nộp 2026-09-26, cũng dài ở mức báo cáo). Cấu trúc và văn phong mô
> phỏng theo đề cương găng tay nông nghiệp lớp 10 của chính chủ dự án (`LV1-10-10A2.pdf`): bốn phần
> A–D ngắn gọn, nhiều gạch đầu dòng, ít công thức, số liệu luôn kèm nguồn.
> **Quy ước:** không có con số nào dưới đây là kết quả đo của đề tài, trừ khi ghi rõ "đã làm thật".
> Mọi ngưỡng GATE là **mục tiêu cam kết trước khi đo**, không phải kết quả.

| Cần điền (không tự điền) | Giá trị |
|---|---|
| Họ và tên học sinh | *⟨điền⟩* |
| Lớp / Trường / Tỉnh | *⟨điền⟩* |
| Giáo viên hướng dẫn | *⟨điền⟩* |
| Lĩnh vực dự thi | *⟨điền — khuyến nghị: Hệ thống nhúng⟩* |

---

## A. VẤN ĐỀ NGHIÊN CỨU

### 1. Lý do chọn đề tài

Đột quỵ là một trong những nguyên nhân gây tàn tật vận động hàng đầu. Tại Việt Nam, tỉ lệ đang
sống chung với di chứng đột quỵ vào khoảng **1.541/100.000 dân**, tỉ lệ mắc mới **222/100.000
dân/năm**, và đột quỵ là nguyên nhân gây **135.999 ca tử vong** năm 2019 — đứng thứ 4 trong 11 nước
láng giềng về tỉ lệ tử vong do đột quỵ [1]. Theo tổng hợp của Cochrane qua nhiều nghiên cứu, khoảng
**80%** người bệnh đột quỵ có tổn thương vận động mặt–tay–chân một bên, và **chỉ khoảng một nửa** số
người liệt hoàn toàn chi trên lấy lại được chức năng tay hữu ích sau 6 tháng [2].

Phục hồi chức năng bàn tay phụ thuộc chủ yếu vào **lượng và chất lượng luyện tập giữa hai lần tái
khám** — nhưng chính khoảng thời gian đó lại là một **"hộp đen"**: kỹ thuật viên không biết người bệnh
có tập đúng, tập đủ, và tầm vận động **tự làm được** đang tăng hay giảm. Cách thay thế hiện nay —
nhật ký tự ghi hoặc đếm số lần cử động bằng thiết bị đeo cổ tay — đã được chứng minh là **không đủ
tin cậy**: độ thay đổi tối thiểu có ý nghĩa (MDC) của một ứng dụng theo dõi tay đã kiểm định vào
khoảng **31%** mức dùng tay trung bình ngày, với **100–200 lần đếm nhầm mỗi giờ** [3].

Chính vì khoảng trống đó, tôi lựa chọn nghiên cứu đề tài **"Nghiên cứu và phát triển găng tay hỗ trợ
đánh giá, theo dõi và hỗ trợ vận động bàn tay trong phục hồi chức năng sau đột quỵ"**.

### 2. Xác định vấn đề nghiên cứu

- Nghiên cứu một cấu hình cảm biến áp trở gắn trên **vách cứng** của khung ngón tay để ghi nhận
  **lực ép có hướng**, thay vì đo trực tiếp góc gập bằng cảm biến gập (flex) hay IMU.
- Nghiên cứu cách tách phần **"người bệnh tự làm"** khỏi phần **"được trợ giúp"** trong cùng một
  động tác, bằng ba chỉ số định lượng (Effort Index, GAP, RAL — xem mục B.IV).
- Nghiên cứu cơ chế **trợ lực theo nhu cầu (Assist-as-Needed, AAN)** chỉ chạy trên rig cơ khí và mô
  hình tay giả (phantom), không bao giờ tác động lực lên ngón tay người thật ở giai đoạn này.
- Nghiên cứu cơ cấu cơ khí để bệnh nhân (có thể yếu/run tay) tự **đeo và tháo** nẹp ngón bằng một
  tay (xem mục C.1 — benchmark 9 phương án).

### 3. Mục tiêu nghiên cứu

| # | Mục tiêu | Cổng kiểm chứng (GATE) |
|---|---|---|
| M1 | Chế tạo sensing element áp trở (Velostat) trên vách khung, có độ lặp lại đo được | GATE 0 |
| M2 | Suy luận **dấu** gập/duỗi của khớp ngón từ mẫu kích hoạt trên vách, không cần encoder/IMU | GATE A |
| M3 | Tái tạo tầm vận động dưới dạng **chỉ số tương đối**, đối chiếu với chuẩn cơ khí đã biết | GATE B |
| M4 ⭐ | Chứng minh hệ thống phát hiện được **thay đổi chức năng mô phỏng thật**, lớn hơn nhiễu/trôi của chính nó | GATE C — nếu fail thì dừng, không viết tiếp như đã thành công |
| M5 | Tự gắn cờ phiên đo "không đáng tin" khi dữ liệu không đạt điều kiện | GATE D/E |
| M6 | Chạy được mô hình nhận dạng rút gọn (lượng tử hóa INT8) tại biên, không phụ thuộc mạng | GATE F |

### 4. Tiêu chí của dự án (cam kết trước khi đo, không đổi sau khi thấy số)

- Tồn tại một mức tiền tải sao cho tín hiệu **vừa đủ nhạy** (tỉ số tín hiệu/nhiễu ≥ 8 bước lượng tử
  hóa tại một thay đổi lực chuẩn 1 N) **vừa đủ ổn định** (hệ số biến thiên giữa các chu kỳ ≤ 5%).
- Độ trễ đường lên so với đường xuống (hysteresis) ≤ 15%; độ lún khi giữ tải (creep) ≤ 3%.
- Độ lặp lại giữa các ngày đo (ICC, đo 3 ngày) ≥ 0,75; tốc độ lấy mẫu thực tế ≥ 20 Hz trên tối thiểu
  12 kênh.
- **GATE sống còn:** độ lớn thay đổi tín hiệu khi cố ý thay đổi mức chức năng mô phỏng phải **lớn
  hơn có ý nghĩa thống kê** so với biến thiên trôi/nhiễu của chính hệ đo trong cùng khung thời gian.
- Không có bước nào quy đổi trực tiếp "ADC → newton" hay "ADC → độ góc" — mọi chỉ số xuất ra đều
  không thứ nguyên hoặc ở đơn vị riêng của nó (xem bảng B.IV).

*(Bộ ngưỡng đầy đủ — 10 mục GATE 0 — xem `research/protocols/06_glove_hand_GATE_experiment.md` và
`research/protocols/08_gate0_execution_plan.md`; một số ô "chốt?" của GATE 0 vẫn đang chờ chủ dự án
xác nhận cuối cùng trước khi bật nguồn đo chính thức.)*

### 5. Đối tượng và phạm vi nghiên cứu

- **Đối tượng đo:** tín hiệu lực–hướng tại các vách khung lóng ngón tay, thu trên **mô hình tay giả
  (phantom) và rig cơ khí có tải đã hiệu chuẩn**. **Không** đo trên bệnh nhân thật ở giai đoạn này —
  mọi phép đo trên người (kể cả tình nguyện viên khỏe mạnh, không tải) chỉ thực hiện **sau khi** có
  phê duyệt đạo đức theo quy định cuộc thi.
- **Lịch sử đề tài:** công cụ đánh giá lâm sàng hiện có (FMA, ARAT, Box and Block Test, lực kế cầm
  tay) cho một "ảnh chụp" tại cơ sở y tế, không theo dõi được tại nhà; một số găng tay cảm biến/găng
  trợ lực đã công bố trong và ngoài nước nhưng chưa thấy tổ hợp đủ: lực có hướng qua vách khung +
  khung thống kê MDC/ICC cho theo dõi tiến triển + tự gắn cờ độ tin cậy — xem mục B.II.
- **Giải pháp kỹ thuật:** vật liệu áp trở Velostat, khung ngón in 3D (PLA/TPU), mạch chọn kênh
  CD74HC4067, vi điều khiển ESP32-S3, khuếch đại đo lường INA333 + ADC ADS1115, rig cơ khí AAN (lò
  xo trợ giúp + 1 servo), xử lý tại biên trên NPU (RK3588).

### 6. Địa điểm nghiên cứu và thực nghiệm

- Tại trường (phòng thực hành) và tại nhà: lắp ráp, lập trình, thử nghiệm trên rig/phantom.
- Không cần địa điểm y tế ở giai đoạn này vì chưa đo trên người bệnh.

### 7. Phương pháp nghiên cứu

- Phương pháp **thực nghiệm trên bench**: đo đặc tính vật liệu (điện trở theo áp suất, trễ, từ
  biến, trôi theo ngày) bằng khối lượng đã cân làm lực chuẩn.
- Phương pháp **thống kê**: ICC, SEM, MDC (độ thay đổi tối thiểu có ý nghĩa) cho mọi chỉ số; so sánh
  **trong cùng một người theo thời gian**, không so giữa người với người.
- Phương pháp **tiêm lỗi có chủ đích** (fault injection) trên rig để kiểm chứng cờ độ tin cậy có
  hoạt động thật hay chỉ là trang trí.
- Tham khảo ý kiến chuyên gia vật lý trị liệu–phục hồi chức năng về tính cấp thiết và giao thức đo
  (ý kiến chuyên gia là bằng chứng về **nhu cầu**, không phải bằng chứng về **kết quả**).

---

## B. GIẢI PHÁP VÀ THIẾT KẾ

### I. Tổng quan đề tài

Thiết bị là một **găng tay đo, không phải găng tay tập**: khung cứng định vị từng lóng ngón, mặt
trong vách gắn mảng cảm biến áp trở. Khi ngón ép vào vách nào, hệ thống ghi nhận lực và suy ra
**hướng** chuyển động — không dùng IMU hay encoder. Từ chuỗi tín hiệu đó, đề tài trích ba chỉ số
(Effort Index, GAP, RAL) để tách phần bệnh nhân **tự làm** khỏi phần **được trợ giúp**, kèm cờ cảnh
báo khi một phiên đo không đủ tin cậy. Một cơ cấu trợ lực theo nhu cầu (AAN) chạy trên rig + phantom
mô phỏng phần "hỗ trợ vận động" ở mức đo được, không tác động lên người.

### II. Bất cập và giới hạn của giải pháp hiện tại và giải pháp của đề tài

**2.1. Bất cập và giới hạn của các giải pháp hiện tại**

- Thang đo lâm sàng chuẩn (FMA, ARAT, Box and Block Test) chính xác nhưng chỉ cho **một ảnh chụp**
  tại mỗi lần tái khám, cần người đánh giá có chuyên môn.
- Cảm biến gập (flex)/IMU đo trực tiếp **góc hoặc tầm vận động**, nhưng tầm vận động bị ảnh hưởng
  đồng thời bởi yếu cơ và co cứng — không tách được "cố mà không được" khỏi "co cứng cản lại".
- Một số găng cảm biến/găng trợ lực đã công bố (trong và ngoài nước) dùng khung cứng + da áp trở để
  đo góc bằng encoder, hoặc dùng EMG để suy ý định vận động — nhưng EMG kém ổn định ở nhóm bệnh nhân
  đột quỵ do đồng co cơ bất thường, còn hướng tiếp cận dùng vách cứng + áp trở để suy **hướng** đã có
  tiền lệ ở quy mô cảm biến xúc giác đơn lẻ, chưa thấy ở quy mô mảng trên khung ngón kết hợp khung
  thống kê MDC/ICC cho theo dõi tại nhà.
- Thiết bị PHCN tại nhà đã được FDA chấp thuận có giá phổ biến **350–6.000 USD**, cao so với khả năng
  tiếp cận phổ thông.

**2.2. Giải pháp của đề tài**

Từ những giới hạn đó, đề tài ghép ba thành phần đã có sẵn thành một phép đo **tự kiểm chứng được**:
(1) khung cứng định hướng lực trên vách từng lóng ngón để phân biệt nỗ lực chủ động với co cứng ngay
trong một phiên đo; (2) ba chỉ số định lượng (Effort Index, GAP, RAL) định nghĩa tường minh trên rig
có tải đã biết; (3) cờ độ tin cậy theo từng phiên, được kiểm chứng bằng lỗi tiêm có chủ đích. Đóng
góp không nằm ở một nguyên lý vật lý mới, mà ở cách tổ hợp và ở khung kiểm chứng công khai đi kèm.

### III. Cơ sở lý thuyết

**3.1. Vì sao chọn bàn tay làm đối tượng — bản đồ vỏ não vận động/cảm giác**

Theo bản đồ vỏ não vận động và cảm giác cổ điển (*motor/sensory homunculus*, dựng từ dữ liệu kích
thích điện trực tiếp trên 126 bệnh nhân phẫu thuật thần kinh) [4], **diện tích vỏ não dành cho bàn
tay và các ngón tay lớn hơn nhiều lần so với tỉ lệ diện tích bề mặt cơ thể thực tế** — phản ánh mức
độ điều khiển vận động tinh vi cần thiết cho thao tác cầm nắm khéo léo. Một nghiên cứu fMRI hiện đại
hơn [5] đã tinh chỉnh mô hình này (các vùng hiệu ứng tay/chân/miệng xen kẽ với một mạng lưới hành
động–nhận thức cơ thể) nhưng không thay đổi kết luận cốt lõi: bàn tay chiếm diện tích biểu diễn vỏ
não không cân xứng so với kích thước vật lý của nó. **Đây là lý do sinh lý thần kinh để chọn bàn tay
làm đối tượng — không phải điều đề tài tự đo hay chứng minh** (đề tài không có EEG/fNIRS/TMS/fMRI).

**3.2. Nguyên lý Hebbian và vì sao phản hồi cần đến gần như đồng thời**

Phục hồi sau đột quỵ dựa trên **tính mềm dẻo thần kinh**, được thúc đẩy bởi luyện tập lặp lại, có
mục đích, đủ cường độ. Một nguyên lý nền tảng lâu đời của khoa học thần kinh — nguyên lý Hebbian [6]
— mô tả rằng các kết nối thần kinh được củng cố khi tín hiệu vận động (lệnh) và tín hiệu cảm giác
phản hồi (kết quả) xảy ra gần như đồng thời. Đây là lý do lý thuyết cho việc một hệ thống theo dõi
cần ghi nhận được **nỗ lực** ngay khi nó xảy ra — kể cả khi ngón tay **chưa** dịch chuyển được — thay
vì chỉ ghi nhận động tác đã hoàn thành. Nếu không, những lần bệnh nhân cố nhiều nhưng chưa làm được
sẽ bị hệ thống ghi nhận như "không tập gì", trong khi y văn mô tả đây chính là cơ chế dẫn tới hiện
tượng "bất hoạt do học được" (*learned non-use*) nếu lặp lại kéo dài [6].

> **Ranh giới bắt buộc nêu rõ:** nguyên lý Hebbian và bản đồ vỏ não ở trên là **kiến thức nền giải
> thích lý do chọn biến số và đối tượng nghiên cứu**. Đề tài **không** đo hoạt động điện não, **không**
> có nhóm chứng lâm sàng, và do đó **không** được phép nói các câu như "thiết bị tái tổ chức vỏ não"
> hay "chứng minh tăng tính mềm dẻo thần kinh".

**3.3. Ba chế độ tập và hiện tượng ỷ lại**

Luyện tập phục hồi có ba chế độ: **thụ động** (ngoại lực/rig tạo chuyển động, đo được tầm vận động
thụ động PROM), **chủ động có trợ lực — AAN** (người bệnh tự phát lực, thiết bị chỉ bù phần còn
thiếu, đo được tầm vận động chủ động AROM và mức trợ giúp cần), và **chủ động kháng lực** (ngoài
phạm vi đề tài). Hai chế độ đầu khác nhau ở **bao nhiêu phần động tác do người bệnh tự tạo ra**,
không khác ở có hay không có chuyển động — đây là lý do đề tài tách AROM và PROM thành chỉ số GAP
(mục B.IV). Y văn cũng ghi nhận hiện tượng "ỷ lại" (*motor slacking*): người bệnh học được rằng
thiết bị sẽ lo phần còn lại nên giảm nỗ lực — vì vậy biến số cần theo dõi là **tỉ lệ tham gia**, chứ
không chỉ độ chính xác bám quỹ đạo [6].

### IV. Nguyên lý và cơ chế hoạt động của hệ thống

**4.1. Sơ đồ khối**

```
Bàn tay / phantom → khung cứng + mảng Velostat trên vách từng lóng ngón
   → ép vào vách → điện trở thay đổi → CD74HC4067 (chọn kênh)
   → INA333 (khuếch đại đo lường) → ADS1115/ESP32-S3 (ADC)
   → xử lý tại biên (RK3588, INT8): bù đồng pha, suy hướng gập/duỗi
   → 3 chỉ số: Effort Index (EI) · GAP = AROM − PROM · RAL (mức trợ giúp cần)
   → cờ "dữ liệu không đáng tin" khi mất điều kiện hợp lệ
   → dashboard theo tuần cho kỹ thuật viên
```

- **EI (Effort Index):** tỉ lệ tín hiệu lực khi ngón "cố mà chưa dịch chuyển" so với lúc nghỉ —
  không thứ nguyên (0–1), **không phải** newton hay %MVC.
- **GAP = AROM − PROM:** chênh lệch tầm vận động chủ động trừ thụ động, đo trong cùng một phiên;
  GAP tiến về 0 nghĩa là phần "được làm hộ" đang co lại.
- **RAL (Required Assistance Level):** mức tải trợ giúp tối thiểu (đo bằng lực kế lò xo trên rig) để
  người bệnh hoàn thành được phần lớn số lần thử — là chỉ số cơ khí, tự chế tạo và tự kiểm chứng
  được, không cần cảm biến y tế chuẩn.

**4.2. Cơ chế trợ lực theo nhu cầu (AAN) — trụ cột kỹ thuật thứ 4**

Một lò xo trợ giúp thụ động chia nấc, kết hợp một động cơ servo qua khớp truyền lực, tạo lực bù
`F_assist = max(0, F_mục tiêu − F_đo được trên phantom)`, giới hạn lực tối đa 5 N và độ trễ đáp ứng
khoảng 1,2 giây. **Ranh giới an toàn giữ nguyên tuyệt đối:** cơ cấu này chỉ chạy trên **rig cơ khí và
mô hình tay giả silicone (phantom)**; **không bao giờ** tác động lực lên ngón tay người thật, kể cả
tình nguyện viên khỏe mạnh (chỉ được đánh giá độ vừa vặn khi đeo thử, không tải).

---

## C. CHẾ TẠO MÔ HÌNH VÀ KẾ HOẠCH THỬ NGHIỆM

### 1. Đã thực hiện thật: benchmark 9 cơ cấu đóng/mở nẹp ngón tay

Trước khi đo tín hiệu cảm biến, đề tài phải giải quyết một bài toán cơ khí riêng: cơ cấu nào cho
phép bệnh nhân (có thể yếu/run tay) **tự đeo và tháo** vỏ nẹp quanh một lóng ngón bằng một tay, đồng
thời giữ đủ chặt để cảm biến Velostat tiếp xúc ổn định. Tôi đã tự thiết kế, xuất file CAD và **in
thử thực tế trên máy in 3D** lần lượt 9 phương án (Mech 1 → Mech 9) rồi loại dần theo nhược điểm quan
sát trên vật in thật: lực kẹp yếu/nhựa giãn, khó trượt khi ngón co cứng, dây đai bai dão không cố
định cứng cảm biến, chi tiết rời dễ rơi với người run tay, xung đột vị trí với dây cáp gân, hoặc mỏi
nhựa khi phải bẻ cong lặp lại để mở. Phương án hiện tại tốt nhất — **Mech 9 (khóa ngàm xoay hai bản
lề)** — đóng/mở hoàn toàn bằng khớp xoay thay vì bẻ cong nhựa, kỳ vọng bền hơn về chu kỳ sử dụng.
**Lưu ý trung thực:** file CAD của Mech 9 **chưa** có trong hồ sơ dự án, **chưa** được in thử thực
tế, và **chưa** có số liệu độ bền theo chu kỳ đóng/mở — đây là kỳ vọng thiết kế, không phải kết quả
đo. Quan hệ giữa cơ cấu này và bản lề liên-đốt của khung ngón đầy đủ cũng chưa được xác nhận.

### 2. Đã thực hiện thật: bring-up phần cứng sơ bộ

Đã lắp thử trên breadboard chuỗi ESP32-S3 + ADS1115 + INA333 + CD74HC4067, sửa một lỗi cắt tín hiệu
(clipping) của INA333 ở chế độ đơn nguồn và kiểm tra khả năng cách ly giữa các kênh bằng
oscilloscope. **Dữ liệu này chưa đạt chuẩn GATE 0 chính thức** (chưa có đủ nhật ký phiên đo theo đúng
quy trình đã đăng ký) — đây là bước dọn đường kỹ thuật, không phải kết quả GATE 0.

### 3. Kế hoạch tiếp theo

| Giai đoạn | Nội dung | Điều kiện |
|---|---|---|
| P1 | GATE 0: đặc tính điện trở theo áp suất, chọn điện trở tải | có sensing element ổn định |
| P2 | GATE A/B: suy luận hướng + tầm vận động chỉ số | sau P1 đạt |
| P3 | GATE C ⭐ (sống còn) trên rig + phantom | sau P2 đạt |
| P4 | GATE D/E/F: cờ tin cậy + mô hình INT8 tại biên | sau P3 đạt |
| P5 | Viết báo cáo, số liệu, poster | song song P4 |

---

## D. KẾT LUẬN VÀ KIẾN NGHỊ

### I. Đánh giá hiện trạng

Đến thời điểm này, đề tài đã hoàn tất: cơ sở lý thuyết, kiến trúc hệ thống, khung chỉ số (EI/GAP/
RAL) với ngưỡng GATE đăng ký trước khi đo, benchmark cơ khí thật (9 cơ cấu khóa ngón, đã in thử) và
bring-up phần cứng sơ bộ. **Chưa có** số liệu GATE 0 chính thức, chưa đo trên phantom, và CAD của cơ
cấu khóa ngón mới nhất (Mech 9) chưa hoàn tất. Đây là giai đoạn thiết kế và chuẩn bị, không phải giai
đoạn có kết quả đo.

### II. Kết luận

Đề tài không cam kết "bệnh nhân phục hồi tốt hơn" — đó là điều một đề tài học sinh không có cơ sở để
khẳng định. Đề tài cam kết một điều nhỏ hơn nhưng kiểm chứng được: **đo một tín hiệu đáng tin về nỗ
lực và mức trợ giúp cần thiết, với ngưỡng pass/fail công khai và chốt trước khi đo**. Nếu cổng sống
còn (GATE C) không đạt, đề tài sẽ dừng và báo cáo trung thực đó là một kết quả âm tính có giá trị,
không tô hồng.

### III. Hướng phát triển

- Hoàn tất và in thử Mech 9, đo độ bền chu kỳ đóng/mở thực tế.
- Chạy đủ chuỗi GATE 0 → GATE F theo đúng quy trình đã đăng ký.
- Nếu các cổng đều đạt: đề xuất pilot trên người bệnh thật với bệnh viện đối tác và phê duyệt đạo
  đức — việc nằm ngoài phạm vi một đề tài học sinh ở giai đoạn hiện tại.

### IV. Kiến nghị

Xin được tư vấn chuyên môn về giao thức đo lâm sàng, phê duyệt đạo đức khi mở rộng sang người tham
gia, và hỗ trợ vật tư cho giai đoạn hiệu chuẩn (Velostat, linh kiện đo lường, vật liệu in 3D).

---

## TÀI LIỆU THAM KHẢO

[1] Tran M.C. và cộng sự (2025), "Comprehensive analysis of stroke epidemiology in Vietnam", *Global
Epidemiology*, 9:100199, DOI: 10.1016/j.gloepi.2025.100199.
[2] Pollock A. và cộng sự (2014), "Interventions for improving upper limb function after stroke",
*Cochrane Database Syst. Rev.*, 2014(11):CD010820, DOI: 10.1002/14651858.CD010820.pub2.
[3] Nghiên cứu MDC ứng dụng theo dõi chức năng tay (Manumeter), *Sensors* 2022, 22(18):6938.
[4] Penfield W., Boldrey E. (1937), "Somatic motor and sensory representation in the cerebral
cortex of man", *Brain*, 60:389–443.
[5] Gordon E.M. và cộng sự (2023), "A somato-cognitive action network…", *Nature*, 617:351–359,
DOI: 10.1038/s41586-023-05964-2.
[6] Hebb D.O. (1949), *The Organization of Behavior*, New York: Wiley — kiến thức nền, không phải
kết quả đo của đề tài.
[7] Hopkins M. và cộng sự (2020), đặc tính vật liệu Velostat (trễ/từ biến/trôi, sai số 16–48%),
*IEEE Sensors Journal*.
[8] Phần tử xúc giác vách đàn hồi phân biệt hướng lực, *Sensors* 2015, 15(10):25463.
[9] Jiang S. và cộng sự (2017), so sánh FSR/áp trở với sEMG cho phát hiện cử chỉ.

*Mức độ đã đọc (toàn văn/tóm tắt) của từng nguồn được lưu đầy đủ trong hồ sơ nội bộ của dự án, sẵn
sàng đối chiếu khi hội đồng yêu cầu.*
