# ĐỀ CƯƠNG DỰ ÁN DỰ THI KHKT CẤP TRƯỜNG

> **Trạng thái: DỰ THẢO, soạn 2026-10-13 - chưa chốt, chờ chủ dự án duyệt trước khi nộp.**
> File này bám sát đúng 6 mục của "THÔNG BÁO về việc nộp đề cương các dự án đã đăng ký tham gia
> KHKT cấp trường" (ảnh chụp thông báo, nhận 2026-10-13): Tên dự án - Lý do chọn đề tài - Mục tiêu
> nghiên cứu - Ý tưởng và nội dung nghiên cứu - Sản phẩm/kết quả dự kiến - Tính khả thi.
> **Hạn nộp: trước 17h ngày 18/10/2026**, file Word hoặc PDF, qua link sẽ công bố trong nhóm Zalo
> CLB KHKT.
>
> Đây là **bản dùng để nộp đúng khuôn thông báo**, khác với `docs/DE_CUONG_NGAN_5-7_TRANG_DRAFT.md`
> (cấu trúc A-D phỏng theo mẫu lớp 10 của chính chủ dự án, không khớp tiêu đề thông báo này) và
> `docs/DE_CUONG_NOP_TRUONG.md` (bản báo cáo đầy đủ đã nộp 2026-09-26). Nội dung bên dưới tái dùng
> gần như toàn bộ số liệu, định nghĩa và ranh giới an toàn đã có ở hai file đó, chỉ tổ chức lại theo
> đúng 6 mục yêu cầu.
> **Quy ước giữ nguyên:** không có con số nào dưới đây là kết quả đo của đề tài, trừ khi ghi rõ
> "đã làm thật". Mọi ngưỡng GATE là mục tiêu cam kết trước khi đo, không phải kết quả.

| Cần điền (không tự điền) | Giá trị |
|---|---|
| Học sinh 1 | Văn Ngọc Nhật Anh - Lớp 11A2 |
| Học sinh 2 | Nguyễn Duy Quân - Lớp 12A1 |
| Trường / Tỉnh | THPT Quảng Trị, tỉnh Quảng Trị |
| Giáo viên hướng dẫn | Lê Công Long |

---

## 1. Tên dự án

**Tên dự án:** Nghiên cứu và phát triển găng tay hỗ trợ đánh giá, theo dõi và hỗ trợ vận động bàn
tay trong phục hồi chức năng sau đột quỵ.

**Lĩnh vực nghiên cứu:** Hệ thống nhúng (Embedded Systems) - có liên quan kỹ thuật y sinh
(Biomedical Engineering).

---

## 2. Lý do chọn đề tài

Đột quỵ là một trong những nguyên nhân gây tàn tật vận động hàng đầu. Tại Việt Nam, tỉ lệ đang sống
chung với di chứng đột quỵ vào khoảng 1.541/100.000 dân, tỉ lệ mắc mới 222/100.000 dân/năm, và đột
quỵ là nguyên nhân gây 135.999 ca tử vong năm 2019, đứng thứ 4 trong 11 nước láng giềng về tỉ lệ tử
vong do đột quỵ [1]. Theo tổng hợp của Cochrane qua nhiều nghiên cứu, khoảng 80% người bệnh đột quỵ
có tổn thương vận động mặt-tay-chân một bên, và chỉ khoảng một nửa số người liệt hoàn toàn chi trên
lấy lại được chức năng tay hữu ích sau 6 tháng [2].

Phục hồi chức năng bàn tay phụ thuộc chủ yếu vào lượng và chất lượng luyện tập giữa hai lần tái
khám, nhưng chính khoảng thời gian đó lại là một "hộp đen": kỹ thuật viên không biết người bệnh có
tập đúng, tập đủ, và tầm vận động tự làm được đang tăng hay giảm. Cách thay thế hiện nay, nhật ký tự
ghi hoặc đếm số lần cử động bằng thiết bị đeo cổ tay, đã được chứng minh là không đủ tin cậy: độ
thay đổi tối thiểu có ý nghĩa (MDC) của một ứng dụng theo dõi tay đã kiểm định vào khoảng 31% mức
dùng tay trung bình ngày, với 100-200 lần đếm nhầm mỗi giờ [3].

