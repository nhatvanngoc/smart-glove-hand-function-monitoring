# ĐỀ CƯƠNG DỰ ÁN KHOA HỌC KỸ THUẬT

**Tên dự án:** *Nghiên cứu và phát triển găng tay hỗ trợ phục hồi chức năng sau đột quỵ cho vận động tinh.*

Lĩnh vực: ………………………………… · Đơn vị: …………………………………

Thành viên: ………………………………… · Người hướng dẫn: …………………………………

---

## MỤC LỤC

**A. VẤN ĐỀ NGHIÊN CỨU**

1. Lý do chọn đề tài

2. Xác định vấn đề nghiên cứu

3. Mục tiêu nghiên cứu

4. Tiêu chí của dự án

5. Đối tượng và phạm vi nghiên cứu

6. Địa điểm nghiên cứu và thực nghiệm

7. Phương pháp nghiên cứu

**B. GIẢI PHÁP VÀ THIẾT KẾ**

1. Tổng quan đề tài và cơ sở lý thuyết

2. Bất cập của các giải pháp hiện tại và hướng tiếp cận của đề tài

3. Khung nẹp ngón tay và khóa đeo

4. Màng cảm biến áp lực và cảm biến gập

5. Mạch thu nhận và thuật toán xử lý tín hiệu

6. Bộ chỉ số đánh giá tiến triển và kiểm soát chất lượng số liệu

7. Cơ cấu trợ lực và ba pha vận hành

8. Nhánh thị giác và bài tập gắp thìa

**C. KIỂM TRA VÀ KIỂM THỬ**

1. Kiểm tra và kiểm thử khung nẹp và khóa đeo

2. Kiểm tra và kiểm thử màng cảm biến áp lực và cảm biến gập

3. Kiểm tra và kiểm thử mạch thu nhận và thuật toán xử lý tín hiệu

4. Kiểm tra và kiểm thử bộ chỉ số EI – GAP – RAL

5. Kiểm tra và kiểm thử cơ cấu trợ lực và ba pha vận hành

6. Kiểm tra và kiểm thử nhánh thị giác và bài tập gắp thìa

7. Phương tiện, tình trạng thiết bị, mốc thực hiện và bảng tổng hợp chỉ tiêu

8. Kết luận

9. Hướng phát triển

**TÀI LIỆU THAM KHẢO**

**PHỤ LỤC — DANH MỤC HÌNH CẦN BỔ SUNG**

---

## A. VẤN ĐỀ NGHIÊN CỨU

### 1. Lý do chọn đề tài

Đột quỵ là một trong những nguyên nhân hàng đầu gây tàn tật ở Việt Nam, với tỷ lệ hiện mắc năm 2019 khoảng 1.541 ca trên 100.000 dân và mỗi năm thêm khoảng 222 ca mới trên 100.000 dân [1]. Hình 1 minh họa tỷ lệ đột quỵ và di chứng bàn tay kéo dài tại Việt Nam.

Tổng quan của Cochrane ghi nhận khoảng 80% người sống sót bị suy giảm vận động, và trong nhóm liệt hoàn toàn chi trên chỉ khoảng một nửa phục hồi được một phần chức năng sau 6 tháng [5, 6]. Bàn tay hồi phục chậm nhất và khó nhất, vì tay phải làm được các động tác tinh như cầm thìa, cài cúc áo, cầm bút chứ không chỉ co duỗi.

Việc theo dõi quá trình tập luyện đó gần như chưa được định lượng: thang khám lâm sàng FMA-UE và ARAT có tính gián đoạn, vài tuần một lần và phụ thuộc người khám; thiết bị đeo cổ tay Manumeter muốn phát hiện tiến triển thì người đeo phải thay đổi tới khoảng 31% cường độ sử dụng trong ngày, đồng thời đếm sai 100–200 lần dương tính giả mỗi giờ [7].

Khảo sát của nhóm tại cơ sở phục hồi chức năng tháng 9 năm 2026 ghi nhận các loại găng hiện có chưa phù hợp điều kiện tập tại nhà ở Việt Nam về giá thành, khối lượng và thao tác đeo.

Từ những thực tế trên, nhóm nghiên cứu chế tạo găng tay nẹp ba ngón hỗ trợ người tập đi từ vận động gập – duỗi đến thao tác **gắp thìa bằng ngón cái, trỏ, giữa**, thay vì chỉ đếm chuyển động hoặc kéo thụ động theo chu kỳ định sẵn.

### 2. Xác định vấn đề nghiên cứu

Vấn đề đặt ra là liệu mảng cảm biến gập và cảm biến áp trở đặt trên khung nẹp ba ngón có tạo được tín hiệu đủ lặp lại để phát hiện vận động chủ động của người tập hay không, và liệu cơ cấu servo – dây cáp – ba tang có tạo được dạng kẹp ba chấu với mức trợ lực tự giảm dần hay không.

Nhóm tập trung vào sáu nội dung: khung nẹp ba ngón tích hợp 3 cảm biến gập Flex và 6 ô áp trở Velostat bố trí theo cặp lòng – mu; mạch thu nhận và thuật toán lọc tín hiệu; bộ chỉ số đánh giá tiến triển gồm EI, GAP và RAL cùng chỉ số của bài tập; cơ cấu ba tang với chiều duỗi thực hiện bằng nhả dây chủ động; quy tắc tự động chuyển pha trợ lực và nhánh thị giác cho bài tập gắp thìa; quy trình kiểm chứng trên giàn đo cơ học và mô hình bàn tay giả.

Hai câu hỏi khó nhất là: trong phép thử có tải và điều kiện xác định, tín hiệu áp trở từ hai vách lòng – mu có phân biệt được hướng vận động với độ tin cậy chấp nhận được và có tự phát hiện được phiên đo lỗi do đeo nẹp lỏng hay không; và bộ điều khiển có phân biệt được vận động do người tập khởi xướng với chuyển động do chính cơ cấu tạo ra hay không.

### 3. Mục tiêu nghiên cứu

Mục tiêu tổng quát là chế tạo và đánh giá được nguyên mẫu găng tay nẹp ba ngón hoạt động ổn định trên bàn thử, với bộ số liệu đo lường dùng được cho việc theo dõi vận động tinh của bàn tay.

Mục tiêu cụ thể gồm ba phần: hoàn thiện phần đeo, tức khung nẹp có khóa mà người yếu tay tự đeo được bằng một tay, cụm cảm biến 11 kênh đọc ổn định và khối lượng nhẹ; hoàn thiện phần trợ lực, tức cơ cấu ba tang tạo được dạng kẹp ba chấu, trợ lực giảm dần theo đáp ứng của người tập và có đường thoát an toàn; hoàn thiện phần đánh giá, tức bộ chỉ số EI, GAP, RAL cùng chỉ số bài tập thìa và quy trình kiểm soát chất lượng số liệu. Nguyên mẫu được kiểm chứng trên thiết bị đo và mô hình bàn tay giả.

### 4. Tiêu chí của dự án

Nhóm đặt các mục tiêu kỹ thuật sau cho nguyên mẫu.

