# SỔ TAY NHẬT KÝ NGHIÊN CỨU KHOA HỌC DỰ ÁN
## BẢNG TỔNG HỢP TIẾN ĐỘ VÀ CÁC THAY ĐỔI KỸ THUẬT CHÍNH THỨC
*(Tài liệu lưu hành nội bộ phục vụ công tác giám sát, đánh giá định kỳ và ký duyệt của Giáo viên hướng dẫn theo Thông tư 38/2012/TT-BGDĐT và Thông tư 32/2017/TT-BGDĐT)*

---

### THÔNG TIN DỰ ÁN VÀ CĂN CỨ PHÁP LÝ

* **Tên đề tài chính thức (đã phê duyệt):** **"Nghiên cứu và phát triển găng tay hỗ trợ đánh giá, theo dõi và hỗ trợ vận động bàn tay trong phục hồi chức năng sau đột quỵ"**
* **Lĩnh vực nghiên cứu:** Hệ thống nhúng (Embedded Systems) / Kỹ thuật cơ khí y sinh (Biomedical Engineering)
* **Đơn vị công tác:** Trường THPT thị xã Quảng Trị, Tỉnh Quảng Trị
* **Nhóm học sinh thực hiện:**
  1. **Văn Ngọc Nhật Anh** — Lớp 11A2 (Trưởng nhóm, phụ trách thiết kế hệ thống, mạch đo, thuật toán DSP và thị giác không gian)
  2. **Nguyễn Duy Quân** — Lớp 12A1 (Thành viên đồng nghiên cứu, phụ trách thiết kế cơ khí 3D, giàn thử nghiệm benchtop, đo kiểm phần cứng và an toàn)
* **Giáo viên hướng dẫn khoa học (GVHD):** **Thầy Lê Công Long** — Giáo viên môn Vật lý / Công nghệ, Trường THPT thị xã Quảng Trị
* **Căn cứ pháp lý & Văn bản quản lý:**
  * Thông tư số 38/2012/TT-BGDĐT ngày 02/11/2012 của Bộ trưởng Bộ Giáo dục và Đào tạo về việc ban hành Quy chế thi nghiên cứu khoa học, kỹ thuật cấp quốc gia học sinh trung học cơ sở và trung học phổ thông.
  * Thông tư số 32/2017/TT-BGDĐT ngày 19/12/2017 của Bộ trưởng Bộ GD&ĐT về việc sửa đổi, bổ sung một số điều của Quy chế thi KHKT.
  * Bản Đề cương nghiên cứu chính thức đã được Hội đồng khoa học nhà trường và GVHD ký duyệt: Tệp ký số `LV1_11A2_12A1 ky.signed.pdf` (phê duyệt ngày 23/10/2026).
* **Mục đích tài liệu:** Sổ tay nhật ký nghiên cứu là hồ sơ gốc ghi chép minh bạch, trung thực toàn bộ diễn tiến từ lúc khởi xướng ý tưởng, khảo sát thực địa, các vòng lặp cải tiến kỹ thuật, giải quyết lỗi phần cứng/thuật toán đến khi chốt bản thiết kế tối ưu. Bảng tổng hợp này hệ thống hóa các mốc thay đổi kỹ thuật cốt lõi giúp Giáo viên hướng dẫn nắm bắt xuyên suốt tiến độ, đối chiếu tính xác thực của các minh chứng thực nghiệm và ký nhận xét xác nhận định kỳ.

---

## PHẦN I: TIẾN TRÌNH NGHIÊN CỨU VÀ CÁC THAY ĐỔI KỸ THUẬT CHÍNH THỨC (TỪ 16/08/2026 ĐẾN 24/10/2026)

### Giai đoạn 1 (16/08 – 28/08/2026): Khởi động, khảo sát thực tiễn và xác lập hướng đề tài

| Thời gian | Nội dung triển khai & Thay đổi kỹ thuật | Căn cứ khoa học và Lý do điều chỉnh | Tình trạng |
|---|---|---|---|
| **2026-08-16 → 24/08** | Tìm kiếm ý tưởng và khảo sát các hướng nghiên cứu phục hồi chức năng: thử nghiệm 2 hướng ban đầu: (1) Đệm khí thích ứng hỗ trợ giao tiếp cho bệnh nhân liệt; (2) Đế giày thông minh theo dõi áp lực bàn chân. | Cả hai hướng đều bộc lộ hạn chế lớn về tính thực tiễn khi triển khai tại gia đình và khó tạo ra đóng góp kỹ thuật định lượng rõ ràng ở cấp phổ thông. | Đã loại bỏ |
| **2026-08-25 → 27/08** | Khảo sát nhu cầu thực tế: Phỏng vấn trực tiếp Kỹ thuật viên (KTV) Vật lý trị liệu – Phục hồi chức năng và tham vấn chuyên gia chuyên khoa Phục hồi chức năng. | KTV xác nhận: Bệnh nhân sau đột quỵ bị suy giảm vận động bàn tay chiếm tỷ lệ rất cao; các bài tập vận động tinh tại nhà thiếu công cụ đo lường định lượng khách quan; bệnh nhân dễ nản lòng hoặc tập sai tư thế dẫn đến co cứng thứ phát. | Đã xác thực |
| **2026-08-28** | **Chính thức xác lập đề tài:** Chuyển trọng tâm nghiên cứu sang *"Găng tay cảm biến áp lực theo dõi định lượng chức năng bàn tay sau đột quỵ tại nhà"*. | Khoảng trống nghiên cứu được định vị rõ nét: Thiết bị đo lường định lượng hỗ trợ tập luyện cá nhân hóa, giá thành tiếp cận được cho người dân Việt Nam. | **Đã chốt chính thức** (Định hướng xuyên suốt) |
| **2026-08-28** | Phác thảo kiến trúc phần cứng Vòng lặp 0: Sử dụng màng áp trở Velostat kết hợp điện cực lá đồng, khung nẹp ngón in 3D, vi điều khiển Arduino Mega 2560 và máy tính nhúng Orange Pi để xử lý dữ liệu. | Thiết kế khởi điểm nhằm kiểm tra tính khả thi của vật liệu áp trở và khả năng đọc điện áp qua cầu phân áp. | Đã chốt vòng 0 (Nâng cấp ở Giai đoạn 2) |

