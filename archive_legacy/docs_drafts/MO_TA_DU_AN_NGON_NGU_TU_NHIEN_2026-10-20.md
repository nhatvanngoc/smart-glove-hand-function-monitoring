# MÔ TẢ DỰ ÁN

**Tên dự án:** *Nghiên cứu và phát triển găng tay hỗ trợ phục hồi chức năng sau đột quỵ cho vận động tinh.*

Lĩnh vực: ⟨…⟩ · Đơn vị: ⟨…⟩ · Thành viên: ⟨…⟩ · Người hướng dẫn: ⟨…⟩

---

## TÓM TẮT DỰ ÁN

Đột quỵ để lại di chứng nặng nhất ở bàn tay, mà bàn tay lại là thứ khó đo nhất: các thang khám lâm sàng chỉ đánh giá vài tuần một lần, còn thiết bị đeo hiện có chủ yếu đếm chuyển động thô. Nhóm nghiên cứu chế tạo một chiếc găng tay nẹp ba ngón (cái, trỏ, giữa) làm được hai việc cùng lúc: **đo** nỗ lực vận động của người tập bằng cảm biến giá rẻ, và **kéo trợ lực** đúng phần người tập còn thiếu.

Cảm biến gồm 3 cảm biến gập Flex và 6 ô áp trở làm từ tấm Velostat, đọc qua bộ chuyển đổi tương tự – số 16 bit ADS1115 và xử lý trên vi điều khiển ESP32-S3. Trợ lực do servo cuốn dây cáp trên 3 tang riêng, điều khiển theo nguyên tắc trợ lực theo nhu cầu: máy chỉ giúp khi người tập chưa tự hoàn thành tầm vận động, và tự giảm dần khi phát hiện người tập đã tự làm được. Đơn vị đánh giá là một bài tập thật — **gắp thìa** — chứ không phải số lần co duỗi.

Toàn bộ kiểm định thực hiện trên bàn đo và mô hình bàn tay giả silicone. Đến nay nhóm đã in thử và so sánh 9 phương án khóa nẹp, hoàn thành 2 vòng lặp thiết kế mạch thu nhận và xác định được nguyên nhân mạch bị bão hòa ở vòng đầu. Các chỉ số còn lại là mục tiêu thiết kế, chưa phải kết quả đo. Đề tài không thử nghiệm trên người bệnh và không tuyên bố hiệu quả điều trị.

---

## A. VẤN ĐỀ NGHIÊN CỨU

### 1. Lý do chọn đề tài

Đột quỵ là một trong những nguyên nhân hàng đầu gây tàn tật ở Việt Nam. Tỷ lệ hiện mắc năm 2019 vào khoảng 1.541 ca trên 100.000 dân, và mỗi năm có thêm khoảng 222 ca mới trên 100.000 dân [1].

Điều đáng nói là sống sót sau đột quỵ chưa phải là hết vấn đề. Tổng quan của Cochrane ghi nhận khoảng 80% người sống sót bị suy giảm vận động, và trong nhóm liệt hoàn toàn chi trên thì chỉ khoảng một nửa phục hồi được một phần chức năng sau 6 tháng [5, 6]. Bàn tay là bộ phận hồi phục chậm nhất và khó nhất, vì tay phải thực hiện được các động tác tinh như cầm thìa, cài cúc áo, cầm bút chứ không chỉ co duỗi.

Vấn đề nằm ở chỗ quá trình tập luyện đó gần như không được đo lường. Người bệnh xuất viện về nhà và tự tập, trong khi việc theo dõi ngoại viện hiện thiếu một công cụ định lượng ổn định. Các thang đo lâm sàng như FMA-UE hay ARAT thì gián đoạn, vài tuần mới đánh giá một lần và phụ thuộc người khám. Thiết bị đeo cổ tay Manumeter đã được thử nghiệm lâm sàng, nhưng để phát hiện được tiến triển thì người đeo phải thay đổi tới khoảng 31% cường độ sử dụng trong ngày, đồng thời thiết bị đếm sai từ 100 đến 200 lần dương tính giả mỗi giờ [7]. Nói cách khác, công cụ hiện có hoặc là quá thưa, hoặc là quá ồn.

Khảo sát của nhóm tại cơ sở phục hồi chức năng vào tháng 9 năm 2026 cũng ghi nhận các loại găng hỗ trợ đang có trên thị trường chưa phù hợp với điều kiện tập tại nhà ở Việt Nam: giá thành cao, khối lượng nặng và thao tác đeo phức tạp.

Từ những thực tế trên, nhóm nghiên cứu chọn chế tạo một chiếc găng tay nẹp ba ngón hỗ trợ người tập đi từ vận động gập – duỗi cơ bản đến thao tác **gắp thìa bằng ngón cái, trỏ và giữa**. Định hướng này khác với hai hướng phổ biến: không chỉ đếm chuyển động rồi báo cáo, và cũng không kéo tay người tập một cách thụ động theo chu kỳ định sẵn.

### 2. Xác định vấn đề nghiên cứu

Vấn đề nghiên cứu được phát biểu như sau: liệu một mảng cảm biến gập và cảm biến áp trở đặt trên khung nẹp ba ngón có tạo được tín hiệu đủ ổn định và đủ lặp lại để phát hiện vận động chủ động của người tập hay không, và liệu cơ cấu servo – dây cáp – ba tang có tạo được dạng kẹp ba chấu với mức trợ lực tự giảm dần hay không.

Cụ thể, nhóm nghiên cứu tập trung vào sáu nội dung:

- Nghiên cứu chế tạo khung nẹp ba ngón tích hợp 3 cảm biến gập Flex và 6 ô áp trở Velostat bố trí theo cặp lòng – mu, để vừa đọc được tư thế ngón vừa đọc được lực ép.
- Nghiên cứu mạch thu nhận tín hiệu và thuật toán lọc số, để tín hiệu từ cảm biến giá rẻ đủ sạch và đủ nhanh dùng cho điều khiển thời gian thực.
- Nghiên cứu xây dựng bộ chỉ số đánh giá tiến triển gồm EI, GAP và RAL, cùng các chỉ số của bài tập gắp thìa, để việc tập luyện có thể theo dõi bằng số.
- Nghiên cứu thiết kế cơ cấu trợ lực ba tang với duỗi chủ động bằng nhả dây, để găng tay hỗ trợ được cả hai chiều gập và duỗi.
- Nghiên cứu quy tắc tự động chuyển chế độ trợ lực và nhánh thị giác nhận biết bài tập thìa, để hệ thống tự nhận ra khi nào người tập đã tự làm được.
- Nghiên cứu xây dựng quy trình kiểm chứng toàn bộ hệ thống trên giàn đo cơ học và mô hình bàn tay giả, trước khi xét đến bất kỳ thử nghiệm nào trên người.

Hai câu hỏi khó nhất trong sáu nội dung đó là: (i) trong phép thử có tải và điều kiện xác định, tín hiệu áp trở từ hai vách lòng – mu có phân biệt được hướng vận động với độ tin cậy chấp nhận được, và có tự phát hiện được phiên đo lỗi do đeo nẹp lỏng hay không; (ii) bộ điều khiển có phân biệt được chuyển động do người tập khởi xướng với chuyển động do chính cơ cấu tạo ra hay không, vì nếu không phân biệt được thì máy sẽ tự nâng mức hỗ trợ cho một người không hề có vận động chủ động.

