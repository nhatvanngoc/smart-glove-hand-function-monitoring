# ĐỀ CƯƠNG NGHIÊN CỨU KHOA HỌC
## Găng tay thông minh đánh giá và theo dõi chức năng vận động bàn tay trong phục hồi chức năng sau đột quỵ

**Văn bản nộp nhà trường — giai đoạn ý tưởng.** Đề cương này là bản nén của một báo cáo khoa học hoàn chỉnh ở pha *trước khi đo*: nó trình bày vấn đề, cơ sở lý thuyết, nguyên lý hoạt động, phương pháp, **mục tiêu định lượng**, ngân sách dự đoán và các điều kiện dừng.

> **Một câu phải nói thẳng trước tiên:** tài liệu này **chưa có một số liệu đo thực nghiệm nào của tác giả**. Toàn bộ con số xuất hiện bên dưới thuộc một trong ba loại: (a) trích nguồn đã kiểm (có DOI ở §12), (b) **mục tiêu cần đạt** do chính đề tài đặt ra, hoặc (c) **ngân sách dự toán**. Không dòng nào được đọc như kết quả. Đây là lựa chọn có ý thức, không phải thiếu sót: đề tài được thiết kế sao cho mọi tuyên bố đều truy vết được về một phép đo hoặc một nguồn.

| Cần điền | Giá trị |
|---|---|
| Họ tên học sinh | ⟨điền⟩ |
| Lớp / Trường / Tỉnh | ⟨điền⟩ |
| Giáo viên hướng dẫn | ⟨điền⟩ |
| Năm học / thời điểm nộp | ⟨điền⟩ |

---

## 0. Tóm tắt đề cương

Người bệnh đột quỵ tại Việt Nam sống chung với di chứng bàn tay rất lâu sau khi ra viện: khoảng **1.541 người mắc/100.000 dân** (GBD 2019), **~80%** có tổn thương vận động chi trên ở giai đoạn sớm, và chỉ khoảng **một nửa** số người liệt chi trên hoàn toàn lấy lại được chức năng hữu ích sau 6 tháng [1–3]. Phục hồi chức năng phụ thuộc vào **lượng tập luyện giữa hai lần tái khám**, nhưng chính khoảng thời gian đó lại là khoảng trống đo lường: không có công cụ nào ghi lại được một cách định lượng, đáng tin và rẻ *bàn tay đã làm gì ở nhà*. Cách thay thế hiện nay — để người bệnh tự ghi nhật ký số lần nắm — đã được chứng minh là **không đủ tin cậy để làm đơn vị phân tích**: độ thay đổi tối thiểu có nghĩa (MDC) của cường độ dùng tay đo bằng thiết bị đeo vào khoảng **31%**, và hệ thống đếm nhầm **100–200 lần/giờ** [4].

Đề tài này chế tạo một **găng tay đo — không phải găng tay tập**: một mảng áp trở polymer được ép bởi **vách bên cứng** của ốp ngón, đặt trong cấu hình cầu Wheatstone nửa-bridge để đo **thành phần lực ép bên** — đại lượng tăng theo cả tầm vận động lẫn trương lực cơ, tức chính là thứ cần tách ra. Đóng góp không nằm ở một nguyên lý vật lý mới (không có nguyên lý mới), mà ở **cách ghép ba thứ đã có sẵn thành một phép đo tự kiểm chứng được**: (1) khung cứng định hướng lực để phân biệt *co cứng* với *nỗ lực chủ động* ngay trong một phiên đo, (2) một **chỉ số nỗ lực** và **chỉ số RAL** (mức hỗ trợ thực / mức hỗ trợ yêu cầu) định nghĩa tường minh trên rig cơ khí có tải đã biết, (3) **cờ độ tin cậy theo từng phiên** — mỗi con số xuất ra kèm điều kiện đo và ngưỡng chấp nhận, kèm phát hiện lỗi được cố tình tiêm vào để chứng minh cờ hoạt động.

Kết quả dự kiến không phải "bệnh nhân phục hồi tốt hơn" — đề tài **không** cam kết điều đó. Kết quả dự kiến là: một thiết bị nguyên mẫu, một bộ giao thức và ngưỡng **được đăng ký trước khi đo**, **sáu con số tự đo trên chính bàn tay người chế tạo** (độ lặp lại chu kỳ, độ trôi 10 ngày, tốc độ lấy mẫu, tỉ số tín hiệu/nhiễu, độ trễ hệ thống, độ tuyến tính lực–đáp ứng), và một báo cáo nói rõ cái gì đạt, cái gì fail.

---

## 1. Vấn đề và tính cấp thiết

### 1.1 Gánh nặng đột quỵ ở Việt Nam là lớn và có số, không phải ước đoán

| Đại lượng | Giá trị (GBD 2019, dân số ~98 triệu) | Nguồn |
|---|---|---|
| Tỉ lệ **mới mắc** (incidence) | **222**/100.000 dân/năm (95% UI 206–242) | [1] |
| Tỉ lệ **đang sống chung** (prevalence) | **1.541**/100.000 dân (95% UI 1431–1679) | [1] |
| Tử vong do đột quỵ, 2019 | **135.999** — nguyên nhân tử vong hàng đầu trong nhóm tim mạch | [1] |
| Xếp hạng tử vong do đột quỵ trong 11 nước láng giềng | **thứ 4** (170/100.000) | [1] |
| Yếu tố nguy cơ hàng đầu | huyết áp tâm thu cao (79.000 tử vong), chế độ ăn (43.000), glucose đói cao (35.000), ô nhiễm không khí (33.000) | [1] |

Hai hệ quả trực tiếp với đề tài: (a) ở mức 1.541/100.000, số người đang sống sau đột quỵ ở Việt Nam có thể ước lượng **cỡ 1,5 triệu người** (phép nhân của chúng tôi trên [1], không phải con số in trong bài — dùng đúng mức một **ước lượng quy mô**); (b) bài báo kết luận năng lực chăm sóc tập trung ở hai thành phố lớn trong khi nông thôn có tỉ lệ thấp hơn nhưng tiếp cận kém hơn [1] → **công cụ đo tại nhà có giá trị nhất chính ở nơi ít được đo nhất**.

### 1.2 Bàn tay là di chứng "dai" nhất và cũng là thứ khó đo nhất

Tổn thương vận động chi trên ảnh hưởng **khoảng 80%** người bệnh sau đột quỵ ở giai đoạn sớm; trong số người liệt chi trên hoàn toàn, **chỉ ~50%** lấy lại được chức năng chi trên có ích sau 6 tháng; và **50%** số người có tổn thương cánh tay lúc đầu vẫn còn vấn đề sau **4 năm** [2,3]. Đây là lý do bài toán không phải "đo trong 2 tuần điều trị nội trú" mà là "đo trong nhiều tháng, nhiều năm, ở nhà".

Độ khó của phép đo nằm ở một chi tiết lâm sàng: sau đột quỵ, bàn tay yếu đi vì **hai nguyên nhân chồng lên nhau** — cơ liệt/yếu (không tạo được lực) và **co cứng** (trương lực cơ tăng, kháng lại tầm vận động). Cùng một tầm vận động nhỏ có thể là "người bệnh chưa cố" hoặc "cơ kháng lại". Hai tình huống này dẫn tới hai chỉ định ngược nhau, nhưng **một cảm biến gập ngón không phân biệt được** — nó chỉ biết góc. Đây chính là khoảng trống mà đề tài nhắm vào, và nó được nêu độc lập trong y văn về theo dõi co cứng từ xa [5].