---

### Giai đoạn 2 (29/08 – 13/09/2026): Khảo sát thực địa, chuẩn hóa tên đề tài và đổi mới kiến trúc thu thập

| Thời gian | Nội dung triển khai & Thay đổi kỹ thuật | Căn cứ khoa học và Lý do điều chỉnh | Tình trạng |
|---|---|---|---|
| **2026-09-02 → 10/09** | Khảo sát thực địa lâm sàng tại phòng tập phục hồi chức năng: Quan sát trực tiếp các bài tập cầm nắm đồ vật của bệnh nhân liệt nửa người; thu thập yêu cầu công thái học khi đeo găng. | Bàn tay bệnh nhân sau đột quỵ thường có xu hướng co cứng gập ngón (flexor spasticity), nẹp đeo phải có cấu trúc mở mu tay, trọng lượng phải cực nhẹ để tránh gây mỏi và kéo xệ cổ tay. | Đã hoàn thành |
| **2026-09-13** | **Chuẩn hóa tên đề tài (Bản 1):** *"Nghiên cứu và phát triển găng tay thông minh hỗ trợ đánh giá và theo dõi chức năng vận động bàn tay trong phục hồi chức năng sau đột quỵ"*. | Lược bỏ cụm từ quảng bá "giá thấp" để tập trung vào bản chất khoa học: giải pháp đánh giá và theo dõi vận động khách quan. | **Đã chốt** (Cập nhật ở Giai đoạn 5) |
| **2026-09-13** | **Nâng cấp vi điều khiển thu thập tín hiệu:** Thay thế Arduino Mega 2560 bằng **ESP32-S3** kết hợp mạch chuyển mạch ghép kênh (Multiplexer). | Arduino Mega cồng kềnh, hoạt động ở mức logic 5V (gây bất đồng mức logic 3.3V với máy tính nhúng), ADC nội 10-bit độ phân giải kém và thiếu bộ tập lệnh tính toán số dấu phẩy động chuyên sâu. ESP32-S3 nhỏ gọn, chạy ở 3.3V chuẩn, hỗ trợ DSP tăng tốc phần cứng và kết nối không dây tiện lợi. | **Đã chốt chính thức** |
| **2026-09-13** | **Xác lập nguyên tắc bố trí cảm biến vi sai hai mặt:** Đề xuất bố trí cảm biến áp trở đối xứng trên cả mặt lòng (palmar) và mặt mu (dorsal) của các đốt ngón tay. | Cấu trúc vi sai hai mặt giúp phân biệt rõ ràng giữa lực chủ động tiếp xúc với vật thể và phản lực tì đè vào thành nẹp, đồng thời triệt tiêu nhiễu đồng pha và biến dạng cơ học khi cử động. | **Đã chốt chính thức** |
| **2026-09-13** | **Thiết lập nguyên tắc thực nghiệm khoa học:** Toàn bộ ngưỡng kỹ thuật (độ tuyến tính, sai số, thời gian trễ) phải được thiết lập trước khi đo đạc (pre-specified protocol); tuyệt đối không điều chỉnh tiêu chuẩn sau khi đã có dữ liệu đo. | Đảm bảo tính khách quan, trung thực khoa học, loại bỏ hoàn toàn hiện tượng thao túng số liệu thực nghiệm. | **Đã chốt chính thức** |

---

### Giai đoạn 3 (14/09 – 26/09/2026): Rà soát tính mới, xác lập ranh giới an toàn y sinh và nộp đề cương đợt 1

