# DỰ THẢO ĐỀ CƯƠNG KHKT — định hướng A/B/C

> **Cập nhật:** 2026-10-19 (lần 1) sau chỉ đạo chủ dự án `DEC-REHAB-001`; **2026-10-19 (lần 2)** bổ sung phần đăng ký trước chỉ số/ngưỡng, liên kết artifact Gate 0 và lộ trình triển khai công cụ. **2026-10-20 (lần 3)** ghi nhận ba quyết định của chủ dự án — **PA-2** cho bản đồ kênh (`DEC-CHMAP-001`), **M3** cho phương pháp phân biệt vận động tự nguyện vs do máy tạo (`DEC-TASK-002`), **ba tang cuốn riêng + servo nhả dây chủ động** (`DEC-MECH-007`) — và việc dựng lại DOCX review. **Trạng thái:** bản làm việc để rà soát, chưa duyệt và chưa phải bản nộp. Tên dưới đây là tên làm việc; chưa chốt tên cuối. Bản DOCX review đang nằm trên Drive (`11A2_CAP_NHAT_DU_THAO_2026-10-19.docx`) dựa trên draft cũ, **không đại diện cho hướng này** và không bị ghi đè. Ngày 2026-10-20, theo chỉ đạo của chủ dự án, DOCX đã được dựng lại từ chính bản Markdown này: [`exports/11A2_CAP_NHAT_DU_THAO_2026-10-20.docx`](../exports/11A2_CAP_NHAT_DU_THAO_2026-10-20.docx) bằng script [`scripts/build_abc_review_docx.py`](../scripts/build_abc_review_docx.py). **DOCX đó là bản để rà soát, KHÔNG phải bản đã duyệt toàn văn và KHÔNG phải bản nộp.**
> **Quyết định liên quan:** `DEC-REHAB-001`, `DEC-SENSE-001`, `DEC-SCOPE-007`, `DEC-AAN-002`, `DEC-METRIC-003`, `DEC-DEF-002`, `DEC-PROP-004`, `DEC-SCOPE-008`, `DEC-COST-002`, `DEC-MASS-001`; **mới duyệt 2026-10-20:** `DEC-CHMAP-001` (PA-2), `DEC-TASK-002` (M3), `DEC-MECH-007` (ba tang + nhả dây chủ động).
> **Hồ sơ kỹ thuật đi kèm (bản đề xuất, chưa duyệt):** [`research/protocols/10_gate0_task_state_sheet.md`](../research/protocols/10_gate0_task_state_sheet.md) (tờ yêu cầu tác vụ + bảng trạng thái), [`10a_gate0_channel_map_and_acquisition_budget.md`](../research/protocols/10a_gate0_channel_map_and_acquisition_budget.md) + [`10b_channel_map_proposed.csv`](../research/protocols/10b_channel_map_proposed.csv) (bản đồ 16 kênh), [`docs/07_Vision_TaskState_Architecture.md`](07_Vision_TaskState_Architecture.md) (nhánh camera), [`docs/08_Software_Firmware_Roadmap.md`](08_Software_Firmware_Roadmap.md) (lộ trình phần mềm/firmware).
> **Quy tắc bằng chứng:** chức năng dưới đây là mục tiêu thiết kế, không phải kết quả đã chế tạo/đạt. Không tuyên bố đã dùng an toàn tại nhà, thử trên bệnh nhân, cải thiện phục hồi lâm sàng, novelty/“đầu tiên” hoặc hiệu quả thần kinh. Mọi ô số trong các hồ sơ đi kèm đang để trống có chủ đích (`OPEN`); điền số phải kèm căn cứ đo hoặc quyết định có ngày.

**Tên làm việc:** *Nghiên cứu và phát triển găng tay hỗ trợ phục hồi chức năng sau đột quỵ cho vận động tinh.*

## A. Lý do chọn đề tài và vấn đề cần giải quyết

