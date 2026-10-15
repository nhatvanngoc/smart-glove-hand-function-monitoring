# Bộ Thử Nghiệm So Sánh Cơ Cấu Đóng/Mở & Giữ Chặt Nẹp Ngón Tay (Fixation Mechanism Benchmark)

> **Ngày ghi nhận vào repo:** 2026-10-12 (nhóm nghiên cứu báo cáo qua chat quá trình đã thực hiện trên máy
> cá nhân; ngày thực hiện thật của từng lần in thử **chưa được xác nhận chính xác** — xem mục 5).
> **Quyết định liên quan:** `DEC-MECH-005` (loại Mech 1–8), `DEC-MECH-006` (ghi nhận Mech 9, **chưa
> chốt chính thức**) trong `research/context/DECISION_LOG.md`.
> **Trạng thái:** Mech 1–8 có đầy đủ file CAD trong thư mục này (đã in thử thực tế theo lời chủ dự
> án). **Mech 9 (thiết kế hiện tại tốt nhất) CHƯA có file CAD trong repo** — xem mục 5–6.
> **Công cụ thiết kế:** Tinkercad / OpenSCAD (qua CGAL boolean) cho vòng lặp Mech 8; FreeCAD cho các
> mech trước đó (suy từ định dạng `.step` xuất kèm).

---

## 1. Đặt vấn đề: bài toán khác với `full_finger_modular/`

Tài liệu `docs/06_Co_Cau_Co_Khi_Exoskeleton.md` đã mô tả cơ cấu **bản lề giữa các đốt ngón tay**
(khớp PIP/DIP, rãnh trượt tự lựa bù chiều dài, khớp bấm ngàm bên hông) cho bộ khung
`3d_model/custom_exo/full_finger_modular/`. Bộ thử nghiệm trong thư mục này giải quyết một **bài
toán khác, độc lập**: với mỗi đốt ngón, **cơ cấu nào dùng để đóng/mở vỏ nẹp quanh ngón tay** sao
cho bệnh nhân (có thể bị yếu/run tay sau đột quỵ) tự đeo vào và tháo ra được bằng một tay, đồng
thời giữ đủ chặt để cảm biến áp lực Velostat có tiếp xúc ổn định?

Đây vẫn là một **câu hỏi mở chưa chốt** — xem mục 7 "Việc cần làm tiếp" để biết quan hệ giữa hai
bộ thiết kế này cần được nhóm nghiên cứu xác nhận thêm.

Nhóm nghiên cứu đã tự thiết kế, xuất file CAD và **in thử thực tế trên máy in 3D** lần lượt 9 phương án
cơ cấu khác nhau (gọi tắt Mech 1 → Mech 9), ghi nhận ưu/nhược điểm thực tế của từng phương án rồi
loại dần cho tới khi còn lại phương án hiện tại (Mech 9).

---

## 2. Bảng tổng hợp tiến hóa các cơ cấu (Mech 1 → Mech 9)

