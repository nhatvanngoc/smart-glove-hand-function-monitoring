# 01 — Định nghĩa đề tài

> **Cập nhật:** 2026-10-19 · **Hướng hiện hành:** `DEC-REHAB-001` cùng các quyết định kỹ thuật đang hiệu lực trong [`research/context/DECISION_LOG.md`](../research/context/DECISION_LOG.md).
> **Tên đang dùng để phát triển nội dung, chưa phải tên nộp cuối:** *Nghiên cứu và phát triển găng tay hỗ trợ phục hồi chức năng sau đột quỵ cho vận động tinh.*
> Đây là hướng thiết kế/nghiên cứu; không khẳng định nguyên mẫu đã hoàn thành, đã thử trên bệnh nhân, đã an toàn hoặc đã chứng minh hiệu quả lâm sàng.

## 1. Vấn đề và mục tiêu người dùng

Đề tài hướng tới người trung niên sau đột quỵ gặp khó khăn khi vận động tinh bàn tay và có nhu cầu luyện tập tại nhà. “Tại nhà” là bối cảnh sử dụng mong muốn, chưa phải khả năng sử dụng tại nhà đã được xác nhận. Mục tiêu chức năng là phát triển găng tay có thể hỗ trợ người tập theo lộ trình từ vận động ngón cơ bản tới thao tác phối hợp nhiều ngón với một vật thể.

## 2. Chức năng cốt lõi dự kiến

Hệ thống dự kiến có ba giai đoạn liên tiếp:

1. **Hỗ trợ gập–duỗi ngón:** khi người tập chưa tự khởi động hoặc hoàn thành chuyển động, cơ cấu hỗ trợ vận động theo chu kỳ/biên độ đã được thiết kế. Khả năng tạo cả gập lẫn duỗi an toàn còn phụ thuộc vào cơ cấu hồi/nhả dây và phải được kiểm chứng.
2. **Chuyển tự động sang AAN:** bộ điều khiển tự chuyển khi các đặc trưng vận động/tín hiệu đạt quy tắc ngưỡng đã xác định trước. Không yêu cầu KTV nhấn nút chuyển chế độ trong quá trình sử dụng. Tín hiệu và giá trị ngưỡng, số lần lặp, cửa sổ quan sát, hysteresis và trạng thái lỗi còn mở; phải xác lập bằng hiệu chuẩn/bench/phantom, không đặt sau khi xem kết quả.
3. **Luyện thao tác vận động tinh:** người tập phối hợp ngón cái, trỏ và giữa để gắp thìa, nhấc lên, di chuyển đến vị trí đích đã định, rồi thả. Camera theo dõi thìa/vùng đích, nhận biết tiến trình và kết quả nhìn thấy được, sau đó đưa phản hồi trực quan tức thời. Thìa và mục tiêu cụ thể cần được chuẩn hóa trước thử nghiệm.

Mục đích là xây dựng một bài tập có chức năng rõ ràng, không phải chỉ ghi dữ liệu cảm biến hay chỉ trình diễn AI. Tập phối hợp ba ngón là lựa chọn thiết kế; nhận định nó giúp phục hồi thần kinh tốt hơn các bài khác là giả thuyết, chưa được chứng minh bởi dự án.

## 3. Vai trò cảm biến và xử lý

- **Flex sensor:** dùng ba cảm biến, mỗi ngón cái–trỏ–giữa một cảm biến, để theo dõi biến thiên gập–duỗi/tư thế từng ngón. Cần hiệu chuẩn từng cảm biến trên vị trí lắp thật; không mặc định điện trở đầu ra đã là góc giải phẫu chính xác.
- **Velostat:** ghi nhận thay đổi áp lực/tiếp xúc tại vị trí cảm biến. Tín hiệu được dùng theo dạng tương đối để bổ sung bằng chứng về nỗ lực/tương tác ngón; Velostat không trực tiếp “đọc ý định”, không đo góc và không cho phép suy lực tuyệt đối theo Newton.
- **Camera:** nhận diện/vị trí thìa và vùng đích, theo dõi vật qua các pha gắp–di chuyển–đặt và xác định kết quả thị giác. Camera không đo lực ngón và không thay thế thang đo phục hồi chức năng.
- **Bộ xử lý:** Orange Pi 5 Pro dự kiến chạy thị giác máy tính để định vị thìa/vùng đích và theo dõi trạng thái tác vụ; có thể đánh giá mô hình độ sâu đơn ảnh như Depth Anything nếu bài tập cần thông tin độ sâu. Muốn tọa độ metric phải hiệu chuẩn camera và tỷ lệ cảnh. ESP32-S3 dự kiến quét cảm biến và thực hiện state machine/lệnh servo có giới hạn, nhận trạng thái tác vụ từ Orange Pi; đường giao tiếp này cần xác nhận/benchmark. RL không nằm trong phạm vi đã chốt.
- **Phân bổ kênh:** phạm vi ba ngón và mục tiêu một CD74HC4067/16 kênh vẫn giữ. Bản đồ phải phân bổ rõ cả Velostat và Flex; nếu tổng số cảm biến cần đọc vượt 16 thì phải thiết kế lại số kênh/phần cứng, không giả định có sẵn kênh phụ.

