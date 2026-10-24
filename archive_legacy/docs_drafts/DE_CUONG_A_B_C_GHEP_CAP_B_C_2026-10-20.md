# ĐỀ CƯƠNG DỰ ÁN KHOA HỌC KỸ THUẬT

**Tên dự án:** *Nghiên cứu và phát triển găng tay hỗ trợ phục hồi chức năng sau đột quỵ cho vận động tinh.*

Lĩnh vực: ⟨…⟩ · Đơn vị: ⟨…⟩ · Thành viên: ⟨…⟩ · Người hướng dẫn: ⟨…⟩

---

## A. VẤN ĐỀ NGHIÊN CỨU

### 1. Lý do chọn đề tài

Đột quỵ là một trong những nguyên nhân hàng đầu gây tàn tật ở Việt Nam. Tỷ lệ hiện mắc năm 2019 vào khoảng 1.541 ca trên 100.000 dân, và mỗi năm có thêm khoảng 222 ca mới trên 100.000 dân [1].

Điều đáng nói là sống sót sau đột quỵ chưa phải là hết vấn đề. Tổng quan của Cochrane ghi nhận khoảng 80% người sống sót bị suy giảm vận động, và trong nhóm liệt hoàn toàn chi trên thì chỉ khoảng một nửa phục hồi được một phần chức năng sau 6 tháng [5, 6]. Bàn tay là bộ phận hồi phục chậm nhất và khó nhất, vì tay phải thực hiện được các động tác tinh như cầm thìa, cài cúc áo, cầm bút chứ không chỉ co duỗi.

Vấn đề nằm ở chỗ quá trình tập luyện đó gần như không được đo lường. Người bệnh xuất viện về nhà và tự tập, trong khi việc theo dõi ngoại viện hiện thiếu một công cụ định lượng ổn định. Các thang đo lâm sàng như FMA-UE hay ARAT thì gián đoạn, vài tuần mới đánh giá một lần và phụ thuộc người khám. Thiết bị đeo cổ tay Manumeter đã được thử nghiệm lâm sàng, nhưng để phát hiện được tiến triển thì người đeo phải thay đổi tới khoảng 31% cường độ sử dụng trong ngày, đồng thời thiết bị đếm sai từ 100 đến 200 lần dương tính giả mỗi giờ [7]. Nói cách khác, công cụ hiện có hoặc là quá thưa, hoặc là quá ồn.

⟨HÌNH 1 — biểu đồ tỷ lệ đột quỵ tại Việt Nam và di chứng bàn tay kéo dài⟩

Khảo sát của nhóm tại cơ sở phục hồi chức năng vào tháng 9 năm 2026 cũng ghi nhận các loại găng hỗ trợ đang có trên thị trường chưa phù hợp với điều kiện tập tại nhà ở Việt Nam: giá thành cao, khối lượng nặng và thao tác đeo phức tạp.

Hai kịch bản thường gặp khi không có công cụ theo dõi. Kịch bản thứ nhất là không can thiệp sớm: nguy cơ là một chuỗi tiến triển gồm teo cơ do bất động, xơ hóa mô kẽ, mất cân bằng giữa nhóm cơ gập và nhóm cơ duỗi, rồi co rút và dính khớp; đi kèm là hiện tượng vùng biểu diễn bàn tay trên vỏ não bị các vùng lân cận lấn chiếm. Kịch bản thứ hai là chỉ có máy kéo thụ động: kéo thụ động nhịp nhàng có tác dụng ngắn hạn lên trương lực cơ nên không thể coi là vô dụng, nhưng nó không biến tầm vận động thụ động thành tầm vận động chủ động, và không cho kỹ thuật viên biết người tập tự làm được bao nhiêu phần so với tầm thụ động.

Đúng khoảng trống giữa hai kịch bản đó là chỗ đề tài đặt vào: đo được người tập tự làm bao nhiêu, và chỉ bù phần còn thiếu.

Từ những thực tế trên, nhóm nghiên cứu chọn chế tạo một chiếc găng tay nẹp ba ngón hỗ trợ người tập đi từ vận động gập – duỗi cơ bản đến thao tác **gắp thìa bằng ngón cái, trỏ và giữa**. Định hướng này khác với hai hướng phổ biến: không chỉ đếm chuyển động rồi báo cáo, và cũng không kéo tay người tập một cách thụ động theo chu kỳ định sẵn.

### 2. Xác định vấn đề nghiên cứu

Vấn đề nghiên cứu được phát biểu như sau: liệu một mảng cảm biến gập và cảm biến áp trở đặt trên khung nẹp ba ngón có tạo được tín hiệu đủ ổn định và đủ lặp lại để phát hiện vận động chủ động của người tập hay không, và liệu cơ cấu servo – dây cáp – ba tang có tạo được dạng kẹp ba chấu với mức trợ lực tự giảm dần hay không.

Cụ thể, nhóm nghiên cứu tập trung vào sáu nội dung:

- Nghiên cứu chế tạo khung nẹp ba ngón tích hợp 3 cảm biến gập Flex và 6 ô áp trở Velostat bố trí theo cặp lòng – mu, để vừa đọc được tư thế ngón vừa đọc được lực ép.
- Nghiên cứu mạch thu nhận tín hiệu và thuật toán lọc số, để tín hiệu từ cảm biến giá rẻ đủ sạch và đủ nhanh dùng cho điều khiển thời gian thực.
- Nghiên cứu xây dựng bộ chỉ số đánh giá tiến triển gồm EI, GAP và RAL, cùng các chỉ số của bài tập gắp thìa, để việc tập luyện có thể theo dõi bằng số.
- Nghiên cứu thiết kế cơ cấu trợ lực ba tang với duỗi chủ động bằng nhả dây, để găng tay hỗ trợ được cả hai chiều gập và duỗi.
- Nghiên cứu quy tắc tự động chuyển pha trợ lực và nhánh thị giác nhận biết bài tập thìa, để hệ thống tự nhận ra khi nào người tập đã tự làm được.
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
- **Phương pháp suy luận logic và lý luận** giúp phát triển ý tưởng, lựa chọn giữa các phương án cảm biến và phương án truyền động, xây dựng thuật toán lọc tín hiệu và quy tắc chuyển pha trợ lực.
- **Phương pháp thực nghiệm đo lường** là phương pháp chủ đạo: mỗi phương án cơ khí và mỗi vòng lặp mạch đều được chế tạo thật rồi đo thật, so sánh với phương án trước, và ghi lại nguyên nhân khi kết quả không đạt.
- **Phương pháp thống kê** dùng để đánh giá độ tin cậy của phép đo thông qua hệ số biến thiên, sai số chuẩn của phép đo và ngưỡng khác biệt nhỏ nhất có ý nghĩa [7].
- **Phương pháp mô hình hóa** gồm thiết kế và in 3D khung nẹp, dựng mô hình bàn tay giả bằng silicone và giàn đo cơ học để tạo ra tải và chuyển động lặp lại được, thay cho việc phải thử trên người.

---

## B. GIẢI PHÁP VÀ THIẾT KẾ

### 1. Tổng quan đề tài và cơ sở lý thuyết

Bàn tay chiếm diện tích đại diện vận động rất lớn trên vỏ não theo Penfield & Boldrey [11] và mạng SCAN của Gordon et al. [4]; đó là cơ sở để đề tài tập trung vào ba ngón trụ cột cái, trỏ, giữa thay vì làm cả năm ngón.

Theo học thuyết Hebb [12] và nguyên lý phục hồi chức năng [2, 3], phản hồi cảm giác đồng thời với nỗ lực vận động giúp định hướng tập luyện. Đề tài khai thác cơ sở này để xây dựng phản hồi thị giác thời gian thực, cho người tập tự quan sát nỗ lực phát lực đọc từ đáp ứng áp trở vi mô.

Các chế độ tập trong phục hồi chức năng bàn tay được phân biệt bằng một câu hỏi duy nhất: ai tạo ra chuyển động.

| Chế độ tập | Ai tạo chuyển động | Ý nghĩa với hệ thần kinh |
|---|---|---|
| Thụ động | ngoại lực, từ người khác hoặc từ máy; người tập không cần phát lệnh | duy trì tầm vận động thụ động và tình trạng mô mềm; tác động lên trung ương kém hơn |
| Chủ động có trợ lực | người tập phát lệnh và phát lực, thiết bị chỉ bù phần còn thiếu | vừa có lệnh vận động đi ra, vừa có cảm giác bản thể dội về trong cùng một khoảnh khắc |
| Chủ động kháng lực | người tập thắng thêm tải ngoài | giai đoạn sau, không thuộc phạm vi đề tài |

Tập thụ động giữ được tầm vận động thụ động, nghĩa là khớp không bị dính. Mục tiêu của phục hồi chức năng bàn tay là chuyển tầm vận động thụ động thành tầm vận động chủ động, tức người tập tự làm được động tác. Khoảng cách giữa hai đại lượng đó chính là chỉ số GAP mà đề tài đo, còn phần lực còn thiếu mà cơ cấu phải bù chính là mức trợ giúp cần thiết RAL.

⟨HÌNH 2 — bản đồ Homunculus [11] và sự phân bổ chi phối bàn tay [4]⟩

Sau đột quỵ, suy giảm vận động thường kết hợp giữa yếu cơ và tăng trương lực co cứng [8, 10], nên đề tài khảo sát độ thiếu hụt tầm vận động GAP, tức hiệu giữa tầm vận động thụ động PROM và tầm vận động chủ động AROM, như một chỉ số mô tả mức chênh lệch góc, đo bằng thước đo góc bên ngoài. Độ tin cậy của hệ đo đánh giá qua hệ số biến thiên, sai số chuẩn và ngưỡng khác biệt nhỏ nhất có ý nghĩa [7], làm căn cứ bố trí hai ô tham chiếu và đặt tiêu chí kỹ thuật trước khi đo.

Chuỗi sự kiện làm cơ sở cho việc chọn chỉ số đo diễn ra như sau: ý định vận động hình thành ở vỏ não vận động, xung ly tâm truyền xuống tủy sống rồi đến đơn vị vận động, cơ ngón co một phần và tạo ra tín hiệu mà cảm biến áp trở ghi được, ngón cử động thật nhờ phần lực còn thiếu được bù thêm, và cuối cùng các thụ thể bản thể ở thoi cơ, gân và bao khớp phát xung hướng tâm về vỏ não cảm giác.

Theo nguyên lý Hebb, sự tái tổ chức khớp nối thần kinh xảy ra khi tín hiệu lệnh và tín hiệu phản hồi đến đồng thời; chế độ chủ động có trợ lực tạo đúng điều kiện đồng thời đó, còn tập thụ động chỉ có nửa sau của vòng. Nếu lệnh phát ra mà chi thể không đáp ứng, lặp đi lặp lại, thì vùng biểu diễn có xu hướng co lại và bị chức năng lân cận lấn chiếm, gọi là hiện tượng bất hoạt do học được.

Đây là lý do đề tài phải phát hiện được **nỗ lực** chứ không chỉ phát hiện được chuyển động hoàn chỉnh: một người yếu cơ có thể phát lệnh mà ngón chưa kịp dịch chuyển, và nếu hệ thống chỉ đếm chuyển động thì nỗ lực đó không được ghi nhận. Chỉ số EI được đặt ra để đo đúng phần này.

Giới hạn trung thực: đề tài không đo hoạt động vỏ não, không dùng điện não đồ hay kích thích từ xuyên sọ; toàn bộ chuỗi lập luận trên là cơ sở lý thuyết để chọn chỉ số đo, không phải kết quả thực nghiệm của đề tài.

Hệ thống được tổ chức theo kiến trúc phân tán bốn tầng. Tầng đeo là khung nẹp ba ngón in 3D, tích hợp 3 cảm biến gập Flex, 6 ô áp trở Velostat bố trí thành cặp ở mặt lòng và mặt mu của ngón, cùng 2 ô tham chiếu không chịu tải. Tầng thu thập đọc các cảm biến đó qua bộ chuyển mạch CD74HC4067 và bộ chuyển đổi tương tự – số ADS1115 loại 16 bit có tầng khuếch đại lập trình được, rồi xử lý bằng thuật toán lọc số bốn bước trên vi điều khiển ESP32-S3. Tầng trợ lực là cơ cấu trợ lực theo nhu cầu truyền động bằng dây cáp cuốn trên ba tang riêng. Tầng tác vụ chạy trên Orange Pi 5 Pro, dùng camera nhận biết thìa và vùng đích, trích xuất bộ chỉ số tiến triển và hiển thị phản hồi cho người tập.

Điểm khác biệt cốt lõi so với găng kéo thụ động là hệ thống chỉ trợ lực khi nỗ lực chủ động chưa đủ hoàn thành tầm vận động, và tự giảm trợ lực khi phát hiện người tập đã tự khởi xướng chuyển động. Một chu kỳ vận hành gồm: quét 11 kênh, lọc và chuẩn hóa, trích đặc trưng vận động, chọn pha trợ lực, phát lệnh servo có giới hạn, nhận nhãn tác vụ từ camera, rồi ghi nhật ký theo một dấu thời gian chung.

