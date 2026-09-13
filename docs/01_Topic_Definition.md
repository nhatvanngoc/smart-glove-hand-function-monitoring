# 01 — Định nghĩa đề tài

> **Ngày cập nhật:** 2026-09-13
> **Học sinh:** Văn Ngọc Nhật Anh — THPT Quảng Trị
> **Nguồn gốc quyết định:** `research/context/DECISION_LOG.md` (DEC-TOPIC-018, DEC-TOPIC-019, DEC-HW-003, DEC-HW-004).
> **Trạng thái bằng chứng:** tài liệu **định hướng + thiết kế**. Mọi tuyên bố về độ chính xác/độ nhạy/tương quan lâm sàng là **giả thuyết** cho đến khi qua GATE experiment. Chưa có kết quả đo.

---

## 1. Tên đề tài

**Tiếng Việt (chính thức):**

> **Nghiên cứu và phát triển găng tay thông minh hỗ trợ đánh giá và theo dõi chức năng vận động bàn tay trong phục hồi chức năng sau đột quỵ**

**Tiếng Anh (dùng khi nộp ISEF/ViSEF bản tiếng Anh):**

> A low-cost smart glove with directional piezoresistive sensing for quantitative hand motor-function assessment and longitudinal monitoring in post-stroke rehabilitation.

**Pitch 1 câu (nói với giám khảo):**

> "Sau đột quỵ, bệnh nhân phải tự tập tay ở nhà nhưng kỹ thuật viên chỉ gặp họ 1–3 tháng một lần — quãng giữa là một **hộp đen**. Em làm một **găng tay** có **khung cứng** với các **sensing element chế tạo từ vật liệu Velostat** trên vách khung; ngón tay ép vào vách nào thì hệ thống biết lực và **hướng** chuyển động của ngón đó, từ đó **dựng lại bàn tay 3D** và vẽ **đường cong chức năng tay theo tuần** để kỹ thuật viên theo dõi từ xa — không dùng IMU, chi phí thấp, dùng được tại nhà."

---

## 2. Vấn đề (problem-first)

- Sau đột quỵ, phục hồi chức năng phụ thuộc vào **luyện tập chủ động, lặp lại, kéo dài tại nhà**.
- Kỹ thuật viên VLTL-PHCN hướng dẫn trong giai đoạn đầu, sau đó bệnh nhân **tự tập không có giám sát trực tiếp**.
- Nếu quá trình này không được duy trì hoặc tập sai kỹ thuật mà không được phát hiện:
  - **Nhẹ:** co cứng, mỏi cơ cục bộ, đau, sưng viêm, chững lại không tiến triển.
  - **Nặng:** biến dạng khớp, co rút (contracture) khó hồi phục, chèn ép thần kinh ngoại vi.
- Công cụ đánh giá hiện có (FMA, ARAT, Box & Block Test, Jamar, E-Link) chỉ cho **một ảnh chụp tại thời điểm đo**, tại cơ sở y tế, chi phí cao → **không theo dõi được liên tục**.

## 3. Khoảng trống & bằng chứng

| Nguồn | Nội dung dùng cho đề tài |
|---|---|
| Amin K.R. et al., *IEEE OJEMB* (2024), DOI 10.1109/OJEMB.2024.3523442 | Hội đồng chuyên gia: công cụ đánh giá hiện tại hạn chế; theo dõi định lượng **giữa các lần tái khám** có ý nghĩa thay đổi cuộc sống và tiết kiệm chi phí; bài toán này là ví dụ điển hình cho nhiều lĩnh vực PHCN |
| OTHER study (2026), DOI 10.1080/09638288.2026.2643929 | Theo dõi hoạt động tại nhà + coaching từ xa cải thiện chức năng sinh hoạt và tự quản lý sau đột quỵ |
| Phỏng vấn KTVVLTL-PHCN (DEC-CLINICAL-001) | Xác nhận nguyên văn: giữa hai lần tái khám là **"hộp đen"**; thiết bị tại nhà chỉ hữu ích nếu chỉ số **có ý nghĩa lâm sàng + đủ tin cậy + bổ sung chứ không thay thế** đánh giá lâm sàng |
| Ý kiến chuyên gia PHCN độc lập thứ hai (DEC-CLINICAL-002, phcn-online.com) | "Đáng đặt chân và nghiên cứu" |
| Systematic review về AI smart glove (2026, 101 bài 2011–2025) | Phần lớn nguyên mẫu **chưa được kiểm chứng lâm sàng**; tồn tại drift, suy giảm tín hiệu theo thời gian, hiệu chỉnh lại, thiếu chuẩn dữ liệu, ergonomics, thời lượng pin |
| Wearable arm-use monitoring (PMC9901039, medRxiv 2023) | Cảm biến đeo cổ tay **không** ghi được chuyển động ngón và **không** phân biệt được vận động có mục đích |

