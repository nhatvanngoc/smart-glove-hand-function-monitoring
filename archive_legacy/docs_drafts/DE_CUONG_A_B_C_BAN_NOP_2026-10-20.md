# ĐỀ CƯƠNG DỰ ÁN KHOA HỌC KỸ THUẬT

**Tên dự án:** *Nghiên cứu và phát triển găng tay hỗ trợ phục hồi chức năng sau đột quỵ cho vận động tinh.*

Lĩnh vực: ⟨…⟩ · Đơn vị: ⟨…⟩ · Thành viên: ⟨…⟩ · Người hướng dẫn: ⟨…⟩

---

## A. VẤN ĐỀ NGHIÊN CỨU

### 1. Lý do chọn đề tài

Đột quỵ là một trong những nguyên nhân hàng đầu gây tàn tật ở Việt Nam, với tỷ lệ hiện mắc năm 2019 khoảng 1.541 ca trên 100.000 dân và mỗi năm thêm khoảng 222 ca mới trên 100.000 dân [1].

Tổng quan của Cochrane ghi nhận khoảng 80% người sống sót bị suy giảm vận động, và trong nhóm liệt hoàn toàn chi trên chỉ khoảng một nửa phục hồi được một phần chức năng sau 6 tháng [5, 6]. Bàn tay hồi phục chậm nhất và khó nhất, vì tay phải làm được các động tác tinh như cầm thìa, cài cúc áo, cầm bút chứ không chỉ co duỗi.

Việc theo dõi quá trình tập luyện đó gần như chưa được định lượng: thang khám lâm sàng FMA-UE và ARAT có tính gián đoạn, vài tuần một lần và phụ thuộc người khám; thiết bị đeo cổ tay Manumeter muốn phát hiện tiến triển thì người đeo phải thay đổi tới khoảng 31% cường độ sử dụng trong ngày, đồng thời đếm sai 100–200 lần dương tính giả mỗi giờ [7].

Khảo sát của nhóm tại cơ sở phục hồi chức năng tháng 9 năm 2026 ghi nhận các loại găng hiện có chưa phù hợp điều kiện tập tại nhà ở Việt Nam về giá thành, khối lượng và thao tác đeo.

Từ những thực tế trên, nhóm nghiên cứu chế tạo găng tay nẹp ba ngón hỗ trợ người tập đi từ vận động gập – duỗi đến thao tác **gắp thìa bằng ngón cái, trỏ, giữa**, thay vì chỉ đếm chuyển động hoặc kéo thụ động theo chu kỳ định sẵn.

⟨HÌNH 1 — biểu đồ tỷ lệ đột quỵ tại Việt Nam và di chứng bàn tay kéo dài⟩

### 2. Xác định vấn đề nghiên cứu

Vấn đề đặt ra là liệu mảng cảm biến gập và cảm biến áp trở đặt trên khung nẹp ba ngón có tạo được tín hiệu đủ lặp lại để phát hiện vận động chủ động của người tập hay không, và liệu cơ cấu servo – dây cáp – ba tang có tạo được dạng kẹp ba chấu với mức trợ lực tự giảm dần hay không.

Nhóm tập trung vào sáu nội dung: khung nẹp ba ngón tích hợp 3 cảm biến gập Flex và 6 ô áp trở Velostat bố trí theo cặp lòng – mu; mạch thu nhận và thuật toán lọc tín hiệu; bộ chỉ số đánh giá tiến triển gồm EI, GAP và RAL cùng chỉ số của bài tập; cơ cấu ba tang với chiều duỗi thực hiện bằng nhả dây chủ động; quy tắc tự động chuyển pha trợ lực và nhánh thị giác cho bài tập gắp thìa; quy trình kiểm chứng trên giàn đo cơ học và mô hình bàn tay giả.

Hai câu hỏi khó nhất là: trong phép thử có tải và điều kiện xác định, tín hiệu áp trở từ hai vách lòng – mu có phân biệt được hướng vận động với độ tin cậy chấp nhận được và có tự phát hiện được phiên đo lỗi do đeo nẹp lỏng hay không; và bộ điều khiển có phân biệt được vận động do người tập khởi xướng với chuyển động do chính cơ cấu tạo ra hay không.

### 3. Mục tiêu nghiên cứu

Mục tiêu tổng quát là chế tạo và đánh giá được nguyên mẫu găng tay nẹp ba ngón hoạt động ổn định trên bàn thử, với bộ số liệu đo lường dùng được cho việc theo dõi vận động tinh của bàn tay.

Mục tiêu cụ thể gồm ba phần: hoàn thiện phần đeo, tức khung nẹp có khóa mà người yếu tay tự đeo được bằng một tay, cụm cảm biến 11 kênh đọc ổn định và khối lượng nhẹ; hoàn thiện phần trợ lực, tức cơ cấu ba tang tạo được dạng kẹp ba chấu, trợ lực giảm dần theo đáp ứng của người tập và có đường thoát an toàn; hoàn thiện phần đánh giá, tức bộ chỉ số EI, GAP, RAL cùng chỉ số bài tập thìa và quy trình kiểm soát chất lượng số liệu. Đây là nguyên mẫu kỹ thuật kiểm chứng trên thiết bị đo và mô hình bàn tay giả, không phải thiết bị y tế đã hoàn thiện để dùng cho người bệnh.

### 4. Tiêu chí của dự án

Các ngưỡng dưới đây là mục tiêu thiết kế chốt trước khi đo, chưa phải kết quả đã đạt.