⟨HÌNH 3 — sơ đồ khối bốn tầng: cụm đeo → thu thập → trợ lực → tác vụ và phản hồi⟩

### 2. Bất cập của các giải pháp hiện tại và hướng tiếp cận của đề tài

Việc theo dõi vận động bàn tay ngoài bệnh viện hiện gặp bốn rào cản: thang đo lâm sàng FMA-UE và ARAT gián đoạn, hai đến bốn tuần một lần và phụ thuộc người khám; thiết bị đeo cổ tay Manumeter chỉ đếm chuyển động thô với 100–200 lần dương tính giả mỗi giờ [7]; điện cơ bề mặt sEMG suy giảm chất lượng rõ khi ra mồ hôi và khó tách riêng từng nhóm cơ cẳng tay; găng tay robot thương mại chủ yếu kéo thụ động cố định theo chu kỳ, nhận định từ khảo sát của nhóm tại cơ sở phục hồi chức năng.

Ngoài ra, các hệ găng mềm đã công bố [9, 15] được đánh giá chủ yếu trên người khỏe mạnh và không lấy một bài tập vận động tinh với vật thật làm đơn vị đánh giá.

Hướng tiếp cận của đề tài nhắm vào đúng hai chỗ trống đó: lấy **bài tập gắp thìa với vật thật** làm đơn vị đánh giá chức năng thay vì đếm số lần chuyển động, và dùng **cảm biến áp trở giá thành thấp** nhưng chỉ sử dụng kết quả dưới dạng **chỉ số tương đối trong cùng một người** thay vì cố đo lực tuyệt đối [13, 14].

Bài toán phân xử chuyển động do người tập hay do máy tạo ra được giải ở mức tối giản bằng một cửa sổ thăm dò ngắn (mục B.7). Toàn bộ kiểm định đặt trên giàn đo cơ học và mô hình bàn tay giả trước khi xét đến con người.

### 3. Khung nẹp ngón tay và khóa đeo

Đối tượng này chịu hai yêu cầu trái ngược: phải đủ cứng để làm vách cho cảm biến áp trở và làm điểm neo cho dây cáp, nhưng phải đủ nhẹ và dễ thao tác để người yếu tay tự đeo được bằng một tay.

Khung nẹp in 3D ôm ba ngón cái – trỏ – giữa, có khớp rãnh trượt để bù chênh lệch chiều dài ngón giữa các người dùng. Khóa nẹp là phương án 9 dạng ngàm xoay hai bản lề kép, chọn vì người tập đóng mở được bằng một tay. Phương án này đã in xong, thời gian tự đeo sẽ đo ở mốc 2.

Cụm đeo có khối lượng mục tiêu 80–120 gam, sẽ cân khi lắp đủ ba tang; bộ xử lý, pin và servo đặt ngoài tay để giảm khối lượng đeo. Trên mỗi đốt nẹp có chốt mở nhanh, là đường thoát an toàn để người tập tự tháo tay ra khi cần.

Thiết kế chi tiết sẽ xác định vị trí lắp từng ô cảm biến, vật liệu và độ dày vách nẹp, lực tiền tải của khóa và vị trí neo dây.

⟨HÌNH 4 — khung nẹp phương án 9 và cơ cấu ba tang⟩

*Kiểm tra và kiểm thử tương ứng: mục C.1.*

### 4. Màng cảm biến áp lực và cảm biến gập

**Cơ sở lý thuyết.** Velostat là tấm vật liệu dẫn điện giá thấp, thay đổi điện trở khi bị ép; hiện tượng này là áp trở, không phải áp điện, nên tín hiệu phụ thuộc vào cả lực ép lẫn diện tích tiếp xúc. Ưu điểm là rẻ và dễ cắt theo hình ngón tay, nhược điểm là trễ đàn hồi và sai số từ 16 đến 48% toàn dải tùy mẫu và cách lắp [13, 14]. Vì vậy nhóm chỉ dùng nó để so sánh tương đối trong cùng một người, cùng buổi và cùng cách đeo, không quy đổi ra lực theo đơn vị Newton.

Cảm biến gập Flex thay đổi điện trở theo góc uốn, dùng để đọc biến thiên gập – duỗi và tư thế từng ngón; đây là đại lượng trong găng duy nhất phục vụ chỉ số GAP, nên cần hiệu chuẩn với thước đo góc bên ngoài.

**Thiết kế.** Mỗi ngón được bố trí một cặp ô Velostat ở mặt lòng và mặt mu. Cách bố trí vi sai này cho phép phân biệt trường hợp ép vào nẹp, khi ô mặt mu tăng, với trường hợp tiếp xúc vật, khi ô mặt lòng tăng; nếu chỉ có một ô thì hai trường hợp đó cho cùng một tín hiệu.

Cấu hình cảm biến đã chọn gồm 11 kênh quét trên tổng số 16 kênh của bộ chuyển mạch.

| Kênh | Phần tử | Vai trò |
|---|---|---|
| 3 | Cảm biến gập Flex ở ngón cái, trỏ, giữa | đo biến thiên gập – duỗi và tư thế từng ngón |
| 6 | Ô áp trở Velostat ghép cặp lòng – mu cho ba ngón | đo áp lực và tiếp xúc; phân biệt trường hợp ép vào nẹp (ô mặt mu tăng) với trường hợp tiếp xúc vật (ô mặt lòng tăng) |
| 2 | Ô tham chiếu hai ô tham chiếu không chịu tải | theo dõi trôi nền và điều kiện môi trường như ẩm mồ hôi, tĩnh điện; dùng để loại phiên đo khi trôi nền bất thường; không bù được hiện tượng dão tải của ngón vì ô tham chiếu không chịu tải |
| 1 | Kênh 15 nối đất | mốc đo xuyên kênh |
| 4 | dự phòng | mở rộng khi cần thêm vị trí đo |

Hai ô tham chiếu trôi theo cùng điều kiện môi trường như các ô đo, nên phần trôi chung đọc được trên ô tham chiếu là dấu hiệu để nghi ngờ một phiên đo, chứ không dùng để hiệu chỉnh số đo của ngón.

Ba cảm biến gập Flex sẽ mua ở mốc 1. Bước thiết kế chi tiết sẽ xác định dải điện trở của Flex tại đúng vị trí lắp, điện trở phân áp cho từng ô, cùng kích thước và lực tiền tải của ô Velostat.

*Kiểm tra và kiểm thử tương ứng: mục C.2.*

### 5. Mạch thu nhận và thuật toán xử lý tín hiệu

**Cơ sở lý thuyết.** Tín hiệu cần đọc là điện áp trên cầu phân áp, thay đổi theo điện trở cảm biến. Bộ chuyển đổi ADS1115 thuộc họ delta – sigma, nghĩa là nó lấy mẫu rất nhanh rồi lọc số để suy ra giá trị, khác với họ chuyển đổi xấp xỉ liên tiếp; hệ quả thực tế là lần chuyển đổi đầu tiên sau khi đổi kênh vẫn còn chứa mẫu của kênh cũ bên trong bộ lọc số. Bộ chuyển mạch CD74HC4067 nối lần lượt từng cảm biến vào bộ chuyển đổi, nên mỗi lượt chuyển kênh đều phát sinh bóng ma kênh và cần thời gian để mạch RC của nguồn tín hiệu xác lập.

**Thiết kế.** Tín hiệu đi theo chuỗi: cầu phân áp, bộ chuyển mạch CD74HC4067, bộ chuyển đổi ADS1115 giao tiếp I²C, rồi đến vi điều khiển ESP32-S3; hệ thống không dùng tầng khuếch đại cố định, lý do nêu ở mục C.3.

Thuật toán xử lý gồm bốn bước. Bước thứ nhất loại bỏ mẫu nhiễm kênh cũ: sau khi chuyển kênh, hệ thống chờ một khoảng ngắn rồi đọc một lần và bỏ kết quả đó, sau đó mới lấy giá trị thật. Bước thứ hai theo dõi đường nền thích ứng: khi mức thay đổi điện áp còn nhỏ thì coi đó là trôi nền chứ không phải vận động, và cập nhật đường nền rất chậm để bù trôi do nhiệt độ và độ ẩm tiếp xúc da. Bước thứ ba trừ vùng chết, chỉ giữ lại phần thay đổi vượt ngưỡng. Bước thứ tư làm mượt bằng bộ lọc hàm mũ. Mỗi kênh có một đường hiệu chuẩn riêng, lập trên băng thử với tải chuẩn đã biết, ghi lại ngày, nhiệt độ, cách lắp và số lần lặp.

Về thời gian quét, mỗi kênh mất khoảng 2,6 ms nên 11 kênh cho khoảng 35 khung hình mỗi giây và 16 kênh cho khoảng 24 khung hình mỗi giây; con số này là tính toán, sẽ đo lại trên mạch thật.

Bộ tham số đang dùng liệt kê ở bảng dưới đây; các hệ số chưa được tối ưu có hệ thống.

| Tham số | Giá trị đang dùng | Ghi chú |
|---|---|---|
| Thời gian chờ sau khi chuyển kênh | 300 µs | sẽ xác định lại trên băng thử |
| Số lần đọc nháp rồi bỏ | 1 lần mỗi lượt chuyển kênh | giữ nguyên theo kiến trúc delta – sigma |
| Tốc độ lấy mẫu của bộ chuyển đổi | 860 mẫu mỗi giây | theo cấu hình đang dùng |
| Ngưỡng cập nhật đường nền và vùng chết | 180 mV | **chưa đạt**: cao hơn dải nhiễu nền đã ghi nhận 50–135 mV |
| Hệ số cập nhật đường nền | 0,998 phần cũ cộng 0,002 phần mới | chưa tối ưu |
| Hệ số làm mượt hàm mũ | α = 0,20 | chưa tối ưu |

Trừ vùng chết ghim đầu ra về 0 lúc nghỉ nhưng nhiễu thô vẫn còn, đo được 50–135 mV, nên khi báo cáo nhiễu phải kèm cả tín hiệu thô lẫn sau lọc. Ngưỡng vùng chết 180 mV hiện cao hơn dải nhiễu nền đó và có thể triệt tiêu tín hiệu nỗ lực sớm biên độ nhỏ của người tập yếu cơ, nên sẽ xác định lại từ dữ liệu đo ở mục C.2.

*Kiểm tra và kiểm thử tương ứng: mục C.3.*

### 6. Bộ chỉ số đánh giá tiến triển và kiểm soát chất lượng số liệu

**Cơ sở lý thuyết.** Một chỉ số dùng để theo dõi tiến triển phải phân biệt được thay đổi thật của người tập với thay đổi của phép đo; vì vậy đề tài dùng bộ ba đại lượng đo lường đã được kiểm chứng trong nghiên cứu phục hồi chức năng là hệ số biến thiên, sai số chuẩn của phép đo và ngưỡng khác biệt nhỏ nhất có ý nghĩa [7].

**Thiết kế.** Chỉ số nỗ lực EI là tích phân của đáp ứng tương đối trong pha người tập vận động chủ động, chuẩn hóa theo mức tham chiếu của chính buổi tập đó; công thức cụ thể và cách chọn mức tham chiếu xác định sau lượt thử đầu. Chỉ số này không chuẩn hóa theo lực đặt trước, vì hệ cảm biến không đo được lực tuyệt đối.

Độ thiếu hụt tầm vận động GAP là hiệu giữa tầm vận động thụ động và tầm vận động chủ động, tính theo độ, đo bằng thước đo góc bên ngoài kết hợp với biên độ gập đọc từ cảm biến Flex đã hiệu chuẩn. Găng tay không có cảm biến góc tuyệt đối, nên thước đo góc bên ngoài là nguồn tham chiếu cho chỉ số này.

Mức trợ giúp cần thiết RAL là mức trợ lực nhỏ nhất đủ để hoàn thành một chu kỳ gập – duỗi theo tiêu chí đặt trước; ngưỡng tỷ lệ hoàn thành xác định sau lượt thử đầu trên mô hình bàn tay giả. Nhóm chỉ số của bài tập gồm tỷ lệ hoàn thành bài tập thìa, thời gian hoàn thành, số lần rơi thìa hoặc đặt sai vị trí, số lần chuyển pha đúng và sai, cùng số sự kiện trợ lực sai pha.

Về kiểm soát chất lượng số liệu, mỗi buổi đo ghi phiên bản cấu hình vào phiếu buổi đo, đổi tham số thì đổi phiên bản; dữ liệu dùng để chỉnh tham số tách riêng khỏi dữ liệu dùng để báo cáo, và dữ liệu báo cáo được cố định trước lượt đánh giá. Dữ liệu mô phỏng ghi rõ là mô phỏng và không đưa vào bảng kết quả đo.

*Kiểm tra và kiểm thử tương ứng: mục C.4.*

### 7. Cơ cấu trợ lực và ba pha vận hành