- Tốc độ khung khi quét 11 kênh không thấp hơn 20 Hz; tỷ số tín hiệu trên nhiễu không thấp hơn 18 dB và hệ số xác định R² không thấp hơn 0,90 trên tải chuẩn.
- Phân biệt đúng hướng vận động không thấp hơn 90%; phân loại đúng mức kích hoạt không thấp hơn 85%.
- Hệ số biến thiên không vượt quá 5% trong cùng buổi và 8% giữa các ngày; trễ đàn hồi không quá 18%; độ dãn tải tĩnh sau 60 giây giữ tải không quá 8%; nhiễu nền sau lọc không quá 5 mV đỉnh – đỉnh.
- Trễ từ cảm biến đến lệnh servo không vượt quá 20 ms; chỉ tiêu này không áp dụng cho nhãn tác vụ từ camera.
- Giới hạn an toàn đặt theo hành trình dây, góc kéo và chốt mở nhanh trên nẹp; không dùng ngưỡng lực suy ra từ cảm biến áp trở làm cơ chế an toàn.
- Khóa nẹp cho phép thao tác bằng một tay; đánh giá bằng thời gian tự đeo, tự tháo và số chu kỳ đóng mở.
- Đánh giá bài tập thìa bằng tỷ lệ hoàn thành và độ đúng của nhãn trạng thái từ camera.
- Khối lượng cụm đeo 80–120 gam.
- Thử khả năng tự đeo và bắt tín hiệu vận động tự nguyện ở người tình nguyện khỏe mạnh, theo quy trình an toàn được phê duyệt trước.

### 5. Đối tượng và phạm vi nghiên cứu

- **Con người:** số liệu thống kê về đột quỵ và di chứng vận động bàn tay; khó khăn của người tập trong sinh hoạt và khi tự tập tại nhà, làm cơ sở chọn bài tập gắp thìa làm đơn vị đánh giá.
- **Lịch sử đề tài:** 9 phương án khóa nẹp đã in, kết quả đeo thử các phương án trước và 2 vòng lặp thiết kế mạch thu nhận, và các hệ găng tay phục hồi chức năng đã công bố.
- **Giải pháp kỹ thuật:** cảm biến gập và cảm biến áp trở, mạch chuyển đổi tương tự – số, thuật toán lọc số, cơ cấu truyền động bằng dây cáp, nguyên lý trợ lực theo nhu cầu, xử lý ảnh nhận biết vật dụng, lập trình vi điều khiển và in 3D.
- **Phạm vi:** đề tài dừng ở nguyên mẫu và kiểm chứng trên bàn thử cùng mô hình bàn tay giả; việc thử có cấp nguồn trên người chỉ xem xét với người trưởng thành khỏe mạnh sau khi rà soát an toàn đạt và có phê duyệt. Đề tài không thử trên người bệnh và không đánh giá hiệu quả điều trị.

### 6. Địa điểm nghiên cứu và thực nghiệm

Phòng thực hành Vật lý và phòng sáng tạo của trường, cùng nhà riêng của các thành viên, dùng để thảo luận ý tưởng, lựa chọn giải pháp, lập trình, in 3D, lắp ráp và vận hành thử nghiệm. Khảo sát thực tế về các loại găng hỗ trợ hiện có được thực hiện tại cơ sở phục hồi chức năng.

### 7. Phương pháp nghiên cứu

Nhóm nghiên cứu kết hợp năm phương pháp sau.

- Phương pháp quan sát ghi nhận cách người yếu tay tự đeo tháo nẹp và cách họ cầm thìa, làm cơ sở cho yêu cầu của khóa nẹp và bài tập đánh giá.
- Phương pháp suy luận logic và lý luận giúp phát triển ý tưởng, lựa chọn giữa các phương án cảm biến và phương án truyền động, xây dựng thuật toán lọc tín hiệu và quy tắc chuyển pha trợ lực.
- Phương pháp thực nghiệm đo lường là chủ đạo: mỗi phương án cơ khí và mỗi vòng lặp mạch đều chế tạo thật rồi đo thật, so với phương án trước và ghi lại nguyên nhân khi không đạt.
- Phương pháp thống kê dùng để đánh giá độ tin cậy của phép đo thông qua hệ số biến thiên, sai số chuẩn của phép đo và ngưỡng khác biệt nhỏ nhất có ý nghĩa [7].
- Phương pháp mô hình hóa gồm in 3D khung nẹp, dựng mô hình bàn tay giả silicone và giàn đo cơ học tạo tải cùng chuyển động lặp lại được, thay cho thử trên người.

---

## B. GIẢI PHÁP VÀ THIẾT KẾ

### 1. Tổng quan đề tài và cơ sở lý thuyết

Bàn tay chiếm diện tích đại diện vận động rất lớn trên vỏ não theo Penfield & Boldrey [11] và mạng SCAN của Gordon et al. [4]; đó là cơ sở để đề tài tập trung vào ba ngón trụ cột cái, trỏ, giữa thay vì làm cả năm ngón. Hình 2 minh họa bản đồ vận động của Penfield và vùng chi phối bàn tay theo Gordon.

Theo học thuyết Hebb [12] và nguyên lý phục hồi chức năng [2, 3], phản hồi cảm giác đồng thời với nỗ lực vận động giúp định hướng tập luyện. Đề tài khai thác cơ sở này để xây dựng phản hồi thị giác thời gian thực, cho người tập tự quan sát nỗ lực phát lực đọc từ đáp ứng áp trở vi mô.

Sau đột quỵ, suy giảm vận động thường kết hợp giữa yếu cơ và tăng trương lực co cứng [8, 10], nên đề tài khảo sát độ thiếu hụt tầm vận động GAP, tức hiệu giữa tầm vận động thụ động PROM và tầm vận động chủ động AROM, như một chỉ số mô tả mức chênh lệch góc, đo bằng thước đo góc bên ngoài. Độ tin cậy của hệ đo đánh giá qua hệ số biến thiên, sai số chuẩn và ngưỡng khác biệt nhỏ nhất có ý nghĩa [7], làm căn cứ bố trí hai ô tham chiếu và đặt tiêu chí kỹ thuật trước khi đo.

Hệ thống được tổ chức theo kiến trúc phân tán bốn tầng. Tầng đeo là khung nẹp ba ngón in 3D, tích hợp 3 cảm biến gập Flex, 6 ô áp trở Velostat bố trí thành cặp ở mặt lòng và mặt mu của ngón, cùng 2 ô tham chiếu không chịu tải. Tầng thu thập đọc các cảm biến đó qua bộ chuyển mạch CD74HC4067 và bộ chuyển đổi tương tự – số ADS1115 loại 16 bit có tầng khuếch đại lập trình được, rồi xử lý bằng thuật toán lọc số bốn bước trên vi điều khiển ESP32-S3. Tầng trợ lực là cơ cấu trợ lực theo nhu cầu truyền động bằng dây cáp cuốn trên ba tang riêng. Tầng tác vụ chạy trên Orange Pi 5 Pro, dùng camera nhận biết thìa và vùng đích, trích xuất bộ chỉ số tiến triển và hiển thị phản hồi cho người tập. Hình 3 là sơ đồ khối của bốn tầng này.

