# OUTLINE BÁO CÁO TOÀN VĂN — ViSEF

## Đề tài: Nghiên cứu và phát triển găng tay thông minh hỗ trợ đánh giá và theo dõi chức năng vận động bàn tay trong phục hồi chức năng sau đột quỵ

> **Học sinh:** Văn Ngọc Nhật Anh — THPT Quảng Trị
> **Phiên bản:** v2.0 — 2026-09-13 (chốt tên đề tài; phần cứng ESP32-S3 + CD74HC4067; bổ sung mục tiêu tái tạo bàn tay 3D)
> **"Viên đạn":** Theo dõi định lượng chức năng bàn tay tại nhà, liên tục giữa các lần tái khám lâm sàng.
> **Lưu ý:** Mọi ô `[X]` chỉ được điền **sau** GATE experiment. Không bịa số. Xem `AGENTS.md`.

---

## A. VẤN ĐỀ NGHIÊN CỨU

### 1. Lý do chọn đề tài

*(Bản chốt hiện tại nằm ở `docs/bao_cao/A1_ly_do_chon_de_tai.md` — 4 đoạn, viết theo form giải nhất.)*

Cấu trúc đoạn:
- Gánh nặng đột quỵ + di chứng liệt/yếu tay; vì sao đây là vấn đề con người, không phải vấn đề kỹ thuật.
- Phục hồi bàn tay = luyện tập tại nhà; kỹ thuật viên chỉ gặp bệnh nhân mỗi 1–3 tháng → quãng giữa là **"hộp đen"**.
- Công cụ hiện tại (FMA, ARAT, Box and Block, lực kế Jamar, E-Link) là **ảnh chụp tại thời điểm đo**, chi phí cao, chủ yếu ở cơ sở y tế.
- Xác nhận độc lập: hội đồng chuyên gia quốc tế 2024 (DOI 10.1109/OJEMB.2024.3523442) + nghiên cứu OTHER 2026 (DOI 10.1080/09638288.2026.2643929) + phỏng vấn KTVVLTL-PHCN.
- Câu chốt tên đề tài + một câu mô tả giải pháp.

### 2. Mục tiêu nghiên cứu

*(Bản chốt ở `docs/bao_cao/A2_muc_tieu.md`)*
- Chế tạo găng tay tích hợp khung cứng và mảng phần tử cảm biến, ghi nhận lực và hướng chuyển động của từng lóng ngón.
- Xây dựng phương pháp xử lý tín hiệu giảm ảnh hưởng drift, trích xuất vector lực và suy luận hướng khớp.
- Xây dựng mô hình **tái tạo bàn tay 3D** từ dữ liệu lực-hướng để chuyên gia đánh giá từ xa.
- Xây dựng mô hình đánh giá chức năng và triển khai trên thiết bị biên.
- Đánh giá khả năng theo dõi diễn tiến qua nhiều phiên đo.

### 3. Tiêu chí của dự án

*(Bản chốt ở `docs/bao_cao/A3_tieu_chi.md`; ngưỡng số điền sau GATE)*
- Mảng sensing element ổn định, lặp lại trong các bài tập chuẩn.
- Tái tạo được bàn tay 3D phản ánh flexion/extension từng ngón.
- Phân biệt được ≥ 3 mức suy giảm chức năng trên phantom.
- Chỉ số thu được có tương quan với công cụ đánh giá lâm sàng chuẩn.
- **Biên độ tín hiệu phản ánh thay đổi chức năng lớn hơn biên độ drift/nhiễu** *(tiêu chí sống còn — GATE C)*.
- Không tạo cảnh báo thay đổi giả qua nhiều phiên đo *(GATE D)*.
- Suy luận tại biên với độ trễ thấp *(GATE F)*.
- Tự phát hiện được sensing element hoạt động bất thường *(GATE E)*.

### 4. Đối tượng và phạm vi nghiên cứu

