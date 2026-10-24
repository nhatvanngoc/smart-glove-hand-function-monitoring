# Kiểm kê thiết bị & quyền truy cập (2026-09-19)

## Kiểm kê cập nhật 2026-10-24 — ĐÃ CHỐT TOÀN BỘ DANH MỤC VÀ KIẾN TRÚC PHẦN CỨNG (`DEC-HW-008`)

Chủ dự án đã chính thức chốt mã linh kiện, thông số và phương án phân bổ 2 cụm (đai hông và đeo tay):

| Linh kiện / Module | Mã / Thông số kỹ thuật chốt | Vị trí lắp đặt | Vai trò chức năng |
|---|---|---|---|
| **Cảm biến uốn cong (Flex)** | **3x ZD10-100** (Dài 100 mm, dày <0,25 mm, $R > 10	ext{ M}\Omega 	o 20-50	ext{ k}\Omega$, >1 triệu lần uốn) | Mu nẹp 3 ngón (kéo dài qua khớp MCP về mu bàn tay) | Đo góc gập ngón liên tục ($0^\circ - 90^\circ$); cầu phân áp $R_{\text{ref}} = 47	ext{ k}\Omega - 100	ext{ k}\Omega$ |
| **Động cơ trợ lực (Servo)** | **3x MG90S** (Bánh răng kim loại, 13,4 g, $22,8 	imes 12,2 	imes 28,5	ext{ mm}$, mô-men $1,8 - 2,2	ext{ kg}\cdot	ext{cm}$) | Cụm nẹp cổ tay | Tang cuốn 14 mm sinh lực kéo ~25 N (vượt mức yêu cầu 3–6 N để gập ngón) |
| **Cảm biến thị giác** | **Camera OV13855** (13 MP, MIPI-CSI 4-lane cho Orange Pi 5 Pro) | Giá đỡ bàn tập / chân đế bao quát cảnh gắp thìa | Cung cấp luồng ảnh RGB cho mô hình Depth Anything V2 ước lượng độ sâu 3D |
| **Khối nguồn chính** | **Khối Pin Li-ion 2S (2 cell 18650, 7,4 V danh định)** | Hộp điều khiển đai hông | Cung cấp năng lượng di động, an toàn y sinh |
| **Mạch hạ áp** | **Module Buck DC-DC XL4005 (Dòng tải đỉnh 5A)** | Hộp điều khiển đai hông | Hạ áp từ 7,4V xuống 5V sạch cấp cho Orange Pi 5 Pro và 5V động lực cho Servo |
| **Phân bổ 2 cụm & Cáp nối** | **Chiều dài cáp: 50 cm** từ cẳng tay về đai hông | Cáp bẹ mềm bọc dù (~10–11 lõi) | Giảm 70% khối lượng trên tay (còn ~80–90g), chống mỏi và chống sụt cổ tay |


Theo chủ dự án, hai hạng mục chính còn cần mua là **3 cảm biến Flex** và **module camera**. ADS1115 đã được chủ dự án xác nhận có trong trao đổi trước. Không dùng lại dòng “ADS1115 chưa xác nhận” hoặc cấu hình 11 kênh trong bảng lịch sử phía dưới để lập danh sách mua hiện tại.

Thiết kế trong PDF final: 16 Velostat trên ngón + 2 ô tham chiếu + 3 Flex = **21 kênh**, dùng 2 MUX và ADS1115; 3 servo độc lập. Việc có đủ vật tư khác theo lời chủ dự án không thay cho xác nhận mã linh kiện, điện áp, dòng tải hoặc số lượng module khi chọn nguồn.

| Hạng mục còn cần mua | Thông tin cần có trước khi chọn mã |
|---|---|
| Flex ×3 | chiều dài vùng nhạy phù hợp đường uốn trên từng nẹp, giới hạn uốn, dải điện trở; hiệu chuẩn với thước góc ngoài |
| Module camera RGB | vị trí gá, khoảng cách camera–vùng thao tác, góc nhìn, khả năng khóa lấy nét/phơi sáng và tương thích bo/hệ điều hành; chưa chọn USB hay CSI |

**Bố trí đang thảo luận:** hộp pin và mạch trên dây đai hông, cảm biến và servo trên tay. Chưa chốt vị trí servo, vị trí mạch thu nhận, đường truyền hay cấu hình nguồn. Đề xuất của agent: hộp hông chứa pin/nguồn/Orange Pi; bo MUX–ADS1115–ESP32 nhỏ gần cổ/cẳng tay để giữ dây analog và I²C ngắn; truyền dữ liệu số về hông. Đây chưa phải cấu hình được chủ dự án chọn.

**Cần chủ dự án cung cấp:** mã/ảnh 3 servo; loại pin và mạch nguồn đang có; vị trí dự kiến đặt servo và camera. Không tự điền công suất/dòng định mức hoặc kết luận nguồn đủ tải khi chưa có những thông tin này.

