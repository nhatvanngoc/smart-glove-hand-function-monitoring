# NGHIÊN CỨU VÀ PHÁT TRIỂN GĂNG TAY HỖ TRỢ ĐÁNH GIÁ, THEO DÕI VÀ HỖ TRỢ VẬN ĐỘNG BÀN TAY TRONG PHỤC HỒI CHỨC NĂNG SAU ĐỘT QUỴ

> **Học sinh:** Văn Ngọc Nhật Anh (11A2) + Nguyễn Duy Quân (12A1) · **GVHD:** Lê Công Long · **Trường:** THPT Quảng Trị, Quảng Trị
> **Trạng thái hồ sơ (cập nhật 2026-10-11, `DEC-PHASE-002`):** cơ sở lý thuyết & thiết kế **đã hoàn tất**; nhóm nghiên cứu **đã tự thực hiện** thử nghiệm bring-up phần cứng thật trên breadboard (ESP32-S3+ADS1115+INA333+CD74HC4067, log ở [`research/notebooklm_sync/experiments/`](research/notebooklm_sync/experiments/)) — **chưa đạt chuẩn GATE 0 chính thức** (thiếu schema `protocols/08a`), nên **vẫn chưa có số liệu GATE 0 đưa vào `research/bench/logs/`**.
> **Bản đã nộp trường:** [`docs/DE_CUONG.pdf`](docs/DE_CUONG.pdf) (15 trang, 2026-09-26) · **Bản đề cương mới nhất (chưa rõ đã nộp lại hay chưa — `DEC-SYNC-002`, chờ xác nhận):** [`de_cuong/DE_CUONG_NGHIEN_CUU.pdf`](de_cuong/DE_CUONG_NGHIEN_CUU.pdf) (16 trang, 2026-10-03) — bổ sung Mục 10 (cơ cấu **AAN** trên giàn đo + mô hình tay giả, nay là trụ cột thứ 4, `DEC-SCOPE-006`).
> **Tên hiển thị ở trên = `DEC-TITLE-003` (ADOPTED 2026-10-11, nhóm nghiên cứu chốt "Hướng A": giữ nguyên nội dung đề xuất, không thêm chữ).** **Tên đã nộp trường (`DEC-TOPIC-019`, 2026-09-13) vẫn là:** *"Nghiên cứu và phát triển găng tay **thông minh** hỗ trợ đánh giá **và** theo dõi chức năng vận động bàn tay trong phục hồi chức năng sau đột quỵ"* — dùng trong `docs/DE_CUONG.pdf` (26/09) và `de_cuong/DE_CUONG_NGHIEN_CUU.pdf` (03/10); **2 tên khác nhau ở chỗ: bỏ "thông minh", và đổi "...đánh giá và theo dõi chức năng vận động..." → "...đánh giá, theo dõi và hỗ trợ vận động..." để phản ánh AAN là trụ cột thứ 4 (`DEC-SCOPE-006`).** Tên mới **chỉ áp dụng cho các tài liệu repo từ nay**; hồ sơ đã nộp **không** bị sửa hồi tố — khi nộp lại/nộp bản mới mới dùng tên `DEC-TITLE-003`. (Tên đề xuất 2026-09-19 `DEC-TITLE-001` **chưa từng được duyệt**, đã hạ thành `DEC-TITLE-002` chờ hủy — không liên quan tới `DEC-TITLE-003`.)

**Tên tiếng Anh (hồ sơ ISEF/ViSEF bản dịch, cập nhật theo `DEC-TITLE-003`):**

> *A glove with directional piezoresistive sensing for quantitative hand motor-function assessment, longitudinal monitoring, and assist-as-needed movement support (bench/phantom-verified) in post-stroke rehabilitation*

**Phụ đề kỹ thuật (dùng ở đầu báo cáo, không nằm trong tên):**

> *Găng tay đo lực ép bên trên khung cứng + tầm vận động chủ động/thụ động từng ngón, kèm ngưỡng tin cậy đăng ký trước khi đo.*

**Lĩnh vực dự thi (đã nộp):** Hệ thống nhúng (Embedded Systems) · **Thời gian:** 09/2026–01/2027 · **Địa điểm:** phòng sáng tạo trường + nhà riêng · chờ `DEC-TEAM-001` phê chuẩn vào log.

**Câu nói với giám khảo (12 giây):**

> Một găng tay đo **lực ép theo hướng** ở từng ngón, chạy tại nhà, kèm **bộ tiêu chí khiến mỗi con số tự nói được nó có đáng tin hay không** — để khoảng trống giữa hai lần tái khám không còn là hộp đen.

---

## Mục lục