- Tốc độ khung khi quét 11 kênh không thấp hơn 20 Hz; tỷ số tín hiệu trên nhiễu không thấp hơn 18 dB và hệ số xác định R² không thấp hơn 0,90 trên tải chuẩn.
- Phân biệt đúng hướng vận động không thấp hơn 90%; phân loại đúng mức kích hoạt không thấp hơn 85%.
- Hệ số biến thiên không vượt quá 5% trong cùng buổi và 8% giữa các ngày; trễ đàn hồi không quá 18%; độ dãn tải tĩnh sau 60 giây giữ tải không quá 8%; nhiễu nền sau lọc không quá 5 mV đỉnh – đỉnh.
- Trễ từ cảm biến đến lệnh servo không vượt quá 20 ms; chỉ tiêu này không áp dụng cho nhãn tác vụ từ camera.
- Giới hạn an toàn đặt theo hành trình dây, góc kéo và chốt mở nhanh trên nẹp; không dùng ngưỡng lực suy ra từ cảm biến áp trở làm cơ chế an toàn.
- Thời gian người tập tự đeo và tự tháo găng, cùng độ bền của khóa nẹp theo số chu kỳ đóng mở: sẽ đo ở mốc 2.
- Tỷ lệ hoàn thành bài tập thìa và độ đúng của nhãn trạng thái từ camera: xác định sau lượt thử đầu trên mô hình bàn tay giả.
- Khối lượng cụm đeo 80–120 gam, chưa cân cho cấu hình ba tang.
- Thử khả năng tự đeo và bắt tín hiệu vận động tự nguyện ở người tình nguyện khỏe mạnh, theo quy trình an toàn được phê duyệt trước.

Hai điểm an toàn cần nói thẳng: nguyên mẫu chưa có điện trở shunt nên chưa giám sát được dòng servo; hộp số servo tỉ số truyền lớn không quay ngược trục được khi ngắt điện, nên hành vi nhả dây lúc mất nguồn phải đo thực tế chứ không được giả định. Đường thoát an toàn là chốt mở nhanh trên từng đốt nẹp, thời gian tháo sẽ đo ở mốc 2.

### 5. Đối tượng và phạm vi nghiên cứu

- **Con người:** số liệu thống kê về đột quỵ và di chứng vận động bàn tay; khó khăn của người tập trong sinh hoạt và khi tự tập tại nhà, làm cơ sở chọn bài tập gắp thìa làm đơn vị đánh giá.
- **Lịch sử đề tài:** chín thế hệ khóa nẹp đã in thử và đeo thử, hai vòng lặp thiết kế mạch thu nhận đã đo kiểm, và các hệ găng tay phục hồi chức năng đã công bố.
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

Bàn tay chiếm diện tích đại diện vận động rất lớn trên vỏ não theo Penfield & Boldrey [11] và mạng SCAN của Gordon et al. [4]; đó là cơ sở để đề tài tập trung vào ba ngón trụ cột cái, trỏ, giữa thay vì làm cả năm ngón.

Theo học thuyết Hebb [12] và nguyên lý phục hồi chức năng [2, 3], phản hồi cảm giác đồng thời với nỗ lực vận động giúp định hướng tập luyện. Đề tài khai thác cơ sở này để xây dựng phản hồi thị giác thời gian thực, cho người tập tự quan sát nỗ lực phát lực đọc từ đáp ứng áp trở vi mô; đề tài không đo hoạt động vỏ não và không chứng minh sự tái tổ chức thần kinh.

⟨HÌNH 2 — bản đồ Homunculus [11] và sự phân bổ chi phối bàn tay [4]⟩

Sau đột quỵ, suy giảm vận động thường kết hợp giữa yếu cơ và tăng trương lực co cứng [8, 10], nên đề tài khảo sát độ thiếu hụt tầm vận động GAP, tức hiệu giữa tầm vận động thụ động PROM và tầm vận động chủ động AROM, như một chỉ số mô tả chênh lệch góc đo bằng công cụ ngoài chứ không phải một phép chẩn đoán. Độ tin cậy của hệ đo đánh giá qua hệ số biến thiên, sai số chuẩn và ngưỡng khác biệt nhỏ nhất có ý nghĩa [7], làm căn cứ bố trí hai ô tham chiếu và chốt trước tiêu chí kỹ thuật.

Hệ thống được tổ chức theo kiến trúc phân tán bốn tầng. Tầng đeo là khung nẹp ba ngón in 3D, tích hợp 3 cảm biến gập Flex, 6 ô áp trở Velostat bố trí thành cặp ở mặt lòng và mặt mu của ngón, cùng 2 ô tham chiếu không chịu tải. Tầng thu thập đọc các cảm biến đó qua bộ chuyển mạch CD74HC4067 và bộ chuyển đổi tương tự – số ADS1115 loại 16 bit có tầng khuếch đại lập trình được, rồi xử lý bằng thuật toán lọc số bốn bước trên vi điều khiển ESP32-S3. Tầng trợ lực là cơ cấu trợ lực theo nhu cầu truyền động bằng dây cáp cuốn trên ba tang riêng. Tầng tác vụ chạy trên Orange Pi 5 Pro, dùng camera nhận biết thìa và vùng đích, trích xuất bộ chỉ số tiến triển và hiển thị phản hồi cho người tập.

Điểm khác biệt cốt lõi so với găng kéo thụ động là hệ thống chỉ trợ lực khi nỗ lực chủ động chưa đủ hoàn thành tầm vận động, và tự giảm trợ lực khi phát hiện người tập đã tự khởi xướng chuyển động. Một chu kỳ vận hành gồm: quét 11 kênh, lọc và chuẩn hóa, trích đặc trưng vận động, chọn pha trợ lực, phát lệnh servo có giới hạn, nhận nhãn tác vụ từ camera, rồi ghi nhật ký theo một dấu thời gian chung.

⟨HÌNH 3 — sơ đồ khối bốn tầng: cụm đeo → thu thập → trợ lực → tác vụ và phản hồi⟩

### 2. Bất cập của các giải pháp hiện tại và hướng tiếp cận của đề tài

