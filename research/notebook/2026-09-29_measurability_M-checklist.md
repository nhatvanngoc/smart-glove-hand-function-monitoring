# Sổ tay NCKH — 2026-09-29: Xử lý checklist M-01..M-27 + khả năng đo của bộ đồ nghề

> **Ủy quyền:** owner (chat 2026-09-29): *"xem các chỉ số có thể đo được không, nếu không thì loại bỏ… dưới 10 triệu là được… đề tài hoạt động theo E2E (không đưa vào báo cáo mà cập nhật sổ tay nckh)"*.
> **Quy tắc tài liệu:** mọi quyết định dưới đây ghi vào **sổ tay** (`research/`); **báo cáo chính thức không đụng** cho tới khi owner duyệt riêng từng mục.

## 0. Bộ đồ nghề đã chốt (owner khai 2026-09-29)

- **DMM rời ×1** (model chưa rõ — việc phải điền: số count, thang mV/Ω).
- **FNIRSI 2C23T ×1** (gộp cả 2 dòng "Oscilloscope 2C23T" + "Signal Generator 2C23T" — là **1 máy 3-trong-1**):
  scope 2 kênh, 10 MHz, 50 MSa/s, nhớ 32 kpts, thang đứng 20 mV/div–10 V/div (x1),
  timebase 50 ns–10 s, trigger auto/normal/single, AC/DC, lưu ảnh + xuất PC;
  phát sóng 1 kênh 1 Hz–2 MHz, biên độ 0,1–3,3 V (sine/square/triangle/full/half/noise/DC);
  DMM 10.000 count: DCV ±(0,5%+3), R ±(0,5%+3); pin 3000 mAh → **máy floating** (không vòng mass lưới).
  *(Nguồn: manual 2C23T; Elektor review: độ chính xác thực tế tốt gấp ~2 lần spec.)*
- **Load cell 5 kg ×1, CHƯA có HX711** (món mua bắt buộc đầu tiên).
  Thực tế dùng: ~0,1% FS ≈ **±5 g (≈ ±0,05 N)**; creep ±0,02% FS/10 phút (≈ ±1 g/10 phút);
  trôi zero theo nhiệt ±0,02% FS/°C (≈ ±1 g/°C); HX711 10/80 SPS.

## 1. Tám giới hạn máy quyết định phương pháp (L1–L8)

| Mã | Giới hạn | Hệ quả phương pháp |
|---|---|---|
| L1 | Scope thang đứng tối thiểu **20 mV/div** | C1.1 (5 mVpp) **không đo bằng scope đơn độc** → phương pháp tách 3 chân (§2) |
| L2 | Gen biên độ tối thiểu **0,1 V** | Muốn kích mV để test chuỗi INA333–ADS1115 → **chia áp ngoài 100:1** (2 điện trở) |
| L3 | Spec không xác nhận **FFT** trên scope | Cấm chữ "phổ" ở M6 (đã thu nhỏ thành cửa sổ V_base ✓); EI-dạng-phổ (nếu có) phải **tính trên Pi từ log**, ghi rõ trong M-25 |
| L4 | Scope ~8-bit → ở 20 mV/div ≈ 0,6 mV/LSB | 5 mVpp ≈ 8 LSB + average: scope **chứng kiến được**, đo chính bằng ADS1115 (LSB 62,5 µV) |
| L5 | Máy chạy pin (floating) | Lợi: không nhiễu mass lưới. Kỷ luật: **mass đơn điểm** khi nối vào mạch cấp nguồn USB (ESP32/Pi) |
| L6 | DMM 10k count: DCV tới 1 mV, R tới 1 Ω ở thang kΩ | **Dư** cho mọi phép GATE 0 (tín hiệu ~0,5–2 V, R ~kΩ, biến thiên hàng trăm Ω/N) |
| L7 | Load cell sàn thực tế ±5 g | Bước 0,1 N (= 10 g) ở ngưỡng marginal → **quả cân (F = m·g) là chuẩn tĩnh chính**, load cell chỉ cho động + đối chứng (đúng `protocols/08`) |
| L8 | Ngân sách lấy mẫu: 860 SPS ÷ 13 lần đọc + settling MUX 100–500 µs | Quét toàn bộ ≈ 40–60 Hz tối đa → **danh định 20 Hz ✓**, 50 Hz chật, 200 Hz chết (M-02/M-03) |

## 2. Verdict từng chỉ số: đo được hay loại?

**Kết luận tổng: M1–M6 + C1.1–C1.10 ĐỀU ĐO ĐƯỢC. Không loại chỉ số nào — chỉ loại claim.**

