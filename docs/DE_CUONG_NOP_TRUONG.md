A. VẤN ĐỀ NGHIÊN CỨU

1. Lí do chọn đề tài

Đột quỵ là một trong những nguyên nhân hàng đầu gây tàn tật ở Việt Nam, với tỉ lệ hiện mắc tại năm 2019 khoảng 1.541 ca trên 100.000 dân và mỗi năm tăng thêm khoảng 222 ca mới trên 100.000 dân [1].

Hình 1: Tỉ lệ đột quỵ tại Việt Nam và di chứng bàn tay kéo dài [1, 2, 3]

Hơn nữa theo tổng quan của Cochrane:

-  Khoảng 80% người sống sót bị suy giảm vận động, trong nhóm liệt hoàn toàn chi trên chỉ khoảng một nửa phục hồi được một phần chức năng sau 6 tháng [2, 3].

- Bàn tay hồi phục chậm nhất và khó nhất, vì phải làm được các động tác tinh như cầm thìa, cài cúc áo, cầm bút chứ không chỉ co duỗi.

Việc theo dõi quá trình tập luyện gần như chưa được định lượng. Thang FMA-UE và ARAT chỉ đo gián đoạn, vài tuần một lần và phụ thuộc người khám. Thiết bị đeo cổ tay Manumeter muốn phát hiện tiến triển thì người đeo phải thay đổi tới khoảng 31% cường độ sử dụng trong ngày, đồng thời đếm sai 100 - 200 lần dương tính giả mỗi giờ [4].

Khảo sát với kĩ thuật viên phục hồi chức năng tháng 9/2026 cho thấy các loại găng hiện có chưa phù hợp tập tại nhà ở Việt Nam về thao tác đeo.

Chính vì những vấn đề trên, nhóm đã lựa chọn nghiên cứu đề tài “Nghiên cứu và phát triển găng tay hỗ trợ phục hồi chức năng sau đột quỵ cho vận động tinh”.

2. Cơ sở lý thuyết về y sinh

2.1. Đại diện vỏ não và cơ chế phản hồi Hebbian

Nghiên cứu của Penfield & Boldrey [5] và mạng SCAN của Gordon et al. [6] cho thấy bàn tay chiếm diện tích đại diện vận động rất lớn trên vỏ não, định hướng cho việc tập trung vào 3 ngón trụ cột (cái, trỏ, giữa).

Hình 2: Bản đồ Homunculus [5] và sự phân bổ chi phối bàn tay [6]

Theo học thuyết Hebb [7] và nguyên lý phục hồi chức năng [8, 9], việc cung cấp phản hồi cảm giác đồng bộ với nỗ lực vận động giúp định hướng tập luyện. Nhóm khai thác cơ sở này để xây dựng cơ chế phản hồi thị giác từ đáp ứng áp trở vi mô.

2.2. Trương lực cơ, chênh lệch tầm vận động (GAP) và độ tin cậy đo lường

Sau đột quỵ, suy giảm vận động thường kết hợp giữa yếu cơ và tăng trương lực co cứng [10, 11]. Nhóm sẽ khảo sát độ thiếu hụt tầm vận động GAP = PROM − AROM như một chỉ số mô tả chênh lệch góc (đo bằng công cụ ngoài). Về thống kê y sinh, độ tin cậy của hệ thống đo được đánh giá qua hệ số biến thiên (CV), sai số chuẩn (SEM) và ngưỡng MDC thực tế của thiết bị [4].

3. Xác định vấn đề nghiên cứu

- Nghiên cứu xây dựng khung nẹp 3 ngón tích hợp cảm biến phát hiện vận động chủ động trong thời gian thực.

- Nghiên cứu sử dụng cảm biến gập Flex và cảm biến áp trở Velostat bố trí theo cặp lòng - mu để đọc đáp ứng bóp của ngón cái, trỏ, giữa.

- Nghiên cứu phương pháp thu nhận và lọc tín hiệu với ADC 16-bit ADS1115 và vi điều khiển ESP32-S3.

- Nghiên cứu phương pháp tính bộ chỉ số EI, GAP, RAL để theo dõi tiến triển.