## Bảng kiểm kê lịch sử — không phải trạng thái mua hiện tại

> **Nguồn:** lời khai của nhóm nghiên cứu trong đối thoại 2026-09-19. Agent **không kiểm kê vật lý** được — ô "xác nhận" dưới đây để nhóm nghiên cứu tự điền.
> File này **chỉ dùng để lập kế hoạch**, không phải bằng chứng trong báo cáo.
> **Cập nhật hiệu lực 2026-10-19:** AAN là mục tiêu chính; cơ cấu là servo cuốn dây câu cá trực tiếp trên tang. Hướng chức năng hiện tại là assisted flexion/extension → tự động chuyển AAN theo ngưỡng → tập gắp/di chuyển/đặt thìa bằng ba ngón; Flex theo dõi gập–duỗi, Velostat đo áp lực/tiếp xúc tương đối, camera theo dõi vật/đích/tác vụ. Orange Pi 5 Pro là máy tính thị giác dự kiến, chưa benchmark. Không cần KTV để chuyển mode. Các dòng BOM bên dưới là lịch sử và không tự xác nhận hiện trạng thiết bị. Tang, hồi/nhả, đo lực tham chiếu, ngưỡng và giới hạn an toàn còn mở. Không dùng Velostat để xác nhận Newton; 5 N đã rút. Xem `CURRENT_DESIGN_BASELINE.md`.

## 1. Thiết bị

| Món | Trạng thái | Cần cho | Xác nhận của trưởng nhóm (số lượng / tình trạng) |
|---|---|---|---|
| Velostat (film áp trở) | **Đã có** | GATE 0 → C: mọi sensing element | *[điền: mấy tấm, kích thước, lô]* |
| Cảm biến gập Flex ×3 (cái / trỏ / giữa) | **CHƯA CÓ — phải mua ở mốc 1** (chủ dự án xác nhận 2026-10-20) | cấu hình 11 kênh đã chọn = 3 Flex + 6 Velostat + 2 REF; Flex đo gập–duỗi và tư thế từng ngón, là đại lượng trong găng duy nhất cho GAP | *[điền: mã hàng, số lượng, giá, nơi mua]* |
| Băng đồng (copper tape) | **Đã có** | điện cực của sensing element | *[điền: độ dài]* |
| ESP32-S3 | **Đã có** | GATE 0 §3 (đo `R_max`, ENOB, `fps_meas`) + bring-up 12 kênh | *[điền: loại board — còn chân ADC1 tự do?]* |
| Orange Pi 5 Pro (RK3588) | **Đã có** (owner inventory 2026-09-29; re-check current condition before testing) | proposed host for spoon/target/task-state computer vision and visual-feedback pipeline; no claim of tested model/metric depth/latency | Earlier note says INT8/image processing was tried, but model, software, end-to-end latency and current configuration need traceable benchmark; do not treat as proof of current rehabilitation function |
| CD74HC4067 (MUX 16:1) | **Đã có — đã chạy thử** (chủ dự án xác nhận 2026-10-20) | GATE 0 §3 trở lên; linh kiện quyết định toàn bộ cấu hình 11 kênh đã chọn | *[điền: ngày chạy thử, kết quả quét từng kênh]* |
| DMM chính = FNIRSI 2C23T (10.000 count, DCV ±(0,5%+3), R ±(0,5%+3) theo datasheet) | **Đã có** | GATE 0: `R`/`V` gốc; C1.3–C1.9; M6 | trưởng nhóm 2026-09-29: chốt spec theo datasheet 2C23T; DMM rời chỉ làm máy phụ (đo đồng thời), không cần tra model |
| FNIRSI 2C23T: scope 2ch/10MHz/50MSa/s/20mV/div min + gen 1Hz–2MHz/0,1–3,3V | **Đã có** | C1.1 (chứng kiến) · M1 · M5/C1.10 · spec sheet E1–E4 · test chuỗi mV (qua chia áp) | spec đã xác minh 2026-09-29 → notebook M-checklist L1–L5 |
| Quả cân chuẩn (hoặc chai nước đã cân) | [Chưa xác định] | **lực chuẩn cho GATE 0** — thay được load cell ở giai đoạn tĩnh | *[điền]* |
| Máy in 3D + PLA/PETG + TPU | [Chưa xác định] | jig GATE 0, khung vách, phantom | *[điền: trường có phòng sáng tạo không — `A.5` ghi là có]* |
| Load cell + HX711 | [Chưa xác định] (mua sau) | GATE A/B/C: lực động khi ngón đang chuyển | *chưa cần cho GATE 0* |
| Khung đỡ + vít M5 + êcu hãm + lò xo | [Chưa xác định] | preload cơ khí (biến số `F_p`) | *[điền]* |
| INA333 + ADS1115 + MCP6001 + SHT30 + LSM6DS3 *(mới từ bản nộp 2026-09-26)* | [Chưa xác định] — **cập nhật 2026-10-20:** INA333 đã bỏ sau vòng lặp 2; MCP6001, SHT30, LSM6DS3 không còn trong kiến trúc hiện hành; riêng **ADS1115 vẫn chưa xác nhận** tình trạng dù toàn bộ chuỗi đo hiện hành phụ thuộc nó | chuỗi đo đã nộp (`CLM-HW-003`); kiến trúc hiện hành = cầu phân áp → CD74HC4067 → ADS1115 → ESP32-S3 | *[điền: ADS1115 đã có chưa, mấy module]* |
| Khung nhôm 2020 + trượt tuyến tính + vít me + phanh từ + servo Bowden *(rig AAN/RAL cũ — SUPERSEDED)* | [Chưa xác định] (mua sau) | Phương án rig cũ; chưa xác nhận khả năng tái dùng cho tang cuốn dây câu | *chưa cần cho GATE 0; thiết kế lại theo protocol 09* |
| Silicone y tế Shore A 25–30 *(phantom theo bản nộp)* | [Chưa xác định] (mua sau) | đúc phantom tay giả | *đối chiếu tài liệu mô mềm trước khi chốt độ cứng* |