*(Bản chốt ở `docs/bao_cao/A4_doi_tuong_pham_vi.md`)*
- **Kỹ thuật:** sensing element Velostat + copper tape, khung găng in 3D, ESP32-S3 + CD74HC4067, Orange Pi 5 Pro, phantom bàn tay, load cell tham chiếu.
- **Y sinh:** di chứng yếu/liệt tay sau đột quỵ — nghiên cứu nền; giai đoạn này chỉ bench/phantom, người tình nguyện khỏe chỉ sau khi có phê duyệt.
- **Giới hạn:** không chẩn đoán; không phải thiết bị tập; không thay thế đánh giá lâm sàng.

### 5. Địa điểm nghiên cứu và thực nghiệm

*(Bản chốt ở `docs/bao_cao/A5_dia_diem.md`)*
- Phòng thực hành vật lý, phòng sáng tạo trường THPT Quảng Trị, và tại nhà.
- Tham khảo thực tiễn: KTVVLTL-PHCN (chị tác giả) — xác nhận pain point và góp ý giao thức bài tập; chuyên gia PHCN tại phcn-online.com.

### 6. Phương pháp nghiên cứu

*(Bản chốt ở `docs/bao_cao/A6_phuong_phap.md`)*
- **Tổng quan tài liệu:** prior art găng tay cảm biến; công cụ đánh giá tay sau đột quỵ; đặc tính Velostat; các hệ thống theo dõi tại nhà.
- **Tham khảo ý kiến:** KTV VLTL-PHCN (phỏng vấn có ghi chép) + chuyên gia độc lập.
- **Thực nghiệm bench:** jig nén + load cell tham chiếu; phantom bàn tay nhiều mức chức năng; đo lặp, ghi log thô.
- **Phân tích tín hiệu:** trích đặc trưng, đọc vi sai, bù ảnh hưởng drift, suy luận hướng khớp.
- **Thống kê:** CV, ICC, SEM, MDC, Cohen's d, tương quan Pearson/Spearman, tỷ lệ báo động giả.

---

## B. GIẢI PHÁP VÀ THIẾT KẾ

### 1. Tổng quan đề tài

**Sơ đồ pipeline (chốt):**

```
Bàn tay người dùng
      ↓ [bài tập chuẩn: gập / duỗi / chụm / bóp / chạm ngón]
Khung găng in 3D + mảng sensing element (Velostat + copper tape)
      ↓
CD74HC4067 (16 kênh) ×1 (12 kênh) hoặc ×2 (24 kênh)
      ↓ [1 kênh analog, chọn MUX bằng chân EN]
ESP32-S3  · ADC1 12-bit + trung bình N mẫu · frame + CRC · BLE/UART
      ↓
Orange Pi 5 Pro (RK3588, NPU ~6 TOPS)
  ├─ Bù ảnh hưởng drift (ô tham chiếu + cặp đối xứng)
  ├─ Trích đặc trưng → vector lực theo khớp
  ├─ Suy luận hướng gập/duỗi → tái tạo bàn tay 3D
  ├─ Mô hình INT8 (RKNN) trên NPU
  └─ Cờ "UNRELIABLE" khi dữ liệu không hợp lệ
      ↓
Đường cong chức năng theo tuần
      ↓
Dashboard → KTV / bác sĩ theo dõi từ xa
```

**Nguyên lý cơ khí (điểm kỹ thuật trung tâm):**
ngón tay chuyển động theo hướng X → tì vào vách khung hướng X → nén sensing element trên vách đó → đọc được lực-hướng → **suy luận** hướng gập/duỗi của từng khớp. Không dùng IMU.

### 2. Bất cập của các giải pháp hiện tại và giải pháp đề tài

| Giải pháp hiện tại | Bất cập | Giải pháp của đề tài |
|---|---|---|
| Lực kế Jamar | Chỉ đo tổng lực bóp, một thời điểm, cần người đo | Theo dõi tại nhà, nhiều ngón, theo thời gian |
| Hệ thống E-Link | Chi phí cao, chỉ ở cơ sở y tế | Linh kiện rẻ, dùng được tại nhà |
| Găng tay IMU/flex thương mại | Đắt theo số trục, trôi, cồng kềnh | Vách khung + vật liệu piezoresistive, mã hóa cả hướng và lực |
| Găng tay phục hồi chức năng chủ động (robot găng) | Gây phụ thuộc máy, rủi ro an toàn, cần người có chuyên môn | **Không can thiệp vào vận động** — chỉ đánh giá/theo dõi |
| Đeo cảm biến ở cổ tay | Không ghi được chuyển động ngón; không phân biệt vận động có mục đích | Đo tại từng khớp ngón |
| Phần mềm mô phỏng (RehabReach và tương tự) | Mô phỏng, thiếu vi cử động và không tương tác thực | Đo trực tiếp trên bàn tay thật; 🔵 cần xác minh thông tin RehabReach trước khi đưa vào báo cáo |