Sau đột quỵ, khả năng chủ động gập–duỗi và phối hợp các ngón tay có thể bị hạn chế, gây khó khăn khi thao tác với đồ vật nhỏ hoặc dụng cụ sinh hoạt. Đề tài hướng tới người trung niên sau đột quỵ và bối cảnh luyện tập tại nhà; đây là nhóm người dùng/bối cảnh mà dự án muốn phục vụ, chưa phải kết luận dịch tễ hoặc xác nhận thiết bị đã phù hợp để dùng tại nhà.

Vấn đề kỹ thuật được chọn là làm thế nào để một găng tay hỗ trợ người tập đi từ vận động ngón cơ bản tới một thao tác vận động tinh có mục đích, thay vì chỉ đo tín hiệu hoặc lặp một chu kỳ đóng/mở. Chức năng mục tiêu là **hỗ trợ người tập gắp một chiếc thìa bằng ngón cái, trỏ và giữa, nhấc thìa, di chuyển đến một vùng đích rồi thả**. Bài tập này làm rõ đầu vào cảm biến, hành động cơ cấu, trạng thái tác vụ và kết quả có thể quan sát.

Hướng thiết kế gồm ba bước: máy hỗ trợ gập–duỗi khi người tập chưa thể tự hoàn thành chuyển động; bộ điều khiển tự động chuyển sang assist-as-needed (AAN) khi tín hiệu vận động đạt quy tắc ngưỡng đã thiết lập trước; sau đó hệ thống hỗ trợ bài tập gắp–di chuyển–đặt vật bằng ba ngón. Hệ thống không yêu cầu kỹ thuật viên trực tiếp chuyển chế độ khi vận hành. Tác dụng phục hồi dài hạn là mục tiêu của hướng nghiên cứu, không phải kết quả đã chứng minh.

## B. Mục tiêu và giải pháp thiết kế

### B.1. Mục tiêu chức năng

Phát triển và kiểm tra trên bàn thử/phantom một nguyên mẫu găng tay ba ngón có khả năng:

1. Hỗ trợ chuyển động gập–duỗi ngón trong chế độ vận động có trợ giúp.
2. Tự động chuyển sang AAN theo một quy tắc ngưỡng được xác định và khóa trước khi đánh giá.
3. Hỗ trợ người tập phối hợp ngón cái, trỏ và giữa để gắp, nhấc, di chuyển và đặt một chiếc thìa vào vùng đích.
4. Dùng camera để theo dõi thìa/vùng đích và trạng thái hoàn thành có thể quan sát; cung cấp phản hồi trực quan ngay cho người tập.
5. Ghi lại kết quả tác vụ và sự kiện trợ lực để đánh giá kỹ thuật hệ thống, không chẩn đoán hoặc thay thế thang đo lâm sàng.

### B.2. Vai trò của cảm biến và xử lý