- Nghiên cứu phương pháp điều khiển trợ lực theo nhu cầu với cơ cấu servo - dây cáp - 3 tang.

- Nghiên cứu ứng dụng mô hình ước lượng độ sâu đơn mục Depth Anything V2 để đo khoảng cách 3D tay - vật và hỗ trợ định thời đón trước trong bài tập vận động tinh.

4. Mục tiêu nghiên cứu

- Nghiên cứu thiết kế và phát triển găng tay nẹp 3 ngón hỗ trợ người tập đi từ vận động gập - duỗi đến thao tác gắp thìa dạng kẹp 3 chấu (tripod pinch).

- Hoàn thiện khung nẹp có khóa ngàm xoay, người yếu tay tự đeo được bằng một tay.

- Xây dựng cụm 21 kênh cảm biến gồm 16 ô Velostat trên ngón, 2 ô tham chiếu và 3 Flex. Nhóm đặt mục tiêu quét đủ 21 kênh với tốc độ ≥15 Hz.

- Xây dựng cơ cấu servo - dây cáp - 3 tang tạo dạng kẹp 3 chấu, trợ lực giảm dần theo đáp ứng của người tập, có đường tháo an toàn độc lập.

- Xây dựng bộ chỉ số EI, GAP, RAL và chỉ số bài tập gắp thìa.

- Kiểm chứng nguyên mẫu trên giàn đo cơ học và mô hình bàn tay giả silicone, không thử trên người bệnh.

5. Tiêu chí của dự án

- Tốc độ quét đủ 21 kênh ≥15 Hz. Nhóm sẽ đo độ trễ từ lúc cảm biến biến đổi đến khi phát lệnh servo trên toàn chuỗi thu nhận và xử lí, sau đó mới xác định ngưỡng đáp ứng.

- Tỉ số tín hiệu trên nhiễu ≥18 dB và R² ≥0,90 khi thử với tải chuẩn. Nhiễu nền sau lọc ≤5 mV đỉnh–đỉnh, đo trên nhánh không áp dụng vùng chết.

- Phân biệt đúng hướng vận động ≥ 90%, phân loại đúng mức kích hoạt ≥ 85%.

- Hệ số biến thiên ≤ 5% trong cùng buổi và ≤ 8% giữa các ngày, trễ đàn hồi ≤ 18%, độ dãn tải tĩnh sau 60 s ≤ 8%.

B. GIẢI PHÁP VÀ THIẾT KẾ

I. Tổng quan đề tài

Găng tay nẹp 3 ngón hỗ trợ việc theo dõi và trợ lực vận động tinh cho ngón cái, trỏ, giữa. Găng được đeo bằng một tay với khóa ngàm xoay, đọc đáp ứng ngón bằng Flex và Velostat, xử lí bằng ESP32-S3 và trợ lực bằng servo cuốn dây. Hệ thống thị giác không gian 3D ứng dụng mô hình Depth Anything V2 ước lượng khoảng cách thực tế tay - vật để định thời trợ lực đón trước và hiển thị phản hồi trực quan bài tập cho người bệnh. Người tập chỉ cần đeo nẹp và vận động tự do hoặc tập theo hướng dẫn.

Hình 3: Sơ đồ chức năng của bộ ba ngón trụ cột trong thao tác kẹp 3 chấu và bố trí các điểm cảm biến [12]

II. Bất cập và giới hạn của các giải pháp hiện tại và giải pháp của đề tài

Qua khảo sát, nhóm nhận thấy các giải pháp hiện có vẫn còn hạn chế khi theo dõi vận động bàn tay thường xuyên và tổ chức bài tập với vật dụng sinh hoạt. Cụ thể:

- Thang đo FMA-UE và ARAT: đo gián đoạn, 2 - 4 tuần/lần và phụ thuộc người khám.

- Thiết bị đeo cổ tay Manumeter: chỉ đếm chuyển động thô, muốn phát hiện tiến triển phải thay đổi tới 31% cường độ sử dụng trong ngày, đồng thời đếm sai 100 - 200 lần mỗi giờ [4].