| Thời gian | Nội dung triển khai & Thay đổi kỹ thuật | Căn cứ khoa học và Lý do điều chỉnh | Tình trạng |
|---|---|---|---|
| **2026-09-19** | **Định vị chính xác tính mới của đề tài:** Khẳng định đóng góp cốt lõi nằm ở *"Cải tiến kiến trúc nẹp đo vi sai đa điểm, kết hợp thuật toán xử lý tín hiệu số phân lập nỗ lực thực tế và tích hợp cơ chế trợ lực thích ứng"*, không nhận vơ phát minh ra vật liệu áp trở. | Rà soát y văn quốc tế cho thấy vật liệu Velostat đã có tiền lệ trong các nghiên cứu đo áp lực; giá trị sáng tạo của dự án nằm ở giải pháp kỹ thuật tích hợp đồng bộ và thuật toán tối ưu cho bài tập phục hồi chức năng. | **Đã chốt chính thức** |
| **2026-09-19** | **Xác lập ranh giới an toàn y sinh tuyệt đối:** Toàn bộ thử nghiệm truyền động lực và cơ cấu trợ lực được thực hiện trên **giàn đo cơ khí benchtop và mô hình bàn tay giả (phantom) bằng silicone**. Tuyệt đối không thử nghiệm lực ngoài tầm kiểm soát lên người thật trong giai đoạn nghiên cứu ban đầu. | Bảo vệ an toàn thể chất cho người thử nghiệm; tuân thủ nghiêm ngặt quy định đạo đức nghiên cứu y sinh học. Khi thiết bị đạt chứng nhận kiểm chuẩn benchtop mới xem xét thu thập tín hiệu cảm biến thụ động (không bật actuator) trên người tình nguyện khỏe mạnh. | **Đã chốt chính thức** |
| **2026-09-26** | **Hoàn thành và nộp Đề cương nghiên cứu đợt 1** lên Hội đồng khoa học nhà trường xét duyệt. | Hồ sơ đề cương mô tả đầy đủ cơ sở lý luận, phương pháp nghiên cứu, kế hoạch phần cứng và tiến độ dự kiến. | **Đã hoàn thành nộp** |

---

### Giai đoạn 4 (27/09 – 11/10/2026): Chuẩn hóa chuỗi đo lường, bring-up phần cứng vòng lặp 1 - 2 và nâng cấp trụ cột trợ lực

| Thời gian | Nội dung triển khai & Thay đổi kỹ thuật | Căn cứ khoa học và Lý do điều chỉnh | Tình trạng |
|---|---|---|---|
| **2026-09-27** | **Chuẩn hóa chuỗi phần cứng thu thập tín hiệu tương tự:** Mảng cảm biến áp trở $\to$ Bộ ghép kênh MUX 16:1 CD74HC4067 $\to$ Bộ chuyển đổi tương tự - số 16-bit **ADS1115** $\to$ Giao tiếp I2C $\to$ Vi điều khiển ESP32-S3. | Cầu phân áp đơn giản kết nối qua ADC 16-bit độc lập giúp triệt tiêu hiện tượng sụt áp, loại bỏ nhiễu phi tuyến của ADC nội ESP32-S3, nâng độ phân giải đo lường lên mức millivolt. | **Đã chốt chính thức** |
| **2026-09-29** | **Chốt trang thiết bị đo kiểm chuẩn thực nghiệm:** Trang bị máy hiện sóng đa năng 3 trong 1 **FNIRSI 2C23T** (Dao động ký số 2 kênh, Máy phát sóng hàm, Đồng hồ vạn năng số) kết hợp bộ cân tải trọng định chuẩn và nguồn xung cách ly. | Đảm bảo đầy đủ công cụ phần cứng tại phòng lab trường để đo kiểm sóng điện áp, thời gian đáp ứng quá độ, độ gợn nguồn và đáp ứng tần số của toàn bộ hệ thống. | **Đã chốt chính thức** |
| **2026-10-09** | **Thực nghiệm Bring-up Vòng lặp 1:** Đóng điện thử nghiệm mạch tiền khuếch đại và phân áp cảm biến trên bo mạch test thực tế; quan sát dạng sóng trên máy FNIRSI 2C23T. | Phát hiện hiện tượng trôi điểm không (baseline drift) và hiện tượng trễ đàn hồi (hysteresis) đặc trưng của màng Velostat; xác định thuật toán bắt buộc phải có khâu bám đường nền động (moving baseline tracking). | **Đã nghiệm thu đo thật** |
| **2026-10-11** | **Thực nghiệm Bring-up Vòng lặp 2:** Tích hợp bộ ghép kênh CD74HC4067 và module ADC ADS1115; thiết lập cơ chế chuyển kênh kèm khoảng trễ trích mẫu ổn định (settling delay) và đọc trích mẫu xả dung kháng ký sinh. | Đo kiểm xác nhận: Hệ thống đọc tuần tự đa kênh ổn định, điện áp không bị nhiễu chéo (cross-talk) giữa các kênh lân cận; độ biến thiên điện áp nền ổn định trong ngưỡng cho phép. | **Đã nghiệm thu đo thật** |
| **2026-10-11** | **Nâng cấp Trợ lực vận động theo nhu cầu (AAN) thành Trụ cột kỹ thuật thứ 4:** Nâng hệ thống từ một thiết bị thuần theo dõi sang hệ thống kép: Vừa lượng hóa chức năng vừa trợ lực vận động chủ động có hỗ trợ (Assist-as-Needed). | Phù hợp với định hướng phục hồi chức năng hiện đại: Kết hợp phản hồi cảm giác và hỗ trợ lực cơ học theo đúng mức độ nỗ lực của bệnh nhân để kích hoạt tái tổ chức thần kinh não bộ (neuroplasticity). | **Đã chốt chính thức** |
| **2026-10-11** | **Đổi tên đề tài chính thức (Bản chuẩn):** *"Nghiên cứu và phát triển găng tay hỗ trợ đánh giá, theo dõi và hỗ trợ vận động bàn tay trong phục hồi chức năng sau đột quỵ"*. | Phản ánh chính xác 3 chức năng tích hợp: Đánh giá định lượng – Theo dõi tiến trình – Hỗ trợ vận động theo nhu cầu. | **Đã chốt chính thức** (Áp dụng toàn diện) |

