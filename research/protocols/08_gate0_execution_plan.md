# 08 — KẾ HOẠCH CHẠY GATE 0 (đặc trưng sensing element + cửa sổ làm việc)

> **Mục đích file:** `research/protocols/06…` định nghĩa GATE 0 ở mức *tiêu chí*. File này định nghĩa **cách chạy**, để một người bất kỳ
> (kể cả chủ dự án lúc 22h, không có AI) làm đúng một lần và không phải tự quyết định giữa chừng.
> **Trạng thái:** bản đề xuất của agent, **chờ chủ dự án duyệt** (`DEC-GATE0-001`, chưa tồn tại → tạo khi duyệt).
> **Công cụ đo:** phiếu in được từng bảng ở [`08a_gate0_bench_sheets.md`](08a_gate0_bench_sheets.md) — thiết kế cho **DMM + khối lượng đã cân**, phép tính chỉ gồm trừ số nguyên.
> **Ràng buộc:** giai đoạn này **không viết script phân tích, không viết firmware** (`DEC-PHASE-001`); không đo trên người; ngưỡng **chốt trước khi đo**, cấm chỉnh sau khi thấy số.
> **Không có số nào trong file này là kết quả đo của đề tài.**

---

## 1. Câu hỏi GATE 0 thật ra là hai câu, phải tách ra

| # | Câu hỏi | Số cần lấy | Quyết định |
|---|---|---|---|
| **Q1** | Vật liệu + cấu trúc có cho **độ nhạy** đủ lớn so với nỗ lực cần đo không? | `γ = −dlnR/dlnF`, `ΔV` tại `ΔF = 1 N`, nhiễu nền `σ_V` | Nếu không → mọi cổng sau vô nghĩa |
| **Q2** | Có tồn tại **mức preload nào** mà mạch đọc thật (ESP32-S3 + CD74HC4067) còn phân giải được tín hiệu ấy không? | `R₀(F_p)` và `R_max` (ngưỡng trở nguồn đo được, không đoán) | Đây là **cửa sổ 2 đầu** ở `docs/02` §5.5 — GATE 0 sinh ra chủ yếu để trả lời câu này |

> **Điểm dễ sai nhất:** nếu chỉ đo "cảm biến có nhạy không" (Q1) mà bỏ Q2, đề tài có thể chế tạo được phần tử tốt nhưng **mạch đọc không nghe thấy**,
> và lỗi bị quy nhầm cho Velostat. Vì vậy §3 đặt `R_max` làm thí nghiệm độc lập, đo bằng hộp điện trở thập, **trước khi** chế tạo găng.

---

## 2. Mẫu: **hai họ**, vì phải quy được lỗi cho vật liệu hay cho cơ khí

| Họ | Là gì | Số lượng | Dùng để trả lời |
|---|---|---|---|
| **A — phẳng** | 2 bản đồng tự dính + 1 patch Velostat, ép giữa 2 phiến acrylic phẳng | **5** phần tử (ký hiệu `A1…A5`), mỗi phần tử **làm ở 2 lần chế tạo khác ngày** | `γ`, hysteresis, creep, độ nhất quán *chế tạo* — vật liệu thuần |
| **B — vách + khung** | patch Velostat dán trên **vách nghiêng 45°** của khung in 3D, có ốc preload + chốt hành trình | **5** cụm (`B1…B5`) | `γ` của **cả cụm**, `R₀(F_p)`, CV khi nén bằng vít, và ảnh hưởng **độ mềm của khung** |
| **C — đối chứng cơ khí** | cụm B **không có Velostat** (2 bản đồng tiếp xúc/mock), chỉ đo xem khung bị lún bao nhiêu | 2 cụm | Loại trừ khả năng "tín hiệu đến từ khung dẻo, không phải từ vật liệu" |

**Kiểm soát chế tạo (bắt buộc ghi vào log):** diện tích patch (đo bằng thước cặp, sai số ±0,1 mm), số lớp Velostat, kích thước bản đồng, lực ép khi dán,
nhãn lô vật liệu, ngày giờ chế tạo. Hai phần tử **không được phép** khác nhau ở 1 biến không ghi lại.

**Giả định hình học để thiết kế, không phải để báo cáo:** patch `8 mm × 12 mm`, `A_c ≈ 9,6·10⁻⁵ m²` (`docs/02` §5.5) — **đo lại thật**, giá trị đo mới là số dùng sau này.

