# research/bench/logs — nơi chứa log GATE

**Quy tắc (bất biến):**
1. Một file **một phiên đo**. Tên: `YYYY-MM-DD_G<n>_<mã-mẫu>_<loại>.csv` (schema của GATE 0: `research/protocols/08_gate0_execution_plan.md` §9).
2. File gốc **không bao giờ bị sửa**. Mọi bản đã làm sạch/tính toán lại đặt tên `…_derived.csv`.
3. Đầu file có comment `#` chép lại: **ngưỡng đã chốt trước khi đo** (ảnh chụp trang §7), số serial DMM, dãy thứ tự tải ngẫu nhiên viết tay.
4. Không có file nào ở đây được coi là "kết quả của đề tài" cho tới khi có `research/reviews/…-results.md` đối chiếu ngưỡng.
5. Tính đến **2026-09-19, thư mục này rỗng** — đề tài chưa có bất kỳ phép đo nào. Không được tạo file giả/benchmark giả ở đây.