**Cơ sở lý thuyết.** Trong cơ chế trợ lực theo nhu cầu, vận động ngón luôn do người tập khởi xướng; bộ điều khiển chỉ bù đúng phần còn thiếu dựa trên tín hiệu vận động và trạng thái bài tập, chứ không đóng ngón tay hoàn toàn theo lệnh từ camera. Cách làm này khác với kéo cưỡng bức theo chu kỳ ở chỗ nó giữ người tập trong vòng điều khiển, và khác với găng thụ động ở chỗ nó vẫn hỗ trợ được khi người tập chưa tự hoàn thành tầm vận động.

Trợ lực theo nhu cầu được định nghĩa bằng ba điều kiện: thiết bị chỉ can thiệp khi có nỗ lực vượt ngưỡng nền; khi nỗ lực đó không đủ để đạt mục tiêu trong khoảng thời gian cho phép; và mức bù giảm dần khi người tập làm được nhiều hơn.

Một hiệu ứng phải nêu thẳng là hiệu ứng ỷ lại: người tập học được rằng máy sẽ lo phần còn lại nên giảm dần nỗ lực. Y văn mô tả đây là một thích nghi học được chứ không phải phản xạ tự động tức thời, và bản thân cơ chế trợ lực tính theo sai số quỹ đạo không triệt tiêu được hiện tượng này; tài liệu gần đây đề xuất tách thành hai kênh điều khiển, một kênh đặt độ lợi trợ giúp và một kênh phản ánh mức tham gia của người tập.

Hệ quả cho đề tài: muốn chống ỷ lại thì phải đo được mức tham gia. Đó là lý do chỉ số EI và cửa sổ thăm dò tồn tại song song với cơ cấu kéo; cơ cấu chỉ là phần bù lực, còn phần đo mức tham gia mới giữ cho người tập không buông.

| Tiêu chí | Thụ động đơn thuần | Chủ động có trợ lực |
|---|---|---|
| Kích hoạt lệnh vận động | thấp và không ổn định | bắt buộc, vì đó là định nghĩa của chế độ |
| Bằng chứng về lợi ích bổ sung | nhỏ hơn; tổng quan gộp cho thấy chế độ thụ động không có lợi ích thêm so với nhóm chứng | lớn hơn; các chế độ có thành phần chủ động cho thấy lợi ích |
| Hiệu ứng ỷ lại | cao | thấp hơn, nhưng chỉ khi thuật toán có theo dõi mức tham gia |
| Kết quả cơ học | duy trì tầm vận động thụ động | hướng tới tầm vận động chủ động và kỹ năng cầm nắm |
| Rủi ro | thấp nếu có giới hạn mô-men, tăng khi đặt máy quá mạnh | cần giới hạn lực và giám sát; hiệu quả giảm khi co cứng nặng |
| Bằng chứng về cải thiện chức năng so với điều trị thường quy | — | **chưa rõ**: một thử nghiệm lớn trên robot chi trên không thấy khác biệt về thang ARAT ở thời điểm 3 tháng |

Dòng cuối của bảng là lý do đề tài không được suy ra rằng có trợ lực thì tốt hơn về chức năng; đề tài chỉ tuyên bố đo được phần người tập tự làm và bù phần còn thiếu, trên bàn thử và mô hình bàn tay giả.

**Thiết kế cơ cấu.** Bộ truyền trợ lực dùng servo cuốn dây câu cá trực tiếp lên ba tang riêng, mỗi ngón một tang; chiều duỗi thực hiện bằng servo nhả dây chủ động, không dùng lò xo hồi vị, đàn hồi nối tiếp hay khớp bốn khâu. Ở bước thiết kế chi tiết còn phải xác định dùng một động cơ kéo cả ba tang hay ba động cơ riêng, đường kính tang, hành trình dây, vị trí neo, phương pháp đo độ căng dây độc lập và hành vi nhả dây khi mất nguồn; hành vi này là bài toán cơ khí chứ không xử lý bằng phần mềm.

**Thiết kế điều khiển.** Việc chuyển từ hỗ trợ gập – duỗi sang trợ lực giảm dần diễn ra tự động, không cần kỹ thuật viên nhấn nút. Toàn bộ vận hành được tổ chức thành ba pha nối tiếp nhau, để hệ thống đơn giản và trả lời được câu hỏi chuyển pha dựa trên tín hiệu nào.

**Pha nghỉ** là trạng thái mặc định khi khởi động, đồng thời là trạng thái hệ thống trở về khi kết thúc buổi tập hoặc khi phát hiện sự cố: servo không tải, dây cáp ở vị trí nhả, người tập có thể rút tay ra.

**Pha đo nỗ lực** bắt đầu khi người tập vào tư thế sẵn sàng và hai ô tham chiếu ổn định. Ở pha này hệ thống xác định người tập có tự khởi xướng được vận động hay không bằng cách mở một cửa sổ thăm dò: tạm ngưng trợ lực trong khoảng ngắn định trước rồi quan sát đáp ứng.

**Pha kéo trợ lực** bắt đầu khi cửa sổ thăm dò không thấy vận động tự nguyện đủ hoàn thành tầm vận động. Servo kéo theo biên độ đặt trước và giảm dần mức trợ lực mỗi lần pha đo nỗ lực phát hiện người tập tự làm được. Bài tập gắp thìa nằm trong pha này, nhãn trạng thái từ camera dùng để điều chỉnh trợ lực theo từng giai đoạn của tác vụ.

Mọi lỗi phần mềm phát hiện được, gồm mất phản hồi servo, mất đồng bộ dấu thời gian và vượt giới hạn hành trình, đều đưa hệ thống về pha nghỉ và ghi nhật ký. Nguyên mẫu chưa có điện trở shunt đo dòng, chưa có cảm biến góc và chưa có rơ-le ngắt nguồn, nên không có điều kiện chuyển pha nào dựa trên ba tín hiệu đó; an toàn khi mất nguồn dựa vào chốt chặn cơ khí và ngàm bẩy mở nẹp.

Trường hợp đeo nẹp lỏng hoặc ô tham chiếu trôi bất thường không phải một pha, mà là **trạng thái loại phiên đo**: hệ thống ngưng trợ lực, yêu cầu kiểm tra lại cách đeo, và phiên đó bị loại khỏi tập số liệu báo cáo kèm lý do.

Điểm khó nhất là phân biệt vận động do người tập khởi xướng với chuyển động do chính cơ cấu tạo ra; nếu không, hệ thống sẽ tự giảm trợ lực cho một người không có vận động chủ động và số liệu đánh giá mất ý nghĩa. Cửa sổ thăm dò giải quyết đúng vấn đề đó ở mức tối giản. Độ dài cửa sổ, tần suất mở, tiêu chí nhận diện đáp ứng, hành vi khi không có đáp ứng và số lần lặp sẽ xác định bằng thực nghiệm trên giàn đo, và rà soát an toàn trước mọi lần chạy có cấp nguồn. Phương pháp này không phát hiện được nỗ lực không tạo ra chuyển động.

*Kiểm tra và kiểm thử tương ứng: mục C.5.*

### 8. Nhánh thị giác và bài tập gắp thìa

**Cơ sở lý thuyết.** Lấy một tác vụ thật làm đơn vị đánh giá thì phép đo mới gắn với chức năng sinh hoạt, thay vì gắn với số lần co duỗi. Chiếc thìa được chọn vì nó là vật dụng quen thuộc, có khối lượng và hình dạng xác định, và bài tập gắp – nâng – di chuyển – đặt bao trùm được cả ba ngón trụ cột.

**Thiết kế.** Camera nhận biết thìa và vùng đích trong bố trí cố định, rồi gán nhãn cho từng giai đoạn của bài tập: sẵn sàng, nắm thìa, nâng thìa, di chuyển, thành công, rơi thìa, đặt sai chỗ hoặc không xác định. Nhãn này vừa dùng tính chỉ số tác vụ vừa hiển thị phản hồi trực quan cho người tập; nhánh thị giác không đo lực ngón tay.

Bộ nhận biết viết theo dạng thay thế được: trước hết dùng xử lý ảnh cổ điển bằng OpenCV trên Orange Pi 5 Pro, chỉ chuyển sang mô hình học sâu nếu kết quả đo thử trên đúng phần cứng đó không đạt. Nếu cần tọa độ thật thì phải hiệu chuẩn tỷ lệ trước khi quy đổi từ tọa độ ảnh.

Các chỉ số của nhánh thị giác gồm độ đúng của nhãn, tỷ lệ nhãn không xác định, độ trễ đầu – cuối và số khung hình mỗi giây; tất cả đo ở mốc 3, và giao tiếp giữa Orange Pi 5 Pro với ESP32-S3 hiện chưa tích hợp. Độ trễ đầu – cuối của nhánh thị giác không thể nhỏ hơn một chu kỳ phơi sáng của camera, ở 30 khung hình mỗi giây là 33,3 ms; vì vậy chỉ tiêu không vượt quá 20 ms chỉ áp dụng cho đường từ cảm biến đến lệnh servo.

Bài tập thìa cần một tờ yêu cầu tác vụ ghi rõ loại thìa và khối lượng, kích thước và vị trí vùng đích, khoảng cách di chuyển, tiêu chí để coi là đặt thành công, thời gian tối đa cho một lượt và số lượt trong mỗi buổi tập; các thông số này xác định khi đo trên vật thật.

⟨HÌNH 5 — bố trí bàn thử: camera, vùng đích và mô hình tay giả⟩

**Giả định về cảnh quay.** Nhánh thị giác chỉ hoạt động được trong một cảnh đã khai báo trước, và mọi giả định này phải ghi vào nhật ký từng phiên: camera đặt cố định trên giá, vị trí lặp lại được, nếu xê dịch giữa các phiên thì phải hiệu chuẩn lại; trong cảnh chỉ có một chiếc thìa duy nhất với đặc tính đã khai báo; vùng đích được đánh dấu nhìn thấy được bằng khuôn in, điểm mốc hoặc màu tương phản, để tiêu chí "trong vùng đích" định nghĩa được bằng hình học; nền và ánh sáng trong nhà kiểm soát được một phần và phải ghi điều kiện ánh sáng mỗi phiên; không có vật thể gây nhiễu cùng màu hoặc cùng mẫu với thìa; góc nhìn thấy được cả vùng xuất phát và vùng đích và không bị bàn tay che khuất toàn bộ. Ba giả định cuối chưa được xác nhận và phải kiểm tra bằng ảnh thử trước khi chạy, chọn vị trí camera rồi chụp lại làm bản ghi.

**Bộ nhận biết viết theo dạng thay thế được.** Yêu cầu thiết kế là logic tác vụ phải độc lập với bộ nhận biết, để đổi bộ nhận biết mà không phải viết lại luật chuyển pha. Mọi bộ nhận biết trả về cùng một lược đồ đầu ra gồm: tên, phiên bản và mã phiên bản mô hình để truy vết; cờ có thìa hay không, hộp bao quanh và góc nghiêng của thìa trong mặt phẳng ảnh; độ tin cậy theo định nghĩa của chính bộ nhận biết; đa giác vùng đích đã hiệu chuẩn cùng cờ vùng đích có mặt; cờ che khuất và lý do che khuất; và hai trường tùy chọn là điểm cán thìa nơi ba ngón tiếp xúc, cùng khoảng cách tính bằng milimét chỉ khi bật nhánh độ sâu và đã hiệu chuẩn tỷ lệ. Bộ nhận biết không suy được trường nào thì để trống kèm cờ, không được điền giá trị suy diễn.

**Bắt đầu bằng xử lý ảnh cổ điển, không dùng học sâu.** Bộ nhận biết mặc định tách nền bằng cách trừ ảnh nền tĩnh với khung hiện tại, vì cảnh cố định; phân đoạn thìa theo màu hoặc vật liệu đã khai báo, hoặc theo điểm mốc thụ động nếu được duyệt; tách vùng đích theo đa giác hiệu chuẩn trước; ước lượng hình dạng bằng đường bao và hình chữ nhật ngoại tiếp nhỏ nhất cho bầu thìa, trục cán suy ra bằng phân tích thành phần chính trên đường bao; chống nhiễu bằng cách lọc theo diện tích và tỷ lệ cạnh, bỏ ứng viên ngoài vùng làm việc; rồi bám vật thể bằng cách liên kết hộp bao giữa các khung theo dự đoán vị trí và khoảng cách. Lý do chọn cổ điển trước là cảnh cố định, vật thể đã biết, yêu cầu giải thích được từng bước trước hội đồng, và chi phí tính toán thấp. Nếu thử nghiệm cho thấy ánh sáng và nền trong nhà làm phương pháp cổ điển không ổn định thì khi đó mới xét mô hình học sâu; việc đổi bộ nhận biết phải ghi lại kèm lý do và dữ liệu so sánh, không đổi âm thầm.