Các công cụ đánh giá lâm sàng hiện có (FMA, ARAT, Box and Block Test) chính xác nhưng chỉ cho "một
ảnh chụp" tại mỗi lần tái khám. Cảm biến gập (flex)/IMU đo trực tiếp góc hoặc tầm vận động, nhưng
tầm vận động bị ảnh hưởng đồng thời bởi yếu cơ và co cứng, không tách được "cố mà không được" khỏi
"co cứng cản lại". Thiết bị hỗ trợ phục hồi tại nhà đã được FDA chấp thuận có giá phổ biến
350-6.000 USD, cao so với khả năng tiếp cận phổ thông.

Chính vì khoảng trống đó, tôi lựa chọn nghiên cứu một thiết bị vừa đo được tín hiệu đáng tin về nỗ
lực vận động của bệnh nhân tại nhà, vừa hỗ trợ lực theo nhu cầu (Assist-as-Needed, AAN) để bệnh nhân
hoàn thành động tác, với ngưỡng kiểm chứng công khai thay vì chỉ dựa vào cảm nhận chủ quan.

---

## 3. Mục tiêu nghiên cứu

Đề tài kiểm chứng theo **hai nhánh song song, ngang hàng** (không chỉ có nhánh đo): nhánh **Đo**
(sensing/đánh giá) và nhánh **Trợ lực - AAN** (Assist-as-Needed), vì cơ cấu AAN là một trong bốn trụ
cột kỹ thuật chính thức của đề tài, không phải tính năng phụ thêm vào phần đo.

**Nhánh Đo:**

| # | Mục tiêu | Cổng kiểm chứng (GATE) |
|---|---|---|
| M1 | Chế tạo sensing element áp trở (Velostat) trên vách khung ngón tay, có độ lặp lại đo được | GATE 0 |
| M2 | Suy luận dấu gập/duỗi của khớp ngón từ mẫu kích hoạt trên vách, không cần encoder/IMU | GATE A |
| M3 | Tái tạo tầm vận động dưới dạng chỉ số tương đối, đối chiếu với chuẩn cơ khí đã biết | GATE B |
| M4 ⭐ (cổng sống còn của nhánh Đo) | Chứng minh hệ thống phát hiện được thay đổi chức năng mô phỏng thật, lớn hơn nhiễu/trôi của chính nó | GATE C |

**Nhánh Trợ lực - AAN:**

| # | Mục tiêu | Cổng kiểm chứng (GATE) |
|---|---|---|
| M5 | Phát hiện được nỗ lực chủ động của người dùng trước khi ngón thực sự di chuyển - nền tảng để trợ lực đúng lúc | GATE AAN-1 |
| M6 ⭐ (cổng sống còn của nhánh Trợ lực) | Chứng minh AAN không chỉ là một lò xo trợ lực cố định: đường cong tải-hoàn thành (RAL) ổn định VÀ mức tham gia chủ động không bị xói mòn về 0 qua các lần thử (không gây ỷ lại) | GATE AAN-2 |

**Cổng Trạm Y Sinh Biên (Orange Pi 5 Pro):**

| # | Mục tiêu | Cổng kiểm chứng (GATE) |
|---|---|---|
| M7 | Trạm biên Orange Pi 5 Pro (RK3588, NPU 6 TOPS) thực thi mô hình RL bù trôi/trễ Velostat và suy luận lực trợ lực AAN thời gian thực ($\le 20\text{ ms}$), kết hợp camera đối chứng góc độc lập | GATE EDGE |

*(Lưu ý về phạm vi kiểm định: Các tiêu chuẩn an toàn thiết bị y sinh và độ tin cậy vận hành dài hạn sẽ do cơ quan thử nghiệm lâm sàng độc lập / phòng kiểm định chuyên môn thực hiện, học sinh không tự cấp chứng nhận kiểm định — theo quyết định DEC-GATE-003).*

**Kết quả dự kiến:** đề tài không đặt mục tiêu "bệnh nhân phục hồi tốt hơn", vì đó là điều một đề
tài học sinh không có cơ sở lâm sàng để khẳng định. Mục tiêu cụ thể và kiểm chứng được là: một thiết
bị nguyên mẫu đo được ba chỉ số (Effort Index, GAP, RAL), một bộ ngưỡng GATE đăng ký trước khi đo cho
cả hai nhánh, và một cơ cấu trợ lực AAN hoạt động trên giàn cơ khí và mô hình tay giả (phantom). Hai
cổng sống còn (⭐) có hệ quả khác nhau khi không đạt: nếu **GATE C** (nhánh Đo) không đạt, **toàn bộ
đề tài dừng lại** vì không còn lý do để đo. Nếu **GATE AAN-2** (nhánh Trợ lực) không đạt, đề tài
**không dừng**, nhưng cơ cấu trợ lực chỉ còn được gọi trung thực là "trợ lực cố định phân bậc", không
được gọi là "theo nhu cầu/thích ứng". Cả hai trường hợp đều sẽ được báo cáo trung thực, kể cả khi là
kết quả âm tính.