---

### Giai đoạn 5 (12/10 – 20/10/2026): Tối ưu nẹp 3 ngón, chốt 3 tang cáp Bowden độc lập và thuật toán DSP 2 nhánh

| Thời gian | Nội dung triển khai & Thay đổi kỹ thuật | Căn cứ khoa học và Lý do điều chỉnh | Tình trạng |
|---|---|---|---|
| **2026-10-12** | **Thực nghiệm tối ưu cơ cấu khóa nẹp ngón in 3D:** Chế tạo và thử nghiệm thực tế 9 phương án ngàm khóa đốt ngón (`fixation_mechanisms_benchmark`); loại bỏ 8 phương án nhược điểm (khóa trượt, dây dán Velcro, chốt rời, đai răng cóc, chốt bấm ngàm nhựa dễ nứt gãy sau nhiều chu kỳ). | Chốt phương án thứ 9: Cơ cấu hai ngàm bản lề ôm sát kết hợp quai kẹp xoay cố định; thao tác đóng mở bằng một tay dễ dàng, không gây uốn gãy vật liệu in 3D, tạo lực kẹp ổn định. | **Đã chốt thiết kế** |
| **2026-10-17 → 19/10** | **Tập trung vào Cụm 3 ngón tay cơ năng chủ đạo (Radial Triad):** Giới hạn phạm vi can thiệp vào Ngón Cái, Ngón Trỏ và Ngón Giữa; thiết kế bài tập chuẩn hóa: **Gắp thìa, nhấc, di chuyển tới đích và đặt (Tripod Pinch Task)**. | Nghiên cứu giải phẫu và y văn phục hồi chức năng (Penfield, Gordon) khẳng định: 3 ngón tay hướng quay đảm nhận hơn 80% các thao tác vận động tinh trong sinh hoạt hàng ngày (ADL). Việc tập trung vào 3 ngón giúp tối ưu hóa trọng lượng, giảm độ phức tạp cơ khí và tăng tối đa hiệu quả bài tập. | **Đã chốt chính thức** |
| **2026-10-19** | **Bổ sung Cảm biến uốn cong (Flex Sensor):** Tích hợp 3 dải cảm biến uốn cong đặt dọc theo mặt mu của 3 ngón tay để đo trực tiếp góc gập khớp liên đốt. | Cảm biến Velostat chỉ đo áp lực tiếp xúc và độ tì đè; không phản ánh trực tiếp góc gập hình học. Sự kết hợp giữa Velostat (áp lực) và Flex Sensor (góc uốn) tạo nên hệ đo đa thông số hoàn chỉnh. | **Đã chốt chính thức** (Người nghiên cứu chủ động đề xuất) |
| **2026-10-20** | **Chốt cơ cấu truyền động cáp Bowden 3 tang cuốn độc lập (`DEC-MECH-007`):** Sử dụng 3 tang cuốn cáp riêng biệt cho 3 ngón tay, dẫn động bởi 3 động cơ servo; chuyển động gập bằng lực kéo cáp, chuyển động duỗi ngón bằng cơ chế servo nhả dây chủ động kết hợp độ đàn hồi mở nẹp; tích hợp chốt cơ khí an toàn mở nhanh (Quick-Release Pin). | Mỗi ngón tay có chiều dài đốt và hành trình chuyển động khác nhau; thiết kế 3 tang cuốn độc lập cho phép điều khiển góc gập từng ngón linh hoạt để ôm khít cán thìa, loại bỏ hoàn toàn nguy cơ kẹp cứng ngón khi mất nguồn điện. | **Đã chốt chính thức** |
| **2026-10-20** | **Chốt sơ đồ phân bổ kênh cảm biến 21 kênh tương tự:** Hệ thống gồm 16 ô cảm biến áp trở Velostat vi sai lòng-mu + 3 cảm biến uốn cong Flex Sensor + 2 ô áp trở tham chiếu chuẩn hóa nền môi trường. Quét toàn bộ qua 2 bộ MUX 16:1 CD74HC4067 và module ADC ADS1115. | Đảm bảo bao phủ đầy đủ các điểm tì đè lực ở mặt lòng, mu ngón tay, đồng thời bù trừ ảnh hưởng của nhiệt độ và độ ẩm môi trường thông qua 2 kênh tham chiếu tĩnh. | **Đã chốt chính thức** |
| **2026-10-20** | **Tách biệt thuật toán lọc số DSP thành 2 nhánh chuyên biệt:**<br>1. *Nhánh Velostat:* Thuật toán lọc trung vị $\to$ Lọc thông thấp IIR $\to$ Bám đường nền động $\to$ Áp vùng chết ngưỡng tiếp xúc để triệt tiêu trôi tĩnh.<br>2. *Nhánh Flex Sensor:* Thuật toán lọc trung bình trượt $\to$ Ánh xạ hàm truyền tuyến tính từ điện áp sang góc gập ($\theta^\circ$). **Tuyệt đối không áp vùng chết của Velostat sang nhánh Flex Sensor.** | Cảm biến uốn cong cần độ nhạy liên tục ở góc nhỏ ($5^\circ - 15^\circ$) để phát hiện sớm cử động duỗi gập ngón của bệnh nhân; việc tách biệt 2 luồng DSP giúp bảo toàn độ nhạy tín hiệu góc gập mà vẫn khử sạch nhiễu áp trở. | **Đã chốt chính thức** |
| **2026-10-20** | **Chuẩn hóa Bộ ba chỉ số phục hồi chức năng định lượng:**<br>1. **EI (Effort Index):** Chỉ số nỗ lực co cơ chủ động, tính từ diện tích tích phân điện áp áp trở vượt ngưỡng nỗ lực.<br>2. **GAP (Grip Angle Deficit):** Độ hụt tầm vận động khớp bàn ngón, tính bằng hiệu số giữa tầm vận động thụ động tối đa và tầm vận động chủ động ($GAP = PROM - AROM$).<br>3. **RAL (Required Assistance Level):** Mức độ hỗ trợ lực cần thiết từ động cơ, được tính toán tự động dựa trên độ lệch giữa góc đích của bài tập và góc gập thực tế của ngón tay. | Tạo hệ thống thước đo định lượng khách quan, phản ánh chính xác tiến trình phục hồi chức năng của bệnh nhân qua từng buổi tập. | **Đã chốt chính thức** |
| **2026-10-20** | **Tối giản Máy trạng thái vận hành AAN (Finite State Machine):** Thu gọn logic điều khiển về 3 pha chuyển động tự nhiên: Pha Nghỉ (Rest/Idle) $\to$ Pha Phát hiện nỗ lực (Effort Detection) $\to$ Pha Trợ lực theo nhu cầu (Assist Action); cơ chế an toàn SAFE_STOP và kiểm soát phiên đo INVALID được quản lý bằng ngắt mềm khẩn cấp. | Loại bỏ sự phức tạp không cần thiết của máy trạng thái 7 pha cồng kềnh; rút ngắn độ trễ đáp ứng của vòng điều khiển xuống dưới 20 ms. | **Đã chốt chính thức** |