Việc theo dõi vận động bàn tay ngoài bệnh viện hiện gặp bốn rào cản: thang đo lâm sàng FMA-UE và ARAT gián đoạn, hai đến bốn tuần một lần và phụ thuộc người khám; thiết bị đeo cổ tay Manumeter chỉ đếm chuyển động thô với 100–200 lần dương tính giả mỗi giờ [7]; điện cơ bề mặt sEMG suy giảm chất lượng rõ khi ra mồ hôi và khó tách riêng từng nhóm cơ cẳng tay; găng tay robot thương mại chủ yếu kéo thụ động cố định theo chu kỳ, nhận định đến từ khảo sát thực tế của nhóm tại cơ sở phục hồi chức năng chứ chưa có nguồn y văn trực tiếp.

Ngoài ra, các hệ găng mềm đã công bố [9, 15] được đánh giá chủ yếu trên người khỏe mạnh và không lấy một bài tập vận động tinh với vật thật làm đơn vị đánh giá.

Hướng tiếp cận của đề tài nhắm vào đúng hai chỗ trống đó: lấy **bài tập gắp thìa với vật thật** làm đơn vị đánh giá chức năng thay vì đếm số lần chuyển động, và dùng **cảm biến áp trở giá thành thấp** nhưng chỉ sử dụng kết quả dưới dạng **chỉ số tương đối trong cùng một người** thay vì cố đo lực tuyệt đối [13, 14].

Bài toán khó nhất về điều khiển, là phân xử chuyển động do người tập hay do máy tạo ra, được giải ở mức tối giản bằng một cửa sổ thăm dò ngắn (mục B.6). Toàn bộ kiểm định đặt trên giàn đo cơ học và mô hình bàn tay giả trước khi xét đến con người.

### 3. Thiết kế phần cứng

Khung nẹp in 3D ôm ba ngón cái – trỏ – giữa, có khớp rãnh trượt bù chênh lệch chiều dài ngón. Khóa nẹp là phương án Mech 9 dạng ngàm xoay hai bản lề kép, chọn vì người tập đóng mở được bằng một tay; phương án này đã in xong nhưng chưa bấm giờ, nên thời gian tự đeo sẽ đo ở mốc 2.

Cụm đeo có khối lượng mục tiêu 80–120 gam và chưa được cân cho cấu hình ba tang; bộ xử lý, pin và servo đặt ngoài tay để giảm khối lượng đeo. Bộ truyền trợ lực dùng servo cuốn dây câu cá trực tiếp lên ba tang riêng, mỗi ngón một tang; chiều duỗi thực hiện bằng servo nhả dây chủ động, không dùng lò xo hồi vị, đàn hồi nối tiếp hay khớp bốn khâu.

Cấu hình cảm biến đã chọn gồm 11 kênh quét trên tổng số 16 kênh của bộ chuyển mạch.

| Kênh | Phần tử | Vai trò |
|---|---|---|
| 3 | Cảm biến gập Flex ở ngón cái, trỏ, giữa | đo biến thiên gập – duỗi và tư thế từng ngón |
| 6 | Ô áp trở Velostat ghép cặp lòng – mu cho ba ngón | đo áp lực và tiếp xúc; phân biệt trường hợp ép vào nẹp (ô mặt mu tăng) với trường hợp tiếp xúc vật (ô mặt lòng tăng) |
| 2 | Ô tham chiếu REF_1 và REF_2 không chịu tải | theo dõi trôi nền và điều kiện môi trường như ẩm mồ hôi, tĩnh điện; làm cổng kiểm soát chất lượng để loại phiên đo, không bù được hiện tượng dão tải của ngón vì ô tham chiếu không chịu tải |
| 1 | CH15 nối đất | mốc đo xuyên kênh |
| 4 | dự phòng | mở rộng khi cần thêm vị trí đo |

Velostat là tấm vật liệu dẫn điện giá thấp, đổi điện trở khi bị ép; ưu điểm là rẻ và dễ cắt theo hình ngón tay, nhược điểm là trễ đàn hồi và sai số 16–48% toàn dải tùy mẫu và cách lắp [13, 14]. Vì vậy nhóm chỉ dùng nó để so sánh tương đối trong cùng một người, cùng buổi và cùng cách đeo, không quy đổi ra lực.

Tín hiệu đi theo chuỗi: cầu phân áp, bộ chuyển mạch CD74HC4067, bộ chuyển đổi ADS1115 giao tiếp I²C, rồi đến vi điều khiển ESP32-S3; hệ thống không dùng tầng khuếch đại cố định, lý do nêu ở mục C.2. Về thời gian quét, mỗi kênh mất khoảng 2,6 ms nên 11 kênh cho khoảng 35 khung hình mỗi giây và 16 kênh cho khoảng 24 khung hình mỗi giây; đây là tính toán, chưa đo thực tế.

Các thông số sẽ chốt ở bước thiết kế chi tiết: vị trí lắp từng ô cảm biến, dải điện trở của Flex tại đúng vị trí lắp đó, điện trở phân áp và tốc độ khung thực tế; dùng một động cơ kéo cả ba tang hay ba động cơ riêng; đường kính tang, hành trình dây và vị trí neo; hành vi nhả dây khi mất nguồn, vốn là bài toán cơ khí chứ không xử lý bằng phần mềm; và phương pháp đo độ căng dây một cách độc lập.

⟨HÌNH 4 — khung nẹp Mech 9 và cơ cấu ba tang⟩

### 4. Thuật toán xử lý tín hiệu

Tín hiệu từ cảm biến áp trở vốn nhiễu và trôi theo nhiệt độ cùng độ ẩm tiếp xúc da, nên cần một chuỗi xử lý bốn bước trước khi dùng cho điều khiển.

