# Bảng tổng hợp các thay đổi chính thức của đề tài (dành cho GVHD)

**Đề tài:** Nghiên cứu và phát triển găng tay hỗ trợ đánh giá, theo dõi và hỗ trợ vận động bàn tay
trong phục hồi chức năng sau đột quỵ.
**Nhóm thực hiện:** Văn Ngọc Nhật Anh (11A2) + Nguyễn Duy Quân (12A1).
**Giáo viên hướng dẫn (GVHD):** Lê Công Long — THPT thị xã Quảng Trị.
**Ngày biên soạn:** 2026-10-12.

## Mục đích của file này

Đây **không phải** là nhật ký nghiên cứu đầy đủ (bản đầy đủ nằm ở file
`2026-10-12_SO_TAY_NHAT_KY_NGHIEN_CUU_TOM_TAT.md` cùng thư mục, và tài liệu nguồn chi tiết hơn
nữa nằm trong thư mục con `Ho_so_day_du/`). File này là **bảng tóm lược riêng các thay đổi đã
được chốt chính thức** trong suốt quá trình làm đề tài (đổi đề tài, đổi tên, đổi kiến trúc phần
cứng, đổi phạm vi nghiên cứu...), để thầy/cô có thể đọc nhanh một lượt và nắm được đề tài đã biến
đổi như thế nào từ lúc bắt đầu tới nay, không cần đọc lại toàn bộ chi tiết kỹ thuật.

**Quy ước đọc bảng:** cột "Trạng thái" ghi **Đã chốt** nghĩa là thay đổi này đã được nhóm/chủ đề
tài quyết định dứt khoát và đang áp dụng; ghi **Đang chờ duyệt** nghĩa là đây mới là đề xuất, nhóm
hoặc GVHD cần xác nhận lại trước khi coi là chính thức.

---

## Giai đoạn 1 (16/08 – 28/08/2026): Tìm hướng đề tài

| Ngày | Thay đổi | Lý do | Trạng thái |
|---|---|---|---|
| 2026-08-25 → 26 | Bỏ 2 hướng đề tài thử nghiệm ban đầu: (1) "đệm khí thích ứng hỗ trợ giao tiếp", (2) "đế giày thông minh theo dõi lực bàn chân". | Cả hai hướng đều yếu ở tiêu chí "tính hữu ích thực tiễn" khi rà soát kỹ. | Đã chốt |
| 2026-08-28 | **Chốt đề tài hiện tại:** chuyển hẳn từ hướng "theo dõi độ cứng mô bàn chân ở người tiểu đường" sang **"găng tay cảm biến áp lực theo dõi định lượng chức năng bàn tay sau đột quỵ tại nhà"**. | Hướng cũ thiếu bằng chứng khoa học đủ mạnh cho việc theo dõi dài hạn; khoảng trống nghiên cứu mới (theo dõi bàn tay sau đột quỵ) được xác nhận qua một hội thảo chuyên gia quốc tế và một nghiên cứu khác cùng năm. Đồng thời, phỏng vấn trực tiếp một kỹ thuật viên Vật lý trị liệu – Phục hồi chức năng và tham khảo một chuyên gia phục hồi chức năng khác đều xác nhận đây là hướng "đáng làm". | Đã chốt — **không đổi lại từ đây về sau** |
| 2026-08-28 | Phác thảo kiến trúc phần cứng đầu tiên: vật liệu cảm biến áp lực (Velostat) + băng đồng dẫn điện, gắn trên găng in 3D, nối với vi điều khiển Arduino Mega 2560 và một máy tính nhúng Orange Pi xử lý trung tâm. | Thiết kế khởi điểm dựa trên linh kiện sẵn có. | Đã chốt (sau đó đổi một phần ở giai đoạn 2, xem bên dưới) |

## Giai đoạn 2 (13/09/2026): Chốt tên đề tài + đổi kiến trúc thu thập tín hiệu