- **Ba Flex sensor:** mỗi ngón cái, trỏ, giữa có một cảm biến để theo dõi biến thiên gập–duỗi/tư thế từng ngón. Mỗi cảm biến cần hiệu chuẩn trên vị trí lắp thật; đầu ra không mặc định là góc giải phẫu chính xác.
- **Velostat:** sensing element bố trí tại vùng được thiết kế để ghi nhận biến thiên áp lực/tiếp xúc trên mặt lòng hoặc mu ngón. Tín hiệu tương đối này bổ sung thông tin về nỗ lực/tương tác cơ học. Velostat không tự nhận biết ý định, không đo góc và không được quy đổi sang Newton.
- **Camera:** nhận biết/vị trí thìa và vùng đích, theo dõi trạng thái nhìn thấy được trong chu trình gắp–nhấc–di chuyển–đặt, rồi trả kết quả và phản hồi trực quan. Camera không đo lực ngón và không xác nhận phục hồi lâm sàng.
- **Orange Pi 5 Pro:** nền tảng dự kiến để chạy thị giác máy tính, định vị thìa/vùng đích và theo dõi trạng thái tác vụ; có thể đánh giá mô hình độ sâu đơn ảnh như Depth Anything nếu tác vụ cần. Tọa độ metric cần hiệu chuẩn camera/tỷ lệ cảnh. ESP32-S3 dự kiến quét tín hiệu, chạy state machine ngưỡng và phát lệnh servo có giới hạn sau khi nhận trạng thái tác vụ từ Orange Pi; giao tiếp này còn phải tích hợp/benchmark. Mô hình, tốc độ khung, độ trễ và độ tin cậy chưa có kết quả đo. Không đưa RL vào phạm vi hiện hành.
- **Phân bổ kênh:** chủ dự án xác nhận ba Flex sensor — một cho mỗi ngón cái, trỏ, giữa (`DEC-SENSE-001`). Mục tiêu điện tử là 16 kênh qua một CD74HC4067; nếu cả ba Flex dùng chung MUX thì dành 3 kênh và còn tối đa 13 kênh cho Velostat/ô tham chiếu — đây là trần số học, không phải số phần tử Velostat đã chốt. Bốn phương án phân bổ (tối thiểu 7 kênh; vi sai lòng/mu 11 kênh; Flex đọc thẳng vào ngõ vào còn trống của ADC ngoài; Flex vào ADC nội của vi điều khiển) đã được lập bảng kèm đánh đổi tại [`10a`](../research/protocols/10a_gate0_channel_map_and_acquisition_budget.md) §2–§3; bản đồ kênh đề xuất ở [`10b`](../research/protocols/10b_channel_map_proposed.csv). Nếu cấu hình cần nhiều hơn 16 kênh phải sửa kiến trúc thu thập trước khi chế tạo găng. **Đã duyệt 2026-10-20 (`DEC-CHMAP-001`): phương án PA-2** — 3 Flex qua MUX + 6 Velostat (cặp lòng/mu cho cái–trỏ–giữa) + 2 ô tham chiếu = **11 kênh quét**, 5 kênh dự phòng. Vị trí lắp từng phần tử, dải điện trở Flex thật, điện trở phân áp và tốc độ khung thật **vẫn `OPEN`**; nếu Gate 1 cho thấy phần tử mặt mu không bổ sung thông tin, phải quay lại duyệt bản đồ kênh thay vì diễn giải ép nẹp thành tiếp xúc vật.

### B.3. Nguyên lý trợ lực và quy tắc tự động chuyển chế độ

Cơ cấu AAN dự kiến dùng servo cuốn dây câu cá trực tiếp trên tang cuốn; không dùng lò xo trợ lực/SEA hoặc khớp bốn khâu. Trong chế độ AAN, vận động ngón do người dùng khởi xướng; bộ điều khiển bổ sung trợ lực theo tín hiệu vận động và trạng thái tác vụ, thay vì đóng ngón hoàn toàn theo lệnh camera.

Chuyển từ chế độ hỗ trợ gập–duỗi sang AAN là **tự động**, không phụ thuộc KTV nhấn nút. Quy tắc dự kiến dựa trên tiêu chí vận động lặp lại/ổn định lấy từ Flex sensor, có thể dùng Velostat làm tín hiệu bổ sung về nỗ lực/tiếp xúc. Các đặc trưng, ngưỡng, số chu kỳ, cửa sổ quan sát, hysteresis và xử lý tín hiệu lỗi hiện còn mở. Nhóm phải xác định căn cứ, hiệu chuẩn, thử trên bàn/phantom và khóa quy tắc trước khi so sánh kết quả; không chọn ngưỡng sau khi đã xem dữ liệu đánh giá.

