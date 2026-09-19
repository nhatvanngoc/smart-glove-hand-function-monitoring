# 08a — PHIẾU ĐO GATE 0 (bản in được · **không cần máy tính, không cần firmware**)

> **Dùng khi nào:** ngay khi 9 ngưỡng `…/08_gate0_execution_plan.md` §7 được chốt. In 1 phiếu/mã phần tử/điều kiện.
> **Tại sao tồn tại file này:** chủ dự án chốt giữ pha lý thuyết → **chưa viết script, chưa viết firmware**. Nhưng GATE 0 **không** cần cả hai:
> mọi đại lượng ở đây đo bằng **DMM + cân nhà bếp + đồng hồ bấm giờ**, và mọi phép tính yêu cầu chỉ là **trừ số nguyên** và **so sánh**.
> **Quy tắc ghi chép:** viết bút mực; sai thì **gạch một lần, viết giá trị mới, ký nháy bên cạnh** — không tẩy, không viết đè. Lý do: hội đồng có thể yêu cầu xem bản gốc.
> **Không có ô nào ở đây là "kết quả của đề tài"** cho tới khi ngưỡng §7 đã chốt và số liệu được chép vào `research/bench/logs/`.

---

## 0. Khối lượng ↔ lực (không phải tính ở bàn đo)

`F = m · g`, lấy `g = 9,81 m/s²`. Khối lượng 102 g cho **đúng ~1,0 N** → dùng làm bước `ΔF = 1 N` (Δ = 2 %, chấp nhận được; ghi chú vào phiếu nếu dùng vật khác).

| `m` [g] | 25 | 51 | 102 | 204 | 306 | 510 | 1020 | 1530 | 2040 | 3060 | 4080 | 6120 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `F` [N] | 0,25 | 0,5 | 1,0 | 2,0 | 3,0 | 5,0 | 10,0 | 15,0 | 20,0 | 30,0 | 40,0 | 60,0 |

> Tải nặng hơn 60 N: chồng thêm khối lượng đã cân, và ghi tổng `m` (đừng đoán). Nếu phần tử đã tới giới hạn hành trình: ghi `HẾT HÀNH TRÌNH` vào cột ghi chú, **vẫn giữ dòng đó**.

---

## 1. Đầu phiếu (điền một lần cho mỗi phần tử)

| Mục | Giá trị |
|---|---|
| Ngày / người đo | |
| Mã phần tử (A1…A5 / B1…B5 / C1, C2) | |
| Họ + mô tả chế tạo (số lớp Velostat, `A_c` đo bằng thước cặp = ___ mm × ___ mm) | |
| Cấu hình ADC: `atten` ___ dB · `clock` ___ · `bit_width` ___ · `R_ref` ___ kΩ | |
| DMM: model ___ · 2 dây / **4 dây** · dải ___ | |
| Nhiệt độ ___ °C · Ẩm ___ %RH | |
| Ảnh chụp trang §7 `protocols/08` **đã chốt ngưỡng** (dán/số ảnh) | |
| Dãy tải ngẫu nhiên viết tay (chụp ảnh, dán vào log) | |

---

## 2. Bảng B.1 — Đường cong tăng/giảm (mỗi phần tử, 3 vòng)

Với mỗi tải: đặt tải → đợi **10 s** → ghi **5 số đọc liên tiếp** của `adc_raw` và 1 giá trị `R` (DMM). Không chỉnh gì giữa các mức.

| Vòng | Chiều | `m` [g] | `F` [N] | `adc_raw` 1 | 2 | 3 | 4 | 5 | `R` DMM [kΩ] | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ↑ | 0 | 0 | | | | | | | |
| 1 | ↑ | 51 | 0,5 | | | | | | | |
| 1 | ↑ | 102 | 1,0 | | | | | | | |
| 1 | ↑ | 204 | 2,0 | | | | | | | |
| 1 | ↑ | 510 | 5,0 | | | | | | | |
| 1 | ↑ | 1020 | 10,0 | | | | | | | |
| 1 | ↑ | 2040 | 20,0 | | | | | | | |
| 1 | ↑ | 3060 | 30,0 | | | | | | | |
| 1 | ↑ | 4080 | 40,0 | | | | | | | |
| 1 | ↑ | 6120 | 60,0 | | | | | | | |
| 1 | ↓ | *(lặp lại ngược từ 60 N về 0)* | | | | | | | | |
| 2 | ↑↓ | *(như vòng 1, nghỉ 60 s giữa hai vòng)* | | | | | | | | |
| 3 | ↑↓ | *(như vòng 1)* | | | | | | | | |