**Khoảng trống:** chưa có hệ thống nào **vừa rẻ, vừa dùng tại nhà, vừa tạo ra dữ liệu định lượng chức năng bàn tay có ý nghĩa lâm sàng theo thời gian**, cho cả bệnh nhân không chuyên môn và kỹ thuật viên theo dõi từ xa.

---

## 4. Điểm mới (nói trung thực — theo đúng mức ViSEF)

| # | Thành phần | Mức mới | Ghi chú |
|---|---|---|---|
| 1 | **Cảm biến hướng qua vách khung cứng** — mã hóa hướng chuyển động của lóng ngón bằng áp lực lên vách khung, không dùng IMU/flex sensor | **Ứng viên chính (vật lý/cơ khí)** | Phải qua rà soát prior art + GATE A/B. Prior art gần nhất (Zhu lab IROS 2017; reconfigurable data glove 2023) dùng IMU để đo pose, Velostat chỉ đo lực tiếp xúc |
| 2 | **Cặp sensing element đối xứng (differential pair)** triệt thành phần drift/nhiệt đồng pha | Kỹ thuật — **KHÔNG mới** | Nguyên lý dummy-gauge/Wheatstone đã có từ lâu trong đo lường. Chỉ là execution tốt, phải trích dẫn prior art |
| 3 | **Theo dõi dọc tại nhà + tái tạo bàn tay 3D để chuyên gia xem từ xa** | Ứng dụng — khoảng trống được xác nhận | Không claim "hệ thống đầu tiên" khi chưa rà soát xong |
| 4 | **INT8 quantized trên NPU RK3588** | Triển khai kỹ thuật | Không mới về thuật toán |

**Câu định vị dùng khi bị hỏi "cái này có gì mới?":**

> "Cái mới không nằm ở chỗ 'găng tay + AI'. Cái mới nằm ở **cơ chế**: em đo **lực có hướng** qua vách khung cứng thay vì đo góc bằng IMU, nên hạ được chi phí mà vẫn dựng lại được bàn tay 3D; và em dùng chính cấu trúc đó để **tự phát hiện khi dữ liệu không còn đáng tin** trước khi đưa ra kết luận về tiến triển của bệnh nhân."

---

## 5. Câu hỏi nghiên cứu (RQ 2 tầng)

**RQ chính (quyết định đề tài sống/chết):**

> R1. Tín hiệu lực-hướng thu được từ mảng sensing element trên khung găng tay có **đủ ổn định và đủ nhạy** để phát hiện **thay đổi chức năng bàn tay thật** theo tuần, **vượt trên** biên độ drift/nhiễu của chính hệ thống đo — đồng thời **không tạo cảnh báo thay đổi giả** không?

**RQ phụ:**

> R2. Từ trường lực-hướng rời rạc đó có thể **suy luận hướng gập/duỗi của từng khớp ngón** và **tái tạo mô hình bàn tay 3D** đủ trung thực để chuyên gia đọc được không?
> R3. Các chỉ số trích xuất có **tương quan** với công cụ đánh giá lâm sàng chuẩn (Box & Block Test / lực kế / ARAT) ở mức đủ để dùng làm thông tin bổ sung không?

**Điều KHÔNG hỏi (và do đó không claim):** hệ thống không đo lực tuyệt đối, không đo góc khớp tuyệt đối, không đo hoạt động cơ, không chẩn đoán, không thay thế đánh giá lâm sàng.

---

## 6. Pipeline hệ thống