Hai điểm kỹ thuật của quy tắc tự động đã được nêu thành hồ sơ riêng, vẫn ở mức đề xuất: (1) máy trạng thái chế độ vận hành với các trạng thái an toàn/không hợp lệ/lỗi và điều kiện rời trạng thái ([`protocols/10`](../research/protocols/10_gate0_task_state_sheet.md) §4); (2) năm phương pháp ứng viên để **phân biệt vận động do người tập khởi xướng với chuyển động do chính cơ cấu tạo ra** — nếu không giải quyết điểm này, hệ thống có thể tự thăng cấp cho người tập không có vận động chủ động ([`protocols/10`](../research/protocols/10_gate0_task_state_sheet.md) §5). Cả hai phải chọn và kiểm chứng trên bench/phantom trước khi đặt bất kỳ giá trị ngưỡng nào. **Cập nhật 2026-10-20:** chủ dự án đã **chọn M3** — cửa sổ "thăm dò tự nguyện", tạm ngưng trợ lực một khoảng ngắn rồi đo đáp ứng của người tập (`DEC-TASK-002`). Đây là **chọn phương pháp làm việc, không phải quy tắc đã kiểm chứng**: độ dài cửa sổ, tần suất mở, tiêu chí nhận diện đáp ứng, hành vi khi không thấy đáp ứng và số lần lặp vẫn `OPEN`; bắt buộc rà an toàn trước bất kỳ lần chạy có cấp nguồn nào; và M3 **không phát hiện nỗ lực không tạo ra chuyển động** (có thể cần M1/M4 làm lớp đối chiếu — chưa duyệt). Máy trạng thái chế độ và bộ nhãn trạng thái tác vụ (`DEC-TASK-001`) **vẫn chưa được duyệt**.

Cơ cấu servo cuốn dây trực tiếp trên tang là hướng thiết kế, chưa phải hệ đã chế tạo hoặc xác nhận an toàn. Kích thước tang, loại và đường đi dây, neo, hồi/nhả, khả năng duỗi, điều khiển ba ngón, lệnh servo, phép đo lực độc lập và giới hạn vận hành vẫn cần hoàn thiện. **Đã duyệt 2026-10-20 (`DEC-MECH-007`): ba tang cuốn riêng (mỗi ngón một tang) và duỗi bằng cách servo nhả dây chủ động**, không thêm lò xo hồi vị. Còn mở: một động cơ kéo ba tang trên cùng trục hay ba động cơ riêng; đường kính tang, hành trình và giới hạn an toàn; **hành vi nhả khi mất nguồn** (câu hỏi cơ khí, không xử lý bằng phần mềm được); và tham chiếu lực/căng dây độc lập. Không dùng Velostat làm phép đo lực an toàn; không áp dụng `F_assist=max(0,F_target−F_active)` hoặc tiêu chí 5 N đã rút.

### B.4. Khối lượng và chi phí

Mục tiêu khối lượng 80–120 g chỉ tính cụm nẹp/cảm biến đeo trên tay; bộ xử lý, pin và servo đặt ngoài tay. Đây là mục tiêu chưa cân. Vật tư cụm đeo ước tính 1,0–1,3 triệu VNĐ; hệ thống/giàn thử E2E ước tính khoảng 5,5 triệu VNĐ khi tận dụng thiết bị phòng thí nghiệm. Đây là dự toán, không phải kiểm toán; cần BOM có ngày, báo giá và khai báo thiết bị dùng chung. **Lưu ý 2026-10-20:** cả hai con số được lập **trước** khi chốt phương án ba tang (`DEC-MECH-007`) nên chưa phản ánh khối lượng, lượng dây và số động cơ tăng thêm; phải cân cụm đeo thật và lập lại BOM trước khi trích dẫn. Không dùng tiêu chí cũ “toàn hệ thống <1,5 triệu VNĐ”.

## C. Phương pháp, kế hoạch thử nghiệm và sản phẩm dự kiến

### C.1. Trình tự thực hiện

