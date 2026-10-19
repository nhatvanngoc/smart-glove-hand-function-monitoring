# 09 — Găng AAN servo–tang cho luyện gắp thìa: khung thử bench/phantom và cổng người có điều kiện

> **Cập nhật:** 2026-10-19 · **Trạng thái:** khung lập kế hoạch, chưa phải protocol được phê duyệt. Hướng chức năng được chủ dự án ghi nhận ở `DEC-REHAB-001`; thiết kế AAN/cơ khí ở `DEC-AAN-002`.
>
> **An toàn:** không gắn/vận hành actuator có cấp nguồn trên người theo tài liệu này. Bất kỳ bước có người nào chỉ có thể được cân nhắc sau khi hoàn tất một protocol riêng và các phê duyệt cần thiết.
>
> **Supersedes:** các bước lò xo, Bowden/4-bar, `F_assist=max(0,F_target−F_active)`, ngưỡng 5 N và quy trình RAL dựa lò xo trong tài liệu cũ không phải chỉ dẫn hiện hành.

## 1. Chức năng hệ thống cần kiểm tra

Mục tiêu dài hạn là găng hỗ trợ người trung niên sau đột quỵ luyện vận động tinh tại nhà; mục tiêu sử dụng tại nhà chưa được xác nhận. Chức năng dự kiến có ba trạng thái theo thứ tự:

1. **Hỗ trợ gập–duỗi:** actuator hỗ trợ chuyển động khi người tập chưa tự hoàn thành được. Cơ cấu hồi/nhả và chuyển động duỗi phải được thiết kế riêng, không suy ra từ khả năng servo cuốn dây.
2. **Chuyển tự động sang AAN:** bộ điều khiển tự chuyển khi các tín hiệu/tiêu chí vận động đã định trước đạt điều kiện ổn định. Không yêu cầu kỹ thuật viên thao tác chuyển mode. Đặc trưng, ngưỡng, số chu kỳ, cửa sổ quan sát, hysteresis, điều kiện hủy và trạng thái fallback còn OPEN.
3. **Bài tập tác vụ:** phối hợp ngón cái, trỏ và giữa để gắp thìa, nhấc, di chuyển tới vùng đích và thả. Camera dự kiến nhận biết thìa, vùng đích và kết quả nhìn thấy được, rồi cung cấp phản hồi trực quan.

## 2. Vai trò tín hiệu và cơ cấu

- Flex sensor: biến thiên gập–duỗi/tư thế; phải hiệu chuẩn so với phương pháp tham chiếu phù hợp.
- Velostat: biến thiên áp lực/tiếp xúc tại vị trí lắp; dùng tương đối làm tín hiệu hỗ trợ suy luận về nỗ lực/tương tác. Velostat không trực tiếp nhận biết ý định, không đo góc, không tạo phép đo Newton và không thay thiết bị đo lực độc lập.
- Camera: vật/vùng đích và kết quả task-level; không đo lực hoặc hiệu quả lâm sàng.
- Tổ hợp/chuỗi điều khiển: cảm biến cung cấp dấu hiệu chuyển động/tiếp xúc; bộ điều khiển suy ra trạng thái; camera đưa ngữ cảnh tác vụ; lệnh servo có giới hạn và fallback. Camera không được phát lệnh kéo không giới hạn.
- Mục tiêu hiện tại là ba ngón và 16 kênh qua một CD74HC4067. Owner xác nhận 3 Flex sensor, mỗi ngón một chiếc; nếu cùng MUX thì dành 3 kênh, còn tối đa 13 kênh cho Velostat/ô tham chiếu. Bản đồ cuối, số Velostat elements, tốc độ quét, đồng bộ và độ trễ vẫn mở. Nếu vượt 16 kênh, sửa kiến trúc acquisition trước khi thử.
- Servo cuốn dây câu cá trực tiếp lên tang; không lò xo/SEA, không khớp 4 khâu. Tang, dây, neo, hồi/nhả, điều khiển ngón, mức độc lập ba ngón và giới hạn vận hành còn chưa chốt.

## 3. Stage 0 — thiết kế/đánh giá trước khi cấp nguồn

Trước khi energize actuator, lập và rà soát:

1. Bản vẽ tang, đường dây, điểm neo và toàn bộ hành trình cơ khí trên fixture.
2. Cách hồi/nhả và duỗi ngón; chứng minh hành vi khi mất điện, lỗi tín hiệu và dừng khẩn. Không dựa duy nhất vào phần mềm để nhả dây.
3. Servo, nguồn, hành vi khởi động, giới hạn hành trình và phân tích nguy cơ: cuốn/rối dây, kẹp/cắt, quá hành trình, tự kích hoạt, mất nguồn/điều khiển, không nhả được.
4. Thiết bị tham chiếu độc lập và quy trình hiệu chuẩn/kiểm tra lực căng dây trên bench. Velostat/EI không được dùng làm force reference.
5. Bản đồ kênh, hiệu chuẩn Flex, kiểm tra vị trí Velostat để phân biệt tín hiệu ngón–vật với áp lực ngón–nẹp.
6. Logic trạng thái và điều kiện dừng/fallback trước khi thử; các ngưỡng số chỉ được điền sau khi có căn cứ đo và rà soát có trách nhiệm. Không tự dùng lại 5 N.
7. Protocol bench, schema dữ liệu, operator, cấu hình, timestamps, chỉ tiêu đạt/dừng đã định trước.

Không bắt đầu thử actuator có lực cho tới khi hồ sơ đánh giá xác nhận fixture sẵn sàng và người giám sát có thẩm quyền chấp thuận bước đó.

## 4. Stage 1 — kiểm tra cảm biến, logic và cơ cấu trên bàn/phantom

### 4.1. Đặc trưng tín hiệu

- Ghi dữ liệu Flex và Velostat thô trong các thao tác không tải/lắp nẹp/tiếp xúc thìa trên fixture.
- Kiểm tra liệu Velostat ở vị trí dự kiến phản ánh tương tác ngón–vật hay phần lớn là lực ép vào nẹp; kiểm tra tính lặp lại, drift và thay đổi theo cách lắp.
- So sánh Flex với phương pháp tham chiếu góc/chuyển động phù hợp; báo sai số theo giao thức thực, không gán ADC thành độ nếu chưa có hiệu chuẩn.
- Kiểm tra kênh MUX, cross-talk, settling, tần số khung và dấu thời gian trên toàn bộ kênh đã phân bổ.

### 4.2. Thiết lập và kiểm tra quy tắc chuyển mode tự động

Quy tắc tự động là một phần chức năng của thiết kế, nhưng **chưa có ngưỡng số được chốt**. Trước khi đánh giá:

1. Chọn đặc trưng từ Flex (ví dụ biên độ/độ lặp lại của chu kỳ vận động) và Velostat (biến thiên áp lực/tiếp xúc) dựa trên dữ liệu hiệu chuẩn.
2. Xác định trước ngưỡng, cửa sổ quan sát, số chu kỳ cần đạt, hysteresis, điều kiện tín hiệu mất/không hợp lệ, quy tắc quay về trạng thái hỗ trợ/fallback. Không thêm vai trò KTV làm thao tác chuyển chế độ.
3. Tách dữ liệu dùng để thiết lập ngưỡng khỏi lượt đánh giá; khóa cấu hình và ghi version.
4. Kiểm tra false transition, missed transition, độ trễ chuyển mode, lệnh servo phát sinh và hành vi stop/release trên bench/phantom.

Không chọn threshold hậu nghiệm để làm đẹp kết quả. Threshold trạng thái vận động không phải ngưỡng an toàn lực; giới hạn lực vẫn cần phép đo độc lập và rà soát riêng.

### 4.3. Camera và bài tập thìa

- Bắt đầu bằng camera cố định, ánh sáng/nền và vùng thao tác được kiểm soát, một thìa và vùng đích đã đánh dấu.
- Định nghĩa nhãn/task outcome rõ: thìa được tiếp cận, nhấc, di chuyển, đặt trong vùng đích, rơi/đặt sai, hoặc trạng thái không xác định.
- Đánh giá detection/tracking/placement classification, che khuất, nhầm lẫn và độ trễ end-to-end trên Orange Pi 5 Pro theo đúng phiên bản mô hình.
- Tọa độ độ sâu đơn ảnh không mặc định là tọa độ metric; cần hiệu chuẩn/chuẩn tỷ lệ nếu dùng tọa độ thực. Không cần buộc có depth nếu task 2D với camera cố định đủ đáp ứng.
- Kiểm tra phản hồi thị giác có khớp với nhãn kết quả; đây là phản hồi tác vụ, không phải clinical assessment.