Điểm khác biệt cốt lõi so với găng kéo thụ động là hệ thống chỉ trợ lực khi nỗ lực chủ động chưa đủ hoàn thành tầm vận động, và tự giảm trợ lực khi phát hiện người tập đã tự khởi xướng chuyển động. Một chu kỳ vận hành gồm: quét 11 kênh, lọc và chuẩn hóa, trích đặc trưng vận động, chọn pha trợ lực, phát lệnh servo có giới hạn, nhận nhãn tác vụ từ camera, rồi ghi nhật ký theo một dấu thời gian chung.

### 2. Bất cập của các giải pháp hiện tại và hướng tiếp cận của đề tài

Việc theo dõi vận động bàn tay ngoài bệnh viện hiện gặp bốn rào cản: thang đo lâm sàng FMA-UE và ARAT gián đoạn, hai đến bốn tuần một lần và phụ thuộc người khám; thiết bị đeo cổ tay Manumeter chỉ đếm chuyển động thô với 100–200 lần dương tính giả mỗi giờ [7]; điện cơ bề mặt sEMG suy giảm chất lượng rõ khi ra mồ hôi và khó tách riêng từng nhóm cơ cẳng tay; găng tay robot thương mại chủ yếu kéo thụ động cố định theo chu kỳ, nhận định từ khảo sát của nhóm tại cơ sở phục hồi chức năng.

Ngoài ra, các hệ găng mềm đã công bố [9, 15] được đánh giá chủ yếu trên người khỏe mạnh và không lấy một bài tập vận động tinh với vật thật làm đơn vị đánh giá.

Hướng tiếp cận của đề tài nhắm vào đúng hai chỗ trống đó: lấy **bài tập gắp thìa với vật thật** làm đơn vị đánh giá chức năng thay vì đếm số lần chuyển động, và dùng **cảm biến áp trở giá thành thấp** nhưng chỉ sử dụng kết quả dưới dạng **chỉ số tương đối trong cùng một người** thay vì cố đo lực tuyệt đối [13, 14].

Bài toán phân xử chuyển động do người tập hay do máy tạo ra được giải ở mức tối giản bằng một cửa sổ thăm dò ngắn (mục B.7). Toàn bộ kiểm định đặt trên giàn đo cơ học và mô hình bàn tay giả trước khi xét đến con người.

### 3. Khung nẹp ngón tay và khóa đeo

Người yếu tay phải đóng được khóa nẹp bằng một tay, trong khi nẹp vẫn đủ cứng để giữ ô cảm biến và neo dây cáp. Nhóm đã khảo sát 9 phương án khóa, từ vòng kẹp và đai dán đến khóa gài, thanh răng và bản lề. Các phương án đầu mất nhiều thời gian căn chỉnh hoặc không giữ được tiền tải; phương án 8 đóng nhanh hơn nhưng gặp lỗi bền mỏi.

Từ đó, nhóm chọn phương án 9 dạng ngàm xoay hai bản lề kép để tiếp tục chế tạo. Khung nẹp ôm 3 ngón cái, trỏ, giữa, có khớp rãnh trượt bù chênh lệch chiều dài ngón. Phần khóa được thiết kế lại hình học để xử lý vị trí gãy của phương án 8.

Để giữ khối lượng cụm đeo trong khoảng mục tiêu 80–120 gam, nhóm đặt bộ xử lý, pin và servo ngoài tay. Chốt mở nhanh trên từng đốt nẹp tạo đường tháo tay độc lập với truyền động. Hình 4 trình bày khung nẹp phương án 9 và bố trí cơ cấu 3 tang.

Bản vẽ chi tiết cần thể hiện vị trí từng ô cảm biến, vật liệu và độ dày vách nẹp, lực tiền tải của khóa cùng vị trí neo dây.

### 4. Màng cảm biến áp lực và cảm biến gập

Theo dõi đáp ứng bóp của 3 ngón bằng vật liệu rẻ, dễ cắt theo khung nẹp là yêu cầu nhóm đặt ra cho phần cảm biến. Velostat đáp ứng yêu cầu này nhờ điện trở thay đổi khi bị ép; đây là hiệu ứng áp trở, phụ thuộc cả tải ép lẫn diện tích tiếp xúc. Tuy nhiên, các nghiên cứu ghi nhận trễ đàn hồi và sai số 16–48% toàn dải tùy mẫu và cách lắp [13, 14]. Nhóm chọn dùng tín hiệu để so sánh tương đối trong cùng một người, cùng buổi và cùng cách đeo, không quy đổi thành lực theo đơn vị Newton.

Một ô cảm biến có thể tăng đáp ứng cả khi ngón ép vào nẹp lẫn khi ngón tiếp xúc vật. Nhóm vì vậy chọn cặp ô mặt lòng – mặt mu cho mỗi ngón để kiểm tra khả năng tách 2 tình huống: ô mặt mu tăng khi ép vào nẹp, ô mặt lòng tăng khi tiếp xúc vật. Khả năng phân biệt được đánh giá bằng phép đối chứng riêng, thay vì suy ra chỉ từ cách bố trí.

Cảm biến gập Flex bổ sung thông tin mà Velostat không cung cấp: điện trở biến thiên theo góc uốn, cho biết tiến trình gập – duỗi và tư thế ngón. Nhóm dùng 3 Flex, mỗi ngón một chiếc, và hiệu chuẩn với thước đo góc ngoài để tính GAP.

Cấu hình được chọn gồm 11 kênh quét trên tổng số 16 kênh của bộ chuyển mạch.

| Số kênh | Phần tử | Vai trò |
|---|---|---|
| 3 | Cảm biến gập Flex ở ngón cái, trỏ, giữa | đọc biến thiên gập – duỗi và tư thế từng ngón |
| 6 | Ô Velostat ghép cặp lòng – mu cho 3 ngón | đọc đáp ứng áp lực và tiếp xúc; kiểm tra khả năng phân biệt ép vào nẹp với tiếp xúc vật |
| 2 | Hai ô tham chiếu không chịu tải | theo dõi trôi nền do điều kiện môi trường như ẩm mồ hôi, tĩnh điện; loại phiên đo khi trôi nền bất thường |
| 1 | Kênh 15 nối đất | mốc đo xuyên kênh |
| 4 | Kênh dự phòng | mở rộng khi cần thêm vị trí đo |

Hai ô tham chiếu cùng chịu ảnh hưởng môi trường với ô đo, nên giúp nhận ra phần trôi chung. Do không chịu tải ngón, chúng không bù được hiện tượng dão tải tại ô cảm biến.

Khi lắp cụm cảm biến, nhóm sẽ đo dải điện trở Flex tại đúng vị trí uốn để chọn điện trở phân áp; với Velostat, các thông số cần xác định là kích thước ô, điện trở phân áp và lực tiền tải.

### 5. Mạch thu nhận và thuật toán xử lý tín hiệu

Ở mạch đầu tiên, nhóm dùng INA333 để khuếch đại tín hiệu trước khi chuyển đổi sang số. Cách này hoạt động với nguồn tín hiệu chuẩn nhưng gặp bão hòa khi lắp cảm biến thật và gài tiền tải của nẹp. Nhóm chuyển sang đọc trực tiếp điện áp cầu phân áp bằng tầng khuếch đại lập trình được của ADS1115; kết quả so sánh 2 vòng lặp được trình bày ở C.3.

