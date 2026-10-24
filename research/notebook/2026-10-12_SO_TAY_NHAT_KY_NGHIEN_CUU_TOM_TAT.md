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
2. **Cột "Vai trò thành viên":** Để đảm bảo tính trung thực theo quy định về đánh giá mức độ tham gia thực chất của từng thành viên, nhóm tác giả trực tiếp phân công và ghi nhận vai trò cụ thể tại từng buổi làm việc.
3. **Cột "Xác nhận GVHD" để trống chủ đích.** Điều 14 khoản 1 yêu cầu người hướng dẫn xác nhận
   *trực tiếp, định kỳ ít nhất 1 lần/tháng* — việc này không thể và không được làm thay bằng công
   cụ phần mềm. Thầy Lê Công Long cần ký (giấy hoặc chữ ký điện tử có giá trị tương đương) trực
   tiếp vào từng mốc, hoặc theo chu kỳ tháng mà quy chế của BTC/hệ thống quản lý nhật ký điện tử
   quy định cụ thể hơn (Điều 14 khoản 4 — BTC sẽ ra hướng dẫn mẫu riêng).
4. **Về Điều 15 (khai báo công nghệ số/AI):** tài liệu này **không** thực hiện việc khai báo đó.
   Theo đúng yêu cầu của nhóm nghiên cứu, việc khai báo sử dụng công nghệ số/AI cho BTC sẽ do nhóm tự
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
  quy định trong quy chế quản lý dữ liệu thực nghiệm.
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
  I2C/kênh) kết hợp quyết định của nhóm nghiên cứu.
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
  6. Chốt khoá pha lý thuyết: chưa viết firmware/script phân tích trong giai đoạn đề cương;
     ưu tiên hoàn thiện mạch phần cứng và đo kiểm thực tế trước (xem mục 10).
  7. Hoàn thiện và nộp đề cương lần 1 cho trường: `docs/DE_CUONG_NOP_TRUONG.md` → xuất bản
     `docs/DE_CUONG.pdf` (nộp 2026-09-26).
  8. Chốt chính sách không nêu danh tính người được tham khảo chuyên môn trong hồ sơ nộp.
- **Phương pháp thực hiện:** Tìm kiếm tài liệu học thuật có hệ thống, đối chiếu dự án tham chiếu đã
  đạt giải, phỏng vấn/trao đổi trực tiếp với nhóm nghiên cứu để chốt phạm vi.
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
  điểm chưa khớp (I1–I8) để nhóm nghiên cứu duyệt.
- **Kết quả:** Một số mục còn ở trạng thái **ĐỀ XUẤT, chờ nhóm nghiên cứu duyệt** tại thời điểm ghi nhật
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
> 2C23T do nhóm nghiên cứu gửi qua chat (trưởng nhóm ghi nhận ngày đo là 09/10/2026) — số liệu `G≈6,5×` trong
> note 05 khớp gần như tuyệt đối với số đo trong ảnh (`G≈6,46×`), nên hai nguồn được gộp vào 1 mục.
> **Đây là dữ liệu thật do nhóm nghiên cứu trực tiếp đo kiểm trên bàn thí nghiệm**, xác nhận qua `DEC-PHASE-002`.

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
- **Dữ liệu gốc/minh chứng:** 1 ảnh chụp màn hình oscilloscope 2C23T (do nhóm nghiên cứu gửi qua chat,
  **chưa có bản lưu ngoài chat** — cần tự tải lên Google Drive, xem mục "Việc cần làm" cuối tài liệu).
- **Vai trò thành viên:** ⟨nhóm tự điền⟩ — **Xác nhận GVHD:** ______________________ (ngày ___/___/2026)

## 9. 2026-10-11 (ngày đo xác nhận cho ảnh Serial Plotter; các mục khác trong ngày này được hệ thống lưu trữ tài liệu dự án ghi nhận đúng ngày) — Thử nghiệm thật #2 + loạt quyết định quan trọng

### 9.1. Thử nghiệm thật: tích hợp ADC 16-bit ADS1115 + quét đa kênh CD74HC4067

> Nguồn: `research/notebooklm_sync/experiments/01,02,03,04_...md` + ảnh Serial Plotter (trưởng nhóm xác
> nhận ngày đo 11/10/2026). Ngày chính xác của riêng từng ghi chú 01–04 (phân biệt với ngày
> công cụ đồng bộ vào repo) **chưa được xác nhận độc lập** — chỉ có ảnh Serial Plotter là có ngày
> đo tường minh do nhóm nghiên cứu xác nhận; 01–04 được xếp vào cùng mốc vì nội dung kỹ thuật nối tiếp
> trực tiếp mục 8 và khớp số liệu với ảnh này. **(ngày suy luận — nhóm cần tự xác nhận lại)**

- **Nội dung công việc:** Ghép nối ADS1115 (ADC 16-bit) đọc ngõ ra INA333 qua ESP32-S3, mở rộng
  đa kênh bằng CD74HC4067 (MUX 16:1); đấu nối MUX kênh C0 = máy phát sóng sine 51Hz/duty 99/amp
  2,1 (đơn vị cài đặt máy, chưa chắc là giá trị thực tại điểm đo), C1 = một nguồn áp tĩnh
  "khoảng 1,5 vôn mấy" (nhóm nghiên cứu không nhớ chính xác), C2 = GND.
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
    giá trị kênh C1 đo được (~3,2–3,3V) không khớp với nguồn "~1,5V" mà nhóm nghiên cứu nhớ — gần sát
    mức nguồn VCC 3,3V, nghi vấn dây đo có thể đang nổi (floating) hoặc chạm nhầm điểm khác.
  - Thiết kế phần mềm Auto-Tare (hiệu chỉnh mốc 0 tự động: lấy trung bình 100 mẫu sau 500ms ổn
    định mạch, trừ baseline khỏi mỗi phép đo tiếp theo) đã được mô tả xong, chưa xác nhận đã chạy
    thử nghiệm thật hay mới là thiết kế trên giấy — **nhóm cần tự xác nhận**.