| Cơ cấu | Tên cơ chế | Nguyên lý hoạt động | Ưu điểm | Nhược điểm thực tế & lý do phải thay đổi | File CAD trong thư mục này |
|---|---|---|---|---|---|
| **Mech 1** | C-Clip Spring Cuff | Vòng kẹp hở miệng chữ C đàn hồi, ấn ngón tay vào qua khe hở | In 1 chi tiết cực nhanh, nhẹ | Lực kẹp yếu; sau vài lần tháo đeo nhựa FDM bị giãn; khi dây gân kéo tải > 15 N vòng bị banh miệng tuột khỏi ngón tay; ấn ngón qua khe hẹp gây đau | `mech1_c_clip_spring_cuff.step/.stl` |
| **Mech 2** | Dovetail Slide Lock | Hai nửa vỏ ghép lại, khóa bằng rãnh trượt mộng đuôi én tịnh tiến dọc trục ngón | Rất cứng vững theo phương hướng kính | Khó đeo/tháo: phải trượt dọc 15 mm trên ngón tay (bệnh nhân co cứng ngón rất khó làm); ma sát giữa các lớp in FDM dễ gây kẹt cứng rãnh trượt | `mech2_dovetail_slide_lock.step/.stl` (+ bản `_closed`) |
| **Mech 3** | Velcro Strap Slots | Vỏ mu cứng + dây đai dán Velcro xỏ qua 2 khe luồn để siết lòng ngón | Ôm vừa nhiều cỡ ngón, đệm êm | Dây dán nhanh bai dão, bám bẩn, khó sát khuẩn y tế; không cố định cứng vững cảm biến áp trở Velostat ở lòng bàn tay | `mech3_velcro_strap_slots.step/.stl` |
| **Mech 4** | Cross-Pin Latch | Một bản lề bên sườn trái, sườn phải khóa bằng một chốt pin xỏ dọc từ trên xuống | Khóa tuyệt đối chắc chắn, không thể bung | Chốt pin là chi tiết rời nhỏ, người bệnh run tay/yếu cơ rất dễ làm rơi mất; thao tác xỏ chốt bằng một tay gần như bất khả thi | `mech4_cross_pin_latch.step/.stl` |
| **Mech 5** | Top Buckle Snap | Lẫy móc bấm dạng khóa cài đặt ở đỉnh mu ngón tay | Đóng mở tương đối nhanh | Chiếm dụng không gian đỉnh mu ngón, xung đột vị trí với đường đi của dây cáp kéo gân và tai chạc liên kết giữa các đốt ngón tay | `mech5_top_buckle_snap.step/.stl` |
| **Mech 6** | Ratchet Cable Clamp | Dải đai có răng cưa uốn cong từ lòng ngón luồn qua khe có lẫy cóc giữ | Siết được nhiều nấc to/nhỏ | Dải đai bị uốn gập mỏi liên tục, rất dễ nứt gãy dọc theo đường lớp in 3D FDM; khi cần tháo phải dùng móng tay bẩy lẫy rất đau tay | `mech6_ratchet_cable_clamp.step/.stl` |
| **Mech 7** | Double Hinge Toggle V1/V2 | Bản lề kép với thanh đòn kẹp trung gian | Lực kẹp khỏe, không uốn nhựa | Kết cấu nhiều khớp động nhỏ sát nhau, dễ bị dính lớp khi in máy FDM phổ thông; kích thước cồng kềnh | `mech7_double_hinge_toggle_clasp.step/.stl` + các biến thể `mech7_*` (dorsal shell, heavy-duty jaw, pip closed pose, toggle lever...) |
| **Mech 8** | 1-Hinge Ratchet Snap-Fit | Một bản lề trục in liền bên sườn A + mấu răng đực bấm gập vào lỗ cái bên sườn B | Gọn gàng, thẩm mỹ, in Print-in-Place tiện lợi | Đóng thì bấm chặt, nhưng **mỗi lần mở ra phải dùng lực bẻ cong mép nhựa** → mỏi vật liệu (fatigue), giảm tuổi thọ nhựa in FDM, dễ gãy lẫy sau thời gian ngắn sử dụng | `mech8_1hinge_ratchet_latch*.step/.stl`, `mech8_pin_hinge*`, `mech8_dorsal_shell_only`, `mech8_palmar_shell_only`, `mech8_scad_*` (nhiều vòng lặp, xem mục 3) |
| **Mech 9** *(hiện tại, triển vọng nhất)* | Double-Hinge Toggle Clasp | Bản lề kép + 2 ngàm đực nhô cao + quai gông kẹp chữ U có cần gạt mở | Đóng/mở hoàn toàn bằng khớp xoay, không bẻ cong nhựa (kỳ vọng bền hơn Mech 8); ôm ngàm chặt; mở bằng một ngón tay theo mô tả; in Print-in-Place một file duy nhất | *(Đã xử lý 2 lỗi dựng CAD — xem mục 4. **Chưa có số liệu kiểm tra độ bền theo chu kỳ đóng/mở thực tế**, chưa in thử thực tế theo xác nhận tại thời điểm ghi nhận này)* | **CHƯA có trong repo** — xem mục 5 |

**Lưu ý đọc bảng:** cột "Ưu điểm" là mô tả định tính theo kỳ vọng thiết kế ban đầu, không
phải số liệu đo được (vd. không có số chu kỳ đóng/mở trước khi nhựa gãy, không có lực kế đo lực
kẹp thật). Theo nguyên tắc liêm chính khoa học của dự án, các mô tả này **chưa được
nâng lên mức "đã kiểm chứng"** cho tới khi có phép đo thực tế đi kèm.

