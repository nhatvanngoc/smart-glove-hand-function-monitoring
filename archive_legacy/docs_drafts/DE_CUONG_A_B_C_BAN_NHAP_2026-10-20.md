# ĐỀ CƯƠNG DỰ ÁN KHOA HỌC KỸ THUẬT

> Nhãn bằng chứng: `[SƠ BỘ]` ghi nhận trên bàn đo, chưa có biên bản · `[MỤC TIÊU]` ngưỡng tự đặt, chưa đo · `[TÍNH TOÁN]` suy từ tham số · `OPEN` cố ý để trống. Bám cấu trúc và mật độ của `11A2.pdf`; đã sửa 9 điểm P0 theo `research/reviews/2026-10-20_11A2_pdf_improvement_plan.md`.

**Tên dự án (tên làm việc):** *Nghiên cứu và phát triển găng tay hỗ trợ phục hồi chức năng sau đột quỵ cho vận động tinh.* — Lĩnh vực: ⟨…⟩ · Trường/CLB: ⟨…⟩ · Thành viên: ⟨nhóm tự điền⟩ · Người hướng dẫn: ⟨nhóm tự điền⟩

---

## A. VẤN ĐỀ NGHIÊN CỨU

### 1. Lý do chọn đề tài

Tại Việt Nam, tỷ lệ hiện mắc đột quỵ năm 2019 khoảng 1.541/100.000 dân, mắc mới 222/100.000 dân/năm [1]. Tổng quan Cochrane ghi nhận suy giảm vận động ảnh hưởng ~80% người sống sót; trong nhóm liệt hoàn toàn chi trên, khoảng một nửa phục hồi được một phần chức năng sau sáu tháng [5], [6].

⟨HÌNH 1 — biểu đồ tỷ lệ đột quỵ tại Việt Nam và di chứng bàn tay kéo dài⟩

Theo dõi ngoại viện thiếu công cụ định lượng ổn định: Manumeter cần thay đổi tới ~31% cường độ sử dụng ngày mới phát hiện tiến triển, đếm sai 100–200 lần dương tính giả/giờ [7]; phỏng vấn kỹ thuật viên PHCN (09/2026, nguồn sơ cấp của nhóm) ghi nhận găng hiện có không phù hợp tập tại nhà về giá, khối lượng, thao tác. Nhóm chế tạo găng nẹp ba ngón đưa người tập từ vận động gập–duỗi đến thao tác **gắp thìa bằng ngón cái, trỏ, giữa**, thay vì chỉ đếm chuyển động hay kéo thụ động theo chu kỳ.

### 2. Cơ sở lý thuyết về y sinh

**2.1. Đại diện vỏ não và cơ chế phản hồi Hebbian.** Penfield & Boldrey [11] và mạng SCAN của Gordon et al. [4] cho thấy bàn tay chiếm diện tích đại diện vận động rất lớn trên vỏ não — cơ sở tập trung vào ba ngón trụ cột (cái, trỏ, giữa). Theo học thuyết Hebb [12] và nguyên lý PHCN [2], [3], phản hồi cảm giác đồng bộ với nỗ lực vận động giúp định hướng tập luyện; đề tài khai thác cơ sở này để xây chế độ trợ lực theo nhu cầu và phản hồi thị giác từ đáp ứng cảm biến. Đề tài không đo hoạt động vỏ não, không chứng minh tái tổ chức thần kinh.

⟨HÌNH 2 — bản đồ Homunculus [11] và sự phân bổ chi phối bàn tay [4]⟩

**2.2. Trương lực cơ, chênh lệch tầm vận động (GAP) và độ tin cậy đo lường.** Sau đột quỵ, suy giảm vận động thường kết hợp yếu cơ và tăng trương lực co cứng [8], [10]. Đề tài khảo sát GAP = PROM − AROM như chỉ số mô tả chênh lệch góc, đo bằng công cụ ngoài, không xem riêng nó là phép chẩn đoán. Độ tin cậy hệ đo đánh giá qua hệ số biến thiên (CV), sai số chuẩn (SEM) và ngưỡng MDC [7] — căn cứ dành hai ô cảm biến tham chiếu và đăng ký trước chỉ số (B.3, C.3).

### 3. Xác định vấn đề nghiên cứu

Vấn đề nghiên cứu: mảng cảm biến gập và áp trở trên khung nẹp ba ngón có tạo tín hiệu đủ lặp lại để phát hiện vận động chủ động, và cơ cấu servo–dây–ba tang có tạo được dạng kẹp ba chấu với trợ lực giảm dần tự động hay không. Hai câu hỏi chính: (i) trong phép thử có tải, điều kiện xác định, tín hiệu áp trở hai vách lòng–mu phân biệt được hướng vận động với độ tin cậy chấp nhận được và tự phát hiện phiên đo lỗi do lỏng nẹp hay không; (ii) bộ điều khiển phân biệt được vận động do người tập khởi xướng với chuyển động do chính cơ cấu tạo ra hay không.