| Ngày | Thay đổi | Lý do | Trạng thái |
|---|---|---|---|
| 2026-09-13 | **Chốt tên đề tài chính thức (bản đầu):** *"Nghiên cứu và phát triển găng tay thông minh hỗ trợ đánh giá và theo dõi chức năng vận động bàn tay trong phục hồi chức năng sau đột quỵ"*. | Bỏ các cụm nêu công nghệ cụ thể ("hệ thống... giá thấp") vì đó chỉ là phương tiện thực hiện, không phải đối tượng nghiên cứu của đề tài. | Đã chốt (sau đó đổi tên một lần nữa ngày 11/10, xem giai đoạn 5) |
| 2026-09-13 | **Đổi bộ vi điều khiển thu thập tín hiệu:** từ Arduino Mega 2560 sang ESP32-S3, có bổ sung thêm bộ chuyển mạch (giúp đọc được nhiều cảm biến hơn số chân cắm vật lý cho phép). | Mega 2560 có độ phân giải đo thấp hơn, cồng kềnh, không có kết nối không dây, và mức điện áp của nó không khớp trực tiếp với máy xử lý trung tâm (phải qua thêm một mạch chuyển đổi điện áp trung gian). ESP32-S3 giải quyết được cả 3 vấn đề này. | Đã chốt — **giữ nguyên tới nay (10/2026)** |
| 2026-09-13 | Chốt cách bố trí các điểm đo theo 2 giai đoạn: giai đoạn đầu dùng 12 điểm đo (thử nghiệm sơ bộ), giai đoạn sau nâng lên 24 điểm đo (đo đối xứng hai mặt của mỗi khớp ngón tay để xác định hướng gập/duỗi và giảm nhiễu). | Đo đối xứng hai mặt giúp phân biệt được hướng chuyển động chính xác hơn, đồng thời tự triệt được một phần nhiễu tín hiệu chung. | Đã chốt |
| 2026-09-13 | Chốt nguyên tắc: ngưỡng đạt/không đạt của mỗi vòng kiểm tra kỹ thuật phải **quyết định trước khi đo**, cấm điều chỉnh lại sau khi đã xem kết quả đo. | Đảm bảo tính trung thực khoa học, tránh "nhìn kết quả rồi mới đặt tiêu chuẩn" (p-hacking). | Đã chốt — áp dụng xuyên suốt |
| 2026-09-13 | Chốt cách diễn đạt báo cáo: dùng "suy luận hướng gập/duỗi" (không nói "đo góc khớp"); "giảm ảnh hưởng trôi tín hiệu" (không nói "loại bỏ hoàn toàn"); gọi sản phẩm là "găng tay đánh giá và theo dõi" (không gọi là "robot phục hồi chức năng" hay "găng tập phục hồi chức năng"). | Tránh mô tả phóng đại so với khả năng thực tế đã được kiểm chứng của thiết bị. | Đã chốt |

## Giai đoạn 3 (19/09/2026): Rà soát tính mới + chốt phạm vi nghiên cứu + nộp đề cương lần 1

| Ngày | Thay đổi | Lý do | Trạng thái |
|---|---|---|---|
| 2026-09-19 | **Hạ mức tự đánh giá về tính mới của đề tài:** từ "nguyên lý kỹ thuật hoàn toàn mới" xuống "cải tiến cách bố trí + cách lập luận trên nền nguyên lý đã có". | Khi rà soát tài liệu khoa học, phát hiện nguyên lý cảm biến tương tự đã được công bố trước đó (một bài báo khoa học năm 2015). Nhóm chủ động nhìn nhận đúng mức độ mới, không nhận vơ. | Đã chốt |
| 2026-09-19 | **Chốt phạm vi phần "tập luyện chủ động có hỗ trợ":** chỉ thực hiện trên giàn đo cơ khí + mô hình bàn tay giả (phantom) bằng silicone, với một lò xo trợ lực và một động cơ nhỏ kéo mô hình. **Không có bất kỳ lực nào tác động lên ngón tay người thật** ở giai đoạn này. | Giữ an toàn tuyệt đối cho người tham gia; vì không có lực tác động lên người thật nên không cần xin phép hội đồng đạo đức nghiên cứu. Quyết định này đối chiếu với một dự án đã đạt giải ở một cuộc thi khoa học kỹ thuật lớn trước đó, cho thấy việc tổ hợp đúng công nghệ sẵn có kèm minh chứng tự làm vẫn được đánh giá cao, không nhất thiết phải có nguyên lý vật lý hoàn toàn mới. | Đã chốt |
| 2026-09-19 | Quyết định chạy toàn bộ quy trình kiểm tra kỹ thuật đầy đủ các bước, không cắt giảm bớt phần nào (kể cả phần xử lý tín hiệu nâng cao). | Chủ đề tài xác nhận còn đủ thời gian thực hiện trọn vẹn. | Đã chốt |
| 2026-09-19 | Chốt chính sách: **không nêu tên hay thông tin cá nhân** của người được tham khảo ý kiến chuyên môn (kỹ thuật viên Vật lý trị liệu) trong hồ sơ nộp — chỉ ghi chung là "đã tham khảo ý kiến kỹ thuật viên vật lý trị liệu – phục hồi chức năng". | Bảo vệ thông tin cá nhân của người được tham khảo. | Đã chốt |
| 2026-09-19 | Hoàn thiện và **nộp đề cương lần 1 cho trường** (26/09/2026). | — | Đã thực hiện |