---

## 3. Diễn biến chi tiết quá trình tinh chỉnh Mech 8 (khóa bấm ngàm đực/lỗ cái)

Nhóm nghiên cứu đã trực tiếp in ra thực tế trên máy in 3D nhiều lần và phát hiện từng điểm bất hợp lý
của cơ cấu bấm snap-fit. Các trích dẫn dưới đây là **nguyên văn lời nhóm nghiên cứu**, giữ lại để truy
vết quá trình ra quyết định thiết kế:

1. **Lần in 1 — răng quá nhỏ, trượt:**
   > "Rồi đã in ra, tuy nhiên mấu răng đực nó vẫn dài hơn lỗ cái, hơn nữa nó quá nhỏ, quá dễ trượt
   > không bám chắc được."
   **Cải tiến:** tăng độ dày mấu răng, vát góc hãm 45°, mở rộng khoang ngàm cái.
2. **Lần in 2 — vẫn dễ tuột khi giật mạnh:**
   > "Cũng ổn, tuy nhiên, vẫn quá dễ rớt, tôi muốn tăng độ cao của mấu răng đực, vì bản hiện tại
   > tôi giật mạnh ra là nó tự ra."
   **Cải tiến:** tăng chiều cao nhô của mấu răng đực thêm +0,6 mm để cắn sâu vào lỗ cái.
3. **Lần in 3 — hở viền, lỏng khớp:**
   > "Tôi nghĩ nên thu gọn nhỏ cái lỗ cái vào cho khớp mấu răng đực, hiện tại nó đang bị lỏng, hơn
   > nữa phần tiếp xúc, tức là phần viền của bên cái tiếp xúc vào bên đực ấy nó to hơn và không ôm
   > khít vào bên đực."
   **Cải tiến:** thu nhỏ lỗ cái, bo cong vách viền bên cái để ôm sát khít biên dạng bên đực.
4. **Lần in 4 — lỗ cái quá chật:**
   > "Lần này cái lỗ cái nhỏ quá."
   **Cải tiến:** tinh chỉnh dung sai bù co ngót nhựa FDM về chuẩn 0,35 mm.
5. **Lần in 5 — bước ngoặt đổi cơ cấu:**
   > "Được đó bây giờ đóng rất chặt gài chỉ cần bấm lại là xong, tuy nhiên mở cũng khó phải nén, bẻ
   > cong nhựa làm giảm tuổi thọ."
   **Phân tích kỹ thuật:** loại khóa bấm snap-fit dù chỉnh chặt đến đâu thì về bản chất vật lý vẫn
   bắt buộc **phải bẻ uốn mép nhựa để mở**. Nhựa in FDM (PLA/PETG) có điểm yếu ở liên kết giữa các
   lớp in; sau vài chục lần bẻ cong, lẫy sẽ bị giãn hoặc nứt gãy dọc theo thớ in. Đây là lý do
   trực tiếp dẫn tới việc đổi hẳn sang nguyên lý cơ cấu mới ở Mech 9 (đóng/mở bằng khớp xoay thay
   vì bẻ cong nhựa).

**Ghi chú minh chứng:** 5 lần in thử trên là mô tả bằng lời của nhóm nghiên cứu qua chat, **chưa có ảnh
chụp/video đính kèm trong repo** cho từng lần in. Nếu còn giữ ảnh các bản in thất bại, nên tải lên
để làm minh chứng trực quan (tương tự cách đã làm với ảnh oscilloscope/Serial Plotter trong
`research/notebook/`).

---

## 4. Khởi tạo và xử lý lỗi khi dựng Mech 9 (bản lề kép)

### 4.1. Ý tưởng do chính nhóm nghiên cứu đề xuất

> "Tại sao ở 2 gàm không làm 2 phần đực nhô ra, và một bên sẽ có bản lề thứ 2 kèm 1 khung cố định.
> Khi khép 2 gàm này lại sát nhau, gạt khung cố định xuống để 2 gàm dính chặt vào nhau. Bạn thấy
> thế nào, nếu được thì tốt nhất 2 gàm cao một chút."

