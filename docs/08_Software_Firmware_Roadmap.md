# 08 — Lộ trình phần mềm & firmware (kế hoạch, chưa viết code)

> **Ngày lập:** 2026-10-19 · **Trạng thái:** `PLAN — PROPOSED`. **Chưa có dòng code nào được viết cho pipeline hiện hành**; tài liệu này là kế hoạch để bắt đầu code **sau khi** đề cương và Gate 0 được duyệt (theo chỉ đạo chủ dự án ngày 2026-10-19).
> **Căn cứ:** [`IMPLEMENTATION_PIPELINE.md`](../research/context/IMPLEMENTATION_PIPELINE.md), [`CURRENT_DESIGN_BASELINE.md`](../research/context/CURRENT_DESIGN_BASELINE.md), [`protocols/10`](../research/protocols/10_gate0_task_state_sheet.md) + [`10a`](../research/protocols/10a_gate0_channel_map_and_acquisition_budget.md), [`docs/07`](07_Vision_TaskState_Architecture.md), `DEC-PHASE-001/002`.
> **Lưu ý:** `firmware/mega_link_diagnostics/` là **di sản** của đề tài cũ (Mega ↔ Orange Pi), giữ để truy vết, không dùng làm nền cho firmware mới.
> **⚠ CẬP NHẬT 2026-10-20 (`DEC-AAN-003`, `DEC-PROP-015`):** danh sách trạng thái `ASSIST/EVAL/AAN/TASK/INVALID/FAULT` ở §2 và §4 (pha F4) là **mô hình 7 trạng thái đã bị thay thế** — mô hình hiện hành là **3 pha vận hành** (trợ lực toàn phần → trợ lực theo nhu cầu → tự vận động có theo dõi), cộng trạng thái **không hợp lệ** cho phiên đo lỗi và trạng thái **dừng an toàn**. Các mã `F0–F7`, `Gate n`, `OPEN`, `SIMULATED` là **mã nội bộ**, không dùng trong văn bản nộp; bản ghép cặp đã dịch sang "pha thứ nhất…thứ bảy", "mốc n", "chưa chốt", "nhãn mô phỏng" (`docs/DE_CUONG_A_B_C_GHEP_CAP_B_C_2026-10-20.md` B.9, C.7).

---

## 1. Nguyên tắc bất biến khi viết code

1. **Không hardcode ngưỡng.** Mọi đặc trưng, ngưỡng, cửa sổ, số chu kỳ, hysteresis, timeout, giới hạn hành trình đều nằm trong file cấu hình có phiên bản. Giá trị chưa chốt phải là `null`/`OPEN` và code phải **từ chối chạy** chế độ đánh giá nếu gặp `null`, thay vì tự thay giá trị mặc định.
2. **Đóng băng trước khi đánh giá.** Cấu hình được băm (`config_version_hash`) và ghi vào `session_manifest`; dữ liệu dùng để chỉnh tham số tách khỏi dữ liệu dùng để báo cáo.
3. **Mô phỏng ≠ số đo.** Mọi dữ liệu tổng hợp/replay gắn nhãn `SIMULATED`; log thật gắn `REAL_BENCH` hoặc `PHANTOM`. Báo cáo không được trộn.
4. **Log gốc bất biến.** File gốc không bị ghi đè; bản tính lại đặt `…_derived.csv` (quy tắc `research/bench/logs/README.md`). Không sinh file log giả trong `research/bench/logs/`.
5. **An toàn nằm ở tầng thấp.** Giới hạn hành trình, dừng, nhả và watchdog phải chạy độc lập với suy luận thị giác và độc lập với logic cấp cao; cơ cấu nhả không chỉ dựa phần mềm (`protocols/09` §3.2).
6. **Không có thao tác KTV trong luồng vận hành** (`DEC-REHAB-001`); nút bấm của người vận hành chỉ dùng cho khởi động/dừng khẩn ở pha bench, không dùng để chuyển chế độ thay hệ thống.
7. **Mọi module có test.** Test chạy được **không cần phần cứng** (dùng replay/simulator), để không lấy cớ "chưa có board" mà bỏ test.
8. **Không claim trong code/comment/README** về hiệu quả lâm sàng, an toàn được chứng nhận, novelty hay "đã dùng tại nhà".

---

## 2. Kiến trúc phần mềm đề xuất