> **Khoảng trống thật:** chưa có hệ thống nào **vừa rẻ, vừa tại nhà, vừa tạo ra dữ liệu định lượng chức năng bàn tay theo tuần**, dùng được bởi người không chuyên môn và theo dõi được bởi kỹ thuật viên từ xa — **và tự biết khi nào dữ liệu của mình không còn đáng tin**.

### 3. Thiết kế phần cứng

*(Chi tiết đầy đủ: `docs/04_Hardware_Architecture.md`)*

| STT | Linh kiện | SL | Chức năng |
|---|---|---|---|
| 1 | Vật liệu piezoresistive Velostat | [X] tấm | Lớp nhạy áp lực trong sensing element |
| 2 | Copper tape (điện cực) | [X] | Điện cực trên/dưới, cấu trúc sandwich |
| 3 | Khung găng in 3D (PLA/PETG + TPU) | 1 | Vách ép tạo hướng + định vị sensing element |
| 4 | CD74HC4067 (MUX 16:1) | 1–2 | Mở rộng 12–24 kênh analog |
| 5 | **ESP32-S3** | 1 | ADC1 12-bit, lọc/trung bình, đóng gói frame + CRC, BLE/UART |
| 6 | Orange Pi 5 Pro (RK3588) | 1 | Xử lý tín hiệu, suy luận INT8 trên NPU, dashboard |
| 7 | Load cell + HX711 | 1 | Tham chiếu lực trên bench (ground truth cho GATE) |
| 8 | Phantom bàn tay (in 3D, khớp hãm góc) | 1 | Ground truth cho GATE A/B/C |

*(Bỏ mục level shifter 5V→3.3V của phiên bản cũ — ESP32-S3 chạy 3.3 V nên khớp trực tiếp với Orange Pi.)*

### 4. Nguyên lý sensing element và trích đặc trưng

**4.1 Cơ chế piezoresistive**
- Velostat: điện trở giảm khi nén; quan hệ **phi tuyến**, có hysteresis, creep, drift, phụ thuộc nhiệt độ và cơ tính nền.
- Hệ quả: **không** chuyển ADC thành Newton; chỉ dùng đặc trưng **tương đối** và **động**.

**4.2 Bố trí kênh**
- Cấu hình 1 (12 kênh): 4 ngón dài × 2 khớp + ngón cái × 2 + lòng bàn tay × 1 + ô tham chiếu × 1.
- Cấu hình 2 (24 kênh): mỗi khớp có **cặp đối xứng** hai vách → đọc vi sai.

**4.3 Bài tập chuẩn và đặc trưng**

| Bài tập | Vùng kích hoạt | Đặc trưng |
|---|---|---|
| Gập từng ngón (flexion) | vách lòng bàn tay của ngón đó | Biên độ, thời gian lên đỉnh |
| Duỗi (extension) | vách đối diện | Dấu và biên độ vi sai |
| Chụm ngón (pinch) | ngón cái + ngón đối diện | Tỷ lệ giữa hai vùng |
| Bóp cả bàn tay (power grip) | nhiều ngón + lòng bàn tay | Tổng lực, phân bố, độ bền |
| Chạm ngón cái–đầu ngón (opposition) | ngón cái + 4 ngón | Mẫu phối hợp |

**4.4 Bù ảnh hưởng drift**
- Cặp sensing element đối xứng → hiệu `d` triệt thành phần đồng pha.
- Ô tham chiếu → phát hiện trôi hệ thống → cờ `UNRELIABLE`.
- Không dùng từ "loại bỏ drift".

### 5. Mô hình học máy và suy luận tại biên

