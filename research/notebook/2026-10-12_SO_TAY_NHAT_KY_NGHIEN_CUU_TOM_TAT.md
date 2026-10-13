# Sổ tay nhật ký nghiên cứu (bản tóm tắt chắt lọc)

**Đề tài:** Nghiên cứu và phát triển găng tay hỗ trợ đánh giá, theo dõi và hỗ trợ vận động bàn tay
trong phục hồi chức năng sau đột quỵ (`DEC-TITLE-003`, 2026-10-11).
**Nhóm thực hiện:** Văn Ngọc Nhật Anh (11A2) + Nguyễn Duy Quân (12A1) — dự án tập thể (2 học sinh).
**Giáo viên hướng dẫn (GVHD):** Lê Công Long — THPT thị xã Quảng Trị.
**Căn cứ lập tài liệu:** Điều 14 Quy chế ban hành kèm Thông tư số 84/2026/TT-BGDĐT
("Nhật ký nghiên cứu, dữ liệu gốc và minh chứng quá trình thực hiện dự án").
**Ngày biên soạn bản tóm tắt này:** 2026-10-12.

---

## 0. Giải thích về tài liệu này — đọc trước khi dùng

1. **Đây là bản chắt lọc, không phải nhật ký gốc.** Nhật ký nghiên cứu đầy đủ của dự án nằm rải
   rác trong các tệp đã lưu vào hệ thống tài liệu dự án theo thời gian thực: `research/context/DECISION_LOG.md`
   (log quyết định có ngày tháng), `research/notebook/2026-09-29_measurability_M-checklist.md`
   (sổ tay đo lường), và `research/notebooklm_sync/experiments/01-06` (nhật ký thử nghiệm phần
   cứng thật). Bản này **gộp và rút gọn** các nguồn đó theo đúng 5 trường thông tin Điều 14
   khoản 1 yêu cầu: *thời gian — nội dung công việc — phương pháp thực hiện — kết quả từng giai
   đoạn — vai trò cụ thể của từng thành viên*. Các tệp gốc **vẫn giữ nguyên trong repo**, không bị
   xoá hay thay thế — đây chỉ là bản tổng hợp để nộp/lưu trữ dễ đọc hơn. Bản đầy đủ (8 tệp gốc,
   đã bỏ bớt thuật ngữ nội bộ về công cụ lưu trữ tài liệu để dễ đọc hơn, giữ nguyên nội dung
   chuyên môn) cũng đã được tải lên cùng thư mục Drive, trong thư mục con `Ho_so_day_du/`.
2. **Cột "Vai trò thành viên" chưa điền được.** Agent hỗ trợ biên soạn tài liệu này **không biết**
   và **không được suy diễn** ai trong hai bạn (An / Quân) trực tiếp làm phần việc nào ở từng mốc —
   đây là thông tin chỉ có nhóm mới xác nhận được, và theo Điều 16 khoản 2, việc phân vai trò cũng
   chính là thứ giám khảo dùng để đánh giá "mức độ tham gia thực chất". **Nhóm bắt buộc phải tự
   điền** cột này trước khi coi tài liệu là hợp lệ.
3. **Cột "Xác nhận GVHD" để trống chủ đích.** Điều 14 khoản 1 yêu cầu người hướng dẫn xác nhận
   *trực tiếp, định kỳ ít nhất 1 lần/tháng* — việc này không thể và không được làm thay bằng công
   cụ phần mềm. Thầy Lê Công Long cần ký (giấy hoặc chữ ký điện tử có giá trị tương đương) trực
   tiếp vào từng mốc, hoặc theo chu kỳ tháng mà quy chế của BTC/hệ thống quản lý nhật ký điện tử
   quy định cụ thể hơn (Điều 14 khoản 4 — BTC sẽ ra hướng dẫn mẫu riêng).
4. **Về Điều 15 (khai báo công nghệ số/AI):** tài liệu này **không** thực hiện việc khai báo đó.
   Theo đúng yêu cầu của chủ dự án, việc khai báo sử dụng công nghệ số/AI cho BTC sẽ do nhóm tự
   thực hiện riêng, không nằm trong phạm vi bản tóm tắt nhật ký này.
5. **Một số ngày tháng trong mục 10 (thử nghiệm phần cứng) chỉ được suy luận gián tiếp** từ nội
   dung kỹ thuật trùng khớp với 2 ảnh chụp thiết bị đo thật (oscilloscope 09/10, Serial Plotter
   11/10) — không phải do tệp gốc tự ghi ngày tháng tường minh. Các chỗ này được đánh dấu rõ
   **"(ngày suy luận — nhóm cần tự xác nhận lại)"**; đây là điểm nhóm cần xác nhận/sửa trước khi
   dùng vào hồ sơ chính thức, vì Điều 14 đòi hỏi "ghi nhận đầy đủ, liên tục" — không được phỏng đoán.

---

## 1. 2026-08-16 — Thiết lập quy trình lưu trữ nghiên cứu

- **Nội dung:** Khởi tạo kỷ luật ghi chép: mọi nguồn/công cụ bên thứ ba phải ghim phiên bản; mọi
  bối cảnh, tìm kiếm, luận điểm và ý kiến phản biện phải lưu vào sổ sách có theo dõi.