Các bộ nhận biết ứng viên khác được giữ lại nhưng chưa nhận vào phạm vi: theo dõi bàn tay bằng mô hình có sẵn, chỉ dùng để đối chiếu pha tiếp xúc và phải khai báo rõ là theo dõi bàn tay chứ không suy ra lực; mô hình phát hiện vật thể tổng quát, chỉ dùng khi nền phức tạp tới mức thìa không tách được bằng màu, và phải ghim trọng số cùng phiên bản rồi báo cáo độ đúng trên tập nhãn của chính cảnh này; ước lượng độ sâu từ một ảnh, chỉ dùng khi tác vụ thật sự cần tọa độ ba chiều, và tọa độ chưa hiệu chuẩn thì không được gọi là milimét. Ba hướng sau đây không thuộc phạm vi: học tăng cường để sinh chính sách trợ lực; lượng tử hóa và suy luận trên bộ xử lý thần kinh của máy tính thị giác; và thuật toán tự động gắn nhãn phiên đo nghi vấn. Phiên đo lỗi được xử lý bằng trạng thái không hợp lệ kèm lý do ghi trong nhật ký.

Về tọa độ: đề tài bắt đầu bằng tọa độ mặt phẳng ảnh hai chiều đã hiệu chuẩn, chỉ thêm độ sâu nếu bài tập thật sự cần. Trước khi gọi bất kỳ tọa độ nào là đo theo đơn vị thật, phải có bản ghi hiệu chuẩn camera và vật chuẩn tỷ lệ trong cảnh.

**Hiệu chuẩn camera.** Các bản ghi phải có trước khi chạy phiên đo là: vị trí camera gồm tọa độ, độ cao và góc so với mặt bàn kèm ảnh chụp bố trí; nội tham số nếu cần, tức ma trận camera và hệ số méo, hoặc bỏ qua nếu dùng ảnh phẳng hai chiều; vật chuẩn tỷ lệ có kích thước đã biết đặt trong mặt phẳng thao tác; ánh xạ từ ảnh sang mặt bàn bằng phép biến đổi đồng dạng từ bốn điểm chuẩn trở lên; đa giác vùng đích khai báo bằng số, lưu trong tệp cấu hình và có mã phiên bản; và mỗi phiên chụp một ảnh chuẩn để so lệch vị trí. Nếu không hiệu chuẩn thì chỉ được nói tọa độ trong ảnh tính bằng điểm ảnh, không được nói milimét.

**Phản hồi trực quan cho người tập.** Màn hình hiển thị trạng thái tác vụ hiện tại, kết quả thành công hay thử lại, và tiến trình, ví dụ vùng đích sáng lên khi đặt đúng. Chữ và hình phải đủ lớn, tương phản cao, đọc được bởi người trung niên sau đột quỵ; yêu cầu này cần thử với người dùng thật và chỉ thử khi đã có phê duyệt phù hợp. Độ trễ cảm nhận phải đo từ đầu đến cuối, tức từ camera qua xử lý tới hiển thị, và đề tài không hứa trước con số. Hai ràng buộc cố định: không hiển thị nội dung mang tính chẩn đoán, tiên lượng hay đánh giá phục hồi; và khi chưa đủ bằng chứng thì hiển thị "chưa xác nhận, hãy thử lại" chứ không hiển thị "thất bại". Phản hồi thị giác là phản hồi tác vụ, không phải bằng chứng về tái tổ chức thần kinh hay cải thiện phục hồi.

**Giao tiếp giữa hai bo mạch.** Ở giai đoạn bàn thử dùng kết nối nối tiếp qua USB; kết nối không dây chỉ xét sau khi đo nhiễu. Định dạng là dòng JSON, mỗi thông báo ứng với một lần đổi trạng thái, gồm phiên bản lược đồ, dấu thời gian phía máy tính thị giác, số hiệu khung, nhãn tác vụ, độ tin cậy, cờ che khuất, tên và phiên bản bộ nhận biết, hộp bao và cờ trong vùng đích. Tần suất là chỉ gửi khi đổi nhãn, kèm tín hiệu sống định kỳ mà chu kỳ chưa chốt. Bộ giám sát treo hoạt động theo nguyên tắc: nếu vi điều khiển không nhận được tín hiệu sống quá một khoảng chưa chốt thì coi luồng thị giác mất tin cậy và về trạng thái an toàn đã định trước. Hai ràng buộc không thương lượng: luồng thị giác không có trường nào ra lệnh kéo servo, nó chỉ báo nhãn tác vụ và pha; và độ lệch đồng hồ giữa hai thiết bị phải được ước lượng rồi ghi vào nhật ký mỗi phiên.

**Kế hoạch đo thử trên máy tính thị giác.** Phiếu đo gồm chín chỉ số, tất cả đều chưa có giá trị mục tiêu và chưa đo: tốc độ khung xử lý tính bằng cách đếm số khung hoàn tất cả luồng chia cho thời gian; độ trễ từ camera tới nhãn, đo bằng chênh dấu thời gian bắt khung và dấu thời gian phát nhãn; độ trễ phản hồi hiển thị, đo bằng video tốc độ cao hoặc sự kiện đồng bộ; độ đúng của từng nhãn trên tập ảnh và video đã gán nhãn thủ công để lập bảng nhầm lẫn; tỷ lệ nhãn chưa xác nhận; ảnh hưởng của che khuất trên tập thử có che khuất chủ đích; tải bộ xử lý và nhiệt độ đọc trong lúc chạy; sai số vị trí tính bằng điểm ảnh và bằng milimét sau hiệu chuẩn, so với mốc thật đo bằng thước; và độ ổn định giữa các phiên và điều kiện sáng bằng cách lặp lại cùng cảnh.

Bốn yêu cầu phương pháp đi kèm phiếu đo: tập thử phải là ảnh và video của đúng cảnh thật sẽ dùng, có nhãn thủ công độc lập, số lượng và cách chia tập chỉnh tham số với tập đánh giá phải khai báo trước; mọi kết quả phải ghim tên bộ nhận biết, phiên bản, mã phiên bản mô hình, mã phiên bản cấu hình và bản mã nguồn, đổi bất kỳ thành phần nào là một phiên bản mới và không so sánh chéo như cùng một hệ; dữ liệu dùng để chỉnh tham số tách khỏi dữ liệu dùng để báo cáo, không chọn ngưỡng sau khi đã xem kết quả đánh giá; và dữ liệu tổng hợp hoặc phát lại phải gắn nhãn mô phỏng, không trộn vào bảng kết quả thật.

*Kiểm tra và kiểm thử tương ứng: mục C.6.*

---

### 9. Kiến trúc phần mềm, phần mềm nhúng và lộ trình triển khai

**Cơ sở.** Phần cứng và cơ cấu chỉ trả lời được câu hỏi đo có đúng hay không nếu dữ liệu đi kèm một hạ tầng ghi chép đáng tin: mỗi khung dữ liệu phải có số hiệu và dấu thời gian, mỗi phiên phải khai báo cấu hình đã dùng, và dữ liệu mô phỏng phải tách khỏi dữ liệu đo thật. Vì vậy đề tài dành một mục riêng cho kiến trúc phần mềm, dù đến nay chưa viết dòng mã nào.

**Nguyên tắc bất biến khi viết mã.** Tám nguyên tắc sau được chốt trước để tránh loại lỗi phổ biến nhất của dự án học sinh là chỉnh tham số sau khi đã thấy kết quả.

Một là không gán cứng ngưỡng: mọi đặc trưng, ngưỡng, cửa sổ, số chu kỳ, độ trễ, giới hạn hành trình đều nằm trong tệp cấu hình có phiên bản; giá trị chưa chốt phải để trống và chương trình phải từ chối chạy chế độ đánh giá thay vì tự thay bằng giá trị mặc định. Hai là đóng băng trước khi đánh giá: cấu hình được băm thành mã phiên bản và ghi vào phiếu buổi đo; dữ liệu dùng để chỉnh tham số tách khỏi dữ liệu dùng để báo cáo. Ba là mô phỏng không phải số đo: dữ liệu tổng hợp và dữ liệu phát lại gắn nhãn mô phỏng, dữ liệu thật gắn nhãn bàn đo hoặc mô hình tay giả, và báo cáo không được trộn hai loại.

Bốn là nhật ký gốc bất biến: tệp gốc không bị ghi đè, bản tính lại đặt tên riêng. Năm là an toàn nằm ở tầng thấp: giới hạn hành trình, dừng, nhả và bộ giám sát phải chạy độc lập với suy luận thị giác và độc lập với logic cấp cao; cơ cấu nhả không chỉ dựa vào phần mềm. Sáu là không có thao tác của kỹ thuật viên trong luồng vận hành; nút bấm của người vận hành chỉ dùng cho khởi động và dừng khẩn ở giai đoạn bàn thử, không dùng để chuyển pha thay hệ thống. Bảy là mọi mô-đun đều có kiểm thử chạy được mà không cần phần cứng, dùng bộ phát lại hoặc bộ mô phỏng, để không lấy cớ chưa có bo mạch mà bỏ kiểm thử. Tám là không tuyên bố hiệu quả lâm sàng, an toàn đã được chứng nhận, tính mới hay "đã dùng tại nhà" trong mã nguồn, chú thích và tài liệu.

**Kiến trúc hai bo mạch.** Vi điều khiển ESP32-S3 đảm nhiệm phần thời gian thực: quét bộ chuyển mạch và bộ chuyển đổi để tạo khung dữ liệu có số hiệu khung và dấu thời gian; chạy chuỗi xử lý bốn bước; gắn cờ hợp lệ cho từng kênh và kiểm tra độ trôi của hai ô tham chiếu; chạy bộ giám sát pha; phát lệnh servo có giới hạn hành trình kèm chức năng dừng, nhả và bộ giám sát; phát nhật ký dạng dòng JSON qua cổng nối tiếp USB; và nhận nhãn trạng thái tác vụ từ máy tính thị giác.

Orange Pi 5 Pro đảm nhiệm phần không thời gian thực: ghi nhật ký phiên cùng phiếu buổi đo và giá trị kiểm tra tổng, chạy luồng thị giác gồm bộ nhận biết, bộ bám và bộ gán nhãn, hiển thị phản hồi cho người tập, và phân tích để sinh đường cong hiệu chuẩn, đặc trưng, bảng nhầm lẫn cùng báo cáo phiên.

Một quyết định kiến trúc còn mở: đặt bộ giám sát pha trên vi điều khiển, để có trễ thấp và vẫn chạy khi mất kết nối với máy tính thị giác, hay đặt trên máy tính thị giác, để dễ kiểm thử và dễ đổi luật. Nhóm đề xuất đặt trên vi điều khiển và để máy tính thị giác chỉ gửi pha tác vụ cùng nhãn, vì lý do an toàn; đây là đề xuất, chưa phải quyết định đã chốt.

Về bố trí mã nguồn, phần phần mềm nhúng cho vi điều khiển tách thành các khối thu nhận, xử lý tín hiệu, giám sát pha, servo, giao thức và an toàn, kèm một bản sao logic giám sát pha chạy trên máy tính để kiểm thử đơn vị mà không cần bo mạch. Phần mềm phía máy tính tách thành các khối nạp và kiểm tra lược đồ, hiệu chuẩn, trích đặc trưng, giám sát pha, thị giác, bàn điều khiển, sinh báo cáo và lược đồ dữ liệu; kèm thư mục cấu hình có phiên bản, thư mục mô phỏng và thư mục kiểm thử. Dữ liệu đo, ảnh và video không đưa vào kho mã nguồn.

**Lộ trình triển khai.** Pha thứ nhất là hạ tầng dữ liệu: viết lược đồ cho khung dữ liệu, sự kiện, nhãn tác vụ và phiếu buổi đo, cùng tệp cấu hình mẫu với mọi ngưỡng để trống và công cụ kiểm tra lược đồ; pha này không cần phần cứng. Pha thứ hai là bộ mô phỏng và bộ phát lại, sinh tín hiệu cảm biến và nhãn tác vụ có tham số về biên độ, độ trôi, nhiễu và trễ; pha này cho phép chạy thử logic giám sát pha trước khi có bo mạch, nhưng kết quả của nó không phải bằng chứng thiết bị hoạt động.

Pha thứ ba là phần mềm nhúng thu nhận, chạy trên bo mạch thật với bản đồ kênh đã duyệt, đo tốc độ khung thật rồi so với giá trị tính toán. Pha thứ tư là hiệu chuẩn và đặc trưng hóa cảm biến, tức các phép kiểm ở mục C.2. Pha thứ năm là bộ giám sát pha và quy tắc chuyển pha tự động, chạy trước với bộ mô phỏng rồi chạy lại với dữ liệu thật. Pha thứ sáu là nhánh thị giác, chạy song song từ sớm. Pha thứ bảy là bàn điều khiển và báo cáo, để xem trực tiếp khung cảm biến, pha vận hành, nhãn tác vụ và các sự kiện trợ lực hoặc dừng, đồng thời sinh báo cáo phiên từ nhật ký.