1. **Chốt tác vụ và tín hiệu:** xác định loại thìa, vùng đích, cách xác nhận đặt thành công, bản đồ kênh Flex/Velostat, vị trí camera và quy trình hiệu chuẩn. Tách rõ tín hiệu người dùng, tín hiệu cơ cấu và nhãn kết quả tác vụ.
2. **Kiểm tra cảm biến:** đo Flex sensor so với phương pháp tham chiếu phù hợp; thử Velostat ở các vị trí dự kiến để kiểm tra nó phản ánh tương tác ngón–vật hay chủ yếu là ngón–nẹp. Ghi lặp lại, trôi và ảnh hưởng khi lắp/đeo; không suy ra Newton từ tín hiệu.
3. **Kiểm tra cơ cấu trên bench/phantom:** hoàn thiện đường dây, hồi/nhả, chuyển động gập/duỗi, hành vi dừng và phương pháp đo lực độc lập. Kiểm tra không tải trước; mọi giới hạn an toàn phải được xác lập bằng quy trình đo và rà soát phù hợp, không tự điền con số.
4. **Xây dựng và thử quy tắc chuyển chế độ:** xác định trước các đặc trưng tín hiệu, cửa sổ, ngưỡng, hysteresis, trạng thái không tin cậy và cách trở về trạng thái an toàn. Dùng dữ liệu hiệu chuẩn riêng để thiết lập; dùng lượt thử độc lập để đánh giá, tránh chọn ngưỡng theo chính dữ liệu báo cáo kết quả.
5. **Xây dựng nhánh thị giác:** nhận biết thìa và vùng đích trong bố trí cố định; xác nhận các sự kiện nhìn thấy được như nhấc vật, di chuyển và đặt vào vùng đích. Đo độ đúng, trường hợp che khuất và độ trễ trên đúng phần cứng. Nếu dùng độ sâu đơn ảnh, cần hiệu chuẩn tỷ lệ/không gian trước khi gọi tọa độ là tọa độ thực.
6. **Tích hợp bài tập và đánh giá kỹ thuật:** chạy chu trình hỗ trợ cơ bản → chuyển AAN tự động → gắp/di chuyển/đặt thìa trên bàn thử/phantom. Lưu tín hiệu thô, trạng thái chế độ, trạng thái thị giác, lệnh servo, kết quả tác vụ, cấu hình và dấu thời gian.
7. **Cổng người tham gia:** chỉ sau thử nghiệm phantom, đánh giá an toàn đạt và đủ phê duyệt mới xem xét thử cấp nguồn trên tình nguyện viên khỏe mạnh theo protocol riêng. Không thử trên bệnh nhân trong phạm vi hiện tại.

### C.2. So sánh và chỉ số dự kiến

Các chỉ số cần được xác định và đăng ký trước khi thử, gồm:

- tỷ lệ hoàn thành đúng tác vụ đặt thìa vào vùng đích;
- thời gian hoàn thành, số lần rơi/thử lại;
- mức và thời điểm chuyển động gập–duỗi, độ lặp lại của chu trình;
- số lần chuyển chế độ đúng/sai và phản ứng khi tín hiệu không tin cậy;
- độ đúng của camera khi phát hiện thìa, vùng đích và kết quả đặt;
- số sự kiện trợ lực không đúng pha, cùng phép đo độc lập cho kiểm tra cơ cấu.

So sánh tối thiểu nên bao gồm một baseline trợ lực cố định và chế độ AAN tự động, nếu hai cấu hình có thể được thử an toàn và điều kiện thử được giữ tương đương. Có thể dùng các lượt tắt từng nguồn cảm biến để xác định đóng góp của Flex, Velostat và camera, nhưng mục tiêu chính vẫn là chức năng hoàn thành bài tập, không phải so sánh thuật toán cho riêng nó. Không coi camera feedback đơn thuần là bằng chứng cải thiện phục hồi.