---

## 3. Thí nghiệm Q2 trước: đo `R_max` của **mạch đọc thật** (nửa ngày, không cần Velostat)

Đây là phép đo rẻ nhất và giá trị nhất trong cả GATE 0.

**Mạch:** `Vcc — R_sensor(mô phỏng bằng hộp điện trở thập) — R_ref — GND`, điểm giữa vào `CD74HC4067` → `ADC1` của ESP32-S3; song song là **DMM** làm tham chiếu.

**Quét có chủ đích:**
1. `R_series ∈ {100 Ω, 1 k, 10 k, 100 k, 500 k, 1 M, 2 M, 5 M, 10 M}` — mỗi giá trị ghi `adc_raw` và `V_DMM`; tính `e = |V_adc − V_DMM|`.
2. Với **mỗi** `R_series`, quét `adc_atten ∈ {0 dB, 2,5 dB, 6 dB, 11 dB}` × `adc_clock ∈ {1 RC_FAST, 1 RC_SLOW, 2 RC_FAST, 8 RC_SLOW}` × `bit_width ∈ {12, 9}` — chính 3 tham số này (không phải "12-bit") quyết định tốc độ lấy mẫu và trở nguồn cho phép.
3. `R_ref` đặt ở 3 mức: `0,1·R_series`, `1·R_series`, `10·R_series` → tìm cấu hình divider tốt nhất.
4. **ENOB thật:** ngắn `R_sensor = 0 Ω`, lấy ≥ 5.000 mẫu liên tiếp ở mỗi cấu hình, ghi σ (theo LSB và theo mV) → `ENOB = log₂(V_FS/σ·k)` với `k` do chủ dự án chốt (§7). Không có ENOB thật thì **cấm** dùng "12-bit" như một con số độ phân giải.

**Biến thể chạy được ngay nếu chưa có CD74HC4067** (kiểm kê 2026-09-19: board có thể là món duy nhất còn thiếu): tách §3 thành **§3.1 — chỉ ESP32-S3 trực tiếp** (ngõ vào nối thẳng qua R_series, đo `e` và σ → cho **ENOB** và `R_max(ADC)` riêng), rồi **§3.2 — thêm MUX** khi linh kiện về để có `R_max(ADC+MUX)`; chỉ số `R_max` dùng ở `G0.1` là giá trị **nhỏ hơn** của hai phép (an toàn hơn). §4 (đặc trưng phần tử) **không** bị chặn bởi §3.2.

**Định nghĩa để dùng (không đổi sau khi đo):** `R_max` = giá trị `R_series` lớn nhất mà tại đó
`e ≤ 1 LSB` **và** σ không vượt quá 2× σ ở `R_series = 100 Ω` **và** tỉ lệ khung `fps ≥` mức chủ dự án chốt ở §7.
→ Đây chính là `R_max(ADC+MUX)` trong `docs/02` §5.5, biến một **hằng số đi mượn** (100 kΩ) thành **số đo của đề tài**.

---

## 4. Thí nghiệm Q1 — đặc trưng vật liệu/cụm

**Dụng cụ:** bệ nén (ren M5 + lò xo + êcu hãm), **quả cân chuẩn** (tham chiếu lực — vì `F = m·g` chính xác hơn lực kế lò xo), DMM 4 dây (đo `R`),
thước cặp, nhiệt–ẩm kế, kẹp cố định. Tốc độ nén **quasi-tĩnh (≤ 1 mm/s)** cho toàn bộ §4.1–4.3; §4.4 là mục kiểm tra tốc độ riêng.

### 4.1 Đường cong tăng/giảm (`γ`, hysteresis)
- Tải: `F ∈ {0, 1, 2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128 N}` — **mức tải 2 chiều, mỗi mức giữ 10 s, lấy trung bình 5 số đọc liên tiếp**.
- Mỗi phần tử chạy **3 vòng** (tăng → giảm) liên tiếp, nghỉ 60 s giữa vòng.
- Ghi `R` (DMM 4 dây) **và** `adc_raw` **và** `fps` thực tế ở mọi điểm.
- Xử lý (sau này, bằng script **chưa viết**): hồi quy `ln R = ln R₀ − γ ln F` trên đoạn `4…64 N`; `γ` là **slope**, không phải hằng số giả định.
- `ΔR_hys(F)` = hiệu `R` ở cùng `F` giữa nhánh tăng và nhánh giảm, chuẩn hoá theo `R(F_min) − R(F_max)` của cùng vòng.