**Tính ngay trên phiếu (chỉ trừ số nguyên):** với mỗi mức tải, `nhịp_adc = max(5 số) − min(5 số)` → ghi vào cột cuối. Đây là `noise_pp` (mục 5 dưới đây) — **số duy nhất** cần thiết để xử lý `G0.1` mà không cần tính trung bình/phương sai.

## 2b. Bảng B.2 — Hệ số `γ` (làm sau, bằng tay, trên giấy nháp)

Với các điểm từ 5 N tới 40 N ở vòng 1: kẻ `lg(R)` và `lg(F)`, vẽ 2 điểm ngoài cùng, `γ ≈ (lgR₁ − lgR₂) / (lgF₂ − lgF₁)`.
*Không cần hồi quy để biết γ có gần 0,5 hay không; nếu 5 phần tử cho γ trải quá ±40% → ô `G0.8` fail và **kết luận nằm ở quy trình chế tạo** — đó là một kết quả, không phải thất bại.*

---

## 3. Bảng B.3 — Creep và hồi phục (2 mức tải)

Giữ tải không đổi, bấm giờ, ghi `R` DMM tại các mốc. **Không chỉnh tải, không chạm vào bệ** trong suốt thời gian đo.

| Mốc | `t` [s] | 0 | 10 | 20 | 30 | 60 | 120 | 300 | 600 |
|---|---|---|---|---|---|---|---|---|---|
| `F = 16 N` (≈1,63 kg) — `R` [kΩ] | | | | | | | | | |
| `F = 48 N` (≈4,9 kg) — `R` [kΩ] | | | | | | | | | |
| **Hồi phục** sau khi thôi tải — `R` [kΩ] | 0 | 10 | 60 | 120 | 300 | 600 | | | | |
| `R` nghỉ trước khi đo (để so) | | | | | | | | | |

**Đọc trên phiếu:** `creep_2dec = (R₁₀₀ₛ − R₁₀ₛ) / R₁₀ₛ` (lấy từ cột 10 s → 120 s, chia cho `R` tại 10 s; nhân 100 = %). Ngưỡng đề xuất `≤ 3 %`.

---

## 4. Bảng B.4 — Thang preload (chỉ họ B) → **bảng quan trọng nhất của GATE 0**

Với mỗi `F_p`: ghi `R₀`, rồi **thêm đúng 102 g** (≈1 N) và ghi `adc_raw` trung vị của 5 mẫu ở mỗi trạng thái.

| `F_p` [N] | `m_p` [g] | `R₀` DMM [kΩ] | `R` khi +1 N [kΩ] | `adc_raw` nghỉ | `adc_raw` +1 N | **`Δadc` (counts)** | `noise_pp` | `Δadc ≥ 8`? | `R₀ ≤ R_max`? |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | | | | | | | ☐ | ☐ |
| 5 | 510 | | | | | | | ☐ | ☐ |
| 10 | 1020 | | | | | | | ☐ | ☐ |
| 20 | 2040 | | | | | | | ☐ | ☐ |
| 40 | 4080 | | | | | | | ☐ | ☐ |
| 60 | 6120 | | | | | | | ☐ | ☐ |
| 80 | 8160 | | | | | | | ☐ | ☐ |

> **Đây chính là `G0.1`:** ô "ĐỦ" tích được khi **có ít nhất một dòng** mà cả hai cột ☐ đều đạt. Không có dòng nào → cửa sổ **rỗng**, và đó là một kết luận khoa học (xem cây quyết định `protocols/08` §8), không phải "thí nghiệm hỏng".

---

## 5. Bảng B.5 — Quét trở nguồn (§3): `R_max` của mạch đọc

Không cần Velostat. Nối `Vcc — R_series — R_ref — GND`, điểm giữa vào ADC (và sang MUX nếu đã có `CD74HC4067`).

| # | `R_series` | `V_adc` [mV] | `V_DMM` [mV] | **`e = |V_adc − V_DMM|`** [mV] | `nhịp_adc` 20 mẫu liên tiếp (max−min) | fps đếm tay trong 10 s × 6 lần |
|---|---|---|---|---|---|---|
| 1 | 100 Ω | | | | | |
| 2 | 1 kΩ | | | | | |
| 3 | 10 kΩ | | | | | |
| 4 | 100 kΩ | | | | | |
| 5 | 500 kΩ | | | | | |
| 6 | 1 MΩ | | | | | |
| 7 | 2 MΩ | | | | | |
| 8 | 5 MΩ | | | | | |
| 9 | 10 MΩ | | | | | |

**Định nghĩa dùng được mà không cần script (chọn 1 và ghi vào §7 TRƯỚC khi đo — agent không chọn giúp):**
- **Bản A (đề xuất, đo tay được):** `R_max` = `R_series` lớn nhất sao cho `e ≤ 1 LSB` (LSB = `V_FS / 2^bit`, tra ở chân phiếu) **và** `nhịp_adc ≤ 2 × nhịp_adc` ở dòng 100 Ω.
- **Bản B (đúng thống kê hơn, cần script):** `e ≤ 1 LSB` **và** `σ ≤ 2σ(100 Ω)` với σ tính trên ≥ 5.000 mẫu → **hoãn**, chỉ chạy khi chủ dự án mở khoá giai đoạn script.

