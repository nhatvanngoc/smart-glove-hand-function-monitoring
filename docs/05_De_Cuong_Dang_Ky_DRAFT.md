# ĐỀ CƯƠNG NGHIÊN CỨU KHOA HỌC — BẢN ĐĂNG KÝ VỚI TRƯỜNG (BẢN NHÁP)

> ⚠️ **Bản để nộp là [`DE_CUONG_NOP_TRUONG.md`](DE_CUONG_NOP_TRUONG.md)** (`DEC-PROP-001`). File này là **outline nội bộ** dùng để soạn và đối chiếu; không nộp file này.

> **Trạng thái:** `DRAFT — chờ chủ dự án điền mục in nghiêng` · Ngày soạn: 2026-09-19
> **Dành cho:** phiếu đăng ký đề tài NCKH cấp trường / hồ sơ sơ khảo ViSEF
> **Nguyên tắc viết:** mỗi con số đều có id nguồn trong `research/evidence/SOURCE_LEDGER.csv` kèm **mức đã đọc**; không có số nào là kết quả đo của đề tài ở thời điểm nộp đề cương.
> **Cấm (đã chốt):** "hệ thống đầu tiên", "3–6 tháng vàng", "40–50% khối lượng cơ", "đo góc khớp", "loại bỏ drift", "tái tổ chức vỏ não", "thiết bị tập PHCN", trích dẫn thành tích hội thi.

---

## 1. Tên đề tài

**Tiếng Việt:** *Nghiên cứu và phát triển găng tay thông minh hỗ trợ đánh giá và theo dõi chức năng vận động bàn tay trong phục hồi chức năng sau đột quỵ*

**Tiếng Anh:** *A low-cost smart glove with directional piezoresistive sensing for quantitative hand motor-function assessment and longitudinal monitoring in post-stroke rehabilitation*

**Học sinh:** *[điền]* · **Giáo viên hướng dẫn:** *[điền]* · **Đơn vị:** *THPT [điền]* · **Lĩnh vực dự thi:** *[chủ dự án chọn]* — khuyến nghị của agent: **chính = Hệ thống nhúng (Embedded Systems)**, **phụ = Y sinh & Khoa học sức khỏe**. Lý do: toàn bộ bằng chứng ta có kế hoạch đo là độ lặp/nhiễu/độ trễ/cổng pass-fail (ngôn ngữ của giám khảo kỹ thuật), còn ô Y sinh sẽ mở ra câu hỏi "người bệnh đâu?" mà đề tài **không** được phép trả lời trước phê duyệt đạo đức (xem `research/reviews/2026-09-19_benchmark_xe_lan_ALS_QG2025.md` §4.1)

## 2. Mở đầu — vấn đề bằng số

Sau đột quỵ, phần lớn thời gian phục hồi chức năng bàn tay diễn ra **ở nhà**, không ở bệnh viện. Kỹ thuật viên vật lý trị liệu gặp người bệnh theo lịch thưa; giữa hai lần hẹn là một **hộp đen**: không ai biết người bệnh có tập không, tập đúng động tác không, và tầm vận động **chủ động** thay đổi ra sao.

Ba khoảng trống định lượng được, dùng làm căn cứ chọn đề tài:

| Khoảng trống | Bằng chứng (id · mức đọc) |
|---|---|
| Đánh giá hiện tại là **ảnh chụp rời rạc tại cơ sở y tế** (FMA/ARAT/BBT/NHPT/Jamar), không theo dõi được dọc | `SRC-AMIN-2024-SPASTICITY` (IEEE OJEMB 2024, chuyên gia đồng thuận) · `READ_ABSTRACT` |
| Ngay cả công cụ chuẩn và thiết bị đeo đã kiểm định cũng **nhiễu lớn**: STEF có **MDC95 = 12,7 điểm** (ICC 0,98, n = 53); Manumeter RCT có **MDC ≈ 31%** mức dùng tay trung bình ngày + **100–200 lần đếm nhầm/giờ** | `SRC-STEF-MDC-2026` · `SRC-MANUMETER-RCT-2022` · `READ_ABSTRACT` |
| Găng tay có bán trên thị trường **không làm được cả tầm chủ động và lực trong tầm giá thấp**: đánh giá găng thương mại (VMG-30 + áp lực) cho thấy sai số tầm động lớn và áp lực không cải thiện phân tích tầm | `SRC-VMG30-APPLSCI-2023` · `READ_ABSTRACT` |