### 4.2 Creep và hồi phục
- Giữ tải cố định **600 s** (không phải 60 s — 60 s không đủ để thấy dạng log-time) tại `F = 16 N` và `F = 48 N`: `ΔR/R` theo mỗi thập phân thời gian (10 s / 100 s / 600 s).
- Thôi tải, ghi 600 s: **thời gian hồi phục tới 90%** giá trị nghỉ → con số này quyết định **nghỉ bao lâu giữa các lần đo** ở GATE A/B/C.

### 4.3 Độ lặp lại
- **Trong phiên:** cùng tải 20 lần lặp (nâng–hạ vít), tính CV.
- **Giữa 3 ngày:** cùng phần tử, cùng tải, mỗi ngày 5 lần.
- **Giữa 5 phần tử họ A và 5 cụm họ B:** cùng tải → nếu `γ` trải rộng hơn ±40% thì **quy trình chế tạo** là nút thắt, không phải vật liệu (ghi rõ kết luận đó, nó là kết quả hợp lệ).
- Preload của cụm B: `F_p ∈ {0, 5, 10, 20, 40, 60, 80 N}` — **đây là biến số chính của Q2**: với mỗi `F_p` ghi `R₀(F_p)` (để so `R_max`) và `ΔV` tại `ΔF = 1 N`.

### 4.4 Kiểm tra tốc độ (chuẩn bị cho E4 và `EI_v`)
- `F = 16 N` áp ở **2 tốc độ** ≈ 0,2 mm/s và ≈ 2 mm/s, mỗi tốc độ 10 lần, cùng phần tử.
- Câu hỏi duy nhất: `ΔV` có đổi quá `3σ` giữa 2 tốc độ không? Nếu có → **mọi chỉ số ở GATE A/B/C phải ghi kèm tốc độ** và dùng dạng `EI_v`
  (đó là điều `SRC-TW-SPASTICITY-2022` buộc ta dự phòng; `docs/02` §5.5).

### 4.5 Trôi dài ngày (bắt buộc, vì GATE C sống hay chết ở đây)
- **2 cụm B** giữ nguyên preload `F_p = 20 N`, ghi liên tục **≥ 10 ngày** (mẫu cách ≤ 60 s, kèm `T`, `RH`), **không** có bất kỳ thao tác nào.
- Không hiệu chỉnh trôi trong suốt thời gian này (quy tắc đã ghi ở `research/protocols/06` E1).
- Kết quả cần: `drift_peak_to_end / σ_ngày` và `drift / (ΔV của ΔF = 1 N)` → tỉ số này **là** nội dung định lượng của GATE C trên giấy.
- **Bản thay thế khi chưa có firmware (`DEC-PHASE-001`):** không ghi liên tục 60 s được → dùng **3 lần/ngày × 10 ngày**, mỗi lần trung vị 5 số đọc (`08a` §7). So sánh với `trôi / Δadc(1 N)` thay cho `trôi / σ_ngày`; σ ngày khi đó lấy bằng `noise_pp` nhân √(số lần/ngày) — **phải chọn một định nghĩa trước khi đo**, không đổi sau.

---

## 5. Định nghĩa số phải dùng (viết **trước** khi đo)

| Đại lượng | Định nghĩa |
|---|---|
| `γ_i` | slope hồi quy `ln R` theo `ln F`, đoạn 4–64 N, phần tử thứ *i* |
| `SNR(F_p, ΔF)` | `ΔV / σ_V` với `σ_V` lấy ở **cùng preload, không tải**, đơn vị **LSB** — không nhân ra vôn, không nhân ra niutơn |
| `hys_norm` | `max_F ΔR_hys(F) / (R(F_min) − R(F_max))`, cùng vòng |
| `creep_2dec` | `ΔR/R` giữa mốc 10 s và 100 s, tải giữ không đổi |
| `R₀(F_p)` | `R` ở trạng thái nghỉ **có** preload `F_p` (DMM 4 dây) |
| `cv_day` | hệ số biến thiên của `R₀` qua 3 ngày |
| `drift_ratio` | `(R₀(ngày 10) − R₀(ngày 1)) / σ_ngày` |
| `fps_meas` | trung vị số khung/giây của **10 đoạn 60 s** (không phải tốc độ danh định của sketch) |