- **Phương pháp:** Lập `research/` làm thư mục sổ sách trung tâm (ledger nguồn, ledger luận điểm),
  quy định trong `AGENTS.md`.
- **Kết quả:** Có nơi lưu trữ có cấu trúc cho toàn bộ quá trình nghiên cứu từ đây về sau.
- **Vai trò thành viên:** ⟨nhóm tự điền⟩

## 2. 2026-08-25 → 2026-08-26 — Hai lần đổi hướng đề tài ban đầu

- **Nội dung công việc:** Thử hướng 1 "đệm khí thích ứng + AAC" → bỏ, chuyển hướng 2 "đế giày
  thông minh Edge-AI (3D-GRF & COP)" → tinh chỉnh thành "theo dõi động lực học dài hạn chống
  trôi" → sau đó bỏ tiếp, chuyển hướng 3 "theo dõi độ cứng mô bàn chân do loét bàn chân đái tháo
  đường (DFU)".
- **Phương pháp thực hiện:** Rà soát tài liệu tham khảo cho từng hướng, đánh giá theo khung GATE
  (tính mới, tính khả thi, tính hữu ích).
- **Kết quả từng giai đoạn:** Cả 2 hướng đều bị loại — hướng DFU bị dừng ở bước tiếp theo
  (xem mục 3) vì GATE 3 (tính hữu ích) yếu. Toàn bộ file cũ của các hướng bị xoá khỏi repo
  (ghi nhận trong lịch sử lưu trữ tài liệu dự án).
- **Vai trò thành viên:** ⟨nhóm tự điền⟩

## 3. 2026-08-28 — Chốt đề tài hiện tại + phỏng vấn thực địa + kiến trúc phần cứng v1

- **Nội dung công việc:**
  1. **PIVOT quyết định:** bỏ hướng DFU, chốt đề tài mới — "Găng tay cảm biến áp lực Velostat +
     TinyML INT8 theo dõi định lượng chức năng bàn tay sau đột quỵ tại nhà". Lý do bỏ DFU: thiếu
     bằng chứng RCT lâm sàng cho theo dõi dài hạn qua proxy độ cứng mô; khoảng trống nghiên cứu
     mới được xác nhận bởi hội thảo chuyên gia quốc tế (Remote Monitoring Spasticity 2024,
     Birmingham) và một nghiên cứu khác năm 2026.
  2. **Phỏng vấn thực địa lần 1** với kỹ thuật viên Vật lý trị liệu – Phục hồi chức năng (KTVVLTL-PHCN,
     người thân trong gia đình): xác nhận 3 điểm đau của bài toán — (a) các thang đo lâm sàng
     (FMA/ARAT/Box and Block) chỉ cho "ảnh chụp tại một thời điểm", không theo dõi liên tục; (b)
     khoảng giữa hai lần tái khám là "hộp đen" không biết bệnh nhân tập đúng hay không; (c) thiết
     bị tại nhà chỉ hữu ích nếu đủ ý nghĩa lâm sàng + đủ tin cậy + đơn giản + bổ sung (không thay
     thế) đánh giá của KTV.
  3. **Xác nhận độc lập thứ hai** từ chuyên gia PHCN (phcn-online.com): đề tài "đáng đặt chân và
     nghiên cứu".
  4. **Kiến trúc phần cứng v1 (bản nháp đầu):** Velostat + băng đồng (6 vùng: 5 ngón + lòng bàn
     tay) + găng in 3D + Arduino Mega 2560 + Orange Pi 5 Pro RK3588 (NPU INT8).
  5. **Nguyên lý cơ học:** khung cứng kiểu exoskeleton ép sát ngón tay; ngón tay chuyển động theo
     hướng X → đụng vách khung hướng X → tạo áp lực lên dải Velostat hướng X → ADC đọc lực → suy
     ra vector hướng X — khác với găng Velostat thông thường (đo lực tiếp xúc trực tiếp).
- **Phương pháp thực hiện:** Phỏng vấn trực tiếp 2 nguồn độc lập trong ngành; thiết kế dựa trên
  linh kiện sẵn có; đối chiếu GATE 3 trước khi quyết định pivot.
- **Kết quả:** Đề tài hiện tại được xác lập và **không đổi nữa kể từ đây** (các thay đổi sau này
  chỉ là đổi *tên gọi* và *phần cứng thu thập*, không đổi *đối tượng nghiên cứu*).
- **Vai trò thành viên:** ⟨nhóm tự điền — lưu ý: phỏng vấn KTVVLTL-PHCN do ai trực tiếp thực hiện,
  cần ghi rõ vì liên quan Điều 16 khoản 2⟩

## 4. 2026-09-13 — Chốt tên đề tài chính thức (bản đầu) + đổi toàn bộ kiến trúc thu thập tín hiệu