Chuỗi thu nhận gồm cầu phân áp, bộ chuyển mạch CD74HC4067, ADS1115 giao tiếp I²C và ESP32-S3. ADS1115 thuộc họ delta–sigma, kết hợp lấy mẫu và lọc số. Khi CD74HC4067 đổi kênh, điện dung ký sinh và trở kháng nguồn làm điện áp đầu vào cần thời gian xác lập; đọc quá sớm có thể lẫn đáp ứng của kênh trước.

Nhóm xử lý tín hiệu theo 4 bước. Sau mỗi lần chuyển kênh, chương trình chờ rồi đọc nháp và bỏ kết quả trước khi lấy mẫu chính thức. Tiếp đó, đường nền được cập nhật chậm khi biến thiên điện áp nhỏ để theo dõi trôi do nhiệt độ và độ ẩm tiếp xúc da. Tín hiệu được trừ vùng chết rồi làm mượt bằng bộ lọc hàm mũ. Đường hiệu chuẩn của từng kênh được lập với tải chuẩn, kèm ngày đo, nhiệt độ, cách lắp và số lần lặp.

Với tốc độ chuyển đổi và khoảng chờ đang dùng, thời gian tính toán cho mỗi kênh khoảng 2,6 ms; 11 kênh tương ứng khoảng 35 khung mỗi giây, còn 16 kênh khoảng 24 khung mỗi giây.

| Tham số | Giá trị đang dùng | Cách kiểm chứng trên băng thử |
|---|---|---|
| Khoảng chờ sau chuyển kênh | 300 µs | kích thích một kênh, đọc các kênh đang nghỉ và so sánh khi có hoặc không có khoảng chờ |
| Số lần đọc nháp rồi bỏ | 1 lần mỗi lượt chuyển kênh | so giá trị đọc ngay sau đổi kênh với lần đọc tiếp theo trên cùng tải chuẩn |
| Tốc độ chuyển đổi | 860 mẫu mỗi giây | đo thời gian hoàn tất chuyển đổi; đếm riêng số khung đủ 11 kênh |
| Ngưỡng cập nhật đường nền và vùng chết | 180 mV | lấy phân bố nhiễu từng kênh lúc nghỉ rồi kiểm tra khả năng giữ tín hiệu nỗ lực sớm |
| Hệ số cập nhật đường nền | 0,998 phần cũ cộng 0,002 phần mới | theo dõi ít nhất 10 ngày, đối chiếu tín hiệu ô đo với 2 ô tham chiếu |
| Hệ số làm mượt hàm mũ | α = 0,20 | so biên độ nhiễu sau lọc với tín hiệu nhỏ nhất cần giữ trên cùng băng thử |

Khi thả lỏng, nhật ký chạy thử ghi nhận nhiễu thô 50–135 mV, trong khi vùng chết đặt ở 180 mV. Đầu ra sau trừ vùng chết về 0 nhưng tín hiệu nhỏ cũng có nguy cơ bị xóa. Ngưỡng này chưa đạt yêu cầu giữ nỗ lực sớm; nhóm cần xác định lại từ phân bố nhiễu từng kênh và lưu đồng thời tín hiệu thô, tín hiệu sau lọc để đối chiếu.

### 6. Bộ chỉ số đánh giá tiến triển và kiểm soát chất lượng số liệu

Để biết một thay đổi là do vận động hay do chính phép đo, nhóm chọn hệ số biến thiên, sai số chuẩn của phép đo và ngưỡng khác biệt nhỏ nhất có ý nghĩa làm khung đánh giá độ tin cậy [7]. Trên cơ sở đó, 3 chỉ số EI, GAP và RAL mô tả lần lượt nỗ lực, tầm vận động còn thiếu và mức trợ giúp cần thiết.

Nhóm định nghĩa EI bằng tích phân đáp ứng tương đối trong pha vận động chủ động, chuẩn hóa theo mức tham chiếu của buổi tập. Cách định nghĩa này dùng tín hiệu áp trở, không lấy một lực tuyệt đối đặt trước làm mẫu số. Công thức cụ thể và cách chọn mức tham chiếu được xác lập từ lượt thử đầu.

Với GAP, nhóm lấy hiệu giữa tầm vận động thụ động PROM và tầm vận động chủ động AROM. Thước đo góc ngoài cung cấp số đo theo độ; cảm biến Flex đã hiệu chuẩn cung cấp biến thiên gập để đối chiếu. Đây là cách bổ sung nguồn tham chiếu góc cho găng chưa có cảm biến góc tuyệt đối.

RAL được xác định bằng mức trợ lực nhỏ nhất đủ hoàn thành một chu kỳ gập – duỗi theo tiêu chí đặt trước. Tỷ lệ hoàn thành dùng cho tiêu chí này được chọn từ lượt thử đầu trên mô hình bàn tay giả. Khi chuyển sang bài tập thìa, nhóm theo dõi thêm tỷ lệ và thời gian hoàn thành, số lần rơi hoặc đặt sai, số lần chuyển pha đúng và sai, cùng số sự kiện trợ lực sai pha.

Nhóm tách dữ liệu dùng để chỉnh tham số khỏi dữ liệu đánh giá, cố định cấu hình trước lượt đo báo cáo và ghi phiên bản trên phiếu buổi đo. Dữ liệu mô phỏng được lưu riêng với số liệu thực nghiệm.

### 7. Cơ cấu trợ lực và ba pha vận hành

Trợ lực phải bổ sung cho vận động người tập còn thiếu, thay vì thay người tập làm toàn bộ động tác. Nhóm chọn cơ chế trợ lực theo nhu cầu có sẵn trong y văn: người tập khởi xướng, bộ điều khiển dựa vào tín hiệu vận động và diễn biến bài tập để điều chỉnh mức kéo. Nhãn camera cung cấp ngữ cảnh tác vụ, không trực tiếp ra lệnh đóng ngón.

Về truyền động, nhóm chọn servo cuốn dây câu cá trực tiếp lên 3 tang riêng, mỗi ngón một tang; chiều duỗi dùng servo nhả dây chủ động. Thiết kế không dùng lò xo hồi vị, đàn hồi nối tiếp hay khớp 4 khâu. Bản thiết kế chi tiết sẽ xác định dùng một động cơ kéo 3 tang hay 3 động cơ riêng, đường kính tang, hành trình, vị trí neo và phương pháp đo độ căng dây độc lập.

Khó khăn của điều khiển là chuyển động nhìn thấy có thể do người tập hoặc do chính servo tạo ra. Nhóm chọn cửa sổ thăm dò: tạm ngưng trợ lực trong khoảng ngắn rồi quan sát đáp ứng, làm căn cứ tự động chuyển giữa đo nỗ lực và kéo trợ lực, không cần kỹ thuật viên nhấn nút. Độ dài, tần suất mở cửa sổ, tiêu chí đáp ứng, cách xử lý khi không có đáp ứng và số lần lặp được xác định trên giàn đo trước khi chạy có cấp nguồn theo quy trình an toàn.

Nhóm tổ chức vận hành thành 3 pha:

- **Nghỉ:** pha khởi động, kết thúc buổi tập và tiếp nhận lệnh dừng khi có sự cố; yêu cầu servo không tải, dây ở vị trí nhả để tháo tay.
- **Đo nỗ lực:** bắt đầu khi người tập vào tư thế sẵn sàng và 2 ô tham chiếu ổn định; mở cửa sổ thăm dò để quan sát vận động tự khởi xướng.
- **Kéo trợ lực:** bắt đầu khi đáp ứng trong cửa sổ thăm dò chưa đủ hoàn thành tầm vận động; servo kéo theo biên độ đặt trước, giảm mức trợ lực khi người tập tự làm được. Bài tập thìa nằm trong pha này, với nhãn camera điều chỉnh trợ lực theo giai đoạn tác vụ.

Các lỗi phần mềm phát hiện được, gồm mất phản hồi servo, mất đồng bộ dấu thời gian và vượt giới hạn hành trình, đưa lệnh điều khiển về pha nghỉ và được ghi lại. Nguyên mẫu chưa có điện trở shunt đo dòng, cảm biến góc hay rơ-le ngắt nguồn, nên quy tắc chuyển pha không dựa trên các tín hiệu đó.

Hộp số servo có tỉ số truyền lớn, khó quay ngược khi mất điện; lệnh nhả bằng phần mềm vì vậy khác với khả năng nhả cơ khí khi mất nguồn. Nhóm dùng chốt chặn cơ khí và ngàm bẩy mở nẹp làm đường tháo độc lập, đồng thời đo hành vi nhả dây và thời gian tháo trong phép thử cơ cấu.

Nẹp lỏng hoặc ô tham chiếu trôi bất thường được xử lý bằng trạng thái loại phiên đo, không bổ sung pha vận hành. Khi đó bộ điều khiển ngưng trợ lực, yêu cầu kiểm tra cách đeo và lưu lý do loại phiên.

### 8. Nhánh thị giác và bài tập gắp thìa

Số lần co duỗi chưa cho biết người tập có cầm và đặt được vật hay không. Nhóm chọn bài tập gắp thìa vì đây là vật dụng quen thuộc, có thể xác định khối lượng và hình dạng; chuỗi gắp, nâng, di chuyển rồi đặt cần phối hợp cả 3 ngón cái, trỏ, giữa.

Trong bố trí camera cố định, nhánh thị giác nhận biết thìa và vùng đích rồi phân loại diễn biến: sẵn sàng, nắm thìa, nâng thìa, di chuyển, thành công, rơi thìa, đặt sai chỗ hoặc không xác định. Nhãn được dùng tính chỉ số tác vụ và hiển thị phản hồi trực quan. Việc đọc đáp ứng ngón vẫn do Flex và Velostat đảm nhiệm.

Nhóm chọn xử lý ảnh cổ điển bằng OpenCV trên Orange Pi 5 Pro làm phương án đầu. Phần nhận biết ảnh được tách khỏi phần tính chỉ số để có thể thay phương pháp khi cần; mô hình học sâu chỉ được xem xét nếu phép đo trên đúng phần cứng này không đạt yêu cầu. Khi cần tọa độ thực, camera và tỷ lệ kích thước phải được hiệu chuẩn trước.

Ở tốc độ 30 khung mỗi giây, khoảng cách giữa 2 khung là 33,3 ms. Nhóm vì vậy đo riêng độ trễ đầu – cuối của nhánh thị giác, cùng độ đúng nhãn, tỷ lệ không xác định và tốc độ khung; chỉ tiêu 20 ms của dự án dành cho đường cảm biến đến lệnh servo.

Trước khi đo, nhóm lập phiếu bài tập ghi loại thìa, khối lượng, kích thước và vị trí vùng đích, khoảng cách di chuyển, tiêu chí đặt thành công, thời gian tối đa một lượt và số lượt mỗi buổi. Hình 5 minh họa bố trí camera, vùng đích và mô hình bàn tay giả trên bàn thử.

---

## C. KIỂM TRA VÀ KIỂM THỬ

Số liệu dưới đây lấy từ nhật ký chạy thử mạch và đeo thử nội bộ, chưa có biên bản đo chuẩn hóa; hạng mục chưa đo được ghi kèm mốc thực hiện.

| Đối tượng kỹ thuật | Thiết kế | Kiểm tra và kiểm thử |
|---|---|---|
| Khung nẹp ngón tay và khóa đeo | B.3 | C.1 |
| Màng cảm biến áp lực và cảm biến gập | B.4 | C.2 |
| Mạch thu nhận và thuật toán xử lý tín hiệu | B.5 | C.3 |
| Bộ chỉ số EI – GAP – RAL | B.6 | C.4 |
| Cơ cấu trợ lực và ba pha vận hành | B.7 | C.5 |
| Nhánh thị giác và bài tập gắp thìa | B.8 | C.6 |

### 1. Kiểm tra và kiểm thử khung nẹp và khóa đeo

Nhóm khảo sát khóa nẹp trước vì thao tác đóng khóa quyết định người tập có tự đeo được găng hay không. Qua các phương án vòng kẹp, rãnh trượt và đai dán, khó khăn chính là giữ tiền tải trong khi chỉ dùng một tay. Các dạng chốt và thanh răng giảm thời gian đeo nhưng còn đòi hỏi căn chỉnh chính xác.

Phương án 8 dùng bản lề một trục với ngàm đàn hồi, đóng nhanh hơn các nhóm trước nhưng gặp lỗi bền mỏi. Nhóm chuyển sang hình học ngàm xoay 2 bản lề kép của phương án 9 để xử lý vị trí gãy. Hình 6 tập hợp các thế hệ khóa nẹp đã in.

| Phương án | Nguyên lý khóa | Thời gian đeo thử nội bộ | Ghi nhận sau 50 chu kỳ đóng mở |
|---|---|---|---|
| 1–3 | vòng kẹp chữ C; rãnh trượt đuôi én; đai Velcro | 55–80 s | không đạt |
| 4–6 | chốt xuyên ngang; khóa gài mặt mu; thanh răng rút | 40–65 s | không đạt |
| 7 | không có số liệu | chưa có | chưa có |
| 8 | bản lề một trục kết hợp ngàm đàn hồi | 28 s | lỗi bền mỏi |
| 9 | ngàm xoay 2 bản lề kép; đã in | chưa đo — mốc 2 | chưa đo — mốc 2 |

Ở mốc 2, nhóm sẽ bấm giờ tự đeo, tháo qua chốt mở nhanh, đếm chu kỳ đóng mở đến khi xuất hiện lỗi và cân cụm đeo hoàn chỉnh. Phép thử độ bền cần số chu kỳ phù hợp với việc đóng mở nhiều tuần; 50 chu kỳ của lượt khảo sát ban đầu chỉ dùng để sàng lọc phương án.

### 2. Kiểm tra và kiểm thử màng cảm biến áp lực và cảm biến gập

Nhóm sẽ kiểm từng ô Velostat trước khi ghép cặp lòng – mu, sau đó đối chiếu với Flex và 2 ô tham chiếu. Sáu phép kiểm được bố trí trên băng thử có tải chuẩn.

