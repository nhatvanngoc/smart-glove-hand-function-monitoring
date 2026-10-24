# 07 — Nhánh thị giác: kiến trúc nhận biết thìa/vùng đích và trạng thái tác vụ

> **Ngày lập:** 2026-10-19 · **Trạng thái:** `DRAFT — PROPOSED` (đặc tả thiết kế, **chưa có code, chưa benchmark**).
> **Vị trí trong pipeline:** Gate 3 của [`research/context/IMPLEMENTATION_PIPELINE.md`](../research/context/IMPLEMENTATION_PIPELINE.md); nhãn trạng thái lấy từ [`research/protocols/10_gate0_task_state_sheet.md`](../research/protocols/10_gate0_task_state_sheet.md) §3; ranh giới an toàn từ [`research/protocols/09_AAN_spool_phantom_and_conditional_volunteer.md`](../research/protocols/09_AAN_spool_phantom_and_conditional_volunteer.md).
> **Quyết định liên quan:** `DEC-REHAB-001`, `CLM-VISION-001`, `DEC-RL-001/002` (RL **không** thuộc phạm vi).
> **Quy tắc:** mọi con số về độ đúng, độ trễ, tốc độ khung, sai số tọa độ trong tài liệu này là ô `OPEN`. Không được trình bày đặc tả này như năng lực đã có của thiết bị.

---

## 1. Camera làm gì và không làm gì

**Camera làm:** xác định vị trí thìa và vùng đích trong cảnh cố định; theo dõi tiến trình nhìn thấy được của chu trình gắp–nhấc–di chuyển–đặt; gán nhãn kết quả (`T_SUCCESS`, `T_FAIL_DROP`, `T_FAIL_MISPLACE`, `T_UNKNOWN`); cung cấp phản hồi trực quan tức thời cho người tập.

**Camera không làm:** không đo lực ngón; không đọc ý định; không đánh giá phục hồi chức năng hay thay thế thang đo lâm sàng; **không** trực tiếp ra lệnh kéo dây không giới hạn. Giới hạn hành trình, dừng và nhả của actuator nằm ở tầng thấp (ESP32-S3/cơ khí), độc lập với suy luận thị giác.

Hệ quả thiết kế: nhánh thị giác được phép **gate pha tác vụ** và **gắn nhãn kết quả**, nhưng khi thị giác mất tin cậy thì hệ thống phải rơi về trạng thái an toàn đã định trước, không được "đoán rồi kéo".

---

## 2. Giả định cảnh (phải khai báo trong mọi log)

| Giả định | Trạng thái | Ghi chú |
|---|---|---|
| Camera cố định trên giá/đế, vị trí lặp lại được | đề xuất | nếu xê dịch giữa các phiên thì phải hiệu chuẩn lại |
| Một thìa duy nhất trong cảnh, đã khai báo đặc tính ở `protocols/10` §2.1 | đề xuất | nhiều vật thể = mở rộng tương lai |
| Vùng đích đánh dấu nhìn thấy được (khuôn in/marker/màu tương phản) | đề xuất | tiêu chí "trong vùng đích" định nghĩa bằng hình học |
| Nền và ánh sáng kiểm soát được một phần (trong nhà) | `[OPEN]` | phải ghi điều kiện ánh sáng mỗi phiên |
| Không có vật thể gây nhiễu cùng màu/mẫu với thìa | `[OPEN]` | kiểm tra bằng ảnh thử trước khi chạy |
| Góc nhìn thấy được cả vùng xuất phát và vùng đích, không bị tay che khuất toàn bộ | `[OPEN]` | chọn vị trí camera bằng ảnh thử, chụp lại làm bản ghi |

---

## 3. Kiến trúc: detector cắm được, logic tác vụ độc lập với detector

Nguyên tắc: **toàn bộ logic trạng thái tác vụ, hysteresis, xử lý `UNKNOWN` và log phải không phụ thuộc vào việc detector là gì.** Nhờ vậy có thể bắt đầu bằng OpenCV cổ điển (nhẹ, chạy được ngay trên Orange Pi 5 Pro, không cần NPU) và thay detector khác khi có căn cứ, mà không phải viết lại phần tác vụ hay phá vỡ so sánh giữa các phiên.