- **Nội dung công việc:**
  1. Chốt tên đề tài chính thức: *"Nghiên cứu và phát triển găng tay thông minh hỗ trợ đánh giá và
     theo dõi chức năng vận động bàn tay trong phục hồi chức năng sau đột quỵ"* (bỏ cụm "hệ thống…
     TinyML… giá thấp" vì đó là phương tiện, không phải đối tượng nghiên cứu).
  2. **Đổi vi điều khiển thu thập: Arduino Mega 2560 → ESP32-S3**, thêm **CD74HC4067** (MUX 16:1).
     Lý do: Mega chỉ có ADC 10-bit, cồng kềnh, không có truyền không dây, mức logic 5V buộc phải
     có bộ chuyển mức logic sang Orange Pi (3.3V); ESP32-S3 có ADC1 12-bit, 240 MHz, BLE 5, logic
     3.3V khớp trực tiếp. Đánh đổi phải ghi nhận: ADC ESP32-S3 kém tuyến tính hơn danh định → bắt
     buộc hiệu chuẩn ADC, chỉ dùng ADC1 (ADC2 xung đột Wi-Fi) → cần MUX vì số chân ADC ít.
  3. Chốt bố trí kênh 2 giai đoạn: Cấu hình 1 (12 kênh, bring-up + GATE 0/A) và Cấu hình 2 (24
     kênh, đọc vi sai hai vách đối diện mỗi khớp để lấy dấu gập/duỗi và triệt drift đồng pha).
  4. Chốt nguyên tắc: ngưỡng PASS/FAIL của mỗi GATE phải chốt **trước khi đo**, cấm chỉnh ngưỡng
     sau khi xem kết quả; GATE C (độ nhạy phát hiện thay đổi) là cổng sống còn.
  5. Chốt quy tắc ngôn ngữ báo cáo: dùng "suy luận hướng gập/duỗi" (không phải "đo góc khớp"),
     "giảm ảnh hưởng drift" (không phải "loại bỏ drift"), "găng tay đánh giá và theo dõi" (không
     phải robot/găng tập phục hồi chức năng).
  6. Đề nghị đổi tên dự án trên hệ thống lưu trữ tài liệu cho khớp đề tài (chưa thực hiện được
     do quyền truy cập của phiên làm việc lúc đó).
- **Phương pháp thực hiện:** Phân tích đánh đổi kỹ thuật (ADC bit-depth, logic level, băng thông
  I2C/kênh) kết hợp quyết định của chủ dự án.
- **Kết quả:** Kiến trúc thu thập tín hiệu (ESP32-S3 + CD74HC4067 + ADS1115 + INA333) được chốt và
  **giữ nguyên tới nay** (10/2026); đây là nền tảng cho mọi thử nghiệm phần cứng thật ở mục 10–11.
- **Vai trò thành viên:** ⟨nhóm tự điền⟩

## 5. 2026-09-19 — Rà soát tính mới (novelty), chốt phạm vi AAN/AAT, nộp đề cương lần 1

- **Nội dung công việc:**
  1. **Rà soát prior art vòng 1** cho nguyên lý "vách áp-điện-trở → hướng chuyển động" — phát hiện
     nguyên lý này đã có trong y văn (Sensors 2015); hạ mức tự nhận định từ "nguyên lý mới" xuống
     "cải tiến cấu hình + phương pháp lập luận".
  2. **Quyết định phạm vi AAT (tập chủ động có trợ lực):** sau phản biện ("phân tích kiểu IEEE
     journal thì học sinh không có cửa"), nhóm chốt phương án **E4 (rig phantom + RAL) + E5 (1
     servo kéo phantom) + E6 (tầng kê đơn phần mềm)** — không có lực nào tác động lên người thật ở
     giai đoạn này nên **không cần IRB**; hoãn viết script, giai đoạn này chỉ làm cơ sở lý thuyết.
  3. Đối chiếu với dự án tham khảo ISEF 2025 ROBO065T (giải Tư, THPT thị xã Quảng Trị) để xác nhận
     chuẩn novelty của cuộc thi là "tầng bài toán + tái tổ hợp + bằng chứng tự làm", không phải
     "nguyên lý vật lý mới" — quyết định không trích dự án này vào hồ sơ nộp, chỉ lưu nội bộ.
  4. Chốt kế hoạch chạy toàn bộ 7 cổng GATE 0→F (không cắt bớt phần INT8 hay tái dựng 3D) do chủ
     dự án xác nhận "đủ thời gian hết"; không có mốc nộp cố định tại thời điểm này.
  5. Xác nhận nguồn lực sẵn có: Velostat, Orange Pi 5 Pro, ESP32-S3, đồng tự dính — không cần mua
     board ở lớp 0–1.
  6. Chốt khoá pha lý thuyết: chưa viết firmware/script phân tích (áp dụng cho phần việc do agent
     hỗ trợ; không ràng buộc việc tự tay chủ dự án làm — xem mục 10).
  7. Hoàn thiện và nộp đề cương lần 1 cho trường: `docs/DE_CUONG_NOP_TRUONG.md` → xuất bản
     `docs/DE_CUONG.pdf` (nộp 2026-09-26).
  8. Chốt chính sách không nêu danh tính người được tham khảo chuyên môn trong hồ sơ nộp.