Một là đáp ứng theo tải và độ tuyến tính, với tải tăng dần rồi giảm dần, ít nhất ba lượt lặp, để lấy đường chuẩn của từng ô và hệ số xác định. Hai là trễ đàn hồi và độ dãn tải tĩnh, so nhánh tăng tải với nhánh giảm tải và giữ tải không đổi 60 giây. Ba là độ lặp lại nội phiên và liên ngày, trong cùng điều kiện và cùng cách lắp. Bốn là nhiễu nền và tỷ số tín hiệu trên nhiễu ở trạng thái nghỉ, báo cáo cả tín hiệu thô lẫn sau lọc.

Năm là xuyên kênh, kích thích một kênh rồi đọc các kênh đang nghỉ, lấy kênh 15 làm mốc. Sáu là trôi nền, bằng chuỗi nhật ký ít nhất 10 ngày với hai ô tham chiếu, để tách phần trôi do môi trường khỏi phần trôi do dão tải của ngón.

Riêng phép kiểm cặp lòng – mu cần một bước mà phép đo đơn ô không có: ép vào nẹp và ép vào vật phải cho hai mẫu tín hiệu khác nhau, tức ô mặt mu tăng trong trường hợp thứ nhất và ô mặt lòng tăng trong trường hợp thứ hai. Nếu hai trường hợp cho cùng một mẫu thì cách bố trí vi sai không dùng được và phải đổi vị trí lắp.

Phép kiểm nhiễu đồng thời dùng để chọn lại vùng chết ở B.5: từ phân bố nhiễu từng kênh, nhóm chọn ngưỡng rồi kiểm tra tín hiệu nỗ lực sớm còn giữ được sau lọc hay không. Kết quả này quyết định khả năng tính EI.

Sáu phép kiểm chưa đo — mốc 1.

### 3. Kiểm tra và kiểm thử mạch thu nhận và thuật toán xử lý tín hiệu

Nhóm đã thử 2 cấu hình mạch bằng cách đối chiếu điện áp trên đồng hồ số, dạng sóng của máy hiện sóng FNIRSI 2C23T và đồ thị dữ liệu đọc về máy tính.

Vòng đầu dùng INA333 với hệ số khuếch đại khoảng 6,5. Tín hiệu từ nguồn chuẩn cho ngõ ra sạch, các kênh cách ly tốt. Khi lắp Velostat thật và gài tiền tải nẹp, điện áp cầu phân áp xuống dưới 1,42 V, ngõ ra kẹt khoảng 2.838 mV và vùng tuyến tính chỉ còn 1,44–1,92 V. Nhóm xác định khuếch đại cố định không phù hợp với dải điện trở biến thiên lớn khi có tiền tải, nên bỏ tầng này thay vì tiếp tục chỉnh linh kiện.

Vòng thứ 2 đọc trực tiếp qua tầng khuếch đại lập trình được của ADS1115, kết hợp chuỗi xử lý 4 bước, giữ dải ngõ vào 0–3.300 mV trong lần chạy thử. Hình 7 đối chiếu ngõ ra giữa cấu hình có INA333 và cấu hình đọc trực tiếp.

| Hạng mục | Phương pháp đo | Ghi nhận trên bàn đo | Mục tiêu |
|---|---|---|---|
| Kiến trúc ngõ vào | đối chiếu điện áp ngõ vào, ngõ ra và đồ thị dữ liệu khi lắp cảm biến thật, có tiền tải | bỏ INA333; đọc trực tiếp giữ dải 0–3.300 mV | thu trọn dải ở cấu hình 11 kênh |
| Bão hòa | quan sát dạng sóng và điện áp khi gài tiền tải rồi gập nhẹ | vòng 1: cầu phân áp < 1,42 V; ngõ ra ≈ 2.838 mV; vùng tuyến tính 1,44–1,92 V | không bão hòa ở tải thiết kế |
| Nhiễu nền | theo dõi tín hiệu khi nghỉ; đo đỉnh – đỉnh cả dữ liệu thô và sau lọc trong lượt xác nhận ở mốc 1 | nhiễu thô 50–135 mV; vùng chết 180 mV đưa đầu ra lúc nghỉ về 0 | không quá 5 mV đỉnh – đỉnh sau lọc |
| Xuyên kênh | kích thích một kênh, đọc các kênh đang nghỉ; dùng kênh 15 nối đất cho lượt đo xác nhận | đọc nháp và chờ 300 µs làm giảm bóng ma kênh | xác định ngưỡng từ phân bố đo được |
| Tỷ số tín hiệu trên nhiễu và độ tuyến tính | đo với tải chuẩn; tính tỷ số trên cửa sổ tín hiệu và nhiễu, hồi quy theo các điểm tải | chưa đo — mốc 1 | không thấp hơn 18 dB; R² không thấp hơn 0,90 |
| Tốc độ khung | đo lại bằng số khung đủ kênh trong một khoảng thời gian biết trước | vòng 1 khoảng 22 Hz với 16 kênh; khoảng chờ chuyển kênh 120 µs | không thấp hơn 20 Hz toàn khung |
| Trôi nền dài hạn | ghi ít nhất 10 ngày với 2 ô tham chiếu, giữ nguyên cách lắp | chưa đo — bắt đầu mốc 0 | nhận ra phần trôi chung trên 2 ô tham chiếu |

Khi đo xác nhận, nhóm ghi tải chuẩn, số lần lặp, điều kiện môi trường và kiểm tra ô tham chiếu trước, sau phiên. Độ trễ từ khung dữ liệu hoàn tất đến lúc lệnh servo thay đổi được đo riêng trên đồng hồ thời gian chung.

### 4. Kiểm tra và kiểm thử bộ chỉ số EI – GAP – RAL

Với bộ chỉ số, nhóm kiểm tra độ lặp lại trước khi dùng để theo dõi thay đổi giữa các buổi tập.

GAP được kiểm bằng cách đối chiếu biên độ gập đọc từ cảm biến Flex đã hiệu chuẩn với thước đo góc bên ngoài, trên cùng một mô hình bàn tay giả, ở cả tầm vận động thụ động và chủ động. Nhóm tính sai lệch góc giữa 2 cách đọc và đánh giá độ lặp lại qua hệ số biến thiên; sai lệch so với tham chiếu và độ lặp lại được báo cáo riêng.

EI và RAL được kiểm trên giàn đo cơ học: giàn trục trượt tạo chuyển động gập – duỗi lặp lại theo biên độ và tốc độ đặt trước, tải chuẩn có khối lượng đã biết đặt đúng đường truyền lực, và mô hình bàn tay giả silicone làm đối tượng đeo. Độ tin cậy của từng chỉ số đánh giá bằng hệ số biến thiên nội phiên, hệ số biến thiên liên ngày, sai số chuẩn của phép đo và ngưỡng khác biệt nhỏ nhất có ý nghĩa [7].

Quy tắc phiên đo áp dụng chung cho mọi phép kiểm: mỗi phiên ghi ngày giờ, người vận hành, phiên bản cấu hình, nhiệt độ và độ ẩm nếu có, cách lắp, số lần lặp, kết quả kiểm tra ô tham chiếu trước và sau phiên. Phiên đo bị loại khi ô tham chiếu trôi vượt ngưỡng, mất đồng bộ dấu thời gian hoặc có can thiệp vào cách đeo giữa phiên; phiên bị loại phải ghi rõ lý do.