- **Dữ liệu gốc/minh chứng:** 1 ảnh chụp Serial Plotter (do nhóm nghiên cứu gửi qua chat, **chưa có bản
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
  > **Ghi chú bổ sung 2026-10-20 (giữ nguyên bản ghi lịch sử ở trên, không sửa lùi ngày):** cơ chế vừa nêu — lò xo trợ giúp
  > thụ động chia nấc, khớp truyền lực bốn khâu, công thức `F_assist(t) = max(0, F_target − F_phantom)`, ngưỡng `F_max ≤ 5N`
  > và độ trễ `1,2 s` — **đã được RÚT ở Giai đoạn 7 (17–20/10/2026)**. Hướng hiện hành: servo cuốn dây câu cá trực tiếp lên tang,
  > **ba tang riêng** cho ngón cái–trỏ–giữa, duỗi bằng cách **nhả dây chủ động** (`DEC-MECH-007`, duyệt 2026-10-20); **không** lò
  > xo/SEA, **không** khớp bốn khâu; Velostat **không** được quy đổi sang Newton và ngưỡng 5 N **không còn** được dùng làm tiêu chí.
  > Căn cứ: `research/context/CURRENT_DESIGN_BASELINE.md`, mục 13–14 của sổ này, và bảng tổng hợp thay đổi (Giai đoạn 7).
- **Ghi nhận chính thức việc thử nghiệm phần cứng thật đã xảy ra** (mục 8–9.1 ở trên): nhóm nghiên cứu
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

## 10b. 2026-10-12 (ghi nhận từ thực nghiệm của nhóm; ngày in thử thật từng mech chưa xác nhận chính xác) — Thử nghiệm và loại bỏ các phương án cơ cấu đóng/mở nẹp ngón tay (Mech 1 → Mech 9)

> Nguồn: Quá trình thiết kế và in thử thực tế của nhóm nghiên cứu, kèm bảng so sánh và đánh giá các phương án cơ cấu nẹp đốt ngón. Toàn văn chi tiết: `3d_model/custom_exo/fixation_mechanisms_benchmark/README.md`.

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
    tưởng nguyên lý do chính nhóm nghiên cứu đề xuất. Khi dựng mô hình CAD đã gặp và xử lý xong 2 lỗi kỹ
    thuật: (1) một đa giác 2D tự giao cắt làm phần mềm dựng hình xóa mất thân quai kẹp; (2) một
    lệnh khoét rãnh vô tình cắt rỗng luôn trục bản lề chính khiến vật in rời ra khi nhấc lên.
  - **Lưu ý trung thực (chưa xử lý, cần nhóm/nhóm xác nhận):** Mech 9 **chưa có file CAD trong
    repo này** (chỉ tồn tại trên máy tính cá nhân của nhóm nghiên cứu tại thời điểm ghi nhận), **chưa
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

## 11. 2026-10-15 — Vòng lặp Thiết kế số 2 (Design Iteration 2): Tối ưu hóa kiến trúc phần cứng dựa trên thực nghiệm tích hợp cơ khí

> **Căn cứ quy chuẩn:** Quy trình Thiết kế Kỹ thuật (Engineering Design Process) theo Thông tư số 84/2026/TT-BGDĐT.  
> **Nguyên tắc phương pháp luận:** Không xóa bỏ dữ liệu thực nghiệm Vòng lặp 1 (INA333 $G \approx 6.5$, notes 01–06), mà kế thừa và phân tích nguyên nhân vật lý dẫn đến quyết định cải tiến kiến trúc phần cứng (Hardware Simplification & Trade-off).

- **Nội dung công việc:** Chế tạo cảm biến kẹp Sandwich trên khung ốp đốt tay, phát hiện hiện tượng bão hòa tín hiệu INA333 do lực ép tĩnh cơ khí, tối ưu hóa kiến trúc mạch đo (loại bỏ INA333, khai thác PGA 16-bit ADS1115) và thiết lập thuật toán lọc nhiễu động (DSP Pipeline).
- **Phương pháp thực hiện & Cơ sở lý luận:**
  1. **Cấu trúc Cơ - Điện Cảm biến Đốt tay (Sandwich Piezoresistive Transducer):**
     - Cấu tạo: Khung ốp in 3D gắn 2 cụm cảm biến đối xứng tại Mặt lòng (Palmar — Kênh C0) và Mặt mu (Dorsal — Kênh C1).
     - Cấu trúc 3 lớp: Cuộn dây đồng mạ niken $\to$ Màng áp trở Velostat $\to$ Cuộn dây đồng mạ niken (lớp mạ niken chống oxy hóa bề mặt và giảm điện trở tiếp xúc ký sinh).
     - Mạch định thiên: Cầu phân áp với $R_{pullup} = 10\text{ k}\Omega$ độc lập lên nguồn $3.3\text{V}$.
  2. **Bảng Đối chứng Tối ưu hóa Kiến trúc Phần cứng (Hardware Optimization):**

| Tiêu chí đánh giá | Kiến trúc Vòng lặp 1 (Sử dụng INA333, $G \approx 6.5$) | Kiến trúc Vòng lặp 2 — Tối ưu hóa (Đo trực tiếp qua PGA 16-bit ADS1115) | Cơ sở Lý luận & Bằng chứng Thực nghiệm |
|---|---|---|---|
| **Biên độ biến thiên của Velostat** | $\Delta V \approx 1500\text{ mV} - 2200\text{ mV}$ (từ $2.5\text{V}$ xuống $0.3\text{V}$ khi bóp). | Thu nhận trọn vẹn toàn bộ dải biến thiên tự nhiên $0\text{V} - 3.3\text{V}$. | Màng Velostat có hệ số nhạy áp trở lớn gấp hàng trăm lần Loadcell kim loại, không cần khuếch đại tiền tầng hệ số lớn. |
| **Cửa sổ điện áp tuyến tính** | Bị giới hạn hẹp trong khoảng $\pm 0.24\text{V}$ quanh mốc $V_{REF} = 1.68\text{V}$ ($1.44\text{V} \to 1.92\text{V}$). | Mở rộng toàn dải từ $0.000\text{V}$ đến $3.300\text{V}$ (độ phân giải $0.125\text{ mV/LSB}$). | Lực siết cơ khí ban đầu của khung ốp làm điện áp tĩnh rơi xuống $< 1.42\text{V}$, khiến INA333 chạm sàn bão hòa và kẹt đồ thị ở $\approx 2838\text{ mV}$. |
| **Hiện tượng Nhiễu nền & Trôi** | Bị khuếch đại gấp $6.5$ lần cùng với tín hiệu. | Giữ ở mức nguyên bản ($50\text{ mV} - 135\text{ mV}$), dễ dàng triệt tiêu bằng thuật toán. | Giảm 1 mắt xích IC tương tự giúp loại bỏ tạp âm nhiệt nội bộ và giảm công suất tiêu thụ trên găng tay. |

  3. **Quy trình 4 bước Lọc Tín hiệu Số (DSP) trên ESP32-S3:**
     - *Bước 1 — Đọc nháp xả điện tích (Dummy Read & $300\,\mu\text{s}$ Settling):* Sau khi chuyển kênh MUX, chờ $300\,\mu\text{s}$ và thực hiện 1 lần đọc nháp (Dummy Read) để nạp đầy tụ lấy mẫu nội bộ ADS1115, triệt tiêu $100\%$ hiện tượng bóng ma (Ghosting) giữa C0 và C1.
     - *Bước 2 — Khóa vùng chết trừ tuyến tính (Subtracted Dead-band, $V_{gate} = 180\text{ mV}$):*
       $$F_{clean} = \max\left(0.0, \; \vert{}V_{base} - V_{raw}\vert{} - 180\text{ mV}\right)$$
       Đảm bảo tín hiệu đứng yên tuyệt đối tại $0.00\text{ mV}$ khi thả lỏng và tăng tuyến tính mượt mà ngay từ điểm 0 khi bắt đầu tác dụng lực.
     - *Bước 3 — Tự động thích nghi điểm 0 (Adaptive Drift Tracking, $\gamma = 0.002$):* Khi ngón tay thả lỏng ($\vert{}\Delta V\vert{} \le 180\text{ mV}$), mốc tĩnh tự động cập nhật chậm:
       $$V_{base}[k] = 0.998 \cdot V_{base}[k-1] + 0.002 \cdot V_{raw}[k]$$
       Tự động bù trừ sự giãn nở của nhựa ốp và nhiệt độ bàn tay theo thời gian thực.
     - *Bước 4 — Lọc EMA ($\alpha = 0.20$) & Tổng hợp Vi sai Gập/Duỗi:*
       $$F_{net} = F_{palmar(C0)} - F_{dorsal(C1)}$$
       Phân tách rạch ròi ý định vận động: Gập ngón ($F_{net} > 0$) và Duỗi ngón ($F_{net} < 0$).
- **Kết quả từng giai đoạn:**
  - Loại bỏ hoàn toàn hiện tượng kẹt bão hòa $2838\text{ mV}$ của INA333 khi siết ốp cơ khí.
  - Tín hiệu lực vi sai $F_{net}$ phản hồi nhạy, không trôi, đáp ứng trơn tru trên Serial Plotter.
  - Tối giản phần cứng: giảm diện tích bo mạch và dòng tiêu thụ tĩnh.
- **Ý nghĩa đối với Quy trình Thiết kế Kỹ thuật (ViSEF):** Chứng minh quá trình R&D thực chất dựa trên va chạm thực nghiệm thật, có năng lực đánh đổi kỹ thuật (Trade-off) và làm chủ nguyên lý vật lý của cảm biến.
- **Dữ liệu gốc/minh chứng:** File ghi chép chi tiết `research/notebooklm_sync/experiments/07_vong_lap_thiet_ke_2_toi_uu_kien_truc_phan_cung_va_dsp.md`.
- **Vai trò thành viên:** ⟨nhóm tự điền⟩ — **Xác nhận GVHD:** ______________________ (ngày ___/___/2026)

## 12. Các nội dung trọng tâm cần hoàn thiện tiếp theo

1. Điền cột "Vai trò thành viên" cho từng mục 1–9 (bắt buộc theo Điều 14 khoản 1 — dự án tập thể).
2. GVHD Lê Công Long xác nhận trực tiếp (ký) vào nhật ký này theo đúng chu kỳ tối thiểu 1 lần/tháng
   (Điều 14 khoản 1) — có thể ký theo từng mốc ngày hoặc theo hướng dẫn hệ thống nhật ký điện tử
   thống nhất của BTC khi được ban hành (Điều 14 khoản 4).
3. Xác nhận/sửa các ngày đánh dấu "(ngày suy luận — nhóm cần tự xác nhận lại)" ở mục 8–9.1 bằng
   ngày thật ghi trong sổ tay viết tay/điện thoại/lịch sử ảnh của nhóm.
4. Tải 2 ảnh chụp minh chứng (oscilloscope 2C23T 09/10, Serial Plotter 11/10) lên Google Drive
   (`02_Hinh_anh_2C23T/` và `03_Serial_Plotter_exports/` trong folder đã tạo trên Drive) để lưu trữ đồng bộ.
5. Xử lý 3 câu hỏi mở về kỹ thuật nêu ở mục 8–9.1: (a) đơn vị trục Y Serial Plotter (mV hay raw
   ADC count); (b) giá trị kênh C1 không khớp kỳ vọng; (c) chênh lệch G≈6,5 đo được vs G=10 thiết
   kế ban đầu.
6. Khi đã rõ mục 3 và 5, chính thức hoá số liệu bring-up thành log GATE 0 hợp lệ trong
   `research/bench/logs/` theo đúng schema `session_manifest.csv`/`perturbation_log.csv`/
   `reference_check.csv` (mỗi ngày đo một `bench_session_id` riêng) — thư mục này hiện vẫn phải
   giữ rỗng cho tới khi đủ điều kiện.
7. Việc khai báo sử dụng công nghệ số/trí tuệ nhân tạo theo Điều 15 Quy chế — **nhóm tự thực hiện
   riêng, không nằm trong phạm vi tài liệu này.**
8. Các mục "PROPOSED, chờ nhóm nghiên cứu duyệt" còn tồn đọng tính tới 2026-10-11 (xem danh sách đầy đủ
   và cập nhật mới nhất tại `research/context/DECISION_LOG.md` mục "Open decisions"): chốt ngưỡng
   GATE 0 cuối cùng, duyệt bảng phân biệt tính mới `docs/05` §4, xác nhận bản đề cương nào sẽ dùng
   để nộp lại, xác nhận đổi cảm biến nhiệt-ẩm SHT30 → AHT20 là chủ đích hay lỗi đánh máy, và việc
   tra cứu bằng sáng chế theo IPC một cách có hệ thống (vẫn còn nợ từ 2026-09-19).
9. Xuất file CAD Mech 9 (cơ cấu đóng/mở nẹp ngón tay, mục 10b) từ máy tính cá nhân vào repo, in thử
   thực tế và kiểm tra độ bền qua nhiều chu kỳ đóng/mở trước khi coi là thiết kế chính thức; xác
   nhận quan hệ giữa bộ thử nghiệm này với cơ cấu bản lề liên-đốt đã chốt ở `docs/06`.
10. **(MỚI 2026-10-19)** Duyệt 7 mã đề xuất trong `research/context/DECISION_LOG.md`: `DEC-TASK-001` (tờ yêu cầu bài tập
    thìa + bảng trạng thái), `DEC-TASK-002` (chọn 1 trong 5 cách phân biệt vận động tự nguyện với chuyển động do máy kéo),
    `DEC-CHMAP-001` (chọn phương án bố trí 16 kênh), `DEC-ACQ-001` (tốc độ quét mục tiêu — phải đo rồi mới chốt),
    `DEC-VIS-001` (kiến trúc camera), `DEC-IMPL-001` (lộ trình phần mềm F0–F6), `DEC-IMPL-002` (đặt bộ điều khiển
    chuyển chế độ ở ESP32-S3 hay ở Orange Pi). Hồ sơ tương ứng: `research/protocols/10`, `10a`, `10b`, `docs/07`, `docs/08`.
11. **(MỚI 2026-10-19)** Kiểm tra trên mạch thật 8 điểm ở `research/protocols/10a` §7 — trong đó hai điểm đáng chú ý:
    (a) đối chiếu giới hạn điện áp đầu vào của ADS1115 theo tài liệu hãng với ghi nhận cũ "đọc toàn dải 0–3,3 V";
    (b) chip ADS1115 trên board có đưa 3 ngõ vào `A1–A3` ra chân hàn hay không (nếu có, đọc 3 cảm biến gập thẳng vào đó
    và giải phóng 3 kênh của bộ chuyển mạch).
12. **(MỚI 2026-10-19)** Chốt cơ cấu nhả/hồi dây để **duỗi** ngón và phương án một tang kéo cả ba ngón hay ba tang riêng;
    thu xếp thiết bị đo lực/căng dây độc lập (không dùng Velostat làm chuẩn lực) trước khi thử cơ cấu.

---

## 13. 2026-10-19 — Lượt tài liệu Gate 0 (chốt bài tập + bản đồ kênh) và kế hoạch viết code

> **Bản đầy đủ:** [`2026-10-19_NHAT_KY_BO_SUNG_GATE0_VA_KE_HOACH_CODE.md`](2026-10-19_NHAT_KY_BO_SUNG_GATE0_VA_KE_HOACH_CODE.md)
> (cùng thư mục; trên Drive nằm trong `04_So_tay_nhat_ky_nghien_cuu/`). Mục này tóm tắt để sổ tay liền mạch.
> Báo cáo rà soát chi tiết: `research/reviews/2026-10-19_gate0_packet_and_abc_review.md`.

- **Nội dung công việc:** theo chỉ đạo của chủ dự án *"hoàn thiện đề cương rồi mới bắt đầu code"*, đã soạn bộ hồ sơ Gate 0
  (tờ yêu cầu bài tập thìa + 14 trạng thái tác vụ + máy trạng thái chế độ + 5 phương pháp phân biệt vận động tự nguyện với
  chuyển động do máy tạo ra + sơ đồ ngón↔cảm biến↔cơ cấu), bản đồ 16 kênh cảm biến với 4 phương án bố trí, đặc tả nhánh
  camera (xử lý ảnh cổ điển trước, phần nhận vật thể thiết kế dạng thay thế được), lộ trình viết phần mềm theo 7 pha F0–F6;
  bổ sung vào đề cương A/B/C bảng "đăng ký trước" 14 chỉ số và mục thứ tự triển khai công cụ; cập nhật sổ quyết định
  (+7 mã đề xuất) và sổ luận điểm (+6 luận điểm).
- **Phương pháp thực hiện:** đọc lại toàn bộ tài liệu điều hành trước khi sửa; đối chiếu từng phát biểu với quyết định đã chốt;
  chỉ dùng số do nhóm đã ghi từ mạch thật và ghi rõ xuất xứ; phép tính tự làm thì dán nhãn "tính toán, phải đo lại";
  quét các cụm từ dễ vi phạm quy chế; kiểm tra liên kết tài liệu, tính hợp lệ sổ luận điểm và chạy công cụ kiểm tra mẫu phiếu đo.
- **Kết quả từng giai đoạn:** 6 tài liệu mới + 10 tài liệu cập nhật, **tất cả ở mức đề xuất chờ duyệt**; **không điền bất kỳ
  ngưỡng/thông số bài tập/con số an toàn nào** (để trống có chủ đích kèm cột "căn cứ để điền"); **chưa viết code/firmware**,
  **không chạy benchmark**, **không đo phần cứng**, **không sửa hồ sơ đã nộp và tệp nguồn trên Drive**, **chưa đưa lên GitHub**
  theo yêu cầu của chủ dự án. Phát hiện 2 điểm kỹ thuật cần kiểm tra: giới hạn điện áp đầu vào ADS1115 so với ghi nhận
  "đọc 0–3,3 V", và bảng tốc độ khung cũ (~415 lần/giây) không áp dụng cho mạch ADS1115 hiện hành (tính lại ≈ 24–54 lần/giây
  tuỳ số kênh — là phép tính, chưa phải số đo).
- **Vai trò thành viên:** ⟨nhóm tự điền⟩ — **Xác nhận GVHD:** ______________________ (ngày ___/___/2026)

---

## 14. 2026-10-20 — Chủ dự án duyệt ba hạng mục (PA-2 · M3 · ba tang) và dựng lại bản Word rà soát

> **Bản đầy đủ:** [`2026-10-20_NHAT_KY_QUYET_DINH_PA2_M3_BA_TANG_VA_DUNG_LAI_DOCX.md`](2026-10-20_NHAT_KY_QUYET_DINH_PA2_M3_BA_TANG_VA_DUNG_LAI_DOCX.md)
> (cùng thư mục). Ghi nhận chi tiết và các kiểm tra đã chạy: `research/reviews/2026-10-20_owner_decisions_and_docx_rebuild.md`.

- **Nội dung công việc:** chủ dự án trả lời trực tiếp ba câu hỏi đang chờ: (1) **bản đồ kênh — chọn PA-2** (3 cảm biến gập qua bộ
  chuyển mạch + 6 ô Velostat theo cặp lòng/mu cho cái–trỏ–giữa + 2 ô tham chiếu = **11 kênh quét**, 5 kênh dự phòng) → `DEC-CHMAP-001`;
  (2) **phân biệt vận động tự nguyện với chuyển động do máy tạo — chọn M3** (cửa sổ "thăm dò tự nguyện": tạm ngưng trợ lực một khoảng
  ngắn rồi đo đáp ứng) → `DEC-TASK-002`; (3) **cơ cấu truyền động — ba tang cuốn riêng + servo nhả dây chủ động** để duỗi, không lò xo,
  không khớp bốn khâu → mã mới `DEC-MECH-007`. Việc tiếp theo được chỉ đạo: **dựng lại bản Word để rà soát** từ đề cương A/B/C.
- **Phương pháp thực hiện:** ghi quyết định vào sổ quyết định trước rồi mới lan toả sang hồ sơ kỹ thuật; mỗi quyết định ghi kèm
  **danh sách những gì vẫn còn trống** ngay trong cùng dòng để "đã duyệt" không bị đọc nhầm thành "đã xong"; đổi trạng thái từng dòng
  bản đồ kênh dạng bảng; dựng bản Word bằng **công cụ chuyển đổi đọc trực tiếp tệp Markdown** (không gõ lại nội dung), giữ quy ước trình
  bày sẵn có của repo (Times New Roman 14, lề 3/2/2/2 cm, giãn dòng 1,35) và **không tạo hyperlink** để tránh liên kết gãy; công cụ có chế
  độ tự kiểm tra (dò cú pháp Markdown còn sót, dò lỗi cắt đường dẫn, đếm dòng/cột bảng đăng ký chỉ số, kiểm tra ngày dựng và đề mục).
- **Kết quả từng giai đoạn:** 2 mã chuyển sang **đã duyệt** + 1 mã mới; 11 tài liệu cập nhật; 3 tài liệu mới (nhật ký bổ sung, ghi nhận
  quyết định, bản Word `exports/11A2_CAP_NHAT_DU_THAO_2026-10-20.docx` ~3.670 từ). Tự kiểm tra bản Word **PASS** sau khi sửa 4 lỗi của công
  cụ (ngày lấy theo giờ UTC bị lùi một ngày so với giờ Việt Nam; danh sách trộn đánh số tự động với số chữ khiến mục đầu mất số; bốn ghi chú
  đầu tệp bị gộp thành một đoạn; đường dẫn liên kết bị cắt mất ký tự cuối). **Không điền ngưỡng/thông số bài tập nào; chưa viết
  code/firmware; không đo phần cứng; không benchmark; không ghi đè tệp nào trên Drive; chưa đưa lên GitHub.** Nhấn mạnh: cả ba quyết định
  là **lựa chọn phương án**, chưa được chế tạo, chưa chạy thử, chưa kiểm chứng an toàn; bản Word là **bản rà soát, không phải bản nộp**.
- **Bản sao trên Drive (tải lên mới 2026-10-20, không ghi đè tệp nào):** nhật ký bổ sung mục 14 nằm trong `04_So_tay_nhat_ky_nghien_cuu/` (ID `1ja-Q3G-OM2tHIotD2f6w3bemZlUillCc`); bản Word rà soát nằm trong `01_Cac_file_lam_viec/` với tên `11A2_CAP_NHAT_DU_THAO_2026-10-20_BAN_RA_SOAT.docx` (ID `1j4D_fxomFLwh4a2Vmok__b77f3hwmi2O`) — cố ý đặt **ngoài** thư mục chứa bản đã nộp để không thể nhầm với bản nộp. Đã để lại bình luận trên sổ tay (ID `AAACJEAXHn4`), trên bảng tổng hợp (ID `AAACBEnB3HY`) và trên bản Word cũ ngày 19/10 (ID `AAACI3RglQo`, bản cũ vẫn lỗi thời và không bị ghi đè). Chi tiết: `research/reviews/2026-10-20_owner_decisions_and_docx_rebuild.md` mục 6.
- **Cùng ngày (2026-10-20) — đọc `11A2.pdf` và đề xuất hướng cải thiện trước hạn nộp:** đọc bản 12 trang do chủ dự án cung cấp (chỉ đọc, không sửa tệp trên Drive; công cụ đọc trả toàn bộ chữ nhưng bị cắt giữa nên đã đọc lại bằng nhiều lát cắt — phần B.3, nội dung B.6, chỉ tiêu 2–10 của C.3, C.4 và chú thích hình **chưa trích xuất được**, đã khai báo rõ trong tài liệu). Kết quả đối chiếu: bản PDF **vẫn theo trục "thiết bị đo lường" cũ** (EI/GAP/RAL, ma trận 16 ô Velostat, một mục riêng cho Học tăng cường) trong khi hướng đã chốt là **hỗ trợ tập vận động tinh** (3 Flex + 6 Velostat = 11 kênh, camera, bài tập thìa, ba tang, phương pháp M3); **Bảng 3 ở mục C.2 trình bày SNR 21,4 dB / R² 0,93 / 25 Hz / 0,00 mV "phẳng tuyệt đối" như kết quả đã đạt**, trong khi chính những số đó được mục A.4 gọi là *"ngưỡng mục tiêu dự kiến"* và mục C.3 nói sẽ kiểm định từ 10/2026 đến 01/2027 — và **trong kho dự án không có log/biên bản nào cho bốn con số đó** (thư mục log bàn thử rỗng; số nhiễu 50–135 mV và hiện tượng bão hòa ≈2838 mV thì có ghi nhận bring-up nhưng chưa formal hoá thành buổi đo theo mẫu). Ngoài ra PDF còn nguyên ngưỡng **≤ 5 N** và cách nói *"chỉ bù đúng phần lực thiếu hụt"* (đã rút), Mech 9 ghi **"Đạt tối ưu"** dù chưa có bản vẽ CAD trong kho và chưa đo độ bền, mục C.6 nói tới thử đối chứng lâm sàng trên người bệnh. **Ghi nhận công bằng:** bản PDF đã sửa được nhiều lỗi của bản DOCX 17/10 (GAP = PROM − AROM đúng chiều, Manumeter ~31 % diễn giải đúng đại lượng, có câu chặn *"đề tài không đo hoạt động vỏ não"*, nguồn riêng cho Penfield/Hebb, danh mục [1]–[12] khớp sổ nguồn) — những chỗ đó nên giữ. Đề xuất 9 điểm P0 + 8 điểm P1 + ưu tiên cắt trang (vì khuôn A/B/C được chọn do giới hạn trang) + ba phương án bản nền + kế hoạch theo quỹ thời gian: `research/reviews/2026-10-20_11A2_pdf_improvement_plan.md`; chờ duyệt **`DEC-PROP-005`** (chọn bản nền, hạn nộp thật, số trang tối đa). **Chưa sửa một chữ nào trong `11A2.pdf`/`11A2.docx`, chưa dựng bản nộp mới, không thêm số đo nào, mọi ô trống vẫn trống.**
- **Cùng ngày (2026-10-20) — dựng BẢN NỘP mới theo Phương án A:** sau khi chủ dự án duyệt bản nền (`DEC-PROP-005`), chốt độ dài **≤ 14 trang nội dung, 15 kể cả bìa** và nguyên tắc *"đề cương không phải báo cáo toàn văn: có kết quả gì báo cáo kết quả đó và đưa ra các mục tiêu định lượng"* (`DEC-PROP-006`), nhóm agent dựng `docs/DE_CUONG_A_B_C_BAN_NHAP_2026-10-20.md` rồi chuyển sang Word (`exports/DE_CUONG_A_B_C_BAN_NHAP_2026-10-20.docx`, 7.023 từ, 6 bảng, công cụ tự kiểm tra PASS; bản Word rà soát của lượt trước không bị ghi đè). Bản này áp dụng cả chín điểm phải sửa đã nêu: đổi trục đề tài sang hỗ trợ tập vận động tinh; trình bày số liệu theo **ba cột đã đo – sơ bộ – mục tiêu** (hai con số SNR 21,4 dB và R² 0,93 được ghi rõ là **kho dự án không truy vết được**, phải đối chiếu đồ thị trong thư mục Drive `03_Serial_Plotter_exports` và lập phiếu buổi đo trước khi trích lại); gỡ ngưỡng 5 N và mọi cách nói theo Newton; bỏ Học tăng cường khỏi phạm vi; cập nhật PA-2 11 kênh, ba tang + nhả dây chủ động, M3, camera và bài tập thìa; hạ mức khẳng định Mech 9 thành *"phương án triển vọng nhất, chưa có bản vẽ trong kho, chưa đo độ bền theo biên bản"*; kết luận sơ bộ tách rõ **đã làm** và **chưa làm**; giữ ranh giới bàn thử/mô hình tay giả trước, người khỏe chỉ có điều kiện, IRB là chuyện của giai đoạn sau. **Chưa điền** thông tin bìa/thành viên/người hướng dẫn, **chưa chèn** hình (để sẵn năm chỗ `⟨HÌNH …⟩`), **chưa đếm trang thật** (máy dựng không có công cụ xuất PDF), **chưa tải lên Drive, chưa commit**. Ba nguồn [2] [3] [6] vẫn `UNVERIFIED` trong sổ nguồn — phải đối chiếu toàn văn hoặc bỏ trước khi nộp.
- **Cùng ngày (2026-10-20, lượt 2) — viết lại hoàn chỉnh mục B và C, rồi tải lên Drive:** theo chỉ đạo *"viết hoàn thành B/C luôn đi, phần A tham khảo bản cũ"* và *"cấu trúc này cần tái lại nội dung các mục"* (`DEC-PROP-007`), bản dựng nộp được viết lại: mục A theo cấu trúc A.1–A.4 của `11A2.pdf`; mục B thành 10 tiểu mục (thêm kiến trúc phần mềm–luồng dữ liệu–nhật ký đo, và bảng máy trạng thái 7 trạng thái); mục C thành 9 tiểu mục (thêm phương pháp kiểm định với 8 quy trình đo, điều kiện ghi nhận, tiêu chí loại phiên; và mục riêng về phạm vi thử trên người + đạo đức nghiên cứu). Kết quả 12.817 từ, 199 đoạn, 8 bảng, công cụ tự kiểm tra PASS. **Phải ghi rõ một vấn đề:** bản đầy đủ này ước tính **24–26 trang** ở cỡ 14 pt, giãn dòng 1,35, trong khi chủ dự án đã chốt trần **14 trang nội dung + 1 bìa** (`DEC-PROP-006`) — máy dựng không có LibreOffice/pandoc nên **không đếm trang được**, số trang phải kiểm tra trong Word; ba cách xử lý và thứ tự cắt đã ghi ở `research/reviews/2026-10-20_11A2_pdf_improvement_plan.md` §10. **Bản sao trên Drive (tệp mới, không ghi đè):** `DE_CUONG_A_B_C_BAN_DAY_DU_2026-10-20.docx` trong `01_Cac_file_lam_viec` (ID `1PNVjezxgTSeur_nEdcLXu-BasvFIlLsr`) và `2026-10-20_11A2_pdf_improvement_plan.md` trong `04_So_tay_nhat_ky_nghien_cuu` (ID `1viIe0njVXkH0TCaCQFlOzDXPwkJopTpw`); bình luận trỏ về: `AAACI4VCoFs` (sổ tay), `AAACJDB1Y4w` (bảng tổng hợp). `11A2.pdf` và `11A2.docx` **không bị chỉnh sửa**. **Chưa điền** bìa/thành viên/GVHD, **chưa chèn** hình, **chưa commit**; ba nguồn [2] [3] [6] vẫn `UNVERIFIED` trong sổ nguồn.
- **Cùng ngày (2026-10-20, lượt 3) — viết lại cô đọng theo bản mẫu:** chủ dự án chỉ ra nguyên nhân bản đầy đủ quá dài: *"có quá nhiều câu xã giao, bạn đọc file pdf mẫu của tôi bạn sẽ thấy nó rất cô đọng, đi thẳng vào vấn đề"* (`DEC-PROP-008`). Agent đọc lại toàn bộ mục A và danh mục tài liệu tham khảo của `11A2.pdf` để đo mật độ thật của bản mẫu — **A.1 "Lý do chọn đề tài" chỉ ~90 từ cho cả mục**, B.1 là một đoạn ~90 từ, B.2 là một đoạn ~110 từ liệt kê 4 rào cản, A.4 là một câu dẫn cộng 5 gạch đầu dòng — rồi viết lại đề cương theo đúng khung đó: A.1–A.4 · B.1–B.7 · C.1–C.6 · TLTK [1]–[15]. Kết quả **12.817 từ → 5.718 từ**; chủ dự án yêu cầu làm gấp và *"đừng cắt bớt nội dung"*, nên nén thêm một lượt chỉ ở mức câu chữ (bỏ từ đệm, gộp mệnh đề bằng dấu chấm phẩy, thay câu trần thuật bằng tham chiếu chéo) còn **5.519 từ** — 101 đoạn, 6 bảng, ước tính **12,4 trang nội dung kể cả 7 hình**, vừa trần 14 trang, dư ~1,6 trang. Bài học: khi bản đã đặc thì nén câu chỉ ăn được ~3%, phần còn lại phải giải bằng chỗ dư trang hoặc cỡ chữ, **không giải bằng cách bỏ ý**. Bài học ghi thành chuẩn trong `research/tooling/WRITING_STYLE_PROFILE.md`: **mỗi tiểu mục một đoạn 2–4 câu hoặc một danh sách; cần nói nhiều hơn thì chuyển thành bảng, không viết thêm đoạn; trạng thái bằng chứng đưa vào nhãn `[SƠ BỘ]`/`[MỤC TIÊU]`/`OPEN` hoặc một cột bảng, không viết thành câu trần thuật; không câu dẫn nhập, câu chuyển ý lặp, câu tóm tắt lại ý vừa nói**. Nhờ đọc lại bản mẫu cũng **sửa được 5 chi tiết thư mục đã ghi sai** ở bản đầy đủ ([4], [7], [8], [10], [11]) và phát hiện một **mâu thuẫn cần đối chiếu**: [8] trong bản mẫu ghi *Sensors*/PMC11793859 trong khi sổ nguồn của dự án ghi *IEEE OJEMB*. **Bản sao trên Drive (tệp mới, không ghi đè):** `DE_CUONG_A_B_C_BAN_NOP_CO_DONG_2026-10-20_v2.docx` trong `01_Cac_file_lam_viec` (ID `19cAEh8g02ruoBsPUOL_cj1ebtlZi9N1t`) là **bản để nộp hiện hành**; v1 (ID `176tj3MWVVa6p6tkuw-GCsKzk6GzbdE70`, bình luận `AAACJC-ltuc`) và bản đầy đủ (ID `1PNVjezxgTSeur_nEdcLXu-BasvFIlLsr`, bình luận `AAACI3sp9I4`) đều **không bị xóa**, giữ làm vết lịch sử và hồ sơ nội dung. **Chưa duyệt toàn văn, chưa điền bìa/thành viên/GVHD, chưa chèn 7 hình, chưa đếm trang thật trong Word, chưa commit.**
- **Cùng ngày (2026-10-20, lượt 4) — tách BẢN NỘP khỏi bản làm việc:** chủ dự án yêu cầu *"cho tôi 1 bản đề cương chuẩn để nộp đi"* và gạch đúng câu *"Khác bản trước: bỏ ngưỡng 'lực an toàn ≤ 5 N'…"* là **"sặc mùi trợ lí"**. Bài học: tài liệu agent dựng là **tài liệu làm việc**, nó mang theo cả nhật ký chỉnh sửa và vết kiểm toán; bản nộp phải là tài liệu của đề tài. Agent dựng tệp riêng `docs/DE_CUONG_A_B_C_BAN_NOP_2026-10-20.md` (không ghi đè bản nội bộ `…BAN_NHAP…`) và bỏ khỏi đó: câu nói về phiên bản trước, câu kiểm toán nội bộ, mã nội bộ `PA-2`/`M3`/`Gate`, nhãn `OPEN`/`[SƠ BỘ]`/`[MỤC TIÊU]`, đường dẫn tệp trong kho, banner đầu tệp và ghi chú nội bộ cuối tệp. Thay bằng tiếng Việt tự nhiên mà **không mất nội dung**: hai số SNR 21,4 dB và R² 0,93 (không truy vết được) chuyển hẳn thành mục tiêu ≥ 18 dB và ≥ 0,90 kèm câu nói sẽ đo bằng buổi đo có biên bản; Mech 7 ghi "không có số liệu trong hồ sơ hiện tại của nhóm"; trạng thái bằng chứng chỉ nói một lần ở đầu phần C. Kết quả **5.627 từ, 100 đoạn, 6 bảng, 7 chỗ chèn hình, ước tính 12,7 trang**, `--check` PASS, `grep` 0 từ khóa nội bộ. Quy tắc đã ghi thành chuẩn trong `research/tooling/WRITING_STYLE_PROFILE.md` mục "Quy tắc riêng cho BẢN NỘP". **Bản sao trên Drive (tệp mới):** `DE_CUONG_A_B_C_BAN_NOP_2026-10-20.docx` trong `01_Cac_file_lam_viec` (ID `1-jBcBMSKeA_a05STGboKMwXn7AMZYTJa`) — **đây là bản để nộp**; v2 (ID `19cAEh8g02ruoBsPUOL_cj1ebtlZi9N1t`, bình luận `AAACI37XCmQ`) nay là bản nội bộ có nhãn kiểm toán. **Chưa duyệt toàn văn, chưa điền lĩnh vực/đơn vị/thành viên/GVHD, chưa chèn 7 hình, chưa đếm trang thật trong Word, chưa commit.**
- **Cùng ngày (2026-10-20, lượt 5) — bài học về GIỌNG VĂN, quan trọng nhất cả ngày:** chủ dự án nhận xét *"Bạn vẫn chưa thấy được phong cách văn phong ngắn gọn"* rồi tự viết lại mục A.2.1 và đưa cả hai bản để đối chiếu (`DEC-PROP-010`). So sánh cho thấy agent đã **đo sai đại lượng**: suốt bốn lượt chỉ đếm tổng số từ, trong khi vấn đề là giọng văn. Bản của agent nhồi ba ý vào một câu bằng dấu chấm phẩy và lược chủ ngữ kiểu điện tín ("phản hồi cảm giác đồng bộ với nỗ lực vận động giúp định hướng tập luyện"), nên đọc mệt hơn dù ngắn; bản của chủ dự án **tách mỗi ý một đoạn 1–3 câu** và viết có danh hóa ("Nghiên cứu của Penfield & Boldrey [11]…", "việc cung cấp phản hồi cảm giác…", "định hướng cho việc tập trung vào 3 ngón trụ cột (cái, trỏ, giữa)"). Năm điểm khác còn lại: trích dẫn gộp `[2, 3]` chứ không `[2], [3]`; tên tác giả giữ dạng quốc tế `Penfield & Boldrey`, `Gordon et al.`; số đếm bằng chữ số; liệt kê ngắn trong ngoặc đơn; và câu giới hạn phạm vi **gắn vào mệnh đề chính bằng ";"** ("…từ đáp ứng áp trở vi mô; đề tài không đo hoạt động vỏ não hay chứng minh sự tái tổ chức thần kinh") thay vì đứng riêng thành một câu phòng thủ. Ngoài ra gọi đúng tên cơ chế ("áp trở vi mô", không nói "cảm biến" chung chung) và không nhắc trước khái niệm đã có mục riêng. Đã viết lại toàn bộ bản nộp: **100 → 143 đoạn**, trung bình 43 từ/đoạn, 5.723 từ, ước tính 12,9 trang, `--check` PASS. Toàn bộ ví dụ đối chiếu và sáu quy tắc đã chép vào `research/tooling/WRITING_STYLE_PROFILE.md` mục "Giọng văn chuẩn". **Thước đo mới để tự kiểm trước khi giao: số đoạn và số từ trung bình mỗi đoạn (~140 đoạn, ~40–45 từ), không phải tổng số từ.** **Bản sao trên Drive (tệp mới):** `DE_CUONG_A_B_C_BAN_NOP_2026-10-20_v2.docx` trong `01_Cac_file_lam_viec` (ID `11UW8oIMmgNtZ87IWMWbxEO5P61UlaKd0`) — **đây là bản để nộp**; bản lượt trước (ID `1-jBcBMSKeA_a05STGboKMwXn7AMZYTJa`, bình luận `AAACJEo1aEk`) giữ làm vết. **Chưa duyệt toàn văn, chưa điền lĩnh vực/đơn vị/thành viên/GVHD, chưa chèn 7 hình, chưa đếm trang thật trong Word, chưa commit.**
- **Cùng ngày (2026-10-20) — loại bỏ vai trò edge-AI của Orange Pi 5 Pro (`DEC-EDGE-001`):** chủ dự án chỉ đạo bỏ chức năng cũ *"lượng tử hóa mô hình RL INT8 trên Orange Pi 5 Pro và kiểm chứng thuật toán tự động gắn nhãn 'Nghi vấn'"* vì *"hơi xàm"*. Truy vết cho thấy câu chữ đó xuất phát từ **bản đã nộp trường** `de_cuong/DE_CUONG_NGHIEN_CUU_NOP_TRUONG.docx` (đoạn 48, 114, 126) và còn nằm rải rác ở `docs/02` §9, `docs/04`, `docs/05` M6, `docs/03` dòng 10, `OUTLINE_BAOCAO_VISEFD`, `DE_CUONG_NGAN_5-7_TRANG_DRAFT` M6/P4, `PROJECT_SNAPSHOT` (GATE EDGE), `protocols/06` (GATE EDGE + 3 nhân NPU), `protocols/07` §3b. Ba mục bị loại: lượng tử hóa INT8/RKNN và suy luận NPU ≤ 20 ms; mô hình RL bù trôi/trễ (MDP Inversion) và chính sách AAN, tức toàn bộ GATE EDGE/M6; và nhiệm vụ kiểm chứng thuật toán tự động gắn nhãn "Nghi vấn". Orange Pi 5 Pro **chỉ còn nhánh thị giác** theo `CURRENT_DESIGN_BASELINE.md` và `DEC-VIS-001`. Điều cần nhớ để không mất nội dung thật: **kiểm soát chất lượng phiên đo vẫn còn**, nhưng nằm ở trạng thái `INVALID` của máy trạng thái 7 chế độ cộng quy tắc "phiên bị loại phải ghi rõ lý do" — không cần một thuật toán gắn nhãn tự động. RL vốn đã ngoài phạm vi từ `DEC-RL-001/002` (19/10), nên đây là bước dọn nốt phần INT8/NPU và nhãn "Nghi vấn". **Bản nộp hiện hành không chứa ba mục đó (quét 0 kết quả)**; các tệp đã nộp/lịch sử **không bị sửa**, 12 tài liệu còn sống được gắn banner loại bỏ; `CLAIM_LEDGER` sửa `CLM-HW-002` và thêm `CLM-EDGE-001` (56 dòng). **Chưa commit.**
- **Cùng ngày (2026-10-20) — thẩm định danh sách 16 mục cắt giảm trước hội đồng:** chủ dự án đưa danh sách xếp theo 3 cấp độ rủi ro và link bản báo cáo hiện hành `11A2_ban_gop_hoan_thien.docx` (Drive ID `1f8zHjhmekds0TzaTcMi9UqzywXxLHb_B`). Agent đối chiếu từng mục với hồ sơ repo trước khi sửa, kết quả ghi ở `research/reviews/2026-10-20_cut_list_triage.md` và ba quyết định `DEC-ACQ-002`, `DEC-MECH-008`, `DEC-PROP-011`. **Bài học quan trọng nhất của lượt này: một danh sách rà soát do máy khác sinh ra cũng phải được kiểm chứng bằng hồ sơ dự án trước khi áp dụng.** Hai mục trong danh sách sai: (a) mục 4 gọi 3 cảm biến Flex là "linh kiện ảo do AI tự thêm" trong khi `PROJECT_SNAPSHOT` ghi rõ *owner confirmed three Flex sensors* và chủ dự án đã duyệt PA-2 = 3 Flex + 6 Velostat + 2 REF (`DEC-CHMAP-001`) — nếu nghe theo thì đã phá một quyết định đã chốt và làm mất nguồn đo gập–duỗi từng ngón cùng đại lượng trong găng của GAP; (b) mục 2 đòi bỏ thao tác đọc nháp vì ADS1115 là delta-sigma — nửa đầu đúng (giải thích "xả tụ ký sinh" là sai cơ chế) nhưng nửa sau sai, vì lần chuyển đổi đầu tiên sau khi đổi kênh vẫn chứa mẫu của kênh cũ trong bộ lọc số, nên **sửa giải thích và giữ thao tác**. Ngược lại, danh sách bắt được **một lỗi thật rất nặng mà các lượt trước không thấy**: ngưỡng vùng chết 180 mV **cao hơn** dải nhiễu nền đã ghi nhận 50–135 mV, nghĩa là nó có thể nuốt luôn tín hiệu nỗ lực sớm của người yếu cơ và làm hỏng chính phép đo EI. Ngưỡng này nay bị đặt lại thành **chưa đạt**. Ba lỗi thật khác cũng được sửa: tuyên bố giám sát dòng servo trong khi không có điện trở shunt; ngụ ý hộp số servo tự nhả dây khi mất nguồn (hộp số tỉ số lớn không quay ngược được khi ngắt điện); và Mech 9 "22 giây / 50 chu kỳ" vốn không có biên bản. Agent cũng tìm ra một rủi ro ngoài danh sách: `EQUIPMENT_AND_ACCESS.md` ghi **CD74HC4067 "[Chưa xác định] — món duy nhất ở Lớp 1 có thể còn thiếu"**, mà toàn bộ cấu hình 11 kênh phụ thuộc nó. Bản nộp tăng 5.723 → **6.315 từ**, 147 đoạn, ước tính **~13,8 trang**, chỉ còn ~0,2 trang dự phòng. **Chưa duyệt toàn văn, chưa điền bìa/thành viên/GVHD, chưa chèn 7 hình, chưa đếm trang thật trong Word, chưa commit.**
- **Cùng ngày (2026-10-20) — chủ dự án trả lời các điểm chờ quyết định và đổi giọng văn bản nộp:** sau khi thẩm định danh sách 16 mục, chủ dự án chốt **thu máy trạng thái về 3 pha** (Nghỉ → Đo nỗ lực → Kéo trợ lực) thay vì giữ 7 trạng thái; xác nhận **CD74HC4067 đã có và đã chạy thử**, **3 cảm biến Flex chưa có và phải mua ở mốc 1 nhưng thiết kế vẫn giữ Flex kết hợp Velostat**, và **Mech 9 đã in nhưng chưa bấm giờ**. Ba câu trả lời đó sửa được ngay ba chỗ sai trong văn bản: con số 22 giây của Mech 9 bị rút vì chưa từng được đo; cảnh báo "CD74HC4067 có thể còn thiếu" được xóa; và Flex chuyển từ trạng thái "chủ dự án đã xác nhận dùng" thành hạng mục phải mua, nhưng **cấu hình 11 kênh không đổi**. **Bài học: câu trả lời của chủ dự án có giá trị hơn mọi suy luận lấy từ danh sách rà soát.** Mục 4 của danh sách đòi cắt Flex, còn chủ dự án thì nói rõ chưa có nhưng vẫn giữ; hai việc đó khác nhau, và hồ sơ thiết bị phải ghi được ba trạng thái (đã có / chưa có phải mua / chưa xác nhận) chứ không chỉ có hay không. Riêng **ADS1115 vẫn chưa xác nhận** dù toàn bộ chuỗi đo hiện hành phụ thuộc nó — món nợ thiết bị duy nhất còn lại ở Lớp 1. Sau đó chủ dự án đưa báo cáo mẫu cấp quốc gia của một dự án khác (xe lăn tự hành cho người xơ cứng teo cơ một bên) và nhận xét mẫu *"không nhồi nhét quá nhiều công thức, quy tắc mà vẫn ổn định"*, yêu cầu viết lại phần A và B theo mẫu đó. Việc viết lại làm lộ ra một **đánh đổi thật sự giữa giọng văn và trần trang**: cùng một nội dung, viết theo lối tự nhiên tốn thêm khoảng 1.600 từ và 2 trang so với lối nén mật độ cao của bản mẫu 11A2. Cách xử lý đã chọn là **không cắt nội dung** (trái chỉ đạo lượt 5) mà **dời công thức vào một bảng tham số duy nhất**, bỏ bảng quy tắc 7 trạng thái, rồi dựng sẵn hai biến thể định dạng để chủ dự án chọn: 14 pt / 1,35 cho ~15,9 trang (vượt trần 14) và 13 pt / 1,15 cho ~13,2 trang (vừa trần). **Đây là lần đầu trần trang bị vượt kể từ lượt 4, và nguyên nhân là yêu cầu về giọng văn chứ không phải do thêm nội dung mới.** **Chưa duyệt toàn văn, chưa điền bìa/thành viên/GVHD, chưa chèn 7 hình, chưa đếm trang thật trong Word, chưa commit.**
- **Vai trò thành viên:** ⟨nhóm tự điền⟩ — **Xác nhận GVHD:** ______________________ (ngày ___/___/2026)