- **Phương pháp thực hiện:** Tìm kiếm tài liệu học thuật có hệ thống, đối chiếu dự án tham chiếu đã
  đạt giải, phỏng vấn/trao đổi trực tiếp với chủ dự án để chốt phạm vi.
- **Kết quả:** Phạm vi kỹ thuật AAN/AAT được giới hạn rõ ràng (chỉ trên giàn đo + mô hình tay giả,
  không tác động lực lên người thật — ranh giới an toàn này **không đổi xuyên suốt dự án**); đề
  cương đầu tiên được nộp trường ngày 2026-09-26.
- **Vai trò thành viên:** ⟨nhóm tự điền⟩

## 6. 2026-09-27 — Đồng bộ lại với bản đề cương đã nộp

- **Nội dung công việc:** Đối chiếu toàn bộ tài liệu repo với bản `docs/DE_CUONG.pdf` (nộp
  2026-09-26) — ghi nhận đội hình (An 11A2 + Quân 12A1, GVHD Lê Công Long, THPT thị xã Quảng Trị,
  lĩnh vực Hệ thống nhúng, mốc 09/2026–01/2027); đề xuất cập nhật chuỗi đo đã nộp (Velostat → cầu
  vi sai hai vách R_ref=10kΩ → INA333 G=10 → ADS1115 16-bit → ESP32-S3 → BLE → Orange Pi); đề xuất
  bộ ngưỡng đo M1–M6 + C1.1–C1.10 thay cho ngưỡng cũ; đề xuất phạm vi 3 ngón (cái/trỏ/giữa) thay
  vì lộ trình 5 ngón trước đó.
- **Phương pháp thực hiện:** So khớp từng mục PDF đã nộp với tài liệu kỹ thuật nội bộ, liệt kê các
  điểm chưa khớp (I1–I8) để chủ dự án duyệt.
- **Kết quả:** Một số mục còn ở trạng thái **ĐỀ XUẤT, chờ chủ dự án duyệt** tại thời điểm ghi nhật
  ký này — nhóm cần tự kiểm tra trạng thái mới nhất trong `DECISION_LOG.md` trước khi dùng.
- **Vai trò thành viên:** ⟨nhóm tự điền⟩

## 7. 2026-09-29 — Chốt bộ đồ nghề đo lường + rà soát khả năng đo + ngân sách

- **Nội dung công việc:**
  1. Chốt bộ đồ nghề đo: đồng hồ vạn năng (DMM) rời + máy hiện sóng/máy phát xung/DMM 3-trong-1
     **FNIRSI 2C23T** (scope 2 kênh/10MHz/50MSa/s, thang đứng tối thiểu 20mV/div; máy phát
     1Hz–2MHz/0,1–3,3V; DMM 10.000 count) + load cell 5kg (thiếu module HX711, cần mua).
  2. Rà soát từng chỉ số đo M-01 đến M-27 xem đo được bằng bộ đồ nghề này hay không — **kết luận:
     M1–M6 và C1.1–C1.10 đều đo được**, không loại chỉ số nào, chỉ loại các *câu khẳng định*
     (claim) không có cơ sở đo (vd. "INT8 < 15ms", chẩn đoán MAS, AAN tác động lên người thật,
     "triệt để loại bỏ drift", tần số lấy mẫu danh định sai, trích dẫn không có DOI...).
  3. Chốt trần ngân sách vận hành nội bộ (E2E) **dưới 10 triệu đồng** — BOM nháp ước tính
     5,5–8,5 triệu (Orange Pi đã có sẵn ở trường). **Quyết định: số liệu này chỉ ghi vào sổ tay,
     không đưa vào báo cáo chính thức** (báo cáo giữ nguyên câu "thiết bị đeo dưới 1,5 triệu" +
     "trạm dùng chung").
  4. Danh sách mua sắm ưu tiên P0: HX711, ADS1115/INA333 chính hãng, SHT30, cân túi 0,01g + quả
     cân chuẩn, thước đo góc, ẩm-nhiệt kế, lò xo, vít, nhựa in PETG.
- **Phương pháp thực hiện:** Đối chiếu thông số kỹ thuật thiết bị đo (độ phân giải, dải đo, sai số)
  với từng ngưỡng GATE cần đo; tính toán ngân sách theo hạng mục.
- **Kết quả:** Toàn bộ 33 chỉ số (M+C) được xác nhận khả thi về mặt đo lường với thiết bị hiện có;
  chi tiết đầy đủ lưu tại `research/notebook/2026-09-29_measurability_M-checklist.md`.
- **Vai trò thành viên:** ⟨nhóm tự điền⟩

## 8. 2026-10-09 (ngày suy luận — nhóm cần tự xác nhận lại) — Thử nghiệm thật #1: hiệu chỉnh tầng tiền khuếch đại INA333

> Nguồn: `research/notebooklm_sync/experiments/05_...md` (nội dung) + ảnh chụp oscilloscope FNIRSI
> 2C23T do chủ dự án gửi qua chat (owner ghi nhận ngày đo là 09/10/2026) — số liệu `G≈6,5×` trong
> note 05 khớp gần như tuyệt đối với số đo trong ảnh (`G≈6,46×`), nên hai nguồn được gộp vào 1 mục.
> **Đây là dữ liệu thật do chủ dự án tự đo ngoài phạm vi agent**, xác nhận qua `DEC-PHASE-002`.

