# Đề tài đề xuất (ViSEF-style) — Velostat ổ cối chân giả tự hiệu chuẩn

**Ngày:** 2026-08-26 · **Trạng thái:** PROPOSED — cần owner duyệt + 1 vòng kill-test cơ chế trước khi chốt.

## Tên đề tài (đóng gói kiểu ViSEF, không kiểu IEEE)

> **"Thiết bị theo dõi áp lực ổ cối chân giả có khả năng tự hiệu chuẩn, cảnh báo sớm nguy cơ tổn thương da cho người khuyết tật chi dưới"**
> Lĩnh vực: **Kỹ thuật Y Sinh** (có thể xếp Hệ thống nhúng).

Tên đặt theo công thức đề tài ViSEF đoạt giải: *[Thiết bị] + [cảnh báo/hỗ trợ] + [nhóm người cụ thể] + [lợi ích nhân văn]*. Cơ chế khoa học nằm bên trong, không nằm ở tiêu đề.

## Vấn đề con người (cấp thiết, có thật)

- Người cụt chi dưới phụ thuộc ổ cối chân giả; thể tích mỏm cụt **thay đổi trong ngày** → ổ cối lỏng/chặt → **điểm áp lực cao** → phồng rộp, loét da, phải bỏ chân giả. Đây là nguyên nhân hàng đầu gây vấn đề da ở người dùng chân giả.
- Cảm biến áp lực ổ cối thương mại (Tekscan F-Socket, novel Pliance) **đắt**, chủ yếu dùng trong phòng khám, không đeo theo dõi liên tục hằng ngày được.

## Khoảng trống (được chính tài liệu thừa nhận)

- Velostat **rẻ** và đã được thử làm cảm biến trong ổ cối, nhưng **không tin cậy**: sai số 16–48%, trôi theo chu kỳ, trôi tĩnh ~1.17%/phút, **nhạy nhiệt tới 67%**, trễ ~7.25%. Chính tác giả kết luận Velostat *"cần cải thiện đáng kể đặc tính điện trước khi dùng được cho đo áp lực chính xác"*, và việc hiệu chuẩn/mô hình hóa **từng cảm biến là bất khả thi với mảng lớn** (`SRC-HOPKINS-2020-IEEEJS`).
- Các hệ ổ cối thông minh đã có (`SRC-SMARTSOCKET-2025-WILEY`, `SRC-SFU-2026-3DPRINT-SOCKET`, `SRC-VA-SOCKET-FIT-SENSOR`, `SRC-SANDIA-TRIAXIAL-SOCKET`) đều **hiệu chuẩn ngoài** và **liệt kê trôi/tuột cảm biến là lỗi còn tồn**, chưa hệ nào **tự chẩn đoán + tự sửa** độ trôi để tin cậy khi đeo cả ngày.

## Cơ chế mới (điểm khác biệt — phải bảo vệ được)

> **Một liner Velostat giá rẻ dùng chính sự "rẻ" để tạo DỰ PHÒNG: vài ô tham chiếu + nhiễu bơm vào có chủ đích giúp hệ THỜI GIAN THỰC tự chẩn đoán nguyên nhân sai số (nhiệt / creep / trễ / mất tiếp xúc / tuột) và tự bù — thay vì hiệu chuẩn lại từng ô (điều Hopkins gọi là bất khả thi).**

- Đối thủ gần nhất (`SRC-VELOSTAT-CALIB-MATRIX`, "Adaptive Calibration of Piezoresistive…") là **hiệu chuẩn tĩnh / giảm tham số**, KHÔNG phải **tự chẩn đoán nguyên nhân lỗi thời gian thực bằng ô tham chiếu + nhiễu**. **Phải đọc kỹ 2 paper này để khẳng định ranh giới trước khi claim.**

## Vì sao hợp ISEF (chấm theo rubric thật, không phải bar IEEE)

| Tiêu chí ISEF (kỹ thuật) | Điểm ước lượng | Lý do |
|---|---:|---|
| Research Problem (10) | 9 | Vấn đề người khuyết tật có thật, cấp thiết, có tài liệu |
| Design & Methodology (15) | 13 | Thiết kế liner + mạch + thuật toán; phương pháp bench rõ |
| Execution: Construction & Testing (20) | 18 | **Test hoàn toàn trên bench/phantom** (mỏm cụt silicone + tải đã biết), không cần người/IRB/force plate |
| Creativity (20) | 17 | "Biến điểm yếu + độ rẻ của Velostat thành năng lực tự hiệu chuẩn" — góc nhìn khác, đánh trúng gap mà paper IEEE 2020 bỏ ngỏ |
| Presentation (35) | 30 | Demo trực quan: cảm biến thường trôi số khi nóng/creep → hệ **tự bắt lỗi và sửa**; bản đồ áp lực ổn định |
| **Tổng** | **~87/100** | Vượt xa bar; mạnh ở Execution+Presentation (70%) |