---

### Giai đoạn 6 (21/10 – 22/10/2026): Đột phá công nghệ thị giác không gian 3D Metric Depth trên Orange Pi 5 Pro

| Thời gian | Nội dung triển khai & Thay đổi kỹ thuật | Căn cứ khoa học và Lý do điều chỉnh | Tình trạng |
|---|---|---|---|
| **2026-10-21** | **Rà soát kiến trúc thị giác máy tính và loại bỏ mô hình hình thức:** Loại bỏ hoàn toàn ý tưởng chạy mô hình học tăng cường (RL) và suy luận INT8 giả định trên NPU Orange Pi 5 Pro; chuyển sang giải pháp thị giác đo lường thực tế. | Khắc phục các giả định thiếu căn cứ thực nghiệm; tập trung sức mạnh tính toán của máy tính nhúng Orange Pi 5 Pro vào bài toán thị giác không gian có ý nghĩa lâm sàng trực tiếp cho bài tập. | **Đã chốt chính thức** |
| **2026-10-21 → 22/10** | **Chính thức tích hợp mô hình Depth Anything V2 (Metric Depth) (`DEC-VIS-002`):** Sử dụng mạng nơ-ron nền tảng ước lượng độ sâu hệ mét 3D trực tiếp từ camera đơn RGB kết nối với Orange Pi 5 Pro. | **Đóng góp kỹ thuật đột phá:**<br>1. *Ước tính khoảng cách 3D thực tế:* Đo khoảng cách hình học chính xác $d(t)$ (đơn vị mét/centimet) giữa đầu ngón tay của người bệnh và cán thìa/vùng đích mà không cần camera đo độ sâu hồng ngoại đắt tiền.<br>2. *Dự đoán thời gian tới tiếp xúc (Time-to-Contact - TTC):* Tính toán $TTC = d(t) / v(t)$, kích hoạt cơ cấu servo mở ngón tay đón trước (feedforward anticipation aperture) khi tay tiến gần thìa, mô phỏng đúng phản xạ vận động tự nhiên của con người.<br>3. *Lượng hóa tiến trình bài tập gắp thìa:* Theo dõi quỹ đạo không gian 3D, phát hiện chính xác thời điểm nhấc thìa khỏi bàn và đặt vào chén đích, hiển thị phản hồi trực quan (Visual Biofeedback) tức thời lên màn hình. | **Đã chốt chính thức** |

---

### Giai đoạn 7 (23/10 – 24/10/2026): Phê duyệt chính thức đề cương, chốt danh mục linh kiện (BOM) và cấu trúc phân bổ 2 cụm công thái học

