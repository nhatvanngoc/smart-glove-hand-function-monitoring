# Bảng tổng hợp thay đổi chính thức — PHẦN BỔ SUNG Giai đoạn 7 (17–19/10/2026)

**Đề tài:** Nghiên cứu và phát triển găng tay hỗ trợ phục hồi chức năng sau đột quỵ cho vận động tinh *(tên làm việc, chưa chốt tên nộp cuối)*.
**Nhóm thực hiện:** Văn Ngọc Nhật Anh (11A2) + Nguyễn Duy Quân (12A1) — **GVHD:** Lê Công Long, THPT thị xã Quảng Trị.
**Ngày lập phần bổ sung:** 2026-10-19.

**Cách dùng tệp này:** đây là phần **bổ sung** cho `2026-10-12_BANG_TONG_HOP_THAY_DOI_CHINH_THUC.md` (bảng tóm lược các thay đổi
đã chốt, dành cho GVHD đọc nhanh). Phần dưới đây đã được ghép vào bản trong kho tài liệu dự án; tệp này tồn tại riêng để
thầy/cô và nhóm đọc được ngay trên hệ thống tài liệu mà không phải mở lại toàn bộ bảng cũ. Quy ước đọc giữ nguyên:
**Đã chốt** = nhóm/chủ dự án đã quyết định dứt khoát; **Đang chờ duyệt** = mới là đề xuất.

---

## Giai đoạn 7 (17/10 – 19/10/2026): Đổi hướng chức năng sang găng hỗ trợ tập vận động tinh + tự động chuyển chế độ

| Ngày | Thay đổi | Lý do | Trạng thái |
|---|---|---|---|
| 2026-10-17 → 19/10 | Tiếp nhận bản đề cương mới nhất do chủ dự án cung cấp (bản 12 trang trên hệ thống tài liệu dự án). Chỉ **đọc để đối chiếu**, không chỉnh sửa, không thay thế. | Bản này là nguồn mới nhất do chủ dự án chỉ định; các bản đã nộp trước đó giữ nguyên làm hồ sơ lịch sử. | Đã ghi nhận |
| 2026-10-19 | **Đổi hướng chức năng của đề tài** thành lộ trình 3 bước: (1) máy hỗ trợ gập–duỗi ngón khi người tập chưa tự làm được; (2) **tự động** chuyển sang chế độ hỗ trợ theo nhu cầu (AAN) khi tín hiệu vận động đạt tiêu chí đã định trước; (3) luyện phối hợp ba ngón cái–trỏ–giữa để **gắp thìa, nhấc, di chuyển tới vùng đích và đặt**. Thêm camera theo dõi thìa/vùng đích/kết quả và báo phản hồi trực quan ngay cho người tập. **Không cần kỹ thuật viên bấm nút chuyển chế độ.** | Chủ dự án xác định đây là chức năng muốn phát triển: từ vận động ngón cơ bản tiến tới một thao tác vận động tinh có mục đích, thay vì chỉ ghi số liệu cảm biến. | **Đã chốt về hướng**; toàn bộ chi tiết kỹ thuật (tiêu chí chuyển chế độ, thông số bài tập, cơ cấu, camera) **còn mở** |
| 2026-10-19 | Cơ cấu trợ lực: dùng **mô-tơ servo cuốn dây câu cá trực tiếp lên tang cuốn**; **bỏ** phương án lò xo trợ lực và khớp bốn khâu. | Chủ dự án xác nhận lại lựa chọn cơ cấu, tránh mô tả sai trong hồ sơ. | Đã chốt về hướng; **cơ cấu nhả/hồi dây để duỗi ngón và phương án một tang hay ba tang cho ba ngón CÒN MỞ** |
| 2026-10-19 | **Bỏ** công thức tính lực trợ giúp theo Newton và **bỏ** ngưỡng 5 N (đã rút trước đó). Cảm biến áp lực Velostat chỉ dùng làm **tín hiệu tương đối** về áp lực/tiếp xúc, không quy đổi thành lực, không dùng làm chuẩn an toàn. | Vật liệu Velostat có sai số lớn theo y văn đã ghi nhận; mọi phát biểu về lực phải dựa trên thiết bị đo độc lập. | Đã chốt |
| 2026-10-19 | Phạm vi thử nghiệm: **bàn thử và mô hình tay giả trước**. Chỉ **xem xét** thử có cấp nguồn trên người trưởng thành khỏe mạnh **sau khi** đánh giá an toàn đạt và có đầy đủ phê duyệt của nơi có thẩm quyền. **Không** thử trên bệnh nhân, **không** khẳng định hiệu quả phục hồi lâm sàng, **không** khẳng định thiết bị đã an toàn hoặc đã dùng được tại nhà. | Giữ ranh giới an toàn và đạo đức; kết quả trên mô hình giả không phải kết quả trên người. | Đã chốt |
| 2026-10-19 | Số cảm biến gập (Flex sensor): **3 chiếc, mỗi ngón cái/trỏ/giữa một chiếc**. Nếu cả ba đọc qua một bộ chuyển mạch 16 kênh thì dành 3 kênh, **còn tối đa 13 kênh** cho cảm biến áp lực và ô tham chiếu. | Chủ dự án làm rõ số lượng cảm biến. | Đã chốt số lượng; **vị trí lắp, số miếng Velostat, bản đồ kênh cuối cùng còn mở** |
| 2026-10-19 | Khối lượng và chi phí: mục tiêu **80–120 g chỉ tính cụm đeo trên tay** (chưa cân); dự toán vật tư cụm đeo **1,0–1,3 triệu đồng**, toàn bộ hệ thống/giàn thử **khoảng 5,5 triệu đồng** khi tận dụng thiết bị phòng thí nghiệm. **Bỏ** hai tiêu chí cũ "<1,5 triệu đồng cho toàn hệ thống" và "<150 g". | Tách phần đeo trên tay khỏi phần máy xử lý/nguồn/mô-tơ đặt ngoài cho đúng thực tế. | Đã chốt là **mục tiêu/dự toán** — chưa cân, chưa kiểm toán, cần báo giá có ngày |
| 2026-10-19 | **Học tăng cường (RL) không thuộc phạm vi** đề tài. Orange Pi 5 Pro là nền tảng **dự kiến** cho xử lý hình ảnh; chưa đo tốc độ, độ trễ hay độ chính xác. | Tránh mô tả năng lực chưa có. | Đã chốt về phạm vi |
| 2026-10-19 | **Lượt làm việc tài liệu (chưa viết code):** soạn bộ hồ sơ "chốt bài tập + chốt cách nối cảm biến" (Gate 0), đặc tả nhánh camera, lộ trình viết phần mềm theo 7 bước; bổ sung vào đề cương A/B/C bảng "đăng ký trước" 14 chỉ số đo; cập nhật sổ quyết định và sổ luận điểm. | Chủ dự án chỉ đạo **hoàn thiện đề cương trước rồi mới bắt đầu code**. | **Đang chờ duyệt** — mọi con số/ngưỡng trong các hồ sơ này để trống có chủ đích |