Về phụ thuộc: hạ tầng dữ liệu và bộ mô phỏng không cần phần cứng nên làm trước được; phần mềm nhúng thu nhận và hiệu chuẩn cần bo mạch thật và cần cảm biến Flex đã mua; bộ giám sát pha có thể bắt đầu sớm nhờ bộ mô phỏng nhưng không được báo cáo như kết quả thiết bị cho tới khi chạy trên dữ liệu thật có nhật ký; bàn điều khiển và phiên tích hợp cần cả ba nhánh cảm biến, cơ cấu và thị giác.

*Toàn bộ mục này là kế hoạch; chưa có mô-đun nào được viết hoặc kiểm thử.*

*Kiểm tra và kiểm thử tương ứng: mục C.7.*

---

## C. KIỂM TRA VÀ KIỂM THỬ

*Mỗi mục của phần C kiểm thử cho thiết kế ở mục cùng số thứ tự của phần B, tính từ B.3. Số liệu trong phần C gồm những gì đã quan sát được trên bàn đo và các ngưỡng mục tiêu sẽ đo ở mốc 1, mốc 2 và mốc 3.*

### 1. Kiểm tra và kiểm thử khung nẹp và khóa đeo

Khóa nẹp quyết định người tập có tự đeo được găng hay không, nên được khảo sát trước tiên: nhóm đã in thử và đeo thử 9 phương án theo ba nhóm nguyên lý.

Nhóm 1 gồm phương án 1 đến 3: vòng kẹp chữ C đàn hồi, rãnh trượt đuôi én và đai Velcro, cho thời gian đeo 55–80 s và không giữ được tiền tải. Nhóm 2 gồm phương án 4 đến 6: chốt xuyên ngang, khóa gài mặt mu và thanh răng rút, rút còn 40–65 s nhưng đòi hỏi hai tay hoặc căn chỉnh chính xác. Nhóm 3 gồm phương án 8, bản lề một trục kết hợp ngàm đàn hồi, đạt 28 s nhưng lỗi bền mỏi; và phương án 9, khóa ngàm xoay hai bản lề kép, khắc phục được lỗi gãy đó nên được chọn làm phương án triển khai.

| Phương án | Nguyên lý khóa | Thời gian tự đeo | Sau 50 chu kỳ đóng mở |
|---|---|---|---|
| Phương án 1–3 | vòng kẹp chữ C; rãnh trượt đuôi én; đai Velcro | 55–80 s | không đạt |
| Phương án 4–6 | chốt xuyên ngang; khóa gài mặt mu; thanh răng rút | 40–65 s | không đạt |
| Phương án 7 | không có số liệu | chưa có | chưa có |
| Phương án 8 | bản lề một trục kết hợp ngàm đàn hồi | 28 s | lỗi bền mỏi |
| Phương án 9 | khóa ngàm xoay hai bản lề kép | chưa bấm giờ | đã in, chưa đo độ bền; phương án được chọn |

Các mốc thời gian trên là kết quả đeo thử nội bộ, chưa lập biên bản đo, nên chỉ dùng để so sánh định tính giữa các phương án.

Phương án 9 đã in xong nhưng chưa bấm giờ, nên chưa có con số thời gian đeo. Thời gian tự đeo, thời gian tháo qua chốt mở nhanh và độ bền mỏi theo số chu kỳ đóng mở là chỉ tiêu kiểm thử của mốc 2; số chu kỳ dùng cho phép đo bền xác định trong quy trình đo, vì 50 chu kỳ là rất nhỏ so với số lần đóng mở của một liệu trình nhiều tuần. Khối lượng cụm đeo cũng cân thật ở mốc 2.

⟨HÌNH 6 — ảnh các thế hệ khóa nẹp đã in thử⟩

### 2. Kiểm tra và kiểm thử màng cảm biến áp lực và cảm biến gập

Đối tượng kiểm thử là từng ô Velostat, từng cặp lòng – mu, từng cảm biến Flex và hai ô tham chiếu. Sáu phép kiểm được lập kế hoạch, tất cả thực hiện trên băng thử với tải chuẩn đã biết.

Một là đáp ứng theo tải và độ tuyến tính, với tải tăng dần rồi giảm dần, ít nhất ba lượt lặp, để lấy đường chuẩn của từng ô và hệ số xác định. Hai là trễ đàn hồi và độ dãn tải tĩnh, so nhánh tăng tải với nhánh giảm tải và giữ tải không đổi 60 giây. Ba là độ lặp lại nội phiên và liên ngày, trong cùng điều kiện và cùng cách lắp. Bốn là nhiễu nền và tỷ số tín hiệu trên nhiễu ở trạng thái nghỉ, báo cáo cả tín hiệu thô lẫn sau lọc.

Năm là xuyên kênh, kích thích một kênh rồi đọc các kênh đang nghỉ, lấy kênh 15 làm mốc. Sáu là trôi nền, bằng chuỗi nhật ký ít nhất 10 ngày với hai ô tham chiếu, để tách phần trôi do môi trường khỏi phần trôi do dão tải của ngón.

Riêng phép kiểm cặp lòng – mu cần một bước mà phép đo đơn ô không có: ép vào nẹp và ép vào vật phải cho hai mẫu tín hiệu khác nhau, tức ô mặt mu tăng trong trường hợp thứ nhất và ô mặt lòng tăng trong trường hợp thứ hai. Nếu hai trường hợp cho cùng một mẫu thì cách bố trí vi sai không dùng được và phải đổi vị trí lắp.

Ngưỡng vùng chết 180 mV nêu ở B.5 sẽ được xác định lại từ chính dữ liệu của phép kiểm bốn: phân bố nhiễu đo trên từng kênh cho ngưỡng, và tín hiệu nỗ lực sớm phải được kiểm tra riêng xem có sống sót sau vùng chết hay không. Phép kiểm này quyết định chỉ số EI có đo được hay không.

Đến nay chưa có buổi đo nào trong sáu phép kiểm trên được thực hiện có biên bản; toàn bộ ngưỡng ở bảng C.8 vẫn là mục tiêu.

### 3. Kiểm tra và kiểm thử mạch thu nhận và thuật toán xử lý tín hiệu

Đối tượng kiểm thử là chuỗi phần cứng và chuỗi xử lý ở B.5. Nhóm đã hoàn thành hai vòng lặp thiết kế.

**Vòng lặp 1, dùng tầng khuếch đại dụng cụ INA333 với hệ số khoảng 6,5.** Ngõ ra sạch và các kênh cách ly tốt khi đo với nguồn tín hiệu chuẩn. Nhưng khi lắp cảm biến thật và gài khóa tiền tải của nẹp, cầu phân áp sụt dưới 1,42 V và ngõ ra bão hòa cứng ở khoảng 2.838 mV, dải tuyến tính còn 1,44–1,92 V, nhiễu nền lúc nghỉ 50–135 mV. Nguyên nhân là khuếch đại cố định không phù hợp với trở kháng và dải điện trở biến thiên lớn của phần tử áp trở khi có tiền tải; đây là lỗi kiến trúc chứ không phải lỗi linh kiện, nên hệ thống không dùng tầng khuếch đại cố định.

**Vòng lặp 2, bỏ INA333 và đọc trực tiếp qua tầng khuếch đại lập trình được của ADS1115, kết hợp chuỗi xử lý bốn bước.** Vòng này giữ trọn dải ngõ vào 0–3.300 mV trên bàn đo, thêm đọc nháp và chờ 300 µs sau chuyển kênh; vùng chết 180 mV giữ đường nền ổn định khi nghỉ.

| Hạng mục | Ghi nhận trên bàn đo | Mục tiêu |
|---|---|---|
| Kiến trúc ngõ vào | bỏ INA333, đọc trực tiếp qua tầng khuếch đại lập trình được, trọn dải 0–3.300 mV | thu trọn dải, không bão hòa ở tải thiết kế |
| Bão hòa ngõ ra | vòng 1: cầu phân áp < 1,42 V, bão hòa ≈ 2.838 mV, dải tuyến tính 1,44–1,92 V | không bão hòa ở cấu hình 11 kênh |
| Nhiễu nền lúc nghỉ | nhiễu thô 50–135 mV; sau vùng chết 180 mV, đầu ra lúc nghỉ ghim về 0 | không quá 5 mV đỉnh – đỉnh sau lọc, đo ≥ 10 phiên |
| Xuyên kênh | đọc nháp và chờ 300 µs làm giảm bóng ma kênh; kênh 15 làm mốc | ngưỡng chưa xác định |
| Tỷ số tín hiệu trên nhiễu và độ tuyến tính | chưa có ghi nhận đạt yêu cầu trên băng thử | không thấp hơn 18 dB; R² không thấp hơn 0,90 |
| Tốc độ khung | vòng 1 khoảng 22 Hz với 16 kênh, trễ chuyển kênh khoảng 120 µs | không thấp hơn 20 Hz toàn khung; tính toán khoảng 35 Hz với 11 kênh |
| Trôi nền dài hạn | chưa có chuỗi nhật ký dài ngày | nhật ký ≥ 10 ngày với hai ô tham chiếu |

Phép kiểm còn lại của mục này là tốc độ khung và trễ biên: đếm số hiệu khung để lấy tốc độ thật, và đo khoảng thời gian từ khung dữ liệu đến lúc lệnh servo thay đổi. Hai chỉ số tỷ số tín hiệu trên nhiễu và độ tuyến tính sẽ xác định bằng buổi đo có biên bản, ghi rõ tải chuẩn, số lần lặp, điều kiện môi trường, kiểm tra kênh tham chiếu trước và sau phiên, cùng định nghĩa phép tính: cửa sổ tín hiệu và cửa sổ nhiễu cho tỷ số tín hiệu trên nhiễu, số điểm tải và phương pháp hồi quy cho hệ số xác định.

⟨HÌNH 7 — đồ thị vòng lặp 1 với hiện tượng bão hòa và vòng lặp 2 giữ trọn dải ngõ vào⟩

### 4. Kiểm tra và kiểm thử bộ chỉ số EI – GAP – RAL

Đối tượng kiểm thử là ba chỉ số ở B.6, tức kiểm tra xem mỗi chỉ số có đủ độ tin cậy để dùng theo dõi tiến triển hay không.

GAP được kiểm bằng cách đối chiếu biên độ gập đọc từ cảm biến Flex đã hiệu chuẩn với thước đo góc bên ngoài, trên cùng một mô hình bàn tay giả, ở cả tầm vận động thụ động và chủ động. Thước đo góc là nguồn tham chiếu; nếu hai nguồn lệch nhau quá hệ số biến thiên cho phép thì chỉ số không dùng được.

EI và RAL được kiểm trên giàn đo cơ học: giàn trục trượt tạo chuyển động gập – duỗi lặp lại theo biên độ và tốc độ đặt trước, tải chuẩn có khối lượng đã biết đặt đúng đường truyền lực, và mô hình bàn tay giả silicone làm đối tượng đeo. Độ tin cậy của từng chỉ số đánh giá bằng hệ số biến thiên nội phiên, hệ số biến thiên liên ngày, sai số chuẩn của phép đo và ngưỡng khác biệt nhỏ nhất có ý nghĩa [7].

Quy tắc phiên đo áp dụng chung cho mọi phép kiểm: mỗi phiên ghi ngày giờ, người vận hành, phiên bản cấu hình, nhiệt độ và độ ẩm nếu có, cách lắp, số lần lặp, kết quả kiểm tra ô tham chiếu trước và sau phiên. Phiên đo bị loại khi ô tham chiếu trôi vượt ngưỡng, mất đồng bộ dấu thời gian hoặc có can thiệp vào cách đeo giữa phiên; phiên bị loại phải ghi rõ lý do.

Công thức của EI, cách chọn mức tham chiếu và ngưỡng tỷ lệ hoàn thành của RAL xác định sau lượt thử đầu trên mô hình bàn tay giả và được ghi lại thành phiên bản.

### 5. Kiểm tra và kiểm thử cơ cấu trợ lực và ba pha vận hành

Đối tượng kiểm thử là cơ cấu ba tang và bộ điều khiển ba pha ở B.7, thực hiện trên mô hình bàn tay giả.

Phép kiểm cơ cấu gồm: hành trình thực tế so với lệnh, dạng kẹp ba chấu có đạt hình học mong muốn hay không, hành vi nhả dây khi cắt nguồn, và độ căng dây đo bằng một phương pháp độc lập. Hành vi nhả khi mất nguồn phải đo chứ không giả định; thời gian tháo tay qua chốt mở nhanh cũng đo ở mốc này.

Phép kiểm điều khiển gồm: số lần chuyển pha đúng và sai so với nhãn đối chiếu, số sự kiện trợ lực sai pha, và độ trễ từ cảm biến đến lệnh servo đo bằng nhật ký đồng bộ. Độ dài cửa sổ, tần suất mở và tiêu chí nhận diện đáp ứng của quy tắc cửa sổ thăm dò xác định bằng thực nghiệm.