- **Đầu vào:** vector đặc trưng từ mảng sensing element theo từng bài tập.
- **Baseline trước:** hồi quy tuyến tính / rừng ngẫu nhiên — **chỉ dùng mạng nơ-ron nếu baseline không đủ**.
- **Hai nhiệm vụ tách biệt:**
  1. **Suy luận hướng khớp** (từ trường lực → hướng) — kiểm chứng bằng GATE B trên phantom có góc biết trước.
  2. **Chỉ số chức năng** (từ đặc trưng → chỉ số theo tuần) — kiểm chứng bằng GATE C/D.
- **Không claim thay thế Fugl-Meyer.** Chỉ claim: chỉ số có **tương quan** với công cụ chuẩn (khi đo được).
- **Lượng tử hóa:** INT8 → RKNN → NPU RK3588; phải báo cáo độ trễ và mức giảm độ chính xác so với FP32.

### 6. Tái tạo bàn tay 3D

- Đầu vào: vector lực-hướng theo khớp.
- Đầu ra: mô hình bàn tay 3D biểu diễn mức gập/duỗi từng ngón theo thời gian.
- Mục đích: chuyên gia xem nhanh "bệnh nhân tuần này gập được tới đâu", không phải để thay goniometer.
- Kiểm chứng: GATE B (MAE theo khớp so với phantom góc biết trước) + đánh giá định tính của KTV.

### 7. Dashboard và theo dõi từ xa

- Bệnh nhân: hướng dẫn bài tập, phản hồi tức thời, không cần đọc số liệu kỹ thuật.
- KTV: xem đường cong theo tuần của từng bệnh nhân; thấy ngay khi đường cong đi ngang hoặc giảm.
- Cảnh báo: chỉ khi vượt MDC **và** dữ liệu ở trạng thái hợp lệ.

---

## C. CHẾ TẠO MÔ HÌNH VÀ VẬN HÀNH THỬ NGHIỆM

*(Toàn bộ ngưỡng PASS/FAIL chi tiết ở `research/protocols/06_glove_hand_GATE_experiment.md`)*

### 1. GATE 0 — Độ lặp lại của sensing element
- Đường cong tải tăng/giảm (hysteresis), creep 60 s, 100 chu kỳ, 3 ngày, 5 sensing element.
- Pass dự kiến: CV trong phiên ≤ 5%; ICC giữa phiên ≥ 0,75.

### 2. GATE A — Phân biệt hướng
- Lực theo 4 hướng × 3 mức × 20 lần trên phantom.
- Pass dự kiến: accuracy 4 hướng ≥ 85%; cặp đối lập ≥ 90%.

### 3. GATE B — Tái tạo bàn tay 3D
- Phantom có góc hãm 0°/30°/60°/90°; so góc suy luận với góc thật.
- Pass dự kiến: MAE ≤ 15°, tương quan r ≥ 0,8.

### 4. GATE C — **Độ nhạy phát hiện thay đổi (tiêu chí sống còn)**
> "Thay đổi chức năng thật có lớn hơn drift/nhiễu của chính hệ thống không?"
- 3 mức chức năng mô phỏng × ≥ 5 phiên × ≥ 3 ngày.
- Pass dự kiến: Δ giữa mức 1 và 3 ≥ 2σ; Cohen's d ≥ 0,8; MDC < mức chênh giữa hai mức liền kề.
- **FAIL ⇒ dừng, báo cáo trung thực.**

### 5. GATE D — Nhiều ngày không báo động giả
- Giữ nguyên một mức ≥ 10 ngày; đếm báo động giả.
- Pass dự kiến: ≤ 10% số phiên; không có xu hướng trôi giả đơn điệu.

### 6. GATE E — Tự phát hiện lỗi
- Bơm lỗi có chủ đích: đứt dây, chập, trôi mạnh, giảm độ nhạy, tăng nhiễu.
- Pass dự kiến: phát hiện ≥ 90%; báo động giả ≤ 5%; phát hiện ≤ 10 s.

### 7. GATE F — Suy luận tại biên
- Đo độ trễ, độ ổn định 30 phút, mức giảm độ chính xác INT8 vs FP32.
- Pass dự kiến: ≤ 50 ms; mất mát ≤ 2%.