- **Nội dung công việc:** Đo kiểm và xử lý lỗi tầng tiền khuếch đại INA333 (module CJMCU-333) bằng
  oscilloscope FNIRSI 2C23T.
- **Phương pháp thực hiện:**
  1. Phát hiện lỗi ban đầu: tín hiệu ra bị suy hao (Vpp vào 0,25V → ra chỉ 0,16V, G≈0,64), méo nấc
     bậc thang, bẹp đáy (xén âm xuống −0,85V); đồng thời có hiện tượng sập nguồn tức thời khi kẹp
     mass oscilloscope (nghi do đoản mạch vòng mass — ground loop — giữa mass BNC của máy đo và
     điểm lệch thế trên mạch).
  2. Xác định nguyên nhân gốc: INA333 chạy nguồn đơn 3,3V/GND, không xử lý được điện áp âm; tín
     hiệu AC từ máy phát xung tụt dưới 0V kích hoạt diode bảo vệ ESD nội, làm tắc nghẽn tầng vi sai.
  3. Khắc phục: (a) thêm tụ chặn AC 0,47µF ngăn dòng một chiều rò từ nguồn phát; (b) ghim điện áp
     phân cực DC tĩnh V_REF ≈ 1,5–1,65V (virtual ground) vào ngõ vào vi sai; (c) tinh chỉnh biến
     trở SMD R_G (loại xoay 270°).