### 1.3 Khoảng trống thật sự: giữa hai lần tái khám, không ai đo được gì

| Nơi xảy ra | Hiện đo bằng gì | Vấn đề đã được chứng minh |
|---|---|---|
| Phòng khám, mỗi 2–8 tuần | Thang điểm lâm sàng (FMA, ARAT, MAS, Box-and-Block) | Cho kết quả **một thời điểm**, và **MDC của chính các thang điểm này đề tài chưa kiểm chứng** (`SRC-ARAT-MDC` vẫn `UNVERIFIED`). Con số MDC ≈ 31 % ở dòng dưới thuộc về chỉ số *cường độ dùng tay do thiết bị đo*, không thuộc về FMA/ARAT |
| Tại nhà | Tự ghi nhật ký số lần tập / tự nhận xét | Không có đối chứng thiết bị; nghiên cứu dùng thiết bị đeo cho thấy người bệnh **đếm lệch 100–200 lần/giờ** khi tự báo cáo [4] |
| Thiết bị PHCN thương mại | Găng robot tại nhà, hệ thống đã FDA chấp thuận | Giá **~350–6.000 USD** [6]; theo khảo sát ý kiến chuyên gia của đề tài, các găng này **không phù hợp** dùng hằng ngày vì giá, rủi ro an toàn và **tạo phụ thuộc vào thiết bị** [14] |

Nhịp đo là vấn đề cốt lõi: chức năng tay thay đổi theo tuần, còn đánh giá lâm sàng xảy ra theo tháng. **Đề tài nhắm đúng khớp nối đó** — không phải bằng cách làm thiết bị tốt hơn, mà bằng cách làm một phép đo *đủ rẻ và đủ tự tin* để lặp lại hằng ngày.

### 1.3bis Số lần tập tự báo cáo là một đại lượng đã biết là hỏng

Nghiên cứu Manumeter (RCT, n = 20 người mạn tính, đeo 3 tuần tại nhà) thiết kế chính xác cho câu hỏi "để người bệnh tự đếm có đủ tin không", và trả lời: **không đủ** — MDC ≈ 31% giá trị trung bình ngày, tỉ lệ đếm nhầm 100–200 lần/giờ, và **hệ thống phải nhỏ, nhẹ, đủ đơn giản để người bệnh dùng được một mình** thì số liệu mới có ý nghĩa phân tích [4]. Ba ý cuối của câu đó định nghĩa luôn ràng buộc thiết kế của đề tài này: **nhẹ, không dây, một người đeo được**.

### 1.4 Ba loại tác động — đề tài tự chấm cả ba, không chỉ loại nghe hay nhất

| Loại tác động | Cơ chế | Bằng chứng đề tài có thể đưa ra ở giai đoạn này | Mức độ mạnh/yếu tự đánh giá |
|---|---|---|---|
| **Với người bệnh** | Phát hiện sớm *điểm dừng tiến bộ* giữa các lần tái khám, khi còn có thể chỉnh bài tập | [1,2,4,5] cho thấy khoảng trống tồn tại và có hậu quả; thiết bị của đề tài **không** tự tuyên bố cải thiện kết cục | **Trung bình** — hợp lý về mặt logic, chưa có dữ liệu người bệnh, và đề tài không xin được hơn thế |
| **Với hệ thống y tế** | Một phép đo rẻ, lặp lại hằng ngày, làm **chuẩn so sánh nội** giữa các phiên, thay vì phụ thuộc hoàn toàn vào các lần đo thưa | Chỉ là **lập luận chi phí cơ hội**, có neo ở [4] và [6]; đề tài **không** đưa con số tiết kiệm | **Yếu–trung bình** — nêu như giả thuyết, không nêu như kết quả |
| **Với phương pháp luận** | Cách **đăng ký trước ngưỡng tin cậy + gắn cờ chất lượng vào từng con số + tiêm lỗi để chứng minh cờ hoạt động** — thứ gần như vắng mặt trong sản phẩm sinh viên và hữu ích trở lại ở mọi đề tài đo lường | Toàn bộ §4.5 (bộ GATE 0→F), §4.4, Phụ lục A | **Mạnh nhất** và là thứ đề tài thực sự sở hữu |

Hàng cuối không phải cách nói giảm để chữa việc thiếu số liệu lâm sàng: nó là **sản phẩm trí tuệ** mà một học sinh có thể làm trọn vẹn mà không cần phê duyệt đạo đức y sinh.

### 1.5 Tính cấp thiết đã được đối chiếu với người làm nghề, không chỉ với bài báo

Giao thức đo, cách chọn ngón, và định nghĩa "thế nào là một phiên đo đáng tin" đã được **tham khảo ý kiến một kỹ thuật viên Vật lý trị liệu – Phục hồi chức năng** [14]. Theo quyết định của chủ dự án, hồ sơ **không nêu danh tính** người được tham khảo; giá trị của bước này chỉ dừng ở mức **"nhu cầu và tính khả thi lâm sàng của phép đo được người làm nghề xác nhận"** — nó **không** là bằng chứng về hiệu quả, và **không** thay thế việc tuyển người bệnh qua hội đồng đạo đức.

---

## 2. Tính mới — xét theo tiêu chí nào

### 2.1 Tiêu chí được nêu tường minh, để hội đồng biết đề tài đang tự chấm mình ở đâu

Đề tài này **không** tuyên bố phát hiện nguyên lý vật lý mới và **không** tự đo mình theo chuẩn tạp chí kỹ thuật (nơi đòi nguyên lý mới + dataset + đối chứng lâm sàng). Nó được thiết kế theo tiêu chí của **Cuộc thi KHKT cấp quốc gia / ViSEF–ISEF**: *một câu hỏi hẹp, trả được bằng một thiết bị tự làm, với số liệu tự đo và phương pháp có thể kiểm điểm được, kết hợp các linh kiện sẵn có theo một cách chưa ai làm cho đúng đối tượng này.* Mọi nhận định "mới/không mới" trong tài liệu này đều đi kèm tên bộ tiêu chí đang dùng, vì cùng một đề tài thay đổi kết luận khi đổi tiêu chí.

### 2.2 Bảng đối chiếu với các công trình và sản phẩm gần nhất (mọi dòng đều có nguồn đã kiểm)