## Kế hoạch thực thi (bench-first, an toàn đạo đức)

1. Chế tạo mảng Velostat + điện cực + Mega (ADC) + Orange Pi (Edge-AI suy luận).
2. Phantom mỏm cụt (silicone/3D-print) + tải chuẩn (quả cân) làm ground-truth — **không cần người**.
3. Bơm nhiễu có kiểm soát: gia nhiệt, tải dài (creep), che một phần (mất tiếp xúc), xê dịch liner.
4. Chứng minh: (a) hệ phát hiện + phân biệt đúng loại nhiễu; (b) sau khi bù, sai số/độ trôi giảm rõ so với baseline không bù; (c) cảnh báo áp lực cao **không báo nhầm** khi cảm biến trôi.
5. (Tùy chọn, cần IRB) thử trên người dùng chân giả tình nguyện.

## Kill-test cơ chế — kết quả (2026-08-26)

Đã đọc abstract/record các đối thủ sát nhất:

| Đối thủ | Nó làm gì | Có giết đề tài? |
|---|---|---|
| `SRC-VELOSTAT-CALIB-MATRIX` (Chauhan, IEEE FLEPS 2023) | Hiệu chuẩn **tĩnh** ma trận Velostat NxN bằng 2N tham số (thay 2N²), test trên thảm足 32×32 | Không — hiệu chuẩn lúc chế tạo, không chẩn đoán lỗi lúc chạy |
| `SRC-AISUWARYA-2025-ADAPTCALIB` (IEEE MCSoC 2025) | Hiệu chuẩn **thích nghi** theo kích cỡ cảm biến | Không — vẫn là calibration, không phải tự chẩn đoán nguyên nhân |
| `SRC-DUMMYGAUGE-TEMPCOMP` (IEEE 1997) | Mảng tactile 16 ô, mỗi ô ghép **"dummy gauge"** trong cầu Wheatstone để **bù nhiệt** | Không giết, nhưng **quan trọng**: ý "ô tham chiếu để bù nhiệt" là **kỹ thuật cũ** |
| `SRC-HYBRIDFREQ-2026-VELOSTAT` (Sensors 2026) | Mảng Velostat + FPGA; thừa nhận Velostat trôi, nên **dùng biến thiên tương đối** giữa các kênh thay vì giá trị tuyệt đối | Không giết, nhưng là **cách tiếp cận kề**: né trôi bằng cảm biến tương đối, không chẩn đoán/sửa |

**Kết luận kill-test: đề tài KHÔNG bị giết.** Chưa thấy hệ nào **chẩn đoán đa nguyên nhân (nhiệt/creep/trễ/mất tiếp xúc/tuột) theo thời gian thực + bơm nhiễu có chủ đích + tự sửa từng ô** cho ổ cối chân giả.

**Định vị trung thực (bắt buộc, để không bị bắt bẻ "chỉ là kết hợp"):**
- **Không** claim "ô tham chiếu bù nhiệt" là mới (đã có từ 1997).
- **Không** claim "hiệu chỉnh trôi" là mới (đã có dummy-gauge, relative-sensing, calibration).
- Điểm mới **thật** và **hẹp**: một thiết bị ổ cối Velostat **giá thành thấp, đeo được**, **chủ động bơm nhiễu đã biết** để **nhận diện đúng nguyên nhân** suy giảm (không chỉ bù mù), rồi **tự sửa theo nguyên nhân** và **từ chối cảnh báo khi không tin cậy** — chứng minh trên bench.
- **Phải trích dẫn và phân biệt rõ** cả 4 đối thủ trên trong báo cáo; nếu không sẽ bị quy là "kết hợp A+B+C".

**Điều chỉnh điểm ISEF:** vì cơ chế "mới" hẹp hơn ban đầu (nhiều mảnh đã có), hạ **Creativity 17 → 14**; bù lại Application/Execution/Presentation vẫn mạnh. **Tổng ~84/100** — vẫn đạt, và **rất hợp ViSEF** (application hiếm + nhân văn + demo được). Nhưng với bar IEEE/"cơ chế mới hoàn toàn" của bạn thì nó **không** đạt — cần nói thẳng như vậy.

## Việc còn lại trước khi khóa đề tài
- (Tùy chọn, chắc ăn hơn) đọc **toàn văn** `SRC-VELOSTAT-CALIB-MATRIX` + `SRC-HYBRIDFREQ-2026-VELOSTAT` để trích dẫn chính xác.
- Chốt phạm vi bench + danh sách nhiễu sẽ bơm (nhiệt, tải dài, che ô, xê dịch liner).
- Không claim y khoa; IRB trước mọi thử nghiệm trên người.
