# 10a — Gate 0: Bản đồ kênh 16 và ngân sách thu thập tín hiệu

> **Ngày lập:** 2026-10-19 · **Cập nhật:** 2026-10-20 · **Trạng thái:** `ADOPTED (PA-2)` — chủ dự án duyệt phương án **PA-2** và bản đồ kênh mục 3 (`DEC-CHMAP-001` ADOPTED 2026-10-20). **Gate 0 VẪN CHƯA đạt:** vị trí lắp từng cảm biến, dải điện trở Flex thật, điện trở phân áp, tốc độ khung/SPS/N thật (`DEC-ACQ-001`) và 8 câu hỏi phần cứng mục 7 đều còn `OPEN`. Artifact Gate 0 #2 theo [`IMPLEMENTATION_PIPELINE.md`](../context/IMPLEMENTATION_PIPELINE.md) §3.
> **Căn cứ:** `DEC-SENSE-001` (3 Flex sensor, mỗi ngón một chiếc; nếu dùng chung CD74HC4067 16:1 thì còn tối đa 13 kênh cho Velostat/tham chiếu), `DEC-HW-003/004`, `DEC-HW-006` (vòng lặp thiết kế 2: bỏ INA333, đọc trực tiếp PGA 16-bit ADS1115), [`docs/04_Hardware_Architecture.md`](../../docs/04_Hardware_Architecture.md), [`10_gate0_task_state_sheet.md`](10_gate0_task_state_sheet.md).
> **Nhãn bằng chứng dùng trong tài liệu:** `[CHỐT]` = quyết định đã có trong log · `[GHI NHẬN DỰ ÁN]` = số do nhóm ghi lại trong quá trình bring-up thật, **chưa** chính thức hoá thành log GATE hợp lệ (`DEC-PHASE-002`, `CLM-EVID-002`) · `[TÍNH TOÁN]` = phép tính của nhóm từ các số trên, phải đo lại · `[THIẾT KẾ]` = ngân sách trên giấy · `[OPEN]` = chưa chốt, cấm tự điền.

---

## 1. Ràng buộc đã chốt và hệ quả số học

| Ràng buộc | Nguồn | Giá trị |
|---|---|---|
| Số kênh analog mục tiêu | `[CHỐT]` `DEC-HW-004`, baseline 2026-10-19 | 16 kênh qua **một** CD74HC4067 |
| Số Flex sensor | `[CHỐT]` `DEC-SENSE-001` | 3 (cái / trỏ / giữa), mỗi ngón 1 |
| Kênh còn lại cho Velostat + tham chiếu nếu Flex đi chung MUX | `[TÍNH TOÁN]` 16 − 3 | **tối đa 13** — đây là trần số học, **không** phải số phần tử Velostat đã chốt |
| Số phần tử Velostat | `[OPEN]` | chưa chốt; phụ thuộc kết quả Gate 1 (tín hiệu là ngón–vật hay ngón–nẹp) |
| Số ngón tác vụ | `[CHỐT]` `DEC-SCOPE-005/008` | 3 (cái / trỏ / giữa) |
| Chuỗi đo Velostat hiện hành | `[GHI NHẬN DỰ ÁN]` `DEC-HW-006`, `docs/04` §9 | Velostat + điện trở kéo lên 10 kΩ → CD74HC4067 → PGA 16-bit ADS1115 (0,125 mV/LSB) → ESP32-S3 (DSP 4 bước) |
| Trễ chuyển kênh MUX | `[GHI NHẬN DỰ ÁN]` `docs/04` §9 | 300 µs + 1 lần đọc nháp để xả điện tích ký sinh |
| Tốc độ chuyển đổi ADS1115 đang dùng | `[GHI NHẬN DỰ ÁN]` `experiments/05` | 860 SPS, chế độ liên tục, ngắt ALRT → GPIO10 |

Nếu tổng số cảm biến cần đọc vượt 16 kênh: **phải sửa kiến trúc thu thập trước khi chế tạo găng đầy đủ** (baseline 2026-10-19), không được giả định có kênh phụ.

---

## 2. Bốn phương án phân bổ kênh