| Công trình / sản phẩm | Nó đo gì | Nó **không** làm gì | Đề tài này khác ở đâu |
|---|---|---|---|
| Găng đa cảm biến tách co cứng khỏi nỗ lực chủ động (Lin et al., *Sensors* 2022;22(19):7212, n = 14, có IRB) [7] | 9 trục + **19 IMU** + 1 bóng áp lực; >1000 đặc trưng/nhiệm vụ | Không có **vách cứng định hướng lực**, không có lực theo hướng, không có khung cờ tin cậy theo phiên | Cùng mục đích, kiến trúc ngược lại: **cơ khí tạo ra sự phân tách** thay vì học máy suy ra nó, với 3 ngón thay vì 19 IMU |
| Găng da xúc giác vỏ cứng khớp nối, 2048 taxel, 22 DoF (ART-Glove, arXiv 2026) [8] | Bản đồ tiếp xúc để thu dữ liệu cho robot học thao tác | Không dành cho bệnh nhân; không theo dõi diễn tiến; không đo lực ép có đơn vị lực | Đề tài dùng **vỏ cứng + phần tử áp trở** cho một mục đích ngược: đo *lực kháng bên* của mô sinh học |
| Găng dữ liệu tái cấu hình, 15 IMU, 3 chế độ dùng chung một backbone (Liu et al., *Engineering* 2024;32:202–216) [9] | Hình dạng bàn tay + lực qua phần tử áp trở mềm **tự chế** để ít cản trở | Chế độ lực được tối ưu cho **không cản trở**, không phải cho **đo được lực theo hướng** | Đề tài chấp nhận **cản trở có chủ đích** (ốp cứng) để có trục lực xác định — đánh đổi ngược chiều |
| Găng mềm robot bàn tay (ironHand) — JR Rehab Assist Technol Eng 2016 [10] và J Rehabil Med 2018;50:598–606 [11] | Hỗ trợ một số động tác ADL; n = 5, 2 phiên | **Không dùng thiết bị đo lực chuẩn hoá làm kết quả chính** | Đề tài bỏ hẳn chức năng hỗ trợ chuyển động để dồn toàn bộ vào phép đo |
| Manumeter — RCT, *Sensors* 2022;22(18):6938 [4] | Số lần dùng tay ở nhà bằng cảm biến | Không tách được co cứng; không có tầm vận động chủ động/thụ động trong cùng một phiên | Đề tài đo **cả hai trong một phiên** (AROM rồi PROM) — chính phép so sánh này tách "không cố" khỏi "bị giữ lại" |
| Găng đo góc + flex, khảo sát hệ thống (arXiv 2024) [12] | Phân loại 6 dòng công nghệ găng | Bản thân tài liệu kết luận flex **1 DoF, khó đặt đủ sensor, nhiễu liên khớp (crosstalk)** | Đề tài **không dùng flex sensor làm số liệu chính** — flex chỉ để suy đoán tư thế |
| Neofect Smart Glove (sản phẩm thương mại, có game và dashboard cho chuyên gia) [13] | Góc + 9 DoF, 132 g, phản hồi thị giác | Không đo lực ép; trạng thái **chưa xác minh độc lập** về thông số | Đề tài không cạnh tranh về phần mềm giải trí; cạnh tranh ở **đơn vị lực + cờ tin cậy** |
| Găng robot tại nhà điều khiển bằng nam châm, *Device* (Cell Press) 2024 [6] | Hỗ trợ duỗi/nắm tại nhà, tổng chi phí **423 USD** (riêng phần găng 22 USD) | Là thiết bị **tác động**, không phải thiết bị **đo** | Đề tài dùng **một phần chi phí đó cho phép đo**, không cho cơ cấu truyền động |

### 2.3 Ba lớp khác biệt — xếp theo thứ tự đề tài dám bảo vệ

1. **Kiến trúc cơ khí:** phần tử cảm biến được ép bởi **vách bên cứng** của ốp ngón, cấu hình **nửa cầu Wheatstone**, để đo riêng thành phần lực ép bên. Không dùng "áp trở dán trên ngón" theo nghĩa thông thường. *Trạng thái: **chưa đo** — và đó chính là câu hỏi của GATE 0 (§4.5).*
2. **Thiết kế phép đo:** **AROM rồi PROM trong cùng một phiên, cùng một ngón**, với hai tốc độ kéo (vì phản ứng co cứng phụ thuộc tốc độ). *Trạng thái: **định nghĩa đã chốt** trên giấy; độ nhạy phụ thuộc tốc độ có nguồn y văn hỗ trợ [5,7].*
3. **Lớp thống kê tự kiểm chứng:** ngưỡng **đăng ký trước khi đo** (MDC, ICC(3 ngày), CV giữa các chu kỳ), mỗi phiên đo mang cờ `UNRELIABLE` khi vượt ngưỡng, và **lỗi được tiêm có chủ đích** để chứng minh cờ bắt được. *Trạng thái: đã thiết kế đầy đủ; **đây là lớp mà đề tài này mạnh hơn cả các công trình đã công bố trong bảng trên**, vì họ có n lớn nhưng không có lớp này.*

### 2.4 Giới hạn của chữ "mới": những câu đề tài này không nói

| Không nói | Vì sao | Câu nói đúng |
|---|---|---|
| "Chưa ai làm găng tay đo lực cho người đột quỵ" | Sai — có sản phẩm thương mại và có công trình [7,9,13] | "Chưa tìm thấy công trình nào dùng **vách cứng định hướng lực + lớp cờ tin cậy theo phiên** cho mục đích theo dõi diễn tiến" |
| "Độ chính xác tương đương máy đo lực lâm sàng" | Chưa so với bất kỳ chuẩn nào | "Chỉ số nỗ lực là **đại lượng không thứ nguyên so sánh nội giữa các phiên**; không quy đổi ADC → newton" |
| "Loại bỏ ảnh hưởng trôi" | Không vật liệu áp trở nào làm được | "**Giảm ảnh hưởng của trôi và từ biến** bằng chu trình chuẩn + phục hồi, và **đo nó** thay vì giả sử nó bằng 0" |
| "Găng tay chẩn đoán / điều trị / ra y lệnh" | Sai phạm vi và sai pháp lý | "Thiết bị **đo và ghi nhận**, hỗ trợ tài liệu cho quyết định của cán bộ y tế" |
| "Lần đầu tiên" | Không dùng được nếu chưa có số liệu tự đo | Chỉ được dùng mẫu câu "**lần đầu tích hợp [A+B] cho [nhóm X]**" **và chỉ khi** đã có số liệu tự đo |

### 2.5 Bối cảnh bằng sáng chế (để hội đồng thấy đã kiểm, không phải chưa nghĩ tới)

| Tài liệu | Trạng thái đã kiểm | Ý nghĩa với đề tài |
|---|---|---|
| US20150233779A1 (Waltop — găng đo áp suất, phân lớp G01L1/20, G01L1/22, G01L5/009) | **Abandoned** | Yêu cầu bảo hộ đã từ bỏ → không phải rào cản; **không** có nghĩa ý tưởng tự do hoàn toàn |
| CN116954366A (ĐH Đông Nam Á — găng mảng cảm biến xúc giác) | **Pending** | Cần đọc điểm yêu cầu bảo hộ trước nếu đề tài thương mại hoá |
| Tra cứu theo nhóm phân lớp (G06F3/014, G01L1/20, G01L1/205, G01L1/22, G01L5/009, A61H1/02, A61H3/01, A61B5/11) | **PARTIAL — chưa đọc toàn văn yêu cầu bảo hộ** | Đề tài chỉ tuyên bố "đã tra cứu và không phát hiện xung đột trực tiếp", không tuyên bố "không vi phạm" |

---

## 3. Cơ sở lý thuyết và nguyên lý hoạt động

### 3.1 Chuỗi truyền đo — và chỗ nào trong chuỗi thì thông tin mất