## Giai đoạn 4 (27/09 – 29/09/2026): Đồng bộ với đề cương đã nộp + chốt công cụ đo + ngân sách

| Ngày | Thay đổi | Lý do | Trạng thái |
|---|---|---|---|
| 2026-09-27 | Đề xuất cập nhật chuỗi đo lường theo đúng bản đề cương đã nộp trường: cảm biến áp lực → mạch khuếch đại tín hiệu nhỏ (INA333) → bộ chuyển đổi tín hiệu số có độ chính xác cao (ADS1115) → ESP32-S3 → kết nối không dây → Orange Pi. Đồng thời đề xuất bộ tiêu chí đo mới (ký hiệu M1–M6, C1.1–C1.10) thay cho bộ tiêu chí cũ, và đề xuất thu hẹp phạm vi còn 3 ngón tay (cái/trỏ/giữa) thay vì cả 5 ngón. | Khớp đúng với những gì đã viết trong hồ sơ nộp chính thức cho trường. | **Đang chờ duyệt** (tại thời điểm ghi chú này — nhóm cần tự kiểm tra lại trạng thái mới nhất) |
| 2026-09-29 | **Chốt bộ dụng cụ đo lường** sẽ dùng: đồng hồ vạn năng + một máy đo 3 trong 1 (dao động ký + máy phát tín hiệu + đồng hồ đo, model FNIRSI 2C23T) + cân tải trọng 5kg. Đã rà soát và **xác nhận toàn bộ 33 chỉ tiêu đo đặt ra đều có thể đo được** bằng bộ dụng cụ này — không phải loại bỏ chỉ tiêu nào, chỉ loại bỏ một số *câu khẳng định* trong báo cáo không có cơ sở đo thực tế. | Đảm bảo tính khả thi về mặt đo lường trước khi bắt đầu đo. | Đã chốt |
| 2026-09-29 | **Chốt ngân sách vận hành nội bộ dưới 10 triệu đồng** (ước tính 5,5–8,5 triệu, máy Orange Pi đã có sẵn ở trường). Số liệu ngân sách thực tế này **chỉ ghi vào sổ tay nội bộ, không đưa vào báo cáo chính thức** — báo cáo chính thức vẫn giữ nguyên câu "thiết bị đeo dưới 1,5 triệu đồng" (vì đây là chi phí riêng phần thiết bị đeo tay, không tính phần máy trạm xử lý dùng chung). | Minh bạch hoá ngân sách thực tế trong nội bộ nhóm, đồng thời giữ đúng cách trình bày chi phí thiết bị đeo trong báo cáo (tách riêng phần thiết bị cá nhân và phần trạm xử lý dùng chung cho nhiều thiết bị). | Đã chốt |

## Giai đoạn 5 (09/10 – 11/10/2026): Thử nghiệm phần cứng thật lần đầu + loạt quyết định quan trọng