### 3. Mục tiêu nghiên cứu

Mục tiêu tổng quát là chế tạo và đánh giá được nguyên mẫu găng tay nẹp ba ngón, hoạt động ổn định trên bàn thử nghiệm, với bộ số liệu đo lường có thể dùng để theo dõi tiến triển vận động tinh của bàn tay.

Mục tiêu cụ thể gồm ba phần. Thứ nhất, hoàn thiện phần đeo: khung nẹp in 3D có khóa mà người yếu tay vẫn tự đeo được bằng một tay, cụm cảm biến 11 kênh đọc ổn định, khối lượng nhẹ. Thứ hai, hoàn thiện phần trợ lực: cơ cấu ba tang tạo được dạng kẹp ba chấu, trợ lực giảm dần theo đáp ứng của người tập, có đường thoát an toàn. Thứ ba, hoàn thiện phần đánh giá: bộ chỉ số EI, GAP, RAL và bộ chỉ số bài tập thìa, cùng quy trình kiểm soát chất lượng số liệu.

Cần nói rõ phạm vi của các mục tiêu này: đây là nguyên mẫu kỹ thuật được kiểm chứng trên thiết bị đo và mô hình bàn tay giả, không phải thiết bị y tế đã hoàn thiện để dùng cho người bệnh.

### 4. Tiêu chí của dự án

Các ngưỡng dưới đây là **mục tiêu thiết kế được chốt trước khi đo**, dùng làm căn cứ đánh giá nguyên mẫu trên băng thử và mô hình bàn tay giả; chúng chưa phải là kết quả đo đã đạt được.

- Quét đồng thời 11 kênh cảm biến với tốc độ khung không thấp hơn 20 Hz; đáp ứng trên tải chuẩn đạt tỷ số tín hiệu trên nhiễu không thấp hơn 18 dB và hệ số xác định R² không thấp hơn 0,90.
- Phân biệt đúng hướng vận động ở mức không thấp hơn 90%; phân loại đúng mức kích hoạt ở mức không thấp hơn 85%.
- Độ lặp lại của phép đo: hệ số biến thiên trong cùng một buổi tập không vượt quá 5%, giữa các ngày khác nhau không vượt quá 8%.
- Trễ đàn hồi của cảm biến không vượt quá 18%; độ dãn tải tĩnh sau 60 giây giữ tải không vượt quá 8%; nhiễu nền sau lọc không vượt quá 5 mV đỉnh – đỉnh.
- Trễ từ lúc cảm biến đọc được tín hiệu đến lúc phát lệnh servo không vượt quá 20 ms.
- Giới hạn an toàn của cơ cấu được đặt theo hành trình dây, góc kéo và chốt mở nhanh trên nẹp; **không** dùng ngưỡng lực suy ra từ cảm biến áp trở làm cơ chế an toàn, vì cảm biến áp trở không đo được lực tuyệt đối.
- Thời gian người tập tự đeo găng và tự tháo găng, cùng độ bền của khóa nẹp sau nhiều chu kỳ đóng mở: sẽ đo ở mốc 2.
- Tỷ lệ hoàn thành bài tập thìa và độ đúng của nhãn trạng thái từ camera: xác định sau lượt thử đầu trên mô hình bàn tay giả.

Hai điểm về an toàn cần được nói thẳng. Nguyên mẫu hiện chưa có điện trở shunt nên chưa giám sát được dòng điện của servo. Hộp số servo có tỉ số truyền lớn không cho phép quay ngược trục khi ngắt điện, vì vậy hành vi nhả dây lúc mất nguồn là đại lượng phải đo thực tế chứ không được giả định là "tự nhả". Đường thoát an toàn khi mất nguồn là chốt mở nhanh trên từng đốt nẹp để người tập tự tháo tay ra, và thời gian tháo sẽ được đo ở mốc 2.

### 5. Đối tượng và phạm vi nghiên cứu

- **Về con người:** tìm hiểu số liệu thống kê về đột quỵ và di chứng vận động bàn tay; tìm hiểu khó khăn của người tập trong sinh hoạt hằng ngày và những trở ngại khi tự tập tại nhà, làm cơ sở chọn bài tập gắp thìa làm đơn vị đánh giá.
- **Về lịch sử đề tài:** chín thế hệ khóa nẹp mà nhóm đã in thử và đeo thử, hai vòng lặp thiết kế mạch thu nhận đã đo kiểm, và các dự án găng tay phục hồi chức năng đã công bố.
- **Về giải pháp kỹ thuật:** cảm biến gập và cảm biến áp trở, mạch chuyển đổi tương tự – số, thuật toán lọc số, cơ cấu truyền động bằng dây cáp, nguyên lý trợ lực theo nhu cầu, xử lý ảnh để nhận biết vật dụng, lập trình vi điều khiển và in 3D.
- **Phạm vi:** đề tài dừng ở nguyên mẫu và kiểm chứng trên bàn thử cùng mô hình bàn tay giả. Việc thử có cấp nguồn trên người chỉ được xem xét với người trưởng thành khỏe mạnh, sau khi rà soát an toàn đạt và có phê duyệt, theo một quy trình riêng. **Đề tài không thử nghiệm trên người bệnh** và không đánh giá hiệu quả điều trị.

### 6. Địa điểm nghiên cứu và thực nghiệm

Phòng thực hành Vật lý và phòng sáng tạo của trường, cùng nhà riêng của các thành viên, được dùng để thảo luận ý tưởng, lựa chọn giải pháp, lập trình, in 3D, lắp ráp và vận hành thử nghiệm. Việc khảo sát thực tế về các loại găng hỗ trợ hiện có được thực hiện tại cơ sở phục hồi chức năng.

### 7. Phương pháp nghiên cứu

Trong quá trình thực hiện, nhóm nghiên cứu kết hợp nhiều phương pháp:

- **Phương pháp quan sát** được dùng để ghi nhận cách người yếu tay tự đeo và tháo nẹp, cách họ cầm thìa, từ đó xác định yêu cầu cho khóa nẹp và cho bài tập đánh giá.
- **Phương pháp suy luận logic và lý luận** giúp phát triển ý tưởng, lựa chọn giữa các phương án cảm biến và phương án truyền động, xây dựng thuật toán lọc tín hiệu và quy tắc chuyển chế độ trợ lực.
- **Phương pháp thực nghiệm đo lường** là phương pháp chủ đạo: mỗi phương án cơ khí và mỗi vòng lặp mạch đều được chế tạo thật rồi đo thật, so sánh với phương án trước, và ghi lại nguyên nhân khi kết quả không đạt.
- **Phương pháp thống kê** dùng để đánh giá độ tin cậy của phép đo thông qua hệ số biến thiên, sai số chuẩn của phép đo và ngưỡng khác biệt nhỏ nhất có ý nghĩa [7].
- **Phương pháp mô hình hóa** gồm thiết kế và in 3D khung nẹp, dựng mô hình bàn tay giả bằng silicone và giàn đo cơ học để tạo ra tải và chuyển động lặp lại được, thay cho việc phải thử trên người.

---

## B. GIẢI PHÁP VÀ THIẾT KẾ

### 1. Tổng quan đề tài

Hệ thống được tổ chức theo kiến trúc phân tán bốn tầng, mỗi tầng một nhiệm vụ rõ ràng.