```text
Camera (V4L2/USB) ──> Frame capture + timestamp tại thời điểm bắt khung
                              │
                              ▼
                     Tiền xử lý (cân bằng sáng, khử nhiễu, mặt nạ vùng quan tâm)
                              │
                              ▼
        ┌──────────────────────────────────────────────┐
        │  DETECTOR (interface cắm được)               │
        │  ├─ ClassicCV  (mặc định, Gate 3 pha 1)      │
        │  ├─ MediaPipeHands (ứng viên, pha 2)         │
        │  ├─ YOLO/Deep model (ứng viên, pha 3)        │
        │  └─ DepthAnything (tuỳ chọn, chỉ khi cần 3D) │
        └──────────────────────────────────────────────┘
                              │  spoon_bbox/pose, target_polygon, confidence
                              ▼
                     Tracker (liên kết giữa các khung, xử lý mất vật thể)
                              │
                              ▼
        Task-state classifier (nhãn T_*, hysteresis, quy tắc UNKNOWN)
                              │
              ┌───────────────┴────────────────┐
              ▼                                ▼
   Phản hồi trực quan cho người tập     Log JSONL + gửi trạng thái sang ESP32-S3
```

### 3.1. Interface detector (đề xuất chữ ký, chưa code)

| Trường đầu ra | Ý nghĩa | Bắt buộc |
|---|---|---|
| `detector_name`, `detector_version`, `model_hash` | truy vết phiên bản | có |
| `spoon_present` (bool), `spoon_bbox`, `spoon_angle_deg` | vị trí/hướng thìa trong mặt phẳng ảnh | có |
| `spoon_confidence` | độ tin cậy [0–1] theo định nghĩa của detector | có |
| `target_polygon` (đã hiệu chuẩn), `target_present` | vùng đích | có |
| `occluded` (bool), `occlusion_reason` | che khuất / mất vật thể | có |
| `handle_point` | điểm cán thìa nơi ba ngón tiếp xúc (nếu suy được) | tuỳ chọn |
| `depth_mm` | chỉ có khi bật adapter độ sâu **và** đã hiệu chuẩn tỷ lệ | tuỳ chọn |

Mọi adapter phải trả về cùng schema; adapter không suy được trường nào thì để `null` kèm cờ, **không** được điền giá trị suy diễn.

### 3.2. Adapter mặc định — ClassicCV (OpenCV, không học sâu)

| Bước | Phương pháp đề xuất | Ngưỡng |
|---|---|---|
| Tách nền | ảnh nền tĩnh trừ khung hiện tại (static background / frame differencing) vì cảnh cố định | `OPEN` |
| Phân đoạn thìa | theo màu/vật liệu đã khai báo, hoặc theo marker thụ động nếu được duyệt | `OPEN` |
| Tách vùng đích | polygon hiệu chuẩn trước, hoặc marker in sẵn | `OPEN` |
| Ước lượng hình dạng | contour + `minAreaRect`/ellipse fit cho bầu thìa; trục cán bằng PCA trên contour | — |
| Chống nhiễu | lọc theo diện tích/tỷ lệ cạnh, bỏ ứng viên ngoài vùng làm việc | `OPEN` |
| Bám vật thể | liên kết bbox giữa các khung (dự đoán vị trí + khoảng cách) | `OPEN` |

Lý do chọn cổ điển trước: cảnh cố định, một vật thể đã biết, yêu cầu giải thích được từng bước cho hội đồng, và chi phí tính toán thấp trên RK3588. **Nếu** thử nghiệm cho thấy ánh sáng/nền trong nhà làm phương pháp cổ điển không ổn định, khi đó mới xét tới model học sâu; việc đổi adapter phải được ghi lại kèm lý do và dữ liệu so sánh, không đổi âm thầm.

### 3.3. Adapter ứng viên (chưa nhận vào phạm vi)