Nhóm tập trung vào 6 nội dung: (1) khung nẹp ba ngón tích hợp 3 cảm biến gập Flex và 6 ô Velostat vi sai lòng–mu; (2) khảo sát tải, độ trôi trên mô hình tay silicone; (3) xác định bộ chỉ số EI, GAP, RAL và chỉ số tác vụ; (4) cơ cấu ba tang với duỗi chủ động bằng nhả dây; (5) quy tắc tự động chuyển chế độ và nhánh thị giác cho bài tập gắp thìa; (6) kiểm chứng trên giàn đo và phantom, thử đeo thụ động trên người tình nguyện khỏe mạnh sau khi được phê duyệt.

### 4. Mục tiêu nghiên cứu

Mục tiêu: chế tạo và đánh giá nguyên mẫu găng nẹp ba ngón theo các ngưỡng kỹ thuật dự kiến sau trên băng thử và phantom — toàn bộ `[MỤC TIÊU]`, chưa đo:

- Quét 11 kênh (PA-2) với tốc độ khung ≥ 20 Hz; đáp ứng trên tải chuẩn đạt SNR ≥ 18 dB và R² ≥ 0,90.
- Phân biệt hướng vận động ≥ 90%; phân loại mức kích hoạt ≥ 85%.
- Độ lặp lại nội phiên CV ≤ 5%, giữa ngày CV ≤ 8%; trễ đàn hồi h ≤ 18%; dãn tải tĩnh sau 60 s ≤ 8%.
- Trễ xử lý biên ≤ 20 ms; giới hạn an toàn cơ cấu đặt theo hành trình dây, góc kéo, dòng servo và hành vi nhả khi mất nguồn — không dùng ngưỡng lực suy ra từ cảm biến áp trở.
- Tỷ lệ hoàn thành bài tập thìa và độ đúng nhãn trạng thái từ camera: `OPEN`, chốt sau lượt pilot trên phantom.
- Thử khả năng tự đeo và bắt tín hiệu vận động tự nguyện ở người tình nguyện khỏe mạnh theo quy trình an toàn được phê duyệt trước khi đo.

Khác bản trước: bỏ ngưỡng "lực an toàn ≤ 5 N" và bỏ chuẩn hóa chỉ số theo lực đặt trước, vì Velostat chưa hiệu chuẩn bằng tải độc lập, sai số lớn [13], [14]; ngưỡng chỉ điền khi có căn cứ, không chọn sau khi xem dữ liệu.

---

## B. GIẢI PHÁP VÀ THIẾT KẾ

### 1. Tổng quan đề tài

Hệ thống găng tay theo dõi định lượng và tập vận động tinh bàn tay sau đột quỵ, kiến trúc phân tán: khung nẹp ba ngón in 3D tích hợp 3 cảm biến gập Flex, 6 ô áp trở Velostat vi sai hai vách lòng–mu, 2 ô tham chiếu; mạch thu thập PGA 16-bit ADS1115 qua bộ chuyển mạch CD74HC4067, lọc số DSP 4 bước trên ESP32-S3; Orange Pi 5 Pro nhận biết thìa và vùng đích, trích xuất bộ ba chỉ số tiến triển (EI, GAP, RAL); cơ cấu trợ lực theo nhu cầu (AAN) truyền động bằng dây cáp cuốn trên ba tang riêng. Khác với kéo cưỡng bức: chỉ trợ lực khi nỗ lực chủ động chưa đủ hoàn thành tầm vận động, tự giảm khi phát hiện vận động do người tập khởi xướng, kèm phản hồi thị giác trực tiếp để thúc đẩy người tập chủ động.

⟨HÌNH 3 — sơ đồ khối bốn tầng: cụm đeo → thu thập → trợ lực → tác vụ và phản hồi⟩

Một chu kỳ vận hành: quét 11 kênh → lọc và chuẩn hóa → đặc trưng vận động → máy trạng thái chọn chế độ → lệnh servo có giới hạn → nhãn tác vụ từ camera → ghi log theo dấu thời gian chung.

### 2. Hạn chế của các giải pháp hiện tại và hướng tiếp cận của đề tài

Rào cản của phương pháp ngoại viện hiện tại: thang đo lâm sàng (FMA-UE, ARAT) gián đoạn, 2–4 tuần/lần; thiết bị đeo cổ tay (Manumeter) chỉ đếm chuyển động thô, 100–200 lần dương tính giả/giờ [7]; điện cơ bề mặt (sEMG) suy giảm do mồ hôi, khó tách co cơ; găng robot thương mại chủ yếu kéo thụ động cố định (CPM) — ghi nhận từ phỏng vấn kỹ thuật viên PHCN, chưa có nguồn y văn trực tiếp; các hệ găng mềm đã công bố [9], [15] đánh giá chủ yếu trên người khỏe, không lấy bài tập vận động tinh với vật thật làm đơn vị đánh giá.