---

## Những điểm còn đang chờ quyết định — bổ sung ngày 19/10/2026

7. **(19/10/2026)** Duyệt 7 mã đề xuất trong nhật ký quyết định: tờ yêu cầu bài tập thìa và bảng trạng thái; cách phân biệt
   vận động do người tập tự làm với chuyển động do máy kéo; phương án bố trí 16 kênh cảm biến; tốc độ quét mục tiêu (phải đo
   rồi mới chốt); kiến trúc nhánh camera; lộ trình viết phần mềm; nơi đặt bộ điều khiển chuyển chế độ.
8. **(19/10/2026)** Kiểm tra trên mạch thật 8 điểm kỹ thuật đã liệt kê, trong đó có: giới hạn điện áp đầu vào của bộ chuyển đổi
   ADS1115 so với ghi nhận cũ "đọc toàn dải 0–3,3 V"; bộ chuyển đổi trên board có còn 3 ngõ vào trống để đọc thẳng 3 cảm biến
   gập hay không; nhiễu khi mô-tơ servo chạy; quy tắc nối mass để tránh đoản mạch vòng mass như đã gặp.
9. **(19/10/2026)** Chốt cơ cấu **nhả/hồi dây để duỗi ngón** và phương án một tang kéo cả ba ngón hay ba tang riêng; thu xếp
   **thiết bị đo lực/căng dây độc lập** trước khi thử cơ cấu (không dùng Velostat làm chuẩn lực).
10. **(19/10/2026)** Điền các thông số bài tập thìa bằng cách đo vật thật (loại thìa, kích thước, khối lượng, vị trí vùng xuất
    phát và vùng đích, độ cao tính là "nhấc", thời gian giữ tính là "đặt thành công", số lần thử và thời gian nghỉ mỗi buổi).
    Không điền theo ước đoán.

---

## Xác nhận của GVHD (cho phần bổ sung này)

Tôi, **Lê Công Long**, đã xem và nắm được các thay đổi nêu trên của đề tài.

Chữ ký GVHD: ______________________          Ngày: ___/___/2026