| Adapter | Khi nào cân nhắc | Ràng buộc |
|---|---|---|
| MediaPipe Hands | cần thông tin bàn tay/ngón để đối chiếu pha tiếp xúc | phải khai báo là theo dõi bàn tay, **không** suy ra lực; kiểm tra độ trễ/tải CPU |
| YOLO / model phát hiện vật thể | nền phức tạp, thìa không tách được bằng màu | phải ghim trọng số + phiên bản, báo cáo độ đúng trên tập nhãn thật của chính cảnh này |
| Depth Anything (độ sâu đơn ảnh) | **chỉ khi** tác vụ cần tọa độ metric 3D | tọa độ chưa hiệu chuẩn **không** được gọi là mm; phải có vật chuẩn tỷ lệ trong cảnh |
| RL / chính sách học tăng cường | — | **không** thuộc phạm vi đã chốt (`DEC-RL-001/002`) |
| Lượng tử hóa INT8 / suy luận NPU (RKNN) trên Orange Pi 5 Pro | — | **không** thuộc phạm vi (`DEC-EDGE-001`, 2026-10-20) |
| Thuật toán tự động gắn nhãn "Nghi vấn" | — | **đã loại bỏ** (`DEC-EDGE-001`); phiên đo lỗi xử lý bằng trạng thái `INVALID` + ghi lý do |

**Quyết định độ sâu (baseline đã nêu):** bắt đầu bằng tọa độ mặt phẳng ảnh 2D đã hiệu chuẩn; chỉ thêm độ sâu nếu bài tập thật sự cần. Trước khi gọi bất kỳ tọa độ nào là "metric", phải có bản ghi hiệu chuẩn camera + vật chuẩn tỷ lệ.

---

## 4. Từ đầu ra detector tới nhãn trạng thái tác vụ

Bảng ánh xạ dùng chung nhãn với `protocols/10` §3. Ngưỡng/hysteresis đều `OPEN`.

| Nhãn | Điều kiện đề xuất từ đầu ra thị giác | Cần thêm bằng chứng gì |
|---|---|---|
| `T_READY` | thìa trong vùng xuất phát **và** vùng đích nhìn thấy được | Flex ở mốc duỗi |
| `T_APPROACH` | bbox thìa ổn định, xuất hiện vùng tay tiến lại gần (nếu adapter tay bật) | — |
| `T_CONTACT` | chỉ gán nếu quan sát được trực tiếp; nếu không → `T_UNKNOWN` | Velostat/Flex (đối chiếu, không thay thế) |
| `T_GRASP` | thìa di chuyển cùng tay, không trượt khỏi bbox dự đoán | `OPEN` tiêu chí ổn định |
| `T_LIFT` | dịch chuyển theo trục "lên" trong ảnh vượt ⟨px/mm⟩ so với mốc | mốc tham chiếu tỷ lệ |
| `T_TRANSFER` | bbox nằm giữa vùng xuất phát và vùng đích | — |
| `T_PLACE` | thìa chạm bề mặt trong polygon đích, vận tốc ảnh ≈ 0 | `OPEN` tiêu chí đứng yên |
| `T_RELEASE` | thìa nằm yên trong vùng đích, không còn liên kết với tay | Flex/Velostat |
| `T_SUCCESS` | `PLACE_OK` theo `protocols/10` §2.4 | thời gian giữ `OPEN` |
| `T_FAIL_DROP` | mất vật thể ở pha `T_LIFT`/`T_TRANSFER` rồi tìm thấy ngoài vùng đích | — |
| `T_FAIL_MISPLACE` | thìa đứng yên ngoài polygon đích | — |
| `T_UNKNOWN` | `occluded` / `confidence` dưới ⟨mức⟩ / mất vật thể quá ⟨n⟩ khung | mặc định khi không đủ bằng chứng |
| `T_INVALID_SIGNAL` | nhánh thị giác không phải nguồn của nhãn này; nhãn này do acquisition phát | — |

**Quy tắc chống gán nhãn sai:**
1. Hysteresis bắt buộc cho mọi chuyển nhãn (chống nhấp nháy); giá trị `OPEN`.
2. `T_UNKNOWN` không được suy thành thất bại; phải đếm riêng và báo cáo tỷ lệ.
3. Một nhãn chỉ được gán khi **nguồn bằng chứng khai báo trước** có mặt; không "vá" nhãn bằng cảm tính của người vận hành.
4. Nhãn do thị giác sinh ra phải lưu kèm `confidence` và `detector_version` để đối chiếu hậu nghiệm.