### 8. Kết quả tích hợp hệ thống (ESP32-S3 ↔ Orange Pi)
- Tốc độ khung thực đo, tỷ lệ lỗi CRC, độ trễ đầu–cuối, số frame mất khi truyền BLE.

### 9. Kết luận
- Bảng đối chiếu **tiêu chí A.3 → kết quả đo thật** (không có ô nào bỏ trống).
- Nêu rõ: proof-of-concept trên phantom; chưa thử trên bệnh nhân; không thay thế đánh giá lâm sàng.

### 10. Hướng phát triển
- Giai đoạn 2: người tình nguyện khỏe (sau IRB/SRC).
- Giai đoạn 3: pilot bệnh nhân sau đột quỵ (bệnh viện đối tác + IRB).
- Mở rộng: bại não trẻ em, phục hồi sau chấn thương bàn tay, sàng lọc sa sút vận động tinh.

---

## TÀI LIỆU THAM KHẢO *(verify đầy đủ trước khi nộp — xem `research/evidence/SOURCE_LEDGER.csv`)*

- [ ] Amin K.R. et al., *Remote Monitoring for the Management of Spasticity: Challenges, Opportunities and Proposed Technological Solution*, IEEE OJEMB (2024), DOI 10.1109/OJEMB.2024.3523442
- [ ] *Occupational Therapy at Home E-Rehabilitation (OTHER)* (2026), DOI 10.1080/09638288.2026.2643929, PMID 41918405
- [ ] Systematic review: AI-based smart glove for hand movement recognition and rehabilitation monitoring (Springer, 2026) 🔵 verify
- [ ] Zhu lab, *A Glove-based System for Studying Hand-Object Manipulation* (IROS 2017) — prior art gần nhất
- [ ] *A Reconfigurable Data Glove for Reconstructing Physical and Virtual Grasps* (2023)
- [ ] *Development of an Instrumented Glove for Palmar Pressure Assessment in Kayakers* (Sensors 2026)
- [ ] *Wearable technology to capture arm use of stroke survivors in home and community settings* (medRxiv 2023 / PMC9901039)
- [ ] *Tracking Upper Limb Motion via Wearable Solutions* — JMIR 2024
- [ ] Hopkins M. et al., đặc tính Velostat — IEEE Sensors J 2020 🔵 verify
- [ ] *Effect of task-oriented training assisted by force feedback hand rehabilitation robot…* (2024, PMC11092254)
- [ ] *Quantitative measurement of finger usage in stroke hemiplegia using ring-shaped wearable devices* (2023, PMC10242812)
- [ ] Nguồn dịch tễ đột quỵ Việt Nam + nguồn "80% bệnh nhân yếu tay" — **bắt buộc đối chiếu lại**
- [ ] Nguồn giá/giới hạn của Jamar và E-Link — **bắt buộc đối chiếu lại**

---

## GHI CHÚ CHO PHIÊN SAU

**Đã thay đổi trong phiên 2026-09-13:**
- ✅ Chốt tên đề tài chính thức (bỏ chữ "hệ thống … TinyML … giá thấp" trong tên cũ).
- ✅ Phần cứng: Arduino Mega 2560 → **ESP32-S3 + CD74HC4067** (DEC-HW-003).
- ✅ Bố trí kênh: 6 vùng → **12 kênh (tối thiểu) / 24 kênh (đọc vi sai)** (DEC-HW-004).
- ✅ Bổ sung mục tiêu **tái tạo bàn tay 3D** vào A.2/A.3/outline.
- ✅ GATE experiment viết lại cho găng tay: `research/protocols/06_glove_hand_GATE_experiment.md`.
- ✅ Đồng bộ README, INDEX, docs/01–04, GLOSSARY, ledger.

**Còn chờ:**
- [ ] Chốt cấu hình kênh 1 hay 2 (hoặc lộ trình 1 → 2).
- [ ] Chốt giao thức bài tập chuẩn cùng KTVVLTL-PHCN (thứ tự, số lần, thời gian nghỉ).
- [ ] Đo `R_sensor` theo tải → chọn R_f.
- [ ] Đo ENOB thực + tốc độ khung thực.
- [ ] Rà soát prior art (docs/03) → chốt lại mức novelty.
- [ ] Điền số thật vào A.3 và mục C sau khi có log.