Nguyên lý này nhằm giải quyết vấn đề mỏi vật liệu của Mech 8:
- Hai ngàm đực khép khít vào nhau thành một khối dày dặn (6,4 mm, nhô cao 4,1 mm).
- Bản lề thứ 2 gắn quai gông kẹp chữ U. Khi đóng, quai kẹp xoay xuống ngậm trọn cả 2 ngàm đực.
- Khi mở, chỉ cần gạt nhẹ cần mở để quai xoay lên trên → về nguyên tắc **không làm biến dạng, bẻ
  cong hay mỏi nhựa** (kỳ vọng thiết kế, chưa kiểm chứng bằng số liệu thực tế — xem mục 2).

### 4.2. Hai lỗi kỹ thuật gặp phải khi dựng mô hình CAD & cách đã xử lý

**Lỗi 1 — khối ngũ giác trôi nổi đơn độc, thân quai kẹp biến mất:**
- *Hiện tượng:* trên bàn in xuất hiện một trụ ngũ giác đứng lẻ loi một mình, còn thân quai kẹp thì
  biến mất khỏi mô hình.
- *Nguyên nhân:* đa giác 2D của quai kẹp có các đoạn thẳng tự giao cắt (self-intersecting
  segments). Khi công cụ dựng hình xử lý phép toán hợp/trừ khối (boolean CGAL), thuật toán đã loại
  bỏ phần thân bị lỗi và chỉ giữ lại phần mũi cần gạt mở ngón tay trôi nổi trên bàn in. Đồng thời,
  lệnh khoét hình trụ tại bản lề thứ 2 vô tình cắt xuyên qua cốt chốt xoay.
- *Khắc phục:* tái cấu trúc biên dạng quai kẹp thành một đa giác chuẩn toán học (ngược chiều kim
  đồng hồ, diện tích 20 mm², tuyệt đối không tự giao cắt). Thân quai kẹp, chốt bản lề ⌀2,6 mm và 2
  tay đòn xoay (tại 2 đoạn dọc trục khớp) được hợp nhất thành một khối đặc duy nhất.

**Lỗi 2 — bản lề chính bị rỗng ruột, nhấc lên là tách rời:**
- *Hiện tượng:* in ra thực tế, "cái bản lề chính bị lỗ, mất đi đâu rồi ấy, in ra là nhấc lên một
  cái là tách ra luôn chứ không có trục cố định."
- *Nguyên nhân:* trong phần vỏ mu ngón, lệnh khoét rãnh xoay cho ống bọc vỏ lòng nằm trong khối
  phép trừ (difference) đã cắt gọt luôn cả đoạn giữa của chốt xoay bản lề 1. Đoạn giữa bị rỗng ruột
  hoàn toàn (kiểm tra mặt cắt ngang qua giữa trục bằng 0 vật liệu), làm ống bọc vỏ lòng không có
  trục giữ và rơi tuột ra.
- *Khắc phục:* chuyển lệnh đúc chốt xoay ⌀2,6 mm ra ngoài khối phép trừ, hợp nhất vào giai đoạn
  cuối của quá trình dựng hình. Kết quả kiểm tra lại: mặt cắt ngang qua trục đã có vật liệu đặc
  liên tục trên toàn bộ chiều dài, chốt xoay đúc liền xuyên suốt.

---

## 5. Tình trạng minh chứng & giới hạn cần lưu ý (đọc trước khi dùng vào báo cáo)

1. **Mech 1–8:** file CAD (`.step`/`.stl`) đã có sẵn trong thư mục này, đã được in thử thực tế trên
   máy in 3D theo lời nhóm nghiên cứu. Lý do loại từng phương án ở mục 2 là quan sát thực tế trên vật in
   — đây là mức bằng chứng cao (quan sát trực tiếp), nhưng **chưa có ảnh/video/ghi chú ngày tháng
   đính kèm trong repo** cho từng lần in, nên ngày thực hiện chính xác của mỗi mech hiện **chưa xác
   định được** (ghi tạm là "trước 2026-10-12" — ngày nhóm nghiên cứu báo cáo qua chat).
2. **Mech 9 — CHƯA có file CAD trong repo này.** Toàn bộ nội dung mục 4 (ý tưởng, 2 lỗi kỹ thuật và
   cách xử lý) được ghi nhận trong quá trình thử nghiệm thiết kế. Nhóm nghiên cứu
   đang hoàn thiện tệp CAD Mech 9 trước khi đưa vào kho lưu trữ.