Phép so sánh tối thiểu khi tích hợp là đối chiếu trợ lực cố định với trợ lực theo nhu cầu tự động, trên cùng một mô hình bàn tay giả và trong điều kiện tương đương. Đây là phép kiểm trả lời câu hỏi cốt lõi của đề tài: cơ chế tự giảm trợ lực có tạo ra khác biệt đo được so với kéo cố định hay không.

### 6. Kiểm tra và kiểm thử nhánh thị giác và bài tập gắp thìa

Đối tượng kiểm thử là bộ nhận biết thìa và vùng đích ở B.8, đo thử trên đúng phần cứng sẽ dùng là Orange Pi 5 Pro.

Các chỉ số thị giác gồm độ đúng của nhãn, tỷ lệ nhãn không xác định, độ trễ đầu – cuối đo bằng dấu thời gian ở hai đầu, và số khung hình mỗi giây. Độ đúng của nhãn được lập bảng nhầm lẫn so với nhãn gán thủ công, để biết loại lỗi nào chiếm ưu thế thay vì chỉ có một tỷ lệ chung.

Các chỉ số tác vụ gồm tỷ lệ hoàn thành bài tập thìa, thời gian hoàn thành, số lần rơi thìa hoặc đặt sai vị trí; tất cả lấy từ nhãn camera và nhật ký trên đồng hồ thời gian chung. Tờ yêu cầu tác vụ lập trước khi đo: loại thìa và khối lượng, kích thước và vị trí vùng đích, khoảng cách di chuyển, tiêu chí đặt thành công, thời gian tối đa một lượt và số lượt mỗi phiên.

Độ nhạy riêng của từng nguồn đo đánh giá bằng cách tắt lần lượt từng nguồn: chỉ cảm biến gập, chỉ màng áp trở, chỉ camera, rồi đủ cả ba.

**Bài tập thìa chưa được định nghĩa đủ để đo.** Trước khi chạy bất kỳ phiên nào, các ô sau của bài tập phải chốt bằng cách đo vật thật và ghi vào phiếu kèm ảnh: loại thìa, ưu tiên vật dụng thật có sẵn tại nhà để đúng bối cảnh thiết kế; chiều dài toàn phần; khối lượng, là đầu vào cho thiết kế cơ cấu chứ không phải giới hạn lực an toàn; chiều rộng và bề dày cán tại điểm cầm, quyết định khe ngàm nẹp ngón; vật liệu và màu, phải tương phản với nền và vùng đích để nhánh thị giác hoạt động; và có dùng điểm mốc nhận dạng hay không, nếu dùng thì phải khai báo là bài tập có hỗ trợ điểm mốc chứ không mô tả như nhận dạng vật thể tổng quát. Ngoài ra còn phải chốt vùng xuất phát và vùng đích, cách cầm, định nghĩa thả và hoàn thành, chỉ dẫn cho người tập, và cấu trúc phiên gồm số lượt, thời gian nghỉ và tiêu chí dừng.

**Quy tắc diễn giải nhãn.** Không gán nhãn tiếp xúc hoặc giữ thìa chỉ từ tín hiệu màng áp trở, vì màng áp trở là bằng chứng tương đối về áp lực và tiếp xúc, không tự nhận biết ý định. Nhãn chưa xác nhận là một nhãn hợp lệ, phải được đếm và báo cáo riêng, không gộp vào thất bại. Nhãn tác vụ không phải chỉ số phục hồi, chúng chỉ mô tả thiết bị và bài tập.

### 7. Kiểm thử phần mềm, mô phỏng và nhật ký phiên

Đối tượng kiểm thử là kiến trúc phần mềm ở B.9. Vì chưa có mô-đun nào được viết, mục này nêu các phép kiểm sẽ áp dụng và điều kiện đạt của chúng.

Bộ mô phỏng phải sinh được tín hiệu cảm biến gập, tín hiệu màng áp trở và nhãn tác vụ với tham số điều khiển được về biên độ, độ trôi, nhiễu và trễ, và mọi đầu ra của nó phải mang nhãn mô phỏng. Bộ phát lại đọc nhật ký thật khi đã có, để chạy lại đúng một phiên đã đo mà không cần phần cứng.

Bộ giám sát pha phải qua bốn phép kiểm. Thứ nhất, không bao giờ coi chuyển động do servo tạo ra là vận động tự nguyện; phép kiểm này chạy bằng cách phát lại một phiên mà cơ cấu tự kéo và xác nhận hệ thống không thăng pha. Thứ hai, tín hiệu không hợp lệ thì hệ thống phải về trạng thái an toàn. Thứ ba, mất luồng thị giác thì không được kéo trợ lực cho bài tập thìa. Thứ tư, khi một ngưỡng còn để trống trong tệp cấu hình thì chương trình phải từ chối chạy chế độ đánh giá chứ không tự điền giá trị mặc định.

Nhật ký phiên phải qua phép kiểm lược đồ: mỗi khung dữ liệu có số hiệu khung và dấu thời gian, mỗi phiên có phiếu buổi đo chứa mã phiên bản cấu hình, và công cụ kiểm tra lược đồ chạy được trên tệp ví dụ. Tốc độ khung đo thật được so với giá trị tính toán ở B.5, và số khung mất trong một khoảng thời gian phải bằng không; khoảng thời gian đó chưa chốt.

Giới hạn của mục này: kết quả chạy với bộ mô phỏng không được báo cáo như kết quả thiết bị, và một phiên chạy trên mô hình bàn tay giả không được trình bày như thử nghiệm trên người. Bộ công cụ biên dịch cho vi điều khiển phải cài trên máy của nhóm; đây là rủi ro tiến độ chứ không phải rủi ro kỹ thuật.

### 8. Phương tiện, tình trạng thiết bị, mốc thực hiện và bảng tổng hợp chỉ tiêu

Phương tiện kiểm định gồm giàn đo cơ học trục trượt, tải chuẩn có khối lượng đã biết, mô hình bàn tay giả đúc bằng silicone và thước đo góc làm tham chiếu; công dụng của từng thứ nêu ở mục C.4 và C.5.

Về tình trạng thiết bị: Velostat, băng đồng, ESP32-S3, Orange Pi 5 Pro, đồng hồ đo, bộ tạo tín hiệu và bộ chuyển mạch CD74HC4067 đã có, trong đó CD74HC4067 đã được chạy thử; 3 cảm biến gập Flex chưa có, sẽ mua ở mốc 1; giàn trục trượt, cảm biến lực, khối lượng chuẩn và silicone đúc mô hình tay giả thuộc nhóm phải chế tạo hoặc mua ở mốc 1; tình trạng của bộ chuyển đổi ADS1115 chưa được xác nhận. Đến nay đã chạy thử mạch trên breadboard và đo bằng đồng hồ số, chưa có buổi đo nào trên giàn cơ học.

Toàn bộ kiểm định thực hiện trên bàn thử và mô hình bàn tay giả; chỉ xem xét thử có cấp nguồn trên người trưởng thành khỏe mạnh sau khi rà soát an toàn đạt và có phê duyệt, theo một quy trình riêng.

Thứ tự triển khai gồm 5 giai đoạn. **Mốc 0** (~3 tuần): tờ yêu cầu tác vụ, bản đồ kênh cảm biến, phiếu buổi đo, đặc tả ba pha vận hành và chuỗi nhật ký trôi nền ít nhất 10 ngày. **Mốc 1** (~3–4 tuần): mua 3 cảm biến Flex, hiệu chuẩn Flex và Velostat trên băng thử, đo tỷ số tín hiệu trên nhiễu, độ tuyến tính, hệ số biến thiên, trễ đàn hồi và độ dãn tải tĩnh — tức các mục C.2 và C.3. **Mốc 2** (~3–4 tuần): cơ cấu ba tang trên mô hình bàn tay giả, đo hành trình, hành vi nhả khi mất nguồn, giới hạn an toàn, bấm giờ thời gian tự đeo và đo độ bền phương án khóa 9, cân cụm đeo, xuất bản vẽ CAD — tức các mục C.1 và C.5.

**Mốc 3** (~2–3 tuần): nhánh thị giác và bài tập thìa, đo thử trên Orange Pi 5 Pro — tức mục C.6. **Tích hợp** (~2 tuần): chu trình ba bước trên mô hình bàn tay giả và so sánh trợ lực cố định với trợ lực theo nhu cầu — tức mục C.4 và C.5.

Chi phí vật tư cho cụm đeo dự toán 1,0–1,3 triệu đồng, toàn hệ thống và giàn thử khoảng 5,5 triệu đồng khi tận dụng thiết bị phòng thí nghiệm; đây là dự toán, sẽ lập thành bảng vật tư có ngày kèm báo giá. Về khả năng hoàn thành: mốc 0, mốc 1, bản vẽ CAD, phép đo phương án khóa 9 và cụm ba tang thử trên mô hình bàn tay giả nằm trong khả năng chắc chắn; mốc 3 và tích hợp đầy đủ có rủi ro trễ vì nhánh thị giác chưa đo thử và giao tiếp giữa hai bo mạch chưa tích hợp.

Bảng dưới đây liệt kê các rủi ro đã nhận diện được, cùng phương án dự phòng. Đây là rủi ro của việc thực hiện đề tài, không phải rủi ro lâm sàng.

| Rủi ro | Hệ quả nếu xảy ra | Phương án dự phòng | Trạng thái |
|---|---|---|---|
| Chưa mua được 3 cảm biến gập Flex trước mốc 1 | không hiệu chuẩn được biên độ gập, chỉ số GAP mất đại lượng đọc trong găng | mua sớm ngay đầu mốc 1; nếu không kịp thì chạy trước các phép kiểm của màng áp trở và mạch thu nhận, dời phép kiểm Flex về cuối mốc 1 | chưa có cảm biến |
| Tình trạng bộ chuyển đổi ADS1115 chưa xác nhận | không dựng được chuỗi đo hiện hành, mọi phép kiểm ở C.2 và C.3 dừng lại | xác nhận ngay trong tuần; nếu chưa có thì đưa vào danh sách mua cùng Flex | chưa xác nhận |
| Ngưỡng vùng chết 180 mV triệt tiêu tín hiệu nỗ lực sớm | chỉ số EI không đo được, tức mất chỉ số chính của đề tài | xác định lại ngưỡng từ phân bố nhiễu từng kênh ở phép kiểm bốn của C.2; kiểm tra riêng tín hiệu nỗ lực sớm có sống sót sau vùng chết hay không | đã nhận diện, chưa đo |
| Sai số và trễ đàn hồi của màng áp trở vượt mức dùng được | chỉ số áp lực chỉ còn giá trị định tính | đã chấp nhận từ đầu: chỉ dùng chỉ số tương đối trong cùng người, không quy đổi ra lực; nếu trễ vượt 18% thì báo cáo là không đạt và thu hẹp phạm vi tuyên bố | đã chấp nhận giới hạn |
| Hành vi nhả dây khi mất nguồn không như giả định | mất đường thoát an toàn chủ động | đã chuyển thành đại lượng phải đo ở C.5; đường thoát an toàn chính là chốt mở nhanh cơ khí, không phụ thuộc điện | phải đo ở mốc 2 |
| Người tập có co cứng cơ gập nặng, duỗi thụ động không đủ | chiều duỗi của cơ cấu không hoàn thành chức năng | đây là điểm chưa chốt: hoặc ghi rõ giới hạn, hoặc bổ sung dải nẹp đàn hồi ở mặt mu, hoặc tuyên bố trợ lực duỗi ngoài phạm vi nguyên mẫu | **chờ quyết định** |
| Nhánh thị giác không đạt trên đúng phần cứng | mốc 3 trễ, bài tập thìa không có nhãn tác vụ | bộ nhận biết viết theo dạng thay thế được, bắt đầu bằng xử lý ảnh cổ điển; nếu không đạt thì mới xét mô hình học sâu; trường hợp xấu nhất thì đánh giá tác vụ bằng nhãn thủ công và ghi rõ | chưa đo thử |
| Giao tiếp giữa hai bo mạch chưa tích hợp | không có phiên tích hợp đầy đủ | đã tách thành pha riêng trong lộ trình; phiên tích hợp chỉ cần nhãn tác vụ ở mức tối thiểu nên có thể chạy với giao tiếp đơn giản trước | chưa tích hợp |
| phương án khóa 9 chưa được đo độ bền | khóa nẹp có thể hỏng trong liệu trình dài | đã chuyển thành chỉ tiêu của mốc 2 với số chu kỳ lớn hơn nhiều so với 50; phương án dự phòng là nhóm khóa phương án khóa 4–6 nếu phương án khóa 9 hỏng sớm | phải đo ở mốc 2 |
| Nguồn trích dẫn chưa đọc toàn văn | nhận định lý thuyết ở A.1 và B.7 có thể sai khi đối chiếu | đã liệt kê trong phụ lục nguồn chờ xác minh; phải đọc toàn văn hoặc bỏ nhận định trước khi nộp | còn nợ |
| Mốc 3 và phiên tích hợp trễ tiến độ | không có bảng so sánh trợ lực cố định với trợ lực theo nhu cầu | đã tuyên bố từ đầu là có rủi ro trễ; phần chắc chắn hoàn thành là mốc 0, mốc 1, bản vẽ cơ khí và cụm ba tang thử trên mô hình bàn tay giả | đã khai báo |