```
nỗ lực thần kinh → co cơ → ngón ép vào vách cứng của ốp
   → áp suất tiếp xúc p trên mảng Velostat (Δp)
   → biến dạng màng carbon-black, điện trở thay đổi:  ΔR/R = γ · (Δp/p₀)
   → nửa cầu Wheatstone với điện trở cố định R_ref, kích bằng V_EX
   → ΔV = V_EX · ΔR / (R₀ + R_ref)
   → bộ chọn kênh đa hợp (mux) → ADC 12 bit → ESP32-S3
   → cửa sổ trung bình + lấy mẫu lại 20 Hz
   → đại lượng suy ra: EI, GAP, RAL  (KHÔNG phải newton, KHÔNG phải độ khớp)
```

Bốn tầng đầu là **vật lý**, tầng cuối là **định nghĩa**. Đề tài chỉ có thể bảo vệ từng đoạn một, và đó là lý do §4.5 tồn tại: mỗi GATE kiểm chứng đúng một mũi tên ở trên.

### 3.2 Vì sao phải là *lực ép bên*, không phải góc gập

Cảm biến gập (flex) đo **biến dạng của chính ngón** — tức là tầm vận động, và tầm vận động bị ảnh hưởng đồng thời bởi yếu cơ và bởi co cứng ⇒ **nhập nhằng về bản chất**, không phải do thuật toán chưa tốt. Ngược lại, khi ngón bị **duỗi thụ động** khi cơ gấp đang hoạt động, mô mềm bị ép vào vách cứng: phần tử áp trở ở vách **không đổi** nếu người bệnh không cố, và **tăng** khi người bệnh chống lại ⇒ tín hiệu trên vách **tỉ lệ với nỗ lực**. Đây là "nguyên lý hoạt động" của đề tài, và nó **dựa trên** hiệu ứng áp trở đã biết của vật liệu (không phải khám phá mới) [12,15].

### 3.3 Mô hình áp kế vách cứng — và một cửa sổ thiết kế **hai phía**

Với mảng áp trở đặt trên vách cứng, diện tích tiếp xúc chủ động `A_c`, tiền tải `F_p` ⇒ `p₀ = F_p/A_c`, độ nhạy áp trở `γ = d lnR / d lnp`:

```
ΔV/V_EX ≈ γ · Δp / (4 p₀)          (cầu nửa, sai phân bậc nhất)
```

Từ đó suy ra ba điều, và cả ba đều **kiểm chứng được bằng tay**:

1. **`A_c` triệt tiêu ở bậc nhất** ⇒ kích thước mảng **không** phải vấn đề tỉ số tín hiệu/nhiễu; nó là vấn đề **cơ khí** (áp suất phân bố lại, độ lặp lại khi tháo/lắp). Hệ quả thực hành: không cần mua mảng to hơn.
2. **Điều kiện dưới (tín hiệu phải nhìn thấy được).** Với `n_eff ≈ 11` mảng trên 12 kênh, `V_EX = 3,1 V`, `LSB = 1,51 mV` (đây là **ngân sách thiết kế** của `docs/04` §1, **không** phải kết quả đo), và yêu cầu `ΔV ≥ 8 LSB` tại `ΔF = 1 N`, bất đẳng thức rút ra là

   ```
   F_p  ≤  68 · γ · ΔF        → với γ = 0,5 và ΔF = 1 N:  F_p ≲ 34 N
   ```
3. **Điều kiện trên (tiền tải không được quá nhỏ).** Ở tải rất nhẹ, tiếp xúc không ổn định, điện trở cao, nhiễu và từ biến tăng; điện trở nguồn lớn còn làm bộ chọn kênh **kéo dài thời gian ổn định** — nếu thời gian ổn định vượt thời gian một kênh ở 20 Hz thì **cấu hình kênh không khả thi**.

⇒ **Thiết kế chỉ sống trong một cửa sổ `F_p` bị chặn hai phía.** Câu hỏi "cửa sổ đó có rỗng không" chính là nội dung của GATE 0. Đây là điểm mà mọi bản mô tả "dán Velostat lên ngón" đều bỏ qua.

### 3.4 Ba đại lượng dẫn xuất, định nghĩa tường minh, và đơn vị được phép nói

| Đại lượng | Định nghĩa | Điều kiện đi kèm (bắt buộc, in trong mọi bảng số) | Đơn vị |
|---|---|---|---|
| **`EI` — Effort Index** | `EI = median(\|d\|) / (1 + κ·\|v̂\|)` với `d` = đạo phổ ADC của mảng vách, `v̂` = vận tốc góc góc-IMU, `κ` = hằng số làm chậm đã hiệu **hiệu chuẩn trên rig**, không đổi trong một phiên | ngón, tốc độ kéo, hướng dẫn bằng giọng nói | **counts (không thứ nguyên)**, không phải N |
| **`GAP = AROM − PROM`** | tầm vận động **chủ động** trừ tầm vận động **thụ động** trên cùng ngón, cùng phiên | do rig/niêm phong kéo (PROM), tốc độ kéo **hai mức** | độ (IMU) — chỉ trong thang của nó, **không** suy từ ADC |
| **`RAL`** | `RAL = mức hỗ trợ thực / mức hỗ trợ yêu cầu`, đo trên **rig có tải đã biết** | tải (g), vị trí khớp, tốc độ | không thứ nguyên, ∈ [0,1] |

Quy tắc đơn vị là một phần của đề cương, không phải phần trang trí: **không có bước ADC → newton nào**, vì đề tài **không có load cell trên ngón** (load cell chỉ dùng ở **chuẩn đối chứng** trong phòng thí nghiệm); và **không có ADC → độ**, vì góc chỉ đến từ IMU đã tích hợp.

### 3.5 Phi tuyến, trễ, từ biến, trôi: xử lý bằng cách đo, không bằng cách giả sử

Vật liệu áp trở polymer có bốn hiệu ứng đã được ghi nhận rộng rãi: phi tuyến theo tải, **trễ** (đường lên ≠ đường xuống), **từ biến** (creep khi giữ tải), và **trôi theo thời gian** [12,15]. Đề tài đối xử với chúng như **đại lượng phải đo**:

| Hiện tượng | Biện pháp | Ngưỡng chấp nhận (§4.5) | Nếu vượt |
|---|---|---|---|
| Trễ | Chuẩn hoá mọi số đọc tại một điểm trong chu trình | `hys_norm ≤ 15 %` | đổi sang "chu kỳ mở đầu bắt buộc" |
| Từ biến | Chu trình xả–nạp trước khi đo; giữ mẫu 60 s | `creep_2dec ≤ 3 %` | đổi quy trình tiền tải |
| Trôi ngày | **3 lần/ngày × 10 ngày**, không tải | `drift_peak_to_end / σngày ≤ 2` **và** trôi 10 ngày < `ΔV` của `ΔF = 1 N` | **dừng: `GATE C` fail** |
| Nhiệt độ / ẩm | Ghi `T`, `RH` trong mọi phiên; đo lại ở hai mức RH | `γ(T)` giảm được bằng hiệu chính; `γ(RH)` **không** giảm được → dùng bao phủ | đưa `RH` vào điều kiện đo hoặc đổi vật liệu |

Câu "đề tài **loại bỏ** được trôi" là câu đề tài **không** nói. Câu nói được là "đề tài đo trôi, và nói rõ nó còn lại bao nhiêu".

### 3.6 Vì sao phải kéo ở hai tốc độ

Phản ứng căng cơ **phụ thuộc tốc độ kéo** — duỗi nhanh tạo phản ứng mạnh hơn duỗi chậm ở cùng tầm vận động [5,7]. Một phép đo ở một tốc độ không phân biệt được "cứng" với "bị kéo nhanh" ⇒ đề tài quy định **hai tốc độ đã hiệu chuẩn** cho mỗi lần PROM ở GATE 0 và GATE A.