- **Kết quả từng giai đoạn:** Đạt hệ số khuếch đại **G ≈ 6,46–6,5 lần** (Vpp từ 0,24V lên 1,55V,
  Vmax 1,62V, Vmin 0,06V — cách sàn GND an toàn, sóng sin tròn đều, không còn xén ngọn). Khi tắt
  nguồn phát AC, V_OUT giữ cố định ở ≈1,500mV đúng theo mốc tĩnh thiết kế.
  **Lưu ý trung thực (chưa xử lý, cần nhóm quyết định):** giá trị đo được G≈6,5 thấp hơn khoảng 35%
  so với mục tiêu thiết kế ghi trong `docs/04_Hardware_Architecture.md` ("INA333 G = 10,
  R_ref = 10kΩ") — do R_G là biến trở chỉnh tay (không phải điện trở cố định 10kΩ như dự kiến) để
  giải quyết lỗi xén nguồn đơn. Nhóm cần chọn: (1) chấp nhận G≈6,5 làm giá trị thật, cập nhật lại
  tài liệu + ngân sách độ phân giải; hoặc (2) chỉnh lại biến trở để kéo G lên gần 10 rồi đo lại.
- **Dữ liệu gốc/minh chứng:** 1 ảnh chụp màn hình oscilloscope 2C23T (do chủ dự án gửi qua chat,
  **chưa có bản lưu ngoài chat** — cần tự tải lên Google Drive, xem mục "Việc cần làm" cuối tài liệu).
- **Vai trò thành viên:** ⟨nhóm tự điền⟩ — **Xác nhận GVHD:** ______________________ (ngày ___/___/2026)

## 9. 2026-10-11 (ngày đo xác nhận cho ảnh Serial Plotter; các mục khác trong ngày này được hệ thống lưu trữ tài liệu dự án ghi nhận đúng ngày) — Thử nghiệm thật #2 + loạt quyết định quan trọng

### 9.1. Thử nghiệm thật: tích hợp ADC 16-bit ADS1115 + quét đa kênh CD74HC4067

> Nguồn: `research/notebooklm_sync/experiments/01,02,03,04_...md` + ảnh Serial Plotter (owner xác
> nhận ngày đo 11/10/2026). Ngày chính xác của riêng từng ghi chú 01–04 (phân biệt với ngày
> công cụ đồng bộ vào repo) **chưa được xác nhận độc lập** — chỉ có ảnh Serial Plotter là có ngày
> đo tường minh do chủ dự án xác nhận; 01–04 được xếp vào cùng mốc vì nội dung kỹ thuật nối tiếp
> trực tiếp mục 8 và khớp số liệu với ảnh này. **(ngày suy luận — nhóm cần tự xác nhận lại)**

- **Nội dung công việc:** Ghép nối ADS1115 (ADC 16-bit) đọc ngõ ra INA333 qua ESP32-S3, mở rộng
  đa kênh bằng CD74HC4067 (MUX 16:1); đấu nối MUX kênh C0 = máy phát sóng sine 51Hz/duty 99/amp
  2,1 (đơn vị cài đặt máy, chưa chắc là giá trị thực tại điểm đo), C1 = một nguồn áp tĩnh
  "khoảng 1,5 vôn mấy" (chủ dự án không nhớ chính xác), C2 = GND.
- **Phương pháp thực hiện:**
  1. Cấu hình đọc kênh đơn A0, dùng Continuous Conversion Mode (860 SPS) + ngắt phần cứng ALRT
     trên GPIO10 để loại bỏ jitter/rớt mẫu khi đọc qua I2C 400kHz.
  2. Điều khiển chọn kênh CD74HC4067 bằng 4 chân GPIO (S0–S3), chèn `delayMicroseconds(120)` sau
     mỗi lần chuyển kênh để xả điện dung ký sinh, tránh "nhớ áp" giữa các kênh.
  3. Quan sát 3 kênh trên Serial Plotter: kênh nối GND (phẳng gần 0), kênh nối nguồn tĩnh
     (phẳng cao ~3.0–3.3 nghìn đơn vị), kênh nối máy phát sóng (dao động tuần hoàn dạng
     răng cưa/tam giác do nội suy tuyến tính giữa các điểm quét rời rạc).
- **Kết quả từng giai đoạn:**
  - Bộ dồn kênh CD74HC4067 hoạt động đúng, **không phát hiện rò/nhiễu xuyên kênh (crosstalk)**
    giữa các kênh có chênh lệch điện áp lớn — kết luận này lặp lại nhất quán ở cả 3 lần đo riêng
    biệt (notes 01/02/03) và ở ảnh Serial Plotter mới nhất.
  - "Sóng tam giác" quan sát được trên Serial Plotter được xác định là hiện tượng hiển thị
    (nội suy tuyến tính giữa các điểm quét tuần tự qua 4 kênh), **không phải nhiễu phần cứng thật**
    — không ảnh hưởng tới ứng dụng thực tế vì tín hiệu Velostat biến thiên chậm (0–3Hz).
  - **Hai nghi vấn chưa xử lý (nhóm cần xác minh trước khi coi đây là bằng chứng chính thức):**
    (1) đơn vị trục Y của Serial Plotter là mV đã quy đổi trong firmware hay raw ADC count —
    nghi là mV vì độ lớn khớp với số liệu mV của note 02, nhưng chưa được xác nhận; (2) nếu là mV,
    giá trị kênh C1 đo được (~3,2–3,3V) không khớp với nguồn "~1,5V" mà chủ dự án nhớ — gần sát
    mức nguồn VCC 3,3V, nghi vấn dây đo có thể đang nổi (floating) hoặc chạm nhầm điểm khác.
  - Thiết kế phần mềm Auto-Tare (hiệu chỉnh mốc 0 tự động: lấy trung bình 100 mẫu sau 500ms ổn
    định mạch, trừ baseline khỏi mỗi phép đo tiếp theo) đã được mô tả xong, chưa xác nhận đã chạy
    thử nghiệm thật hay mới là thiết kế trên giấy — **nhóm cần tự xác nhận**.
- **Dữ liệu gốc/minh chứng:** 1 ảnh chụp Serial Plotter (do chủ dự án gửi qua chat, **chưa có bản
  lưu ngoài chat** — cần tự tải lên Drive).
- **Vai trò thành viên:** ⟨nhóm tự điền⟩ — **Xác nhận GVHD:** ______________________ (ngày ___/___/2026)

### 9.2. Các quyết định/bổ sung luận điểm trong ngày 2026-10-11

- **Đồng bộ đề cương mới:** công nhận `de_cuong/DE_CUONG_NGHIEN_CUU.pdf` (tạo 2026-10-03, có thêm
  Mục 10 về AAN + RAL trên giàn đo + phantom) là bản đề cương kỹ thuật mới nhất; bản
  `docs/DE_CUONG.pdf` (nộp trường 26/09) **vẫn là bản đã nộp chính thức** cho tới khi nộp lại.
- **Nâng AAN (Assist-as-Needed) thành trụ cột kỹ thuật thứ 4** của đề tài (ngang hàng với mảng
  cảm biến vi sai hai vách, bộ ba chỉ số EI/GAP/RAL, lớp tự kiểm chuẩn hai vòng lặp) — cơ chế: lò
  xo trợ giúp thụ động chia nấc (20–120g) + 1 servo qua khớp truyền lực 4 khâu, công thức
  `F_assist(t) = max(0, F_target(t) − F_phantom(t))`, `F_max ≤ 5N`, `t_delay = 1,2s`.
  **Ranh giới an toàn không đổi:** AAN chỉ chạy trên giàn đo + mô hình tay giả silicone, **không
  bao giờ** tác động lực lên ngón tay người thật kể cả tình nguyện viên khỏe mạnh.
- **Ghi nhận chính thức việc thử nghiệm phần cứng thật đã xảy ra** (mục 8–9.1 ở trên): chủ dự án
  xác nhận "đã đo thật" trên breadboard; dữ liệu này **chưa đạt chuẩn GATE 0 chính thức** (còn
  thiếu `session_manifest.csv`/`perturbation_log.csv`/`reference_check.csv` theo quy trình nội bộ
  `protocols/08a`) nên **chưa được dùng làm bằng chứng GATE 0 trong báo cáo nộp**.
- **Chốt tên hiển thị đề tài (bản hiện hành):** *"Nghiên cứu và phát triển găng tay hỗ trợ đánh
  giá, theo dõi và hỗ trợ vận động bàn tay trong phục hồi chức năng sau đột quỵ"* — thay cho tên
  2026-09-13 (bỏ "thông minh"; đổi "đánh giá và theo dõi chức năng vận động" → "đánh giá, theo dõi
  và hỗ trợ vận động"). **Tên này không hồi tố** vào các hồ sơ đã nộp trước đó (vẫn dùng tên cũ).
- **Bổ sung cơ sở lý thuyết thần kinh học:** thêm bản đồ vỏ não vận động/cảm giác (*motor/sensory
  homunculus*, Penfield & Boldrey 1937; mô hình hiện đại hơn — Gordon et al., *Nature* 2023) để
  giải thích vì sao đề tài chọn bàn tay làm đối tượng nghiên cứu. **Rào chắn bắt buộc:** cấm suy
  rộng thành việc đề tài tự đo/chứng minh hoạt động não bộ (đề tài không có EEG/fNIRS/TMS/fMRI).
- **Mở rộng luận điểm Velostat vs sEMG thành 5 trục so sánh** (chi phí, so với các cảm biến khác
  ngoài sEMG, hạn chế vật liệu đã biết của Velostat, độ tin cậy sEMG ở nhóm đột quỵ, tiền lệ ổn
  định của họ FSR/piezoresistive) — kèm rào chắn cấm tuyên bố "đầu tiên dùng FSR cho AAN" (đã có
  NASA RoboGlove, Bioservo SEM Glove).
- **Vai trò thành viên:** ⟨nhóm tự điền⟩

## 10b. 2026-10-12 (owner báo cáo qua chat; ngày in thử thật từng mech chưa xác nhận chính xác) — Thử nghiệm và loại bỏ các phương án cơ cấu đóng/mở nẹp ngón tay (Mech 1 → Mech 9)

> Nguồn: chủ dự án tường thuật qua chat quá trình thiết kế/in thử đã thực hiện trên máy tính cá
> nhân (ngoài phạm vi agent), kèm bảng so sánh và trích dẫn trực tiếp lời chủ dự án trong từng lần
> in thử. Toàn văn chi tiết: `3d_model/custom_exo/fixation_mechanisms_benchmark/README.md`.

- **Nội dung công việc:** Thiết kế và in thử thực tế trên máy in 3D **9 phương án cơ cấu khác
  nhau** để đóng/mở và giữ chặt vỏ nẹp quanh **một đốt ngón tay** (bài toán khác với bản lề nối
  giữa các đốt đã chốt trước đó ở `docs/06`): cần cơ cấu nào để bệnh nhân (có thể yếu/run tay) tự
  đeo vào và tháo ra được bằng một tay, vẫn giữ đủ chặt cho cảm biến áp lực có tiếp xúc ổn định.
- **Phương pháp thực hiện:** Thiết kế CAD từng phương án (vòng kẹp lò xo hở miệng, khóa trượt mộng
  đuôi én, dây đai Velcro, chốt ngang rời, khóa cài đỉnh mu ngón, dải đai răng cóc, bản lề kép
  thanh đòn, khóa bấm ngàm đực/lỗ cái), in thử thực tế từng phương án, quan sát trực tiếp lỗi/nhược
  điểm trên vật in rồi loại dần.
- **Kết quả từng giai đoạn:**
  - **8 phương án đầu (Mech 1–8) đều bị loại** vì các lý do quan sát thực tế trên vật in: lực kẹp
    yếu/nhựa giãn (Mech 1), khó đeo/tháo một tay (Mech 2), dây dán bai dão khó sát khuẩn (Mech 3),
    chi tiết rời dễ rơi với người run tay (Mech 4), xung đột vị trí dây cáp (Mech 5), dải đai mỏi
    gãy khi uốn lặp lại (Mech 6), kết cấu cồng kềnh nhiều khớp nhỏ (Mech 7), và đặc biệt Mech 8
    (khóa bấm ngàm) phải **bẻ cong nhựa mỗi lần mở** → mỏi vật liệu, giảm tuổi thọ — đây là lý do
    trực tiếp dẫn tới đổi hẳn nguyên lý thiết kế.
  - Riêng Mech 8 đã trải qua **5 lần in thử và tinh chỉnh liên tiếp** (răng quá nhỏ/dễ trượt → vẫn
    dễ tuột khi giật mạnh → hở viền lỏng khớp → lỗ cái quá chật → cuối cùng đóng chặt nhưng mở khó,
    phải bẻ cong nhựa) trước khi quyết định đổi hẳn nguyên lý ở Mech 9.
  - **Mech 9 (Double-Hinge Toggle Clasp) là phương án hiện tại triển vọng nhất**: hai ngàm đực nhô
    cao khép khít vào nhau, một quai gông chữ U gắn trên bản lề thứ 2 xoay xuống ngậm trọn hai
    ngàm — đóng/mở hoàn toàn bằng khớp xoay, kỳ vọng không còn phải bẻ cong nhựa như Mech 8. Ý
    tưởng nguyên lý do chính chủ dự án đề xuất. Khi dựng mô hình CAD đã gặp và xử lý xong 2 lỗi kỹ
    thuật: (1) một đa giác 2D tự giao cắt làm phần mềm dựng hình xóa mất thân quai kẹp; (2) một
    lệnh khoét rãnh vô tình cắt rỗng luôn trục bản lề chính khiến vật in rời ra khi nhấc lên.
  - **Lưu ý trung thực (chưa xử lý, cần nhóm/owner xác nhận):** Mech 9 **chưa có file CAD trong
    repo này** (chỉ tồn tại trên máy tính cá nhân của chủ dự án tại thời điểm ghi nhận), **chưa
    được xác nhận đã in thử thực tế**, và **chưa có số liệu kiểm tra độ bền qua nhiều chu kỳ
    đóng/mở** — các mô tả "tuổi thọ vĩnh cửu"/"đóng mở hoàn toàn bằng khớp xoay" là kỳ vọng thiết
    kế, chưa phải kết quả đã đo. Quan hệ giữa bộ thử nghiệm này với cơ cấu "Khớp Bấm Ngàm Bên Hông"
    đã chốt trước đó cho bản lề liên-đốt (`docs/06` §2.5) cũng **chưa được xác nhận rõ** — có thể
    là hai nhánh thiết kế song song chưa hợp nhất.
- **Dữ liệu gốc/minh chứng:** File CAD Mech 1–8 (`.step`/`.stl`) đã có trong
  `3d_model/custom_exo/fixation_mechanisms_benchmark/`. **Mech 9 chưa có file trong repo.** Chưa có
  ảnh/video minh chứng cho bất kỳ lần in thử nào của cả 9 phương án — nếu còn giữ, nhóm nên tải lên
  để làm minh chứng trực quan (tương tự ảnh oscilloscope/Serial Plotter ở mục 8–9).
- **Vai trò thành viên:** ⟨nhóm tự điền⟩ — **Xác nhận GVHD:** ______________________ (ngày ___/___/2026)

## 10. Việc cần làm tiếp (tổng hợp từ tất cả các mục trên, owner/nhóm quyết định — agent không tự chọn hướng)

1. Điền cột "Vai trò thành viên" cho từng mục 1–9 (bắt buộc theo Điều 14 khoản 1 — dự án tập thể).
2. GVHD Lê Công Long xác nhận trực tiếp (ký) vào nhật ký này theo đúng chu kỳ tối thiểu 1 lần/tháng
   (Điều 14 khoản 1) — có thể ký theo từng mốc ngày hoặc theo hướng dẫn hệ thống nhật ký điện tử
   thống nhất của BTC khi được ban hành (Điều 14 khoản 4).
3. Xác nhận/sửa các ngày đánh dấu "(ngày suy luận — nhóm cần tự xác nhận lại)" ở mục 8–9.1 bằng
   ngày thật ghi trong sổ tay viết tay/điện thoại/lịch sử ảnh của nhóm.
4. Tự tải 2 ảnh chụp minh chứng (oscilloscope 2C23T 09/10, Serial Plotter 11/10) lên Google Drive
   (`02_Hinh_anh_2C23T/` và `03_Serial_Plotter_exports/` trong folder đã tạo trên Drive) — agent
   không thể copy file ảnh chat vào Drive thay nhóm.
5. Xử lý 3 câu hỏi mở về kỹ thuật nêu ở mục 8–9.1: (a) đơn vị trục Y Serial Plotter (mV hay raw
   ADC count); (b) giá trị kênh C1 không khớp kỳ vọng; (c) chênh lệch G≈6,5 đo được vs G=10 thiết
   kế ban đầu.
6. Khi đã rõ mục 3 và 5, chính thức hoá số liệu bring-up thành log GATE 0 hợp lệ trong
   `research/bench/logs/` theo đúng schema `session_manifest.csv`/`perturbation_log.csv`/
   `reference_check.csv` (mỗi ngày đo một `bench_session_id` riêng) — thư mục này hiện vẫn phải
   giữ rỗng cho tới khi đủ điều kiện.
7. Việc khai báo sử dụng công nghệ số/trí tuệ nhân tạo theo Điều 15 Quy chế — **nhóm tự thực hiện
   riêng, không nằm trong phạm vi tài liệu này.**
8. Các mục "PROPOSED, chờ chủ dự án duyệt" còn tồn đọng tính tới 2026-10-11 (xem danh sách đầy đủ
   và cập nhật mới nhất tại `research/context/DECISION_LOG.md` mục "Open decisions"): chốt ngưỡng
   GATE 0 cuối cùng, duyệt bảng phân biệt tính mới `docs/05` §4, xác nhận bản đề cương nào sẽ dùng
   để nộp lại, xác nhận đổi cảm biến nhiệt-ẩm SHT30 → AHT20 là chủ đích hay lỗi đánh máy, và việc
   tra cứu bằng sáng chế theo IPC một cách có hệ thống (vẫn còn nợ từ 2026-09-19).
9. Xuất file CAD Mech 9 (cơ cấu đóng/mở nẹp ngón tay, mục 10b) từ máy tính cá nhân vào repo, in thử
   thực tế và kiểm tra độ bền qua nhiều chu kỳ đóng/mở trước khi coi là thiết kế chính thức; xác
   nhận quan hệ giữa bộ thử nghiệm này với cơ cấu bản lề liên-đốt đã chốt ở `docs/06`.