Bảng dưới đây tổng hợp toàn bộ chỉ tiêu của bảy mục kiểm thử trên, để đối chiếu với tiêu chí ở A.4.

| Chỉ số | Cách đo | Mục tiêu | Căn cứ |
|---|---|---|---|
| Tỷ lệ hoàn thành tác vụ; thời gian; số lần rơi hoặc đặt sai | nhãn camera và nhật ký trên đồng hồ thời gian chung | chưa xác định | lượt thử đầu trên mô hình bàn tay giả (C.6) |
| Tỷ lệ nhãn không xác định; độ đúng nhãn trạng thái | nhật ký nhãn; bảng nhầm lẫn so với nhãn thủ công | chưa xác định | đo thử nhánh thị giác trên Orange Pi 5 Pro (C.6) |
| Độ trễ thị giác đầu – cuối | dấu thời gian hai đầu | chưa xác định | đo trên phần cứng thật (C.6) |
| Tốc độ khung thu thập | đếm số hiệu khung | không thấp hơn 20 Hz | tính toán khoảng 35 Hz (C.3) |
| Trễ cảm biến đến lệnh servo | nhật ký đồng bộ | không quá 20 ms | đo trên bàn thử (C.5) |
| Chuyển pha đúng và sai; trợ lực sai pha | nhật ký pha vận hành và nhãn đối chiếu | chưa xác định | phương pháp cửa sổ thăm dò (C.5) |
| Biên độ và độ lặp lại chu kỳ gập – duỗi | nhật ký cảm biến Flex và thước đo góc | hệ số biến thiên không quá 5% nội phiên, 8% liên ngày | mốc 1 (C.2, C.4) |
| Trôi tín hiệu | nhật ký hai ô tham chiếu | chưa xác định | mốc 1, chuỗi nhật ký ≥ 10 ngày (C.2) |
| Tỷ số tín hiệu trên nhiễu và độ tuyến tính | băng thử trục trượt và tải chuẩn | không thấp hơn 18 dB và R² không thấp hơn 0,90 | mốc 1 (C.2, C.3) |
| Trễ đàn hồi, dãn tải tĩnh, nhiễu nền | băng thử | trễ đàn hồi không quá 18%; dãn tải sau 60 s không quá 8%; nhiễu không quá 5 mV đỉnh – đỉnh sau lọc | mốc 1 (C.2, C.3) |
| Độ nhạy riêng của từng nguồn đo | tắt lần lượt Flex, Velostat, camera rồi đủ cả ba | chưa xác định | mốc 3 và tích hợp (C.6) |
| Thời gian tự đeo, thời gian tháo, độ bền khóa nẹp | bấm giờ có biên bản, đếm chu kỳ đóng mở | chưa xác định | mốc 2 (C.1) |
| Khối lượng cụm đeo | cân thật, ghi ngày | 80–120 g | cân sản phẩm hoàn chỉnh (C.1) |
| Chi phí vật tư | bảng vật tư có ngày và báo giá | dự toán 1,0–1,3 triệu đồng cho cụm đeo, khoảng 5,5 triệu đồng cho toàn hệ thống | kiểm toán bảng vật tư |

### 9. Kết luận

**Đã làm:** in thử và so sánh 9 phương án khóa nẹp, chọn phương án khóa 9; hoàn thành 2 vòng lặp thiết kế mạch thu nhận, xác định nguyên nhân bão hòa ngõ vào ở vòng 1 và chuyển sang đọc trực tiếp qua tầng khuếch đại lập trình được của ADS1115.

Xác định chuỗi xử lý bốn bước cùng bộ tham số đang dùng; chọn cấu hình cảm biến 11 kênh quét và cơ cấu ba tang với duỗi chủ động bằng nhả dây; xây dựng định nghĩa EI, GAP, RAL cùng bảng tiêu chí kỹ thuật đặt trước khi đo; đặc tả ba pha vận hành và phương pháp cửa sổ thăm dò.

Các kết quả trên là quan sát trên bàn đo, chưa lập biên bản đo chính thức.

**Chưa làm:** mua 3 cảm biến gập Flex; chế tạo cụm cảm biến theo cấu hình đã chọn; bấm giờ thời gian tự đeo của phương án khóa 9; biên bản đo cho tỷ số tín hiệu trên nhiễu, độ tuyến tính, tốc độ khung và độ lặp lại; đo độ bền mỏi phương án khóa 9 theo quy trình; xuất và lưu bản vẽ CAD; cân khối lượng cụm đeo; kiểm toán chi phí; viết phần mềm cho vi điều khiển và các mô-đun xử lý; đo thử nhánh thị giác; kiểm chứng quy tắc cửa sổ thăm dò; thử nghiệm trên người.

**Giới hạn:** kết quả trên bàn đo và mô hình bàn tay giả chưa nói được hiệu quả trên người; dữ liệu trên người khỏe không thay thế dữ liệu trên người bệnh.

Trợ lực theo nhu cầu là nền tảng có sẵn trong y văn; đề tài dùng nó làm cơ sở chọn đại lượng đo và đặt câu hỏi kiểm thử. Cảm biến áp trở chỉ cho chỉ số tương đối trong cùng người, không dùng làm thiết bị đo lực hay cơ chế an toàn.

### 10. Hướng phát triển

- **Phần cứng:** thay hệ dây dẫn rời bằng mạch in mềm đi chìm trong nẹp in 3D để tăng độ bền cơ học, chống đứt gãy và tăng tính thẩm mỹ; mở rộng từ 3 ngón lên 5 ngón sau khi có dữ liệu hiệu chuẩn đủ tin cậy.
- **Quy chuẩn y sinh và thử nghiệm lâm sàng:** sau khi hoàn tất các mốc kiểm định an toàn kỹ thuật trên giàn đo cơ học và mô hình bàn tay giả silicone, xây dựng hồ sơ xin phê duyệt của Hội đồng Đạo đức trong nghiên cứu y sinh học tại cơ sở y tế chuyên khoa trước khi triển khai thử nghiệm đối chứng lâm sàng với thang đo FMA-UE và ARAT; đây là giai đoạn sau, ngoài phạm vi đề tài này.
- **Điều khiển:** cá nhân hóa ngưỡng theo tầm vận động của từng người tập; các phương pháp điều khiển thích ứng nâng cao, kể cả học máy, chỉ xem xét khi đã có bộ dữ liệu bàn thử đủ lớn và quy trình an toàn hoàn chỉnh.

---

## PHỤ LỤC A — THUẬT NGỮ VÀ CÁCH DÙNG TRONG ĐỀ TÀI

Phụ lục này giữ cho cách dùng từ nhất quán giữa các mục, và ghi rõ giới hạn của từng thuật ngữ để tránh tuyên bố vượt quá những gì thiết bị làm được.

| Thuật ngữ | Cách dùng trong đề tài | Giới hạn |
|---|---|---|
| Hỗ trợ gập duỗi | Chế độ dự kiến hỗ trợ vận động ngón khi người tập chưa tự hoàn thành được | Cơ cấu tạo gập, nhả và đưa ngón duỗi trở lại chưa được xác nhận an toàn |
| Trợ lực theo nhu cầu | Trợ lực khi người tập chủ động cố gắng vận động nhưng cần hỗ trợ bổ sung | Quy tắc điều khiển và giới hạn vận hành còn phải chốt và kiểm chứng |
| Chuyển pha tự động theo ngưỡng | Bộ điều khiển tự chuyển từ trợ lực toàn phần sang trợ lực theo nhu cầu khi tiêu chí tín hiệu đã định trước được thỏa mãn | Không dùng thao tác của kỹ thuật viên; đặc trưng, ngưỡng, cửa sổ, độ trễ phản hồi và hành vi dự phòng chưa chốt và phải khóa trước khi đánh giá |
| Bài tập mức tác vụ | Gắp thìa bằng ngón cái, trỏ và giữa, nhấc, di chuyển đến vùng đích rồi thả | Kích thước thìa, cách gắp, vùng đích và quy trình cần chuẩn hóa |
| Phản hồi thị giác | Màn hình cho người tập biết vật, đích, tiến trình và kết quả thao tác | Không phải thang đánh giá lâm sàng, không chứng minh phục hồi thần kinh |
| Ba cảm biến gập | Một cảm biến trên từng ngón cái, trỏ, giữa để theo dõi biến thiên gập duỗi và tư thế | Cần hiệu chuẩn từng cảm biến trên vị trí lắp thật; không mặc định đầu ra đã là góc giải phẫu chính xác |
| Màng áp trở | Vật liệu áp trở tự chế để ghi nhận thay đổi áp lực và tiếp xúc tại vị trí lắp | Không tự đọc ý định, không đo góc, không cho lực tuyệt đối theo đơn vị Newton |
| Chỉ số nỗ lực | Đặc trưng tín hiệu màng áp trở đã xử lý, mô tả biến thiên tương đối trong một cấu hình và một phiên đã xác định | Công thức và cửa sổ còn mở; không quy đổi sang Newton hay phần trăm lực co cơ tối đa khi chưa có phương pháp được kiểm chứng |
| Đọc vi sai | Hiệu tín hiệu giữa hai màng đối diện nếu cấu hình thực sự có cặp | Có thể giảm thành phần chung; không đồng nghĩa loại bỏ mọi độ trôi |
| Nhãn trạng thái tác vụ | Ước lượng vị trí thìa, vùng đích, tiến trình và kết quả nhìn thấy được của tác vụ | Không đo lực ngón, không đo góc khớp chính xác, không phản ánh tình trạng lâm sàng |
| Khoảng cách theo đơn vị thật | Khoảng cách và vị trí theo đơn vị thực trong không gian đã hiệu chuẩn | Khoảng cách suy ra từ một ảnh không tự động là tọa độ thật; cần hiệu chuẩn và vật chuẩn tỷ lệ |
| Mười sáu kênh | Mục tiêu thu nhận qua một bộ chuyển mạch cho vùng ba ngón | Phải phân bổ cả cảm biến gập và màng áp trở; nếu vượt mười sáu thì phải sửa phần thu nhận chứ không giả định có kênh miễn phí |
| Chênh lệch chủ động thụ động | Câu hỏi nghiên cứu về chênh lệch giữa tầm vận động thụ động và tầm vận động chủ động | Cần phương pháp đo góc độc lập và được kiểm chứng; không lấy góc từ màng áp trở |
| Mức trợ giúp cần thiết | Chỉ số mức trợ giúp còn thiếu mà cơ cấu phải bù | Chưa có công thức và đơn vị hiện hành; định nghĩa cũ dựa trên lò xo và nấc tải đã bỏ |

Những cách nói sau đây bị tránh trong toàn bộ tài liệu, và được thay bằng cách diễn đạt chính xác hơn.

| Tránh | Dùng cách diễn đạt chính xác hơn |
|---|---|
| Màng áp trở đọc được ý định | Màng áp trở đo biến thiên áp lực và tiếp xúc; bộ điều khiển suy luận trạng thái từ mẫu tín hiệu và ngữ cảnh |
| Màng áp trở đo chính xác lực | Màng áp trở tạo tín hiệu áp trở tương đối; lực tuyệt đối cần phép đo tham chiếu độc lập |
| Đã tự động chuyển pha đạt ngưỡng nào đó, khi chưa đo | Quy tắc và ngưỡng đang thiết kế, chưa đo thử |
| Trí tuệ nhân tạo xác định độ sâu chính xác | Chỉ nêu độ sâu và độ chính xác khi có hiệu chuẩn và đo thử trên cấu hình thật |
| Đã phục hồi rõ rệt hoặc tăng tái tổ chức thần kinh | Đây là giả thuyết dài hạn; đề tài hiện chỉ kiểm tra chức năng tác vụ |
| Đã dùng an toàn tại nhà | Chỉ nêu là bối cảnh sử dụng dự kiến cho tới khi có nghiên cứu phù hợp |
| Có tính mới hoặc là đầu tiên | Trình bày vấn đề, thiết kế và kiểm chứng; không kết luận tính mới trước khi rà soát |
| Kết quả đạt một giá trị nào đó, khi mới là kế hoạch | Mục tiêu hoặc tiêu chí cần đạt giá trị đó |

---

## PHỤ LỤC B — BỘ NHÃN TRẠNG THÁI TÁC VỤ

Bộ nhãn dưới đây dùng chung cho camera, bộ điều khiển và nhật ký. Mỗi nhãn phải có nguồn bằng chứng khai báo trước; nhãn không có bằng chứng quan sát được thì không được gán.