Bước thứ nhất loại bỏ mẫu nhiễm kênh cũ: sau khi chuyển kênh, hệ thống chờ một khoảng ngắn rồi đọc một lần và bỏ kết quả đó, sau đó mới lấy giá trị thật. Lý do là ADS1115 thuộc họ delta – sigma nên lần chuyển đổi đầu sau khi đổi kênh vẫn chứa mẫu kênh cũ trong bộ lọc số; bỏ lần đọc đầu, cộng với thời gian chờ để mạch RC của nguồn tín hiệu xác lập, sẽ giảm hiện tượng bóng ma kênh.

Bước thứ hai theo dõi đường nền thích ứng: khi mức thay đổi điện áp còn nhỏ thì hệ thống coi đó là trôi nền chứ không phải vận động, và cập nhật đường nền rất chậm để bù trôi do nhiệt độ và độ ẩm. Bước thứ ba trừ vùng chết, chỉ giữ lại phần thay đổi vượt ngưỡng. Bước thứ tư làm mượt bằng bộ lọc hàm mũ để có tín hiệu đáp ứng cuối cùng. Mỗi kênh có một đường hiệu chuẩn riêng, lập trên băng thử với tải chuẩn đã biết, ghi lại ngày, nhiệt độ, cách lắp và số lần lặp.

Bộ tham số đang dùng liệt kê ở bảng dưới đây; chưa tham số nào được tối ưu có hệ thống hay kiểm chứng trên nhiều mẫu cảm biến.

| Tham số | Giá trị đang dùng | Trạng thái |
|---|---|---|
| Thời gian chờ sau khi chuyển kênh | 300 µs | chưa đo, sẽ xác định lại trên băng thử |
| Số lần đọc nháp rồi bỏ | 1 lần mỗi lượt chuyển kênh | giữ nguyên theo kiến trúc delta – sigma |
| Tốc độ lấy mẫu của bộ chuyển đổi | 860 mẫu mỗi giây | cố định theo cấu hình đang dùng |
| Ngưỡng cập nhật đường nền và vùng chết | 180 mV | **chưa đạt**: cao hơn dải nhiễu nền đã ghi nhận 50–135 mV |
| Hệ số cập nhật đường nền | 0,998 phần cũ cộng 0,002 phần mới | chưa tối ưu có hệ thống |
| Hệ số làm mượt hàm mũ | α = 0,20 | chưa tối ưu có hệ thống |

Việc sử dụng tín hiệu có hai giới hạn cần nêu rõ. Trừ vùng chết ghim đầu ra về 0 lúc nghỉ nhưng không có nghĩa nhiễu thô đã mất, vì nhiễu thô đo được 50–135 mV, nên khi báo cáo nhiễu phải kèm cả tín hiệu thô lẫn sau lọc. Tín hiệu sau lọc cũng không phải lực theo đơn vị Newton vì Velostat có trễ đàn hồi và sai số lớn, nên các chỉ số chỉ dùng ở dạng tương đối trong cùng người, cùng phiên và cùng cách đeo.

Riêng ngưỡng vùng chết 180 mV đang có vấn đề: nó cao hơn dải nhiễu nền đã ghi nhận nên có nguy cơ triệt tiêu luôn tín hiệu nỗ lực sớm biên độ nhỏ của người tập yếu cơ, tức làm hỏng chính phép đo EI. Ngưỡng này vì vậy chưa được coi là đạt, sẽ xác định lại theo phân bố nhiễu trên từng kênh, và tín hiệu nỗ lực sớm phải kiểm tra riêng xem có sống sót sau vùng chết hay không.

### 5. Bộ chỉ số đánh giá tiến triển và kiểm soát chất lượng số liệu

Bộ chỉ số gồm ba đại lượng chính và một nhóm chỉ số của bài tập.

Chỉ số nỗ lực EI là tích phân của đáp ứng tương đối trong pha người tập vận động chủ động, chuẩn hóa theo mức tham chiếu của chính buổi tập đó; công thức cụ thể và cách chọn mức tham chiếu sẽ chốt sau lượt thử đầu. Chỉ số này không chuẩn hóa theo lực đặt trước, vì hệ cảm biến không đo được lực tuyệt đối.

Độ thiếu hụt tầm vận động GAP là hiệu giữa tầm vận động thụ động và tầm vận động chủ động, tính theo độ, đo bằng thước đo góc bên ngoài kết hợp với biên độ gập đọc từ cảm biến Flex đã hiệu chuẩn. Găng tay không có cảm biến góc tuyệt đối nên phần mềm không tự xuất ra góc theo độ; thước đo góc bên ngoài mới là nguồn tham chiếu. Chỉ số này mô tả mức yếu liệt chứ không phải một phép chẩn đoán.

Mức trợ giúp cần thiết RAL là mức trợ lực nhỏ nhất đủ để hoàn thành một chu kỳ gập – duỗi theo tiêu chí đặt trước; ngưỡng tỷ lệ hoàn thành sẽ chốt sau lượt thử đầu trên mô hình bàn tay giả. Nhóm chỉ số của bài tập gồm tỷ lệ hoàn thành bài tập thìa, thời gian hoàn thành, số lần rơi thìa hoặc đặt sai vị trí, số lần chuyển pha đúng và sai, cùng số sự kiện trợ lực sai pha.

Về kiểm soát chất lượng số liệu, mỗi buổi đo ghi mã băm của cấu hình vào phiếu buổi đo, nghĩa là đổi tham số thì đổi phiên bản; dữ liệu dùng để chỉnh tham số được tách riêng khỏi dữ liệu dùng để báo cáo, và phiên bản dữ liệu được khóa trước lượt đánh giá. Dữ liệu mô phỏng phải ghi rõ là mô phỏng và không đưa vào bảng kết quả đo; chỉ số nào chưa đo được thì ghi là chưa đo được, không ước lượng.

### 6. Cơ chế trợ lực theo nhu cầu và ba pha vận hành