| Chỉ số | Verdict | Máy + phương pháp |
|---|---|---|
| M1/C1.2 SNR ≥ 18 dB @ΔF = 1 N (≥10/12 kênh) | ✅ GIỮ | Quả cân 100 g (≈ 0,98 N, ghi giá trị thật) + scope ở ngõ ra INA333 + log ADS1115. **M1 đồng thời là kill-test của M-01:** nếu chuỗi hiện tại cho S = 0,5 mV/N thì M1 FAIL → phải tính lại độ lợi (G, R_ref) — đó chính là giá trị của phép đo |
| M2/C1.3 γ ≥ 0,25, R² ≥ 0,90 (0,5–10 N) | ✅ GIỮ | DMM-R + quả cân 50 g–1 kg; fit + R² offline (Python). 10 N ≈ 1,02 kg — cần cục 1 kg |
| M3/C1.4/C1.5 CV ≤ 5% nội phiên, ≤ 8% liên ngày | ✅ GIỮ | DMM + phiếu `08a`. DMM 1 mV trên tín hiệu ~1 V = 0,1% ≪ 5% ✓ |
| M4/C1.8 trôi/tín hiệu ≤ 2,0 sau 10 ngày + auto-zero | ✅ GIỮ | DMM 3 lần/ngày + log T/RH (SHT30). Auto-zero firmware test sau bring-up; trước đó thay bằng re-tare thủ công |
| M5/C1.10 fs ≥ 20 Hz + trễ ≤ 500 ms | ✅ GIỮ | fs: timestamp firmware + scope kẹp chân DRDY/toggle. Trễ: gen phát bước → GPIO mirror + timestamp log (500 ms rất rộng, dự kiến pass dễ nhưng vẫn phải đo) |
| M6 đeo sai (bản thu nhỏ: cửa sổ V_base + 20–30 lần tháo/đeo) | ✅ GIỮ | DMM. 1–2 buổi. **Đường lui:** nếu vỡ tiến độ, M6 hạ thành "quy trình thao tác", không claim % |
| C1.1 Vpp ≤ 5 mV / 5.000 mẫu tĩnh | ✅ GIỮ (phương pháp tách) | (1) **ADS1115 tự log 5.000 mẫu** = số chính; (2) scope chứng kiến dạng sóng (không dao động/kim); (3) scope đo shorted-input = sàn máy. Không vòng tròn (PB-1 §4) |
| C1.6 hys ≤ 18% | ✅ GIỮ | DMM + quả cân lên/xuống |
| C1.7 creep ≤ 8% (60 s @ 5 N) | ✅ GIỮ | DMM + bấm giờ (5 N ≈ 510 g). Bonus: scope timebase chậm bắt đường cong liên tục (32 kpts) |
| C1.9 đồng đều kênh ±40% | ✅ GIỮ | DMM quét các mảng |
| RAL (đường cong nấc tải) | ✅ GIỮ | Quả cân + đếm 10 chu kỳ/nấc. Món "đinh" để thi |
| GAP = PROM − AROM | ⚠️ GIỮ CÓ ĐIỀU KIỆN | Mua/chế **thước đo góc (~50k)** + giàn 2 vận tốc (metronome/bấm giờ hoặc profile servo) + **cấm ADC→độ** (M-13) |
| EI | ⚠️ GIỮ CÓ ĐIỀU KIỆN | Viết **công thức tường minh trước** (M-25) + đường log thô → tính offline |
| Nhiệt (bản hẹp) | ⚠️ GIỮ CÓ ĐIỀU KIỆN | SHT30 (BOM) + **ẩm-nhiệt kế phòng (~100k)** → 1 đồ thị trôi-vs-T + hệ số r từ dữ liệu C1.8 sẵn có |
| Thực nghiệm E1–E4 rules-vs-ML | ⚠️ GIỮ CÓ ĐIỀU KIỆN (P1) | Giàn + injector sự kiện + spec sheet bằng scope. P1, làm sau P0 |
| Claim INT8 < 15 ms | ❌ LOẠI (M-08) | Không cơ sở. Chỉ quay lại dưới dạng benchmark đo thật NẾU ML sống sót qua cổng bằng chứng |
| Phân loại MAS / chẩn đoán / RAL→hồi phục | ❌ LOẠI (M-11/M-14/M-15) | Claim lâm sàng: cấm tuyệt đối |
| AAN trên người / vòng kín lực lên người | ❌ LOẠI (M-12/M-15) | Giữ tối đa PID + ma sát demo trên phantom |
| "Triệt tiêu hoàn toàn/triệt để" | ❌ LOẠI → sửa chữ (M-10) | "Giảm trôi đồng pha; phần dư định lượng qua C1.8" |
| Góc "quy đổi từ tín hiệu" | ❌ LOẠI (M-13) | Góc độc lập (thước + camera đối chứng) |
| 200 Hz đa kênh / 50 Hz danh định | ❌ LOẠI (M-02/M-03) | Danh định **20 Hz**; 50 Hz chỉ ghi "tối đa" nếu đo được |