| Nhãn | Mô tả | Nguồn bằng chứng chính | Bằng chứng bổ sung | Điều kiện gán được |
|---|---|---|---|---|
| Sẵn sàng | Tay ở vị trí bắt đầu, thìa ở vùng xuất phát | Camera | Cảm biến gập ở mốc duỗi | Cả hai điều kiện cùng đạt |
| Tiến lại | Các ngón tiến về cán thìa | Camera | Tín hiệu gập tăng dần | Không ràng buộc thêm |
| Tiếp xúc | Có tiếp xúc giữa ngón và thìa | Camera, nếu quan sát được | Biến thiên tín hiệu màng áp trở | Nếu camera không phân biệt được thì để nhãn chưa xác nhận, không suy từ màng áp trở một mình |
| Giữ | Thìa được giữ ổn định giữa ba ngón | Camera | Cảm biến gập và màng áp trở | Tiêu chí giữ ổn định chưa chốt |
| Nhấc | Thìa rời bề mặt, cao hơn một ngưỡng | Camera | Không có | Ngưỡng chiều cao chưa chốt |
| Di chuyển | Thìa đang di chuyển về vùng đích | Camera | Không có | Không có; vận tốc ghi trong nhật ký là vận tốc ảnh nếu chưa hiệu chuẩn tỷ lệ |
| Đặt | Thìa được đặt xuống vùng đích | Camera | Không có | Không có; nhật ký ghi mã vùng đích |
| Nhả | Thìa rời tay | Camera | Tín hiệu gập và màng áp trở giảm | Tiêu chí chưa chốt |
| Hoàn thành | Đặt đúng vùng đích rồi nhả | Camera | Không có | Chỉ gán sau nhãn đặt và nhãn nhả; nhật ký ghi thời gian tác vụ |
| Rơi khi nhấc hoặc di chuyển | Thìa rơi giữa chừng | Camera | Không có | Nhật ký ghi pha xảy ra rơi |
| Đặt sai vùng đích | Thìa được đặt ngoài vùng đích | Camera | Không có | Không có |
| Chưa xác nhận | Không đủ bằng chứng do che khuất, mất vật thể hoặc độ tin cậy thấp | Camera | Không có | Đây là nhãn mặc định khi không gán được nhãn khác; phải đếm và báo cáo riêng |
| Tín hiệu không hợp lệ | Tín hiệu cảm biến ngoài dải hợp lệ hoặc trôi vượt mức cho phép | Phần thu nhận | Không có | Dải hợp lệ xác định ở mốc 1; nhật ký ghi kênh lỗi |

---

## PHỤ LỤC C — PHƯƠNG PHÁP CỬA SỔ THĂM DÒ VÀ CÁC THÔNG SỐ CHƯA CHỐT

Đây là điểm rủi ro logic cao nhất của việc chuyển pha tự động: nếu bộ điều khiển đếm chu kỳ do chính cơ cấu tạo ra, nó sẽ tự thăng cấp cho người tập không có vận động chủ động. Phương pháp làm việc đã chọn là cửa sổ thăm dò tự nguyện: bộ điều khiển tạm ngưng trợ lực trong một khoảng ngắn, đo đáp ứng của người tập trong khoảng đó, rồi quyết định có chuyển pha hay không.

Chọn phương pháp không đồng nghĩa với việc đã có quy tắc. Sáu thông số sau vẫn chưa chốt và phải chốt bằng quyết định có ngày hoặc bằng dữ liệu bàn đo và mô hình bàn tay giả: độ dài cửa sổ ngưng trợ lực, xác định bằng thử trên mô hình kèm rà soát an toàn; tần suất mở cửa sổ, theo mỗi chu kỳ, mỗi khoảng thời gian hay theo pha tác vụ; tiêu chí coi là có đáp ứng tự nguyện trong cửa sổ, gồm đặc trưng và ngưỡng, và chỉ đặt được sau khi có dữ liệu hiệu chuẩn ở mốc 1; hành vi khi cửa sổ hết mà không thấy đáp ứng, là giữ trợ lực toàn phần, giảm dần, hay về trạng thái dừng an toàn; giới hạn hành trình và cơ cấu nhả phải bảo vệ được khoảng ngưng này; và số lần lặp tối thiểu trước khi chuyển từ trợ lực toàn phần sang trợ lực theo nhu cầu.

Ràng buộc an toàn: ngưng trợ lực giữa chừng là hành vi có thể làm thay đổi tải lên ngón, nên không chạy phương pháp này trên người, kể cả người khỏe, trước khi có rà soát an toàn và phê duyệt theo quy trình đã viết; mọi lần thử trong giai đoạn này là trên giàn thử và mô hình bàn tay giả. Giới hạn đã biết: phương pháp này chỉ thấy đáp ứng tạo ra chuyển động, còn nỗ lực đẳng trường, tức gồng mà không dịch chuyển, có thể không bị phát hiện; vì vậy có thể cần một lớp kiểm tra chéo bằng chuỗi thử có trợ lực và không trợ lực xen kẽ trên mô hình, hoặc bằng pha tác vụ từ camera. Việc kết hợp này chưa được duyệt.

Bốn phương pháp ứng viên khác được giữ lại để đối chiếu, chưa chọn: chuỗi thử có và không trợ lực xen kẽ trên mô hình, so biên độ tín hiệu gập khi cơ cấu ra lệnh và khi cơ cấu im, điểm yếu là chưa tự động áp dụng được cho người thật nếu chưa xác nhận; dùng lệnh điều khiển cơ cấu làm biến giải thích, phần biên độ gập không giải thích được bởi lệnh đó coi là đóng góp của người tập, điểm yếu là trễ cơ khí và đàn hồi dây có thể làm sai phần dư nên phải đo trễ; đối chiếu pha tác vụ từ camera, điểm yếu là camera không thấy được nỗ lực không tạo ra chuyển động; và tín hiệu dòng hoặc mô-men của động cơ làm đại lượng thay thế tải cơ học, điểm yếu là đó là phép đo cơ cấu chứ không phải lực ngón, không thay được tham chiếu lực độc lập.

---

## PHỤ LỤC D — BẢN ĐỒ MƯỜI SÁU KÊNH THU NHẬN

Cấu hình đã chọn phân bổ mười một kênh có tín hiệu và năm kênh dự phòng trên một bộ chuyển mạch mười sáu kênh. Vị trí lắp của tất cả các kênh đều chưa chốt và phải xác nhận bằng hiệu chuẩn trên vị trí lắp thật.

| Kênh | Vai trò tín hiệu | Ngón | Vị trí lắp đề xuất | Loại cảm biến | Mạch đầu vào |
|---|---|---|---|---|---|
| 0 | Gập ngón cái | Cái | Dọc đốt ngón cái, mặt mu, không tì vào nếp gấp da | Cảm biến gập áp trở | Cầu phân áp, qua bộ chuyển mạch, vào bộ chuyển đổi có khuếch đại |
| 1 | Gập ngón trỏ | Trỏ | Dọc đốt một đến hai ngón trỏ, mặt mu | Cảm biến gập áp trở | Như trên |
| 2 | Gập ngón giữa | Giữa | Dọc đốt một đến hai ngón giữa, mặt mu | Cảm biến gập áp trở | Như trên |
| 3 | Áp lực ngón cái, mặt lòng | Cái | Mặt lòng, vùng tiếp xúc cán thìa dự kiến | Màng áp trở | Kéo lên mười kilôôm, qua bộ chuyển mạch, vào bộ chuyển đổi |
| 4 | Áp lực ngón cái, mặt mu | Cái | Mặt mu, đối diện kênh 3 | Màng áp trở | Như trên; là kênh đối chiếu của cặp đọc vi sai |
| 5 | Áp lực ngón trỏ, mặt lòng | Trỏ | Mặt lòng đốt một đến hai | Màng áp trở | Như trên |
| 6 | Áp lực ngón trỏ, mặt mu | Trỏ | Mặt mu, đối diện kênh 5 | Màng áp trở | Như trên; kênh đối chiếu của cặp đọc vi sai |
| 7 | Áp lực ngón giữa, mặt lòng | Giữa | Mặt lòng đốt một đến hai | Màng áp trở | Như trên |
| 8 | Áp lực ngón giữa, mặt mu | Giữa | Mặt mu, đối diện kênh 7 | Màng áp trở | Như trên; kênh đối chiếu của cặp đọc vi sai |
| 9 | Tham chiếu một | Không | Trên nẹp cổ tay, không chịu tải người dùng | Màng áp trở dùng làm ô tham chiếu | Như trên; theo dõi độ trôi của hệ thống |
| 10 | Tham chiếu hai | Không | Cạnh kênh 9, không chịu tải | Màng áp trở dùng làm ô tham chiếu | Như trên; kiểm tra chéo độ trôi giữa hai ô |
| 11 đến 14 | Dự phòng | Không | Chưa gán | Không | Không; dùng để dự phòng hoặc thử vị trí màng áp trở mới; nếu dùng cho cảm biến nhiệt độ và độ ẩm thì phải chốt loại cảm biến |
| 15 | Kiểm tra xuyên kênh | Không | Nối mass | Không | Không; dùng để đo hiện tượng bóng ma và xuyên kênh giữa các nhóm kênh |

Ba kênh cảm biến gập ở cấu hình này không trùng với phương án nối trực tiếp ba cảm biến gập vào ba đầu vào phụ của bộ chuyển đổi, là phương án đã không được chọn; nếu muốn đổi sang phương án đó thì phải xét duyệt lại bản đồ kênh.

---

## PHỤ LỤC E — NHẬT KÝ PHIÊN ĐO TỐI THIỂU

Từ mốc 1 trở đi, mỗi phiên phải có phiếu buổi đo và các bản ghi chứa những trường sau.

Phiếu buổi đo gồm mã phiên bàn thử, thời điểm bắt đầu theo giờ quốc tế, mã người vận hành chứ không định danh người tham gia, mã phiên bản phần mềm nhúng, mã phiên bản phiên bản cấu hình, và phiên bản bố trí lắp đặt.

Phần dữ liệu thô gồm giá trị số hóa từng kênh và dấu thời gian lúc lấy mẫu, trên một đồng hồ chung. Phần dẫn xuất gồm đặc trưng của cảm biến gập và màng áp trở, cùng cờ hợp lệ của từng kênh. Phần điều khiển gồm pha vận hành, nhãn tác vụ, độ tin cậy, lệnh điều khiển động cơ, và giới hạn hành trình đang áp dụng. Phần tham chiếu độc lập, nếu có, gồm tên thiết bị, giá trị đo và bản ghi hiệu chuẩn của thiết bị đó. Phần kết quả gồm nhãn tác vụ, thời gian, sự kiện rơi hoặc thử lại, sự kiện trợ lực, và sự kiện dừng hoặc nhả.

Một trường bắt buộc nữa là khai báo nguồn dữ liệu: bàn đo thật, mô hình bàn tay giả, hay mô phỏng. Trường này bắt buộc để không lẫn dữ liệu mô phỏng với số đo thật. Tệp nhật ký gốc không bao giờ bị sửa; bản tính lại được đặt tên riêng để phân biệt.

---

## PHỤ LỤC F — NGUỒN CHỜ XÁC MINH TOÀN VĂN

Các nhận định sau đây đang dựa trên nguồn mà nhóm mới đọc ở mức tóm tắt hoặc chưa xác minh. Phải đọc toàn văn, bổ sung số thứ tự vào danh sách tài liệu tham khảo, hoặc bỏ nhận định, trước khi nộp hồ sơ.

- Hai kịch bản ở mục A.1: chuỗi tiến triển teo cơ, xơ hóa mô kẽ, mất cân bằng nhóm gập – duỗi, co rút và dính khớp; hiện tượng vùng biểu diễn bàn tay bị lấn chiếm; tác dụng ngắn hạn của kéo thụ động nhịp nhàng lên trương lực cơ.
- Các dòng bằng chứng trong bảng so sánh ở mục B.7: tổng quan gộp theo chế độ tập cho thấy chế độ thụ động không có lợi ích thêm so với nhóm chứng; các chế độ có thành phần chủ động cho thấy lợi ích; thử nghiệm lớn trên robot chi trên không thấy khác biệt về thang ARAT ở thời điểm 3 tháng; hiệu quả giảm khi co cứng nặng.
- Hiệu ứng ỷ lại là thích nghi học được chứ không phải phản xạ tức thời, và đề xuất tách hai kênh điều khiển gồm độ lợi trợ giúp và độ lợi phản ánh mức tham gia.
- Mức trần thương mại của nhóm thiết bị chỉ gồm cảm biến và trò chơi phản hồi cho cùng mục đích: có tồn tại sản phẩm như vậy, nhưng giá bán và chỉ định sử dụng chưa được xác minh nên chưa nêu trong thân bài.

Ba khoản nợ khác của danh sách tài liệu tham khảo hiện hành: mục [2] Quyết định 4039/QĐ-BYT, mục [3] giáo trình Phục hồi chức năng và mục [6] tổng quan của Langhorne chưa được đối chiếu toàn văn; mục [8] Amin 2024 đang mâu thuẫn giữa sổ nguồn của nhóm, ghi tạp chí IEEE OJEMB, và bản đề cương cũ, ghi tạp chí Sensors với mã PMC11793859 — phải chốt một trong hai trước khi nộp.

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