```text
┌────────────────────────── ESP32-S3 (firmware) ──────────────────────────┐
│ scan MUX (CD74HC4067) + ADS1115 → khung dữ liệu (frame_id, t_ms)        │
│ DSP 4 bước đang dùng (đọc nháp → vùng chết → bám mốc tĩnh → EMA)        │
│ validity flags / REF drift check                                        │
│ MODE SUPERVISOR (ASSIST/EVAL/AAN/TASK/INVALID/FAULT) ← config có version │
│ servo bounded command + giới hạn hành trình + stop/release + watchdog    │
│ stream JSONL qua USB-serial; nhận task_state từ Orange Pi               │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │ serial (JSON Lines, schema v1)
┌──────────────────────────────┴──────────── Orange Pi 5 Pro ─────────────┐
│ host ingest: ghi log phiên, manifest, checksum                          │
│ vision pipeline (docs/07): detector adapter → tracker → task-state      │
│ feedback UI cho người tập                                               │
│ analysis: calibration curves, đặc trưng, bảng nhầm lẫn, báo cáo         │
└─────────────────────────────────────────────────────────────────────────┘
```

**Quyết định kiến trúc còn `OPEN`:** đặt mode supervisor trên ESP32-S3 (trễ thấp, chạy cả khi mất kết nối với Orange Pi) hay trên Orange Pi (dễ test/dễ đổi luật). Đề xuất của agent: **supervisor ở ESP32-S3**, Orange Pi chỉ gửi pha tác vụ + nhãn; lý do là yêu cầu an toàn mục 1.5. Đây là đề xuất, cần `DEC-IMPL-002`.

---

## 3. Bố trí thư mục đề xuất trong repo

```text
firmware/
├── esp32s3_glove_acq/            # sketch/PlatformIO project (F2)
│   ├── src/{acq,dsp,supervisor,servo,protocol,safety}/
│   ├── config/channel_map.h      # sinh từ 10b_channel_map_proposed.csv
│   └── test_host/                # bản mirror logic supervisor để unit test trên PC
software/
├── glove/                        # package Python phía host
│   ├── ingest/                   # đọc serial/replay, validate schema
│   ├── calib/                    # hiệu chuẩn Flex/Velostat/REF
│   ├── features/                 # đặc trưng cho supervisor
│   ├── supervisor/               # mirror state machine (test được không cần board)
│   ├── vision/                   # adapters + tracker + task_state (docs/07)
│   ├── console/                  # dashboard bench
│   ├── reports/                  # sinh bảng/biểu từ log
│   └── schemas/                  # JSON schema: frame, event, manifest, config
├── configs/                      # *.yaml có version; ngưỡng OPEN = null
├── sim/                          # simulator/replay; output luôn nhãn SIMULATED
└── tests/                        # pytest; không yêu cầu phần cứng
data/                             # BỊ GIT IGNORE (log thô, ảnh, video)
```

Dữ liệu đo, ảnh, video, và bất kỳ thứ gì có thể liên quan người tham gia **không** vào Git; dùng `data/` (ignore) hoặc lưu ngoài theo quy tắc `research/README.md`.

---

## 4. Các pha triển khai

### F0 — Schema & hạ tầng dữ liệu (không cần phần cứng)

| | |
|---|---|
| Đầu vào | `protocols/10`, `10a`, `10b`, `research/bench/templates/*.csv` |
| Đầu ra | JSON Schema cho `frame`, `event`, `task_state_msg`, `session_manifest` (mở rộng từ template có sẵn, **không** đổi header template cũ), file cấu hình mẫu với mọi ngưỡng `null`, script validate |
| Exit | schema được duyệt; validate chạy được trên file ví dụ; `research/bench/logs/` vẫn rỗng |
| Rủi ro | đổi header template cũ sẽ phá `scripts/check_bench_templates.py` → chỉ **thêm** file mới, không sửa template |

### F1 — Simulator / replay bench

| | |
|---|---|
| Đầu vào | schema F0 |
| Đầu ra | bộ sinh tín hiệu Flex/Velostat/nhãn tác vụ tổng hợp có tham số (biên độ, trôi, nhiễu, trễ), **luôn** nhãn `SIMULATED`; bộ replay log thật (khi có) |
| Exit | supervisor chạy được với simulator; test phủ các tình huống tín hiệu lỗi/mất khung |
| Giới hạn | không phải bằng chứng thiết bị hoạt động; chỉ để phát triển và test logic |

### F2 — Firmware acquisition (ESP32-S3)