Hướng tiếp cận: lấy **bài tập gắp thìa** làm đơn vị đánh giá chức năng thay vì đếm chuyển động; dùng cảm biến áp trở giá rẻ với **chỉ số tương đối trong cùng người** thay vì đo lực tuyệt đối [13], [14]; đặt toàn bộ kiểm định trên giàn đo và phantom trước khi xét đến người; giải bài toán phân xử ý định người–máy ở mức tối giản bằng một cửa sổ thăm dò (B.6).

### 3. Thiết kế khung nẹp ngón tay và cấu trúc cảm biến

Khung nẹp in 3D ôm ba ngón cái–trỏ–giữa, khớp rãnh trượt bù chênh chiều dài ngón, khóa ngàm xoay hai bản lề kép (Mech 9) cho thời gian tự đeo 22 s `[SƠ BỘ]`, đóng/mở bằng một tay. Cụm đeo mục tiêu 80–120 g `[MỤC TIÊU]`, chưa cân; bộ xử lý, pin, servo đặt ngoài tay. Truyền trợ lực: servo cuốn dây câu cá trực tiếp lên **ba tang riêng**, mỗi ngón một tang; duỗi bằng servo nhả dây chủ động; không lò xo hồi vị, không đàn hồi nối tiếp, không khớp bốn khâu.

Cấu hình cảm biến PA-2 (đã duyệt 2026-10-20): **11 kênh quét** trên 16 kênh của CD74HC4067.

| Kênh | Phần tử | Vai trò |
|---|---|---|
| 3 | Flex cái / trỏ / giữa | biến thiên gập–duỗi, tư thế từng ngón |
| 6 | Velostat cặp lòng–mu ba ngón | áp lực/tiếp xúc; phân biệt "ép vào nẹp" (ô mu tăng) với "tiếp xúc vật" (ô lòng tăng) |
| 2 | tham chiếu `REF_1`, `REF_2` không chịu tải | trôi nền, phát hiện phiên đo lỗi |
| 1 | `CH15` nối đất | mốc đo xuyên kênh |
| 4 | dự phòng | mở rộng nếu Gate 1 cần thêm vị trí đo |

Ngân sách quét `[TÍNH TOÁN]`: chờ 300 µs + 1 đọc nháp + 860 mẫu/giây ⇒ 2,63 ms/kênh ⇒ 11 kênh ≈ 35 Hz toàn khung, 16 kênh ≈ 24 Hz; chưa đo. Con số ~415 Hz ở tài liệu cũ giả định ADC nội của vi điều khiển, không áp dụng cho ADC ngoài.

Còn `OPEN`: vị trí lắp từng ô, dải điện trở Flex tại vị trí lắp (phải đo), điện trở phân áp, tốc độ khung thật; một động cơ kéo ba tang hay ba động cơ riêng; đường kính tang, hành trình dây, vị trí neo; hành vi nhả khi mất nguồn (câu hỏi cơ khí, không xử lý bằng phần mềm); phương pháp đo căng dây độc lập; bản vẽ CAD Mech 9 chưa có trong kho.

⟨HÌNH 4 — khung nẹp Mech 9 và cơ cấu ba tang⟩

### 4. Chuỗi thu thập tín hiệu và thuật toán lọc số DSP 4 bước

Kiến trúc: cầu phân áp → CD74HC4067 → PGA ADS1115 (16-bit, I²C) → ESP32-S3. Không dùng tầng khuếch đại cố định (lý do ở C.2).

Bốn bước: (1) sau chuyển kênh, chờ **300 µs** và đọc nháp một lần trước khi lấy `V_raw[k]` — xả điện tích dư trên tụ ký sinh, giảm bóng ma kênh; (2) đường nền thích ứng khi |ΔV| ≤ **180 mV**: `V_base[k] = 0,998·V_base[k−1] + 0,002·V_raw[k]`, bù trôi do nhiệt độ và độ ẩm tiếp xúc da; (3) vùng chết trừ tuyến tính: `S_clean = 0` nếu ΔV ≤ 180 mV, ngược lại `ΔV − 180 mV`; (4) làm mượt hàm mũ EMA **α = 0,20** cho tín hiệu đáp ứng `S_net`. Mỗi kênh có đường hiệu chuẩn riêng trên băng thử với tải chuẩn đã biết, ghi ngày, nhiệt độ, cách lắp, số lần lặp.

Ba giới hạn khi trích dẫn: bước (3) ghim đầu ra về 0 khi nghỉ nhưng **không có nghĩa nhiễu thô đã mất** (thô 50–135 mV, xem C.2) — báo cáo nhiễu phải kèm cả tín hiệu thô lẫn sau lọc; `S_clean`/`S_net` **không phải lực theo Newton**, vì Velostat trễ đàn hồi, sai số 16–48% toàn dải tùy mẫu và cách lắp [13], [14], nên chỉ dùng làm chỉ số tương đối trong cùng người, cùng phiên, cùng cách đeo; các hằng số 300 µs, 180 mV, 0,998/0,002, α = 0,20 là tham số đang dùng, chưa tối ưu có hệ thống, chưa kiểm chứng trên nhiều mẫu.

