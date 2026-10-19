# GLOSSARY — thuật ngữ hiện hành

> **Cập nhật:** 2026-10-19 · Dùng [`research/context/CURRENT_DESIGN_BASELINE.md`](../../research/context/CURRENT_DESIGN_BASELINE.md), `DEC-REHAB-001`, [`docs/01_Topic_Definition.md`](../01_Topic_Definition.md) và protocol 09 làm nguồn hiện hành. Các định nghĩa trong đề cương cũ có thể đã superseded.

## Chức năng và chế độ tập

| Thuật ngữ | Cách dùng trong dự án | Giới hạn |
|---|---|---|
| **Hỗ trợ gập–duỗi** | Chế độ dự kiến hỗ trợ vận động ngón khi người tập chưa tự hoàn thành được | Cơ cấu tạo gập, nhả và đưa ngón duỗi trở lại chưa được xác nhận an toàn |
| **AAN (assist-as-needed)** | Trợ lực khi người dùng chủ động/cố gắng vận động nhưng cần hỗ trợ bổ sung | Quy tắc điều khiển và giới hạn vận hành còn phải chốt/kiểm chứng |
| **Chuyển chế độ tự động theo ngưỡng** | Bộ điều khiển tự chuyển từ hỗ trợ gập–duỗi sang AAN khi tiêu chí tín hiệu/vận động đã định trước được thỏa mãn | Không yêu cầu KTV vận hành nút chuyển; đặc trưng, ngưỡng, cửa sổ, hysteresis, fallback còn OPEN và phải khóa trước đánh giá |
| **Bài tập task-level** | Gắp thìa bằng ngón cái–trỏ–giữa, nhấc, di chuyển đến vùng đích rồi thả | Kích thước thìa, cách gắp, vùng đích và protocol cần chuẩn hóa |
| **Phản hồi thị giác** | Camera/hiển thị cho người tập biết vật/đích, tiến trình và kết quả thao tác | Không phải thang đánh giá lâm sàng và không chứng minh phục hồi thần kinh |

## Cảm biến và tín hiệu

| Thuật ngữ | Cách dùng hiện hành | Giới hạn |
|---|---|---|
| **Ba Flex sensor** | Một cảm biến trên từng ngón cái, trỏ, giữa để theo dõi biến thiên gập–duỗi/tư thế | Cần hiệu chuẩn từng cảm biến trên vị trí lắp thật; không mặc định điện trở đầu ra đã là góc giải phẫu chính xác |
| **Velostat** | Vật liệu áp trở chế tạo sensing element để ghi nhận thay đổi áp lực/tiếp xúc tại vị trí lắp | Không tự đọc ý định, không đo góc, không cung cấp lực tuyệt đối theo Newton |
| **EI / tín hiệu nỗ lực tương đối** | Đặc trưng tín hiệu Velostat đã xử lý để mô tả biến thiên tương đối trong cấu hình/phiên đã xác định | Công thức/cửa sổ còn mở; không quy đổi sang N hoặc %MVC khi chưa có phương pháp được kiểm chứng |
| **Đọc vi sai** | Hiệu tín hiệu giữa hai sensing element đối diện nếu cấu hình thực sự có cặp | Có thể giảm thành phần chung; không đồng nghĩa loại bỏ mọi drift |
| **Camera / vision state** | Ước lượng thìa, vùng đích, tiến trình và kết quả nhìn thấy được của tác vụ | Không đo lực ngón, góc khớp chính xác hay tình trạng lâm sàng |
| **Độ sâu metric** | Khoảng cách/vị trí theo đơn vị thực trong không gian đã hiệu chuẩn | Độ sâu tương đối từ một ảnh không tự động là tọa độ metric; cần hiệu chuẩn/chuẩn tỷ lệ phù hợp |
| **16 kênh** | Mục tiêu acquisition qua một CD74HC4067 cho vùng ba ngón | Phải phân bổ cả Flex và Velostat; chưa chốt bản đồ. Nếu vượt 16, sửa acquisition thay vì giả định kênh miễn phí |
| **GAP** | Câu hỏi nghiên cứu về chênh lệch vận động chủ động–thụ động | Chưa là chỉ số sản phẩm; cần phương pháp đo góc độc lập/được kiểm chứng; không lấy góc từ Velostat |
| **RAL** | Chỉ số mức trợ giúp cần thiết, đang được xác định lại theo AAN mới | Định nghĩa cũ dựa lò xo/nấc tải đã superseded; chưa có công thức/đơn vị hiện hành |

## Cơ cấu AAN và bằng chứng

- Cơ cấu dự kiến: servo cuốn dây câu cá trực tiếp trên tang, không lò xo trợ lực/SEA hoặc khớp bốn khâu.
- Mọi Newton/tension phải đến từ phép đo độc lập đã hiệu chuẩn; Velostat/EI không phải force reference. Không dùng `F_assist=max(0,F_target−F_active)` hoặc ngưỡng 5 N đã rút.
- Bench/phantom trước. Thử actuator có cấp nguồn trên người trưởng thành khỏe mạnh chỉ là khả năng có điều kiện sau đánh giá an toàn và phê duyệt cần thiết. Không thử bệnh nhân trong phạm vi hiện tại.
- Task success, thời gian, drops/retries, camera state accuracy và mode-transition behavior là chỉ số kỹ thuật/tác vụ, không phải bằng chứng hiệu quả lâm sàng.

## Cách viết cần tránh

| Tránh | Dùng cách diễn đạt chính xác hơn |
|---|---|
| “Velostat đọc được ý định” | “Velostat đo biến thiên áp lực/tiếp xúc; bộ điều khiển suy luận trạng thái từ mẫu tín hiệu và ngữ cảnh” |
| “Velostat đo chính xác lực/Newton” | “Velostat tạo tín hiệu áp trở tương đối; lực tuyệt đối cần phép đo tham chiếu độc lập” |
| “đã tự động chuyển chế độ đạt ngưỡng X” khi chưa đo | “quy tắc/ngưỡng đang thiết kế; chưa benchmark” |
| “AI xác định độ sâu chính xác” | Chỉ nêu độ sâu/độ chính xác khi có hiệu chuẩn và benchmark trên cấu hình thật |
| “đã phục hồi rõ rệt / tăng neuroplasticity” | “đây là mục tiêu/giả thuyết dài hạn; dự án hiện chỉ kiểm tra chức năng tác vụ” |
| “đã dùng an toàn tại nhà” | Chỉ nêu là intended home context cho tới khi có nghiên cứu phù hợp |
| “tính mới/đầu tiên” | Trình bày vấn đề, thiết kế và kiểm chứng; không kết luận novelty trước khi rà soát |
| “kết quả đạt X” khi mới là kế hoạch | “mục tiêu/tiêu chí cần đạt X” |