| | |
|---|---|
| Đầu vào | bản đồ kênh đã duyệt (`DEC-CHMAP-001`), SPS/tốc độ khung đã chốt (`DEC-ACQ-001`) |
| Đầu ra | scan MUX + ADS1115, khung dữ liệu có `frame_id`/`t_ms`, DSP hiện hành, cờ hợp lệ kênh, streaming JSONL, watchdog, lệnh servo có giới hạn hành trình, stop/release |
| Exit | đo được tốc độ khung thật và ghi vào log; so với `[TÍNH TOÁN]` ở `10a` §5; không mất khung trong ⟨thời gian⟩ (giá trị `OPEN`) |
| Rủi ro | toolchain ESP32 không cài được trong sandbox agent (chỉ truy cập github/pypi) → build/nạp firmware phải làm trên máy nhóm; agent có thể viết code + test logic mirror trên PC |

### F3 — Hiệu chuẩn & đặc trưng hoá cảm biến (Gate 1)

| | |
|---|---|
| Đầu vào | phương pháp tham chiếu Flex đã chọn; tải tham chiếu độc lập cho bench Velostat |
| Đầu ra | đường cong hiệu chuẩn từng Flex trên vị trí lắp thật; bảng so sánh vị trí Velostat (ngón–vật vs ngón–nẹp); đặc trưng trôi từ `REF_1/REF_2`; báo cáo lặp lại |
| Exit | mỗi tín hiệu chứng minh được là diễn giải đúng vai trò đã giao, hoặc phải đổi vị trí/vai trò |
| Cấm | quy đổi Velostat → Newton; gán ADC thành độ khi chưa hiệu chuẩn |

### F4 — Mode supervisor & quy tắc chuyển tự động (Gate 4)

| | |
|---|---|
| Đầu vào | kết quả F3 + phương pháp phân biệt tự nguyện/máy đã chọn (`protocols/10` §5) |
| Đầu ra | state machine đầy đủ (`ASSIST/EVAL/AAN/TASK/INVALID/FAULT`), config có version, test property: (a) không bao giờ coi chuyển động do servo tạo là tự nguyện, (b) tín hiệu không hợp lệ → fallback an toàn, (c) mất thị giác → không kéo, (d) ngưỡng `null` → từ chối chạy chế độ đánh giá |
| Exit | trên bench/phantom hệ thống chuyển mode lặp lại được, từ chối tín hiệu mơ hồ, dừng/nhả đúng quy trình |
| Cấm | chọn ngưỡng hậu nghiệm; dùng lại ngưỡng 5 N đã rút; mô tả thử phantom như kết quả trên người |

### F5 — Nhánh thị giác (Gate 3) — chạy song song từ sau Gate 0

Theo [`docs/07`](07_Vision_TaskState_Architecture.md): adapter ClassicCV trước, tracker, classifier nhãn, hiệu chuẩn, phiếu benchmark trên Orange Pi 5 Pro, tập nhãn + bảng nhầm lẫn. Exit: có số đo độ đúng/độ trễ **của bản thử** trên đúng phần cứng, kèm phiên bản model/config.

### F6 — Bench console & báo cáo (Gate 5)

| | |
|---|---|
| Đầu ra | dashboard xem trực tiếp khung cảm biến, mode, nhãn tác vụ, sự kiện trợ lực/dừng; công cụ sinh báo cáo phiên (bảng + biểu) từ log; phiếu so sánh baseline trợ lực cố định vs AAN tự động |
| Exit | một phiên tích hợp bench/phantom chạy trọn chu trình và log đủ các trường bắt buộc |
| Cấm | trình bày phiên phantom như thử nghiệm người; so sánh không công bằng giữa hai cấu hình |

### F7 — Cổng người (không thuộc lộ trình code này)

Chỉ xem xét sau khi Stage 1 + đánh giá an toàn độc lập + phê duyệt cần thiết hoàn tất (`protocols/09` §5). **Không viết code cho mục đích thử trên người trong phạm vi tài liệu này.**

---

## 5. Thứ tự khuyến nghị và phụ thuộc

```text
Gate 0 duyệt (10/10a/10b) ──> F0 ──> F1 ──> F4 (logic, chạy với simulator)
                        └────> F5 (thị giác, song song)
Board thật + DEC-ACQ-001 ───> F2 ──> F3 ──> F4 (chạy với dữ liệu thật)
F3 + F4 + F5 ─────────────────────────────> F6 ──> phiên tích hợp bench/phantom
```

