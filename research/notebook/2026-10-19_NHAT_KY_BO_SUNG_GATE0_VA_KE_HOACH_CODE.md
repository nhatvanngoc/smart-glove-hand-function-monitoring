# Nhật ký nghiên cứu bổ sung — 2026-10-19: hoàn thiện hồ sơ Gate 0 và lập kế hoạch viết code

**Đề tài:** Nghiên cứu và phát triển găng tay hỗ trợ phục hồi chức năng sau đột quỵ cho vận động tinh *(tên làm việc, chưa chốt tên nộp cuối)*.
**Nhóm thực hiện:** Văn Ngọc Nhật Anh (11A2) + Nguyễn Duy Quân (12A1).
**Giáo viên hướng dẫn (GVHD):** Lê Công Long — THPT thị xã Quảng Trị.
**Căn cứ lập:** Điều 14 Quy chế ban hành kèm Thông tư 84/2026/TT-BGDĐT (nhật ký nghiên cứu, dữ liệu gốc và minh chứng quá trình).
**Quan hệ với các sổ khác:** đây là **mục bổ sung** cho `2026-10-12_SO_TAY_NHAT_KY_NGHIEN_CUU_TOM_TAT.md` (mục 13). Không thay thế sổ tay cũ, không sửa hồ sơ đã nộp.

---

## 13. 2026-10-19 — Lượt làm việc về tài liệu: soạn hồ sơ "chốt bài tập và chốt cách nối cảm biến", lập kế hoạch phần mềm

### 13.1. Nội dung công việc

1. **Soạn tờ yêu cầu bài tập (hồ sơ Gate 0).** Viết rõ bài tập đầu tiên của găng: người tập dùng ngón cái – trỏ – giữa gắp một chiếc thìa, nhấc lên, di chuyển tới vùng đích rồi thả. Liệt kê **những thông số phải chốt** (loại thìa, kích thước, khối lượng, vị trí vùng xuất phát và vùng đích, độ cao nhấc bao nhiêu thì tính là "nhấc", đặt trong vùng đích bao lâu thì tính là thành công, một buổi tập bao nhiêu lần, nghỉ bao lâu) và để **trống toàn bộ**, kèm cột "cần căn cứ gì để điền".
2. **Lập bảng 14 trạng thái của bài tập** (sẵn sàng → tiến lại gần → tiếp xúc → cầm → nhấc → di chuyển → đặt → thả → thành công / rơi / đặt sai / không xác định được), mỗi trạng thái ghi rõ **bằng chứng nào được phép dùng để kết luận** (camera, cảm biến gập, cảm biến áp lực) và phải ghi những trường dữ liệu gì. Quy tắc quan trọng: khi không đủ bằng chứng thì ghi nhận là "không xác định", **không** được suy ra "thất bại".
3. **Lập máy trạng thái chế độ hoạt động** của thiết bị: an toàn/dừng → máy hỗ trợ gập duỗi → đánh giá tiêu chí → chế độ hỗ trợ theo nhu cầu (AAN) → bài tập thìa → trạng thái tín hiệu không tin cậy → trạng thái lỗi. Kèm 5 ràng buộc không được vi phạm (không cần kỹ thuật viên bấm nút chuyển chế độ; camera không được ra lệnh kéo dây; giới hạn hành trình và cơ cấu nhả nằm ở tầng thấp…).
4. **Nêu 5 phương pháp để phân biệt "người tập tự vận động" với "máy kéo tay người tập".** Đây là điểm rủi ro lớn nhất của tính năng tự chuyển chế độ: nếu bộ điều khiển đếm chu kỳ do chính mô-tơ tạo ra thì nó sẽ tự "lên lớp" cho người tập không hề chủ động vận động. Cả 5 phương pháp đều **chưa được chọn và chưa kiểm chứng**.
5. **Soạn bản đồ 16 kênh cảm biến.** Với 3 cảm biến gập (mỗi ngón một chiếc) đã được chủ dự án chốt, tính ra còn **tối đa 13 kênh** cho cảm biến áp lực Velostat và ô tham chiếu — đây là phép trừ, **không phải** con số đã chốt về số miếng Velostat. Lập 4 phương án bố trí (tối thiểu 7 kênh; mỗi ngón 2 miếng đối diện lòng/mu dùng 11 kênh; đọc 3 cảm biến gập thẳng vào 3 ngõ vào còn trống của chip chuyển đổi để giải phóng kênh; đọc cảm biến gập bằng bộ chuyển đổi trong vi điều khiển) kèm bảng so sánh đánh đổi, và đề xuất phương án dùng cho bước kiểm tra cảm biến.
6. **Tính lại ngân sách tốc độ quét.** Dùng đúng những con số nhóm đã ghi lại khi thử mạch thật (chờ ổn định 300 µs sau khi chuyển kênh, một lần đọc nháp, chip chuyển đổi chạy 860 mẫu/giây) để tính: quét 7 kênh ≈ 54 lần/giây, 11 kênh ≈ 35 lần/giây, 16 kênh ≈ 24 lần/giây. **Đây là phép tính, không phải số đo**, phải đo lại trên mạch thật.
7. **Soạn đặc tả nhánh camera.** Chọn cách làm gọn, giải thích được từng bước: camera cố định, trừ nền tĩnh, tách thìa theo màu/marker, bám vật thể, rồi suy ra trạng thái bài tập; phần "nhận vật thể" được thiết kế theo dạng **có thể thay thế** để sau này lắp mô hình học sâu vào nếu số liệu thử cho thấy cách cổ điển không đủ ổn định. Kèm phiếu ghi để đo trên Orange Pi 5 Pro (tốc độ khung, độ trễ, độ đúng từng trạng thái, tỷ lệ "không xác định được", tải CPU/NPU) — **để trống toàn bộ**, chưa đo.
8. **Lập lộ trình viết phần mềm** theo 7 bước: khung dữ liệu và schema → bộ tạo dữ liệu giả/replay để test → firmware đọc cảm biến trên ESP32-S3 → hiệu chuẩn và đặc trưng hoá cảm biến → bộ điều khiển chuyển chế độ → nhánh camera → bàn điều khiển theo dõi buổi thử và sinh báo cáo. Kèm 8 nguyên tắc bất biến khi code, quan trọng nhất là: **không được viết cứng ngưỡng trong code**; ngưỡng chưa chốt phải để trống và chương trình phải **từ chối chạy** ở chế độ đánh giá; dữ liệu mô phỏng phải dán nhãn riêng, không được trộn với số đo thật.
9. **Bổ sung đề cương A/B/C** hai mục: bảng "đăng ký trước" 14 chỉ số (định nghĩa, đơn vị, cách đo, cột ngưỡng để trống, cột căn cứ để điền) và mục nêu thứ tự triển khai công cụ.
10. **Cập nhật sổ sách dự án:** thêm 7 mã quyết định ở trạng thái *đề xuất, chờ duyệt*, 6 luận điểm mới, và ghi chú trạng thái vào các tài liệu điều hành.