---

## 4. Thiết kế và phương pháp

### 4.1 Kiến trúc hệ thống (ba tầng, mỗi tầng có "cửa" riêng)

```
[Ốp ngón]   12 mảng Velostat trên khung in 3D (3 ngón: 2, 3, cái)
            + 12 flex (chỉ suy đoán tư thế) + 6 IMU + 1 cảm biến môi trường
            → 36 kênh analog → bộ chọn kênh CD74HC4067 (8 × R_ext 100 kΩ)
            → ESP32-S3: ADC 12 bit, V_EX = 3,1 V, cửa sổ trung bình, lấy mẫu lại 20 Hz
            → USB CDC 921.600 baud → [Orange Pi 5 Pro] ghi log nguồn thô + dashboard
```

Tầng 3 chỉ được bật ở `GATE F`; **việc có sẵn máy tính mạnh không làm nhẹ đi tầng 1**.

### 4.2 Quy trình đo trên một ngón (thứ tự cố định, có chủ đích)

`(a)` ngón duỗi — (b) **PROM bị động** (niêm phong kéo, tốc độ A) — (c) **AROM chủ động** (làm theo hướng dẫn bằng giọng nói) — (d) **giữ tư thế giữa** — (e) **kháng nhẹ** — rồi lặp lại cùng quy trình với **tốc độ B**. `GAP` = b − c; `EI` = trung vị độ lớn đạo phổ ở (b), quy đổi về đơn vị chuẩn `V_ex`, chia cho tử số làm chậm.

### 4.3 Hiệu chuẩn và chuẩn lực: dùng **trọng lượng đã cân**, không dùng lực kế

Trong toàn bộ GATE 0, **lực chuẩn là `F = m·g` của các khối lượng đã cân** — không trễ, không cần điện tử, không cần tuyến tính, và có thể kiểm lại bằng cân nhà bếp. Hệ quả thực hành: đề tài bắt đầu bằng vài trăm nghìn đồng khối lượng và một đồng hồ đo, **không** phải bằng một load cell. `Δp` được tạo ra bằng **cơ cấu dẫn động đã biết** ở GATE A, **không** bằng một vật nặng đặt lên mảng (vật nặng làm méo mảng không kiểm soát được, dù nó là lực chuẩn tốt — `docs/02` §5.1).

### 4.4 Xử lý số liệu và cờ độ tin cậy

Chuỗi thô `R_i(t)` từng kênh; `ΔR/R₀(t)`; hệ số suy giảm chậm `λ = 3,75·10⁻⁴ s⁻¹` (kịch bản tài liệu thiết kế `docs/04` §1 — **dùng làm đầu vào cho mô phỏng, có ghi rõ là kịch bản, không phải kết quả**); các phiên bản λ nhân 0,25 và ×4 để tìm độ nhạy. Chỉ số theo phiên:

```
EI_v   = median(|d|) / (1 + κ·|v̂|)        R_rel = median(EI_v,PROM)/median(EI_v,AROM)
CV     = std(EI_v)/mean(EI_v)              FLAG = UNRELIABLE khi SNR < 8 LSB hoặc |T−23|>5 °C
```

**Định nghĩa nhiễu được chốt ở ô `G0.0`** và dùng nhất quán: bản A `noise_pp = max − min` trên 20 mẫu liên tiếp (tính tay được) hoặc bản B `σ` trên ≥ 5.000 mẫu đứng yên. **Chọn một trong hai trước khi đo, không đổi sau.**

### 4.5 Bộ kiểm chứng: 10 ngưỡng, đăng ký trước khi đo

> **Cam kết phương pháp của đề tài:** các ngưỡng dưới đây được viết ra và **đóng chốt trước khi có bất kỳ số liệu đo nào**, và sẽ **không** được chỉnh lại sau khi thấy số. Nếu một ngưỡng không đạt, đề tài báo cáo **fail** ở ngưỡng đó. "GATE 0 pass" không được viết khi `G0.1` hoặc `G0.7` fail.

| ID | Câu hỏi mà nó trả lời | Ngưỡng |
|---|---|---|
| **G0.0** | Chọn định nghĩa nhiễu **trước khi đo** | A: `noise_pp` = max−min/20 mẫu (đo tay được) · B: `σ`/≥5.000 mẫu (cần script) |
| **G0.1** | Có tồn tại một `F_p` sao cho mảng **vừa đủ nhạy, vừa đủ ổn định**? | ∃ `F_p` với `R₀ ≤ R_max` **và** `SNR ≥ 8 LSB` tại `ΔF = 1 N` |
| **G0.2** | Mảng có thật sự hoạt động như áp kế? | `γ_i ≥ 0,25` ở ≥ 4/5 mảng họ A, `R² ≥ 0,95` |
| **G0.3** | Có lặp lại được giữa các chu kỳ không? | `CV_chu kỳ ≤ 5 %` |
| **G0.4** | Có lặp lại được giữa các **ngày** không? | `ICC(3 ngày) ≥ 0,75`; nếu không → `MDC` không đổi được hệ số trong 4 tuần |
| **G0.5** | Đường lên có trùng đường xuống? | `hys_norm ≤ 15 %` |
| **G0.6** | Có bị lún khi giữ tải? | `creep_2dec ≤ 3 %` |
| **G0.7** | **Tín hiệu trôi chậm hơn biên độ cần đo không?** | `drift_ratio ≤ 2` **và** trôi 10 ngày < `ΔV` tại `ΔF = 1 N` |
| **G0.8** | Các mảng có đủ giống nhau để so sánh giữa các ngón? | độ rải `γ` ≤ ±40 % (dùng để **chấp nhận** ma trận hiệu chỉnh, không phải để chứng minh vật liệu ổn định) |
| **G0.9** | CẤU HÌNH kênh có đọc được đủ nhanh? | `fps_meas ≥ 20 Hz` trên 12 kênh |

**Nếu GATE 0 fail:** ba hướng cứu đã chuẩn bị sẵn — (i) bộ đệm FET cho phép trở nguồn cao, (ii) bỏ `EI`, chỉ giữ `GAP`/`RAL` (chuyển sang IMU + tải), (iii) chuyển sang **đai đàn hồi** (đo lực kéo của dây chun) — tất cả đều được chấm **trước khi** mua gì thêm, theo nguyên tắc "mỗi lớp giải ngân chỉ khi lớp trước pass". **Nếu cả ba hướng đều không mở lại được cửa sổ trong ≤ 3 tuần, đề tài dừng ở dạng báo cáo phương pháp + kết quả âm tính** và vẫn được nộp như một báo cáo trung thực.

### 4.6 Nguyên mẫu tác động (E4) và rig kiểm chứng (E5) — phục vụ đo lường, không phục vụ điều trị

Một **rig cơ khí** gồm: trục trượt + vít me dẫn động 1 khớp, **phanh từ** để chặn đột ngột một tư thế, và **tải chuẩn** (lò xo + khối lượng). Nó có **hai** vai trò: (1) tạo `Δp` đã biết cho GATE A; (2) **tiêm lỗi có chủ đích** — một tải bị thiếu, một kênh bị trôi nhanh, một mux hoạt động sai — để chứng minh hệ thống **tự phát hiện** được qua cờ và qua `RAL`, tức là chứng minh lá phiếu `UNRELIABLE` không phải đồ trang trí.