### 5. Phương pháp xác định bộ chỉ số EI – GAP – RAL và kiểm soát chất lượng

**EI:** tích phân đáp ứng tương đối trong pha chủ động, chuẩn hóa theo mức tham chiếu của chính phiên đó; công thức và cách chọn mức tham chiếu `OPEN`; không dùng biểu thức có lực đặt trước ở mẫu số vì dự án không đo được Newton. **GAP = PROM − AROM** (độ): thước đo góc kết hợp biên độ gập đọc từ Flex đã hiệu chuẩn; chỉ mô tả mức yếu/liệt, không phải phép chẩn đoán. **RAL:** mức trợ giúp nhỏ nhất để hoàn thành chu kỳ gập–duỗi theo tiêu chí đặt trước; ngưỡng tỷ lệ hoàn thành `OPEN` (mức ≥ 80% ở bản trước chưa được duyệt). **Chỉ số tác vụ:** tỷ lệ hoàn thành bài tập thìa, thời gian hoàn thành, số lần rơi/đặt sai, số lần chuyển chế độ đúng/sai, số sự kiện trợ lực sai pha.

Kiểm soát chất lượng: mỗi phiên ghi `config_version_hash` vào manifest — đổi tham số là đổi phiên bản; tách dữ liệu chỉnh tham số khỏi dữ liệu báo cáo, khóa phiên bản trước lượt đánh giá; dữ liệu mô phỏng gắn nhãn `SIMULATED`, không trộn vào bảng kết quả; chỉ số không đo được thì ghi "chưa đo được", không ước lượng. Độ tin cậy từng chỉ số đánh giá bằng CV nội phiên, CV liên ngày, SEM, MDC [7].

### 6. Cơ chế trợ lực theo nhu cầu (AAN) và quy tắc tự động chuyển chế độ

Trong AAN, vận động ngón do người tập khởi xướng; bộ điều khiển chỉ bù phần trợ lực cần thiết theo tín hiệu vận động và trạng thái tác vụ, không đóng ngón hoàn toàn theo lệnh camera. Chuyển từ chế độ hỗ trợ gập–duỗi sang AAN là **tự động**, không cần kỹ thuật viên nhấn nút.

Điểm khó: phân biệt vận động do người tập khởi xướng với chuyển động do chính cơ cấu tạo ra — nếu không, hệ thống tự thăng cấp cho người không có vận động chủ động. Phương pháp đã chọn (**M3**): tạm ngưng trợ lực trong một cửa sổ ngắn định trước, đo đáp ứng trong cửa sổ đó, rồi quyết định giữ hay thăng cấp chế độ. Đây mới là chọn phương pháp, chưa kiểm chứng: độ dài cửa sổ, tần suất mở, tiêu chí nhận diện đáp ứng, hành vi khi không có đáp ứng, số lần lặp đều `OPEN`; bắt buộc rà an toàn trước mọi lần chạy có cấp nguồn. M3 không phát hiện nỗ lực không tạo ra chuyển động. Học tăng cường ngoài phạm vi đề tài.

| Trạng thái | Ý nghĩa và hành vi trợ lực |
|---|---|
| `SAFE_STOP` | mặc định khi khởi động hoặc có sự cố; servo không tải, dây ở vị trí nhả |
| `ASSIST` | hỗ trợ gập–duỗi hoàn toàn theo biên độ đặt trước |
| `EVAL` | mở cửa sổ thăm dò tự nguyện (M3); tạm ngưng trợ lực trong khoảng ngắn định trước |
| `AAN` | trợ lực giảm dần theo đáp ứng của người tập |
| `TASK` | thực hiện bài tập thìa; trợ lực theo pha tác vụ từ nhãn camera |
| `INVALID` | phiên đo lỗi (nẹp lỏng, ô tham chiếu trôi bất thường); ngưng trợ lực, yêu cầu kiểm tra cách đeo |
| `FAULT` | lỗi phần cứng (servo quá dòng, mất phản hồi, mất đồng bộ); cắt trợ lực, về `SAFE_STOP`, ghi log |

### 7. Nhánh thị giác và bài tập gắp thìa

Camera nhận biết thìa và vùng đích trong bố trí cố định, gán nhãn trạng thái tác vụ (`T_READY`, `T_GRASP`, `T_LIFT`, `T_MOVE`, `T_SUCCESS`, `T_FAIL_DROP`, `T_FAIL_MISPLACE`, `T_UNKNOWN`) và phản hồi trực quan cho người tập; không đo lực ngón, không xác nhận phục hồi lâm sàng. Detector cắm được: xử lý ảnh cổ điển (OpenCV) trên Orange Pi 5 Pro, chỉ thay bằng mô hình học sâu nếu benchmark trên đúng phần cứng cho thấy không đạt; nếu dùng độ sâu đơn ảnh phải hiệu chuẩn tỷ lệ trước khi gọi tọa độ là tọa độ thực. Toàn bộ chỉ số thị giác — độ đúng, tỷ lệ `T_UNKNOWN`, độ trễ đầu-cuối, số khung/giây — `OPEN`, chưa benchmark (bảng C.3); giao tiếp Orange Pi 5 Pro ↔ ESP32-S3 chưa tích hợp.