---

## 6. Ma trận thí nghiệm & lịch (ước lệ, ~3 tuần lịch, 12–14 ngày công)

| Ngày | Việc | Ghi chú |
|---|---|---|
| D0 | Dán/nhận mẫu, đo kích thước, đánh số, chụp ảnh từng phần tử | ảnh = bằng chứng chế tạo |
| D1 | **§3** đo `R_max` + ENOB + quét cấu hình ADC | chưa cần Velostat; làm 1 buổi |
| D2–D3 | §4.1 + §4.2 cho họ A (A1…A5) | mỗi phần tử ~70 phút |
| D4 | Lắp cụm B, đo `R₀(F_p)` (§4.3 phần preload) | |
| D5–D7 | §4.1 + §4.3 cho họ B; §4.5 **khởi động** log 10 ngày | bắt đầu sớm để log chạy nền |
| D8 | §4.4 kiểm tra tốc độ | |
| D9 | Ngày dự phòng (hỏng jig / dán lại patch) | |
| D15–D16 | Chốt §4.5, đọc kết quả, **đối chiếu ngưỡng đã chốt ở D0** | |
| D17 | Viết `research/reviews/2026-…-gate0-results.md` + bảng vào `docs/02` §5.5 (thay số mượn bằng số đo) | |

---

## 7. Ngưỡng PASS/FAIL — **ĐỀ XUẤT, CHỦ DỰ ÁN CHỐT TRƯỚC KHI ĐO**

> Agent **không** chốt ngưỡng (`DEC-SCOPE-003`). Ô "Chốt?" để trống cho chủ dự án; khi điền xong thì in/dán ảnh trang này **trước** khi bật nguồn.

| # | Tiêu chí (đề xuất) | Ngưỡng đề xuất | Chốt? |
|---|---|---|---|
| G0.1 | **Cửa sổ Q2 tồn tại** | ∃ ít nhất 1 mức `F_p` sao cho `R₀(F_p) ≤ R_max` **và** `SNR ≥ 8 LSB` tại `ΔF = 1 N` | ☐ |
| G0.2 | Vật liệu đủ nhạy | `γ_i ≥ 0,25` ở **≥ 4/5** phần tử họ A **và** R² hồi quy ≥ 0,95 | ☐ |
| G0.3 | Lặp trong phiên | `cv_cycle ≤ 5%` ở tải làm việc | ☐ |
| G0.4 | Lặp giữa ngày | ICC(3 ngày) ≥ 0,75 | ☐ |
| G0.5 | Hysteresis **biết được** (không cần nhỏ) | `hys_norm` đo được và `≤ 15%` **để vẫn dùng được cho chỉ số thứ hạng** | ☐ |
| G0.6 | Creep | `creep_2dec ≤ 3%` | ☐ |
| G0.7 | Trôi so với tín hiệu | `drift_ratio ≤ 2` **và** trôi 10 ngày < `ΔV(ΔF = 1 N)` | ☐ |
| G0.8 | Nhất quán chế tạo | trải `γ` giữa 5 phần tử ≤ ±40% | ☐ |
| G0.9 | Tốc độ đọc đủ cho GATE A/B | `fps_meas ≥ 20 Hz` với 12 kênh đã cấu hình | ☐ |
| **G0.0** (mới) | **Chọn định nghĩa nhiễu trước khi đo** | **Bản A** (đo tay được): `noise_pp = max−min` trên 20 mẫu liên tiếp, ngưỡng `Δadc ≥ 8` và `e ≤ 1 LSB` **hoặc** **Bản B** (cần script): `σ` trên ≥ 5.000 mẫu — *chủ dự án tích vào một ô; chọn B đồng nghĩa phải mở khoá script* | **A ☐ / B ☐** |

**Đọc bảng:** G0.1 **và** G0.7 là hai ô quyết định sự sống còn; G0.2–G0.6, G0.8 là ô *giải thích được* nếu G0.1 fail; G0.9 chỉ chặn đường đi tiếp sang GATE A.

---

## 8. Cây quyết định khi fail (viết trước, để lúc đó không "cố cứu")