- Điện cơ bề mặt sEMG: suy giảm chất lượng khi ra mồ hôi và khó tách riêng từng nhóm cơ cẳng tay.

- Găng tay robot thương mại: chủ yếu kéo thụ động cố định theo chu kỳ.

- Găng mềm điều khiển từ tính (Li et al., 2024) [14]: mới dừng ở bước kiểm chứng nguyên lí vật liệu trên người khỏe mạnh, chưa lượng hóa bài tập gắn với vật dụng sinh hoạt hàng ngày.

Từ những giới hạn đó, nhóm đã lựa chọn giải pháp mới là xây dựng găng nẹp 3 ngón trụ cột cái, trỏ, giữa đảm nhiệm vận động tinh, lấy bài tập gắp thìa với vật thật làm đơn vị đánh giá thay vì đếm chuyển động thô. Đồng thời ứng dụng cảm biến áp trở màng polymer Velostat [15] kết hợp thuật toán vi sai hai vách lòng - mu và bộ ba chỉ số EI, GAP, RAL tính tương đối trong cùng một người để theo dõi tiến triển. Nhóm còn xây dựng cơ chế trợ lực theo nhu cầu với cửa sổ thăm dò ngắn để phân biệt vận động do người tập khởi xướng với chuyển động do máy tạo ra, kết hợp nhánh thị giác không gian 3D ứng dụng mô hình nền tảng Depth Anything V2 trên Orange Pi 5 Pro để ước lượng cự ly thực tế tay - vật, định thời đón trước và lượng hóa toàn diện bài tập.

III. Nguyên lý và cơ chế hoạt động của hệ thống

3.1. Sơ đồ khối kết nối

Hình 4: Sơ đồ khối kiến trúc phân tán 4 tầng

Hệ thống được tổ chức theo kiến trúc phân tán 3 nhóm tương hỗ:

- Nhóm 1 (Tầng nẹp đeo & trợ lực cơ học): Khung nẹp 3 ngón in 3D tích hợp mạng cảm biến Velostat, cảm biến Flex và cụm 3 tang servo cuốn cáp Bowden độc lập.

- Nhóm 2 (Tầng thu thập đa kênh & xử lý DSP): ESP32-S3 đọc 21 kênh cảm biến qua 2 CD74HC4067 và ADS1115 (16-bit), thực hiện chuỗi lọc số DSP 2 nhánh và tính toán bộ ba chỉ số EI - GAP - RAL.

- Nhóm 3 (Tầng thị giác không gian 3D & tác vụ): Camera RGB kết hợp máy tính nhúng Orange Pi 5 Pro chạy mô hình Depth Anything V2 qua NPU, ước lượng khoảng cách 3D thực tế, định thời đón trước (TTC) và phản hồi trực quan bài tập.

Điểm khác biệt so với găng kéo thụ động là hệ thống chỉ trợ lực khi nỗ lực chủ động chưa đủ hoàn thành tầm vận động, và tự giảm trợ lực khi người tập đã tự khởi xướng chuyển động.

3.2. Sơ đồ nguyên lý hoạt động

Hình 5: Sơ đồ nguyên lý hoạt động

### Nhóm 1: Cơ khí nẹp đeo, cảm biến tiếp xúc và cơ cấu trợ lực

#### 3.2.1. Xây dựng cơ chế đeo ngàm xoay một tay và cụm 3 tang servo

Để người yếu tay tự đeo được mà nẹp vẫn đủ cứng giữ cảm biến và neo dây cáp là thách thức ban đầu của nhóm, nhóm quyết định lựa chọn ý tưởng “ngàm xoay” đóng bằng một tay với 2 bản lề.

- Khung nẹp ôm 3 ngón cái, trỏ, giữa, có khớp rãnh trượt bù chênh lệch chiều dài ngón.
- Chốt mở nhanh trên từng đốt nẹp tạo đường tháo tay độc lập với truyền động.
- Cụm 3 tang cuốn cáp Bowden dẫn động bởi 3 động cơ servo độc lập, cho phép kéo chủ động theo chiều gập và nhả dây khi chuyển sang chiều duỗi; nẹp đàn hồi hồi vị mu tay hỗ trợ ngón trở về vị trí mở tự nhiên.