### 5. Kiểm tra và kiểm thử cơ cấu trợ lực và ba pha vận hành

Trước khi ghép bài tập thìa, nhóm sẽ thử cơ cấu 3 tang và chu trình 3 pha trên mô hình bàn tay giả.

Phép kiểm cơ cấu gồm: hành trình thực tế so với lệnh, dạng kẹp ba chấu có đạt hình học mong muốn hay không, hành vi nhả dây khi cắt nguồn, và độ căng dây đo bằng một phương pháp độc lập. Nhóm đồng thời bấm giờ tháo tay qua chốt mở nhanh.

Phép kiểm điều khiển gồm: số lần chuyển pha đúng và sai so với nhãn đối chiếu, số sự kiện trợ lực sai pha, và độ trễ từ cảm biến đến lệnh servo đo bằng nhật ký đồng bộ. Độ dài cửa sổ, tần suất mở và tiêu chí nhận diện đáp ứng của quy tắc cửa sổ thăm dò xác định bằng thực nghiệm.

Phép so sánh tối thiểu khi tích hợp là đối chiếu trợ lực cố định với trợ lực theo nhu cầu tự động, trên cùng một mô hình bàn tay giả và trong điều kiện tương đương. Đây là phép kiểm trả lời câu hỏi cốt lõi của đề tài: cơ chế tự giảm trợ lực có tạo ra khác biệt đo được so với kéo cố định hay không.

### 6. Kiểm tra và kiểm thử nhánh thị giác và bài tập gắp thìa

Nhóm sẽ ghi hình bài tập thìa trên Orange Pi 5 Pro, gán nhãn thủ công để đối chiếu với kết quả của bộ nhận biết.

Các chỉ số thị giác gồm độ đúng của nhãn, tỷ lệ nhãn không xác định, độ trễ đầu – cuối đo bằng dấu thời gian ở hai đầu, và số khung hình mỗi giây. Độ đúng của nhãn được lập bảng nhầm lẫn so với nhãn gán thủ công, để biết loại lỗi nào chiếm ưu thế thay vì chỉ có một tỷ lệ chung.

Các chỉ số tác vụ gồm tỷ lệ hoàn thành bài tập thìa, thời gian hoàn thành, số lần rơi thìa hoặc đặt sai vị trí; tất cả lấy từ nhãn camera và nhật ký trên đồng hồ thời gian chung. Tờ yêu cầu tác vụ lập trước khi đo: loại thìa và khối lượng, kích thước và vị trí vùng đích, khoảng cách di chuyển, tiêu chí đặt thành công, thời gian tối đa một lượt và số lượt mỗi phiên.

Độ nhạy riêng của từng nguồn đo đánh giá bằng cách tắt lần lượt từng nguồn: chỉ cảm biến gập, chỉ màng áp trở, chỉ camera, rồi đủ cả ba.

### 7. Phương tiện, tình trạng thiết bị, mốc thực hiện và bảng tổng hợp chỉ tiêu

Phương tiện kiểm định gồm giàn đo cơ học trục trượt, tải chuẩn có khối lượng đã biết, mô hình bàn tay giả đúc bằng silicone và thước đo góc làm tham chiếu; công dụng của từng thứ nêu ở mục C.4 và C.5.

Về tình trạng thiết bị: Velostat, băng đồng, ESP32-S3, Orange Pi 5 Pro, đồng hồ đo, bộ tạo tín hiệu và bộ chuyển mạch CD74HC4067 đã có, trong đó CD74HC4067 đã được chạy thử; 3 cảm biến gập Flex cần mua ở mốc 1; giàn trục trượt, cảm biến lực, khối lượng chuẩn và silicone đúc mô hình tay giả thuộc nhóm phải chế tạo hoặc mua ở mốc 1; tình trạng của bộ chuyển đổi ADS1115 chưa được xác nhận. Các lượt thử hiện có thực hiện trên bảng mạch thử và đồng hồ số; giàn cơ học được chuẩn bị cho mốc 1.

Thứ tự triển khai gồm 5 giai đoạn. **Mốc 0** (~3 tuần): tờ yêu cầu tác vụ, bản đồ kênh cảm biến, phiếu buổi đo, đặc tả ba pha vận hành và chuỗi nhật ký trôi nền ít nhất 10 ngày. **Mốc 1** (~3–4 tuần): mua 3 cảm biến Flex, hiệu chuẩn Flex và Velostat trên băng thử, đo tỷ số tín hiệu trên nhiễu, độ tuyến tính, hệ số biến thiên, trễ đàn hồi và độ dãn tải tĩnh — tức các mục C.2 và C.3. **Mốc 2** (~3–4 tuần): cơ cấu ba tang trên mô hình bàn tay giả, đo hành trình, hành vi nhả khi mất nguồn, giới hạn an toàn, bấm giờ thời gian tự đeo và đo độ bền phương án khóa 9, cân cụm đeo, xuất bản vẽ CAD — tức các mục C.1 và C.5.

**Mốc 3** (~2–3 tuần): nhánh thị giác và bài tập thìa, đo thử trên Orange Pi 5 Pro — tức mục C.6. **Tích hợp** (~2 tuần): chu trình ba bước trên mô hình bàn tay giả và so sánh trợ lực cố định với trợ lực theo nhu cầu — tức mục C.4 và C.5.

Chi phí dự toán cho cụm đeo là 1,0–1,3 triệu đồng, cho toàn hệ thống và giàn thử khoảng 5,5 triệu đồng khi tận dụng thiết bị phòng thí nghiệm. Nhóm sẽ lập bảng vật tư kèm ngày và báo giá để đối chiếu. Kế hoạch ưu tiên mốc 0, mốc 1, bản vẽ CAD, phép đo khóa 9 và cụm 3 tang trên mô hình tay giả; mốc 3 và tích hợp phụ thuộc kết quả đo nhánh thị giác cùng giao tiếp giữa 2 bo mạch.

Bảng dưới đây tổng hợp chỉ tiêu và cách đo. Dấu “—” ở cột mục tiêu chỉ các ngưỡng sẽ xác lập từ lượt thử đầu theo căn cứ tương ứng.