> **Kết quả duyệt 2026-10-20:** chủ dự án chọn **PA-2**. PA-1, PA-3a, PA-3b **không được chọn**. PA-3a chỉ còn là **kiểm tra phần cứng tuỳ chọn** (nếu board ADS1115 đưa `A1–A3` ra chân hàn thì có thể dời Flex sang đó để lấy lại 3 kênh MUX) — muốn áp dụng phải duyệt lại `DEC-CHMAP-001`. Bảng so sánh và khuyến nghị bên dưới được giữ nguyên để truy vết lý do chọn.

### PA-1 — Tối thiểu: Flex qua MUX, Velostat 1 phần tử/ngón

| Khối | Kênh dùng | Chi tiết |
|---|---|---|
| Flex | 3 | `FLEX_TH`, `FLEX_IDX`, `FLEX_MID` |
| Velostat | 3 | 1 phần tử/ngón ở mặt lòng (vị trí tiếp xúc cán thìa dự kiến) |
| Tham chiếu | 1 | ô không tải trên nẹp cổ tay |
| Dự phòng | 9 | để mở rộng |
| **Tổng đã dùng** | **7 / 16** | |

Ưu: ít dây, nhẹ, dễ làm gọn cụm đeo tay (mục tiêu 80–120 g). Nhược: **không** có cặp lòng/mu đối chiếu nên khó trả lời câu hỏi Gate 1 "tín hiệu là ngón–vật hay ngón–nẹp"; khó tách thành phần gập và duỗi.

### PA-2 — Velostat vi sai từng ngón (2 phần tử/ngón) — **ĐÃ DUYỆT 2026-10-20 làm cấu hình Gate 1**

| Khối | Kênh dùng | Chi tiết |
|---|---|---|
| Flex | 3 | `FLEX_TH`, `FLEX_IDX`, `FLEX_MID` |
| Velostat | 6 | 2/ngón: mặt lòng (palmar) + mặt mu (dorsal) |
| Tham chiếu | 2 | 2 ô không tải đặt cạnh nhau, kiểm tra chéo trôi |
| Dự phòng | 5 | — |
| **Tổng đã dùng** | **11 / 16** | |

Ưu: đúng yêu cầu Gate 1 của baseline — có cặp đối chiếu để phân biệt áp lực lên vật với lực ép vào nẹp; giữ được 5 kênh dự phòng cho hỏng hóc/thử vị trí mới. Nhược: nhiều dây và nhiều phần tử trên ngón hơn → khối lượng/độ cồng kềnh tăng, phải cân và ghi lại.

### PA-3a — Flex đọc thẳng vào ngõ vào còn trống của ADS1115 (biến thể nên kiểm tra trước)

ADS1115 có 4 ngõ vào đơn `A0…A3`. Chuỗi hiện hành của nhóm là **MUX → A0** `[GHI NHẬN DỰ ÁN]`, nghĩa là `A1–A3` có thể còn trống. Nếu đúng:

| Khối | Đường đọc | Chi tiết |
|---|---|---|
| Flex ×3 | ADS1115 `A1`, `A2`, `A3` (cầu phân áp riêng) | không chiếm kênh MUX, không dùng ADC1 nội của ESP32-S3 |
| Velostat | MUX `CH0…CH11` (12 phần tử) qua `A0` | tối đa 12 |
| Tham chiếu | MUX `CH12`, `CH13` | 2 ô không tải |
| Dự phòng | MUX `CH14`, `CH15` | — |

Ưu: Flex không chịu trễ/quét của MUX; tránh được nhược điểm phi tuyến của ADC1 nội ESP32-S3 đã ghi nhận ở `docs/04` §2; trần Velostat tăng từ 13 lên 12 **+** 3 Flex độc lập. Nhược / phải kiểm tra: `[OPEN]` board ADS1115 của nhóm có đưa `A1–A3` ra chân hàn hay không; `[OPEN]` dải điện áp cầu phân áp Flex có nằm trong thang PGA đang đặt hay không; `[OPEN]` thời gian ổn định khi ADS1115 chuyển giữa `A0` và `A1–A3` (MUX nội của chip cũng cần settling — đối chiếu datasheet, chưa tra trong phiên này).

### PA-3b — Flex vào ADC1 nội của ESP32-S3

Ưu: không cần chân ADS1115, rẻ. Nhược: ADC1 ESP32-S3 đã được chính nhóm ghi nhận là **phi tuyến ở hai biên và nhạy nhiễu RF** (`experiments/05`, `docs/04` §2) → bắt buộc hiệu chuẩn đường cong; Flex đo gập–duỗi nên cần độ ổn định dài hạn, đây là rủi ro. Chỉ nên chọn nếu PA-3a không khả thi về phần cứng.