**Tầng đeo** là phần tiếp xúc trực tiếp với tay người tập: khung nẹp ba ngón in 3D, trên đó gắn 3 cảm biến gập Flex và 6 ô áp trở Velostat bố trí thành từng cặp ở mặt lòng và mặt mu của ngón, cùng 2 ô tham chiếu không chịu tải.

**Tầng thu thập** đọc các cảm biến đó. Vì vi điều khiển không thể đọc cùng lúc nhiều kênh tương tự, nhóm dùng một bộ chuyển mạch CD74HC4067 để lần lượt nối từng cảm biến vào bộ chuyển đổi tương tự – số ADS1115 loại 16 bit có tầng khuếch đại lập trình được, rồi xử lý tín hiệu bằng thuật toán lọc số bốn bước trên vi điều khiển ESP32-S3.

**Tầng trợ lực** là cơ cấu trợ lực theo nhu cầu, truyền động bằng dây cáp cuốn trên ba tang riêng, mỗi ngón một tang, dẫn động bằng servo.

**Tầng tác vụ** chạy trên Orange Pi 5 Pro, dùng camera để nhận biết chiếc thìa và vùng đích, từ đó gán nhãn cho từng giai đoạn của bài tập và cung cấp phản hồi hình ảnh trực tiếp cho người tập.

Điểm khác biệt cốt lõi so với các găng kéo thụ động là hệ thống **chỉ trợ lực khi nỗ lực chủ động của người tập chưa đủ** để hoàn thành tầm vận động, và tự giảm trợ lực khi phát hiện người tập đã tự khởi xướng được chuyển động. Phản hồi thị giác đi kèm để người tập tự thấy nỗ lực của mình, tạo động lực chủ động vận động.

Một chu kỳ vận hành của hệ thống diễn ra như sau: quét 11 kênh cảm biến → lọc và chuẩn hóa tín hiệu → trích đặc trưng vận động → máy trạng thái chọn chế độ trợ lực → phát lệnh servo có giới hạn an toàn → nhận nhãn tác vụ từ camera → ghi toàn bộ vào nhật ký theo một dấu thời gian chung.

⟨HÌNH 1 — sơ đồ khối bốn tầng: cụm đeo → thu thập → trợ lực → tác vụ và phản hồi⟩

### 2. Bất cập của các giải pháp hiện tại và giải pháp mới tại đề tài

Việc theo dõi vận động bàn tay ngoài bệnh viện hiện gặp bốn rào cản kỹ thuật.

Thứ nhất, các thang đo lâm sàng như FMA-UE và ARAT có tính gián đoạn: vài tuần mới đánh giá một lần, phụ thuộc vào người khám, nên không thấy được tiến triển từng ngày.

Thứ hai, thiết bị đeo cổ tay Manumeter tuy đã được thử nghiệm lâm sàng nhưng chỉ đếm chuyển động thô, với 100 đến 200 lần dương tính giả mỗi giờ [7].

Thứ ba, điện cơ bề mặt sEMG cho thông tin tốt về hoạt động cơ nhưng chất lượng tín hiệu suy giảm rõ khi ra mồ hôi, và khó tách riêng từng nhóm cơ ở cẳng tay.

Thứ tư, găng tay robot thương mại chủ yếu kéo thụ động theo chu kỳ cố định. Nhận định này đến từ khảo sát thực tế của nhóm tại cơ sở phục hồi chức năng, chưa có nguồn y văn trực tiếp xác nhận. Ngoài ra, các hệ găng mềm đã công bố [9, 15] được đánh giá chủ yếu trên người khỏe mạnh và không lấy một bài tập vận động tinh với vật thật làm đơn vị đánh giá.

Giải pháp của đề tài nhắm vào đúng hai chỗ trống đó. Một là lấy **bài tập gắp thìa với vật thật** làm đơn vị đánh giá chức năng, thay vì đếm số lần chuyển động. Hai là dùng **cảm biến áp trở giá thành thấp** nhưng chỉ sử dụng kết quả dưới dạng **chỉ số tương đối trong cùng một người**, thay vì cố đo lực tuyệt đối theo đơn vị Newton [13, 14].

Về mặt kỹ thuật, bài toán khó nhất — phân xử xem chuyển động là do người tập hay do máy tạo ra — được giải ở mức tối giản bằng một cửa sổ thăm dò, nghĩa là tạm ngưng trợ lực trong một khoảng ngắn để xem người tập có tự vận động hay không, thay vì dùng các phương pháp phức tạp đòi hỏi cảm biến đắt tiền.

Toàn bộ quá trình kiểm định được đặt trên giàn đo cơ học và mô hình bàn tay giả, trước khi xét đến con người.

### 3. Thiết kế phần cứng

**Khung nẹp và khóa.** Khung nẹp in 3D ôm ba ngón cái – trỏ – giữa, có khớp rãnh trượt để bù chênh lệch chiều dài ngón giữa các người dùng. Khóa nẹp là phương án Mech 9, dạng ngàm xoay hai bản lề kép, được chọn vì người tập đóng mở được bằng một tay; phương án này đã in xong nhưng chưa bấm giờ nên thời gian tự đeo sẽ đo ở mốc 2.

**Khối lượng và bố trí.** Cụm đeo trên tay có khối lượng mục tiêu từ 80 đến 120 gam và hiện chưa được cân cho cấu hình ba tang. Bộ xử lý, pin và servo đặt ngoài tay để giảm khối lượng đeo.

**Bộ truyền trợ lực.** Servo cuốn dây câu cá trực tiếp lên ba tang riêng, mỗi ngón một tang. Chiều duỗi thực hiện bằng cách servo nhả dây chủ động; phương án này không dùng lò xo hồi vị, không dùng đàn hồi nối tiếp và không dùng khớp bốn khâu.

**Cấu hình cảm biến.** Cấu hình đã chọn gồm 11 kênh quét trên tổng số 16 kênh của bộ chuyển mạch CD74HC4067.

| Kênh | Phần tử | Vai trò |
|---|---|---|
| 3 | Cảm biến gập Flex ở ngón cái, trỏ, giữa | đo biến thiên gập – duỗi và tư thế từng ngón |
| 6 | Ô áp trở Velostat ghép thành cặp lòng – mu cho ba ngón | đo áp lực và tiếp xúc; phân biệt trường hợp "ép vào nẹp" (ô mặt mu tăng) với trường hợp "tiếp xúc vật" (ô mặt lòng tăng) |
| 2 | Ô tham chiếu REF_1 và REF_2, không chịu tải | theo dõi trôi nền và điều kiện môi trường như ẩm mồ hôi, tĩnh điện; dùng làm cổng kiểm soát chất lượng để loại phiên đo, không bù được hiện tượng dão tải của ngón vì ô tham chiếu không chịu tải |
| 1 | CH15 nối đất | mốc đo xuyên kênh |
| 4 | dự phòng | mở rộng khi cần thêm vị trí đo |

Velostat là tấm vật liệu dẫn điện giá thành thấp, thay đổi điện trở khi bị ép; ưu điểm là rẻ và dễ cắt theo hình dạng ngón tay, nhược điểm là có trễ đàn hồi và sai số lớn, từ 16 đến 48% toàn dải tùy theo mẫu và cách lắp [13, 14]. Vì vậy nhóm chỉ dùng nó để so sánh tương đối trong cùng một người, cùng một buổi và cùng một cách đeo, chứ không quy đổi ra lực.