---

## 4. Ý tưởng và nội dung nghiên cứu

### 4.1. Ý tưởng chính

Đúng với tên đề tài, thiết bị vừa đo vừa hỗ trợ vận động theo nhu cầu (AAN), không phải chỉ đo đơn
thuần: khung cứng định vị từng lóng ngón, mặt trong vách gắn mảng cảm biến áp trở. Khi ngón ép vào
vách nào, hệ thống ghi nhận lực và suy ra hướng chuyển động, không dùng IMU hay encoder.

**Sơ đồ khối nguyên lý hoạt động:**

```
Bàn tay / phantom -> khung cứng + mảng Velostat trên vách từng lóng ngón
   -> ép vào vách -> điện trở thay đổi -> CD74HC4067 (chọn kênh)
   -> INA333 (khuếch đại đo lường) -> ADS1115/ESP32-S3 (ADC)
   -> xử lý tại biên (Orange Pi 5 Pro, RK3588): bù đồng pha, suy hướng gập/duỗi
      (nhiệm vụ suy luận cụ thể của phần biên đang được xác định - xem GATE EDGE, mục 3)
   -> 3 chỉ số: Effort Index (EI) · GAP = PROM - AROM · RAL (mức trợ giúp cần)
   -> cờ "dữ liệu không đáng tin" khi mất điều kiện hợp lệ
   -> dashboard theo tuần cho kỹ thuật viên
```

Ba chỉ số định lượng tách phần bệnh nhân "tự làm" khỏi phần "được trợ giúp":

- **EI (Effort Index):** tỉ lệ tín hiệu lực khi ngón cố mà chưa dịch chuyển so với lúc nghỉ, không
  thứ nguyên (0-1), không phải newton hay %MVC.
- **GAP = PROM - AROM:** tầm vận động thụ động (do kỹ thuật viên/rig kéo) trừ tầm vận động chủ động
  (tự bệnh nhân làm được), đo trong cùng một phiên. Do PROM luôn lớn hơn hoặc bằng AROM, GAP luôn
  lớn hơn hoặc bằng 0; GAP tiến về 0 nghĩa là phần "được làm hộ" đang co lại, đúng hướng kỹ thuật
  viên muốn thấy trong một tuần tập.
- **RAL (Required Assistance Level):** mức tải trợ giúp tối thiểu (đo bằng lực kế lò xo trên rig) để
  người bệnh hoàn thành được phần lớn số lần thử, là chỉ số cơ khí tự chế tạo và tự kiểm chứng được.

Song song, một cơ cấu trợ lực theo nhu cầu (AAN): lò xo trợ giúp thụ động chia nấc kết hợp một động
cơ servo, tạo lực bù `F_assist = max(0, F_mục tiêu - F_đo được trên phantom)`, giới hạn lực tối đa
5 N và độ trễ đáp ứng khoảng 1,2 giây. **Ranh giới an toàn phải nói rõ:** cơ cấu này hiện chỉ kiểm
chứng trên giàn cơ khí và mô hình tay giả silicone (phantom), không bao giờ tác động lực lên ngón
tay người thật ở giai đoạn này, kể cả tình nguyện viên khỏe mạnh (chỉ đánh giá độ vừa vặn khi đeo
thử, không tải). Việc mở rộng sang người thật chờ phê duyệt đạo đức theo quy định cuộc thi.

Cơ sở lựa chọn bàn tay làm đối tượng dựa trên bản đồ vỏ não vận động/cảm giác cổ điển (diện tích vỏ
não dành cho bàn tay lớn hơn nhiều lần so với tỉ lệ diện tích bề mặt cơ thể) [4][5], và nguyên lý
Hebbian về việc tín hiệu vận động và phản hồi cảm giác cần xảy ra gần như đồng thời để củng cố kết
nối thần kinh [6]. Đây là kiến thức nền giải thích lý do chọn biến số và đối tượng nghiên cứu, không
phải điều đề tài tự đo hay chứng minh: đề tài không có EEG/fNIRS/TMS/fMRI, không đo hoạt động điện
não, và không được phép nói các câu như "thiết bị tái tổ chức vỏ não".