## 3. Xử lý M-01..M-27 (mỗi mục: verdict + việc cụ thể)

- **M-01** (số §8.2 tự cắn): 🔴 Đo R(F) thật bằng DMM + quả cân → tính lại toàn bộ chuỗi (Vex? G? R_ref?) → S, SNR, M1 sáng tỏ theo. Nút thắt #1.
- **M-02** (50 vs 20 Hz): chốt **20 Hz danh định** (L8). Sửa §8.1/Hình 7 khi duyệt báo cáo.
- **M-03** (200 Hz): xóa mọi vết 200 Hz đa kênh; viết ngân sách lấy mẫu (860 ÷ kênh − settling).
- **M-04** (12 kênh = ?): định nghĩa 1 lần: *kênh = phần tử đơn; mỗi khớp = 1 cặp vi sai (lòng−mu); 12 phần tử + 1 ô chuẩn = 13 đầu vào ADC.*
- **M-05** (§12 "thành công trọn vẹn"): hạ về đúng mức HOẶC bổ sung chương số liệu. Không để nguyên.
- **M-06** ("Qua thực nghiệm…" không xuất xứ): thêm máy/người/ngày/N/log HOẶC dán "minh họa".
- **M-07** (Hình 4/5/13 như kết quả): dán "số liệu minh họa" vào caption cả 3 hình.
- **M-08** (INT8 < 15 ms): xóa (quay lại chỉ dưới dạng benchmark đo thật).
- **M-09** (1,2 s / 5 N / EI_th): ghi "giá trị đặt trước của quy trình, chờ kiểm định trên giàn" + xóa ngôn ngữ người.
- **M-10** ("triệt tiêu hoàn toàn"): sửa chữ toàn báo cáo.
- **M-11** (RAL→hồi phục): quay về "đặc trưng giao thức kiểm định trên giàn".
- **M-12** (AAN ngôn ngữ người): viết lại §10 theo phantom.
- **M-13** (ADC→độ): đo góc độc lập (thước chuẩn chính + camera đối chứng P1).
- **M-14** (GAP suy nguyên nhân): "ghi nhận chênh lệch; không tự suy nguyên nhân".
- **M-15** (Nâng cấp 1–2 vào báo cáo): không đưa vào. Bản cứu được: heatmap tương quan/NMF, FII mô tả, PID + ma sát phantom.
- **M-16** (INA128/INA333): chốt **INA333** duy nhất (nguồn đơn 3,3 V).
- **M-17** (thiếu Vex): ghi Vex = ? vào §9.2 rồi tính lại chuỗi với M-01.
- **M-18** (thiếu HX711): **mua đầu tiên** (~50k).
- **M-19** (servo "giữ được ngón"): ngân sách mô-men (tải × tay đòn vs định mức × SF ≥ 2–3) + test nhiệt giữ tải 10 phút.
- **M-20** (bỏ phanh): nghiệm thu vít me tự hãm (cúp điện không trôi) + 1 khóa cổ thủ công dự phòng.
- **M-21** (Pi ~2M+ vs <1,5M): tách phạm vi — "thiết bị đeo <1,5 tr" vs "trạm nhà dùng chung". Dự toán E2E <10M ở §5, **sổ tay only**.
- **M-22** (1,5 triệu [1]): "Ước tính của nhóm từ [1]: …".
- **M-23** (80% [1], 85% không nguồn): sửa cite 80% hoặc cắt; tìm nguồn 85% hoặc cắt.
- **M-24** (cite sai): sửa [12] (Engineering 2024), [9] (găng từ tính Device 2024); [17] nộp hồ sơ khảo sát hoặc về "tham khảo ẩn danh"; xác minh hoặc gỡ [15]/[18] + mọi cite không DOI.
- **M-25** (thiếu công thức EI): viết tường minh (công thức + cửa sổ + chuẩn hóa + ngưỡng) **trước khi thu dữ liệu**.
- **M-26** (ai đeo găng?): ghi rõ người đeo (kể cả thành viên nhóm), khi nào, an toàn (pin, cách ly, không lực lên người).
- **M-27** (chính tả): soát 1 lượt (bản tay, dài, trên nhiều, tải tỉnh, phổ V_base→cửa sổ).

**Thứ tự dập:** M-01 → M-05/M-07 → M-13/M-12/M-11 → M-04/M-02/M-16/M-17 → M-18/M-19/M-20 → M-21 → M-24/M-22/M-23 → M-25/M-26/M-27.

## 4. Phản biện (tự bắn vào verdict của chính mình)