*Các con số nền đang dùng trong `A.1` (giữ nguyên, không thêm số mới):* tỷ lệ mắc đột quỵ ở Việt Nam **1.541/100.000 dân** (Farmery et al., SSRN 2024, DOI 10.2139/ssrn.5014421) và **80%** người bệnh có di chứng liệt/yếu chi tay chân (Hendricks et al., *Arch Phys Med Rehabil* 2002;83(11):1629–1637). **Trạng thái trung thực:** cả hai chưa có dòng riêng trong `SOURCE_LEDGER.csv` (`A.1` vẫn đánh dấu *(verify)*) → khi nộp phải kèm nguồn; không thêm con số dịch tễ nào khác nếu chưa có nguồn. Con số địa phương (tần suất lịch hẹn, số người bệnh/phòng) **chờ** phiếu khảo sát KTV (`research/protocols/07`).


**Câu chuyện của đề tài, nói trong một câu:** chúng tôi đo **cái mà kỹ thuật viên cần nhất giữa hai lần hẹn** — *người bệnh tự làm được bao nhiêu so với tầm thụ động, và cần trợ giúp bao nhiêu thì làm xong động tác* — bằng một chiếc găng dùng **nguyên lý cơ học đơn giản, không camera, không IMU, không đo điện cơ**, với **tiêu chí sống/chết công khai và chốt trước khi đo**.

## 3. Mục tiêu và câu hỏi nghiên cứu

| # | Mục tiêu | Câu hỏi tương ứng | Tiêu chí đạt (chốt trước khi đo) |
|---|---|---|---|
| M1 | Chế tạo sensing element áp trở trên vách khung có preload, lặp lại được | Phần tử tự chế có ổn định không? | `GATE 0` (độ lặp R–p, trễ, trôi theo phiên) |
| M2 | Suy luận **dấu** gập/duỗi từ mẫu vách, không encoder/IMU | Hệ phân biệt hướng không? | `GATE A` |
| M3 | Tái tạo tầm vận động **chỉ số** (không quy đổi ra độ) so với ground truth cơ khí | Đủ trung thực để trình bày không? | `GATE B` |
| **M4** ⭐ | Phát hiện **thay đổi chức năng thật** lớn hơn biến thiên của chính hệ đo | Chỉ số có dùng để theo dõi dọc được không? | `GATE C` — **nếu fail thì dừng/đổi trục, không xin xỏ** |
| M5 | Tự phát hiện phiên dữ liệu không tin cậy | Có báo động giả / bỏ sót không? | `GATE D`, `GATE E` |
| M6 | Mô hình nhỏ chạy được tại biên | INT8 có đủ nhanh/đủ đúng? | `GATE F` |

**Giả thuyết trung tâm (🟡, chưa kiểm chứng):** *với preload và hành trình chặn phù hợp, một mảng phần tử áp trở trên vách của khung cứng có thể ghi được nỗ lực co cơ ngay cả khi đầu ngón chưa dịch chuyển, và tách được nỗ lực đó khỏi lực cản co cứng nhờ sự phụ thuộc vận tốc.* Lí do giả thuyết này đứng được — xem `docs/02_Theoretical_Foundation.md` §5.5 (dự toán chuỗi đo + cửa sổ preload).

## 4. Điểm khác biệt so với công trình đã có (bảng bắt buộc, vì chúng tôi không dùng chữ "đầu tiên")