F4 có thể bắt đầu trước khi có board nhờ F1; nhưng **không** được báo cáo kết quả F4 như kết quả thiết bị cho tới khi chạy trên dữ liệu thật có log.

---

## 6. Môi trường & công cụ

| Thành phần | Đề xuất | Ghi chú |
|---|---|---|
| Python host | 3.11, `numpy`, `opencv-python-headless`, `pyserial`, `pytest`, `pyyaml` | thêm vào `requirements.txt` khi bắt đầu F0 (hiện `requirements.txt` chỉ có numpy/matplotlib/scikit-learn) |
| Orange Pi 5 Pro | Debian aarch64, OpenCV; NPU chỉ dùng nếu nhận adapter học sâu | chưa benchmark; kiểm tra phiên bản OpenCV trên máy thật trước |
| Firmware | PlatformIO (ESP32-S3) hoặc Arduino IDE | sandbox agent **không** tải được toolchain ESP32 (chỉ github/pypi) → build trên máy nhóm |
| Logic test trên PC | mirror state machine bằng C++ host-test hoặc Python | để test không cần board |
| Dữ liệu | `data/` ignore; ảnh/video không vào Git | đúng quy tắc `research/README.md` |
| Git | commit nhỏ, PR vào `main` theo `DEC-VCS-001` | chỉ push khi nhóm thống nhất |

---

## 7. Cần gì từ chủ dự án để bắt đầu code

1. Duyệt phương án phân bổ kênh (PA-1/PA-2/PA-3a/PA-3b) → `DEC-CHMAP-001`.
2. Chốt thông số thìa + vùng đích + tiêu chí `PLACE_OK` (`protocols/10` §2).
3. Chọn phương pháp phân biệt vận động tự nguyện vs do máy (M1–M5).
4. Chốt tốc độ khung mục tiêu + SPS + N → `DEC-ACQ-001`.
5. Trả lời 8 câu hỏi kỹ thuật ở `10a` §7 trên board thật.
6. Xác nhận nơi đặt mode supervisor (ESP32-S3 hay Orange Pi) → `DEC-IMPL-002`.
7. Xác nhận cấu trúc thư mục mục 3 và việc mở rộng `requirements.txt`.

Chưa có 1–3 thì **chưa** nên viết F4; chưa có 4–5 thì chưa nên viết F2; F0/F1/F5 có thể bắt đầu ngay sau khi Gate 0 được duyệt vì không phụ thuộc phần cứng.

---

## 8. Rủi ro chính và cách giảm

| Rủi ro | Hệ quả | Cách giảm |
|---|---|---|
| Velostat chủ yếu đo lực ép ngón–nẹp, không phải ngón–vật | đặc trưng chuyển mode vô nghĩa | cặp lòng/mu (PA-2) + test vị trí ở F3 trước khi đặt ngưỡng |
| Servo cuốn dây một chiều không tạo được duỗi/hồi | Gate 2 fail, tác vụ thìa không chạy | thiết kế cơ cấu hồi/nhả và thử không tải trước khi tích hợp (`protocols/09` §3) |
| Supervisor đếm nhầm chu kỳ do servo tạo | thăng cấp sai sang AAN | phương pháp M1–M5 + test property (a) ở F4 |
| Tốc độ khung chuỗi ADS1115 thấp hơn mục tiêu cũ | trễ điều khiển, nhãn tác vụ lệch pha | đo thật ở F2, chọn lại SPS/N, khai báo trễ trong log |
| Thị giác không ổn định dưới ánh sáng trong nhà | nhiều `T_UNKNOWN` | adapter cắm được; tập nhãn thật; báo cáo tỷ lệ `UNKNOWN` thay vì giấu |
| Không có tham chiếu lực độc lập | không được phép phát biểu về lực/an toàn | mua/mượn thiết bị đo độc lập trước Gate 2; Velostat không thay thế |
| Viết code trước khi chốt Gate 0 | phải làm lại, dễ "hợp thức hoá" ngưỡng theo code | tuân thủ thứ tự mục 5 |

---

## 9. Tài liệu này không khẳng định điều gì

- Chưa có module, firmware, pipeline thị giác hay dashboard nào được viết/chạy.
- Không có tốc độ khung, độ trễ, độ đúng, lực, khối lượng hay chi phí nào đã được đo cho cấu hình cuối.
- Kế hoạch này không cấp phép thử có cấp nguồn trên người, và không thay thế đánh giá an toàn hay phê duyệt.