Mọi số trong C.1/C.2 là mục tiêu/tiêu chí cần đạt cho tới khi có log và artifact truy vết; không trình bày kế hoạch thành kết quả. Chỉ tiêu về phục hồi thần kinh, cải thiện chức năng sau đột quỵ hoặc hiệu quả tại nhà cần nghiên cứu lâm sàng/dọc riêng.

### C.3. Sản phẩm dự kiến và giới hạn

Sản phẩm dự kiến: nguyên mẫu găng ba ngón; cơ cấu servo–dây–tang có quy tắc AAN tự động; nhánh camera nhận biết thìa/vùng đích và kết quả tác vụ; giao diện phản hồi trực quan; bộ log thử bench/phantom có thể truy vết; và báo cáo so sánh chức năng với giới hạn được nêu rõ. Đây là sản phẩm/kế hoạch dự kiến, không phải bằng chứng các chức năng đã hoàn thành.

- Thử bàn/phantom không chứng minh hiệu quả trên người, an toàn được chứng nhận hoặc cải thiện sau đột quỵ.
- Kế hoạch người khỏe mạnh chỉ có điều kiện sau đánh giá an toàn/phê duyệt; không đồng nhất dữ liệu người khỏe với dữ liệu bệnh nhân.
- Không tuyên bố găng đã sử dụng tại nhà, đã cải thiện chức năng lâm sàng, đã thúc đẩy tái tổ chức thần kinh hoặc vượt trội hơn phục hồi thông thường.
- Không tuyên bố tính mới/“đầu tiên”; cần rà prior art đúng tổ hợp AAN, Velostat, Flex, camera và bài tập gắp trước khi đưa ra bất kỳ kết luận novelty nào.

### C.4. Đăng ký trước chỉ số, ngưỡng và phiên bản cấu hình

Để tránh chọn tiêu chí sau khi đã thấy kết quả, nhóm lập bảng đăng ký trước. **Cột "Mục tiêu/ngưỡng" cố ý để trống**: chỉ được điền khi có căn cứ ở cột cuối (quyết định có ngày, hoặc phép đo bench/phantom có log truy vết).

| Chỉ số | Định nghĩa | Đơn vị | Cách đo | Mục tiêu/ngưỡng | Căn cứ để chốt |
|---|---|---|---|---|---|
| Tỷ lệ hoàn thành tác vụ | số lần `T_SUCCESS` / tổng số lần thử hợp lệ | % | nhãn tác vụ từ camera + log | `OPEN` | phiên pilot trên phantom, công bố là mục tiêu |
| Thời gian hoàn thành | từ `T_READY` tới `T_SUCCESS` | s | timestamp trên đồng hồ chung | `OPEN` | như trên |
| Số lần rơi / thử lại | đếm `T_FAIL_DROP`, `T_FAIL_MISPLACE` | lần | log nhãn | `OPEN` | như trên |
| Tỷ lệ `T_UNKNOWN` | số khung/phiên không gán được nhãn | % | log nhãn | `OPEN` | benchmark thị giác trên Orange Pi 5 Pro |
| Độ đúng nhãn trạng thái | bảng nhầm lẫn so nhãn thủ công | % | tập ảnh/video đã gán nhãn | `OPEN` | như trên |
| Độ trễ thị giác end-to-end | bắt khung → phát nhãn | ms | timestamp hai đầu | `OPEN` | đo trên phần cứng thật |
| Tốc độ khung thu thập | số vòng quét toàn kênh / giây | Hz | đếm `frame_id` | `OPEN` | xem `[TÍNH TOÁN]` ở `10a` §5, phải đo lại |
| Độ trễ cảm biến → lệnh servo | khung dữ liệu → thay đổi lệnh | ms | log đồng bộ | `OPEN` | đo trên bench |
| Chuyển mode đúng / sai | đếm chuyển `ASSIST→AAN` đúng và sai | lần | log `mode` + nhãn đối chiếu | `OPEN` | phương pháp đã chọn (M3, `DEC-TASK-002` 2026-10-20) nhưng **chưa kiểm chứng**; phải thử trên phantom trước |
| Sự kiện trợ lực sai pha | trợ lực phát ngoài pha tác vụ | lần | log servo + nhãn tác vụ | `OPEN` | như trên |
| Biên độ / độ lặp lại chu kỳ gập–duỗi | đặc trưng Flex sau hiệu chuẩn | đơn vị sau hiệu chuẩn | log Flex + tham chiếu | `OPEN` | Gate 1, sau khi chọn phương pháp tham chiếu góc |
| Trôi tín hiệu | lệch tĩnh của `REF_1/REF_2` theo thời gian | đơn vị ADC/mV | log ô tham chiếu | `OPEN` | Gate 1 |
| Khối lượng cụm đeo tay | nẹp + cảm biến + dây + tang (không gồm xử lý/pin/servo) | g | cân thật, ghi ngày | mục tiêu 80–120 g (`DEC-MASS-001`) — **chưa cân lại cho ba tang** | cân sản phẩm hoàn chỉnh theo `DEC-MECH-007` |
| Chi phí vật tư | cụm đeo / toàn hệ thống giàn thử | VNĐ | BOM có ngày + báo giá | dự toán 1,0–1,3 triệu / ~5,5 triệu (`DEC-COST-002`) | kiểm toán BOM |