| Hướng đã có | Họ làm gì | Đề tài khác ở đâu |
|---|---|---|
| Phần tử áp trở trên **vách bên** | Lõi đàn hồi + 4 vách CNT/PDMS, phân biệt shear 4 hướng, ngưỡng 128 Pa (pháp tuyến) / 5,28 kPa (shear) — `SRC-SIDEWALL-PIEZO-2015` `READ_ABSTRACT` | Họ: **một phần tử xúc giác cho tay máy**. Ta: **mảng vách trên khung lóng ngón + hiệu chuẩn cơ khí + dùng cho theo dõi chức năng**; ta **không** claim nguyên lý vách là mới |
| Găng vỏ cứng khớp nối + da áp trở | 16 bề mặt chức năng cứng, 2048 taxel @120 Hz, **encoder** cho 22 DoF — `SRC-ARTGLOVE-2026` `READ_ABSTRACT` | Họ đo góc bằng **encoder** và hướng tới robot learning; ta **không encoder**, hướng tới theo dõi tại nhà + cờ độ tin cậy |
| Găng grating/quang học đo góc không IMU | 14 dải cách tử + đầu dò quang; 1,67% FS; RMS < 3,29° — `SRC-GRATING-GLOVE-2021` `READ_ABSTRACT` | Của họ cần cơ cấu dẫn hướng chính xác + quang học; ta dùng **cấu trúc dẫn hướng thô hơn, chỉ để suy luận dấu hướng**, đổi lại mất độ chính xác tuyệt đối — và ta nói thẳng điều đó |
| Găng "gộp" cảm biến góc + lực | SenGlove: 10 flex + 5 pressure + 1 IMU, đặc trưng trên test rig (`SRC-SENGLOVE-2023` `READ_ABSTRACT`) | Đo trên test rig, không có khung thống kê theo dõi dọc; ta đặt **MDC/ICC làm điều kiện sống còn** |
| Găng mềm trợ lực phát hiện ý định (ironHand) | intention detection + lực đỡ **tỉ lệ** với lực người dùng, pressure ở đầu ngón + flex sensor — `SRC-IRONHAND-2018` `PARTIAL` (= JRATE **2016**) + `SRC-IRONHAND-JRM-2018` `READ_ABSTRACT` | Họ: **găng đỡ để cầm nắm (ADL)**, dẫn động bằng cơ cấu. Ta: **không tác động lực lên người**; chỉ **đo** mức trợ giúp cần thiết bằng tải cơ khí đã biết |
| Găng đo nỗ lực/co cứng ở bệnh nhân đột quỵ (19 IMU + bóng áp lực, 14 người, MAS) | `SRC-TW-SPASTICITY-2022` `READ_ABSTRACT` | Của họ: **IMU + phòng thí nghiệm + 19 cảm biến**, nhằm phân mức co cứng. Ta: **áp trở + tại nhà + 12–24 kênh**, nhằm theo dõi **AROM so với PROM**; ta dùng chính bộ đặc trưng của họ (median/IQR/CV/RMS/skewness/main-freq) làm khung trích xuất để so sánh |
| Găng chỉ cảm biến + game phản hồi, đã thương mại (Neofect, ~1.925 USD) | `SRC-NEOFECT-SMARTGLOVE` `UNVERIFIED` (nhà sản xuất) | Ta **thấp hơn nhiều về phần cứng** và **thêm lớp định lượng cơ khí** (RAL) mà họ không đo |

## 5. Phương pháp (tóm tắt)

1. **Vật liệu & phần tử:** Velostat + đồng lá + khung in 3D có preload; đo `R(p)` trên máy kéo tự chế → chọn điện trở tải `R_f` (khóa `GATE 0`).
2. **Mạch đọc:** ESP32-S3 + CD74HC4067, 12 kênh tối thiểu / 24 kênh ở cấu hình vi sai; đồng pha theo kênh để giảm trôi (không dùng chữ "loại bỏ drift").
3. **Suy luận hướng:** hiệu hai vách đối diện `d = S_palmar − S_dorsal`; dấu của `d` + mẫu kích hoạt trên chuỗi vách → dấu gập/duỗi. **Không** ADC→newton, **không** ADC→độ.
4. **Ba chỉ số lấy từ lý thuyết tập chủ động có trợ lực** (`docs/02` §7.3): `Effort Index`, `GAP AROM−PROM`, `RAL` — mỗi chỉ số có đơn vị riêng và có bảng **những điều cấm suy diễn**.
5. **Rig E4 (bắt buộc):** lóng ngón cơ khí + lò xo + puli tải treo (nấc tải hiệu chuẩn bằng lực kế) + **≥ 2 tốc độ kéo** để kiểm tra bộ lọc co cứng. Toàn bộ số liệu của đề cương nằm ở đây.
6. **E5:** một servo **chỉ** điều khiển rig (không tiếp xúc người) để đóng vòng khép kín và đo độ trễ.
7. **E6:** tầng sinh liều tập + gắn cờ phiên `UNRELIABLE` + báo cáo tuần cho kỹ thuật viên.
8. **Thống kê:** ICC/SEM/MDC cho mọi chỉ số; baseline là **chính người dùng ở tuần 0**; so trong-person, không so between-person.
9. **Người tham gia:** chỉ phantom/rig trong giai đoạn này. Mọi đo trên người (kể cả người khỏe tình nguyện) **chờ phê duyệt IRB/SRC** theo quy định cuộc thi.