### 13.2. Phương pháp thực hiện

- Đọc lại toàn bộ tài liệu điều hành của dự án (hồ sơ định hướng hiện hành, sổ quyết định, sổ luận điểm, kế hoạch triển khai, quy trình thử bench/phantom, quy tắc viết đề cương và hồ sơ văn phong của nhóm) trước khi sửa bất cứ thứ gì.
- Đối chiếu từng phát biểu trong đề cương với quyết định đã chốt của chủ dự án; chỗ nào là **mục tiêu** thì giữ đúng thì/mốc "dự kiến, mục tiêu, chưa đo", không viết thành kết quả.
- Với phần kênh cảm biến và tốc độ quét: lập bảng phương án + bảng đánh đổi, và chỉ dùng những con số nhóm **đã ghi lại từ mạch thật**, có ghi rõ xuất xứ; phép tính tự làm thì dán nhãn "tính toán, phải đo lại".
- Rà câu chữ bằng cách quét các cụm từ dễ vi phạm quy chế ("đầu tiên", "chứng minh hiệu quả", "an toàn tuyệt đối", công thức lực và ngưỡng 5 N đã rút) trên toàn bộ tệp mới và tệp sửa.
- Kiểm tra cấu trúc sau khi sửa: liên kết giữa các tài liệu, tính hợp lệ của sổ luận điểm (số cột, mã không trùng), chạy công cụ kiểm tra mẫu phiếu đo có sẵn trong dự án.

### 13.3. Kết quả từng giai đoạn