Trong cơ chế trợ lực theo nhu cầu, vận động ngón luôn do người tập khởi xướng; bộ điều khiển chỉ bù đúng phần còn thiếu dựa trên tín hiệu vận động và trạng thái bài tập, chứ không đóng ngón tay hoàn toàn theo lệnh từ camera. Việc chuyển từ hỗ trợ gập – duỗi sang trợ lực giảm dần diễn ra tự động, không cần kỹ thuật viên nhấn nút. Toàn bộ vận hành được tổ chức thành ba pha nối tiếp nhau, để hệ thống đơn giản và trả lời được câu hỏi chuyển pha dựa trên tín hiệu nào.

**Pha nghỉ** là trạng thái mặc định khi khởi động, đồng thời là trạng thái hệ thống trở về khi kết thúc buổi tập hoặc khi phát hiện sự cố: servo không tải, dây cáp ở vị trí nhả, người tập có thể rút tay ra.

**Pha đo nỗ lực** bắt đầu khi người tập vào tư thế sẵn sàng và hai ô tham chiếu ổn định. Ở pha này hệ thống xác định người tập có tự khởi xướng được vận động hay không bằng cách mở một cửa sổ thăm dò: tạm ngưng trợ lực trong khoảng ngắn định trước rồi quan sát đáp ứng.

**Pha kéo trợ lực** bắt đầu khi cửa sổ thăm dò không thấy vận động tự nguyện đủ hoàn thành tầm vận động. Servo kéo theo biên độ đặt trước và giảm dần mức trợ lực mỗi lần pha đo nỗ lực phát hiện người tập tự làm được. Bài tập gắp thìa nằm trong pha này, nhãn trạng thái từ camera dùng để điều chỉnh trợ lực theo từng giai đoạn của tác vụ.

Mọi lỗi mà phần mềm phát hiện được, gồm mất phản hồi servo, mất đồng bộ dấu thời gian và vượt giới hạn hành trình, đều đưa hệ thống về pha nghỉ và ghi nhật ký. Nguyên mẫu chưa có điện trở shunt đo dòng, chưa có encoder góc và chưa có rơ-le ngắt nguồn, nên không có điều kiện chuyển pha nào dựa trên ba tín hiệu đó; an toàn khi mất nguồn dựa vào chốt chặn cơ khí và ngàm bẩy mở nẹp.

Trường hợp đeo nẹp lỏng hoặc ô tham chiếu trôi bất thường không phải một pha, mà là **cờ loại phiên đo**: hệ thống ngưng trợ lực, yêu cầu kiểm tra lại cách đeo, và phiên đó bị loại khỏi tập số liệu báo cáo kèm lý do. Đây là chỗ duy nhất việc kiểm soát chất lượng buổi tập được khai báo.

Điểm khó nhất là phân biệt vận động do người tập khởi xướng với chuyển động do chính cơ cấu tạo ra; nếu không, hệ thống sẽ tự thăng cấp cho một người không có vận động chủ động và số liệu đánh giá trở nên vô nghĩa. Cửa sổ thăm dò giải quyết đúng vấn đề đó ở mức tối giản. Độ dài cửa sổ, tần suất mở, tiêu chí nhận diện đáp ứng, hành vi khi không có đáp ứng và số lần lặp sẽ xác định bằng thực nghiệm; bắt buộc rà soát an toàn trước mọi lần chạy có cấp nguồn. Hạn chế phải thừa nhận: phương pháp không phát hiện được nỗ lực không tạo ra chuyển động.

### 7. Nhánh thị giác và bài tập gắp thìa

Camera nhận biết thìa và vùng đích trong bố trí cố định, rồi gán nhãn cho từng giai đoạn của bài tập: sẵn sàng, nắm thìa, nâng thìa, di chuyển, thành công, rơi thìa, đặt sai chỗ hoặc không xác định. Nhãn này vừa dùng tính chỉ số tác vụ vừa hiển thị phản hồi trực quan cho người tập; nhánh thị giác không đo lực ngón tay và không xác nhận phục hồi lâm sàng.

Bộ nhận biết thiết kế dạng cắm được: trước hết dùng xử lý ảnh cổ điển bằng OpenCV trên Orange Pi 5 Pro, chỉ thay bằng mô hình học sâu nếu kết quả đo thử trên đúng phần cứng đó không đạt. Nếu ước lượng độ sâu từ một ảnh thì phải hiệu chuẩn tỷ lệ trước khi coi tọa độ ảnh là tọa độ thực.

Các chỉ số của nhánh thị giác gồm độ đúng của nhãn, tỷ lệ nhãn không xác định, độ trễ đầu – cuối và số khung hình mỗi giây; tất cả đo ở mốc 3, và giao tiếp giữa Orange Pi 5 Pro với ESP32-S3 hiện chưa tích hợp. Độ trễ đầu – cuối của nhánh thị giác không thể nhỏ hơn một chu kỳ phơi sáng của camera, ở 30 khung hình mỗi giây là 33,3 ms; vì vậy chỉ tiêu không vượt quá 20 ms chỉ áp dụng cho đường từ cảm biến đến lệnh servo.

Bài tập thìa cần một tờ yêu cầu tác vụ ghi rõ loại thìa và khối lượng, kích thước và vị trí vùng đích, khoảng cách di chuyển, tiêu chí để coi là đặt thành công, thời gian tối đa cho một lượt và số lượt trong mỗi buổi tập; các thông số này xác định khi đo trên vật thật.

⟨HÌNH 5 — bố trí bàn thử: camera, vùng đích và mô hình tay giả⟩

---

## C. KẾT QUẢ CHẾ TẠO SƠ BỘ VÀ KẾ HOẠCH KIỂM ĐỊNH

