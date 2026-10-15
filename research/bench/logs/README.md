# research/bench/logs — nơi chứa log GATE

**Quy tắc (bất biến):**
1. Một file **một phiên đo**. Tên: `YYYY-MM-DD_G<n>_<mã-mẫu>_<loại>.csv` (schema của GATE 0: `research/protocols/08_gate0_execution_plan.md` §9).
2. File gốc **không bao giờ bị sửa**. Mọi bản đã làm sạch/tính toán lại đặt tên `…_derived.csv`.
3. Đầu file có comment `#` chép lại: **ngưỡng đã chốt trước khi đo** (ảnh chụp trang §7), số serial DMM, dãy thứ tự tải ngẫu nhiên viết tay.
4. Không có file nào ở đây được coi là "kết quả của đề tài" cho tới khi có `research/reviews/…-results.md` đối chiếu ngưỡng.
5. Tính đến **2026-10-11, thư mục này vẫn rỗng theo đúng schema trên** — không được tạo file giả/benchmark giả ở đây.
6. **Ghi chú (`DEC-PHASE-002`, 2026-10-11):** nhóm nghiên cứu đã tự thực hiện thử nghiệm bring-up phần cứng thật (ESP32-S3+ADS1115+INA333+CD74HC4067) ngoài phạm vi agent, ghi lại ở [`research/notebooklm_sync/experiments/`](../../notebooklm_sync/experiments/). Các file đó là **ghi chú kỹ thuật thật nhưng không theo schema ở trên** (thiếu `session_manifest.csv`/`perturbation_log.csv`/`reference_check.csv`, thiếu ngưỡng-chốt-trước-khi-đo chép lại ở đầu file). Trước khi được tính là "GATE 0 pass" hay trích vào báo cáo nộp, nội dung đó phải được **chuyển hoá đúng định dạng ở đây** (1 file/phiên, header ngưỡng, không sửa bản gốc). Xem `CLM-EVID-002`.