Hình 6: Khung nẹp phương án 9 và bố trí 3 tang

#### 3.2.2. Xây dựng cơ chế cảm biến màng áp trở vi sai lòng - mu và cảm biến gập Flex

Nhóm tiến hành xây dựng cơ chế cho phép cảm biến phân biệt được hai tình huống: ngón ép vào nẹp và ngón tiếp xúc vật.

- Một ô đơn lẻ đều tăng đáp ứng ở cả hai tình huống.
- Nhóm bố trí 16 ô Velostat trên 3 ngón theo các cặp mặt lòng - mặt mu. Vị trí của từng cặp được bố trí theo cấu trúc Sandwich hai vách nẹp.
- Cấu hình gồm 21 kênh cảm biến sử dụng 2 CD74HC4067: 16 ô Velostat trên ngón, 2 ô tham chiếu không chịu tải để theo dõi trôi nền và 3 cảm biến Flex đo biến thiên góc uốn gập - duỗi của các khớp ngón.

Hình 7: Cấu tạo mặt cắt cảm biến Sandwich và vi sai hai vách

### Nhóm 2: Mạch thu nhận đa kênh, xử lý tín hiệu số (DSP) và điều khiển trợ lực AAN

#### 3.2.3. Xây dựng cơ chế thu nhận và chuỗi lọc số DSP hai nhánh

Để đọc chính xác hai loại cảm biến có bản chất vật lí khác nhau, nhóm quyết định tách thuật toán thành 2 nhánh xử lí độc lập.

- Chuỗi phần cứng: cầu phân áp -> 2 CD74HC4067 -> ADS1115 (đọc trực tiếp qua PGA, giao tiếp I2C) -> ESP32-S3.
- Sau mỗi lần chuyển kênh, vi điều khiển chờ 300 µs, bỏ kết quả đọc nháp rồi mới nhận mẫu chính thức. Nhóm chỉ dùng mẫu của lần chuyển đổi hoàn tất sau khi chọn kênh và kiểm tra khoảng chờ bằng phép đo xuyên kênh.
- Nhóm đặt mục tiêu quét đủ 21 kênh với tốc độ ≥15 Hz.

Nhánh 1 xử lí Velostat:
- Tự động bám đường nền tĩnh (Adaptive Baseline Tracking): khi ngón nghỉ, đường nền cập nhật chậm (0,998 phần cũ + 0,002 phần mới) để bù trôi do nhiệt độ và mồ hôi.
- Nhóm chọn ngưỡng thử 180 mV, lớn hơn dải nhiễu 50 - 135 mV đã ghi nhận. Ngưỡng này sẽ được hiệu chỉnh theo từng kênh và kiểm tra lại để không làm mất tín hiệu nỗ lực nhỏ.
- Lọc thông thấp hàm mũ (EMA, α = 0,20): làm mượt đáp ứng trước khi tính tín hiệu vi sai lòng - mu.
- Để đánh giá nhiễu, nhóm lưu thêm một nhánh tín hiệu chỉ bám đường nền và lọc EMA, không áp dụng vùng chết.

Nhánh 2 xử lí Flex:
- Lọc EMA (α = 0,20) khử nhiễu tần số cao.
- Ánh xạ liên tục điện áp sang góc uốn qua hàm hồi quy hiệu chuẩn với thước đo góc ngoài.
- Nhóm không áp dụng vùng chết cho Flex để giữ lại các biến thiên gập - duỗi có biên độ nhỏ.

#### 3.2.4. Xây dựng cơ chế tính bộ ba chỉ số EI - GAP - RAL và thuật toán trợ lực theo nhu cầu

Để biết một thay đổi là do vận động hay do chính phép đo, nhóm quyết định dùng hệ số biến thiên, sai số chuẩn và ngưỡng khác biệt nhỏ nhất có ý nghĩa làm khung đánh giá [4].

