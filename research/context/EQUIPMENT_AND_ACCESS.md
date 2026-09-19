# Kiểm kê thiết bị & quyền truy cập (2026-09-19)

> **Nguồn:** lời khai của chủ dự án trong đối thoại 2026-09-19. Agent **không kiểm kê vật lý** được — ô "xác nhận" dưới đây để chủ dự án tự điền.
> File này **chỉ dùng để lập kế hoạch**, không phải bằng chứng trong báo cáo (mọi con số chi phí phải đến từ hoá đơn/báo giá thật — Phụ lục A `docs/05`).

## 1. Thiết bị

| Món | Trạng thái | Cần cho | Xác nhận của owner (số lượng / tình trạng) |
|---|---|---|---|
| Velostat (film áp trở) | **Đã có** | GATE 0 → C: mọi sensing element | *[điền: mấy tấm, kích thước, lô]* |
| Băng đồng (copper tape) | **Đã có** | điện cực của sensing element | *[điền: độ dài]* |
| ESP32-S3 | **Đã có** | GATE 0 §3 (đo `R_max`, ENOB, `fps_meas`) + bring-up 12 kênh | *[điền: loại board — còn chân ADC1 tự do?]* |
| Orange Pi 5 Pro (RK3588) | **Đã có** | GATE F (INT8/RKNN) — **đừng dùng trước GATE A/B** | *[điền: RAM / đã có nguồn + thẻ nhớ?]* |
| CD74HC4067 (MUX 16:1) | ❓ chưa nêu | GATE 0 §3 trở lên — **món duy nhất ở Lớp 1 có thể còn thiếu** | *[điền]* |
| DMM đo được 4 dây / điện trở thấp | ❓ | GATE 0: `R` là đại lượng gốc | *[điền]* |
| Quả cân chuẩn (hoặc chai nước đã cân) | ❓ | **lực chuẩn cho GATE 0** — thay được load cell ở giai đoạn tĩnh | *[điền]* |
| Máy in 3D + PLA/PETG + TPU | ❓ | jig GATE 0, khung vách, phantom | *[điền: trường có phòng sáng tạo không — `A.5` ghi là có]* |
| Load cell + HX711 | ❓ (mua sau) | GATE A/B/C: lực động khi ngón đang chuyển | *chưa cần cho GATE 0* |
| Khung đỡ + vít M5 + êcu hãm + lò xo | ❓ | preload cơ khí (biến số `F_p`) | *[điền]* |

**Ghi chú kỹ thuật quan trọng cho GATE 0:** lực chuẩn **không** cần load cell. Với mỗi khối lượng `m` đã cân, `F = m·g` là chuẩn cơ bản hơn lực kế lò xo
(không trễ, không cần hiệu chuẩn điện tử). Load cell + HX711 chỉ cần từ GATE A trở đi, lúc đã có chuyển động.

## 2. Quyền truy cập chuyên môn

**Có:** chị ruột của chủ dự án là **kỹ thuật viên Vật lý trị liệu – Phục hồi chức năng, 10 năm kinh nghiệm**; đã xác nhận tính cấp thiết của đề tài
(`SRC-OWNER-2026-09-19-KTV10Y`, cùng chuỗi với `DEC-CLINICAL-001`).

| Được dùng cho ✅ | Không được dùng cho ⛔ |
|---|---|
| Trả lời phiếu 10 câu `research/protocols/07` §5 (tần suất hẹn, số người bệnh/phòng, kỳ vọng về chỉ số) | **Làm đối tượng đo** — kể cả "chỉ 1 ngón, đo nhẹ, trong 5 phút" |
| Chốt **giao thức bài tập chuẩn**: thứ tự động tác, số lần lặp, thời gian nghỉ, cách đọc AROM/PROM | **Tuyển người bệnh** hoặc giới thiệu bệnh nhân để lấy dữ liệu |
| Phản biện bảng tải của rig E4/RAL và tính hợp lý của các nấc `RAL_min` | **Chứng nhận hiệu quả lâm sàng** — "KTV thấy hữu ích" là bằng chứng *nhu cầu* (Tầng 3), không phải bằng chứng *kết quả* |
| Đọc bản diễn giải chỉ số (EI/GAP/RAL) và chỉ ra chỗ **vô nghĩa về mặt lâm sàng** | Ký thay phê duyệt đạo đức; phê duyệt của một cá nhân **không** thay được IRB/SRC (`DEC-ETHICS-001` OPEN) |
| Góp ý câu chữ cho mục "đối tượng & phạm vi" và phần giới hạn | Xuất hiện trong đề tài như "đồng tác giả" nếu chỉ tham gia tư vấn (`DEC-ROLE-001`) |

**Cách dùng đúng mà vẫn hợp lệ:** mời phản biện **trên giấy** (gửi phiếu + 1 trang quy trình), lưu câu trả lời thành `research/reviews/2026-…-ktv-round3.md`.
Như vậy hồ sơ có một dòng mạnh mà vẫn trung thực: "**giao thức đo đã được một chuyên gia vật lý trị liệu – phục hồi chức năng phản biện**" — theo `DEC-ROLE-001` **không** kèm tên, không kèm số năm kinh nghiệm, không kèm quan hệ gia đình; và không có dòng nào phải giải trình trước hội đồng đạo đức.

## 3. Việc còn thiếu để GATE 0 chạy được **tuần này**
1. ☐ Chốt **9 ngưỡng** `research/protocols/08_gate0_execution_plan.md` §7 (việc duy nhất chặn đường).
2. ☐ Điền §1 ở trên (số lượng/tình trạng) → xác nhận CD74HC4067 + DMM + khối lượng chuẩn.
3. ☐ In/cắt jig cho 5 phần tử họ A + 1 cụm họ B (mẫu C đối chứng làm sau cũng được).
4. ☐ Chụp ảnh trang §7 đã chốt và dán vào header của file log đầu tiên (`research/bench/logs/`).