## 6. Sản phẩm dự kiến

1. Bộ găng + khung + firmware + dashboard nguồn dữ liệu thô (mọi phiên log thô, có timestamp, không sửa).
2. Báo cáo kết quả: **bảng 6 con số tự đo** (`research/reviews/…_scope_options.md` §12) + ngưỡng PASS/FAIL công khai + **nói rõ cổng nào fail nếu fail**.
3. Báo cáo toàn văn **15–20 trang** với **≥ 1 ô trình bày (hình/bảng) cho mỗi ~0,75 trang**, mỗi mục tiêu M1–M6 có **đúng một** con số tự đo đặt cạnh tiêu chí; tài liệu lý thuyết chỉ chiếm **~2 trang**.
3. Toàn bộ ledger công khai trong repo: nguồn đã đọc ở mức nào, claim nào còn treo, quyết định nào do ai chốt. *(Đây là điểm khác biệt về phương pháp — nên đưa vào phần trình bày với hội đồng.)*

## 7. Tính khả thi & tiến độ

| Giai đoạn | Nội dung | Thời lượng |
|---|---|---|
| P0 (đang làm) | Cơ sở lý thuyết + mô hình chuỗi đo + khóa ngưỡng GATE | *[điền]* |

**Điều kiện vật chất đã sẵn (không phải hứa hẹn):** đã có **Velostat, copper tape, ESP32-S3, Orange Pi 5 Pro RK3588** — phần lớn chi phí phần cứng không nằm trong đề tài. Khoản còn lại cho giai đoạn hiệu chuẩn là **vật tư tiêu hao + in 3D + khối lượng chuẩn** (vài trăm nghìn đồng). Ghi trung thực: thiết bị *được cung cấp/đã có*, **không** phải "tổng chi phí đề tài = 0", và hồ sơ **không** nêu con số tiền nếu chưa có hoá đơn (xem `research/context/EQUIPMENT_AND_ACCESS.md`).
| P1 | `GATE 0`: đặc trưng `R(p)`, chọn `R_f` | 1–2 tuần |
| P2 | `GATE A/B`: hướng + tầm chỉ số | 2 tuần |
| P3 | `GATE C` ⭐ + rig E4/E5 + bộ 6 con số | 2–4 tuần |
| P4 | `GATE D/E/F` + tầng kê đơn E6 | 1–2 tuần |
| P5 | Viết báo cáo + poster + demo | 2 tuần |

Vật tư chính: Velostat, đồng lá, PLA/TPU in 3D, ESP32-S3, CD74HC4067, tải + lò xo + puli + 1 servo, lực kế lò xo. *[chủ dự án điền bảng giá + nguồn mua]*

## 8. Rủi ro đã lường trước (và cách đề tài tự xử)

| Rủi ro | Nếu xảy ra |
|---|---|
| Vật liệu tự chế trôi/lặp kém | `GATE 0` fail → chỉ báo cáo "chứng minh khả năng chế tạo", không nói gì về lâm sàng |
| Không phân biệt được hướng | `GATE A` fail → bỏ tính năng hướng, giữ biên độ + nhịp |
| Thay đổi thật không vượt được nhiễu | `GATE C` fail → **đổi trục hoặc dừng**; không xin xỏ bằng cách hạ ngưỡng sau khi thấy số |
| Bộ lọc co cứng không phân biệt được với gồng chủ ý | chỉ số `EI`/`EI_v` bị loại; đề tài quay về đo chuyển động |
| Không có cơ sở y tế đồng hành / chưa có IRB | **không** thử trên người; mọi tuyên bố lâm sàng để ở tầng giả thuyết (đây là giới hạn, không phải thiếu sót ẩn) |