---

## 6. Bảng B.6 — Hai tốc độ (chuẩn bị cho `EI_v` và rig E4)

| Lần | Tốc độ | `F` đỉnh [N] | `adc_raw` max | `adc_raw` nền | `Δadc` | Ghi chú (tiếng kêu, trượt, rung) |
|---|---|---|---|---|---|---|
| 1–5 | chậm (~0,2 mm/s — đếm nhẩm 5 s cho 1 mm) | 16 | | | | |
| 6–10 | nhanh (~2 mm/s — 0,5 s cho 1 mm) | 16 | | | | |

Câu hỏi duy nhất: `Δadc` hai nhóm có lệch nhau **vượt 3 lần `noise_pp`** không? Có → mọi chỉ số ở GATE A/B/C **phải ghi kèm tốc độ** (`F_spastic ≈ b·v` — `docs/02` §3.4, §5.5).

---

## 7. Bảng B.7 — Trôi nhiều ngày, **bản không firmware** (thay cho bản ghi liên tục 60 s)

Bản liên tục cần firmware → **chưa được phép viết**. Bản tay dưới đây đủ để xét `G0.7`:

| Ngày | Lần đo | `R₀` [kΩ] (trung vị 5 số) | `adc_raw` nghỉ | `T` °C | `RH` % | Ghi chú (có chạm vào jig không?) |
|---|---|---|---|---|---|---|
| 1 | sáng / trưa / tối | | | | | |
| 2 … 10 | *(nhân bản bảng này, 3 lần/ngày × 10 ngày = 30 dòng)* | | | | | |

**Đọc trên phiếu:** `trôi = |R₀(ngày 10) − R₀(ngày 1)| / R₀(ngày 1)` × 100 %.
So với `Δadc` của cột **ΔF = 1 N** ở bảng B.4: nếu **trôi > tín hiệu** → `G0.7` fail → **GATE C chết trên giấy**, và ta biết điều đó sau 10 ngày chứ không phải sau 6 tuần chế tạo cả găng. **Đây là dòng rẻ nhất để tránh mất 3 triệu đồng.**
Điều kiện ràng buộc: **không** hiệu chỉnh trôi trong 10 ngày; **không** chạm/siết lại jig; nếu phải chạm → ghi vào cột ghi chú và đánh dấu dòng đó `LOẠI (lý do: ...)`.

---

## 8. Ảnh phải chụp trong lúc đo (làm sau không chụp lại được)

| # | Ảnh | Dùng cho ô báo cáo |
|---|---|---|
| 1 | 5 phần tử A cạnh nhau, có thước kẻ (thấy `A_c`) | B.1 phương pháp + §6 sản phẩm |
| 2 | DMM 4 dây đang kẹp vào phần tử, hiển thị số | "chúng tôi đo bằng gì" |
| 3 | bệ nén + chồng khối lượng ở `F_p = 20 N` | ảnh "thiết bị đang chạy" — **ô bắt buộc** |
| 4 | cụm B thấy vách 45° + ốc preload + êcu hãm | giải thích cơ chế (thứ ta khác SenGlove/CN'366) |
| 5 | mặt đồng hồ/`adc_raw` đổi khi thêm 102 g | bằng chứng trực quan "1 N nhìn thấy được" |
| 6 | bảng phiếu **đã điền kín, có chữ ký** | phản biện "số liệu từ đâu ra" |
| 7 | mẫu C (không có Velostat) trên cùng jig | bằng chứng "tín hiệu không đến từ khung dẻo" |
| 8 | dao động `adc_raw` khi **không** tải (chuỗi 20 số viết tay) | ảnh `noise_pp`, nền của mọi claim SNR |

---

## 9. Bốn điều **không** làm trên phiếu này
1. **Không** đổi `adc_raw` thành N hay thành °. `Δadc` là counts, hết. (Mọi con số newton phải qua `research/protocols/03` — chưa chạy.)
2. **Không** viết "đạt PASS" khi §7 chưa được ký chốt. Trên phiếu chỉ được ghi **số** và **∕** so với ngưỡng in ở đầu phiếu.
3. **Không** loại điểm ngoại lai bằng cách xoá. Gạch + ghi lý do + giữ lại giá trị cũ đọc được.
4. **Không** gọi thứ đang đo là "cảm biến găng tay". Ở GATE 0 nó là **sensing element trên jig** — chưa có găng, chưa có ngón tay, chưa có người.