### PA-4 — Vượt 16 kênh

Nếu Gate 1 cho thấy cần nhiều phần tử Velostat hơn trần của phương án đã chọn: thêm MUX/ADC thứ hai là **thay đổi kiến trúc thu thập**, phải duyệt lại trước khi chế tạo; không chắp vá sau khi đã làm găng.

### So sánh nhanh

| Tiêu chí | PA-1 | PA-2 | PA-3a | PA-3b |
|---|---|---|---|---|
| Trả lời được câu hỏi Gate 1 (ngón–vật vs ngón–nẹp) | yếu | **tốt** | tốt (nếu Velostat vẫn 2/ngón) | tốt |
| Rủi ro tuyến ADC Flex | MUX + ADS1115 (thấp) | MUX + ADS1115 (thấp) | ADS1115 (thấp) | ADC1 nội (**cao**) |
| Trần Velostat | 13 | 13 | 12 + 3 Flex riêng | 13 |
| Số kênh đã dùng (đề xuất) | 7 | 11 | 14 | 10 |
| Độ phức tạp đi dây / khối lượng cụm đeo | thấp | trung bình | trung bình | thấp |
| Phụ thuộc phần cứng chưa xác nhận | không | không | **có** (`A1–A3`) | không |

**Khuyến nghị của agent (chỉ là đề xuất, không phải quyết định):** dùng **PA-2 làm cấu hình làm việc cho Gate 1**, và kiểm tra PA-3a ngay trên board hiện có; nếu `A1–A3` hàn được thì chuyển Flex sang PA-3a để lấy lại 3 kênh MUX. Lý do: Gate 1 cần cặp lòng/mu để không diễn giải nhầm lực ép nẹp thành tương tác với vật; còn việc Flex đi đường nào là câu hỏi phần cứng có thể trả lời trong một buổi kiểm tra board. **2026-10-20: chủ dự án duyệt PA-2 → khuyến nghị này đã thành quyết định (`DEC-CHMAP-001` ADOPTED).** Việc kiểm tra PA-3a trên board vẫn nên làm như một cải tiến tuỳ chọn, nhưng không còn là điều kiện để đóng bản đồ kênh.

---

## 3. Bản đồ kênh (PA-2) — đã duyệt 2026-10-20; vị trí lắp còn `OPEN`

Bản máy đọc được: [`10b_channel_map_proposed.csv`](10b_channel_map_proposed.csv) — cột `status` đã đổi sang `ADOPTED_PA2_*` ngày 2026-10-20. Nhãn phiên bản bố trí (`layout_revision`) **chưa gán**: schema dữ liệu pha F0 (`docs/08`) sẽ định nghĩa trường này rồi mới cấp nhãn, để firmware và log dùng chung một chuỗi phiên bản.

| Kênh MUX | Vai trò tín hiệu | Ngón | Vị trí lắp đề xuất | Trạng thái |
|---|---|---|---|---|
| CH0 | `FLEX_TH` | cái | dọc đốt ngón cái, mặt mu, cố định không tì vào nếp gấp da | `[OPEN]` vị trí chính xác + phương pháp hiệu chuẩn |
| CH1 | `FLEX_IDX` | trỏ | dọc đốt 1–2 ngón trỏ, mặt mu | `[OPEN]` như trên |
| CH2 | `FLEX_MID` | giữa | dọc đốt 1–2 ngón giữa, mặt mu | `[OPEN]` như trên |
| CH3 | `VELO_TH_P` | cái | mặt lòng, vùng tiếp xúc cán thìa dự kiến | `[OPEN]` — Gate 1 quyết định giữ hay dời |
| CH4 | `VELO_TH_D` | cái | mặt mu đối diện CH3 | `[OPEN]` |
| CH5 | `VELO_IDX_P` | trỏ | mặt lòng đốt 1–2 | `[OPEN]` |
| CH6 | `VELO_IDX_D` | trỏ | mặt mu đối diện CH5 | `[OPEN]` |
| CH7 | `VELO_MID_P` | giữa | mặt lòng đốt 1–2 | `[OPEN]` |
| CH8 | `VELO_MID_D` | giữa | mặt mu đối diện CH7 | `[OPEN]` |
| CH9 | `REF_1` | — | trên nẹp cổ tay, không chịu tải người dùng | đề xuất |
| CH10 | `REF_2` | — | cạnh `REF_1`, kiểm tra chéo trôi | đề xuất |
| CH11 | `SPARE_1` | — | dự phòng / thử vị trí Velostat mới | đề xuất |
| CH12 | `SPARE_2` | — | dự phòng | đề xuất |
| CH13 | `SPARE_3` | — | dự phòng (ví dụ cảm biến nhiệt–ẩm nếu được duyệt lại) | đề xuất — xem `CLM-HW-004` về SHT30/AHT20 |
| CH14 | `SPARE_4` | — | dự phòng | đề xuất |
| CH15 | `SPARE_5` | — | dự phòng / kênh kiểm tra cross-talk (nối mass) | đề xuất |