### 4.7 Công cụ không phải phần cứng

- **Phiếu tham khảo chuyên gia 10 câu** (`research/protocols/07` §5): câu 1–5 cho thiết kế, 6–10 cho diễn giải; mỗi câu trả lời ghi lại **dưới dạng quyết định** (câu nào được chấp nhận → biến thành ràng buộc thiết kế, câu nào bị từ chối → ghi lý do).
- **9 file markdown đã khoá cấu trúc** (`docs/02`, `docs/04`, `research/evidence/SOURCE_LEDGER.csv` với **137 dòng**, `research/claims/CLAIM_LEDGER.csv`, `research/bench/logs/`...): mỗi tuyên bố trong đề cương này truy vết được về một dòng ledger.
- **Nhật ký truy vấn ngoài** (`research/queries/QUERY_LOG.jsonl`): mỗi lần tra cứu đều được ghi, kể cả những lần **tìm không thấy** — vì "tìm không thấy" không có nghĩa là "không tồn tại".

---

## 5. Mục tiêu định lượng

### 5.1 Mục tiêu sản phẩm (M1–M6) và cửa đo của từng mục tiêu

| ID | Mục tiêu | Đơn vị / công thức | Cửa đo | Thuộc GATE nào |
|---|---|---|---|---|
| M1 | Tín hiệu khả dụng | `SNR ≥ 8 LSB` tại `ΔF = 1 N` | bench, chuỗi thô | **G0.1** |
| M2 | Độ nhạy áp trở | `γ = ∂lnR/∂lnp`, yêu cầu `≥ 0,25` ở ≥ 4/5 mảng | 5 bậc tải | G0.2 |
| M3 | Độ lặp lại | `CV_chu kỳ ≤ 5 %`, `ICC(3 ngày) ≥ 0,75` | 3 ngày × 3 phiên | G0.3, G0.4 |
| M4 | Tín hiệu chống lại trôi | `drift / (ΔV tại 1 N) < 1`, `drift_ratio ≤ 2` | 10 ngày | **G0.7** |
| M5 | Phản hồi theo thời gian thực | `fps_meas ≥ 20 Hz` · `latency_p95 ≤ 500 ms` | 12 kênh | G0.9, GATE F |
| M6 | Cờ độ tin cậy bắt được lỗi | ≥ 4/5 lần tiêm lỗi bị cờ | 5 lỗi tiêm vào | GATE E |

### 5.2 Tiêu chí để hội đồng chấm **đề cương** này (không phải báo cáo)

| Đề cương được coi là hoàn thành mục tiêu khi | Trạng thái hiện tại |
|---|---|
| Có ≥ 6 con số **tự đo** trong báo cáo cuối kỳ | chưa — là cam kết, không phải thành tích |
| Toàn bộ ngưỡng được chốt **trước** khi bật nguồn đo | ☐ **cần chủ dự án tích 10 ô** (`research/protocols/08` §7) — đây là việc còn lại duy nhất |
| Không có tuyên bố hiệu quả lâm sàng, không có dữ liệu người trước IRB | ✔ đang đúng và sẽ giữ đúng |
| Mọi con số trong hồ sơ có hoặc DOI hoặc `research/bench/logs/` | ✔ cơ chế đã dựng xong (137 dòng ledger) |

---

## 6. Kế hoạch triển khai (không có mốc chết — kế hoạch theo thứ tự cửa, không theo lịch thi)

| Pha | Nội dung | Khối lượng dự kiến | Cửa sang pha sau |
|---|---|---|---|
| **0** | Chốt 10 ngưỡng; mua khối lượng chuẩn + in jig | 1 tuần, 8 buổi bench × 2–3 h | `G0.1` + `G0.7` chưa fail |
| **1** | GATE 0 trên bench, không firmware phức tạp: DMM + khối lượng + đồng hồ bấm giây; phiếu đo in được | 8 buổi, **mọi phép tính chỉ là trừ số nguyên** | pass `G0.1…G0.9` |
| **2** | GATE A: 1 ngón, `Δp` đã biết, 60°/s + 10°/s, `SNR/THD/ENOB` (ADS1115 để so sánh) | 2–3 tuần | `GATE A` pass |
| **3** | GATE B: ma trận hiệu chỉnh `γ` + `V_ex`, `MDC` từ chính dữ liệu GATE A | 2 tuần | pass |
| **4** | GATE C: **cửa giết đề tài** — trôi 28 ngày, 60 °C/85 %RH, chu trình tháo/lắp | 4–6 tuần (phần lớn là chờ) | pass hoặc đề tài chuyển thành báo cáo phương pháp |
| **5** | GATE D: `RAL` trên rig có tải; hai tốc độ; `GAP` | 3–4 tuần | pass |
| **6** | GATE E: tiêm lỗi, chứng minh cờ hoạt động | 1–2 tuần | pass |
| **7** | GATE F: bật tầng Orange Pi, `latency_p95` | 1–2 buổi | — |

**Năng lực đã có để làm những việc trên** (không phải hứa hẹn): firmware nhúng đã tồn tại trong repo (`firmware/`, có nhật ký chạy); mô hình toán của chuỗi truyền đo đã viết và đã được kiểm lại; quy trình tra cứu trước nghiệm và sổ bằng chứng đã vận hành.

---

## 7. Ngân sách dự đoán

**Cách đọc bảng:** cột "Cần chi tiền mặt" **đã trừ** các vật tư mà người thực hiện **đã có sẵn**. Vật tư đã có **không** được tính là "chi phí bằng 0" — nó là một mục riêng, vì chi phí cơ hội của nó có thật và hội đồng có quyền biết.

| Lớp | Hạng mục | Dải giá tham khảo (VND) | Trạng thái | Cần chi tiền mặt |
|---|---|---|---|---|
| **0 — GATE 0** | Màng Velostat (~10 mẫu × 2 mặt) | 150.000–400.000 | **đã có** | 0 |
| | Đồng lá tự dính | 80.000–200.000 | **đã có** | 0 |
| | Tấm acrylic/PVC 2 mm làm mẫu áp kế + jig | 60.000–250.000 | cần mua/in | 60–250k |
| | Khối lượng chuẩn 200–500 g (hoặc thay bằng vật đã cân đối chứng) | 0–150.000 | một phần tự làm | 0–150k |
| | Dây, đầu nối, băng polyimide, điện trở 100 kΩ 0,1 % | 60.000–250.000 | một phần có sẵn | 60–250k |
| | Đồng hồ đo số (4 dây) — **nếu chưa có** | 300.000–800.000 | ⟨kiểm tra⟩ | 0 hoặc 300–800k |
| **1 — GATE A/B** | ESP32-S3 + kháng trở + mux CD74HC4067 | 250.000–600.000 | **board đã có**; mux ⟨kiểm tra⟩ | 15–60k |
| | ADC 16 bit rời (ADS1115) để so sánh | 120.000–250.000 | cần mua nếu muốn so | 120–250k |
| | Load cell 5 kg + HX711 (**chỉ dùng ở chuẩn đối chứng**, từ GATE A) | 90.000–220.000 | cần mua | 90–220k |
| | In 3D ốp ngón + khung (TPU/PLA) | 150.000–400.000 | tự in / thuê in | 150–400k |
| | IMU (6), flex (12), cảm biến `T/RH` (1) | 300.000–700.000 | một phần có sẵn | 200–600k |
| **2 — GATE D/F** | Orange Pi 5 Pro | 4.000.000–6.000.000 | **đã có** | 0 (nếu mua: +4–6 tr) |
| | Rig: nhôm V-me, vít me, bạc đạn, encoder, lò xo + tải chuẩn | 900.000–2.000.000 | cần mua | 0,9–2,0 tr |
| | Phantom silicone in khuôn | 200.000–500.000 | tự đúc | 200–500k |
| **3 — nếu mở rộng sang người bệnh** | Phí thẩm định IRB/SRC + biểu mẫu đồng ý + tiêu hao y tế | **chưa xác định được**; thường không phải chi phí lớn nhất | **không nằm trong phạm vi đề cương này** | — |