```
Bàn tay người dùng
   ↓ [bài tập chuẩn: gập / duỗi / cầm nắm / chạm ngón]
Khung găng in 3D + mảng sensing element (Velostat + copper tape)
   ↓ [ép vào vách khung → điện trở thay đổi]
CD74HC4067 (MUX 16 kênh ×1–2)
   ↓ [1 kênh analog, chọn MUX bằng chân EN]
ESP32-S3 (ADC1 12-bit + trung bình N mẫu)
   ↓ [frame + CRC → BLE/UART]
Orange Pi 5 Pro (RK3588)
   ├─ Bù ảnh hưởng drift (ô tham chiếu + cặp đối xứng)
   ├─ Trích đặc trưng → vector lực theo khớp
   ├─ Suy luận hướng gập/duỗi → tái tạo bàn tay 3D
   ├─ Mô hình INT8 (RKNN) trên NPU
   └─ Cảnh báo "dữ liệu không đáng tin" khi mất tính hợp lệ
   ↓
Đường cong chức năng theo tuần (digital trajectory)
   ↓
Dashboard → KTV / bác sĩ theo dõi từ xa → can thiệp sớm
```

---

## 7. Killer experiment (GATE)

Thí nghiệm này quyết định đề tài sống hay chết, và **phải chạy trên bench/phantom, không cần người tham gia**:

> **GATE C:** Với cùng một phantom, đo lặp qua nhiều phiên/ngày. Thay đổi tín hiệu khi **cố ý thay đổi mức chức năng mô phỏng** phải **lớn hơn có ý nghĩa thống kê** so với biến thiên drift/nhiễu của cùng hệ thống trong cùng khung thời gian.
> Nếu **không** → mọi kết luận longitudinal là vô nghĩa → dừng, báo thẳng, không viết báo cáo như thể thành công.

Chi tiết đầy đủ 6 cổng (GATE 0 → GATE E): [`research/protocols/06_glove_hand_GATE_experiment.md`](../research/protocols/06_glove_hand_GATE_experiment.md).

---

## 8. Phần cứng (chốt 2026-09-13 — xem `docs/04_Hardware_Architecture.md`)

| Thành phần | Lựa chọn | Lý do |
|---|---|---|
| Sensing element | Velostat + copper tape + cấu trúc sandwich, do tác giả chế tạo | Rẻ, mềm, làm được dạng dải trên vách khung |
| Khung | Găng in 3D (PLA/TPU) + khung cứng định vị từng lóng ngón | Tạo vách ép để lấy hướng |
| MUX | CD74HC4067 (16 kênh) × 1–2 | 12–24 kênh với 4–5 GPIO |
| ADC / MCU | **ESP32-S3** (ADC1 12-bit, 240 MHz, BLE 5, logic 3.3 V) | Thay Arduino Mega 2560 (10-bit, cồng kềnh, không wireless) |
| Edge | Orange Pi 5 Pro RK3588 (NPU ~6 TOPS) | Suy luận INT8 tại chỗ, không phụ thuộc mạng |
| Tham chiếu | Load cell + HX711 (bench) | Ground truth lực cho GATE |

---

## 9. Lộ trình

| Tầng | Nội dung | Điều kiện |
|---|---|---|
| 0 | Rà soát prior art + chốt bố trí kênh | hiện tại |
| 1 | Chế tạo sensing element + GATE 0 (repeatability) | có Velostat |
| 2 | GATE A/B (hướng + tái tạo 3D) trên phantom | sau tầng 1 |
| 3 | **GATE C** (sensitivity to change) — tiêu chí sống còn | sau tầng 2 |
| 4 | GATE D/E (longitudinal không báo giả, tự kiểm tra lỗi) | sau tầng 3 |
| 5 | Người khỏe tình nguyện (mô phỏng hạn chế) | **chỉ sau khi có IRB/SRC** |
| 6 | Pilot bệnh nhân | cần bệnh viện đối tác + IRB |

---

## 10. Sai lầm phải tránh (tự nhắc)

1. Biến đề tài thành **robot phục hồi chức năng** → sai hướng, sai an toàn, trùng đề tài khác.
2. Nói "thay thế Fugl-Meyer/ARAT" → sai và phản tác dụng với giám khảo y khoa.
3. Nói "đo chính xác lực/góc" khi chưa hiệu chuẩn → mất điểm trung thực.
4. Nói "loại bỏ drift" → sai về kỹ thuật; chỉ được nói "giảm ảnh hưởng drift".
5. Gọi "cảm biến Velostat" như thể Velostat là cái cảm biến → sai thuật ngữ (xem `GLOSSARY.md`).
6. Đưa số liệu chưa đo vào báo cáo → vi phạm `AGENTS.md`.