Bài tập thìa cần tờ yêu cầu tác vụ: loại thìa và khối lượng, kích thước và vị trí vùng đích, khoảng cách di chuyển, tiêu chí đặt thành công, thời gian tối đa một lượt, số lượt mỗi phiên — tất cả `OPEN`, chờ đo vật thật.

⟨HÌNH 5 — bố trí bàn thử: camera, vùng đích, mô hình tay giả⟩

---

## C. KẾT QUẢ CHẾ TẠO SƠ BỘ VÀ KẾ HOẠCH KIỂM ĐỊNH

### 1. Chế tạo và khảo sát thực nghiệm 9 thế hệ cơ khí khóa nẹp

Chín phương án khóa nẹp in thử, đeo thử theo ba nhóm nguyên lý. Nhóm 1 (Mech 1–3: vòng kẹp chữ C đàn hồi, rãnh trượt đuôi én, đai Velcro): 55–80 s, không giữ được tiền tải. Nhóm 2 (Mech 4–6: chốt xuyên ngang, khóa gài mặt mu, thanh răng rút): 40–65 s, đòi hỏi hai tay hoặc căn chỉnh chính xác. Nhóm 3: Mech 8 (bản lề một trục + ngàm đàn hồi) 28 s nhưng lỗi bền mỏi; Mech 9 (khóa ngàm xoay hai bản lề kép) 22 s, chưa hỏng sau 50 chu kỳ — chọn làm phương án triển khai.

| Phương án | Nguyên lý khóa | Thời gian tự đeo | Sau 50 chu kỳ đóng/mở | Ngày / số lần lặp / người thử / thông số in |
|---|---|---|---|---|
| Mech 1–3 | vòng kẹp chữ C; rãnh trượt đuôi én; đai Velcro | 55–80 s | không đạt | `OPEN` |
| Mech 4–6 | chốt xuyên ngang; khóa gài mặt mu; thanh răng rút | 40–65 s | không đạt | `OPEN` |
| Mech 7 | ⟨bổ sung hoặc ghi rõ đã bỏ qua⟩ | `OPEN` | `OPEN` | `OPEN` |
| Mech 8 | bản lề một trục + ngàm đàn hồi | 28 s | lỗi bền mỏi | `OPEN` |
| Mech 9 | khóa ngàm xoay hai bản lề kép | 22 s | phương án triển vọng nhất, chưa hỏng | `OPEN` |

Các mốc thời gian là quan sát thử nội bộ `[SƠ BỘ]`: chưa có biên bản đo, ngày thử, số lần lặp, người thực hiện, loại đồng hồ đo; không dùng so sánh định lượng giữa các phương án theo nghĩa thống kê. Mech 9 chưa có bản vẽ CAD trong kho, chưa đo bền mỏi theo quy trình có biên bản; 50 chu kỳ rất nhỏ so với số chu kỳ đóng/mở của một liệu trình nhiều tuần.

⟨HÌNH 6 — ảnh các thế hệ khóa nẹp đã in thử⟩

### 2. Thực nghiệm đo kiểm mạch thu nhận qua 2 vòng lặp thiết kế phần cứng

**Vòng lặp 1 — tầng khuếch đại dụng cụ INA333, G ≈ 6,5.** Ngõ ra sạch, các kênh cách ly tốt khi đo với nguồn tín hiệu chuẩn. Khi lắp cảm biến thật và gài khóa tiền tải của nẹp: cầu phân áp sụt dưới 1,42 V, ngõ ra bão hòa cứng ≈ 2.838 mV, dải tuyến tính còn 1,44–1,92 V, nhiễu nền lúc nghỉ 50–135 mV. Nguyên nhân: khuếch đại cố định không phù hợp trở kháng và dải điện trở biến thiên lớn của phần tử áp trở khi có tiền tải.

**Vòng lặp 2 — bỏ INA333, đọc trực tiếp qua PGA ADS1115 + DSP 4 bước.** Giữ trọn dải ngõ vào 0–3.300 mV trên bàn đo; thêm đọc nháp và chờ 300 µs sau chuyển kênh; vùng chết 180 mV giữ đường nền ổn định khi nghỉ.