## 4. AAN và cơ cấu

1. AAN là mục tiêu điều khiển chính: người dùng chủ động hoặc cố gắng thực hiện, hệ thống chỉ bổ sung trợ lực theo quy tắc đã đặt.
2. Dự kiến kết hợp tín hiệu Flex (chuyển động) và Velostat (áp lực/tiếp xúc tương đối); trạng thái camera cung cấp ngữ cảnh pha tác vụ/kết quả. Bộ điều khiển suy luận trạng thái từ dữ liệu, không xem một cảm biến đơn lẻ là “ý định” hoàn chỉnh.
3. Cơ cấu hiện hành là servo cuốn dây câu cá trực tiếp trên tang cuốn, không dùng lò xo trợ lực/SEA hoặc khớp bốn khâu.
4. Không quy đổi Velostat sang Newton; không dùng `F_assist=max(0,F_target−F_active)` và không khôi phục ngưỡng 5 N đã rút.
5. Tang, dây, neo, hồi/nhả, servo, điều khiển mở ngón, quy tắc ngưỡng, đo lực độc lập và giới hạn vận hành còn cần thiết kế/kiểm chứng. Một servo cuốn dây theo một chiều không tự chứng minh khả năng gập–duỗi hai chiều hay điều khiển ba ngón độc lập.

## 5. Phạm vi phần cứng, chi phí và khối lượng

- Ba ngón mục tiêu: cái, trỏ, giữa.
- 16 kênh analog mục tiêu qua một CD74HC4067. Nếu ba Flex cùng đi qua MUX thì dự kiến dành 3 kênh Flex và tối đa 13 kênh còn lại cho Velostat/ô tham chiếu; bản đồ cuối cùng còn mở, 13 không mặc nhiên là số phần tử Velostat.
- Mục tiêu khối lượng 80–120 g áp dụng cho cụm đeo tay, không gồm bộ xử lý/pin/servo đặt ngoài tay; chưa đo.
- Ước tính vật tư cụm đeo 1,0–1,3 triệu VNĐ; ước tính hệ thống/giàn thử E2E khoảng 5,5 triệu VNĐ khi tận dụng thiết bị lab; đều là ước tính, cần BOM/báo giá. Không dùng giới hạn cũ <1,5 triệu VNĐ cho toàn hệ thống.

## 6. Kiểm chứng và ranh giới kết luận

- Giai đoạn hiện hành: rà soát cơ khí/an toàn, đo cảm biến, thử bàn và phantom; ghi log thô, trạng thái camera, trạng thái chế độ, lệnh servo và kết quả tác vụ.
- Chỉ số kỹ thuật dự kiến: tỷ lệ gắp/đặt thìa thành công, thời gian, số lần rơi/thử lại, đặc trưng chuyển động ngón, trợ lực khi nào/bao nhiêu theo lệnh, độ đúng trạng thái camera và hành vi chuyển chế độ tự động. Chỉ số sẽ được chốt trước khi thử; không trình bày mục tiêu thành kết quả.
- Có thể xem xét thử có cấp nguồn trên người trưởng thành khỏe mạnh sau khi phantom đạt đánh giá an toàn và có đủ phê duyệt cần thiết; đây không phải hoạt động đã được phép hay đã thực hiện. Không thử bệnh nhân trong phạm vi hiện tại.
- Tỷ lệ hoàn thành tác vụ không đồng nghĩa hiệu quả phục hồi sau đột quỵ. Muốn khẳng định phục hồi rõ rệt cần nghiên cứu dọc trên người bệnh, thước đo chuyên môn và phê duyệt phù hợp.
- Không tuyên bố novelty/“đầu tiên”, chẩn đoán, an toàn được chứng nhận, hiệu quả lâm sàng hay đã xác nhận sử dụng tại nhà.

## 7. Hồ sơ và tài liệu điều khiển

- [`CURRENT_DESIGN_BASELINE.md`](../research/context/CURRENT_DESIGN_BASELINE.md)
- [`DECISION_LOG.md`](../research/context/DECISION_LOG.md)
- [`IMPLEMENTATION_PIPELINE.md`](../research/context/IMPLEMENTATION_PIPELINE.md) — pipeline triển khai đề xuất.
- [`research/protocols/09_AAN_spool_phantom_and_conditional_volunteer.md`](../research/protocols/09_AAN_spool_phantom_and_conditional_volunteer.md)
- [`docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md`](DE_CUONG_A_B_C_DRAFT_2026-10-19.md) — bản làm việc, chưa duyệt/nộp.
- Hồ sơ đã nộp và nguồn Drive lịch sử được giữ nguyên; bản DOCX review trước đây chưa đồng bộ với hướng mới.