- EI: tích phân đáp ứng tương đối trong pha vận động chủ động, chuẩn hóa theo mức tham chiếu của buổi tập.
- GAP: hiệu giữa tầm vận động thụ động PROM và chủ động AROM. Thước đo góc ngoài cho số đo theo độ, Flex đã hiệu chuẩn cho biến thiên gập để đối chiếu.
- RAL: mức trợ lực nhỏ nhất đủ hoàn thành một chu kỳ gập - duỗi theo tiêu chí đặt trước.

Trợ lực phải bổ sung phần vận động người tập còn thiếu, thay vì làm toàn bộ động tác. Nhóm chọn cơ chế trợ lực theo nhu cầu (assist-as-needed - AAN):
- Truyền động: servo cuốn dây câu cá trực tiếp lên 3 tang riêng, mỗi ngón một tang. Khi chuyển sang chiều duỗi, servo chủ động nhả dây.
- Khó khăn của điều khiển là chuyển động nhìn thấy có thể do người tập hoặc do chính servo tạo ra. Nhóm chọn cửa sổ thăm dò: tạm ngưng trợ lực trong khoảng ngắn rồi quan sát đáp ứng, từ đó tự động chuyển giữa đo nỗ lực và kéo trợ lực mà không cần kĩ thuật viên nhấn nút.
- Vận hành chia làm 3 pha:
  + Nghỉ: dùng khi khởi động, kết thúc buổi tập hoặc có lệnh dừng do sự cố. Bộ điều khiển ngưng kéo và ra lệnh cho servo nhả dây. Chốt mở nhanh tạo đường tháo nẹp độc lập với bộ điều khiển.
  + Đo nỗ lực: bắt đầu khi người tập vào tư thế sẵn sàng và 2 ô tham chiếu ổn định. Mở cửa sổ thăm dò để quan sát vận động tự khởi xướng.
  + Kéo trợ lực: bắt đầu khi đáp ứng trong cửa sổ chưa đủ hoàn thành tầm vận động. Servo kéo theo biên độ đặt trước, giảm trợ lực khi người tập tự làm được.

### Nhóm 3: Thị giác không gian 3D Depth Anything V2 và lượng hóa tác vụ vận động tinh

#### 3.2.5. Xây dựng cơ chế ước lượng cự ly không gian 3D và định thời đón trước

Flex và Velostat theo dõi lực tiếp xúc và góc ngón tay nhưng không cho biết cự ly hình học giữa bàn tay và vật thể trước khi chạm, dẫn đến nguy cơ co siết ngón quá sớm hoặc mở ngón sai thời điểm. Do đó, nhóm tích hợp nhánh thị giác không gian 3D ứng dụng mô hình nền tảng Depth Anything V2 (Metric Depth) chạy suy luận trên NPU của máy tính nhúng Orange Pi 5 Pro.

- Mô hình Depth Anything V2 ước lượng bản đồ độ sâu hệ mét 3D trực tiếp từ camera đơn RGB trong không gian thực, khắc phục sự phụ thuộc vào vật chuẩn hay marker cố định.
- Thuật toán theo dõi vị trí tương đối giữa cụm nẹp đầu ngón tay và vật thể đích, tính toán khoảng cách 3D thực tế d(t) và suy ra thời gian tới tiếp xúc dự kiến (Time-To-Contact - TTC).
- Định thời trợ lực đón trước: Khi bàn tay tiến gần vật thể với cự ly giảm dần theo vận tốc tiếp cận, hệ thống chủ động điều phối cơ cấu mở ngón chuẩn bị khẩu độ đón vật; chỉ khi mạng cảm biến Velostat và Flex xác nhận tiếp xúc vật lý thực tế thì bộ điều khiển mới kích hoạt pha trợ lực kẹp giữ, giúp động tác tự nhiên và chính xác.

#### 3.2.6. Xây dựng cơ chế phân loại tiến trình bài tập và phản hồi trực quan

Nhánh thị giác đảm nhiệm lượng hóa tiến trình bài tập gắp thìa dạng kẹp 3 chấu (tripod pinch) và cung cấp phản hồi trực quan:

- Phân loại trực tiếp các pha bài tập: sẵn sàng, tiếp cận đón vật, kẹp giữ thìa, nâng thìa, di chuyển, đặt vào vùng đích, rơi thìa hoặc hoàn thành phiên tập.
- Nhãn phân loại bài tập và thông số cự ly được ghi nhận đồng bộ vào nhật ký tập luyện, đồng thời hiển thị trực quan theo thời gian thực trên màn hình giao diện để người bệnh tự quan sát kết quả vận động của chính mình.
- Tín hiệu thị giác chỉ tham gia điều phối khẩu độ đón trước và đánh giá tác vụ, tuyệt đối không trực tiếp phát lệnh ép siết ngón khi chưa có tín hiệu xác nhận từ cảm biến áp trở trên găng tay.

C. KẾ HOẠCH CHẾ TẠO VÀ PHƯƠNG PHÁP THỬ NGHIỆM

### Nhóm 1: Chế tạo cơ khí nẹp đeo, bố trí cảm biến và kiểm thử cơ cấu trợ lực

#### 1. Thử nghiệm in 3D nẹp ngón, khóa ngàm một tay và cơ cấu 3 tang cuốn cáp

Nhóm khảo sát khóa nẹp trước, vì nẹp là nơi bố trí cảm biến áp lực. Nhóm bắt đầu thiết kế nẹp từ các đốt đầu tiên.

- Qua các phương án vòng kẹp, rãnh trượt và đai dán, khó khăn chính là giữ tiền tải khi chỉ dùng một tay.
- Các dạng chốt và thanh răng giảm thời gian đeo nhưng đòi hỏi căn chỉnh chính xác. Vì vậy đến thời điểm hiện tại, nhóm quyết định sử dụng nẹp 2 bản lề để làm thiết kế chính.
- Kiểm thử cơ cấu 3 tang servo trên mô hình bàn tay giả: đo hành trình thực tế so với góc quay servo, dạng kẹp 3 chấu có đạt hình học mong muốn hay không, hành vi nhả dây khi chuyển sang pha duỗi ngón, độ căng dây đo bằng lực kế độc lập và thời gian tháo nẹp khẩn cấp qua chốt mở nhanh.

Hình 8: Quá trình tiến hóa 9 thế hệ khóa nẹp in 3D

#### 2. Hiệu chuẩn và kiểm thử cảm biến Velostat vi sai hai vách và cảm biến gập Flex

a) Xây dựng thành công cảm biến áp lực Velostat trên nẹp:
Nhóm đã xây dựng và bố trí thành công mạng cảm biến áp lực Velostat lên nẹp (đốt đơn) và bước đầu kiểm thử nguyên lí hoạt động.

b) Kế hoạch kiểm thử cảm biến áp lực Velostat và cảm biến Flex:
Để màng Velostat chạy ổn định trên khung nẹp, nhóm kiểm từng ô trên băng thử có tải chuẩn trước khi ghép cặp lòng - mu, sau đó đối chiếu với Flex và 2 ô tham chiếu:
- Đáp ứng theo tải và độ tuyến tính: tải tăng dần rồi giảm dần, ít nhất 3 lượt, lấy đường chuẩn và R² của từng ô.
- Trễ đàn hồi và độ dãn tải tĩnh: do đặc tính của vật liệu Velostat, nhóm so nhánh tăng tải với nhánh giảm tải, giữ tải không đổi 60 s.
- Độ lặp lại trong cùng buổi và giữa các ngày, cùng một cách lắp.
- Nhiễu nền được đo khi giữ đầu vào ổn định. SNR được tính từ cửa sổ có tín hiệu tải chuẩn và cửa sổ nhiễu tương ứng. Nhóm đối chiếu tín hiệu thô với tín hiệu sau lọc nhưng không áp dụng vùng chết.
- Xuyên kênh: kích thích một kênh, sau đó đọc các kênh đang nghỉ và đối chiếu với kênh kiểm tra nối đất. Kênh này được ghi riêng trong bản đồ kênh.
- Trôi nền: nhóm ghi nhật ký ít nhất 10 ngày với 2 ô tham chiếu không chịu tải để theo dõi độ trôi chung của hệ thống. Độ dãn do tải của các ô trên ngón được kiểm tra riêng bằng phép giữ tải.
- Kiểm tra tín hiệu vi sai cặp lòng - mu: thao tác ép ngón vào nẹp và ngón tiếp xúc vật phải cho hai mẫu đáp ứng điện áp ngược hướng rõ rệt.
- Hiệu chuẩn cảm biến Flex: đối chiếu điện áp đọc từ Flex với góc gập thực tế đo bằng thước đo góc ngoài trên cùng mô hình bàn tay giả, thiết lập hàm hồi quy chuyển đổi liên tục.