| Chỉ số | Cách đo | Mục tiêu | Căn cứ và mốc thực hiện |
|---|---|---|---|
| Tỷ lệ hoàn thành tác vụ; thời gian; số lần rơi hoặc đặt sai | nhãn camera và nhật ký trên đồng hồ thời gian chung | — | lượt thử đầu trên mô hình bàn tay giả (C.6) |
| Tỷ lệ nhãn không xác định; độ đúng nhãn trạng thái | nhật ký nhãn; bảng nhầm lẫn so với nhãn thủ công | — | đo thử nhánh thị giác trên Orange Pi 5 Pro (C.6) |
| Độ trễ thị giác đầu – cuối | dấu thời gian hai đầu | — | đo trên phần cứng thật (C.6) |
| Tốc độ khung thu thập | đếm số hiệu khung | không thấp hơn 20 Hz | tính toán khoảng 35 Hz (C.3) |
| Trễ cảm biến đến lệnh servo | nhật ký đồng bộ | không quá 20 ms | đo trên bàn thử (C.5) |
| Chuyển pha đúng và sai; trợ lực sai pha | nhật ký pha vận hành và nhãn đối chiếu | — | phương pháp cửa sổ thăm dò (C.5) |
| Biên độ và độ lặp lại chu kỳ gập – duỗi | nhật ký cảm biến Flex và thước đo góc | hệ số biến thiên không quá 5% nội phiên, 8% liên ngày | mốc 1 (C.2, C.4) |
| Trôi tín hiệu | nhật ký hai ô tham chiếu | — | mốc 1, chuỗi nhật ký ≥ 10 ngày (C.2) |
| Tỷ số tín hiệu trên nhiễu và độ tuyến tính | so tín hiệu với nhiễu lúc nghỉ; hồi quy đáp ứng theo các điểm tải chuẩn | không thấp hơn 18 dB và R² không thấp hơn 0,90 | mốc 1 (C.2, C.3) |
| Trễ đàn hồi, dãn tải tĩnh, nhiễu nền | so nhánh tăng – giảm tải; giữ tải 60 s; đo đỉnh – đỉnh khi nghỉ | trễ đàn hồi không quá 18%; dãn tải sau 60 s không quá 8%; nhiễu không quá 5 mV đỉnh – đỉnh sau lọc | mốc 1 (C.2, C.3) |
| Độ nhạy riêng của từng nguồn đo | tắt lần lượt Flex, Velostat, camera rồi đủ cả ba | — | mốc 3 và tích hợp (C.6) |
| Thời gian tự đeo, thời gian tháo, độ bền khóa nẹp | bấm giờ thao tác; đếm chu kỳ đến khi xuất hiện lỗi | — | mốc 2 (C.1) |
| Khối lượng cụm đeo | cân cụm đeo đã lắp đủ, ghi ngày | 80–120 g | cân sản phẩm hoàn chỉnh (C.1) |
| Chi phí vật tư | bảng vật tư có ngày và báo giá | dự toán 1,0–1,3 triệu đồng cho cụm đeo, khoảng 5,5 triệu đồng cho toàn hệ thống | kiểm toán bảng vật tư |

### 8. Kết luận

Qua quá trình chế tạo 9 phương án khóa nẹp và đeo thử các phương án trước, nhóm đã chọn ngàm xoay 2 bản lề kép để tiếp tục hoàn thiện thao tác đóng khóa bằng một tay. Sự thay đổi hình học này xuất phát từ lỗi bền mỏi của bản lề một trục, thay vì chỉ điều chỉnh độ chặt của khóa.

Ở mạch thu nhận, khi gài tiền tải nẹp, nhóm phát hiện INA333 bão hòa khoảng 2.838 mV và vùng tuyến tính thu hẹp còn 1,44–1,92 V. Chuyển sang đọc trực tiếp qua ADS1115 đã giữ dải ngõ vào 0–3.300 mV trong lượt chạy thử. Kết quả này là cơ sở chọn chuỗi thu nhận không có tầng khuếch đại cố định và xử lý tín hiệu theo 4 bước.

Nhóm đã chọn cấu hình 11 kênh gồm Flex, Velostat và 2 ô tham chiếu, cơ cấu 3 tang nhả dây chủ động, đồng thời xây dựng định nghĩa EI, GAP, RAL và kiến trúc 3 pha với cửa sổ thăm dò. Các lựa chọn này tạo cơ sở cho phép đo độ tin cậy và so sánh trợ lực cố định với trợ lực theo nhu cầu ở các mốc triển khai.

### 9. Hướng phát triển

Trong giai đoạn tiếp theo, nhóm mua 3 Flex, lắp cụm cảm biến theo cấu hình đã chọn và hiệu chuẩn trên giàn đo. Thời gian tự đeo, tháo, độ bền khóa 9, khối lượng cụm đeo và chi phí được đối chiếu qua phép đo cùng bảng vật tư; bản vẽ CAD được hoàn thiện và lưu theo cấu hình chế tạo. Phần mềm vi điều khiển, các mô-đun xử lý, nhánh thị giác và cửa sổ thăm dò được triển khai, kiểm thử theo kế hoạch ở C.7.

Số liệu hiện có phản ánh hoạt động của từng phần trên bàn thử, chưa cho biết hiệu quả phục hồi trên người; dữ liệu từ người khỏe cũng không thay thế dữ liệu người bệnh. Cửa sổ thăm dò chỉ nhận ra đáp ứng tạo chuyển động, còn nỗ lực không làm ngón di chuyển cần được đánh giá bằng cách khác.

Sau giai đoạn tích hợp, nhóm hướng tới thay dây dẫn rời bằng mạch in mềm đi chìm trong nẹp để giảm đứt gãy và gọn bố trí, rồi mở rộng từ 3 lên 5 ngón khi có dữ liệu hiệu chuẩn. Ngưỡng trợ lực được cá nhân hóa theo tầm vận động; các phương pháp điều khiển thích ứng nâng cao, kể cả học máy, chỉ xem xét khi đã có dữ liệu bàn thử đủ lớn và quy trình an toàn hoàn chỉnh.

Khả năng tự đeo và tín hiệu vận động tự nguyện trên người trưởng thành khỏe mạnh được khảo sát theo điều kiện ở A.5. Thử nghiệm đối chứng lâm sàng với FMA-UE và ARAT là hướng nghiên cứu sau đề tài, cần hoàn tất kiểm định kỹ thuật và hồ sơ phê duyệt của Hội đồng Đạo đức trong nghiên cứu y sinh học tại cơ sở y tế chuyên khoa.

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

---

## PHỤ LỤC — DANH MỤC HÌNH CẦN BỔ SUNG

| Hình | Chú thích dự kiến | Tư liệu cần bổ sung |
|---|---|---|
| Hình 1 | Tỷ lệ đột quỵ tại Việt Nam và di chứng vận động bàn tay sau đột quỵ | biểu đồ từ nguồn [1, 5, 6], ghi riêng phạm vi của từng số liệu |
| Hình 2 | Bản đồ vận động của Penfield & Boldrey và vùng chi phối bàn tay theo Gordon et al. | hình minh họa từ [11] và [4], kèm chú dẫn nguồn |
| Hình 3 | Sơ đồ 4 tầng của găng tay: cụm đeo, thu thập, trợ lực, tác vụ và phản hồi | sơ đồ khối với đường truyền dữ liệu và lệnh điều khiển |
| Hình 4 | Khung nẹp phương án 9 và bố trí cơ cấu 3 tang | ảnh mẫu nẹp đã in và bản vẽ bố trí tang, phân biệt ảnh chế tạo với bản thiết kế |
| Hình 5 | Bố trí bàn thử bài tập gắp thìa | sơ đồ camera, vùng đích và mô hình bàn tay giả; ảnh bố trí khi lắp xong |
| Hình 6 | Các thế hệ khóa nẹp đã in thử | ảnh phương án 1–9, đánh số và chỉ vị trí lỗi của phương án 8 |
| Hình 7 | So sánh ngõ ra mạch dùng INA333 với mạch đọc trực tiếp qua ADS1115 | ảnh máy hiện sóng hoặc đồ thị dữ liệu gốc của 2 vòng lặp, ghi trục và điều kiện đo |