[1. Luận điểm của đề tài](#1-luận-điểm-của-đề-tài) ·
[2. Vấn đề, có số](#2-vấn-đề-có-số) ·
[3. Câu hỏi nghiên cứu và điều kiện giết](#3-câu-hỏi-nghiên-cứu-và-điều-kiện-giết) ·
[4. Nguyên lý hoạt động](#4-nguyên-lý-hoạt-động) ·
[5. Ba đại lượng dẫn xuất và quy tắc đơn vị](#5-ba-đại-lượng-dẫn-xuất-và-quy-tắc-đơn-vị) ·
[6. Phương pháp: bộ kiểm chứng 10 ngưỡng](#6-phương-pháp-bộ-kiểm-chứng-10-ngưỡng) ·
[6.1 Cơ cấu AAN — trụ cột thứ 4](#61-cơ-cấu-hỗ-trợ-theo-nhu-cầu-aan--trụ-cột-thứ-4-dec-scope-006-nguồn-de_cuongde_cuong_nghien_cuupdf-10) ·
[7. Kế hoạch và ngân sách](#7-kế-hoạch-và-ngân-sách) ·
[8. Tính mới — và bộ tiêu chí đang dùng để tự chấm](#8-tính-mới--và-bộ-tiêu-chí-đang-dùng-để-tự-chấm) ·
[9. Giới hạn tự khai](#9-giới-hạn-tự-khai) ·
[10. Bằng chứng của chính hồ sơ này](#10-bằng-chứng-của-chính-hồ-sơ-này) ·
[11. Bản đồ repo](#11-bản-đồ-repo) ·
[12. Thiết lập & quy trình](#12-thiết-lập--quy-trình) ·
[13. Metadata repo GitHub](#13-metadata-repo-github)

---

## 1. Luận điểm của đề tài

Đề tài **không** tuyên bố một nguyên lý vật lý mới và **không** bán một nguyên mẫu. Nó tuyên bố bốn thứ (cập nhật `DEC-SCOPE-006`, 2026-10-11 — mục 4 mới được nâng thành trụ cột chính thức), theo thứ tự bảo vệ được giảm dần:

1. **Một kiến trúc cơ khí** — mảng áp trở đặt trên **vách cứng** của ốp ngón, cấu hình cầu vi sai hai vách (bản nộp: `R_ref = 10 kΩ` → INA333 G=10 → ADS1115 16-bit), để đo riêng **thành phần lực ép bên**: đại lượng tăng khi người bệnh chống lại tầm vận động, tức là thứ mà cảm biến gập góc *về bản chất* không phân biệt được.
2. **Một thiết kế phép đo** — `AROM` rồi `PROM` trên cùng ngón, cùng phiên, ở **hai tốc độ kéo** (vì phản ứng căng cơ phụ thuộc tốc độ). `GAP = PROM − AROM` (bản nộp 2026-09-26; README cũ ghi ngược dấu) chính là phép thử phân tách *"chưa cố"* khỏi *"bị giữ lại"*.
3. **Một lớp tự kiểm chứng** — ngưỡng `MDC`/`ICC`/`CV`/trôi **đăng ký trước khi đo**, mỗi phiên mang cờ `UNRELIABLE` khi vượt ngưỡng, và **lỗi được tiêm có chủ đích** trên rig để chứng minh cờ đó không phải đồ trang trí.
4. **Một cơ cấu hỗ trợ theo nhu cầu (AAN)** — kiểm chứng **chỉ trên giàn đo cơ khí + mô hình tay giả silicone (phantom)**, **không bao giờ** trên ngón tay người thật: lò xo trợ giúp chia nấc + 1 servo qua khớp 4 khâu dưới dẫn động, bù đúng phần lực thiếu theo nguyên tắc can thiệp tối thiểu (`F_assist = max(0, F_target − F_phantom)`, `F_max ≤ 5 N`), dùng để tạo ra chỉ số `RAL` và chứng minh năng lực kỹ thuật tái tạo một vòng điều khiển thích ứng — xem §6.1.

> **Câu chốt cho hội đồng:** phần (1) đã có tiền lệ ở tầng phần tử cảm biến, phần (2) là lựa chọn phương pháp luận, **phần (3) là phần đề tài này mạnh hơn cả một số công trình đã công bố** — và cũng là phần rẻ nhất để làm đúng; **phần (4) không làm thiết bị thành "robot tập phục hồi"**, vì nó không bao giờ chạm vào người dùng cuối — nó là bằng chứng năng lực kỹ thuật + nguồn tạo chỉ số `RAL`.

> **Tên đề tài (`DEC-TITLE-003` — ĐÃ CHỐT 2026-10-11, Hướng A):** nhóm nghiên cứu chọn giữ nguyên nội dung đề xuất gốc, không thêm chữ an toàn bổ sung: *"Nghiên cứu và phát triển găng tay hỗ trợ đánh giá, theo dõi và hỗ trợ vận động bàn tay trong phục hồi chức năng sau đột quỵ"* (xem đầu README). Vì cụm "hỗ trợ vận động" trong tên không tự nêu rõ "chỉ trên giàn đo + mô hình tay giả", **mọi nơi dùng tên này phải đi kèm hoặc đặt ngay sau câu giới hạn phạm vi** (ví dụ §6.1 bên dưới, hoặc dòng đầu phần tóm tắt báo cáo) để tránh hiểu nhầm là thiết bị tác động lực lên người bệnh thật.

## 2. Vấn đề, có số

| Đại lượng | Giá trị | Nguồn (đã kiểm) |
|---|---|---|
| Đột quỵ ở Việt Nam — hiện mắc | **1.541**/100.000 (95% UI 1.431–1.679) | *Global Epidemiology* 2025;9:100199 · [DOI](https://doi.org/10.1016/j.gloepi.2025.100199) |
| Mới mắc / tử vong | **222**/100.000/năm · **135.999** ca tử vong (dẫn đầu nhóm tim mạch) | như trên |
| Tổn thương vận động chi trên, giai đoạn sớm | **~80%** | Cochrane 2014 CD010820 (trích Langhorne 2009) · [DOI](https://doi.org/10.1002/14651858.CD010820.pub2) |
| Liệt chi trên hoàn toàn lấy lại chức năng hữu ích sau 6 tháng | **~50%** | như trên (trích Kwakkel 2003) |
| Còn vấn đề tay sau **4 năm** | **~50%** | như trên (trích Broeks 1999) |
| Độ tin cậy của việc **người bệnh tự đếm số lần tập** | `MDC ≈ 31 %`; đếm nhầm **100–200 lần/giờ** | *Sensors* 2022;22(18):6938 · [DOI](https://doi.org/10.3390/s22186938) |
| Giá hệ thống PHCN bàn tay tại nhà đã FDA chấp thuận | **350–6.000 USD** | *Device* (Cell Press) 2024 |

**Suy ra vấn đề:** di chứng bàn tay kéo dài **nhiều tháng đến nhiều năm**, trong khi nhịp đánh giá lâm sàng là **1–3 tháng**; và cách thay thế đang dùng (tự báo cáo) **đã được đo là không đủ tin cậy để làm đơn vị phân tích**. Khoảng giữa hai lần tái khám là một hộp đen — không biết có tập không, tập đúng hay sai, tiến bộ hay chững.

*(Con số "cỡ 1,5 triệu người đang sống sau đột quỵ ở Việt Nam" là **phép nhân của đề tài** từ tỉ lệ hiện mắc × dân số, không phải số in trong bài báo — nêu rõ như vậy ở mọi chỗ dùng nó.)*

> **Vì sao đặc biệt là bàn tay (`CLM-BIO-005`, 2026-10-11):** bản đồ vỏ não vận động/cảm giác (*motor/sensory homunculus* — Penfield & Boldrey, *Brain* 1937;60:389–443) cho thấy diện tích vỏ não dành cho bàn tay và ngón tay lớn hơn nhiều so với tỉ lệ diện tích cơ thể, phản ánh mức điều khiển tinh vi cần cho cầm nắm khéo léo; mô hình hiện đại hơn (Gordon et al., *Nature* 2023;617:351–359, DOI `10.1038/s41586-023-05964-2`) tinh chỉnh cách tổ chức vỏ não vận động (mạng SCAN) nhưng **không đổi** kết luận cốt lõi đó. Đây là **cơ sở lý thuyết giải thích vì sao chọn bàn tay làm đối tượng**, **không phải** điều đề tài đo hay chứng minh (đề tài không đo EEG/fNIRS/TMS/fMRI) — chi tiết + rào chắn claim: `docs/02_Theoretical_Foundation.md` §1.1b.

## 3. Câu hỏi nghiên cứu và điều kiện giết

**RQ chính** (quyết định đề tài sống/chết):

> **R1.** Đáp ứng lực–hướng từ mảng áp trở trên vách khung có **đủ nhạy và đủ ổn định** để phát hiện thay đổi chức năng bàn tay theo tuần — **vượt trên** biên độ nhiễu/trôi của chính hệ thống đo — và **không** sinh ra cảnh báo tiến triển giả?

**RQ phụ:**

> **R2.** Dấu hiệu gập/duỗi có suy ra được **chỉ từ mẫu đáp ứng trên vách**, không cần encoder, và kết hợp được với góc IMU để tái tạo tư thế bàn tay đủ trung thực cho chuyên gia đọc?
> **R3.** Các chỉ số trích xuất có **đồng biến** với công cụ chuẩn (Box & Block / ARAT / lực kế cầm tay) ở mức đủ để dùng làm thông tin bổ sung giữa hai lần tái khám?

| RQ | Cửa quyết định | Nếu fail thì sao |
|---|---|---|
| R1 | **`GATE 0`** (bản nộp: `C1.2` + `C1.8` là hai ô giết, tương ứng `G0.1` + `G0.7` cũ) | Không có chuỗi số liệu nào để nói về diễn tiến → đề tài đổi thành **báo cáo phương pháp + kết quả âm tính** (vẫn nộp được, vẫn có giá trị) |
| R1 | **`GATE C`** (trôi 28 ngày, nhiệt–ẩm, tháo/lắp) | Dừng đề tài theo đúng nghĩa đã ghi trong `research/protocols/06` |
| R2 | `GATE A`/`GATE B` trên ≥ 1 ngón | Bỏ tái tạo 3D, giữ `GAP`/`EI` |
| R3 | **Chỉ sau IRB** — nằm ngoài phạm vi đề cương này | Không nêu giả thuyết R3 như kết quả; chỉ là thiết kế dự phòng |

**Điều đề tài không hỏi, và do đó không được claim:** không đo lực tuyệt đối trên ngón, không đo góc khớp tuyệt đối từ ADC, không đo hoạt động cơ, không chẩn đoán, không thay thế đánh giá lâm sàng, không cam kết hiệu quả phục hồi.

## 4. Nguyên lý hoạt động

```
Co cơ / bị duỗi thụ động ──► ngón ép vào VÁCH CỨNG của ốp ngón
   ► áp suất tiếp xúc p = F/A_c nén mảng Velostat
   ► ΔR/R = γ · Δp/p₀                       (γ = độ nhạy áp trở, p₀ = F_p/A_c)
   ► cầu vi sai hai vách: d = S(lòng) − S(mu), R_ref = 10 kΩ (bản nộp)
   ► INA333 G=10 ──► mux CD74HC4067 ──► ADS1115 16-bit (62,5 µV/LSB)
   ► ESP32-S3: IIR fc=10 Hz + Notch 50 Hz ──► BLE ──► Orange Pi 5 Pro
   ► auto-zero 3 s + ô tham chiếu + nhãn "Nghi vấn" (2 vòng lặp kín)
   ► EI · GAP · RAL          (KHÔNG phải newton, KHÔNG phải độ suy từ ADC)
```

**Hai kết quả rút ra từ mô hình, và cả hai đều kiểm chứng được bằng tay** (`docs/02` §5.5, `CLM-MET-003`):

1. `A_c` **triệt tiêu ở bậc nhất** ⇒ kích thước mảng **không** phải vấn đề tỉ số tín hiệu/nhiễu; nó là vấn đề cơ khí (áp suất phân bố lại, độ lặp lại khi tháo/lắp). ⇒ Không cần mua mảng to hơn.
2. Thiết kế chỉ sống trong một **cửa sổ tiền tải `F_p` chặn hai phía**: dưới thì không đủ nhạy — với `n_eff ≈ 11`, `V_EX = 3,1 V`, `LSB = 1,51 mV` và `ΔV ≥ 8 LSB` tại `ΔF = 1 N` thì `F_p ≤ 68·γ·ΔF` (γ = 0,5 ⇒ `F_p ≲ 34 N`); trên thì điện trở nguồn cao làm **mux không kịp ổn định ở 20 Hz**. **"Cửa sổ đó có rỗng không" chính là nội dung của GATE 0.**

> `100 kΩ / 10-bit / 1,51 mV` là **ngân sách thiết kế** trong `docs/04` §1, **không phải kết quả đo** — cấm dùng như số liệu.
> Bản nộp 2026-09-26 dùng chuỗi khác (`CLM-HW-003`, chờ `DEC-HW-005`): ADS1115 + INA333 + `R_ref = 10 kΩ` + SHT30 + 1 IMU LSM6DS3 — xem `docs/04` §8.
> Số học cửa sổ preload phải tính lại với LSB mới sau khi `DEC-HW-005` được chốt.

**Đính chính hai chỗ cũ trong README này:** (1) bản trước viết "thiết kế **không dùng IMU**" — đúng hơn: **dấu gập/duỗi** lấy từ mẫu vách mà không cần encoder (ý của `docs/01` §4), còn **góc và tốc độ kéo** thì bản nộp chỉ còn **1 IMU ở mu tay** (bù nghiêng), không còn 6 IMU đo góc khớp — **nguồn đo góc cho `GAP` là câu hỏi mở I7**, chờ `DEC-HW-005` trả lời. (2) bản trước viết `GAP = AROM − PROM` — **bản nộp quy ước `GAP = PROM − AROM ≥ 0°`**; đã sửa đồng bộ ở §5.

Phân cấp thuật ngữ (bắt buộc dùng đúng): [`docs/bao_cao/GLOSSARY.md`](docs/bao_cao/GLOSSARY.md) — **vật liệu Velostat** ≠ **sensing element** (Velostat + đồng tự dính + cấu trúc sandwich) ≠ **mảng sensing element** ≠ **hệ thống cảm biến** (mảng + ESP32-S3 + firmware).

## 5. Ba đại lượng dẫn xuất và quy tắc đơn vị

| Đại lượng | Định nghĩa (bản nộp 2026-09-26, `CLM-DEF-001` — chờ `DEC-METRIC-002` phê chuẩn) | Điều kiện phải in kèm | Đơn vị |
|---|---|---|---|
| **`EI`** (Effort Index) | trung vị biến thiên phổ của tín hiệu vi sai 12 kênh, chuẩn hóa theo vận tốc góc cùng phiên; công thức/cửa sổ/ngưỡng **cố định trước khi đo**, chỉ so sánh nội bộ cùng giao thức | ngón · tốc độ kéo · hướng dẫn bằng giọng nói | **không thứ nguyên** (công thức tường minh còn nợ) |
| **`GAP`** | **`PROM − AROM`** trên cùng ngón, cùng phiên (≥ 0°, theo giao thức; **không** tự suy nguyên nhân yếu/co cứng/khớp) | PROM kéo thụ động chậm · AROM gập chủ động tối đa · **hai tốc độ kéo** | độ — **nguồn đo góc còn mở (I7)**, **không** suy từ ADC |
| **`RAL`** | nấc tải **nhỏ nhất** (thang 120 g → 0 g) đạt tỉ lệ hoàn thành nhịp **P_complete ≥ 80 %** (10 chu kỳ gập/duỗi mỗi nấc, trên giàn + phantom) | tải (g) · vị trí khớp · tốc độ | **gam + bậc tải** (đặc trưng giao thức kiểm định, **không** phải bằng chứng hồi phục) |

**Cấm trong mọi bảng số:** `ADC → newton` (không có load cell trên ngón; load cell chỉ là chuẩn đối chứng ở rig) · `ADC → độ` · dùng `RAL` như chỉ số lâm sàng.
> Lịch sử định nghĩa (để không lẫn khi đọc tài liệu cũ): README/`DE_CUONG_NOP_TRUONG.md` cũ ghi `GAP = AROM − PROM`, `EI = median\|d\|/(1+κ\|v̂\|)`, `RAL = thực/yêu cầu ∈ [0,1]`; `docs/02` §7.3 ghi `GAP` mẫu chuẩn hóa, `EI = E/(E+E_nền)` — xem sổ R2–R4 trong sync review §5.3.

## 6. Phương pháp: bộ kiểm chứng 10 ngưỡng (bản nộp: M1–M6 + C1.1–C1.10)

> Ngưỡng được viết ra và **đóng chốt trước khi có bất kỳ số liệu nào**, và **không** chỉnh lại sau khi thấy số. Một ngưỡng không đạt ⇒ báo cáo **fail** ở ngưỡng đó. Cấm viết "GATE 0 pass" khi `C1.2` hoặc `C1.8` fail. Bảng dưới là ngưỡng **đã nộp** (`CLM-MET-005`, chờ `DEC-METRIC-002` phê chuẩn); cột cuối ghi chỗ đổi so với bộ G0.x cũ.

| ID (nộp) | Câu hỏi | Ngưỡng đã nộp | Đổi so với G0.x |
|---|---|---|---|
| **C1.1** | Sàn nhiễu mạch đo là bao nhiêu? | `Vpp ≤ 5 mV` / 5.000 mẫu tĩnh | chốt luôn định nghĩa B + ngưỡng tuyệt đối |
| **C1.2** [Trọng tâm] | Có tồn tại `F_p` vừa đủ nhạy vừa đủ ổn định? | `SNR ≥ 18 dB` (≈8×) tại `ΔF = 1 N`, ≥10/12 kênh | đơn vị LSB → dB, phạm vi 10/12 kênh |
| C1.3 | Mảng có thật sự là áp kế? | `γ ≥ 0,25` (≥10/12 kênh), `R² ≥ 0,90` | **R² 0,95 → 0,90** |
| C1.4 / C1.5 | Lặp lại giữa chu kỳ / giữa **ngày**? | `CV ≤ 5 %` · `CV ≤ 8 %` (3 ngày, tháo/đeo lại, trên phantom) | **ICC → CV**, nới 5 %→8 % |
| C1.6 / C1.7 | Đường lên có trùng đường xuống? Có bị lún khi giữ tải? | `h ≤ 18 %` · `creep ≤ 8 %` (giữ 60 s @ 5 N) | **15 %→18 %** · **đổi định nghĩa creep** |
| **C1.8** [Trọng tâm] | Tín hiệu có trôi chậm hơn biên độ cần đo? | trôi/tín hiệu ≤ 2,0 sau 10 ngày (qua auto-zero) | **bỏ** điều kiện so ΔV@1N |
| C1.9 | Các mảng có đủ giống nhau để so sánh giữa ngón? | độ rải `γ ≤ ±40 %` (+ bảng chuẩn hóa) | khớp |
| C1.10 | Cấu hình kênh đọc kịp không? | `fs ≥ 20 Hz` đồng thời 12 kênh | khớp (Lưu ý: PDF §8.1/§9.1 ghi 50 Hz — I1) |

[Trọng tâm] = ô chỉ tiêu quyết định loại bỏ đề tài. **Cách chạy GATE 0 mà không cần một dòng code:** `research/protocols/08a` — phiếu in được, chuẩn lực là **khối lượng đã cân** (`F = m·g`, không trễ, không cần hiệu chuẩn điện tử), mọi phép tính chỉ là trừ số nguyên. Kế hoạch đầy đủ + cây fail: `research/protocols/08` (giữ 10 ô chờ chốt; bảng đối chiếu G0↔C1: sync review §4).

## 6.1. Cơ cấu hỗ trợ theo nhu cầu (AAN) — trụ cột thứ 4 (`DEC-SCOPE-006`, nguồn: `de_cuong/DE_CUONG_NGHIEN_CUU.pdf` §10)

> **Ranh giới an toàn — không có ngoại lệ:** toàn bộ nội dung mục này chỉ chạy trên **giàn đo cơ khí + mô hình tay giả silicone (phantom, Shore A 25–30)**. Không servo, lò xo hay cơ cấu chấp hành nào trong mục này được phép chạm/tác động lực lên ngón tay người thật, kể cả tình nguyện viên khỏe mạnh — tình nguyện viên chỉ được dùng để đánh giá **ergonomics đeo thử, không tải** (`docs/02` §10.6, `DEC-SCOPE-003`, `DEC-SCOPE-006`).

**Vì sao cần AAN:** kéo thụ động liên tục (CPM) làm mất tính tương tác chủ động và có thể quá tải cơ học cho khớp co cứng. AAN áp dụng nguyên tắc **can thiệp tối thiểu**: chỉ bù đúng phần lực còn thiếu khi đã phát hiện nỗ lực chủ động nhưng chưa đủ hoàn thành quỹ đạo mục tiêu.

**Giàn đo (research hardware, không phải sản phẩm đeo tay):** khung nhôm định hình 2020 + ray trượt bi + vít me bi tự hãm + servo (holding torque ≥ 10 kg·cm) + load cell 5 kg qua HX711 24-bit làm chuẩn đối chứng độc lập, mang mô hình bàn tay giả silicone y tế (Shore A 25–30).

**Cơ chế 3 khối:**
1. Lò xo trợ giúp thụ động chia nấc: 20 / 40 / 60 / 80 / 100 / 120 g.
2. Servo trợ lực chủ động qua khớp truyền lực cứng 4 khâu dưới dẫn động (1 servo / cặp khớp MCP–PIP mỗi ngón): `F_assist(t) = max(0, F_target(t) − F_phantom(t))`, giới hạn an toàn cơ học `F_max ≤ 5 N`. Quy trình 3 pha: **[Pha 1]** giữ tĩnh khi `EI < EI_th`; **[Pha 2]** độ trễ vận động `t_delay = 1,2 s` cho phantom hoàn thành nỗ lực ban đầu; **[Pha 3]** kéo trợ lực bù đúng phần thiếu hụt.
3. Giao diện phản hồi sinh học thị giác (thanh đo `EI` + lực hỗ trợ thời gian thực).

**Chỉ số `RAL` sinh ra từ AAN:** 10 chu kỳ gập/duỗi mỗi nấc tải (120 g → 0 g); điểm cắt `RAL` = nấc tải nhỏ nhất đạt `P_complete ≥ 80%`. `RAL` giảm dần qua các chu kỳ phản ánh mức giảm phụ thuộc vào lực trợ giúp ngoại vi — **là đặc trưng giao thức kiểm định trên phantom, không phải bằng chứng hồi phục lâm sàng**.

> **Trạng thái bằng chứng:** toàn bộ thông số trên (`F_assist`, `F_max`, `t_delay`, các nấc tải) là **thông số thiết kế đã đăng ký trong bản đề cương 2026-10-03**, **chưa có số đo nào từ rig thật** (`CLM-AAN-001`, `research/bench/logs/` vẫn trống cho AAN). Không trích các con số này như kết quả đã kiểm chứng.

## 7. Kế hoạch và ngân sách

```
Lớp 0 (GATE 0)    Mảng Velostat + đồng tự dính + jig in + khối lượng chuẩn + đồng hồ đo
                  ── chuẩn lực = F = m·g, KHÔNG cần load cell ──►  0,12–0,65 triệu đ
Lớp 1 (GATE A/B)  3 ngón (cái, trỏ, giữa) × 2 khớp, cầu vi sai hai vách + 1 IMU LSM6DS3
                  + INA333 + ADS1115 + 2×CD74HC4067 → ESP32-S3 (20 Hz)  ► +0,57–1,50 triệu đ
Lớp 2 (GATE D/F)  Orange Pi 5 Pro (log nguồn thô + dashboard) + rig E4/E5 (vít me,
                  phanh từ, tải chuẩn) + phantom silicone          ► +1,10–2,50 triệu đ
Lớp 3 (lâm sàng)  IRB + bệnh viện + n ≥ 20                          ► CHƯA MỞ — ngoài đề cương
```

> Bản nộp đặt thêm 3 ràng buộc sản phẩm: giá găng mục tiêu **< 1,5 triệu đ** · khối lượng đeo **< 150 g** · trễ toàn hệ thống **≤ 500 ms** (M5).

| Tổng hợp | Tiền mặt cần chi (vật tư đã có sẵn đã được trừ) |
|---|---|
| Hết GATE 0 | **0,12–0,65 triệu đ** |
| Hết GATE A+B | + 0,57–1,50 triệu đ |
| Hết GATE F | ≈ **1,8–4,7 triệu đ** |
| Kịch bản phải mua tất cả | ≈ 6,5–12 triệu đ |
| **Chi phí tối đa nếu GATE 0 fail** | **≤ 0,65 triệu đ** — thiết kế để cắt lỗ sớm |

Quy tắc: mỗi lớp **chỉ mở khi lớp trước pass**; vật tư được cấp/đã có ghi là **"được cung cấp"**, không ghi thành "chi phí 0 đ"; giá thương mại chỉ là **mốc so sánh có nguồn**, không phải giá của đề tài. Bảng theo hạng mục: `docs/DE_CUONG_NOP_TRUONG.md` §7; trạng thái vật tư: `research/context/EQUIPMENT_AND_ACCESS.md`.

**Kế hoạch theo cửa, không theo lịch thi** (repo **không có ngày nộp**, và không ai được bịa một cái): 8 pha từ "chốt ngưỡng → GATE 0 → A → B → C → D → E → F", chi tiết `research/protocols/06`–`08`.

## 8. Tính mới — và bộ tiêu chí đang dùng để tự chấm

> **Bộ tiêu chí: ViSEF/ISEF**, không phải tạp chí kỹ thuật. Đề tài **không** có nguyên lý mới và không tự đo mình bằng chuẩn cần nguyên lý mới + dataset + đối chứng lâm sàng. Mọi nhận định "mới/không mới" phải kèm tên bộ tiêu chí (`DEC-NOV-001` chờ nhóm nghiên cứu chốt mức).

| Hướng được coi là mới | Kiểm chứng ngược đã làm | Kết luận hiện hành |
|---|---|---|
| Vách cứng phân biệt hướng lực | Phần tử áp điện trở **trên vách** có từ **2015** (`SRC-SIDEWALL-PIEZO-2015`); vỏ cứng khớp nối + da áp điện trở **2026** (`SRC-ARTGLOVE-2026`, 2048 taxel, 22 DoF) | **Cải tiến cấu hình + cách lập luận**, không phải nguyên lý |
| Găng đo lực cho người đột quỵ | Đối thủ gần nhất: Lin et al., *Sensors* 2022;22(19):7212 — **19 IMU + 1 bóng áp lực**, n = 14, **có IRB** | Họ thắng về **học máy + cỡ mẫu**; đề tài phải thắng ở **cơ khí tạo phân tách + lớp tin cậy**, không ở số cảm biến |
| Găng có chức năng tập/hỗ trợ | ironHand (JRATE 2016 **và** J Rehabil Med 2018;50:598–606, n = 5, **không** dùng thiết bị đo lực chuẩn hoá làm kết quả chính) | **Cập nhật `DEC-SCOPE-006` (2026-10-11):** đề tài **không** bỏ hẳn AAN — tích hợp lại làm trụ cột thứ 4 (§6.1), nhưng khác nhóm robot thương mại ở chỗ AAN chỉ chạy **trên giàn đo + mô hình tay giả (phantom)**, không tác động trực tiếp lên người bệnh; thiết bị **giao cho người dùng** vẫn thuần đo/theo dõi |
| Ghi nhận tại nhà thay cho tự báo cáo | Manumeter (RCT, n = 20, *Sensors* 2022) — MDC 31 %, 100–200 đếm nhầm/giờ | Đây là **bằng chứng cho khoảng trống**, không phải cho thiết bị của ta |
| "Hệ thống đầu tiên" | Khảo sát hệ thống găng tự chế (arXiv 2405.15417) + găng đo từ 2006 + Neofect Smart Glove (132 g, flex + 9 DoF, dashboard cho chuyên gia) | **Cấm nói.** Mẫu câu duy nhất được phép: *"chưa tìm thấy công trình nào kết hợp [A+B] cho [nhóm X]"*, và chỉ khi đã có số tự đo |

Bằng sáng chế đã tra: **US20150233779A1** (Waltop) — **đã abandoned**; **CN116954366A** (ĐH Đông Nam Á) — **pending**. FTO = `PARTIAL` vì **chưa đọc toàn văn điểm yêu cầu bảo hộ** ⇒ chỉ được nói "đã tra cứu, không phát hiện xung đột trực tiếp". Chi tiết + nghĩa vụ trích dẫn: `research/reviews/2026-09-19_prior_art_novelty_gate1.md`.

## 9. Giới hạn tự khai

| # | Giới hạn | Cách đề tài xử lý |
|---|---|---|
| 1 | **Chưa có một kết quả đo nào** | nêu ngay đầu README và đầu đề cương; không nói vòng quanh |
| 2 | Chưa hiệu chuẩn `ΔR → N`; ADC không quy đổi ra newton/độ | dùng counts + `EI` không thứ nguyên |
| 3 | Đối tượng tự kiểm chứng ban đầu là **một người** (chính người chế tạo) | chặn mọi kết luận lâm sàng tới khi có IRB + n ≥ 20 |
| 4 | Velostat phi tuyến, trễ, từ biến, trôi, nhạy ẩm | biến thành ngưỡng đo được (G0.5–G0.7), không tuyên bố đã khắc phục |
| 5 | Không có bằng chứng hiệu quả lâm sàng | tuyên bố dừng ở "cung cấp phép đo đáng tin" |
| 6 | `RAL` không phải chỉ số lâm sàng | chỉ dùng để so sánh cấu hình máy + chứng minh phát hiện lỗi |
| 7 | `GAP`/`EI` không thay thế FMA/ARAT/MAS | mục tiêu là **tần suất đo**, không phải thay công cụ chuẩn |

## 10. Bằng chứng của chính hồ sơ này

| Loại | Số lượng | Kiểm ở đâu |
|---|---|---|
| Nguồn đã vào sổ, có locator + mức đã đọc | **168** (cập nhật 2026-10-11: +2 homunculus/SCAN, +10 FSR-vs-sEMG/Velostat-novelty cho `CLM-HW-005`, +3 patent/prior-art cho rà soát novelty Velostat-AAN) | `research/evidence/SOURCE_LEDGER.csv` |
| Tuyên bố, kèm cấp bằng chứng + hành động còn lại | **32** (cập nhật 2026-10-11: +1 `CLM-BIO-005`, +1 `CLM-HW-005`; `CLM-NOV-003`/`CLM-NOV-004` cập nhật bằng chứng mới, không thêm dòng) | `research/claims/CLAIM_LEDGER.csv` |
| Quyết định có ngày + chủ sở hữu + trạng thái | **47** (cập nhật 2026-10-11: +6 ID mới — `DEC-SYNC-002`, `DEC-SCOPE-006`, `DEC-PHASE-002`, `DEC-TITLE-003`, `DEC-BIO-001`, `DEC-HW-006`; **+1 đổi trạng thái** — `DEC-NOV-001` PROPOSED → **ĐÃ CHỐT**, điều kiện ban đầu về tra IPC/lane R5 vẫn còn nợ) | `research/context/DECISION_LOG.md` |
| Nhật ký truy vấn ngoài (**kể cả lần tìm không thấy**) | **94** (cập nhật 2026-10-11: +6 truy vấn patent/prior-art cho rà soát novelty Velostat-AAN, 1 trong đó `blocked` — xem `research/reviews/2026-10-11_prior_art_novelty_velostat_AAN.md`) | `research/queries/QUERY_LOG.jsonl` |
| Phiếu đo/thực nghiệm đã thiết kế, chưa chạy | **10 ngưỡng · 7 gate · 8 buổi bench** | `research/protocols/06`–`08a` |
| Số liệu đo của đề tài (đã chính thức hoá theo schema GATE 0) | **0** | `research/bench/logs/` — đang trống theo đúng schema; **ghi chú kỹ thuật bring-up thật nhưng chưa chính thức hoá** nằm ở `research/notebooklm_sync/experiments/` (`DEC-PHASE-002`) |

Quy tắc chống tự nâng cấp: **không** nâng mức bằng chứng; **một lần tìm không thấy = `UNVERIFIED`**, không phải "không tồn tại"; số liệu giả lập phải dán nhãn giả lập; mọi đề xuất kỹ thuật đều do **nhóm nghiên cứu phê duyệt**. Toàn bộ quy chuẩn lưu trữ tại tài liệu nội bộ của nhóm.

## 11. Bản đồ repo

| Nhóm | File | Vai trò |
|---|---|---|
| **Nộp trường** | [`docs/DE_CUONG_NOP_TRUONG.md`](docs/DE_CUONG_NOP_TRUONG.md) | Đề cương hoàn chỉnh: 4 trụ + M1–M6 + ngân sách + hạn chế tự khai + Phụ lục A chống-claim |
| **Đề cương mới nhất** | [`de_cuong/DE_CUONG_NGHIEN_CUU.pdf`](de_cuong/DE_CUONG_NGHIEN_CUU.pdf) (2026-10-03, 16tr) | Bản PDF/docx mới hơn bản đã nộp trường (`docs/DE_CUONG.pdf`, 2026-09-26, 15tr); bổ sung Mục 10 (AAN + RAL trên giàn + phantom); `DEC-SYNC-002` — chưa rõ đã dùng để nộp lại hay chỉ là bản song song |
| Ghi chú kỹ thuật/NotebookLM | [`research/notebooklm_sync/`](research/notebooklm_sync/) | Đồng bộ từ notebook Google NotebookLM; `experiments/01-05` = log bring-up phần cứng thật do nhóm nghiên cứu thực hiện (`DEC-PHASE-002`, chưa chính thức hoá); `chat_transcripts/`, `studio/` = bản ghi chú nháp ban đầu, chỉ dùng để tham khảo nội bộ — không trích trực tiếp vào hồ sơ nộp |
| Đề tài | [`docs/01_Topic_Definition.md`](docs/01_Topic_Definition.md) | Tên đã chốt, vấn đề, khoảng trống, RQ1–R3, phạm vi (`A.4`: **không** phải thiết bị điều trị) |
| Lý thuyết | [`docs/02_Theoretical_Foundation.md`](docs/02_Theoretical_Foundation.md) | Sinh lý hồi phục, thang đo, cơ sinh học, vật liệu áp trở, mô hình §5.5, `EI`/`GAP`/`RAL`, INT8 |
| Prior art & sáng chế | [`docs/03_Literature_Gap_Analysis_Plan.md`](docs/03_Literature_Gap_Analysis_Plan.md) | Kế hoạch rà soát 2011–2026; §7 phương pháp tra cứu sáng chế + hồ sơ thất bại |
| Phần cứng | [`docs/04_Hardware_Architecture.md`](docs/04_Hardware_Architecture.md) | Kênh, MUX, ngân sách nhiễu/độ phân giải (**ngân sách thiết kế**, không phải kết quả) |
| Cơ cấu nẹp ngón | [`docs/06_Co_Cau_Co_Khi_Exoskeleton.md`](docs/06_Co_Cau_Co_Khi_Exoskeleton.md) · [`3d_model/`](3d_model/custom_exo/full_finger_modular/) | Thiết kế 3 đốt Print-in-Place, khớp rãnh trượt bù 13.5mm cho ngón dài, khoang preload Velostat, file in STL/STEP/FCStd |
| Soạn thảo | [`docs/05_De_Cuong_Dang_Ky_DRAFT.md`](docs/05_De_Cuong_Dang_Ky_DRAFT.md) | **Outline nội bộ** (không nộp) + §8b các chỗ nhóm nghiên cứu cần sửa |
| Mẫu báo cáo | [`docs/OUTLINE_BAOCAO_VISEFD.md`](docs/OUTLINE_BAOCAO_VISEFD.md) · [`docs/bao_cao/`](docs/bao_cao/) | Khung A/B/C + A.1–A.7 + GLOSSARY |
| Kiểm chứng | [`research/protocols/06`](research/protocols/06_glove_hand_GATE_experiment.md) · [`07`](research/protocols/07_ral_phantom_and_ktv_interview.md) · [`08`](research/protocols/08_gate0_execution_plan.md) · [`08a`](research/protocols/08a_gate0_bench_sheets.md) | Master 7 gate · RAL/phantom + phiếu tham khảo chuyên gia · kế hoạch GATE 0 · **phiếu đo in được, không code** |
| Vật tư & tiếp cận | [`research/context/EQUIPMENT_AND_ACCESS.md`](research/context/EQUIPMENT_AND_ACCESS.md) | Đã có / chưa chắc / cần mua + 4 bước chạy GATE 0 |
| Đánh giá chiến lược | [`research/reviews/2026-09-19_project_ceiling.md`](research/reviews/2026-09-19_project_ceiling.md) | Trần theo từng trục + **nguyên tắc giải ngân theo lớp** + quy tắc dừng |
| Benchmark | [`research/reviews/2026-09-19_benchmark_xe_lan_ALS_QG2025.md`](research/reviews/2026-09-19_benchmark_xe_lan_ALS_QG2025.md) | **Nội bộ.** Kiểm đếm một báo cáo từng giải Nhất quốc gia → định cỡ hình thức 15–20 trang, ≥1,3 ảnh/bảng mỗi trang. **Cấm trích trong hồ sơ nộp** (`DEC-SCOPE-003`) |
| Nhật ký đo | [`research/bench/logs/`](research/bench/logs/) | Một file mỗi buổi; **bản gốc không bao giờ bị sửa**; header nhắc lại ngưỡng đã chốt |
| Chỉ mục | [`INDEX.md`](INDEX.md) · [`research/README.md`](research/README.md) | Sơ đồ file, quy ước workspace, quy chuẩn nghiên cứu |

## 12. Thiết lập & quy trình

Yêu cầu: Git, Python 3.10+, Bash.

```bash
python3 -m venv .venv && . .venv/bin/activate
python -m pip install --upgrade pip && python -m pip install -r requirements.txt
bash scripts/bootstrap_research_tooling.sh
python scripts/check_research_environment.py --strict
python scripts/build_context_bundle.py --budget-chars 40000     # -> research/generated/ (đã gitignore)
```

**Bốn việc còn lại, đúng thứ tự (cập nhật 2026-10-11):**

1. [ ] **Nhóm nghiên cứu chốt các quyết định đồng bộ còn mở**: 6 cũ (`DEC-SYNC-001`/`TEAM`/`TITLE-002`/`HW-005`/`METRIC-002`/`SCOPE-005`, sync review §6) + 4 mới (`DEC-TITLE-003` chọn tên, xác nhận `de_cuong/DE_CUONG_NGHIEN_CUU.pdf` có phải bản nộp lại không, chính thức hoá log bring-up thành GATE 0, xác nhận SHT30↔AHT20) **rồi chốt 10 ô** `Chốt?` trong `research/protocols/08` §7 (việc này **không** ai làm thay được).
2. [ ] **Chính thức hoá log bring-up đã có** (`research/notebooklm_sync/experiments/01-05`, `DEC-PHASE-002`) thành log GATE 0 hợp lệ theo schema `research/protocols/08a` (session_manifest + ngưỡng chốt trước đo), hoặc chạy GATE 0 mới bằng `research/protocols/08a` nếu log cũ không đủ trường dữ liệu → mỗi buổi = 1 file log + 8 ảnh; **kể cả buổi fail cũng phải lưu**.
3. [ ] Thay dự toán bằng **báo giá/hoá đơn thật** → `DEC-BUDGET-001` (id dự kiến trong `2026-09-19_project_ceiling.md`, chưa tạo); chỉ khi đó mới xét giải ngân Lớp 1.
4. [ ] Nếu AAN đi tới giai đoạn chế tạo giàn đo thật (§6.1): kiểm chứng trên phantom trước, log vào `research/bench/logs/`, và **không bao giờ** thử trên người thật dù chỉ một lần "thử nhẹ".

Luồng chuẩn cho mỗi thay đổi lớn: đọc `research/context/PROJECT_SNAPSHOT.md` → log truy vấn (`scripts/research_log.py`) → cập nhật `SOURCE_LEDGER`/`CLAIM_LEDGER` → chạy review protocol → cập nhật snapshot + `INDEX.md` → dựng lại bundle.

## 13. Đổi tên repo và đồng bộ metadata trên GitHub

Repo hiện tên `smart-glove-hand-function-monitoring` với **description vẫn là mô tả đề tài cũ**. Bốn lệnh dưới đây chạy theo thứ tự, copy nguyên khối được:

```bash
# 1) Doi ten repo cho khop ten de tai moi (quyen admin cua chu du an)
gh repo rename stroke-hand-monitoring-glove --repo nhatvanngoc/smart-glove-hand-function-monitoring

# 2) Cap nhat remote cua may local theo ten moi
git remote set-url origin https://github.com/nhatvanngoc/stroke-hand-monitoring-glove.git
git push -u origin HEAD

# 3) Mo cua cho cai ten moi: description + topic + homepage (xoa topic cu neu can)
gh repo edit --description "Nghiên cứu, thiết kế găng tay giám sát và đánh giá khả năng vận động bàn tay trong phục hồi chức năng chủ động sau đột quỵ — giai đoạn cơ sở lý thuyết, chưa có kết quả đo; toàn bộ prior art có DOI tại research/evidence/" \
  --add-topic stroke --add-topic rehabilitation --add-topic hand-function --add-topic wearable-sensors \
  --add-topic piezoresistive --add-topic velostat --add-topic esp32-s3 --add-topic isef --add-topic visef

# 4) kiem tra
gh repo view --json name,description,repositoryTopics -q '"\(.name)\n\(.description)\nTopics: \([.repositoryTopics[].name]|join(", "))"'
```

**Nếu không muốn đổi tên repo**, chỉ chạy bước 3 (description/topics) — README và tên đề tài trong repo đã khớp nhau, GitHub redirect tự động nếu sau này đổi tên.

*Ba lựa chọn tên repo, xếp theo khuyến nghị:* `stroke-hand-monitoring-glove` (đúng 3 từ khoá: đối tượng – việc – thiết bị) · `hand-motion-glove` (ngắn, dễ nhớ, hơi rộng) · `smart-glove-stroke-rehab` (dễ đọc nhưng giữ chữ "smart" mà tên đề tài mới đã bỏ).

---

### Lịch sử cập nhật gần nhất

| Ngày | Việc |
|---|---|
| 2026-10-11 | **Đọc toàn bộ repo + setup môi trường** (10/11 check, chỉ `pdflatex` chưa cài đặt trên máy trạm); đọc toàn văn `research/notebooklm_sync/` (10 file) và phát hiện bản đề cương mới chưa đồng bộ `de_cuong/DE_CUONG_NGHIEN_CUU.pdf` (2026-10-03, 16tr, có Mục 10 AAN). Theo yêu cầu minh thị của nhóm nghiên cứu ("AAN là một trong những trụ cột hạt nhân"): chốt `DEC-SYNC-002` (bản đề cương mới) + `DEC-SCOPE-006` (nâng AAN thành trụ cột thứ 4, **ranh giới an toàn phantom-only không đổi**) + `DEC-PHASE-002` (ghi nhận nhóm nghiên cứu đã tự thực hiện bring-up phần cứng thật, chưa đạt chuẩn GATE 0); đề xuất `DEC-TITLE-003` (4 phương án tên, chưa chốt); +6 nguồn/+3 claim/+5 quyết định vào ledger. |
| 2026-09-27 | **Đồng bộ bản nộp `docs/DE_CUONG.pdf` (2026-09-26):** đội hình 2 người + GVHD + timeline + lĩnh vực Nhúng; tên quay về `DEC-TOPIC-019` (`DEC-TITLE-001` chờ hủy); `GAP = PROM − AROM`; ngưỡng C1.x; kiến trúc ADS1115+INA333; +7 nguồn/+3 claim; 6 quyết định chờ chốt (`DEC-SYNC-001`…`DEC-SCOPE-005`) |
| 2026-09-19 (lượt 4) | README dựng lại theo cấu trúc hồ sơ khoa học (luận điểm · RQ + điều kiện giết · nguyên lý · 10 ngưỡng · tự khai); đề xuất tên mới (ghi nhầm là "chốt" — đã sửa 2026-09-27, chờ `DEC-TITLE-002`) |
| 2026-09-19 (lượt 3) | Đề cương nộp `docs/DE_CUONG_NOP_TRUONG.md`; sửa 2 lỗi trích dẫn trong `A.1`; thi hành `DEC-ROLE-001` (không nêu danh tính người được tham khảo) |
| 2026-09-19 (lượt 1–2) | Prior art lượt 1–2 (novelty dịch từ cơ chế sang lớp thống kê); GATE 0 plan + phiếu đo không code; đánh giá trần dự án + mức đầu tư theo lớp |