| Tổng hợp | Số tiền |
|---|---|
| **Tiền mặt cần chi để đi hết GATE 0** | **≈ 0,12–0,65 triệu đồng** |
| Tiền mặt để đi hết **GATE A + B** | + ≈ 0,57–1,5 triệu đồng |
| Toàn bộ tới **GATE F** với vật tư đã có sẵn | ≈ **1,8–4,7 triệu đồng** (= 0,12–0,65 + 0,57–1,50 + 1,10–2,50) |
| Kịch bản phải mua **toàn bộ** (không có gì sẵn) | ≈ **6,5–12 triệu đồng** (thêm Velostat 0,15–0,4 · đồng lá 0,08–0,2 · board 0,25–0,6 · máy tính 4–6) |
| **Chi phí tối đa nếu GATE 0 fail** | **≤ 0,65 triệu đồng** (chưa tính đồng hồ đo nếu phải mua: +0,3–0,8) — thiết kế theo nguyên tắc cắt lỗ sớm |

Ba quy tắc giá áp dụng cho đề cương và mọi tài liệu sau này: **(1)** mọi con số ở đây là **dự toán tham khảo tại thời điểm viết**, chưa phải báo giá, chưa có hoá đơn; **(2)** không dùng giá thương mại (Neofect ~1.925 USD — mức nhà cung cấp, **chưa xác minh độc lập** [13]) làm "giá của đề tài", mà chỉ làm **mốc so sánh**, kèm nguồn; **(3)** mục nào mua thật sẽ được cập nhật bằng báo giá thật + ảnh hoá đơn lưu vào `research/bench/logs/` (xem `research/context/EQUIPMENT_AND_ACCESS.md`).

---

## 8. Rủi ro chính và cách đề tài phản ứng

| Rủi ro | Xác suất tự đánh giá | Hệ quả nếu xảy ra | Phản ứng đã chuẩn bị |
|---|---|---|---|
| **Cửa sổ `F_p` rỗng** — không có tiền tải nào vừa nhạy vừa ổn định | Trung bình–cao | GATE 0 fail | 3 hướng cứu ở §4.5; nếu cả ba fail trong ≤ 3 tuần → báo cáo phương pháp + kết quả âm tính |
| **Trôi 10 ngày vượt biên độ cần đo** | Trung bình–cao | Phá tan mọi kết luận về *diễn tiến* | `G0.7` + quy trình chuẩn hoá; nếu fail → đề tài **không** nói về diễn tiến theo tuần |
| Thiết bị đo góc/áp lực thương mại đã nhiều → bị xem là "không mới" | Cao (đúng là đã nhiều) | Mất điểm nếu chỉ nói "chúng em làm găng tay" | Trình §2.2–2.3: **phân biệt bằng cơ khí + lớp thống kê**, không bằng tên thiết bị |
| Hội đồng hỏi "số liệu người bệnh đâu" | Cao | Bị xem là chưa xong | Trả lời định trước: "đúng, và đề tài **không** lấy số liệu người trước khi có phê duyệt đạo đức; kết quả tự đo trên người chế tạo + rig, có thể kiểm điểm" |
| Công việc chỉ nằm ở giai đoạn ý tưởng quá lâu | Trung bình | Trễ mà không biết | Mỗi buổi bench kết thúc bằng 1 ảnh + 1 file log thô, kể cả buổi fail |

---

## 9. An toàn và đạo đức

1. Thiết bị đeo **không** truyền lực vào người, **không** kích thích điện, **không** chẩn đoán: công cụ **đo và ghi nhận**.
2. Bộ chấp hành (rig/E5) **chỉ** tác động lên **rig và phantom** — **không** thử trên bất kỳ ai, kể cả người nhà của người thực hiện.
3. **Không** thu thập dữ liệu của người khác trước khi có phê duyệt IRB/hội đồng đạo đức của trường + giấy đồng ý; chữ ký của giáo viên hướng dẫn hay gia đình **không** thay được phê duyệt đó.
4. Đã **tham khảo ý kiến chuyên gia vật lý trị liệu – phục hồi chức năng** về tính cấp thiết và giao thức đo. Chuyên gia **không** là đối tượng đo, **không** là nguồn tuyển người bệnh, và ý kiến đó là bằng chứng **nhu cầu**, **không phải** bằng chứng **kết quả**. Hồ sơ **không nêu danh tính** người được tham khảo.
5. Dữ liệu xử lý tại biên; **không** đưa tên, mã số, hình ảnh nhận dạng của bất kỳ người bệnh nào vào tài liệu.
6. Đề cương **không** nêu cam kết nào về hiệu quả lâm sàng. Nếu `GATE C` fail, đề tài **dừng ở đó và nói rõ đã fail**, không hạ chuẩn.

---

## 10. Sản phẩm dự kiến

| Sản phẩm | Mô tả có kiểm chứng được | Tiêu chí "xong" |
|---|---|---|
| Nguyên mẫu găng | 3 ngón có ốp vách cứng, 12 mảng áp trở + 6 IMU, firmware ghi log | ảnh thiết bị **đang chạy** + tín hiệu thật trên màn hình |
| Bộ giao thức + ngưỡng | `research/protocols/06`–`08a`, `docs/04` | 10 ngưỡng được chốt **trước** khi đo, có ngày ghi |
| Sáu con số tự đo | `CV`, `ICC`, `MDC`, trôi 10 ngày, `fps`, `latency_p95` — **bắt buộc có số** | `research/bench/logs/` có file cho từng con số |
| Báo cáo cuối kỳ | 15–20 trang, ≥ 1,3 ảnh/bảng mỗi trang, ≤ 2 trang lý thuyết | mỗi GATE một ô kết quả, fail vẫn in ra |
| Kho tái lập | source + schema + `SOURCE_LEDGER.csv` + log | người khác chạy lại được và ra số trong dung sai đã nêu |

---

## 11. Hạn chế — tự khai trước khi hội đồng hỏi