**Mạch thu nhận.** Tín hiệu đi theo chuỗi: cầu phân áp → bộ chuyển mạch CD74HC4067 → bộ chuyển đổi ADS1115 (16 bit, giao tiếp I²C) → vi điều khiển ESP32-S3. Hệ thống không dùng tầng khuếch đại cố định, lý do được trình bày ở mục C.2.

**Ngân sách thời gian quét** (đây là tính toán, chưa đo thực tế): với thời gian chờ 300 µs, một lần đọc nháp và tốc độ lấy mẫu 860 mẫu mỗi giây, mỗi kênh mất 2,63 ms, tương đương khoảng 35 Hz cho toàn khung 11 kênh và khoảng 24 Hz nếu dùng đủ 16 kênh.

**Các thông số còn phải chốt** ở bước thiết kế chi tiết: vị trí lắp từng ô cảm biến, dải điện trở của Flex tại đúng vị trí lắp đó, điện trở phân áp, tốc độ khung thực tế; dùng một động cơ kéo cả ba tang hay ba động cơ riêng; đường kính tang, hành trình dây và vị trí neo; hành vi nhả dây khi mất nguồn, vốn là bài toán cơ khí chứ không xử lý bằng phần mềm; và phương pháp đo độ căng dây một cách độc lập.

⟨HÌNH 2 — khung nẹp Mech 9 và cơ cấu ba tang⟩

### 4. Xây dựng thuật toán lọc số bốn bước

Tín hiệu từ cảm biến áp trở vốn nhiễu và trôi theo nhiệt độ, độ ẩm, nên cần một chuỗi xử lý. Thuật toán gồm bốn bước.

**Bước một, loại bỏ mẫu nhiễm kênh cũ.** Sau khi chuyển sang kênh mới, hệ thống chờ 300 µs rồi đọc một lần và bỏ kết quả đó, sau đó mới lấy giá trị thật. Lý do là ADS1115 thuộc họ bộ chuyển đổi delta – sigma, nên lần chuyển đổi đầu tiên sau khi đổi kênh vẫn còn chứa mẫu của kênh cũ bên trong bộ lọc số; việc bỏ lần đọc đầu, cộng với thời gian chờ để mạch RC của nguồn tín hiệu xác lập, làm giảm hiện tượng bóng ma kênh. Bản thân con số 300 µs là tham số chưa đo và sẽ được xác định lại trên băng thử.

**Bước hai, theo dõi đường nền thích ứng.** Khi mức thay đổi điện áp còn nhỏ, tức không lớn hơn 180 mV, hệ thống coi đó là trôi nền chứ không phải vận động, và cập nhật đường nền theo công thức V_base[k] = 0,998·V_base[k−1] + 0,002·V_raw[k]. Cách làm này bù được trôi do nhiệt độ và độ ẩm tiếp xúc da.

**Bước ba, trừ vùng chết.** Tín hiệu sạch bằng 0 nếu mức thay đổi không vượt 180 mV, và bằng mức thay đổi trừ đi 180 mV trong trường hợp còn lại.

**Bước bốn, làm mượt.** Áp dụng bộ lọc hàm mũ với hệ số α = 0,20 để có tín hiệu đáp ứng cuối cùng. Mỗi kênh có một đường hiệu chuẩn riêng, lập trên băng thử với tải chuẩn đã biết, ghi lại ngày, nhiệt độ, cách lắp và số lần lặp.

Có ba giới hạn của chuỗi xử lý này phải nêu rõ. Thứ nhất, bước ba ghim đầu ra về 0 lúc nghỉ nhưng điều đó không có nghĩa nhiễu thô đã biến mất; nhiễu thô đo được ở mức 50 đến 135 mV, nên khi báo cáo về nhiễu phải kèm cả tín hiệu thô lẫn tín hiệu sau lọc. Thứ hai, tín hiệu sau lọc không phải là lực theo đơn vị Newton, vì Velostat có trễ đàn hồi và sai số lớn như đã nêu. Thứ ba, các hằng số 300 µs, 180 mV, 0,998 và 0,002, cùng α = 0,20, là tham số đang dùng chứ chưa được tối ưu một cách có hệ thống và chưa kiểm chứng trên nhiều mẫu cảm biến.

Riêng ngưỡng vùng chết 180 mV đang có vấn đề: nó **cao hơn** dải nhiễu nền đã ghi nhận được là 50 đến 135 mV, nên có nguy cơ triệt tiêu luôn tín hiệu nỗ lực sớm vốn có biên độ nhỏ của người tập yếu cơ, tức là làm hỏng chính phép đo mà đề tài cần thực hiện. Vì vậy ngưỡng này chưa được coi là đạt, sẽ phải xác định lại theo phân bố nhiễu đo trên từng kênh, và tín hiệu nỗ lực sớm phải được kiểm tra riêng xem có còn sống sót sau vùng chết hay không.

### 5. Xây dựng bộ chỉ số đánh giá EI – GAP – RAL

Bộ chỉ số gồm ba đại lượng chính và một nhóm chỉ số tác vụ.

**Chỉ số nỗ lực EI** là tích phân của đáp ứng tương đối trong pha người tập vận động chủ động, chuẩn hóa theo mức tham chiếu của chính buổi tập đó. Công thức cụ thể và cách chọn mức tham chiếu sẽ chốt sau lượt thử đầu. Chỉ số này không chuẩn hóa theo lực đặt trước, vì hệ cảm biến không đo được lực tuyệt đối.

**Độ thiếu hụt tầm vận động GAP** được tính bằng hiệu giữa tầm vận động thụ động và tầm vận động chủ động, tức GAP = PROM − AROM, tính theo độ. Phép đo dùng thước đo góc bên ngoài kết hợp với biên độ gập đọc từ cảm biến Flex đã hiệu chuẩn. Găng tay không có cảm biến góc tuyệt đối nên phần mềm không tự xuất ra góc theo độ; thước đo góc bên ngoài mới là nguồn tham chiếu. Chỉ số này mô tả mức yếu liệt chứ không phải một phép chẩn đoán.

**Mức trợ giúp cần thiết RAL** là mức trợ lực nhỏ nhất đủ để hoàn thành một chu kỳ gập – duỗi theo tiêu chí đặt trước; ngưỡng tỷ lệ hoàn thành sẽ chốt sau lượt thử đầu trên mô hình bàn tay giả.

**Chỉ số tác vụ** gồm tỷ lệ hoàn thành bài tập thìa, thời gian hoàn thành, số lần rơi thìa hoặc đặt sai vị trí, số lần hệ thống chuyển chế độ đúng và sai, và số sự kiện trợ lực sai pha.

Về kiểm soát chất lượng số liệu: mỗi buổi đo ghi lại mã băm của cấu hình vào phiếu buổi đo, nghĩa là đổi tham số thì đổi phiên bản; dữ liệu dùng để chỉnh tham số được tách riêng khỏi dữ liệu dùng để báo cáo, và phiên bản dữ liệu được khóa trước lượt đánh giá. Dữ liệu mô phỏng phải ghi rõ là mô phỏng và không đưa vào bảng kết quả đo. Chỉ số nào chưa đo được thì ghi là chưa đo được, không ước lượng. Độ tin cậy của từng chỉ số được đánh giá bằng hệ số biến thiên trong buổi và giữa các ngày, sai số chuẩn của phép đo và ngưỡng khác biệt nhỏ nhất có ý nghĩa [7].