| Hạng mục | `[ĐÃ ĐO]` có log/biên bản | `[SƠ BỘ]` ghi nhận bàn đo | `[MỤC TIÊU]` chưa đo |
|---|---|---|---|
| Kiến trúc ngõ vào | chưa có | bỏ INA333, đọc trực tiếp PGA ADS1115, trọn dải 0–3.300 mV | thu trọn dải, không bão hòa ở tải thiết kế |
| Bão hòa ngõ ra | chưa có | vòng 1: cầu phân áp < 1,42 V, bão hòa ≈ 2.838 mV, dải tuyến tính 1,44–1,92 V | không bão hòa ở cấu hình PA-2 |
| Nhiễu nền lúc nghỉ | chưa có | thô 50–135 mV; sau vùng chết 180 mV đầu ra nghỉ ghim về 0 | V_pp ≤ 5 mV sau lọc, đo ≥ 10 phiên |
| Xuyên kênh | chưa có | đọc nháp + chờ 300 µs giảm bóng ma kênh; `CH15` làm mốc | ngưỡng `OPEN` |
| SNR, độ tuyến tính | **chưa có log trong kho dự án** | bản trước ghi SNR 21,4 dB, R² 0,93 — không truy vết được | SNR ≥ 18 dB; R² ≥ 0,90 |
| Tốc độ khung | chưa có | vòng 1 ≈ 22 Hz/16 kênh (trễ chuyển kênh ~120 µs) | ≥ 20 Hz toàn khung; `[TÍNH TOÁN]` ≈ 35 Hz/11 kênh |
| Trôi nền dài hạn | chưa có | chưa có chuỗi log dài ngày | log ≥ 10 ngày với `REF_1/REF_2` |

Để giữ hai số SNR và R² trong hồ sơ cần ba bước: đối chiếu đồ thị đã xuất trong `03_Serial_Plotter_exports`; lập lại thành buổi đo có biên bản (manifest phiên, tải chuẩn, số lần lặp, điều kiện môi trường, kiểm tra tham chiếu trước/sau); ghi định nghĩa phép tính — cửa sổ tín hiệu và nhiễu cho SNR, số điểm tải và phương pháp hồi quy cho R². Thiếu một bước, hai số chuyển xuống cột `[MỤC TIÊU]`.

⟨HÌNH 7 — đồ thị vòng lặp 1 (bão hòa) và vòng lặp 2 (trọn dải); chú thích ghi rõ là ghi nhận bàn đo, chưa phải buổi đo có biên bản⟩

### 3. Kế hoạch kiểm chuẩn trên giàn đo và mô hình bàn tay giả

Phương tiện: giàn đo cơ học trục trượt tạo chuyển động gập–duỗi lặp lại theo biên độ và tốc độ đặt trước; tải chuẩn khối lượng đã biết đặt đúng đường truyền lực; mô hình bàn tay giả silicone; thước đo góc làm tham chiếu biên độ khớp và PROM/AROM. Toàn bộ kiểm định trên bàn thử và phantom; chỉ xem xét thử có cấp nguồn trên người trưởng thành khỏe mạnh sau khi rà an toàn đạt và có phê duyệt, theo protocol riêng; không thử trên người bệnh trong phạm vi đề tài.

Tám quy trình đo: (1) đáp ứng theo tải và R² — tải tăng dần và giảm dần, ≥ 3 lượt lặp; (2) trễ đàn hồi và creep — so nhánh tăng/giảm, giữ tải không đổi 60 s; (3) độ lặp lại nội phiên và liên ngày — cùng điều kiện, cùng cách lắp; (4) nhiễu nền và SNR — ghi ở trạng thái nghỉ, báo cáo cả tín hiệu thô lẫn sau lọc; (5) xuyên kênh — kích thích một kênh, đọc các kênh nghỉ, `CH15` làm mốc; (6) trôi nền — chuỗi log ≥ 10 ngày với `REF_1/REF_2`; (7) tốc độ khung và trễ biên — đếm `frame_id`, đo từ khung dữ liệu đến thay đổi lệnh servo; (8) cơ cấu ba tang trên phantom — hành trình so với lệnh, dạng kẹp ba chấu, nhả khi cắt nguồn, căng dây đo bằng phương pháp độc lập. Mỗi phiên ghi ngày giờ, người vận hành, băm cấu hình, nhiệt độ/độ ẩm nếu có, cách lắp, số lần lặp, kiểm tra tham chiếu trước/sau. Loại phiên khi ô tham chiếu trôi vượt ngưỡng, mất đồng bộ dấu thời gian, hoặc có can thiệp vào cách đeo giữa phiên — phiên bị loại phải ghi lý do.