3. Mech 9 **chưa được xác nhận đã in thử thực tế** tại thời điểm ghi nhận tài liệu này (chỉ mới
   dựng xong mô hình CAD và xử lý xong 2 lỗi kỹ thuật kể trên).
4. Các cụm từ như "tuổi thọ vĩnh cửu", "đóng mở 100% bằng khớp xoay" là **mô tả định tính kỳ vọng
   thiết kế** ban đầu, không phải kết luận đã qua kiểm tra độ bền (ví dụ: số chu kỳ đóng/mở
   trước khi nhựa hỏng). Theo nguyên tắc liêm chính khoa học, **không đưa các nhận định định tính này vào báo cáo chính thức như một kết quả đã đo được** cho tới khi có phép thử
   độ bền chu kỳ thực tế.
5. Quan hệ giữa bộ thử nghiệm này và cơ cấu "Khớp Bấm Ngàm Bên Hông" đã mô tả trong
   `docs/06_Co_Cau_Co_Khi_Exoskeleton.md` §2.5 (dùng cho bản lề *giữa các đốt ngón*, không phải
   đóng/mở quanh một đốt) cần được nhóm đối chiếu rõ trong giai đoạn tích hợp.

---

## 6. Bản đồ file hiện có trong thư mục này

- `benchmark_plate_all_7_arranged.stl` — tấm in gộp sắp xếp sẵn nhiều mech (tới Mech 7) để in thử
  hàng loạt trên cùng một bàn in.
- `mech1_c_clip_spring_cuff.*` … `mech6_ratchet_cable_clamp.*` — mỗi mech 1 cặp `.step`/`.stl`.
- `mech7_*` — nhiều biến thể của Double Hinge Toggle (dorsal shell riêng, palmar strap riêng, heavy
  duty jaw, toggle lever, phiên bản v2 đã hoàn thiện hơn — `mech7_v2_toggle_closed_perfected`).
- `mech8_*` — nhiều vòng lặp của 1-Hinge Ratchet Snap-Fit (pin hinge vs living hinge, bản mở sẵn
  sàng in "print_ready", bản vỏ mu/lòng tách riêng, bản xuất từ OpenSCAD `mech8_scad_*`) — tương
  ứng với 5 lần in thử mô tả ở mục 3.
- **Mech 9: chưa có file nào trong thư mục này** (xem mục 5–7).

---

## 7. Kế hoạch hoàn thiện tiếp theo của nhóm nghiên cứu

1. Xuất file CAD Mech 9 (`.step`/`.stl`) từ máy tính cá nhân của nhóm nghiên cứu và thêm vào thư mục
   `3d_model/custom_exo/fixation_mechanisms_benchmark/` để repo có đầy đủ bằng chứng thiết kế.
2. In thử Mech 9 thực tế trên máy in 3D, kiểm tra độ bền qua nhiều chu kỳ đóng/mở (ví dụ đóng/mở
   N lần liên tục rồi quan sát dấu hiệu mỏi/nứt vật liệu), ghi lại bằng ảnh/video.
3. Nếu còn giữ ảnh chụp 5 lần in thử Mech 8 (mục 3) và các lần in Mech 1–7, tải lên làm minh chứng
   trực quan.
4. **Xác nhận quan hệ giữa bộ thử nghiệm này với `full_finger_modular/`:** Mech 9 có phải là cơ cấu
   sẽ dùng để thay thế/bổ sung cho cách đóng/mở từng đốt vỏ trong thiết kế đã hoàn thiện ở
   `docs/06` hay không? Nếu có, cần cập nhật `docs/04_Hardware_Architecture.md` và
   `docs/06_Co_Cau_Co_Khi_Exoskeleton.md` để phản ánh; nếu đây vẫn là nhánh thăm dò song song chưa
   tích hợp, cần ghi rõ trạng thái "thăm dò, chưa tích hợp" ở cả hai nơi để tránh hiểu nhầm khi
   viết báo cáo.
5. Xác nhận lại ngày thực hiện thật của từng lần in thử (hiện chỉ ghi "trước 2026-10-12").
