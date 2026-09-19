# NGHIÊN CỨU, THIẾT KẾ GĂNG TAY GIÁM SÁT VÀ ĐÁNH GIÁ KHẢ NĂNG VẬN ĐỘNG BÀN TAY TRONG PHỤC HỒI CHỨC NĂNG CHỦ ĐỘNG SAU ĐỘT QUỴ

> **Học sinh:** Văn Ngọc Nhật Anh — THPT Quảng Trị · **Trường:** THPT Quảng Trị, Quảng Trị
> **Trạng thái hồ sơ:** pha **cơ sở lý thuyết & thiết kế** (`DEC-PHASE-001`) · **chưa có kết quả thực nghiệm** · bản để nộp: [`docs/DE_CUONG_NOP_TRUONG.md`](docs/DE_CUONG_NOP_TRUONG.md)
> **Tên đề tài chốt ngày 2026-09-19** (`DEC-TITLE-001`), thay tên cũ `DEC-TOPIC-019`; lịch sử đặt tên: [`research/reviews/2026-09-19_title_options.md`](research/reviews/2026-09-19_title_options.md)

**Tên tiếng Anh (hồ sơ ISEF/ViSEF bản dịch):**

> *Research and design of a glove that monitors and assesses hand motor function during active post-stroke rehabilitation*

**Phụ đề kỹ thuật (dùng ở đầu báo cáo, không nằm trong tên):**