| Chỉ số | Cách đo | Mục tiêu/ngưỡng | Căn cứ để chốt |
|---|---|---|---|
| Tỷ lệ hoàn thành tác vụ; thời gian; số lần rơi/đặt sai | nhãn camera + log, đồng hồ chung | `OPEN` | pilot trên phantom |
| Tỷ lệ `T_UNKNOWN`; độ đúng nhãn trạng thái | log nhãn; bảng nhầm lẫn so nhãn thủ công | `OPEN` | benchmark thị giác trên Orange Pi 5 Pro |
| Độ trễ thị giác đầu-cuối | dấu thời gian hai đầu | `OPEN` | đo trên phần cứng thật |
| Tốc độ khung thu thập | đếm `frame_id` | mục tiêu ≥ 20 Hz; `OPEN` | `[TÍNH TOÁN]` ≈ 35 Hz, phải đo |
| Trễ cảm biến → lệnh servo | log đồng bộ | mục tiêu ≤ 20 ms; `OPEN` | đo trên bàn thử |
| Chuyển chế độ đúng/sai; trợ lực sai pha | log `mode` + nhãn đối chiếu | `OPEN` | M3 đã chọn, chưa kiểm chứng |
| Biên độ, độ lặp lại chu kỳ gập–duỗi | log Flex + thước đo góc | mục tiêu CV ≤ 5% nội phiên, ≤ 8% liên ngày | Gate 1 |
| Trôi tín hiệu | log `REF_1/REF_2` | `OPEN` | Gate 1, log ≥ 10 ngày |
| SNR, R² trên băng thử | băng thử trục trượt + tải chuẩn | mục tiêu ≥ 18 dB; ≥ 0,90 | Gate 1, phải có log |
| Trễ đàn hồi, creep, nhiễu nền | băng thử | mục tiêu h ≤ 18%; creep 60 s ≤ 8%; V_pp ≤ 5 mV sau lọc | Gate 1 |
| Khối lượng cụm đeo | cân thật, ghi ngày | mục tiêu 80–120 g, chưa cân lại cho ba tang | cân sản phẩm hoàn chỉnh |
| Chi phí vật tư | BOM có ngày + báo giá | dự toán 1,0–1,3 triệu / ~5,5 triệu VNĐ | kiểm toán BOM |

So sánh tối thiểu khi tích hợp: trợ lực cố định và AAN tự động trên cùng phantom, điều kiện tương đương; tắt từng nguồn cảm biến (chỉ Flex, chỉ Velostat, chỉ camera, đủ cả ba) để xác định đóng góp của từng nguồn. Phản hồi thị giác không phải bằng chứng cải thiện phục hồi.

### 4. Kế hoạch hoàn thiện dự án trong tương lai

Thứ tự triển khai: **Gate 0** — tờ yêu cầu tác vụ, bản đồ kênh PA-2, phiếu buổi đo, máy trạng thái, log trôi ≥ 10 ngày (~3 tuần); **Gate 1** — hiệu chuẩn Flex/Velostat trên băng thử, đo SNR, R², CV, trễ đàn hồi, creep (~3–4 tuần); **Gate 2** — cơ cấu ba tang trên phantom, đo hành trình, nhả khi mất nguồn, giới hạn an toàn, xuất CAD và đo độ bền Mech 9 (~3–4 tuần); **Gate 3** — nhánh thị giác và bài tập thìa, benchmark trên Orange Pi 5 Pro (~2–3 tuần); **tích hợp** — chu trình ba bước trên phantom, so sánh trợ lực cố định với AAN tự động (~2 tuần). Chi phí vật tư: cụm đeo dự toán 1,0–1,3 triệu VNĐ, toàn hệ thống và giàn thử ~5,5 triệu VNĐ khi tận dụng thiết bị phòng thí nghiệm; dự toán chưa kiểm toán, cần BOM có ngày và báo giá.

Tính khả thi: chắc chắn hoàn thành Gate 0, Gate 1, CAD và độ bền Mech 9, cụm ba tang thử trên phantom; Gate 3 và tích hợp đầy đủ có rủi ro trễ vì nhánh thị giác chưa benchmark, giao tiếp hai bo mạch chưa tích hợp; không cam kết hoàn thành chuỗi đánh giá trên người trong khuôn khổ đề tài.

### 5. Kết luận

**Đã làm:** in thử và so sánh 9 phương án khóa nẹp, chọn Mech 9 `[SƠ BỘ]`; hoàn thành 2 vòng lặp thiết kế mạch thu nhận, xác định nguyên nhân bão hòa ngõ vào ở vòng 1 và chuyển sang đọc trực tiếp qua PGA ADS1115 `[SƠ BỘ]`; xác định chuỗi DSP 4 bước và bộ tham số đang dùng; chốt cấu hình cảm biến PA-2 (11 kênh quét) và cơ cấu ba tang với duỗi chủ động bằng nhả dây; viết định nghĩa EI, GAP, RAL cùng bảng đăng ký trước chỉ số; đặc tả máy trạng thái 7 chế độ và phương pháp M3.

**Chưa làm:** chế tạo cụm cảm biến theo PA-2; log/biên bản cho SNR, R², tốc độ khung, độ lặp lại; đo bền mỏi Mech 9 theo quy trình; xuất và lưu bản vẽ CAD; cân khối lượng cụm đeo; kiểm toán chi phí; viết firmware và mô-đun phần mềm của luồng xử lý hiện hành; benchmark nhánh thị giác; kiểm chứng quy tắc M3; thử trên người.

Giới hạn: thử trên bàn và phantom không chứng minh hiệu quả trên người, an toàn đã chứng nhận hay cải thiện chức năng sau đột quỵ; dữ liệu người khỏe không thay dữ liệu người bệnh; không tuyên bố tính mới/"đầu tiên" trước khi rà prior art cho tổ hợp AAN + Velostat + Flex + camera + bài tập gắp; cảm biến áp trở chỉ cho chỉ số tương đối trong cùng người, không dùng làm thiết bị đo lực hay cơ chế an toàn.