---

## 5. Hiệu chuẩn camera và hệ tọa độ

| Bản ghi hiệu chuẩn | Nội dung | Trạng thái |
|---|---|---|
| Vị trí camera | tọa độ/độ cao/góc so với mặt bàn, ảnh chụp setup | `OPEN` |
| Nội tham số (nếu cần) | ma trận camera + hệ số méo, hoặc bỏ qua nếu dùng 2D ảnh phẳng | `OPEN` quyết định mức cần thiết |
| Vật chuẩn tỷ lệ | vật có kích thước đã biết đặt trong mặt phẳng thao tác | `OPEN` |
| Ánh xạ ảnh → mặt bàn | homography/đa thức bậc thấp từ ≥ 4 điểm chuẩn | `OPEN` |
| Polygon vùng đích | khai báo số, lưu trong config, băm phiên bản | `OPEN` |
| Kiểm tra lại | mỗi phiên chụp 1 ảnh chuẩn để so lệch vị trí | đề xuất |

Nếu không hiệu chuẩn: chỉ được nói "tọa độ trong ảnh (px)", không được nói "mm".

---

## 6. Phản hồi trực quan cho người tập

| Yêu cầu | Đề xuất | Trạng thái |
|---|---|---|
| Nội dung hiển thị | trạng thái tác vụ hiện tại, thành công/thử lại, tiến trình (vùng đích sáng lên khi đặt đúng) | `OPEN` thiết kế giao diện |
| Độ trễ cảm nhận | phải đo end-to-end (camera → xử lý → hiển thị) | `OPEN` — không hứa con số |
| Khả năng đọc | chữ/hình đủ lớn, tương phản cao, dùng được bởi người trung niên sau đột quỵ | `OPEN` — cần thử với người dùng thật **chỉ khi** đã có phê duyệt phù hợp |
| Thông điệp cấm | không hiển thị nội dung mang tính chẩn đoán, tiên lượng, đánh giá phục hồi | ràng buộc cố định |
| Khi `T_UNKNOWN` | hiển thị "chưa xác nhận — hãy thử lại", không hiển thị "thất bại" | đề xuất |

Phản hồi thị giác là **phản hồi tác vụ**. Nó không phải bằng chứng về tái tổ chức thần kinh hay cải thiện phục hồi.

---

## 7. Giao tiếp Orange Pi 5 Pro ↔ ESP32-S3 (đề xuất schema)

| Hạng mục | Đề xuất | Trạng thái |
|---|---|---|
| Vật lý | USB-serial (UART) cho pha bench; BLE/Wi-Fi chỉ xét sau khi đo nhiễu | `OPEN` |
| Định dạng | JSON Lines, một thông báo/trạng thái thay đổi | đề xuất |
| Trường | `schema_version, t_opi_ms, frame_id, task_state, confidence, occluded, detector_name, detector_version, bbox, target_inside` | đề xuất |
| Tần suất | chỉ gửi khi đổi nhãn + heartbeat định kỳ ⟨ms⟩ | `OPEN` |
| Watchdog | ESP32-S3 không nhận heartbeat quá ⟨n⟩ ms → coi thị giác mất tin cậy → trạng thái an toàn đã định trước | `OPEN` (giá trị) / cố định (nguyên tắc) |
| Quyền hạn | thị giác **không** có trường nào ra lệnh kéo servo; chỉ có `task_state`/pha | ràng buộc an toàn, không OPEN |
| Đồng hồ | `clock_offset_ms` giữa hai thiết bị phải được ước lượng và ghi mỗi phiên | `OPEN` phương pháp (xem `protocols/10a` §6) |

---

## 8. Kế hoạch benchmark trên Orange Pi 5 Pro

Không có con số nào dưới đây được điền trước. Bảng này là **phiếu ghi** để đo.