### Nhóm 2: Chế tạo mạch thu nhận, lập trình DSP và kiểm thử điều khiển AAN

#### 3. Kiểm thử mạch thu nhận 21 kênh và chuỗi lọc số DSP trên ADS1115

Nhóm đã thử 2 cấu hình mạch, đối chiếu bằng đồng hồ số, máy hiện sóng FNIRSI 2C23T và đồ thị dữ liệu đọc về máy tính.

- Vòng 1 dùng INA333 với hệ số khuếch đại khoảng 6,5. Với nguồn chuẩn, ngõ ra sạch và các kênh cách ly tốt. Khi lắp Velostat thật và gài tiền tải nẹp, điện áp cầu phân áp xuống dưới 1,42 V, ngõ ra kẹt khoảng 2.838 mV và vùng tuyến tính chỉ còn 1,44 - 1,92 V. Khuếch đại cố định không phù hợp với dải điện trở biến thiên lớn khi có tiền tải, nên nhóm bỏ tầng này.
- Vòng 2 bỏ INA333, đọc trực tiếp qua ADS1115 (16-bit) và xử lí theo chuỗi DSP 4 bước: bám đường nền động, lọc EMA và vùng chết 180 mV cho Velostat; lọc EMA và ánh xạ góc liên tục cho Flex. Qua các lượt chạy thử, nhóm ghi nhận dải ngõ vào 0 - 3.300 mV và tốc độ quét 21 kênh đạt ≥15 Hz.

Hình 9: Chuỗi xử lý tín hiệu số (DSP) 4 bước trên mạch đọc trực tiếp ADS1115 ở Vòng lặp 2

#### 4. Đánh giá độ tin cậy bộ chỉ số EI - GAP - RAL và chu trình trợ lực ba pha trên giàn đo

- GAP: đối chiếu biên độ gập đọc từ Flex đã hiệu chuẩn với thước đo góc ngoài, trên cùng một mô hình bàn tay giả, ở cả tầm vận động thụ động và chủ động.
- EI và RAL: kiểm trên giàn đo cơ học gồm giàn trục trượt tạo chuyển động gập - duỗi lặp lại theo biên độ và tốc độ đặt trước, tải chuẩn đặt đúng đường truyền lực, mô hình bàn tay giả silicone làm đối tượng đeo.
- Độ tin cậy từng chỉ số đánh giá bằng hệ số biến thiên (CV nội phiên, CV liên ngày), sai số chuẩn của phép đo SEM và ngưỡng khác biệt nhỏ nhất có ý nghĩa MDC [4].
- Kiểm thử thuật toán AAN ba pha: đánh giá số lần chuyển pha đúng và sai so với nhãn đối chiếu trên mô hình, số sự kiện trợ lực sai pha trong cửa sổ thăm dò, độ trễ từ lúc cảm biến nhận tín hiệu đến khi servo phát lực.

### Nhóm 3: Triển khai thị giác không gian Depth Anything V2 và tích hợp toàn hệ thống

#### 5. Triển khai mô hình Depth Anything V2 trên Orange Pi 5 Pro và kiểm chuẩn cự ly 3D

- Cài đặt mô hình nền tảng Depth Anything V2 (bản Metric Depth tối ưu hóa) chạy suy luận trên bộ xử lý đồ họa NPU của máy tính nhúng Orange Pi 5 Pro.
- Kiểm chuẩn độ chính xác ước lượng độ sâu: đối chiếu giá trị cự ly d(t) suy ra từ bản đồ độ sâu với khoảng cách vật lý thực tế đo bằng thước laser hoặc cảm biến chuẩn ở các khoảng cách từ 5 cm đến 50 cm.
- Đánh giá thuật toán định thời đón trước: đo sai số dự đoán thời gian tới tiếp xúc (TTC) ở các vận tốc tiếp cận khác nhau của bàn tay, ghi nhận độ trễ suy luận của mô hình và tốc độ khung hình (fps) trên NPU.