### 6. Hướng phát triển

- **Phần cứng:** thay hệ dây dẫn rời bằng mạch in mềm đi chìm trong nẹp in 3D để tăng độ bền cơ học, chống đứt gãy và tăng tính thẩm mỹ; mở rộng từ ba ngón lên năm ngón sau khi có dữ liệu hiệu chuẩn đủ tin cậy.
- **Quy chuẩn y sinh và thử nghiệm lâm sàng:** sau khi hoàn tất toàn bộ cổng kiểm định an toàn kỹ thuật trên giàn đo cơ học và phantom silicone, xây dựng hồ sơ xin phê duyệt của Hội đồng Đạo đức trong nghiên cứu y sinh học (IRB) tại cơ sở y tế chuyên khoa trước khi triển khai thử nghiệm đối chứng lâm sàng với thang đo FMA-UE và ARAT — giai đoạn sau, ngoài phạm vi đề tài này.
- **Điều khiển:** cá nhân hóa ngưỡng theo tầm vận động từng người tập; các phương pháp điều khiển thích ứng nâng cao, kể cả học máy, chỉ xem xét khi đã có bộ dữ liệu bàn thử/phantom đủ lớn và đã khóa quy tắc an toàn.

---

## TÀI LIỆU THAM KHẢO

[1] Tran et al. (2025), "Comprehensive analysis of stroke epidemiology in Vietnam: Insights from GBD 1990–2019 and RES-Q 2017–2023", *Global Epidemiology*, 9:100199.

[2] Bộ Y tế (2014), "Hướng dẫn chẩn đoán và điều trị Phục hồi chức năng sau đột quỵ não" (Quyết định số 4039/QĐ-BYT).

[3] Cao Minh Châu, Nguyễn Thị Kim Liên, Trần Trọng Hải (2020), "Giáo trình Phục hồi chức năng", Nhà xuất bản Y học, Hà Nội.

[4] Gordon E. M., et al. (2023), "A somato-cognitive action network alternates with effector regions in motor cortex", *Nature*, 617(7960), 351–359.

[5] Pollock A., et al. (2014), "Interventions for improving upper limb function after stroke", *Cochrane Database of Systematic Reviews*, CD010820.

[6] Langhorne P., Coupar F., Pollock A. (2009), "Motor recovery after stroke: a systematic review", *The Lancet Neurology*, 8(8), 741–754.

[7] Schwerz de Lucena D., et al. (2022), "Providing Real-Time Wearable Feedback to Increase Hand Use after Stroke: A Randomized Controlled Trial (Manumeter)", *Sensors*, 22(18):6938.

[8] Amin F., et al. (2024), "Remote Monitoring for the Management of Spasticity: Challenges, Opportunities and Proposed Technological Solution", *Sensors* / PMC11793859.

[9] Li M., et al. (2024), "A magnetically controlled soft robotic glove for hand rehabilitation", *Device* (Cell Press), 2(4):100215.

[10] Lin B. S., et al. (2022), "Design of a Multi-Sensor System for Exploring Upper Limb Spasticity in Stroke Patients", *Sensors*, 22(19):7212.

[11] Penfield W., Boldrey E. (1937), "Somatic motor and sensory representation in the cerebral cortex of man as studied by electrical stimulation", *Brain*, 60, 389–440.

[12] Hebb D. O. (1949), "The Organization of Behavior: A Neuropsychological Theory", New York: Wiley.

[13] Hopkins M., Vaidyanathan R., McGregor A. H. (2020), "Examination of the Performance Characteristics of Velostat as an In-Socket Pressure Sensing Material", *IEEE Sensors Journal*, 20(12).

[14] Blin J., et al. (2022), "Evaluation of the Foot Center of Pressure Estimation from Pressure Insoles during Gait", *Sensors*, 22(15):5628.

[15] Radder B., et al. (2018), "Home-based robot-assisted arm training with an interactive robotic glove after stroke (IRONHAND)", *Journal of Rehabilitation Medicine*, 50, 598–606.

> Ghi chú nội bộ — xóa trước khi nộp: (i) [2], [3], [6], [8] đang `UNVERIFIED` hoặc mới đối chiếu một phần trong `research/evidence/SOURCE_LEDGER.csv` — phải đối chiếu toàn văn hoặc bỏ; [1] `VERIFIED`, [7] `READ_FULL`, [5] `READ_FULL_BACKGROUND`, [11] `VERIFIED` gián tiếp, [12] `READ_SECONDARY_CONFIRMED`, [4] mới đối chiếu abstract; [13]–[15] là nguồn nhóm bổ sung so với bản `11A2.pdf`. (ii) [8] trong bản PDF ghi *Sensors*/PMC11793859 nhưng sổ nguồn của dự án ghi *IEEE Open Journal of Engineering in Medicine and Biology* — phải đối chiếu lại trước khi nộp. (iii) Khối thông tin bản dựng ở đầu tệp Word và ghi chú này phải xóa trước khi nộp.