| Chỉ số | Cách đo | Giá trị mục tiêu | Kết quả đo |
|---|---|---|---|
| Tốc độ khung xử lý (fps) | đếm khung hoàn tất pipeline / thời gian | `OPEN` | chưa đo |
| Độ trễ end-to-end (camera → nhãn) | chênh timestamp bắt khung và timestamp phát nhãn | `OPEN` | chưa đo |
| Độ trễ phản hồi hiển thị | đo bằng video tốc độ cao hoặc sự kiện đồng bộ | `OPEN` | chưa đo |
| Độ đúng từng nhãn | tập ảnh/video đã gán nhãn thủ công → bảng nhầm lẫn | `OPEN` | chưa đo |
| Tỷ lệ `T_UNKNOWN` | đếm trên tập thử | `OPEN` | chưa đo |
| Ảnh hưởng che khuất | tập thử có che khuất chủ đích | `OPEN` | chưa đo |
| Tải CPU/NPU, nhiệt | đọc trong lúc chạy | `OPEN` | chưa đo |
| Sai số vị trí (px và mm sau hiệu chuẩn) | so với mốc thật đo bằng thước | `OPEN` | chưa đo |
| Độ ổn định giữa các phiên/điều kiện sáng | lặp lại cùng cảnh | `OPEN` | chưa đo |

**Yêu cầu phương pháp:**
- Tập thử phải là ảnh/video của **đúng cảnh thật** sẽ dùng, có nhãn thủ công độc lập; số lượng và cách chia tập hiệu chỉnh/tập đánh giá phải khai báo trước.
- Ghim phiên bản: `detector_name + detector_version + model_hash + config_version_hash + commit`. Đổi bất kỳ thành phần nào = phiên bản mới, không so sánh chéo như cùng một hệ.
- Tách dữ liệu dùng để chỉnh tham số khỏi dữ liệu dùng để báo cáo; không chọn ngưỡng sau khi xem kết quả đánh giá.
- Dữ liệu tổng hợp/mô phỏng phải gắn nhãn `SIMULATED`, không được trộn vào bảng kết quả thật.

---

## 9. Log và phiên bản

Mỗi phiên thị giác ghi: cấu hình cảnh, bản ghi hiệu chuẩn, `detector_version`, tập nhãn dùng để đánh giá, bảng nhầm lẫn, số khung, phân bố độ trễ, các sự kiện `T_UNKNOWN` kèm ảnh trích (không chứa thông tin định danh nếu có người trong khung hình — giai đoạn bench chỉ có phantom/fixture).

---

## 10. Thứ tự việc cần làm (sau khi đề cương được duyệt)

1. Chụp/quay cảnh thật với thìa và vùng đích đã chọn ở `protocols/10`; lưu làm bộ dữ liệu nền.
2. Chọn vị trí camera + vật chuẩn tỷ lệ; lập bản ghi hiệu chuẩn đầu tiên.
3. Viết adapter ClassicCV + tracker + classifier nhãn với mọi ngưỡng nằm trong file cấu hình có `OPEN`.
4. Gán nhãn thủ công một tập nhỏ; lập bảng nhầm lẫn đầu tiên (kết quả **của bản thử**, không phải cam kết).
5. Đo độ trễ/fps trên Orange Pi 5 Pro; ghi vào phiếu benchmark mục 8.
6. Chỉ khi số liệu cho thấy cổ điển không đủ ổn định → xét adapter học sâu, ghi lý do và so sánh.
7. Tích hợp schema mục 7 với ESP32-S3 (xem `docs/08`).

---

## 11. Tài liệu này không cho phép kết luận gì

- Chưa có pipeline thị giác nào được triển khai hoặc benchmark; Orange Pi 5 Pro là nền tảng **dự kiến**.
- Không có model, độ đúng, độ trễ, sai số độ sâu hay khả năng dùng tại nhà nào đã được xác nhận.
- Không suy ra hiệu quả phục hồi, chẩn đoán, an toàn được chứng nhận, novelty/"đầu tiên".
- Việc camera nhận biết được thìa trong điều kiện bench có kiểm soát **không** đồng nghĩa hoạt động được trong mọi ngôi nhà.