Quy ước đặt tên: `<LOẠI>_<NGÓN>_<MẶT>`; `P` = palmar (lòng), `D` = dorsal (mu). Tên kênh phải cố định trong firmware và trong log; đổi tên là đổi `layout_revision`.

---

## 4. Điểm lắp và phương pháp hiệu chuẩn từng cảm biến

| Cảm biến | Đại lượng muốn suy ra | Không được suy ra | Phương pháp tham chiếu đề xuất | Trạng thái |
|---|---|---|---|---|
| Flex ×3 | biến thiên gập–duỗi / tư thế, tiến triển chuyển động, độ lặp lại chu kỳ | góc giải phẫu chính xác, lực | cần chọn **một** phương pháp độc lập: thước góc cơ khí đặt trên fixture, ảnh chụp có mốc góc đã hiệu chuẩn, hoặc inclinometer; phải khai báo sai số phương pháp | `[OPEN]` — baseline ghi rõ GAP/chỉ số góc chưa cam kết tới khi chọn và xác nhận phương pháp |
| Velostat (cặp lòng/mu) | biến thiên áp lực/tiếp xúc tương đối, bằng chứng nỗ lực/tương tác | Newton, ý định, góc | tải tham chiếu độc lập (cân tải/load cell đã hiệu chuẩn) **chỉ để đặc trưng hoá trên bench**, không dùng để quy đổi tín hiệu găng thành lực | `[OPEN]` thiết bị + quy trình; `docs/02` §7.3 và `CLM-HW-005` ghi nhận sai số 16–48% toàn thang của Velostat trong y văn |
| `REF_1/REF_2` | trôi hệ thống (nhiệt độ, nguồn, dão nhựa) | tín hiệu người dùng | so lệch tĩnh giữa hai ô theo thời gian | đề xuất |

Yêu cầu bắt buộc khi lắp (từ `docs/06` §1.3): Velostat cần **preload xác định và ổn định**; preload thay đổi theo nấc kẹp sẽ làm dịch điểm làm việc, nên mỗi phiên phải ghi lại nấc kẹp/preload như một phần `layout_revision`.

---

## 5. Ngân sách thời gian quét

Công thức (một vòng quét toàn bộ kênh đang bật):

```text
T_frame = Σ_kênh ( t_settle + t_dummy + t_conv )
f_frame = 1 / T_frame
t_conv  = 1 / SPS_ADS1115
```

Trong đó `t_settle = 300 µs` và `t_dummy = 1 lần chuyển đổi` là `[GHI NHẬN DỰ ÁN]` (`docs/04` §9, `experiments/07`); `SPS = 860` là `[GHI NHẬN DỰ ÁN]` (`experiments/05`).

**`[TÍNH TOÁN]` — ví dụ số, KHÔNG phải kết quả đo của cấu hình cuối; phải đo lại và ghi vào log:**

| Số kênh đọc | Có đọc nháp mỗi kênh | Không đọc nháp |
|---|---|---|
| 7 (PA-1) | ≈ 18,4 ms → **≈ 54 Hz** | ≈ 10,2 ms → ≈ 98 Hz |
| 11 (PA-2) | ≈ 28,9 ms → **≈ 35 Hz** | ≈ 16,0 ms → ≈ 62 Hz |
| 14 (PA-3a) | ≈ 36,8 ms → **≈ 27 Hz** | ≈ 20,4 ms → ≈ 49 Hz |
| 16 (trần) | ≈ 42,0 ms → **≈ 24 Hz** | ≈ 23,4 ms → ≈ 43 Hz |