Quy tắc đi kèm bảng này:

1. Mỗi phiên ghi `config_version_hash` (băm của toàn bộ tham số) vào `session_manifest`; đổi tham số là đổi phiên bản, không sửa ngầm.
2. Tách dữ liệu dùng để chỉnh tham số khỏi dữ liệu dùng để báo cáo; khóa phiên bản trước lượt đánh giá.
3. Dữ liệu mô phỏng/tổng hợp gắn nhãn `SIMULATED` và không được trộn vào bảng kết quả.
4. Một chỉ số không đo được bằng thiết bị hiện có thì ghi rõ "chưa đo được" thay vì bỏ trống hoặc ước lượng.

### C.5. Thứ tự triển khai công cụ và phần mềm

Trình tự chi tiết theo pha F0–F6 (schema dữ liệu → simulator/replay → firmware thu thập → hiệu chuẩn → máy trạng thái chuyển mode → nhánh thị giác → bàn điều khiển bench và báo cáo) nằm ở [`docs/08_Software_Firmware_Roadmap.md`](08_Software_Firmware_Roadmap.md); đặc tả nhánh camera ở [`docs/07_Vision_TaskState_Architecture.md`](07_Vision_TaskState_Architecture.md). Tính đến ngày cập nhật bản này, **chưa có module hay firmware nào của pipeline hiện hành được viết**; việc code bắt đầu sau khi Gate 0 (tác vụ + bản đồ kênh) được duyệt. Nền tảng thị giác dự kiến là xử lý ảnh cổ điển chạy được ngay trên Orange Pi 5 Pro, với kiến trúc detector cắm được để có thể thay bằng model học sâu nếu số liệu bench cho thấy cần; RL không thuộc phạm vi.

## Tài liệu tham khảo làm việc

[1] Tran M.C. và cộng sự (2025), “Comprehensive analysis of stroke epidemiology in Vietnam”, *Global Epidemiology*, 9:100199, DOI: 10.1016/j.gloepi.2025.100199.

[2] Pollock A. và cộng sự (2014), “Interventions for improving upper limb function after stroke”, *Cochrane Database of Systematic Reviews*, 2014(11):CD010820, DOI: 10.1002/14651858.CD010820.pub2.

> Trước khi dùng để nộp: đối chiếu từng phát biểu với toàn văn nguồn, danh mục tham khảo của bản 11A2 và yêu cầu hồ sơ ViSEF hiện hành. Không lấy số liệu y văn làm kết quả của dự án.