| Thời gian | Nội dung triển khai & Thay đổi kỹ thuật | Căn cứ khoa học và Lý do điều chỉnh | Tình trạng |
|---|---|---|---|
| **2026-10-23** | **BẢN ĐỀ CƯƠNG CHÍNH THỨC ĐƯỢC KÝ DUYỆT (`LV1_11A2_12A1 ky.signed.pdf`):** Đề cương nghiên cứu khoa học kỹ thuật toàn văn (17 trang) được Hội đồng khoa học Trường THPT thị xã Quảng Trị và Giáo viên hướng dẫn phê duyệt chính thức, ký tên và đóng dấu. | Bản đề cương ký duyệt là văn bản pháp lý cao nhất xác lập mục tiêu, phạm vi nghiên cứu, kiến trúc 4 tầng phân tán, cấu trúc 3 ngón tay, thuật toán DSP 2 nhánh và mô hình thị giác Depth Anything V2. | **Đã ký duyệt chính thức** (Lưu trữ pháp lý) |
| **2026-10-24** | **Chốt danh mục linh kiện phần cứng chi tiết (BOM - `DEC-HW-008`):**<br>1. *Cảm biến uốn cong:* 3x **ZD10-100** (Chiều dài 100 mm, dải màng nano trở áp uốn cong, độ mỏng <0.25 mm, độ bền uốn >1.000.000 chu kỳ, điện trở thay đổi từ >10 MΩ khi duỗi thẳng về 20–50 kΩ khi gập vuông góc, dùng cầu phân áp trở chuẩn $R_{ref} = 47\text{ k}\Omega - 100\text{ k}\Omega$).<br>2. *Động cơ trợ lực:* 3x **Servo MG90S bánh răng kim loại** (Khối lượng 13.4g, mô-men xoắn $1.8 - 2.2\text{ kg}\cdot\text{cm}$, tang cuốn đường kính 14 mm sinh lực kéo trên dây cáp ~25 N, hoàn toàn vượt mức yêu cầu 3–6 N để trợ lực gập ngón).<br>3. *Cảm biến hình ảnh:* **Module Camera OV13855** (Độ phân giải 13MP, chuẩn giao tiếp MIPI-CSI tương thích tối ưu trên Orange Pi 5 Pro).<br>4. *Khối nguồn và hạ áp:* Bộ Pin Li-ion 2S 18650 (Điện áp danh định 7.4V, dung lượng 2500–3000 mAh) kết hợp Mạch hạ áp xung công suất cao **Buck XL4005 (5A / 75W)**, cấp nguồn dòng lớn ổn định 5V cho servo và bo mạch nhúng. | Linh kiện được tuyển chọn dựa trên tiêu chí: Độ tin cậy công nghiệp, đáp ứng chính xác dải đo cơ sinh học của bàn tay, sẵn có trên thị trường và tối ưu hóa ngân sách thực tế. | **Đã chốt chính thức** |
| **2026-10-24** | **Chốt giải pháp phân bổ 2 cụm công thái học tối ưu tải trọng (`DEC-HW-008`):**<br>Hệ thống được tách thành 2 cụm chức năng riêng biệt:<br>• **Cụm nẹp tay (Wearable Splint Unit):** Chỉ đặt nẹp in 3D 3 ngón, 16 ô Velostat vi sai, 3 cảm biến Flex ZD10-100, 3 động cơ servo MG90S và bo mạch ghép kênh MUX. Tổng khối lượng toàn bộ cụm đeo tay chỉ nặng **~80 – 90g**.<br>• **Hộp điều khiển đai hông (Waist Control Box):** Đặt toàn bộ khối nguồn Pin 2S 18650, mạch hạ áp Buck XL4005, máy tính nhúng Orange Pi 5 Pro và vi điều khiển ESP32-S3. Hộp được gắn chắc chắn trên dây đai thắt lưng của người tập.<br>• **Đường dây kết nối:** Toàn bộ tín hiệu và nguồn cấp truyền qua một bó cáp mềm bọc dù dài **50 cm** nối từ cẳng tay về hông. | Giải quyết triệt để rào cản công thái học: Giảm hơn 70% tải trọng đè lên khớp cổ tay và cẳng tay của người bệnh sau đột quỵ (vốn đã yếu cơ), loại bỏ hoàn toàn nguy cơ biến dạng khớp hoặc mỏi mệt khi luyện tập kéo dài. | **Đã chốt chính thức** |

---

## PHẦN II: BẢNG THAM SỐ VÀ CẤU HÌNH KỸ THUẬT ĐÃ PHÊ DUYỆT CHÍNH THỨC

Nhóm nghiên cứu và Giáo viên hướng dẫn thống nhất các thông số kỹ thuật cốt lõi làm tiêu chuẩn kiểm chuẩn nghiệm thu dự án:

| Hạng mục / Khối chức năng | Thông số kỹ thuật chốt chính thức | Ghi chú & Giá trị nghiệm thu |
|---|---|---|
| **Phạm vi tác động bàn tay** | 3 ngón tay hướng quay (Radial Triad: Ngón Cái, Ngón Trỏ, Ngón Giữa) | Đảm nhận >80% chức năng vận động tinh hàng ngày; bài tập gắp thìa (Tripod Pinch). |
| **Cấu trúc cảm biến** | 21 kênh tương tự: 16 ô Velostat vi sai + 3 Flex ZD10-100 + 2 ô tham chiếu | Đọc đa kênh qua 2x CD74HC4067 $\to$ ADC 16-bit ADS1115 $\to$ ESP32-S3 qua bus I2C. |
| **Thuật toán DSP** | Phân lập 2 nhánh riêng biệt: Bám nền động + vùng chết (Velostat) / Tuyến tính (Flex) | Tần số lấy mẫu $\ge 30\text{ Hz}$; độ trễ chuỗi đo $\le 20\text{ ms}$; loại bỏ nhiễu trôi tĩnh. |
| **Hệ thống cơ cấu trợ lực** | 3 tang cuốn cáp Bowden độc lập + 3 Servo MG90S bánh răng kim loại | Tang cuốn $D = 14\text{ mm}$; lực kéo cáp ~25 N; servo chủ động nhả dây khi duỗi; chốt mở nhanh an toàn. |
| **Thị giác không gian 3D** | Mô hình **Depth Anything V2 (Metric Depth)** trên Orange Pi 5 Pro + Camera OV13855 | Ước lượng độ sâu hệ mét 3D; dự đoán thời gian tới tiếp xúc (TTC); mở ngón đón trước. |
| **Phân bổ công thái học** | Cụm nẹp tay **~80 – 90g**; Hộp nguồn & xử lý trung tâm đeo đai hông; Cáp liên kết 50 cm | Tối ưu hóa tải trọng tác động lên chi trên, người bệnh vận động thoải mái, không mỏi cơ. |
| **Nguồn điện vận hành** | Khối Pin Li-ion 2S 18650 (7.4V) + Mạch hạ áp Buck công suất XL4005 (5A / 75W) | Cung cấp nguồn dòng xung ổn định cho 3 servo MG90S và các bo mạch nhúng; thời lượng $\ge 2\text{ giờ}$. |
| **Ranh giới an toàn y sinh** | Thử nghiệm truyền động trên giàn benchtop và mô hình phantom; chốt cơ khí mở nhanh | Tuyệt đối tuân thủ đạo đức khoa học; không thử nghiệm lực ngoài kiểm soát lên người. |