### 4.4. Thử tích hợp bench/phantom

- Dùng phantom/fixture được cố định; giữ người không nằm trong đường truyền actuator.
- Thử chu trình hỗ trợ gập–duỗi → tự động chuyển AAN theo rule đã khóa → gắp/di chuyển/đặt thìa.
- Ghi raw sensor, feature/threshold state, mode, vision state/confidence, servo command, reference force/tension, task outcome, timestamps, configuration, video tương ứng và sự kiện bất thường.
- Kiểm tra task success, thời gian, drops/retries, đúng/sai mode transition, sai pha trợ lực, lỗi vision, stop/release và độ lặp lại. Chỉ số/tiêu chí phải chốt trước khi xem kết quả.
- So sánh fixed-assistance baseline với AAN tự động nếu hai điều kiện có thể thực hiện an toàn và công bằng; không biến so sánh thuật toán nhỏ thành claim novelty.

### Stage 1 exit gate

Lập báo cáo kết quả và yêu cầu rà soát an toàn riêng. Không mở cổng có người nếu còn nguy cơ chưa xử lý, thiếu đo lực độc lập, lỗi hồi/nhả, threshold chưa khóa/không hoạt động đúng, hoặc không có log truy vết. Thành công trên phantom không tự động cấp phép cho thử nghiệm người.

## 5. Stage 2 — chỉ cân nhắc thử trên người trưởng thành khỏe mạnh có điều kiện

Giai đoạn này **không được cấp phép bởi tài liệu này**. Chỉ có thể xem xét sau khi:

- Stage 1 và đánh giá an toàn độc lập hoàn tất, kết quả chấp nhận được.
- Có xác định bằng văn bản của các cơ quan/trường/đơn vị có thẩm quyền về mọi phê duyệt cần thiết.
- Protocol riêng được rà soát/phê duyệt, gồm tuyển chọn, đồng thuận, giám sát, stop rules, phản ứng sự cố, riêng tư và kiểm tra thiết bị.
- Cấu hình actuator, vận hành, threshold và giới hạn đã được cố định trong protocol được duyệt.

Cho tới khi đủ điều kiện: không tuyển, không đeo thử có lực, không cấp nguồn actuator trên bất cứ người nào. Nếu sau này được duyệt, chỉ thực hiện đúng nhóm và quy trình đã được duyệt. Người khỏe mạnh không thay thế dữ liệu người sau đột quỵ.

## 6. Kết quả và tuyên bố bị loại trừ

- Không thử bệnh nhân trong phạm vi hiện tại; không tuyên bố hiệu quả điều trị, cải thiện thần kinh, phục hồi chức năng rõ rệt hoặc hiệu quả sử dụng tại nhà.
- Không gọi thiết bị “an toàn” chỉ từ kết quả phantom/kiểm tra học sinh; không tuyên bố chứng nhận an toàn.
- Không báo Newton từ Velostat/EI. Tension/force báo cáo phải đến từ phương pháp tham chiếu độc lập có traceability.
- Không claim novelty/“đầu tiên”; rà prior art cần bao gồm đúng vai trò và bố trí Velostat, Flex, AAN, camera/task vision và tác vụ gắp.
- Mọi target là target cho đến khi có raw data/log và cấu hình truy vết.

## 7. Các mục còn mở trước protocol thực thi

| Hạng mục | Trạng thái |
|---|---|
| Hình học tang, mounting | OPEN |
| Loại dây, route, neo, hồi/nhả và duỗi ngón | OPEN |
| Servo, nguồn và control mapping | OPEN |
| Mức điều khiển độc lập ngón cái/trỏ/giữa | OPEN |
| Kênh Flex/Velostat trong giới hạn 16 và scan timing | OPEN |
| Vị trí Velostat đo tương tác nào; đối chứng ngón–nẹp | OPEN |
| Hiệu chuẩn Flex và camera/world coordinates | OPEN |
| Logic chuyển mode tự động; đặc trưng, threshold, window, hysteresis, fallback | OPEN — chưa điền số |
| Camera/model, task labeling, occlusion, latency | OPEN |
| Force/tension reference + calibration | OPEN |
| Stop/release behavior và bench hazard review | OPEN |
| Acceptance/stop criteria của phantom task | OPEN — chốt trước thử |
| Participant determination/approval | OPEN; không tuyển hay actuator test |