*Số liệu trong phần C: "ghi nhận sơ bộ" là quan sát trên bàn đo, chưa có biên bản; "mục tiêu" là ngưỡng dự kiến, chưa đo.*

### 1. Chế tạo và khảo sát thực nghiệm 9 thế hệ cơ khí khóa nẹp

9 phương án khóa nẹp được in thử và đeo thử theo 3 nhóm nguyên lý. Nhóm 1 (Mech 1–3: vòng kẹp chữ C đàn hồi, rãnh trượt đuôi én, đai Velcro) cho thời gian đeo 55–80 s và không giữ được tiền tải.

Nhóm 2 (Mech 4–6: chốt xuyên ngang, khóa gài mặt mu, thanh răng rút) rút còn 40–65 s nhưng đòi hỏi hai tay hoặc căn chỉnh chính xác.

Nhóm 3 gồm Mech 8 (bản lề một trục kết hợp ngàm đàn hồi) đạt 28 s nhưng lỗi bền mỏi, và Mech 9 (khóa ngàm xoay 2 bản lề kép) khắc phục được lỗi gãy đó nên được chọn làm phương án triển khai. Mech 9 đã in xong nhưng chưa bấm giờ, nên chưa có con số thời gian đeo nào cho phương án này.

| Phương án | Nguyên lý khóa | Thời gian tự đeo | Sau 50 chu kỳ đóng mở |
|---|---|---|---|
| Mech 1–3 | vòng kẹp chữ C; rãnh trượt đuôi én; đai Velcro | 55–80 s | không đạt |
| Mech 4–6 | chốt xuyên ngang; khóa gài mặt mu; thanh răng rút | 40–65 s | không đạt |
| Mech 7 | không có số liệu trong hồ sơ hiện tại của nhóm | chưa có | chưa có |
| Mech 8 | bản lề một trục kết hợp ngàm đàn hồi | 28 s | lỗi bền mỏi |
| Mech 9 | khóa ngàm xoay 2 bản lề kép | chưa bấm giờ | đã in, chưa đo độ bền; phương án được chọn |

Các mốc thời gian là ghi nhận sơ bộ khi đeo thử nội bộ: chưa có biên bản đo, ngày thử, số lần lặp, người thực hiện và loại đồng hồ đo, nên chỉ dùng để so sánh định tính giữa các phương án.

Thời gian tự đeo và độ bền mỏi của Mech 9 vì vậy là chỉ tiêu kiểm nghiệm của mốc 2, và Mech 9 được giới thiệu như phương án hình học khắc phục lỗi gãy của Mech 8 chứ không kèm con số kết quả. Số chu kỳ đóng mở dùng cho phép đo bền sẽ chốt trong quy trình đo, vì 50 chu kỳ là rất nhỏ so với số lần đóng mở của một liệu trình nhiều tuần.

⟨HÌNH 6 — ảnh các thế hệ khóa nẹp đã in thử⟩

### 2. Thực nghiệm đo kiểm mạch thu nhận qua 2 vòng lặp thiết kế phần cứng

**Vòng lặp 1 — tầng khuếch đại dụng cụ INA333, G ≈ 6,5.** Ngõ ra sạch và các kênh cách ly tốt khi đo với nguồn tín hiệu chuẩn.

Khi lắp cảm biến thật và gài khóa tiền tải của nẹp, cầu phân áp sụt dưới 1,42 V và ngõ ra bão hòa cứng ở khoảng 2.838 mV, dải tuyến tính còn 1,44–1,92 V, nhiễu nền lúc nghỉ 50–135 mV.

Nguyên nhân là việc khuếch đại cố định không phù hợp với trở kháng và dải điện trở biến thiên lớn của phần tử áp trở khi có tiền tải.

**Vòng lặp 2 — bỏ INA333, đọc trực tiếp qua PGA ADS1115 kết hợp DSP 4 bước.** Vòng này giữ trọn dải ngõ vào 0–3.300 mV trên bàn đo, thêm đọc nháp và chờ 300 µs sau chuyển kênh; vùng chết 180 mV giữ đường nền ổn định khi nghỉ.

| Hạng mục | Đã đo, có biên bản | Ghi nhận sơ bộ trên bàn đo | Mục tiêu, chưa đo |
|---|---|---|---|
| Kiến trúc ngõ vào | chưa có | bỏ INA333, đọc trực tiếp PGA ADS1115, trọn dải 0–3.300 mV | thu trọn dải, không bão hòa ở tải thiết kế |
| Bão hòa ngõ ra | chưa có | vòng 1: cầu phân áp < 1,42 V, bão hòa ≈ 2.838 mV, dải tuyến tính 1,44–1,92 V | không bão hòa ở cấu hình 11 kênh |
| Nhiễu nền lúc nghỉ | chưa có | nhiễu thô 50–135 mV; sau vùng chết 180 mV, đầu ra lúc nghỉ ghim về 0 | V_pp ≤ 5 mV sau lọc, đo ≥ 10 phiên |
| Xuyên kênh | chưa có | đọc nháp và chờ 300 µs làm giảm bóng ma kênh; CH15 làm mốc | ngưỡng chưa xác định |
| SNR và độ tuyến tính | chưa có | chưa có ghi nhận đạt yêu cầu trên băng thử | SNR ≥ 18 dB; R² ≥ 0,90 |
| Tốc độ khung | chưa có | vòng 1 ≈ 22 Hz với 16 kênh, trễ chuyển kênh ~120 µs | ≥ 20 Hz toàn khung; tính toán ≈ 35 Hz với 11 kênh |
| Trôi nền dài hạn | chưa có | chưa có chuỗi log dài ngày | log ≥ 10 ngày với REF_1 và REF_2 |