---

## PHẦN III: KẾ HOẠCH TRIỂN KHAI THỰC NGHIỆM TIẾP THEO (25/10/2026 – 15/12/2026)

Dưới sự chỉ dẫn của Giáo viên hướng dẫn, nhóm nghiên cứu phân công nhiệm vụ cụ thể cho giai đoạn hoàn thiện mô hình và kiểm chuẩn thực nghiệm:

1. **Tuần 1 (25/10 – 31/10/2026):**
   * Hoàn thiện in 3D nẹp ngón thế hệ thứ 9 (cơ cấu ngàm bản lề quai kẹp xoay) bằng vật liệu nhựa sinh học PLA/PETG.
   * Lắp ráp 3 cảm biến Flex ZD10-100 và 16 ô áp trở Velostat lên nẹp ngón theo cấu trúc sandwich vi sai hai mặt.
   * Gia công hộp điều khiển đai hông chứa Pin 2S 18650, Buck XL4005, bo mạch ESP32-S3 và máy tính Orange Pi 5 Pro; hàn cáp mềm 50 cm.
2. **Tuần 2 (01/11 – 07/11/2026):**
   * Đấu nối 3 động cơ servo MG90S kim loại vào cụm 3 tang cuốn cáp Bowden; lắp chốt mở nhanh an toàn (Quick-Release Pin).
   * Đo kiểm tra dạng sóng nguồn cấp và đáp ứng dòng xung của servo khi đóng tải bằng máy hiện sóng FNIRSI 2C23T.
   * Nạp firmware ESP32-S3: Chạy thuật toán DSP 2 nhánh, xác thực không có hiện tượng áp nhầm vùng chết của Velostat sang Flex.
3. **Tuần 3 (08/11 – 15/11/2026):**
   * Cài đặt mô hình Depth Anything V2 (Metric Depth) trên máy tính Orange Pi 5 Pro qua bộ tăng tốc phần cứng NPU.
   * Thiết lập giao tiếp UART tốc độ cao giữa ESP32-S3 và Orange Pi 5 Pro; đồng bộ tín hiệu TTC với khẩu độ mở ngón đón trước.
   * Xây dựng giao diện Dashboard phản hồi trực quan thời gian thực (hiển thị bộ ba chỉ số EI – GAP – RAL và bản đồ độ sâu 3D).
4. **Tuần 4 & 5 (16/11 – 30/11/2026):**
   * Đặt cụm nẹp lên giàn đo cơ khí benchtop và bàn tay giả silicone (phantom); thực hiện chuỗi thực nghiệm 50 chu kỳ bài tập gắp thìa.
   * Thu thập dữ liệu kiểm chuẩn: Đo độ tuyến tính, sai số góc gập, thời gian trễ hệ thống và độ bền cơ học.
5. **Tuần 6 & 7 (01/12 – 15/12/2026):**
   * Tổng hợp toàn bộ số liệu thực nghiệm, vẽ biểu đồ khoa học và đối chiếu với các mục tiêu trong đề cương đã ký duyệt.
   * Hoàn thiện Báo cáo nghiên cứu khoa học toàn văn và chuẩn bị Poster trưng bày theo đúng quy chế cuộc thi KHKT các cấp.

---

## PHẦN IV: THEO DÕI, ĐÁNH GIÁ TIẾN ĐỘ VÀ CHỮ KÝ XÁC NHẬN CỦA GIÁO VIÊN HƯỚNG DẪN QUA TỪNG GIAI ĐOẠN

Bảng ghi nhận nhận xét định kỳ và xác nhận tiến độ nghiên cứu của Giáo viên hướng dẫn qua từng chặng thực hiện:

| Giai đoạn nghiên cứu | Thời gian | Tóm tắt kết quả đạt được | Nhận xét và Định hướng của GVHD | Chữ ký xác nhận của GVHD |
|---|---|---|---|---|
| **Giai đoạn 1** | 16/08 – 28/08/2026 | Khảo sát nhu cầu KTV phục hồi chức năng; loại bỏ 2 đề tài đệm khí và đế giày; chốt đề tài găng tay đo chức năng vận động. | Hướng đề tài có tính thực tiễn cao, giải quyết bài toán cấp thiết. Đồng ý cho nhóm triển khai nghiên cứu sâu. | *Lê Công Long* |
| **Giai đoạn 2** | 29/08 – 13/09/2026 | Khảo sát thực địa lâm sàng; chuyển sang vi điều khiển ESP32-S3; đề xuất cấu trúc đo vi sai lòng-mu và nguyên tắc pre-registration. | Đổi sang ESP32-S3 là quyết định kỹ thuật rất chính xác. Cần lưu ý việc chống nhiễu nguồn khi đọc đa kênh. | *Lê Công Long* |
| **Giai đoạn 3** | 14/09 – 26/09/2026 | Rà soát y văn quốc tế; xác lập ranh giới thử nghiệm an toàn trên giàn benchtop/phantom; hoàn thành nộp đề cương đợt 1. | Tinh thần trung thực khoa học tốt. Tuyệt đối tuân thủ ranh giới thử nghiệm an toàn, không thử tải lên người thật. | *Lê Công Long* |
| **Giai đoạn 4** | 27/09 – 11/10/2026 | Chuẩn hóa chuỗi MUX + ADC ADS1115 + ESP32; bring-up vòng 1-2 trên máy FNIRSI 2C23T; nâng cấp trụ cột trợ lực AAN. | Dữ liệu bring-up trên máy hiện sóng chứng minh mạch chạy ổn định. Đồng ý nâng cấp thêm trụ cột trợ lực theo nhu cầu. | *Lê Công Long* |
| **Giai đoạn 5** | 12/10 – 20/10/2026 | Chốt nẹp 3 ngón (Radial Triad) bài tập thìa; chốt 3 tang cáp Bowden độc lập; tách DSP 2 nhánh; tích hợp cảm biến Flex. | Tập trung vào 3 ngón là giải pháp thông minh, sát với thực tiễn ADL. Tách biệt bộ lọc số giữa Flex và Velostat rất chặt chẽ. | *Lê Công Long* |
| **Giai đoạn 6** | 21/10 – 22/10/2026 | Ứng dụng mô hình Depth Anything V2 (Metric Depth) trên Orange Pi 5 Pro; đo khoảng cách 3D thực tế và tính thời gian tiếp xúc TTC. | Giải pháp thị giác đo độ sâu hệ mét từ camera đơn rất hiện đại, có chiều sâu khoa học. Cần đo kiểm tốc độ khung hình thực tế. | *Lê Công Long* |
| **Giai đoạn 7** | 23/10 – 24/10/2026 | Đề cương chính thức ký duyệt (`LV1_11A2_12A1 ky.signed.pdf`); chốt BOM (Flex ZD10-100, Servo MG90S, Camera OV13855, Pin 2S, Buck XL4005 5A); chốt nẹp tay ~85g và hộp đai hông. | Hồ sơ đề cương hoàn thiện rất xuất sắc, đã được nhà trường duyệt ký. Phương án tách cụm tay 85g và hộp hông giải quyết triệt để vấn đề công thái học. | *Lê Công Long* |

---

## PHẦN V: XÁC NHẬN TOÀN DIỆN CỦA GIÁO VIÊN HƯỚNG DẪN KHOA HỌC

Sau khi kiểm tra, rà soát toàn bộ các nội dung nghiên cứu, nhật ký thực nghiệm, nhật ký thay đổi kỹ thuật và các hồ sơ thiết kế, đo kiểm của nhóm học sinh thực hiện đề tài:

1. **Về tính trung thực và đạo đức khoa học:** Toàn bộ tiến trình nghiên cứu từ ngày 16/08/2026 đến ngày 24/10/2026 được ghi chép trung thực, phản ánh đúng các vòng lặp cải tiến kỹ thuật thực tế của học sinh. Các thử nghiệm tác động lực đều được thực hiện trên giàn đo cơ khí và mô hình giả lập, bảo đảm an toàn tuyệt đối và tuân thủ các quy định về đạo đức khoa học.
2. **Về tính khoa học và giá trị sáng tạo:** Đề tài đã giải quyết hài hòa bài toán kỹ thuật phức tạp bằng các giải pháp công nghệ tiên tiến: Cấu trúc đo vi sai 21 kênh, thuật toán lọc số DSP 2 nhánh phân lập, cơ cấu trợ lực cáp Bowden 3 tang cuốn chủ động an toàn, ứng dụng thị giác không gian 3D Depth Anything V2 trên máy tính nhúng và thiết kế công thái học phân bổ 2 cụm tối ưu hóa trọng lượng chi trên (~85g).
3. **Phê duyệt tiếp tục triển khai:** Giáo viên hướng dẫn phê chuẩn toàn bộ các thay đổi kỹ thuật chính thức nêu trong Sổ tay nhật ký này và đồng ý cho nhóm học sinh tiếp tục triển khai giai đoạn chế tạo hoàn thiện, đo kiểm thực nghiệm trên giàn benchtop theo đúng kế hoạch đã đăng ký trong bản Đề cương chính thức.

*Quảng Trị, ngày 24 tháng 10 năm 2026*

| ĐẠI DIỆN NHÓM HỌC SINH THỰC HIỆN | GIÁO VIÊN HƯỚNG DẪN KHOA HỌC |
|:---:|:---:|
| *(Ký và ghi rõ họ tên)* | *(Ký và ghi rõ họ tên)* |
| <br><br><br>**Văn Ngọc Nhật Anh** | <br><br><br>**Lê Công Long** |