### 6. Xây dựng hệ thống điều khiển trợ lực theo nhu cầu

Trong cơ chế trợ lực theo nhu cầu, vận động ngón luôn do người tập khởi xướng; bộ điều khiển chỉ bù đúng phần trợ lực còn thiếu dựa trên tín hiệu vận động và trạng thái của bài tập, chứ không đóng ngón tay lại hoàn toàn theo lệnh từ camera. Việc chuyển từ chế độ hỗ trợ gập – duỗi sang chế độ trợ lực theo nhu cầu diễn ra **tự động**, không cần kỹ thuật viên nhấn nút.

Điểm khó nhất của cơ chế này là phân biệt vận động do người tập khởi xướng với chuyển động do chính cơ cấu tạo ra. Nếu không phân biệt được, hệ thống sẽ tự thăng cấp chế độ cho một người tập không hề có vận động chủ động, và toàn bộ số liệu đánh giá trở nên vô nghĩa.

Phương pháp được chọn là tạm ngưng trợ lực trong một cửa sổ ngắn đã định trước, đo đáp ứng của người tập trong cửa sổ đó, rồi quyết định giữ nguyên hay thăng cấp chế độ. Độ dài cửa sổ, tần suất mở, tiêu chí nhận diện đáp ứng, hành vi khi không có đáp ứng và số lần lặp đều sẽ xác định bằng thực nghiệm, và bắt buộc phải rà soát an toàn trước mọi lần chạy có cấp nguồn. Phương pháp này có một hạn chế phải thừa nhận: nó không phát hiện được nỗ lực không tạo ra chuyển động.

Toàn bộ vận hành được tổ chức thành **ba pha** nối tiếp nhau, để hệ thống đơn giản và trả lời được câu hỏi chuyển pha dựa trên tín hiệu nào.

**Pha nghỉ** là trạng thái mặc định khi khởi động, đồng thời là trạng thái hệ thống trở về khi kết thúc buổi tập hoặc khi phát hiện sự cố: servo không tải, dây cáp ở vị trí nhả, người tập có thể rút tay ra.

**Pha đo nỗ lực** bắt đầu khi người tập vào tư thế sẵn sàng và hai ô tham chiếu ổn định. Ở pha này hệ thống xác định người tập có tự khởi xướng được vận động hay không, bằng cách mở một cửa sổ thăm dò: tạm ngưng trợ lực trong một khoảng ngắn định trước rồi quan sát đáp ứng.

**Pha kéo trợ lực** bắt đầu khi cửa sổ thăm dò không thấy vận động tự nguyện đủ để hoàn thành tầm vận động. Servo kéo theo biên độ đặt trước, và mức trợ lực giảm dần mỗi lần pha đo nỗ lực phát hiện người tập tự làm được. Bài tập gắp thìa nằm trong pha này, với nhãn trạng thái từ camera dùng để điều chỉnh trợ lực theo từng giai đoạn của tác vụ.

Mọi lỗi mà phần mềm phát hiện được, gồm mất phản hồi servo, mất đồng bộ dấu thời gian và vượt giới hạn hành trình, đều đưa hệ thống về pha nghỉ và ghi nhật ký. Nguyên mẫu chưa có điện trở shunt đo dòng, chưa có encoder góc và chưa có rơ-le ngắt nguồn, nên không có điều kiện chuyển pha nào dựa trên ba tín hiệu đó; an toàn khi mất nguồn dựa vào chốt chặn cơ khí và ngàm bẩy mở nẹp.

Trường hợp đeo nẹp lỏng hoặc ô tham chiếu trôi bất thường không được coi là một pha, mà là **cờ loại phiên đo**: hệ thống ngưng trợ lực, yêu cầu kiểm tra lại cách đeo, và phiên đó bị loại khỏi tập số liệu báo cáo kèm lý do cụ thể. Đây là chỗ duy nhất việc kiểm soát chất lượng buổi tập được khai báo.

### 7. Xây dựng nhánh thị giác và bài tập gắp thìa

Camera nhận biết chiếc thìa và vùng đích trong một bố trí cố định, rồi gán nhãn cho từng giai đoạn của bài tập: sẵn sàng, nắm thìa, nâng thìa, di chuyển, thành công, rơi thìa, đặt sai chỗ, hoặc không xác định. Nhãn này vừa dùng để tính chỉ số tác vụ vừa dùng để hiển thị phản hồi trực quan cho người tập. Nhánh thị giác không đo lực ngón tay và không xác nhận phục hồi lâm sàng.

Bộ nhận biết được thiết kế dạng cắm được: trước hết dùng xử lý ảnh cổ điển bằng thư viện OpenCV chạy trên Orange Pi 5 Pro, và chỉ thay bằng mô hình học sâu nếu kết quả đo thử trên đúng phần cứng đó không đạt yêu cầu. Nếu dùng phương pháp ước lượng độ sâu từ một ảnh thì phải hiệu chuẩn tỷ lệ trước khi coi tọa độ trên ảnh là tọa độ thực.

Các chỉ số của nhánh thị giác gồm độ đúng của nhãn, tỷ lệ nhãn không xác định, độ trễ đầu – cuối và số khung hình mỗi giây; tất cả sẽ đo ở mốc 3. Giao tiếp giữa Orange Pi 5 Pro và ESP32-S3 hiện chưa được tích hợp. Cần lưu ý rằng độ trễ đầu – cuối của nhánh thị giác không thể nhỏ hơn một chu kỳ phơi sáng của camera, mà ở tốc độ 30 khung hình mỗi giây thì chu kỳ đó đã là 33,3 ms; vì vậy chỉ tiêu trễ không vượt quá 20 ms chỉ áp dụng cho đường đi từ cảm biến đến lệnh servo, không áp dụng cho nhãn tác vụ.

Bài tập thìa cần một tờ yêu cầu tác vụ ghi rõ: loại thìa và khối lượng, kích thước và vị trí vùng đích, khoảng cách di chuyển, tiêu chí để coi là đặt thành công, thời gian tối đa cho một lượt và số lượt trong mỗi buổi tập. Các thông số này sẽ xác định khi đo trên vật thật.

⟨HÌNH 3 — bố trí bàn thử: camera, vùng đích và mô hình tay giả⟩

---

## C. CHẾ TẠO MÔ HÌNH VÀ VẬN HÀNH THỬ NGHIỆM

*Số liệu trong phần C được dùng theo ba mức: "đã đo, có biên bản" là số liệu chính thức; "ghi nhận sơ bộ" là quan sát trên bàn đo, chưa có biên bản; "mục tiêu" là ngưỡng dự kiến, chưa đo.*

### 1. Chế tạo và thử nghiệm chín thế hệ khóa nẹp

Khóa nẹp là chi tiết tưởng như đơn giản nhưng lại quyết định người tập có tự đeo được găng hay không. Nhóm đã in thử và đeo thử 9 phương án, chia theo ba nhóm nguyên lý.

Nhóm thứ nhất gồm Mech 1 đến Mech 3: vòng kẹp chữ C đàn hồi, rãnh trượt đuôi én và đai Velcro. Thời gian đeo kéo dài từ 55 đến 80 giây và cả ba đều không giữ được tiền tải, nghĩa là nẹp bị lỏng ra trong quá trình tập.