**Ghi chú kỹ thuật quan trọng cho GATE 0:** lực chuẩn **không** cần load cell. Với mỗi khối lượng `m` đã cân, `F = m·g` là chuẩn cơ bản hơn lực kế lò xo
(không trễ, không cần hiệu chuẩn điện tử). Load cell + HX711 chỉ cần từ GATE A trở đi, lúc đã có chuyển động.

## 2. Quyền truy cập chuyên môn

**Có:** chị ruột của nhóm nghiên cứu là **kỹ thuật viên Vật lý trị liệu – Phục hồi chức năng, 10 năm kinh nghiệm**; đã xác nhận tính cấp thiết của đề tài
(`SRC-OWNER-2026-09-19-KTV10Y`, cùng chuỗi với `DEC-CLINICAL-001`).

| Được dùng cho [Đạt] | Không được dùng cho |
|---|---|
| Trả lời phiếu 10 câu `research/protocols/07` §5 (tần suất hẹn, số người bệnh/phòng, kỳ vọng về chỉ số) | **Làm đối tượng đo** — kể cả "chỉ 1 ngón, đo nhẹ, trong 5 phút" |
| Chốt **giao thức bài tập chuẩn**: thứ tự động tác, số lần lặp, thời gian nghỉ, cách đọc AROM/PROM | **Tuyển người bệnh** hoặc giới thiệu bệnh nhân để lấy dữ liệu |
| Phản biện bảng tải của rig E4/RAL và tính hợp lý của các nấc `RAL_min` | **Chứng nhận hiệu quả lâm sàng** — "KTV thấy hữu ích" là bằng chứng *nhu cầu* (Tầng 3), không phải bằng chứng *kết quả* |
| Đọc bản diễn giải chỉ số (EI/GAP/RAL) và chỉ ra chỗ **vô nghĩa về mặt lâm sàng** | Ký thay phê duyệt đạo đức; phê duyệt của một cá nhân **không** thay được IRB/SRC (`DEC-ETHICS-001` OPEN) |
| Góp ý câu chữ cho mục "đối tượng & phạm vi" và phần giới hạn | Xuất hiện trong đề tài như "đồng tác giả" nếu chỉ tham gia tư vấn (`DEC-ROLE-001`) |

**Cách dùng đúng mà vẫn hợp lệ:** mời phản biện **trên giấy** (gửi phiếu + 1 trang quy trình), lưu câu trả lời thành `research/reviews/2026-…-ktv-round3.md`.
Như vậy hồ sơ có một dòng mạnh mà vẫn trung thực: "**giao thức đo đã được một chuyên gia vật lý trị liệu – phục hồi chức năng phản biện**" — theo `DEC-ROLE-001` **không** kèm tên, không kèm số năm kinh nghiệm, không kèm quan hệ gia đình; và không có dòng nào phải giải trình trước hội đồng đạo đức.

## 3. Việc còn thiếu để GATE 0 chạy được **tuần này**
1. [ ] Chốt **9 ngưỡng** `research/protocols/08_gate0_execution_plan.md` §7 (việc duy nhất chặn đường).
2. [~] Điền §1 ở trên: **CD74HC4067 đã xác nhận** (đã có, đã chạy thử — chủ dự án 2026-10-20); **còn nợ** tình trạng ADS1115, 3 cảm biến gập Flex (đã biết: chưa có, phải mua), DMM và khối lượng chuẩn.
3. [ ] In/cắt jig cho 5 phần tử họ A + 1 cụm họ B (mẫu C đối chứng làm sau cũng được).
4. [ ] Chụp ảnh trang §7 đã chốt và dán vào header của file log đầu tiên (`research/bench/logs/`).