## 8b. Ba chỗ chủ dự án nên cân nhắc sửa khi viết bản chính thức (agent đề xuất — không tự sửa `A.1`/`A.3`)

1. **`A.1` đang viết:** “…ghi nhận lực và hướng chuyển động của từng ngón tay, từ đó **tái tạo mô hình bàn tay 3D** và **đánh giá chức năng vận động**…”. Theo `docs/01` §4.1 và `CLM-NOV-001` (PROPOSED), câu này **vượt quá** bằng chứng hiện có (chưa hiệu chuẩn ra newton, chưa có mốc 0°). Bản an toàn hơn:
   > “…ghi nhận **mẫu lực tác dụng lên vách** ở mỗi lóng ngón, từ đó **suy luận hướng và thứ tự co duỗi** của từng ngón; mô hình 3D là **tái dựng minh hoạ** từ các chỉ số đó, không phải phép đo góc khớp.”
2. **`A.3` có tiêu chí “phân biệt được ít nhất 3 mức độ suy giảm chức năng” và “tương quan với công cụ đánh giá lâm sàng chuẩn”** — đó là **Tầng B** (cần người bệnh + phê duyệt đạo đức). Khi nộp nên tách: Tầng A = đo được + đồng ý với MAS **trên phantom/rig**; Tầng B = ghi rõ *dự kiến, sau phê duyệt*.
3. **Mọi câu “đánh giá chức năng vận động ngay tại nhà”** nên diễn đạt thành “theo dõi **dữ liệu tập luyện và tầm vận động chủ động** tại nhà” — vì “đánh giá” ngụ ý đã xác nhận giá trị lâm sàng, thứ đề tài **chưa** có.

4. **`A.5` đang nêu rõ quan hệ gia đình với người được tham khảo** → theo `DEC-ROLE-001`, bỏ vế đó (và bỏ mọi chi tiết nhận dạng: tên, số năm kinh nghiệm, quan hệ); chỉ giữ "đã tham khảo ý kiến kỹ thuật viên vật lý trị liệu – phục hồi chức năng". Lý do: nêu quan hệ gia đình sẽ chuyển câu hỏi của giám khảo từ "bạn có tiếp cận lâm sàng không?" sang "số liệu của bạn có bị thiên vị vì người thân không?" — câu sau khó trả lời hơn nhiều, và không cần mở ra.

> Cả ba chỗ sửa này **tăng** sức nặng của hồ sơ trước hội đồng: nói đúng cái đã kiểm chứng được là điểm mạnh, không phải điểm yếu.

## 8c. Triển vọng và trần của đề tài (nói thẳng, không hứa vượt)

- **Nếu cả 7 cổng đều pass:** đề tài để lại ba thứ dùng được cho người khác — **(1)** một cách đo hướng chuyển động không cần encoder/IMU,
  **(2)** một bộ chỉ số theo dõi dọc có kèm ngưỡng nhiễu của chính nó (`MDC`), **(3)** toàn bộ log thô + ledger nguồn công khai. Đây là nền để
  một nhóm khác (hoặc chính em ở giai đoạn sau) đề xuất **pilot trên người bệnh với bệnh viện đối tác + phê duyệt đạo đức** — việc mà một đề tài học sinh **không** được phép làm.
- **Nếu `GATE C` fail:** đề tài **dừng ở đó và nói rõ đã fail**, không hạ chuẩn. Kết quả khi đó vẫn có giá trị: một báo cáo chỉ ra rằng
  áp trở polymer tự chế **không** đủ ổn định để theo dõi diễn tiến theo tuần — đó là thông tin mà y văn đang thiếu (`SRC-CUSTOMGLOVE-REVIEW-2024`).
- **Trần thật của đề tài:** không phải thiết bị y tế, không phải kết quả lâm sàng, không phải "bệnh nhân phục hồi tốt hơn".
  Trần của nó là **một phép đo đáng tin + một khung kiểm chứng công khai**. Em chọn trần đó vì nó là thứ duy nhất em có thể chứng minh được trong thời gian của cuộc thi.

## 9. An toàn & đạo đức