| Kết quả | Trạng thái |
|---|---|
| 6 tài liệu mới (tờ yêu cầu bài tập, bản đồ kênh dạng văn bản và dạng bảng, đặc tả camera, lộ trình phần mềm, nhật ký này) | đã soạn xong, **ở mức đề xuất, chờ chủ dự án duyệt** |
| Đề cương A/B/C bản cập nhật lần 2 (thêm 2 mục) | đã sửa, **chưa duyệt, chưa phải bản nộp** |
| Ngưỡng / thông số bài tập / con số an toàn | **không điền số nào** — để trống có chủ đích, kèm cột "căn cứ để điền" |
| Code, firmware, pipeline camera, màn hình theo dõi | **chưa viết** — theo chỉ đạo của chủ dự án là hoàn thiện đề cương trước |
| Phép đo, benchmark, thử trên mạch/bàn thử/phantom | **không thực hiện** trong lượt này |
| Hồ sơ đã nộp và các tệp nguồn trên Drive | **không sửa** |
| Đưa thay đổi lên GitHub | **chưa** — theo yêu cầu của chủ dự án trong lượt này |
| Hai điểm kỹ thuật phát hiện cần kiểm tra | (a) ghi nhận cũ nói mạch đọc toàn dải 0–3,3 V qua chip chuyển đổi ADS1115 — cần đối chiếu giới hạn điện áp đầu vào theo tài liệu hãng và đo lại; (b) bảng tốc độ khung cũ (~415 lần/giây) dựa trên bộ chuyển đổi trong vi điều khiển nên **không áp dụng** cho mạch 16-bit hiện tại |

### 13.4. Việc nhóm cần làm tiếp theo

1. Duyệt hoặc chỉnh 7 mã đề xuất: tờ yêu cầu bài tập; cách phân biệt vận động tự nguyện; bản đồ kênh; tốc độ quét mục tiêu; kiến trúc camera; lộ trình phần mềm; nơi đặt bộ điều khiển chuyển chế độ.
2. Kiểm tra trên mạch thật 8 điểm đã liệt kê (trong đó có: chip chuyển đổi có sẵn 3 ngõ vào còn trống không; điện trở kéo lên cho cảm biến gập phải chọn sau khi đo dải điện trở thật; nhiễu khi mô-tơ servo chạy; quy tắc nối mass để tránh sự cố đoản mạch vòng mass như đã gặp).
3. Chốt **cơ cấu nhả/hồi dây để duỗi ngón** và phương án một tang kéo cả ba ngón hay ba tang riêng — đây là rủi ro cao nhất của bài tập gắp thìa.
4. Thu xếp **thiết bị đo lực/căng dây độc lập** (không dùng Velostat làm chuẩn lực) trước khi thử cơ cấu.
5. Duyệt đề cương bản cập nhật lần 2 rồi mới dựng lại bản Word để rà soát (không ghi đè bản đang có trên Drive).
6. Trả các món nợ cũ: chuyển số liệu thử mạch tháng 10 thành phiếu buổi đo đúng mẫu; tra cứu bằng sáng chế theo phân loại một cách hệ thống; xác nhận việc đổi tên cảm biến nhiệt–ẩm giữa hai bản đề cương; xuất bản vẽ cơ cấu phương án 9 và in thử.

### 13.5. Ghi chú trung thực

- Lượt làm việc này do **công cụ hỗ trợ (agent) soạn theo chỉ đạo của chủ dự án**; nhóm nghiên cứu phải đọc lại, xác nhận và chịu trách nhiệm nội dung trước khi dùng vào hồ sơ.
- Đây **không phải** một lượt phản biện độc lập nhiều chiều, và không được mô tả như vậy.
- Không có bất kỳ phép đo, thử nghiệm phần cứng, benchmark hay dữ liệu người nào được tạo ra trong lượt này. Các con số "tính toán" (ví dụ tốc độ quét) **không phải kết quả đo** và không được trích như kết quả của đề tài.
- Thiết bị chưa được chế tạo hoàn chỉnh, chưa được đánh giá an toàn, chưa thử trên người; không có khẳng định nào về hiệu quả phục hồi, về việc dùng tại nhà đã được xác nhận, hay về tính mới/"đầu tiên".

- **Vai trò thành viên:** ⟨nhóm tự điền — ai yêu cầu, ai đọc lại, ai duyệt từng mục⟩
- **Xác nhận GVHD:** ______________________ (ngày ___/___/2026)