> *Găng tay đo lực ép bên trên khung cứng + tầm vận động chủ động/thụ động từng ngón, kèm ngưỡng tin cậy đăng ký trước khi đo.*

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
[7. Kế hoạch và ngân sách](#7-kế-hoạch-và-ngân-sách) ·
[8. Tính mới — và bộ tiêu chí đang dùng để tự chấm](#8-tính-mới--và-bộ-tiêu-chí-đang-dùng-để-tự-chấm) ·
[9. Giới hạn tự khai](#9-giới-hạn-tự-khai) ·
[10. Bằng chứng của chính hồ sơ này](#10-bằng-chứng-của-chính-hồ-sơ-này) ·
[11. Bản đồ repo](#11-bản-đồ-repo) ·
[12. Thiết lập & quy trình](#12-thiết-lập--quy-trình) ·
[13. Metadata repo GitHub](#13-metadata-repo-github)

---

## 1. Luận điểm của đề tài

Đề tài **không** tuyên bố một nguyên lý vật lý mới và **không** bán một nguyên mẫu. Nó tuyên bố ba thứ, theo thứ tự bảo vệ được giảm dần:

1. **Một kiến trúc cơ khí** — mảng áp trở đặt trên **vách cứng** của ốp ngón, cấu hình nửa cầu Wheatstone, để đo riêng **thành phần lực ép bên**: đại lượng tăng khi người bệnh chống lại tầm vận động, tức là thứ mà cảm biến gập góc *về bản chất* không phân biệt được.
2. **Một thiết kế phép đo** — `AROM` rồi `PROM` trên cùng ngón, cùng phiên, ở **hai tốc độ kéo** (vì phản ứng căng cơ phụ thuộc tốc độ). `GAP = AROM − PROM` chính là phép thử phân tách *"chưa cố"* khỏi *"bị giữ lại"*.
3. **Một lớp tự kiểm chứng** — ngưỡng `MDC`/`ICC`/`CV`/trôi **đăng ký trước khi đo**, mỗi phiên mang cờ `UNRELIABLE` khi vượt ngưỡng, và **lỗi được tiêm có chủ đích** trên rig để chứng minh cờ đó không phải đồ trang trí.

> **Câu chốt cho hội đồng:** phần (1) đã có tiền lệ ở tầng phần tử cảm biến, phần (2) là lựa chọn phương pháp luận, **phần (3) là phần đề tài này mạnh hơn cả một số công trình đã công bố** — và cũng là phần rẻ nhất để làm đúng.

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

## 3. Câu hỏi nghiên cứu và điều kiện giết

**RQ chính** (quyết định đề tài sống/chết):

> **R1.** Đáp ứng lực–hướng từ mảng áp trở trên vách khung có **đủ nhạy và đủ ổn định** để phát hiện thay đổi chức năng bàn tay theo tuần — **vượt trên** biên độ nhiễu/trôi của chính hệ thống đo — và **không** sinh ra cảnh báo tiến triển giả?

**RQ phụ:**

> **R2.** Dấu hiệu gập/duỗi có suy ra được **chỉ từ mẫu đáp ứng trên vách**, không cần encoder, và kết hợp được với góc IMU để tái tạo tư thế bàn tay đủ trung thực cho chuyên gia đọc?
> **R3.** Các chỉ số trích xuất có **đồng biến** với công cụ chuẩn (Box & Block / ARAT / lực kế cầm tay) ở mức đủ để dùng làm thông tin bổ sung giữa hai lần tái khám?

| RQ | Cửa quyết định | Nếu fail thì sao |
|---|---|---|
| R1 | **`GATE 0`** (`G0.1` + `G0.7` là hai ô giết) | Không có chuỗi số liệu nào để nói về diễn tiến → đề tài đổi thành **báo cáo phương pháp + kết quả âm tính** (vẫn nộp được, vẫn có giá trị) |
| R1 | **`GATE C`** (trôi 28 ngày, nhiệt–ẩm, tháo/lắp) | Dừng đề tài theo đúng nghĩa đã ghi trong `research/protocols/06` |
| R2 | `GATE A`/`GATE B` trên ≥ 1 ngón | Bỏ tái tạo 3D, giữ `GAP`/`EI` |
| R3 | **Chỉ sau IRB** — nằm ngoài phạm vi đề cương này | Không nêu giả thuyết R3 như kết quả; chỉ là thiết kế dự phòng |

**Điều đề tài không hỏi, và do đó không được claim:** không đo lực tuyệt đối trên ngón, không đo góc khớp tuyệt đối từ ADC, không đo hoạt động cơ, không chẩn đoán, không thay thế đánh giá lâm sàng, không cam kết hiệu quả phục hồi.

## 4. Nguyên lý hoạt động

```
Co cơ / bị duỗi thụ động ──► ngón ép vào VÁCH CỨNG của ốp ngón
   ► áp suất tiếp xúc p = F/A_c nén mảng Velostat
   ► ΔR/R = γ · Δp/p₀                       (γ = độ nhạy áp trở, p₀ = F_p/A_c)
   ► nửa cầu Wheatstone với R_ref, kích V_EX
   ► ΔV = V_EX · ΔR /(R₀ + R_ref)
   ► mux CD74HC4067 ──► ESP32-S3 ADC 12 bit ──► trung bình + lấy mẫu lại 20 Hz
   ► IMU cùng phiên: góc AROM/PROM + tốc độ kéo
   ► EI · GAP · RAL          (KHÔNG phải newton, KHÔNG phải độ suy từ ADC)
```

**Hai kết quả rút ra từ mô hình, và cả hai đều kiểm chứng được bằng tay** (`docs/02` §5.5, `CLM-MET-003`):

1. `A_c` **triệt tiêu ở bậc nhất** ⇒ kích thước mảng **không** phải vấn đề tỉ số tín hiệu/nhiễu; nó là vấn đề cơ khí (áp suất phân bố lại, độ lặp lại khi tháo/lắp). ⇒ Không cần mua mảng to hơn.
2. Thiết kế chỉ sống trong một **cửa sổ tiền tải `F_p` chặn hai phía**: dưới thì không đủ nhạy — với `n_eff ≈ 11`, `V_EX = 3,1 V`, `LSB = 1,51 mV` và `ΔV ≥ 8 LSB` tại `ΔF = 1 N` thì `F_p ≤ 68·γ·ΔF` (γ = 0,5 ⇒ `F_p ≲ 34 N`); trên thì điện trở nguồn cao làm **mux không kịp ổn định ở 20 Hz**. **"Cửa sổ đó có rỗng không" chính là nội dung của GATE 0.**

> `100 kΩ / 10-bit / 1,51 mV` là **ngân sách thiết kế** trong `docs/04` §1, **không phải kết quả đo** — cấm dùng như số liệu.

**Đính chính một chỗ cũ trong README này:** bản trước viết "thiết kế **không dùng IMU**". Đúng hơn: **dấu gập/duỗi** lấy từ mẫu vách mà không cần encoder (đó là ý của `docs/01` §4), còn **góc và tốc độ kéo** thì **có** 6 IMU — vì `GAP = AROM − PROM` không định nghĩa được nếu không đo góc. Hai mệnh đề này không thay thế nhau.

Phân cấp thuật ngữ (bắt buộc dùng đúng): [`docs/bao_cao/GLOSSARY.md`](docs/bao_cao/GLOSSARY.md) — **vật liệu Velostat** ≠ **sensing element** (Velostat + đồng tự dính + cấu trúc sandwich) ≠ **mảng sensing element** ≠ **hệ thống cảm biến** (mảng + ESP32-S3 + firmware).

## 5. Ba đại lượng dẫn xuất và quy tắc đơn vị

| Đại lượng | Định nghĩa | Điều kiện phải in kèm | Đơn vị |
|---|---|---|---|
| **`EI`** (Effort Index) | `EI = median(\|d\|) / (1 + κ·\|v̂\|)`, `d` = đạo phổ ADC của mảng vách, `v̂` = vận tốc góc IMU | ngón · tốc độ kéo · hướng dẫn bằng giọng nói | **counts (không thứ nguyên)** |
| **`GAP`** | `AROM − PROM` trên cùng ngón, cùng phiên | do rig kéo ở **hai tốc độ đã hiệu chuẩn** | độ (thang IMU), **không** suy từ ADC |
| **`RAL`** | mức hỗ trợ **thực** / mức hỗ trợ **yêu cầu** | tải (g) · vị trí khớp · tốc độ, đo trên **rig** | không thứ nguyên ∈ [0,1] |

**Cấm trong mọi bảng số:** `ADC → newton` (không có load cell trên ngón; load cell chỉ là chuẩn đối chứng ở rig) · `ADC → độ` · dùng `RAL` như chỉ số lâm sàng.

## 6. Phương pháp: bộ kiểm chứng 10 ngưỡng

> Ngưỡng được viết ra và **đóng chốt trước khi có bất kỳ số liệu nào**, và **không** chỉnh lại sau khi thấy số. Một ngưỡng không đạt ⇒ báo cáo **fail** ở ngưỡng đó. Cấm viết "GATE 0 pass" khi `G0.1` hoặc `G0.7` fail (`research/protocols/08` §10.5).

| ID | Câu hỏi | Ngưỡng |
|---|---|---|
| **G0.0** | Chọn định nghĩa nhiễu **trước khi đo** | A: `noise_pp = max−min`/20 mẫu (tính tay được) · B: `σ`/≥5.000 mẫu (cần script) |
| **G0.1** 🎯 | Có tồn tại `F_p` vừa đủ nhạy vừa đủ ổn định? | ∃`F_p`: `R₀ ≤ R_max` **và** `SNR ≥ 8 LSB` tại `ΔF = 1 N` |
| G0.2 | Mảng có thật sự là áp kế? | `γ_i ≥ 0,25` ở ≥4/5 mảng, `R² ≥ 0,95` |
| G0.3 / G0.4 | Lặp lại giữa chu kỳ / giữa **ngày** | `CV ≤ 5 %` · `ICC(3 ngày) ≥ 0,75` |
| G0.5 / G0.6 | Đường lên có trùng đường xuống? Có bị lún khi giữ tải? | `hys_norm ≤ 15 %` · `creep_2dec ≤ 3 %` |
| **G0.7** 🎯 | Tín hiệu có trôi chậm hơn biên độ cần đo? | `drift_ratio ≤ 2` **và** trôi 10 ngày < `ΔV` tại `ΔF = 1 N` |
| G0.8 | Các mảng có đủ giống nhau để so sánh giữa ngón? | độ rải `γ ≤ ±40 %` |
| G0.9 | Cấu hình kênh đọc kịp không? | `fps_meas ≥ 20 Hz` trên 12 kênh |

🎯 = ô giết đề tài. **Cách chạy GATE 0 mà không cần một dòng code:** `research/protocols/08a` — phiếu in được, chuẩn lực là **khối lượng đã cân** (`F = m·g`, không trễ, không cần hiệu chuẩn điện tử), mọi phép tính chỉ là trừ số nguyên. Kế hoạch đầy đủ + cây fail: `research/protocols/08`.

## 7. Kế hoạch và ngân sách

```
Lớp 0 (GATE 0)    Mảng Velostat + đồng tự dính + jig in + khối lượng chuẩn + đồng hồ đo
                  ── chuẩn lực = F = m·g, KHÔNG cần load cell ──►  0,12–0,65 triệu đ
Lớp 1 (GATE A/B)  3 ngón (2, 3, cái) × 4 mảng = 12 mảng áp trở + 6 IMU + 12 flex
                  + CD74HC4067 → ESP32-S3 (12 bit, V_EX = 3,1 V, 20 Hz)  ► +0,57–1,50 triệu đ
Lớp 2 (GATE D/F)  Orange Pi 5 Pro (log nguồn thô + dashboard) + rig E4/E5 (vít me,
                  phanh từ, tải chuẩn) + phantom silicone          ► +1,10–2,50 triệu đ
Lớp 3 (lâm sàng)  IRB + bệnh viện + n ≥ 20                          ► CHƯA MỞ — ngoài đề cương
```

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

> **Bộ tiêu chí: ViSEF/ISEF**, không phải tạp chí kỹ thuật. Đề tài **không** có nguyên lý mới và không tự đo mình bằng chuẩn cần nguyên lý mới + dataset + đối chứng lâm sàng. Mọi nhận định "mới/không mới" phải kèm tên bộ tiêu chí (`DEC-NOV-001` chờ chủ dự án chốt mức).

| Hướng được coi là mới | Kiểm chứng ngược đã làm | Kết luận hiện hành |
|---|---|---|
| Vách cứng phân biệt hướng lực | Phần tử áp điện trở **trên vách** có từ **2015** (`SRC-SIDEWALL-PIEZO-2015`); vỏ cứng khớp nối + da áp điện trở **2026** (`SRC-ARTGLOVE-2026`, 2048 taxel, 22 DoF) | **Cải tiến cấu hình + cách lập luận**, không phải nguyên lý |
| Găng đo lực cho người đột quỵ | Đối thủ gần nhất: Lin et al., *Sensors* 2022;22(19):7212 — **19 IMU + 1 bóng áp lực**, n = 14, **có IRB** | Họ thắng về **học máy + cỡ mẫu**; đề tài phải thắng ở **cơ khí tạo phân tách + lớp tin cậy**, không ở số cảm biến |
| Găng có chức năng tập/hỗ trợ | ironHand (JRATE 2016 **và** J Rehabil Med 2018;50:598–606, n = 5, **không** dùng thiết bị đo lực chuẩn hoá làm kết quả chính) | Đề tài **bỏ** chức năng tác động để dồn vào phép đo |
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
| Nguồn đã vào sổ, có locator + mức đã đọc | **141** | `research/evidence/SOURCE_LEDGER.csv` |
| Tuyên bố, kèm cấp bằng chứng + hành động còn lại | **24** | `research/claims/CLAIM_LEDGER.csv` |
| Quyết định có ngày + chủ sở hữu + trạng thái | **34** | `research/context/DECISION_LOG.md` |
| Nhật ký truy vấn ngoài (**kể cả lần tìm không thấy**) | **81** | `research/queries/QUERY_LOG.jsonl` |
| Phiếu đo/thực nghiệm đã thiết kế, chưa chạy | **10 ngưỡng · 7 gate · 8 buổi bench** | `research/protocols/06`–`08a` |
| Số liệu đo của đề tài | **0** | `research/bench/logs/` — đang trống, và đó là trạng thái thật |

Quy tắc chống tự nâng cấp: **không** nâng mức bằng chứng; **một lần tìm không thấy = `UNVERIFIED`**, không phải "không tồn tại"; số liệu giả lập phải dán nhãn giả lập; agent đề xuất, **chủ dự án phê duyệt**. Toàn bộ ở [`AGENTS.md`](AGENTS.md).

## 11. Bản đồ repo

| Nhóm | File | Vai trò |
|---|---|---|
| **Nộp trường** | [`docs/DE_CUONG_NOP_TRUONG.md`](docs/DE_CUONG_NOP_TRUONG.md) | Đề cương hoàn chỉnh: 4 trụ + M1–M6 + ngân sách + hạn chế tự khai + Phụ lục A chống-claim |
| Đề tài | [`docs/01_Topic_Definition.md`](docs/01_Topic_Definition.md) | Tên đã chốt, vấn đề, khoảng trống, RQ1–R3, phạm vi (`A.4`: **không** phải thiết bị điều trị) |
| Lý thuyết | [`docs/02_Theoretical_Foundation.md`](docs/02_Theoretical_Foundation.md) | Sinh lý hồi phục, thang đo, cơ sinh học, vật liệu áp trở, mô hình §5.5, `EI`/`GAP`/`RAL`, INT8 |
| Prior art & sáng chế | [`docs/03_Literature_Gap_Analysis_Plan.md`](docs/03_Literature_Gap_Analysis_Plan.md) | Kế hoạch rà soát 2011–2026; §7 phương pháp tra cứu sáng chế + hồ sơ thất bại |
| Phần cứng | [`docs/04_Hardware_Architecture.md`](docs/04_Hardware_Architecture.md) | Kênh, MUX, ngân sách nhiễu/độ phân giải (**ngân sách thiết kế**, không phải kết quả) |
| Soạn thảo | [`docs/05_De_Cuong_Dang_Ky_DRAFT.md`](docs/05_De_Cuong_Dang_Ky_DRAFT.md) | **Outline nội bộ** (không nộp) + §8b các chỗ chủ dự án cần sửa |
| Mẫu báo cáo | [`docs/OUTLINE_BAOCAO_VISEFD.md`](docs/OUTLINE_BAOCAO_VISEFD.md) · [`docs/bao_cao/`](docs/bao_cao/) | Khung A/B/C + A.1–A.7 + GLOSSARY |
| Kiểm chứng | [`research/protocols/06`](research/protocols/06_glove_hand_GATE_experiment.md) · [`07`](research/protocols/07_ral_phantom_and_ktv_interview.md) · [`08`](research/protocols/08_gate0_execution_plan.md) · [`08a`](research/protocols/08a_gate0_bench_sheets.md) | Master 7 gate · RAL/phantom + phiếu tham khảo chuyên gia · kế hoạch GATE 0 · **phiếu đo in được, không code** |
| Vật tư & tiếp cận | [`research/context/EQUIPMENT_AND_ACCESS.md`](research/context/EQUIPMENT_AND_ACCESS.md) | Đã có / chưa chắc / cần mua + 4 bước chạy GATE 0 |
| Đánh giá chiến lược | [`research/reviews/2026-09-19_project_ceiling.md`](research/reviews/2026-09-19_project_ceiling.md) | Trần theo từng trục + **nguyên tắc giải ngân theo lớp** + quy tắc dừng |
| Benchmark | [`research/reviews/2026-09-19_benchmark_xe_lan_ALS_QG2025.md`](research/reviews/2026-09-19_benchmark_xe_lan_ALS_QG2025.md) | **Nội bộ.** Kiểm đếm một báo cáo từng giải Nhất quốc gia → định cỡ hình thức 15–20 trang, ≥1,3 ảnh/bảng mỗi trang. **Cấm trích trong hồ sơ nộp** (`DEC-SCOPE-003`) |
| Nhật ký đo | [`research/bench/logs/`](research/bench/logs/) | Một file mỗi buổi; **bản gốc không bao giờ bị sửa**; header nhắc lại ngưỡng đã chốt |
| Chỉ mục | [`INDEX.md`](INDEX.md) · [`research/README.md`](research/README.md) · [`AGENTS.md`](AGENTS.md) | Sơ đồ file, quy ước workspace, luật của repo |

## 12. Thiết lập & quy trình

Yêu cầu: Git, Python 3.10+, Bash.

```bash
python3 -m venv .venv && . .venv/bin/activate
python -m pip install --upgrade pip && python -m pip install -r requirements.txt
bash scripts/bootstrap_research_tooling.sh
python scripts/check_research_environment.py --strict
python scripts/build_context_bundle.py --budget-chars 40000     # -> research/generated/ (đã gitignore)
```

**Ba việc còn lại, đúng thứ tự:**

1. ☐ **Chủ dự án chốt 10 ô** `Chốt?` trong `research/protocols/08` §7 (việc này **không** ai làm thay được).
2. ☐ Chạy GATE 0 bằng `research/protocols/08a` → mỗi buổi = 1 file log + 8 ảnh; **kể cả buổi fail cũng phải lưu**.
3. ☐ Thay dự toán bằng **báo giá/hoá đơn thật** → `DEC-BUDGET-001`; chỉ khi đó mới xét giải ngân Lớp 1.

Luồng chuẩn cho mỗi thay đổi lớn: đọc `research/context/PROJECT_SNAPSHOT.md` → log truy vấn (`scripts/research_log.py`) → cập nhật `SOURCE_LEDGER`/`CLAIM_LEDGER` → chạy review protocol → cập nhật snapshot + `INDEX.md` → dựng lại bundle.

## 13. Đổi tên repo + metadata GitHub (chủ dự án chạy — agent không có quyền Administration)

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
| 2026-09-19 (lượt 4) | README dựng lại theo cấu trúc hồ sơ khoa học (luận điểm · RQ + điều kiện giết · nguyên lý · 10 ngưỡng · tự khai); đề xuất tên mới `DEC-TITLE-001`; điền 3/4 ô danh tính của đề cương; `DEC-DOC-001` |
| 2026-09-19 (lượt 3) | Đề cương nộp `docs/DE_CUONG_NOP_TRUONG.md`; sửa 2 lỗi trích dẫn trong `A.1`; thi hành `DEC-ROLE-001` (không nêu danh tính người được tham khảo) |
| 2026-09-19 (lượt 1–2) | Prior art lượt 1–2 (novelty dịch từ cơ chế sang lớp thống kê); GATE 0 plan + phiếu đo không code; đánh giá trần dự án + mức đầu tư theo lớp |