| Ngày | Thay đổi | Lý do | Trạng thái |
|---|---|---|---|
| 2026-10-09 | **Lần đầu tiên đo thử nghiệm trên mạch thật** (không chỉ trên giấy): hiệu chỉnh mạch khuếch đại tín hiệu cảm biến, xử lý một lỗi kỹ thuật khiến tín hiệu bị méo. | Chuyển từ giai đoạn lý thuyết thuần tuý sang có số liệu thực nghiệm sơ bộ đầu tiên. | Đã ghi nhận (số liệu còn ở mức sơ bộ, chưa đủ chuẩn để dùng làm bằng chứng chính thức trong báo cáo — xem mục "Việc cần làm" trong sổ tay đầy đủ) |
| 2026-10-11 | Tiếp tục thử nghiệm thật: tích hợp thêm bộ chuyển đổi tín hiệu số 16-bit và bộ chuyển mạch đọc nhiều cảm biến cùng lúc; xác nhận hệ thống đọc đúng, không bị nhiễu chéo giữa các kênh đo. | Tiếp nối kết quả ngày 09/10, mở rộng từ đo 1 điểm sang đo nhiều điểm cùng lúc. | Đã ghi nhận (số liệu sơ bộ, còn 2–3 điểm kỹ thuật cần xác minh thêm) |
| 2026-10-11 | **Nâng phần "hỗ trợ vận động theo nhu cầu"** (lò xo trợ lực + 1 động cơ nhỏ kéo mô hình tay giả) thành **một trong 4 trụ cột kỹ thuật chính thức** của đề tài (ngang hàng với mảng cảm biến, bộ chỉ số đánh giá, và lớp tự kiểm chuẩn). **Ranh giới an toàn không đổi:** phần này vẫn chỉ chạy trên giàn đo + mô hình tay giả, không bao giờ tác động lực lên người thật. | Theo định hướng của chủ đề tài, nêu rõ đây là một trong những trọng tâm kỹ thuật cốt lõi cần làm nổi bật trong đề tài. | Đã chốt |
| 2026-10-11 | **Đổi tên đề tài lần 2 (tên hiện hành):** *"Nghiên cứu và phát triển găng tay hỗ trợ đánh giá, theo dõi và hỗ trợ vận động bàn tay trong phục hồi chức năng sau đột quỵ"* — so với tên cũ (13/09), bỏ chữ "thông minh", và đổi "đánh giá và theo dõi chức năng vận động" thành "đánh giá, theo dõi và hỗ trợ vận động" (để phản ánh đúng trụ cột mới ở trên). **Tên mới chỉ áp dụng cho tài liệu từ 11/10/2026 trở đi, không thay đổi ngược lại các hồ sơ đã nộp trước đó** (hồ sơ đã nộp ngày 26/09 vẫn giữ nguyên tên cũ). | Phản ánh đúng phạm vi kỹ thuật mới của đề tài sau khi nâng trụ cột thứ 4. | Đã chốt |
| 2026-10-11 | Bổ sung một phần cơ sở lý thuyết thần kinh học, giải thích vì sao đề tài chọn bàn tay làm đối tượng nghiên cứu (dựa trên bản đồ vùng não điều khiển vận động/cảm giác — một nghiên cứu kinh điển năm 1937 và một nghiên cứu hiện đại hơn năm 2023). **Lưu ý:** đề tài không đo hay chứng minh hoạt động não bộ, phần này chỉ là nền tảng lý thuyết giải thích, không phải phần thực nghiệm của đề tài. | Làm rõ nền tảng khoa học cho việc chọn "bàn tay" (so với các bộ phận khác của cơ thể) làm đối tượng theo dõi. | Đã chốt |
| 2026-10-11 | Mở rộng phần so sánh giữa loại cảm biến đề tài đang dùng (Velostat) với một loại cảm biến khác thường thấy trong y học (cảm biến điện cơ – sEMG), thành 5 khía cạnh so sánh: chi phí, so với các loại cảm biến khác, hạn chế vật liệu đã biết, độ tin cậy ở nhóm bệnh nhân đột quỵ, và tiền lệ sử dụng loại cảm biến này trong các nghiên cứu khác. | Làm chặt chẽ và có cơ sở hơn lý do lựa chọn công nghệ cảm biến của đề tài. | Đã chốt |

## Giai đoạn 6 (trước 12/10/2026, trưởng nhóm báo cáo ngày 12/10): Thử nghiệm cơ cấu đóng/mở nẹp ngón tay