```
G0.1 fail vì R₀(F_p) > R_max mọi F_p            → KHÔNG phải lỗi vật liệu.
   Lối thoát 1: đệm follower (JFET/OPA) trước MUX; đo lại §3. 1 buổi.
   Lối thoát 2: tăng R_ref, giảm băng thông, fps thấp hơn (chấp nhận fps_meas nhỏ hơn) — ghi rõ đánh đổi.
   Lối thoát 3: đổi topology — áp trở thành phần tử **kéo** (dải dọc ngón) thay vì nén trên vách; quay về docs/02 §5.5 với mô hình khác.

G0.1 fail vì SNR < 8 LSB (R₀ nhỏ, ΔV quá nhỏ)   → cửa sổ 2 đầu **rỗng giữa** (vùng đủ nhạy nằm ngoài vùng đọc được).
   Lối thoát 1: tăng ΔF đo được bằng cách **giảm F_p tối thiểu có thể** + tăng `A_c` (đổi cơ khí, không đổi vật liệu).
   Lối thoát 2: hạ yêu cầu: không đo "nỗ lực khi chưa cử động" → **bỏ Effort Index + mọi câu về ý định** (đúng án lệ §5.4), chỉ còn AROM/PROM.
   Lối thoát 3: dùng cấu hình **24 kênh vi sai** (docs/04) để trung bình nhiều phần tử trên cùng một ngón → SNR lên theo √n_eff nhưng mất độ phân giải không gian; phải nêu đánh đổi.

G0.7 fail (trôi > tín hiệu)                       → không có longitudinal. Bỏ M4/GATE C, hạ đề tài về "báo cáo trong phiên";
                                                    nói thẳng trong báo cáo rằng áp trở polymer tự chế **không** đủ ổn định để theo dõi theo tuần.
G0.3/G0.8 fail                                    → quy cho quy trình chế tạo: làm lại 5 phần tử với 1 biến được kiểm soát, **không** đổi ngưỡng.
```

---

## 9. Định dạng log (schema — viết ra để sau này script khớp, **chưa viết script**)

```
session_id,date,start_iso,end_iso,element_id,family,cfg_atten,cfg_clock,bit_width,
R_ref_ohm,R_series_ohm,F_applied_N,step_index,branch(up|down),t_offset_s,
adc_raw,adc_avg5,volt_mv_DMM,R_dmm_ohm,fps_actual,T_c,RH_pct,operator,note
```
- Một file **một phiên**, tên `research/bench/logs/YYYY-MM-DD_G0_<element>_<loại>.csv`; file gốc **không bao giờ bị sửa** (bản dẫn xuất để phân tích đặt tên `…_derived.csv`).
- Đầu mỗi file có **header comment** (`#`) chép lại: ngưỡng đã chốt ở §7 (bản in/ảnh chụp), số serial DMM, và dãy thứ tự tải ngẫu nhiên.
- Dãy tải ngẫu nhiên: **chủ dự án tự viết tay** 1 dãy hoán vị của §4.1 rồi chụp ảnh, dán vào log trước khi đo (không để AI sinh dãy — dãy sinh sau khi thấy số là hành vi bị cấm).

## 10. Cấm trong GATE 0 (lặp lại cho chắc, theo `AGENTS.md`)
1. Nói "ADC 12-bit ⇒ độ phân giải 0,x mV ⇒ 0,y N" — không có phép đổi đơn vị nào được phép trước khi có `γ` + `ENOB` + mặt nạ lực.
2. Gọi "cảm biến Velostat" — phải là "sensing element dùng vật liệu áp trở".
3. Đưa tay người vào jig "cho nhanh". Không có ngoại lệ.
4. Chỉnh ngưỡng §7 sau khi đã thấy số; hoặc loại điểm dữ liệu vì "trông lạ" mà không ghi lý do vào `note`.
5. Viết "GATE 0 pass" khi chỉ có G0.3–G0.6 pass mà **G0.1 hoặc G0.7 fail**.

## 11. Câu chốt phải trả lời được sau GATE 0 (đúng 3 câu, cho báo cáo)
1. **Cửa sổ làm việc có rỗng không**, và biên của nó do **trở nguồn** hay do **tín hiệu nhỏ** quyết định?
2. `γ` thật của phần tử ta chế tạo là bao nhiêu, trải ra sao giữa 5 phần tử — so với giả định `0,5` của `docs/02` §5.5?
3. Trôi 10 ngày của chính hệ đo **nhỏ hơn** tín hiệu của `ΔF = 1 N` hay không? (nếu không, GATE C sẽ fail — và điều đó biết **trước** khi tốn 3 tuần)