1. Thiết bị đeo **không** truyền lực, **không** kích thích điện, **không** chẩn đoán; là công cụ **đo và theo dõi**.
2. Bộ chấp hành (E5) chỉ tác động lên rig/phantom — **không** thử trên bất kỳ ai, kể cả người nhà.
3. Không thu dữ liệu của người khác trước khi có phê duyệt IRB/SRC + giấy đồng ý; mentor/gia đình ký thay không thay được phê duyệt.
4. Dữ liệu xử lý tại biên, không phụ thuộc mạng; không nêu tên/mã người bệnh trong tài liệu.
5. Đề cương **không** nêu cam kết về hiệu quả lâm sàng — đề tài chỉ cam kết đo được và nói thật kết quả đo.
6. Đã **tham khảo ý kiến chuyên gia vật lý trị liệu – phục hồi chức năng** về tính cấp thiết và về giao thức đo. Theo quyết định của chủ dự án (2026-09-19), hồ sơ **chỉ nêu chung chung, không nêu danh tính**. Chuyên gia **không** là đối tượng đo, **không** là nguồn tuyển người bệnh, và ý kiến chuyên gia là bằng chứng **nhu cầu** — không phải bằng chứng **kết quả**.

## 10. Tài liệu tham khảo (trích từ ledger; mỗi dòng ghi rõ mức đã đọc)

`SRC-AMIN-2024-SPASTICITY` (IEEE OJEMB 2024, DOI 10.1109/OJEMB.2024.3523442) · `SRC-STEF-MDC-2026` (Top Stroke Rehabil 2026, DOI 10.1080/10749357.2026.2628557) · `SRC-MANUMETER-RCT-2022` (Sensors 22(18):6938) · `SRC-TW-SPASTICITY-2022` (Sensors 22(19):7212) · `SRC-SIDEWALL-PIEZO-2015` (Sensors 15(10):25463) · `SRC-ARTGLOVE-2026` (arXiv 2606.16370) · `SRC-GRATING-GLOVE-2021` (Sensors 21(13)) · `SRC-IRONHAND-2018` (J Rehabil Assist Technol Eng 3:2055668316670553) · `SRC-RECONFIG-GLOVE-2023` (Engineering 32:202–216) · `SRC-ZHU-2017-GLOVE` (IROS 2017:6617–6624) · `SRC-SMARTGLOVE-REVIEW-2026` (J Eng Appl Sci 73:246) · `SRC-CUSTOMGLOVE-REVIEW-2024` (arXiv 2403.14393) · `SRC-RAT-META-2022` (J Neuroeng Rehabil) · `SRC-RATULS-2019` (Lancet) · `SRC-KAPS-2017` (J Neuroeng Rehabil) · `SRC-VNM-ANNAM-2022`/`SRC-VNM-REHABTECH-GD-2022` (báo chí trong nước)

> *Ghi chú minh bạch:* mức đọc của từng nguồn được lưu trong `research/evidence/SOURCE_LEDGER.csv` (134 dòng, trạng thái `READ_FULL`/`READ_ABSTRACT`/`UNVERIFIED`). Nguồn nào chưa đọc toàn văn thì **không** được dùng để nêu số liệu trong bài.

---

### Phụ lục A — Những điều đề tài **KHÔNG** nói (nêu thẳng để hội đồng khỏi phải đoán)

| Câu bị loại | Vì sao |
|---|---|
| "Hệ thống đầu tiên theo dõi chức năng tay tại nhà" | đã có găng đo dọc + ứng dụng đánh giá tại nhà trong y văn |
| "Đo góc khớp" | ta suy luận hướng/dấu từ mẫu vách; đơn vị là chỉ số, không phải độ |
| "Loại bỏ drift" | chỉ **giảm ảnh hưởng** ở tầng đồng pha, phần còn lại được định lượng |
| "Thiết bị tập phục hồi chức năng" | thiết bị không tác động lực lên người bệnh |
| "Đã chứng minh tăng tính mềm dẻo thần kinh" | đề tài không đo hoạt động não |
| "Rẻ hơn N lần so với thiết bị y tế" | chưa có báo giá thật có hóa đơn |
| "Giai đoạn vàng 3–6 tháng" / "mất 40–50% khối lượng cơ" | chưa xác minh được nguồn gốc |