| Ngày | Thay đổi | Lý do | Trạng thái |
|---|---|---|---|
| Trước 2026-10-12 (ngày thực hiện chính xác chưa xác nhận) | Thiết kế và in thử thực tế **9 phương án cơ cấu khác nhau** để đóng/mở, giữ chặt vỏ nẹp quanh một đốt ngón tay (khác với phần bản lề nối giữa các đốt đã chốt trước đó). Loại dần 8 phương án đầu (vòng kẹp lò xo, khóa trượt, dây đai Velcro, chốt rời, khóa cài, dải đai răng cóc, bản lề kép thanh đòn, khóa bấm ngàm) vì các lý do quan sát thực tế trên vật in thử (lực yếu, khó thao tác một tay, dễ rơi, mỏi/nứt vật liệu...). | Mỗi phương án đều có nhược điểm thực tế cụ thể phát hiện khi in thử — xem bảng chi tiết trong `3d_model/custom_exo/fixation_mechanisms_benchmark/README.md`. | Đã chốt (loại bỏ 8 phương án) |
| Trước 2026-10-12 | Chọn phương án thứ 9 (hai ngàm khớp nối + một quai kẹp xoay đóng/mở, không cần bẻ cong nhựa) làm thiết kế triển vọng nhất hiện tại, thay cho phương án thứ 8 (phải bẻ cong nhựa mỗi lần mở, dễ hỏng theo thời gian). | Giải quyết vấn đề mỏi vật liệu của phương án cũ. | **Đang chờ hoàn thiện** — thiết kế mới hiện mới có bản vẽ máy tính, **chưa in thử thực tế**, chưa có số liệu kiểm tra độ bền, và file bản vẽ chưa được đưa vào kho lưu trữ chính thức của dự án (hiện chỉ có trên máy tính cá nhân) |

---

## Những điểm còn đang chờ quyết định (chưa phải thay đổi chính thức)

Các điểm dưới đây **chưa** được chốt dứt khoát — nhóm và/hoặc GVHD cần xem và quyết định, agent hỗ
trợ không tự ý chọn thay:

1. Bộ tiêu chí đo mới (M1–M6, C1.1–C1.10) và phạm vi 3 ngón tay (đề xuất ngày 27/09) có chính thức
   thay thế bộ tiêu chí cũ và phạm vi 5 ngón hay không.
2. Bản đề cương kỹ thuật mới nhất (soạn 03/10/2026, có thêm phần "hỗ trợ vận động theo nhu cầu")
   có phải là bản sẽ dùng để **nộp lại** chính thức cho trường/hội thi, hay chỉ là bản nháp lưu
   hành nội bộ song song với bản đã nộp ngày 26/09.
3. Số liệu đo thử nghiệm thật ngày 09–11/10 cần được hoàn thiện đầy đủ hồ sơ đi kèm (phiếu ghi
   buổi đo, điều kiện đo, đối chiếu tham chiếu) trước khi được coi là bằng chứng chính thức trong
   báo cáo.
4. Việc đổi tên cảm biến đo nhiệt độ-độ ẩm giữa 2 bản đề cương (một loại cảm biến ở bản 26/09,
   loại khác ở bản 03/10) là thay đổi có chủ đích hay chỉ là lỗi đánh máy — cần nhóm xác nhận lại.
5. Việc khai báo sử dụng công nghệ số/trí tuệ nhân tạo theo quy chế cuộc thi — nhóm tự thực hiện
   riêng, không nằm trong phạm vi tài liệu này.
6. Thiết kế cơ cấu đóng/mở nẹp ngón tay phương án thứ 9 (Giai đoạn 6 ở trên) cần được: xuất file
   bản vẽ vào kho lưu trữ chính thức, in thử thực tế, kiểm tra độ bền qua nhiều lần đóng/mở, và xác
   nhận có thay thế/kết hợp với cơ cấu bản lề nối giữa các đốt ngón đã chốt trước đó hay không.

---

## Xác nhận của GVHD

Tôi, **Lê Công Long**, đã xem và nắm được các thay đổi chính thức nêu trên của đề tài.

Chữ ký GVHD: ______________________          Ngày: ___/___/2026