*(Cơ số: 300 µs + 2 × 1/860 s = 2,63 ms/kênh khi có đọc nháp; 300 µs + 1/860 s = 1,46 ms/kênh khi không.)*

**Hệ quả phải nói thẳng:** bảng ngân sách tốc độ khung cũ ở `docs/04` §5 (12 kênh → ~415 Hz) giả định **ADC nội ESP32-S3 với 200 µs/kênh**, nên **không áp dụng** cho chuỗi ADS1115 + đọc nháp hiện hành. Với chuỗi 16-bit, tốc độ khung thực tế nằm ở mức vài chục Hz. Điều này vẫn cao hơn nhu cầu tối thiểu đã ghi nhận cho động tác phục hồi chức năng 0,5–2 Hz (`docs/04` §5 nêu ≥ 20–50 Hz là đủ bắt dạng sóng), nhưng **thấp hơn mục tiêu thiết kế 45–100 Hz** từng ghi cho cấu hình cũ → phải chọn lại mục tiêu tốc độ khung cho cấu hình hiện hành, hoặc đổi SPS/đổi cách đọc.

| Hạng mục cần chốt | Trạng thái | Ghi chú |
|---|---|---|
| Tốc độ khung mục tiêu của cấu hình hiện hành | `[OPEN]` | phải tương thích với tốc độ camera và chu kỳ tác vụ |
| SPS ADS1115 (đánh đổi nhiễu ↔ tốc độ) | `[OPEN]` | 860 SPS đang dùng; giảm SPS giảm nhiễu nhưng giảm `f_frame` |
| Số mẫu trung bình N trên mỗi kênh | `[OPEN]` | `docs/04` §4.2: nhiễu ngẫu nhiên giảm theo √N `[THIẾT KẾ]` |
| Có cần đọc nháp mỗi kênh hay chỉ khi đổi nhóm kênh | `[OPEN]` | phải đo cross-talk thực tế trên cấu hình cuối |
| Trễ end-to-end cảm biến → quyết định → servo | `[OPEN]` | phải đo, không suy từ datasheet |

---

## 6. Đồng bộ thời gian giữa cảm biến, camera và servo

| Vấn đề | Đề xuất | Trạng thái |
|---|---|---|
| Đồng hồ chung | ESP32-S3 là time master cho luồng cảm biến; mỗi khung quét có `frame_id` + `t_ms` đơn điệu | đề xuất |
| Lệch đồng hồ Orange Pi ↔ ESP32-S3 | ước lượng offset bằng sự kiện chung (ping–pong serial hoặc đèn LED nhấp nháy nhìn thấy ở cả camera và log) và ghi `clock_offset_ms` mỗi phiên | `[OPEN]` phương pháp + giá trị phải đo |
| Timestamp camera | lấy tại thời điểm bắt khung hình, không phải thời điểm xử lý xong | đề xuất |
| Lệnh servo | ghi `t_cmd_ms` và phản hồi vị trí/dòng (nếu đo được) cùng khung thời gian | đề xuất |
| Mất khung / trễ | nếu quá ⟨n⟩ khung liên tiếp không có nhãn tác vụ → `T_UNKNOWN` và cân nhắc `FAULT` theo quy tắc đã khóa | `[OPEN]` |
| Ghi log | một file JSONL/CSV duy nhất cho phiên, mọi nguồn có trường `clock_source` | đề xuất |

---

## 7. Câu hỏi kỹ thuật phải kiểm tra trước khi cấp nguồn (không phải tuyên bố lỗi)

Đây là các điểm agent phát hiện khi rà tài liệu, **chưa được kiểm chứng bằng đo đạc trong phiên này**; cần nhóm kiểm tra trên board thật và ghi lại:

1. `[OPEN]` **Giới hạn điện áp đầu vào tuyệt đối của ADS1115.** Ghi nhận dự án nói chuỗi đo đọc "toàn dải 0,000 V – 3,300 V" với PGA đặt 0,125 mV/LSB. Cần đối chiếu datasheet (giới hạn đầu vào theo `VDD`, thang PGA, và cách bảo vệ nếu đầu vào chạm 3,3 V) và ghi lại `SRC-ID`. Không kết luận "mạch sai" khi chưa tra datasheet và chưa đo.
2. `[OPEN]` **`A1–A3` của ADS1115 có sẵn trên board không** (quyết định PA-3a).
3. `[OPEN]` **Điện trở kéo lên cho Flex.** Ghi nhận dự án dùng 10 kΩ cho Velostat. Flex có dải điện trở khác; phải **đo dải điện trở Flex thật** trước khi chọn điện trở phân áp, không lấy giá trị datasheet thay phép đo (tương tự quy tắc chọn `R_f` ở `docs/04` §4.1).
4. `[OPEN]` **Cross-talk giữa kênh Flex và kênh Velostat** khi dùng chung MUX: Flex có thể có trở kháng cao hơn nhiều → kiểm tra bằng kênh `SPARE_5` nối mass và đo bóng ma.
5. `[OPEN]` **Vòng mass / ground loop.** `experiments/05` ghi nhận sự cố sập nguồn khi kẹp mass oscilloscope do vỏ BNC thông ngầm. Phải có quy tắc nối mass khi đo chung camera + servo + mạch analog.
6. `[OPEN]` **Nguồn cho servo** tách khỏi nguồn mạch analog như thế nào (nhiễu đóng cắt servo có thể phá tín hiệu Velostat) — ghi sơ đồ nguồn và đo nhiễu nền khi servo chạy/không chạy.
7. `[OPEN]` **Hành vi khi mất nguồn/mất điều khiển:** dây có tự nhả không; cơ cấu nhả không được chỉ dựa vào phần mềm (`protocols/09` §3.2).
8. `[OPEN]` **Ảnh hưởng của Wi-Fi/BLE lên chuỗi đo** (`docs/04` §2 khuyến cáo tránh Wi-Fi khi đo; ưu tiên BLE hoặc USB khi ghi log).

---

## 8. Khối lượng và nguồn cho cụm đeo tay

| Hạng mục | Giá trị | Trạng thái |
|---|---|---|
| Mục tiêu khối lượng cụm đeo tay (nẹp + cảm biến + dây) | 80–120 g | `[CHỐT]` là **mục tiêu**, chưa cân (`DEC-MASS-001`) |
| Khối lượng thực tế sau chế tạo | — | `[OPEN]` phải cân và ghi ngày |
| Vị trí đặt bộ xử lý / pin / servo | ngoài tay | `[CHỐT]` hướng; vị trí cụ thể `[OPEN]` |
| Ước tính vật tư cụm đeo | 1,0–1,3 triệu VNĐ | `[CHỐT]` là **dự toán**, cần BOM có ngày + báo giá (`DEC-COST-002`) |
| Ước tính hệ thống/giàn thử E2E | ~5,5 triệu VNĐ khi tận dụng thiết bị lab | `[CHỐT]` là **dự toán** |

PA-2 dùng nhiều phần tử Velostat hơn PA-1 → phải ghi nhận đánh đổi khối lượng/đi dây khi chọn phương án.

---

## 9. Việc phải làm để đóng Gate 0

**1. ~~Chủ dự án duyệt một phương án phân bổ kênh~~ — ĐÃ XONG 2026-10-20:** chủ dự án duyệt **PA-2** + bản đồ kênh mục 3 → `DEC-CHMAP-001` **ADOPTED**.
2. Kiểm tra 8 câu hỏi kỹ thuật mục 7 trên board thật; ghi kết quả vào sổ tay, kèm ảnh.
3. Đo dải điện trở Flex thật và chọn điện trở phân áp → ghi `[GHI NHẬN DỰ ÁN]` kèm ngày.
4. Chốt tốc độ khung mục tiêu + SPS + N (mục 5) → tạo `DEC-ACQ-001`.
5. Chọn phương pháp tham chiếu cho Flex (mục 4) → liên quan chỉ số góc/GAP còn mở ở baseline.
6. ~~Cập nhật `10b_channel_map_proposed.csv` thành bản đã duyệt, đổi `status` từng dòng~~ — **ĐÃ LÀM 2026-10-20** (xem mục 3); phần **ghi `layout_revision` còn nợ**, sẽ cấp khi schema F0 định nghĩa trường này.

**Việc 1 đã xong (2026-10-20); chưa làm xong 5 việc còn lại thì chưa được coi Gate 0 là đạt**, và chưa nên viết firmware đầy đủ (xem `docs/08` về thứ tự code).
