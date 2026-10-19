# Nghiên cứu và phát triển găng tay hỗ trợ phục hồi chức năng sau đột quỵ cho vận động tinh

> **Trạng thái hiện hành — 2026-10-19.** Hướng chức năng mới được chủ dự án xác định và ghi tại [`research/context/CURRENT_DESIGN_BASELINE.md`](research/context/CURRENT_DESIGN_BASELINE.md), `DEC-REHAB-001`. Tên trên là tên làm việc, chưa chốt tên nộp cuối. Không sửa hồi tố hồ sơ đã nộp.

## Định hướng chức năng

Dự án hướng tới găng tay hỗ trợ người trung niên sau đột quỵ luyện vận động tinh tại nhà. Chức năng dự kiến phát triển theo lộ trình cụ thể: (1) máy hỗ trợ gập–duỗi ngón khi người tập chưa tự làm được; (2) hệ thống tự động chuyển sang AAN khi tín hiệu vận động đạt quy tắc ngưỡng đã định trước; (3) tập phối hợp ngón cái, trỏ và giữa để gắp thìa, nhấc, di chuyển tới vùng đích và thả. Chuyển chế độ không phụ thuộc KTV thao tác; đặc trưng/ngưỡng và trạng thái an toàn khi tín hiệu không tin cậy còn phải thiết kế, hiệu chuẩn và kiểm chứng.

Camera được định hướng để thấy thìa và vùng đích, theo dõi tiến trình/kết quả thao tác, rồi đưa phản hồi trực quan tức thời cho người tập. Orange Pi 5 Pro là nền tảng dự kiến cho thị giác máy tính; có thể đánh giá Depth Anything nếu cần ước lượng độ sâu, nhưng tọa độ metric cần hiệu chuẩn camera/tỷ lệ cảnh. Tốc độ khung, độ trễ và độ tin cậy của pipeline chưa được benchmark. Camera không đo lực hay đánh giá phục hồi lâm sàng. Đây là kế hoạch cho một chức năng tại nhà, chưa phải bằng chứng găng đã dùng tại nhà.

## Vai trò cảm biến và cơ cấu

- **Ba Flex sensor:** mỗi ngón cái–trỏ–giữa một cảm biến theo dõi biến thiên gập–duỗi/tư thế; cần hiệu chuẩn riêng, không mặc định là góc giải phẫu chính xác.
- **Velostat:** ghi nhận biến thiên áp lực/tiếp xúc ở vị trí lắp; là tín hiệu tương đối hỗ trợ suy luận về nỗ lực/tương tác, không tự nhận biết ý định, không đo góc và không cung cấp Newton.
- **AAN:** kết hợp tín hiệu ngón với pha tác vụ phù hợp để bổ sung trợ lực khi người dùng cố gắng nhưng động tác chưa đủ. Luật cụ thể và ngưỡng chưa chốt, phải cố định trước khi đánh giá.
- **Cơ cấu:** servo cuốn dây câu cá trực tiếp trên tang; không lò xo/SEA và không khớp 4 khâu. Hồi/nhả dây, khả năng duỗi, an toàn và mức điều khiển độc lập ba ngón còn là việc thiết kế/kiểm chứng.
- Mục tiêu ba ngón cái–trỏ–giữa và 16 kênh qua một CD74HC4067 được giữ. Chủ dự án xác nhận 3 Flex sensor (mỗi ngón 1); nếu cùng MUX thì dành 3 kênh và còn tối đa 13 cho Velostat/ô tham chiếu. Bản đồ và số phần tử Velostat chưa chốt.

## Ranh giới phần cứng và báo cáo

Khối lượng mục tiêu 80–120 g chỉ cho cụm đeo tay, chưa cân. Ước tính vật tư cụm đeo 1,0–1,3 triệu VNĐ và hệ thống/giàn thử khoảng 5,5 triệu VNĐ khi tận dụng thiết bị lab là dự toán, chưa kiểm toán. Không dùng giới hạn cũ <1,5 triệu VNĐ cho toàn hệ thống hoặc <150 g.

Không suy ra Newton từ Velostat; không dùng luật `F_assist=max(0,F_target−F_active)` hay ngưỡng 5 N đã rút. Mọi giới hạn lực phải dùng phép đo độc lập và đánh giá phù hợp.

## Thử nghiệm và giới hạn tuyên bố

1. Kiểm tra cảm biến, cơ cấu, quy tắc ngưỡng và camera trên bàn/phantom trước; lưu log có thể truy vết.
2. Chỉ có thể xem xét thử có cấp nguồn trên người trưởng thành khỏe mạnh sau khi đánh giá an toàn đạt và có mọi phê duyệt cần thiết. Đây là kế hoạch có điều kiện, không phải cho phép hay kết quả.
3. Không thử bệnh nhân trong phạm vi hiện tại. Không khẳng định hiệu quả lâm sàng, cải thiện phục hồi thần kinh, an toàn được chứng nhận, novelty/“đầu tiên” hoặc sử dụng tại nhà đã được xác nhận.
4. Tỷ lệ gắp/đặt thìa, thời gian, số lần rơi/thử lại và hành vi trợ lực là chỉ số kỹ thuật/tác vụ; không thay thế đánh giá phục hồi chuyên môn. Mọi ngưỡng số là mục tiêu cho tới khi có log thực.

## Tài liệu điều khiển

- [`research/context/CURRENT_DESIGN_BASELINE.md`](research/context/CURRENT_DESIGN_BASELINE.md) — hướng hiện hành và giới hạn tuyên bố.
- [`research/context/IMPLEMENTATION_PIPELINE.md`](research/context/IMPLEMENTATION_PIPELINE.md) — pipeline triển khai đề xuất theo các cổng từ task/spec đến thử nghiệm bench/phantom.
- [`research/context/DECISION_LOG.md`](research/context/DECISION_LOG.md) — quyết định mới và lịch sử.
- [`docs/01_Topic_Definition.md`](docs/01_Topic_Definition.md) — định nghĩa đề tài và chức năng.
- [`docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md`](docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md) — bản đề cương làm việc, chưa duyệt/nộp.
- [`research/protocols/09_AAN_spool_phantom_and_conditional_volunteer.md`](research/protocols/09_AAN_spool_phantom_and_conditional_volunteer.md) — khung thử bench/phantom và cổng người có điều kiện.
- [`research/reviews/2026-10-19_repo_scope_sync.md`](research/reviews/2026-10-19_repo_scope_sync.md) — lịch sử đồng bộ và cập nhật hướng mới.

Hồ sơ đã nộp, PDF/DOCX nguồn và các tài liệu lịch sử được giữ nguyên. Bản DOCX review riêng trên Drive dựa trên draft cũ, chưa đồng bộ với hướng hiện hành; không xem đó là bản cuối.