**Đã thực hiện thật, không phải chỉ là ý tưởng trên giấy:** đã tự thiết kế, xuất file CAD và in thử
thực tế trên máy in 3D lần lượt 9 phương án cơ cấu khóa/mở nẹp ngón tay (Mech 1 đến Mech 9), loại
dần theo nhược điểm quan sát trên vật in thật. Phương án hiện tại tốt nhất, Mech 9 (khóa ngàm xoay
hai bản lề), đóng/mở hoàn toàn bằng khớp xoay thay vì bẻ cong nhựa. Đã lắp thử breadboard chuỗi
ESP32-S3 + ADS1115 + INA333 + CD74HC4067, sửa một lỗi cắt tín hiệu (clipping) của INA333 ở chế độ
đơn nguồn. Cả hai phần này là bước dọn đường kỹ thuật, chưa phải số liệu GATE 0 chính thức.

### 4.2. Điểm mới hoặc tính sáng tạo

Một số găng tay cảm biến/găng trợ lực đã công bố trong và ngoài nước dùng khung cứng kết hợp encoder
để đo góc, hoặc dùng EMG để suy ý định vận động; nhưng EMG kém ổn định ở nhóm bệnh nhân đột quỵ do
đồng co cơ bất thường, còn hướng tiếp cận dùng vách cứng + áp trở để suy hướng lực đã có tiền lệ ở
quy mô cảm biến xúc giác đơn lẻ, chưa thấy ở quy mô mảng trên khung ngón kết hợp khung thống kê
MDC/ICC cho theo dõi tại nhà.

Đóng góp của đề tài không nằm ở một nguyên lý vật lý mới, mà ở cách tổ hợp bốn thành phần đã có sẵn
thành một hệ vừa đo vừa hỗ trợ, tự kiểm chứng được: (1) khung cứng định hướng lực trên vách từng
lóng ngón để phân biệt nỗ lực chủ động với co cứng ngay trong một phiên đo; (2) ba chỉ số định lượng
(Effort Index, GAP, RAL) định nghĩa tường minh trên rig có tải đã biết; (3) cờ độ tin cậy theo từng
phiên, được kiểm chứng bằng lỗi tiêm có chủ đích (fault injection), tức là cố ý làm hỏng một phần tín
hiệu để xem cờ cảnh báo có hoạt động thật hay chỉ là trang trí; (4) cơ cấu trợ lực theo nhu cầu (AAN)
bù đúng phần lực còn thiếu để bệnh nhân hoàn thành động tác. Khung kiểm chứng công khai (ngưỡng GATE
chốt trước khi đo, không đổi sau khi thấy số) cũng là một điểm khác biệt so với các báo cáo thương
mại không công bố ngưỡng pass/fail.

---

## 5. Sản phẩm/kết quả dự kiến

| Sản phẩm | Mô tả | Tiêu chí hoàn thành |
|---|---|---|
| Nguyên mẫu găng | Khung ngón có vách cứng, mảng cảm biến áp trở Velostat, mạch đo ESP32-S3/ADS1115/INA333/CD74HC4067 | Ảnh thiết bị đang chạy và tín hiệu thật trên màn hình |
| Cơ cấu AAN | Lò xo trợ giúp chia nấc + servo, hoạt động trên giàn cơ khí và phantom | Lực bù đo được bằng lực kế, giới hạn an toàn xác nhận |
| Ba chỉ số định lượng | Effort Index, GAP, RAL, định nghĩa tường minh kèm đơn vị | Có công thức, có dữ liệu minh họa trên rig |
| Bộ giao thức và ngưỡng GATE | 10 mục GATE 0, các GATE A/B/C (nhánh Đo), GATE AAN-1/AAN-2/AAN-3 (nhánh Trợ lực), GATE D/E dùng chung | Ngưỡng được chốt trước khi đo, có ngày ghi |
| Cơ cấu đeo/tháo một tay | Khóa ngàm xoay hai bản lề (Mech 9), đã qua 8 phương án loại bỏ trước đó | Mẫu in 3D vận hành được bằng một tay |
| Báo cáo/poster | Trình bày kết quả đạt và không đạt theo từng GATE | Mỗi GATE có một ô kết quả, kể cả khi fail |