Nhóm thứ hai gồm Mech 4 đến Mech 6: chốt xuyên ngang, khóa gài mặt mu và thanh răng rút. Thời gian rút còn 40 đến 65 giây nhưng lại đòi hỏi phải dùng hai tay hoặc phải căn chỉnh rất chính xác, điều mà người yếu tay không làm được.

Nhóm thứ ba cho kết quả tốt hơn. Mech 8 dùng bản lề một trục kết hợp ngàm đàn hồi, đạt 28 giây nhưng bị lỗi bền mỏi, tức là gãy sau nhiều lần đóng mở. Mech 9 dùng khóa ngàm xoay hai bản lề kép và khắc phục được lỗi gãy đó, nên được chọn làm phương án triển khai; Mech 9 đã in xong nhưng chưa bấm giờ, vì vậy chưa có con số thời gian đeo nào cho phương án này.

| Phương án | Nguyên lý khóa | Thời gian tự đeo | Sau 50 chu kỳ đóng mở |
|---|---|---|---|
| Mech 1–3 | vòng kẹp chữ C; rãnh trượt đuôi én; đai Velcro | 55–80 giây | không đạt |
| Mech 4–6 | chốt xuyên ngang; khóa gài mặt mu; thanh răng rút | 40–65 giây | không đạt |
| Mech 7 | không có số liệu trong hồ sơ hiện tại của nhóm | chưa có | chưa có |
| Mech 8 | bản lề một trục kết hợp ngàm đàn hồi | 28 giây | lỗi bền mỏi |
| Mech 9 | khóa ngàm xoay hai bản lề kép | chưa bấm giờ | đã in, chưa đo độ bền; phương án được chọn |

Phải nói rõ giá trị của các con số này: chúng là ghi nhận sơ bộ khi đeo thử nội bộ, chưa có biên bản đo, chưa ghi ngày thử, số lần lặp, người thực hiện và loại đồng hồ bấm giờ, nên hiện chỉ dùng được để so sánh định tính giữa các phương án với nhau.

Thời gian tự đeo và độ bền mỏi của Mech 9 vì vậy là chỉ tiêu kiểm nghiệm của mốc 2, và Mech 9 được giới thiệu như một phương án hình học khắc phục lỗi gãy của Mech 8 chứ không kèm con số kết quả. Số chu kỳ đóng mở dùng cho phép đo bền sẽ chốt trong quy trình đo, vì 50 chu kỳ là con số rất nhỏ so với số lần đóng mở của một liệu trình kéo dài nhiều tuần.

⟨HÌNH 4 — ảnh các thế hệ khóa nẹp đã in thử⟩

### 2. Vận hành thử nghiệm mạch thu nhận qua hai vòng lặp thiết kế

**Vòng lặp thứ nhất** dùng tầng khuếch đại dụng cụ INA333 với hệ số khuếch đại khoảng 6,5. Khi đo với nguồn tín hiệu chuẩn thì ngõ ra rất sạch và các kênh cách ly tốt.

Nhưng khi lắp cảm biến thật vào và gài khóa tiền tải của nẹp, mạch bộc lộ vấn đề: cầu phân áp sụt xuống dưới 1,42 V và ngõ ra bão hòa cứng ở khoảng 2.838 mV, dải tuyến tính chỉ còn từ 1,44 đến 1,92 V, trong khi nhiễu nền lúc nghỉ lên tới 50 đến 135 mV.

Nguyên nhân được xác định là việc khuếch đại với hệ số cố định không phù hợp với trở kháng và dải điện trở biến thiên rất lớn của phần tử áp trở khi có tiền tải. Đây là một kết quả có giá trị, vì nó chỉ ra rằng vấn đề nằm ở kiến trúc chứ không phải ở linh kiện.

**Vòng lặp thứ hai** bỏ hẳn tầng INA333 và đọc trực tiếp qua tầng khuếch đại lập trình được của ADS1115, kết hợp chuỗi lọc số bốn bước. Vòng này giữ được trọn dải ngõ vào từ 0 đến 3.300 mV trên bàn đo, đồng thời thêm thao tác đọc nháp và chờ 300 µs sau khi chuyển kênh; vùng chết 180 mV giữ cho đường nền ổn định khi nghỉ.

| Hạng mục | Đã đo, có biên bản | Ghi nhận sơ bộ trên bàn đo | Mục tiêu, chưa đo |
|---|---|---|---|
| Kiến trúc ngõ vào | chưa có | bỏ INA333, đọc trực tiếp qua tầng khuếch đại của ADS1115, trọn dải 0–3.300 mV | thu trọn dải, không bão hòa ở tải thiết kế |
| Bão hòa ngõ ra | chưa có | vòng một: cầu phân áp dưới 1,42 V, bão hòa khoảng 2.838 mV, dải tuyến tính 1,44–1,92 V | không bão hòa ở cấu hình 11 kênh |
| Nhiễu nền lúc nghỉ | chưa có | nhiễu thô 50–135 mV; sau vùng chết 180 mV, đầu ra lúc nghỉ ghim về 0 | không vượt quá 5 mV đỉnh – đỉnh sau lọc, đo ít nhất 10 phiên |
| Xuyên kênh | chưa có | đọc nháp và chờ 300 µs làm giảm bóng ma kênh; CH15 dùng làm mốc | ngưỡng chưa xác định |
| Tỷ số tín hiệu trên nhiễu và độ tuyến tính | chưa có | chưa có ghi nhận đạt yêu cầu trên băng thử | không thấp hơn 18 dB; R² không thấp hơn 0,90 |
| Tốc độ khung | chưa có | vòng một khoảng 22 Hz với 16 kênh, trễ chuyển kênh khoảng 120 µs | không thấp hơn 20 Hz cho toàn khung; tính toán khoảng 35 Hz với 11 kênh |
| Trôi nền dài hạn | chưa có | chưa có chuỗi nhật ký dài ngày | nhật ký ít nhất 10 ngày với REF_1 và REF_2 |

Hai chỉ số về tỷ số tín hiệu trên nhiễu và độ tuyến tính sẽ được xác định bằng những buổi đo có biên bản trên băng thử, trong đó ghi rõ tải chuẩn, số lần lặp, điều kiện môi trường, kết quả kiểm tra kênh tham chiếu trước và sau phiên đo, cùng định nghĩa của phép tính: cửa sổ tín hiệu và cửa sổ nhiễu dùng cho tỷ số tín hiệu trên nhiễu, số điểm tải và phương pháp hồi quy dùng cho R².

⟨HÌNH 5 — đồ thị vòng lặp một với hiện tượng bão hòa và vòng lặp hai giữ trọn dải ngõ vào⟩

### 3. Kế hoạch kiểm định trên giàn đo và mô hình bàn tay giả

Phương tiện kiểm định gồm bốn thứ: giàn đo cơ học dùng trục trượt để tạo ra chuyển động gập – duỗi lặp lại theo biên độ và tốc độ đặt trước; các tải chuẩn có khối lượng đã biết, đặt đúng đường truyền lực của cơ cấu; mô hình bàn tay giả đúc bằng silicone; và thước đo góc dùng làm tham chiếu cho biên độ khớp cùng tầm vận động thụ động và chủ động.