#### 6. Tích hợp toàn diện hệ thống qua bài tập gắp thìa dạng kẹp 3 chấu (Tripod Pinch)

- Thiết lập kịch bản bài tập: loại thìa, kích thước, vị trí xuất phát, khoảng cách di chuyển đến vùng đích, tiêu chí đặt thành công và số lượt mỗi phiên thử nghiệm.
- Chỉ số tác vụ gồm tỉ lệ hoàn thành, thời gian hoàn thành, số lần rơi thìa hoặc đặt sai vị trí, trích xuất từ nhãn thị giác và nhật ký đồng bộ thời gian trên hệ thống.
- So sánh kết quả nhận biết trạng thái khi dùng riêng từng nguồn cảm biến (chỉ găng tay, chỉ thị giác) so với khi kết hợp đồng bộ cả găng tay và mô hình Depth Anything V2.
- So sánh hiệu quả vận động giữa chế độ trợ lực cố định và chế độ trợ lực theo nhu cầu AAN kết hợp thị giác đón trước trên cùng mô hình bàn tay giả và bài tập gắp thìa chuẩn hóa. Đây là phép kiểm chứng cốt lõi chứng minh tính ưu việt của giải pháp tích hợp.

TÀI LIỆU THAM KHẢO

[1] Tran et al. (2025), “Comprehensive analysis of stroke epidemiology in Vietnam: Insights from GBD 1990–2019 and RES-Q 2017–2023”, Global Epidemiology, 9:100199.

[2] Pollock A., et al. (2014), “Interventions for improving upper limb function after stroke”, Cochrane Database of Systematic Reviews, CD010820.

[3] Langhorne P., Coupar F., Pollock A. (2009), “Motor recovery after stroke: a systematic review”, The Lancet Neurology, 8(8), 741–754.

[4] Schwerz de Lucena D., et al. (2022), “Providing Real-Time Wearable Feedback to Increase Hand Use after Stroke: A Randomized Controlled Trial”, Sensors, 22(18):6938.

[5] Penfield W., Boldrey E. (1937), “Somatic motor and sensory representation in the cerebral cortex of man as studied by electrical stimulation”, Brain, 60(4), 389–443.

[6] Gordon E. M., et al. (2023), “A somato-cognitive action network alternates with effector regions in motor cortex”, Nature, 617, 351–359.

[7] Hebb D. O. (1949), “The Organization of Behavior: A Neuropsychological Theory”, Wiley, New York.

[8] Bộ Y tế (2014), “Hướng dẫn chẩn đoán và điều trị Phục hồi chức năng sau đột quỵ não”, Quyết định số 4039/QĐ-BYT.

[9] Cao Minh Châu, Nguyễn Thị Kim Liên, Trần Trọng Hải (2020), “Giáo trình Phục hồi chức năng”, Nhà xuất bản Y học, Hà Nội.

[10] Amin F., et al. (2024), “Remote Monitoring for the Management of Spasticity: Challenges, Opportunities and Proposed Technological Solution”, Sensors, PMC11793859.

[11] Lin B. S., et al. (2022), “Design of a Multi-Sensor System for Exploring Upper Limb Spasticity in Stroke Patients”, Sensors, 22(19):7212.

[12] Kapandji I. A. (2007), “The Physiology of the Joints, Volume 1: Upper Limb”, Churchill Livingstone / Elsevier.

[13] Radder B., et al. (2018), “Home-based robot-assisted arm training with an interactive robotic glove after stroke (IRONHAND)”, Journal of Rehabilitation Medicine, 50, 598–606.

[14] Li M., et al. (2024), “A magnetically controlled soft robotic glove for hand rehabilitation”, Device, 2(4):100215.

[15] Hopkins M., Vaidyanathan R., McGregor A. H. (2020), “Examination of the Performance Characteristics of Velostat as an In-Socket Pressure Sensing Material”, IEEE Sensors Journal, 20(12).