- **PB-1. "ADS1115 tự đo nhiễu của chính mình có vòng tròn?"** Không. Self-noise là đặc tả chuẩn của mạch đo (mọi datasheet đo đúng thế); scope + shorted-input là đối chứng độc lập. Vòng tròn thật sự chỉ có ở ADC→độ — đã cấm (M-13).
- **PB-2 (CHỐT 2026-09-29 theo ý owner: không tra model DMM rời).** DMM chính = 2C23T, spec theo datasheet (10k count, 0,5%) — dư cho mọi phép GATE 0. DMM rời = máy phụ đo đồng thời, không yêu cầu spec. **Bỏ đề xuất mua DMM spare.** Ràng buộc: DMM/scope là 2 mode loại trừ nhau → đo tĩnh trước, bắt sóng sau; riêng gen **chạy nền được trong khi scope** (Elektor) nên đo trễ/kích chuỗi làm trong 1 lần; cần 2 số cùng lúc thì DMM rời gánh số thứ hai. Lưu ý Elektor: DMM auto-detect hỏng dưới 0,7 V → đo V cầu (hàng trăm mV) **bắt buộc chuyển manual**; cổng BNC mỏng manh (có 1 báo cáo hỏng) → thao tác nhẹ tay.
- **PB-3. "Load cell 5 kg đo bước 0,1 N?"** 0,1 N = 10 g ≈ 2× sàn thực tế (±5 g) → marginal. Chuẩn tĩnh chính = quả cân; load cell cho động + đối chứng. Mua thêm **cân túi 0,01 g (~200k)** để cân khối lượng nhỏ.
- **PB-4. "Scope 8-bit đo SNR 18 dB?"** Động 8-bit ≈ 48 dB ≫ 18 dB — đặt thang đúng là đủ (L4).
- **PB-5. "Gen min 0,1 V thì test mV kiểu gì?"** Chia áp ngoài 100:1 (2 điện trở) → 1 mV. Ghi vào phương pháp (L2).
- **PB-6. "Có cần mua máy đắt không?"** Không. Tiền đổ vào **linh kiện chính hãng** (ADS1115/INA333 fake tràn lan), HX711, servo tốt, vật liệu giàn, camera, quả cân. Máy đo hiện tại đủ hết P0.
- **PB-7. "Giữ M6 có đáng 1–2 buổi?"** Đáng (rẻ, demo đẹp, mảnh "tự phát hiện" duy nhất ở mức đeo). Đường lui đã có: vỡ tiến độ → hạ thành quy trình thao tác.
- **PB-8. "Trần 10M có mâu thuẫn <1,5M trong báo cáo?"** Không nếu ghi rõ phạm vi: báo cáo = giá **thiết bị đeo**; sổ tay = ngân sách **vận hành E2E**. Rủi ro duy nhất là trình bày miệng → chuẩn bị câu trả lời 15 giây (M-21).

## 5. Dự toán E2E <10M (SỔ TAY ONLY — không vào báo cáo)

| Nhóm | Món chính | Ước (VNĐ) |
|---|---|---|
| Găng + cổ tay | ADS1115 xịn ~200k, INA333 ~120k, LSM6DS3 ~150k, SHT30 ~50k, MUX×2+MCP6001 ~60k, TP4056+HT7333+LiPo ~150k, PETG+đai+vít+khung ~300k (Velostat/đồng/ESP32-S3 đã có) | ~1,0–1,3M |
| Trạm | Orange Pi 5 Pro + nguồn + thẻ (**0 đồng — trường ĐÃ CÓ**, owner xác nhận 2026-09-29; đã test INT8 + xử lý ảnh OK, chờ số latency/model để viết claim) | 0 |
| Giàn + đo | Nhôm 2020+ray+vít me+khớp ~1,2M; servo ×3 ~0,5M; lò xo+quả cân+cân túi ~0,5M; HX711 ~0,05M; camera USB ~0,3M; thước đo góc + ẩm-nhiệt kế ~0,15M; silicone + khuôn ~0,5M | ~3,2M |
| Dự phòng 20% (+ DMM spare ~0,5M **chỉ nếu DMM rời quá cùi** — xem §6) | | ~0,9–1,2M |
| **Tổng** | | **~5,5M < 10M ✓** |

**Shopping P0 (mua ngay, chặn đường):** HX711 · ADS1115 + INA333 chính hãng (nếu chưa có) · SHT30 ·
cân túi 0,01 g / quả cân · thước đo góc · ẩm-nhiệt kế · lò xo · vít M3/M5 + êcu · PETG.
**P1 (khi dựng giàn):** camera USB · silicone + khuôn · servo · nhôm 2020 + ray + vít me.

## 6. Ghi chú phiên

- Spec 2C23T/ADS1115/HX711/load cell/MUX đã xác minh qua search 2026-09-29 (log `research/queries/QUERY_LOG.jsonl`).
- File này là **quyết định vận hành**, không phải báo cáo. Sửa báo cáo theo §3 cần owner duyệt riêng từng mục.
- Repo hiện **chưa commit** (chờ duyệt theo DEC-VCS-001).