Về tình trạng thiết bị hiện nay: tấm Velostat, băng đồng, vi điều khiển ESP32-S3, Orange Pi 5 Pro, đồng hồ đo, bộ tạo tín hiệu và bộ chuyển mạch CD74HC4067 đều đã có, trong đó CD74HC4067 đã được chạy thử. Ba cảm biến gập Flex chưa có và phải mua ở mốc 1, dù vẫn nằm trong cấu hình 11 kênh đã chọn. Giàn trục trượt, cảm biến lực, bộ khối lượng chuẩn và silicone để đúc mô hình tay giả thuộc nhóm phải chế tạo hoặc mua ở mốc 1. Tình trạng của bộ chuyển đổi ADS1115 chưa được xác nhận. Những gì đã đo kiểm đến nay là chạy thử mạch trên breadboard và đo bằng đồng hồ số; **chưa có buổi đo nào được thực hiện trên giàn cơ học**.

Toàn bộ kiểm định thực hiện trên bàn thử và mô hình bàn tay giả. Chỉ xem xét thử có cấp nguồn trên người trưởng thành khỏe mạnh sau khi rà soát an toàn đạt và có phê duyệt, theo một quy trình riêng; đề tài không thử trên người bệnh.

Tám quy trình đo đã được lập kế hoạch. Một là đo đáp ứng theo tải và độ tuyến tính, với tải tăng dần rồi giảm dần, lặp lại ít nhất ba lượt. Hai là đo trễ đàn hồi và độ dãn tải tĩnh, bằng cách so nhánh tăng tải với nhánh giảm tải và giữ tải không đổi trong 60 giây. Ba là đo độ lặp lại trong cùng buổi và giữa các ngày, trong cùng điều kiện và cùng cách lắp. Bốn là đo nhiễu nền và tỷ số tín hiệu trên nhiễu ở trạng thái nghỉ, báo cáo cả tín hiệu thô lẫn tín hiệu sau lọc.

Năm là đo xuyên kênh, bằng cách kích thích một kênh rồi đọc các kênh đang nghỉ, lấy CH15 làm mốc. Sáu là đo trôi nền bằng chuỗi nhật ký ít nhất 10 ngày với hai ô tham chiếu. Bảy là đo tốc độ khung và trễ biên, bằng cách đếm số hiệu khung và đo khoảng thời gian từ khung dữ liệu đến lúc lệnh servo thay đổi. Tám là đo cơ cấu ba tang trên mô hình bàn tay giả, gồm hành trình thực tế so với lệnh, dạng kẹp ba chấu, hành vi nhả dây khi cắt nguồn và độ căng dây đo bằng một phương pháp độc lập.

Mỗi phiên đo ghi lại ngày giờ, người vận hành, mã băm cấu hình, nhiệt độ và độ ẩm nếu có, cách lắp, số lần lặp, và kết quả kiểm tra kênh tham chiếu trước và sau phiên. Một phiên đo bị loại khi ô tham chiếu trôi vượt ngưỡng, khi mất đồng bộ dấu thời gian, hoặc khi có can thiệp vào cách đeo giữa phiên; phiên bị loại phải ghi rõ lý do.

| Chỉ số | Cách đo | Mục tiêu hoặc ngưỡng | Căn cứ để chốt |
|---|---|---|---|
| Tỷ lệ hoàn thành tác vụ; thời gian; số lần rơi hoặc đặt sai | nhãn camera và nhật ký trên đồng hồ thời gian chung | chưa xác định | lượt thử đầu trên mô hình bàn tay giả |
| Tỷ lệ nhãn không xác định; độ đúng của nhãn trạng thái | nhật ký nhãn; bảng nhầm lẫn so với nhãn thủ công | chưa xác định | đo thử nhánh thị giác trên Orange Pi 5 Pro |
| Độ trễ thị giác đầu – cuối | dấu thời gian ở hai đầu | chưa xác định | đo trên phần cứng thật |
| Tốc độ khung thu thập | đếm số hiệu khung | không thấp hơn 20 Hz, chưa đo | tính toán khoảng 35 Hz, cần đo thực tế |
| Trễ từ cảm biến đến lệnh servo | nhật ký đồng bộ | không vượt quá 20 ms, chưa đo | đo trên bàn thử |
| Chuyển chế độ đúng và sai; trợ lực sai pha | nhật ký chế độ và nhãn đối chiếu | chưa xác định | phương pháp cửa sổ thăm dò đã chọn, chưa kiểm chứng |
| Biên độ và độ lặp lại của chu kỳ gập – duỗi | nhật ký cảm biến Flex và thước đo góc | hệ số biến thiên không quá 5% trong buổi, không quá 8% giữa các ngày | mốc 1 |
| Trôi tín hiệu | nhật ký REF_1 và REF_2 | chưa xác định | mốc 1, chuỗi nhật ký ít nhất 10 ngày |
| Tỷ số tín hiệu trên nhiễu và độ tuyến tính trên băng thử | băng thử trục trượt và tải chuẩn | không thấp hơn 18 dB và R² không thấp hơn 0,90 | mốc 1, phải có biên bản đo |
| Trễ đàn hồi, độ dãn tải tĩnh, nhiễu nền | băng thử | trễ đàn hồi không quá 18%; dãn tải sau 60 giây không quá 8%; nhiễu không quá 5 mV đỉnh – đỉnh sau lọc | mốc 1 |
| Khối lượng cụm đeo | cân thật, ghi ngày | 80–120 gam, chưa cân cho cấu hình ba tang | cân sản phẩm hoàn chỉnh |
| Chi phí vật tư | bảng vật tư có ngày và báo giá | dự toán 1,0 đến 1,3 triệu đồng cho cụm đeo, khoảng 5,5 triệu đồng cho toàn hệ thống | kiểm toán bảng vật tư |

Phép so sánh tối thiểu khi tích hợp là đối chiếu trợ lực cố định với trợ lực theo nhu cầu tự động, trên cùng một mô hình bàn tay giả và trong điều kiện tương đương. Độ nhạy riêng của từng nguồn đo được đánh giá bằng cách tắt lần lượt từng nguồn: chỉ dùng cảm biến gập, chỉ dùng cảm biến áp trở, chỉ dùng camera, rồi dùng đủ cả ba. Phản hồi thị giác không được coi là bằng chứng cho sự cải thiện phục hồi.

### 4. Kế hoạch hoàn thiện và kết luận

**Kế hoạch triển khai** gồm năm giai đoạn. Mốc 0, khoảng 3 tuần: hoàn thiện tờ yêu cầu tác vụ, bản đồ kênh cảm biến, phiếu buổi đo, bản đặc tả máy trạng thái, và chạy chuỗi nhật ký trôi nền ít nhất 10 ngày. Mốc 1, khoảng 3 đến 4 tuần: hiệu chuẩn cảm biến gập và cảm biến áp trở trên băng thử, đo tỷ số tín hiệu trên nhiễu, độ tuyến tính, hệ số biến thiên, trễ đàn hồi và độ dãn tải tĩnh. Mốc 2, khoảng 3 đến 4 tuần: chạy cơ cấu ba tang trên mô hình bàn tay giả, đo hành trình, hành vi nhả dây khi mất nguồn và các giới hạn an toàn, xuất bản vẽ CAD và đo độ bền của khóa Mech 9. Mốc 3, khoảng 2 đến 3 tuần: nhánh thị giác và bài tập thìa, đo thử trên Orange Pi 5 Pro. Giai đoạn tích hợp, khoảng 2 tuần: chạy chu trình ba bước trên mô hình bàn tay giả và so sánh trợ lực cố định với trợ lực theo nhu cầu.