Hai chỉ số SNR và R² sẽ được xác định bằng buổi đo có biên bản trên băng thử, ghi rõ tải chuẩn, số lần lặp, điều kiện môi trường, kiểm tra kênh tham chiếu trước và sau phiên, cùng định nghĩa phép tính: cửa sổ tín hiệu và cửa sổ nhiễu cho SNR, số điểm tải và phương pháp hồi quy cho R².

⟨HÌNH 7 — đồ thị vòng lặp 1 với hiện tượng bão hòa và vòng lặp 2 giữ trọn dải ngõ vào⟩

### 3. Kế hoạch kiểm chuẩn trên giàn đo và mô hình bàn tay giả

Phương tiện gồm giàn đo cơ học trục trượt tạo chuyển động gập–duỗi lặp lại theo biên độ và tốc độ đặt trước, tải chuẩn có khối lượng đã biết đặt đúng đường truyền lực của cơ cấu, mô hình bàn tay giả silicone và thước đo góc làm tham chiếu cho biên độ khớp cùng PROM, AROM.

Về tình trạng thiết bị: Velostat, băng đồng, ESP32-S3, Orange Pi 5 Pro, đồng hồ đo, bộ tạo tín hiệu và bộ chuyển mạch CD74HC4067 đã có, trong đó CD74HC4067 đã được chạy thử; 3 cảm biến gập Flex chưa có và phải mua ở mốc 1 dù vẫn nằm trong cấu hình 11 kênh đã chọn; giàn trục trượt, load cell, khối lượng chuẩn và silicone đúc mô hình tay giả thuộc nhóm phải chế tạo hoặc mua ở mốc 1; tình trạng của bộ chuyển đổi ADS1115 chưa được xác nhận. Những gì đã đo kiểm đến nay là bring-up mạch trên breadboard và đo bằng đồng hồ số, chưa có buổi đo nào trên giàn cơ học.

Toàn bộ kiểm định được thực hiện trên bàn thử và mô hình bàn tay giả; chỉ xem xét thử có cấp nguồn trên người trưởng thành khỏe mạnh sau khi rà soát an toàn đạt và có phê duyệt, theo một quy trình riêng; đề tài không thử trên người bệnh.

Tám quy trình đo được lập kế hoạch: (1) đáp ứng theo tải và R², với tải tăng dần và giảm dần, ít nhất 3 lượt lặp; (2) trễ đàn hồi và creep, so nhánh tăng và giảm, giữ tải không đổi 60 s; (3) độ lặp lại nội phiên và liên ngày trong cùng điều kiện và cùng cách lắp; (4) nhiễu nền và SNR ở trạng thái nghỉ, báo cáo cả tín hiệu thô lẫn sau lọc.

(5) xuyên kênh, kích thích một kênh và đọc các kênh nghỉ, lấy CH15 làm mốc; (6) trôi nền bằng chuỗi log ít nhất 10 ngày với REF_1 và REF_2; (7) tốc độ khung và trễ biên, đếm frame_id và đo từ khung dữ liệu đến thay đổi lệnh servo; (8) cơ cấu 3 tang trên mô hình bàn tay giả, gồm hành trình so với lệnh, dạng kẹp 3 chấu, hành vi nhả khi cắt nguồn và độ căng dây đo bằng phương pháp độc lập.

Mỗi phiên ghi ngày giờ, người vận hành, mã băm cấu hình, nhiệt độ và độ ẩm nếu có, cách lắp, số lần lặp, kết quả kiểm tra tham chiếu trước và sau. Phiên đo bị loại khi ô tham chiếu trôi vượt ngưỡng, mất đồng bộ dấu thời gian hoặc có can thiệp vào cách đeo giữa phiên; phiên bị loại phải ghi rõ lý do.

| Chỉ số | Cách đo | Mục tiêu hoặc ngưỡng | Căn cứ để chốt |
|---|---|---|---|
| Tỷ lệ hoàn thành tác vụ; thời gian; số lần rơi hoặc đặt sai | nhãn camera và log trên đồng hồ thời gian chung | chưa xác định | lượt thử đầu trên mô hình bàn tay giả |
| Tỷ lệ nhãn T_UNKNOWN; độ đúng nhãn trạng thái | log nhãn; bảng nhầm lẫn so với nhãn thủ công | chưa xác định | benchmark thị giác trên Orange Pi 5 Pro |
| Độ trễ thị giác đầu-cuối | dấu thời gian hai đầu | chưa xác định | đo trên phần cứng thật |
| Tốc độ khung thu thập | đếm frame_id | ≥ 20 Hz, chưa đo | tính toán ≈ 35 Hz, cần đo thực tế |
| Trễ cảm biến đến lệnh servo | log đồng bộ | ≤ 20 ms, chưa đo | đo trên bàn thử |
| Chuyển chế độ đúng và sai; trợ lực sai pha | log chế độ và nhãn đối chiếu | chưa xác định | phương pháp cửa sổ thăm dò đã chọn, chưa kiểm chứng |
| Biên độ và độ lặp lại chu kỳ gập–duỗi | log cảm biến Flex và thước đo góc | CV ≤ 5% nội phiên, ≤ 8% liên ngày | mốc 1 |
| Trôi tín hiệu | log REF_1 và REF_2 | chưa xác định | mốc 1, chuỗi log ≥ 10 ngày |
| SNR và R² trên băng thử | băng thử trục trượt và tải chuẩn | ≥ 18 dB và ≥ 0,90 | mốc 1, phải có biên bản đo |
| Trễ đàn hồi, creep, nhiễu nền | băng thử | h ≤ 18%; creep sau 60 s ≤ 8%; V_pp ≤ 5 mV sau lọc | mốc 1 |
| Khối lượng cụm đeo | cân thật, ghi ngày | 80–120 g, chưa cân cho cấu hình ba tang | cân sản phẩm hoàn chỉnh |
| Chi phí vật tư | bảng vật tư có ngày và báo giá | dự toán 1,0–1,3 triệu đồng cho cụm đeo, ~5,5 triệu đồng cho toàn hệ thống | kiểm toán bảng vật tư |