| # | Hạn chế | Cách đề tài xử lý |
|---|---|---|
| 1 | Không có kết quả đo nào tại thời điểm nộp đề cương | nêu ở đầu trang, không nói vòng quanh |
| 2 | Chuỗi truyền đo **chưa** được hiệu chuẩn `ΔR → N`; ADC không quy đổi ra newton | dùng **counts** + `EI` không thứ nguyên; giữ nguyên lời khuyên "dán lên ngón không cho lực" |
| 3 | Đối tượng tự kiểm chứng ban đầu là **một người** (chính người thực hiện) — không phải người bệnh | mọi kết luận về khả năng áp dụng lâm sàng bị chặn tới khi có IRB + n ≥ 20 |
| 4 | Velostat phi tuyến, trễ, từ biến, trôi, nhạy ẩm | đưa thành ngưỡng đo được (G0.5/G0.6/G0.7) thay vì tuyên bố đã khắc phục |
| 5 | Không có bằng chứng về kết cục lâm sàng | tuyên bố dừng ở "cung cấp phép đo đáng tin", không tới "cải thiện phục hồi" |
| 6 | `RAL` **không** dùng như chỉ số lâm sàng, chỉ dùng để so sánh cấu hình máy và chứng minh hệ thống phát hiện lỗi được | ghi rõ trong mọi bảng có `RAL` |
| 7 | `GAP` và `EI` **không** thay thế bất kỳ thang điểm nào (FMA/ARAT/MAS) | mục tiêu là **bổ sung tần suất đo**, không thay thế công cụ chuẩn |

---

## 12. Tài liệu tham khảo

*Mỗi dòng ghi rõ mức đã đọc thật, vì "đã đọc tóm tắt" và "đã đọc toàn văn" là hai mức khác nhau.*

1. Tran M.C., Prisco L., … Mai T.D., Farmery A. "Comprehensive analysis of stroke epidemiology in Vietnam: Insights from GBD 1990–2019 and RES-Q 2017–2023." *Global Epidemiology* 2025;9:100199. DOI: 10.1016/j.gloepi.2025.100199 — **đã đọc toàn văn bản trên PMC**.
2. Pollock A., Farmer S.E., Brady M.C., Langhorne P., Mead G.E., Mehrholz J., van Wijck F. "Interventions for improving upper limb function after stroke." *Cochrane Database Syst Rev* 2014;11:CD010820. DOI: 10.1002/14651858.CD010820.pub2 — **đã đọc abstract + phần Background**; các con số 80%/50% ở §1.2 trích từ mục Background này (nó dẫn Langhorne 2009, Kwakkel 2003, Broeks 1999).
3. Langhorne P., Coupar F., Pollock A. "Motor recovery after stroke: a systematic review." — **trích gián tiếp** qua [2]; chưa đọc bản gốc → **đề tài không trích nguyên văn**.
4. Schwerz de Lucena D., Rowe J.B., Okita S., Chan V., Cramer S.C., Reinkensmeyer L.E. "Providing Real-Time Wearable Feedback to Increase Hand Use after Stroke: A Randomized, Controlled Trial (Manumeter)." *Sensors* 2022;22(18):6938. DOI: 10.3390/s22186938 — **đã đọc abstract**.
5. Amin K.R. et al. "Remote Monitoring for the Management of Spasticity: Challenges, Opportunities and Proposed Technological Solution." *IEEE Open J. EMBC* 2024. DOI: 10.1109/OJEMB.2024.3523442 — **đã đọc abstract** (đối tượng là co cứng nói chung, không riêng bàn tay).
6. "A magnetically controlled soft robotic glove for hand rehabilitation." *Device* (Cell Press) 2024. PII: S2666-9986(24)00412-5 — **đã đọc abstract** (số 423 USD và dải 350–6.000 USD nằm ở đây).
7. Lin B.-S., Lee I.-J., Hsiao P.-C., Yang S.-Y., Chen C.-Y., Lee S.-H., Huang Y.-F., Yen M.-H., Hu Y.H. "Design of a Multi-Sensor System for Exploring … Spasticity." *Sensors* 2022;22(19):7212. DOI: 10.3390/s22197212 — **đã đọc abstract**; đối thủ gần nhất, n = 14, có IRB 11002-007.
8. Lin C., Zhao D. "ART-Glove: Articulated Tactile Glove for Contact-Grounded Dexterous Interaction Capture." arXiv:2606.16370 [cs.RO], 2026. DOI: 10.48550/arXiv.2606.16370 — **đã đọc abstract**.
9. Liu H., Zhang Z., Jiao Z., et al. "A Reconfigurable Data Glove for Reconstructing Physical and Virtual Grasps." *Engineering* 2024;32:202–216. DOI: 10.1016/j.eng.2023.01.009 — **đã đối chiếu trang tạp chí**.
10. Radder B., Prange-Lasonder G.B., Kottink A.I.R., et al. ironHand, *J Rehabil Assist Technol Eng* 2016;3:2055668316670553 — **đã đọc tóm tắt**.
11. Radder B. et al. "Feasibility of a wearable soft-robotic glove to support … daily life." *J Rehabil Med* 2018;50:598–606. DOI: 10.2340/16501977-2357 — **đã đọc** (n = 5; không dùng thiết bị đo lực chuẩn hoá làm kết quả chính).
12. "A Systematic Review on Custom Data Gloves." arXiv:2405.15417, 2024 — **đã đọc abstract**.
13. Neofect Smart Glove, trang nhà cung cấp — **mức nhà cung cấp, chưa xác minh độc lập**, chỉ dùng làm mốc so sánh.
14. Phỏng vấn kỹ thuật viên VLTL–PHCN ngày 13/09/2026, lưu tại `research/context/CONVERSATION_2026-09-13.md` — **ý kiến chuyên môn có ghi chép**, không phải nghiên cứu định lượng.
15. "Low-cost resistive pressure sensing using carbon black-loaded silicon rubber (Velostat)" và "Piezoresistive properties of Velostat" (MIT Media Lab 2012; Sensorix) — **đã đọc**; cơ sở cho `γ`, trễ, từ biến.

---

## Phụ lục A — những câu đề tài này sẽ không nói (và vì sao)

| Câu | Vì sao không |
|---|---|
| "Thiết bị đã được kiểm chứng lâm sàng" | không có nghiên cứu lâm sàng, không xin được trong phạm vi này |
| "Đo lực chính xác đến ±0,1 N" | không có chuẩn so sánh; không có ADC → N |
| "Độ chính xác 99%" kiểu "đạt" sau một lần đo | một lần đo không phải một con số; mọi `Δ` phải đi kèm `CV`/`ICC`/`MDC` |
| "Chi phí 0 đồng vì được tài trợ" | vật tư được **cung cấp**, chi phí cơ hội vẫn tồn tại — nêu như §7 |
| "Thay thế được FMA/ARAT" | mục tiêu là tần suất đo, không phải thay thế công cụ chuẩn |
| "Loại bỏ được trôi" | chỉ **giảm ảnh hưởng** và **đo nó** |
| "Bệnh nhân tập tốt hơn khi dùng găng" | đề tài không can thiệp điều trị ⇒ không có quyền nói về kết cục |

---

### Ghi chú cho người nộp
- Đề cương này **điền 4 ô danh tính** là nộp được; không có ô nào khác chờ số liệu.
- Trước khi nộp, xoá 2 dòng khỏi `docs/bao_cao/A1_ly_do_chon_de_tai.md` nếu lấy nguyên văn từ đó: con số **80%** đang được gán cho Hendricks 2002 trong khi nguồn đúng cho con số đó là [2]/[3] ở đây (Hendricks 2002 bàn về các mốc hồi phục vận động, không đưa tỉ lệ 80% tổn thương chi trên).
- Không có giá nào trong đề cương được trình như giá đã chốt; cập nhật bằng báo giá/hoá đơn trước khi đưa vào báo cáo chính thức.