Chi phí vật tư cho cụm đeo được dự toán ở mức 1,0 đến 1,3 triệu đồng, và khoảng 5,5 triệu đồng cho toàn hệ thống cùng giàn thử nghiệm nếu tận dụng được thiết bị của phòng thí nghiệm. Đây là dự toán chưa kiểm toán và sẽ được lập thành bảng vật tư có ngày kèm báo giá.

Về khả năng hoàn thành: mốc 0, mốc 1, bản vẽ CAD, phép đo độ bền của Mech 9 và cụm ba tang chạy thử trên mô hình bàn tay giả nằm trong khả năng chắc chắn. Mốc 3 và giai đoạn tích hợp đầy đủ có rủi ro trễ tiến độ, vì nhánh thị giác chưa được đo thử và giao tiếp giữa hai bo mạch chưa tích hợp. Đề tài không cam kết hoàn thành chuỗi đánh giá trên người.

**Những việc đã làm:** in thử và so sánh 9 phương án khóa nẹp rồi chọn Mech 9; hoàn thành hai vòng lặp thiết kế mạch thu nhận, xác định được nguyên nhân bão hòa ngõ vào ở vòng một và chuyển sang đọc trực tiếp qua tầng khuếch đại của ADS1115; xác định chuỗi lọc số bốn bước cùng bộ tham số đang dùng; chốt cấu hình cảm biến 11 kênh quét và cơ cấu ba tang với chiều duỗi thực hiện bằng nhả dây chủ động; xây dựng định nghĩa của ba chỉ số EI, GAP và RAL cùng bảng tiêu chí kỹ thuật được chốt trước khi đo; đặc tả ba pha vận hành cùng phương pháp cửa sổ thăm dò. Toàn bộ các kết quả trên ở mức ghi nhận sơ bộ, chưa có biên bản đo.

**Những việc chưa làm:** mua ba cảm biến gập Flex; chế tạo cụm cảm biến theo cấu hình đã chọn; bấm giờ thời gian tự đeo của Mech 9; lập biên bản đo cho tỷ số tín hiệu trên nhiễu, độ tuyến tính, tốc độ khung và độ lặp lại; đo độ bền mỏi của Mech 9 theo quy trình; xuất và lưu bản vẽ CAD; cân khối lượng cụm đeo; kiểm toán chi phí; viết firmware và các mô-đun phần mềm của luồng xử lý; đo thử nhánh thị giác; kiểm chứng quy tắc cửa sổ thăm dò; và thử nghiệm trên người.

**Giới hạn của đề tài:** thử nghiệm trên bàn đo và mô hình bàn tay giả không chứng minh hiệu quả trên người, không chứng minh rằng an toàn đã được chứng nhận, và không chứng minh cải thiện chức năng sau đột quỵ. Dữ liệu thu trên người khỏe mạnh không thay thế được dữ liệu trên người bệnh. Đề tài cũng không tuyên bố tính mới hay tuyên bố "đầu tiên" cho tổ hợp gồm trợ lực theo nhu cầu, cảm biến áp trở Velostat, cảm biến gập, camera và bài tập gắp thìa; cảm biến áp trở chỉ cho chỉ số tương đối trong cùng một người, không dùng làm thiết bị đo lực và không dùng làm cơ chế an toàn.

⟨HÌNH 6 — nguyên mẫu găng tay và bàn thử nghiệm⟩

### 5. Hướng phát triển

- **Về phần cứng:** thay hệ dây dẫn rời bằng mạch in mềm đi chìm trong nẹp in 3D, để tăng độ bền cơ học, chống đứt gãy và tăng tính thẩm mỹ; mở rộng từ ba ngón lên năm ngón sau khi đã có dữ liệu hiệu chuẩn đủ tin cậy.
- **Về quy chuẩn y sinh và thử nghiệm lâm sàng:** sau khi hoàn tất các mốc kiểm định an toàn kỹ thuật trên giàn đo cơ học và mô hình bàn tay giả silicone, nhóm sẽ xây dựng hồ sơ xin phê duyệt của Hội đồng Đạo đức trong nghiên cứu y sinh học tại cơ sở y tế chuyên khoa, trước khi triển khai thử nghiệm đối chứng lâm sàng với thang đo FMA-UE và ARAT. Đây là giai đoạn sau và nằm ngoài phạm vi của đề tài này.
- **Về điều khiển:** cá nhân hóa ngưỡng trợ lực theo tầm vận động của từng người tập. Các phương pháp điều khiển thích ứng nâng cao, kể cả học máy, chỉ được xem xét khi đã có bộ dữ liệu bàn thử và mô hình bàn tay giả đủ lớn cùng bộ quy tắc an toàn đã khóa.

⟨HÌNH 7 — lộ trình năm giai đoạn từ mốc 0 đến tích hợp⟩

---

## TÀI LIỆU THAM KHẢO

[1] Tran et al. (2025), "Comprehensive analysis of stroke epidemiology in Vietnam: Insights from GBD 1990–2019 and RES-Q 2017–2023", *Global Epidemiology*, 9:100199.

[2] Bộ Y tế (2014), "Hướng dẫn chẩn đoán và điều trị Phục hồi chức năng sau đột quỵ não", Quyết định số 4039/QĐ-BYT.

[3] Cao Minh Châu, Nguyễn Thị Kim Liên, Trần Trọng Hải (2020), "Giáo trình Phục hồi chức năng", Nhà xuất bản Y học, Hà Nội.

[4] Gordon E. M., et al. (2023), "A somato-cognitive action network alternates with effector regions in motor cortex", *Nature*, 617(7960), 351–359.

[5] Pollock A., et al. (2014), "Interventions for improving upper limb function after stroke", *Cochrane Database of Systematic Reviews*, CD010820.

[6] Langhorne P., Coupar F., Pollock A. (2009), "Motor recovery after stroke: a systematic review", *The Lancet Neurology*, 8(8), 741–754.

[7] Schwerz de Lucena D., et al. (2022), "Providing Real-Time Wearable Feedback to Increase Hand Use after Stroke: A Randomized Controlled Trial (Manumeter)", *Sensors*, 22(18):6938.

[8] Amin F., et al. (2024), "Remote Monitoring for the Management of Spasticity: Challenges, Opportunities and Proposed Technological Solution", *Sensors*, PMC11793859.

[9] Li M., et al. (2024), "A magnetically controlled soft robotic glove for hand rehabilitation", *Device*, 2(4):100215.

[10] Lin B. S., et al. (2022), "Design of a Multi-Sensor System for Exploring Upper Limb Spasticity in Stroke Patients", *Sensors*, 22(19):7212.

[11] Penfield W., Boldrey E. (1937), "Somatic motor and sensory representation in the cerebral cortex of man as studied by electrical stimulation", *Brain*, 60, 389–440.

[12] Hebb D. O. (1949), "The Organization of Behavior: A Neuropsychological Theory", New York: Wiley.

[13] Hopkins M., Vaidyanathan R., McGregor A. H. (2020), "Examination of the Performance Characteristics of Velostat as an In-Socket Pressure Sensing Material", *IEEE Sensors Journal*, 20(12).

[14] Blin J., et al. (2022), "Evaluation of the Foot Center of Pressure Estimation from Pressure Insoles during Gait", *Sensors*, 22(15):5628.

[15] Radder B., et al. (2018), "Home-based robot-assisted arm training with an interactive robotic glove after stroke (IRONHAND)", *Journal of Rehabilitation Medicine*, 50, 598–606.