So sánh tối thiểu khi tích hợp là trợ lực cố định và AAN tự động trên cùng một mô hình bàn tay giả trong điều kiện tương đương. Độ nhạy riêng của từng nguồn đo được đánh giá bằng cách tắt từng nguồn, chỉ Flex, chỉ Velostat, chỉ camera hoặc đủ cả 3; phản hồi thị giác không được coi là bằng chứng cải thiện phục hồi.

### 4. Kế hoạch hoàn thiện dự án trong tương lai

Thứ tự triển khai gồm 5 giai đoạn. **Mốc 0** (~3 tuần): tờ yêu cầu tác vụ, bản đồ kênh cảm biến, phiếu buổi đo, đặc tả máy trạng thái và chuỗi log trôi nền ít nhất 10 ngày.

**Mốc 1** (~3–4 tuần): hiệu chuẩn Flex và Velostat trên băng thử, đo SNR, R², CV, trễ đàn hồi và creep. **Mốc 2** (~3–4 tuần): cơ cấu 3 tang trên mô hình bàn tay giả, đo hành trình, hành vi nhả khi mất nguồn, giới hạn an toàn, xuất bản vẽ CAD và đo độ bền Mech 9.

**Mốc 3** (~2–3 tuần): nhánh thị giác và bài tập thìa, benchmark trên Orange Pi 5 Pro. **Tích hợp** (~2 tuần): chu trình 3 bước trên mô hình bàn tay giả và so sánh trợ lực cố định với AAN tự động.

Chi phí vật tư cho cụm đeo dự toán 1,0–1,3 triệu đồng, toàn hệ thống và giàn thử khoảng 5,5 triệu đồng khi tận dụng thiết bị phòng thí nghiệm; đây là dự toán chưa kiểm toán, sẽ được lập thành bảng vật tư có ngày kèm báo giá.

Về khả năng hoàn thành: mốc 0, mốc 1, bản vẽ CAD, đo độ bền Mech 9 và cụm 3 tang thử trên mô hình bàn tay giả nằm trong khả năng chắc chắn; mốc 3 và tích hợp đầy đủ có rủi ro trễ vì nhánh thị giác chưa được benchmark và giao tiếp giữa 2 bo mạch chưa tích hợp; đề tài không cam kết hoàn thành chuỗi đánh giá trên người.

### 5. Kết luận

**Đã làm:** in thử và so sánh 9 phương án khóa nẹp, chọn Mech 9; hoàn thành 2 vòng lặp thiết kế mạch thu nhận, xác định nguyên nhân bão hòa ngõ vào ở vòng 1 và chuyển sang đọc trực tiếp qua PGA ADS1115.

Xác định chuỗi DSP 4 bước cùng bộ tham số đang dùng; chốt cấu hình cảm biến 11 kênh quét và cơ cấu 3 tang với duỗi chủ động bằng nhả dây; xây dựng định nghĩa EI, GAP, RAL cùng bảng tiêu chí kỹ thuật và mục tiêu thiết kế, chốt trước khi đo; đặc tả ba pha vận hành cùng phương pháp cửa sổ thăm dò.

Toàn bộ kết quả trên ở mức ghi nhận sơ bộ, chưa có biên bản đo.

**Chưa làm:** mua 3 cảm biến gập Flex; chế tạo cụm cảm biến theo cấu hình đã chọn; bấm giờ thời gian tự đeo của Mech 9; biên bản đo cho SNR, R², tốc độ khung và độ lặp lại; đo độ bền mỏi Mech 9 theo quy trình; xuất và lưu bản vẽ CAD; cân khối lượng cụm đeo; kiểm toán chi phí; viết firmware và các mô-đun phần mềm của luồng xử lý; benchmark nhánh thị giác; kiểm chứng quy tắc cửa sổ thăm dò; thử nghiệm trên người.

**Giới hạn:** thử nghiệm trên bàn đo và mô hình bàn tay giả không chứng minh hiệu quả trên người, không chứng minh an toàn đã được chứng nhận hay cải thiện chức năng sau đột quỵ; dữ liệu trên người khỏe không thay thế dữ liệu trên người bệnh.

Đề tài không tuyên bố tính mới hay "đầu tiên" cho tổ hợp AAN, Velostat, Flex, camera và bài tập gắp thìa; cảm biến áp trở chỉ cho chỉ số tương đối trong cùng người, không dùng làm thiết bị đo lực hay cơ chế an toàn.

### 6. Hướng phát triển

- **Phần cứng:** thay hệ dây dẫn rời bằng mạch in mềm đi chìm trong nẹp in 3D để tăng độ bền cơ học, chống đứt gãy và tăng tính thẩm mỹ; mở rộng từ 3 ngón lên 5 ngón sau khi có dữ liệu hiệu chuẩn đủ tin cậy.
- **Quy chuẩn y sinh và thử nghiệm lâm sàng:** sau khi hoàn tất các mốc kiểm định an toàn kỹ thuật trên giàn đo cơ học và mô hình bàn tay giả silicone, xây dựng hồ sơ xin phê duyệt của Hội đồng Đạo đức trong nghiên cứu y sinh học tại cơ sở y tế chuyên khoa trước khi triển khai thử nghiệm đối chứng lâm sàng với thang đo FMA-UE và ARAT; đây là giai đoạn sau, ngoài phạm vi đề tài này.
- **Điều khiển:** cá nhân hóa ngưỡng theo tầm vận động của từng người tập; các phương pháp điều khiển thích ứng nâng cao, kể cả học máy, chỉ được xem xét khi đã có bộ dữ liệu bàn thử và mô hình bàn tay giả đủ lớn cùng bộ quy tắc an toàn đã khóa.

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