**Khả năng ứng dụng thực tiễn:** nếu các cổng GATE được thông qua, thiết bị có thể dùng làm công cụ
theo dõi tần suất và chất lượng tập luyện tại nhà giữa hai lần tái khám, bổ sung cho các thang đo
lâm sàng hiện có (không thay thế FMA/ARAT), với chi phí vật tư thấp hơn nhiều so với thiết bị thương
mại 350-6.000 USD. Việc mở rộng sang thử nghiệm trên người bệnh thật cần có phê duyệt đạo đức và nằm
ngoài phạm vi giai đoạn hiện tại.

---

## 6. Tính khả thi

**Năng lực và vật tư đã có:** firmware nhúng cơ bản đã tồn tại và chạy thử (ESP32-S3 + ADS1115 +
INA333 + CD74HC4067 trên breadboard), board Orange Pi 5 Pro đã có sẵn, 9 phương án cơ cấu khóa ngón
đã in thử thực tế, quy trình ghi chép và tra cứu nguồn đã vận hành.

**Kinh phí dự kiến:** phần lớn vật tư GATE 0 (Velostat, đồng lá tự dính, board ESP32-S3) đã có sẵn.
Tiền mặt cần chi thêm để hoàn tất GATE 0 ước tính khoảng 0,1-0,65 triệu đồng (tấm acrylic làm jig,
khối lượng chuẩn, dây nối). Đi hết toàn bộ chuỗi GATE với vật tư đã có sẵn ước tính khoảng 1,8-4,7
triệu đồng; nếu phải mua toàn bộ linh kiện từ đầu, ước tính khoảng 6,5-12 triệu đồng. Đây là dự toán
tham khảo tại thời điểm viết, chưa phải báo giá.

**Kế hoạch thời gian và một điểm cần nói rõ trước:** theo kế hoạch kỹ thuật đã lập (xem
`research/protocols/08_gate0_execution_plan.md`), riêng GATE 0 cần khoảng 3 tuần lịch (bao gồm 10
ngày log trôi liên tục bắt buộc), và GATE C (cổng sống còn của nhánh Đo) cần tối thiểu 28 ngày theo
dõi trôi theo đúng giao thức đã đăng ký. Với mốc thi dự kiến cuối tháng 11/2026, đề tài **không hứa**
hoàn tất toàn bộ chuỗi GATE của cả hai nhánh trước thời điểm đó. Mục tiêu khả thi trong khung thời
gian này là hoàn tất GATE 0 và tiến hành một phần GATE A/B (nhánh Đo), đồng thời hoàn thiện cơ cấu cơ
khí Mech 9; nhánh Trợ lực (GATE AAN-1/AAN-2/AAN-3) và việc chốt nhiệm vụ cho Orange Pi 5 Pro (GATE
EDGE) dự kiến triển khai sau vòng trường. Báo cáo nộp vòng trường sẽ trình bày trung thực những gì đã
đạt, những gì đang chạy (ví dụ log trôi 28 ngày của GATE C
có thể đang trong quá trình thực hiện), và kế hoạch tiếp tục sau vòng trường. Đây là lựa chọn có chủ
đích để không báo cáo một kết quả chưa có thật, nhất quán với quy ước "không tô hồng" đã áp dụng
xuyên suốt đề tài.

---

## TÀI LIỆU THAM KHẢO

[1] Tran M.C. và cộng sự (2025), "Comprehensive analysis of stroke epidemiology in Vietnam", *Global
Epidemiology*, 9:100199, DOI: 10.1016/j.gloepi.2025.100199.
[2] Pollock A. và cộng sự (2014), "Interventions for improving upper limb function after stroke",
*Cochrane Database Syst. Rev.*, 2014(11):CD010820, DOI: 10.1002/14651858.CD010820.pub2.
[3] Nghiên cứu MDC ứng dụng theo dõi chức năng tay (Manumeter), *Sensors* 2022, 22(18):6938.
[4] Penfield W., Boldrey E. (1937), "Somatic motor and sensory representation in the cerebral
cortex of man", *Brain*, 60:389-440.
[5] Gordon E.M. và cộng sự (2023), "A somato-cognitive action network...", *Nature*, 617:351-359,
DOI: 10.1038/s41586-023-05964-2.
[6] Hebb D.O. (1949), *The Organization of Behavior*, New York: Wiley, kiến thức nền, không phải
kết quả đo của đề tài.

*Mức độ đã đọc (toàn văn/tóm tắt) của từng nguồn được lưu đầy đủ trong hồ sơ nội bộ của dự án, sẵn
sàng đối chiếu khi hội đồng yêu cầu.*
