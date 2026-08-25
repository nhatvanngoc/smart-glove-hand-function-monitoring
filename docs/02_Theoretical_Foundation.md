# 02 — Cơ sở lí thuyết (Theoretical Foundation)

> **Ngày:** 2026-08-25 · **Đề tài:** Smart Insole Edge-AI (3D-GRF & COP, drift-robust, knee-OA rehab monitoring).
> **Quy ước bằng chứng (đọc trước khi dùng):**
> - 🟢 **CHUẨN (standard):** kiến thức cơ bản đã được thiết lập rộng rãi trong giáo trình cơ sinh học/kỹ thuật. **Vẫn phải đối chiếu với tài liệu gốc (trang/chương) trước khi trích dẫn chính thức** trong bài nộp — không được ghi DOI/trang nếu chưa kiểm chứng.
> - 🟡 **GIẢ THUYẾT (hypothesis):** suy luận hợp lý của đề tài, **chưa** được thực nghiệm xác nhận.
> - 🔵 **CẦN KIỂM CHỨNG (to verify):** giá trị/định lượng phải đo hoặc tra cứu, không được viện dẫn như sự thật.
>
> Không có con số nào trong tài liệu này là kết quả đo của dự án.

---

## 1. Cơ sinh học dáng đi (gait biomechanics)

### 1.1 Chu kỳ dáng đi 🟢
Chu kỳ dáng đi (gait cycle) gồm **pha trụ (stance, ≈ 60% chu kỳ)** và **pha đu (swing, ≈ 40%)** khi đi bộ thường. Các mốc chính trong stance: **heel strike (chạm gót) → foot flat → midstance (giữa trụ) → heel off → toe off (nhấc ngón)**. Trong đi bộ có các khoảng **double support** (cả hai chân chạm đất). Phần trăm thời gian từng pha thay đổi theo tốc độ — các giá trị cụ thể là 🔵.

### 1.2 Lực phản lực mặt đất 3 chiều (3D-GRF) 🟢
Theo định luật III Newton, mặt đất tác dụng lại bàn chân một lực **bằng và ngược chiều** lực bàn chân tác dụng xuống. Trong hệ quy chiếu của đế/người:

| Thành phần | Hướng | Vai trò sinh học |
|---|---|---|
| **Fz** | thẳng đứng | nâng đỡ trọng lượng + gia tốc; dạng **"hình chữ M"** hai đỉnh (impact peak lúc chạm gót, push-off peak lúc đẩy đi) với thung lũng giữa trụ |
| **Fx** | trước–sau | **braking** (hãm, lực hướng sau) đầu trụ → **propulsion** (đẩy, hướng trước) cuối trụ |
| **Fy** | trái–phải (mediolateral) | cân bằng bên, biên độ nhỏ và nhiễu nhất |

**Độ lớn điển hình (đi bộ thường, 🔵 cần trích nguồn gốc):** Fz đỉnh ≈ **1.0–1.2 × trọng lượng cơ thể (BW)**; Fx đỉnh ≈ **0.15–0.2 BW**; Fy ≈ **0.05–0.1 BW** (biến thiên lớn giữa cá nhân). Đây là **giá trị tham khảo chuẩn**, không phải hằng số phổ quát.

### 1.3 Tâm áp lực (Center of Pressure, COP) 🟢
COP là **điểm đặt của hợp lực** phản lực mặt đất lên mặt phẳng tiếp xúc. Với ma trận cảm biến rời rạc (n cell, lực pháp tuyến Fᵢ tại vị trí (xᵢ, yᵢ)):

```
COP_x = Σ Fᵢ·xᵢ / Σ Fᵢ ,   COP_y = Σ Fᵢ·yᵢ / Σ Fᵢ
```

- Quỹ đạo COP trong stance điển hình: vào ở gót, tiến dọc mép ngoài → giữa bàn chân → lệch vào trong ở khớp bàn–ngón → ra ở ngón cái.
- ⚠️ **COP ≠ COM** (center of mass). COP là đại lượng đo trực tiếp từ phân bố áp lực; COM là đại lượng động học toàn thân. Nhầm lẫn này là lỗi phản biện thường gặp — ghi rõ trong bài nộp.

### 1.4 Gait → GRF/COP → tải khớp gối (knee loading) 🟢/🟡
- **Knee Adduction Moment (KAM)** là moment khép gối ở mặt phẳng trán (frontal plane), thường được dùng làm **đại lượng thay thế (surrogate)** cho tải lên khoang trong (medial compartment) khớp gối. KAM phụ thuộc vào **độ lớn GRF** và **cánh tay đòn** từ vector GRF tới tâm khớp gối — vì vậy GRF/COP là đầu vào gián tiếp, không phải bản thân tải khớp. 🟢
- Ở người knee OA, các thay đổi dáng đi thường được báo cáo: **giảm tốc độ đi, rút ngắn sải chân, giảm gập gối, tăng KAM (một số nghiên cứu), bất đối xứng hai chân, thay đổi GRF/COP**. 🟡 — mức độ & hướng thay đổi tùy giai đoạn bệnh và cá nhân; **không suy diễn "GRF ⇒ OA"**.
- Chuỗi hợp lệ: `Gait → GRF/COP → (gián tiếp) knee loading pattern`. Chuỗi bị cấm: `GRF ⇒ OA` hoặc "chẩn đoán".

---

## 2. Cảm biến áp lực dẻo — Velostat/piezoresistive

### 2.1 Nguyên lý piezoresistive 🟢/🔵
Velostat (film carbon-impregnated polyolefin) là cảm biến **piezoresistive**: điện trở khối **giảm** khi chịu lực nén (hạt dẫn tiếp xúc tốt hơn khi vật liệu bị nén). Quan hệ điện trở–lực là **phi tuyến mạnh**, thường xấp xỉ dạng luỹ thừa giảm `R ∝ P^(−α)` với α phụ thuộc vật liệu/điện cực/nhiệt độ. 🔵 — tham số cụ thể phải đo trên chính mẫu cảm biến của dự án, **không suy từ datasheet chung**.

### 2.2 Các phi tuyến tính cố hữu 🟢/🔵
- **Hysteresis (trễ):** đường R–P khi tăng tải khác khi giảm tải → cùng áp lực, đọc khác nhau tùy lịch sử tải.
- **Creep (chảy):** dưới tải **không đổi**, điện trở vẫn tiếp tục đổi theo thời gian.
- **Drift (trôi):** tín hiệu "trôi" chậm theo phút/giờ/ngày do nhiệt, biến dạng, lão hoá vật liệu.
- **Sensitivity/gain change:** độ nhạy thay đổi theo tải/nhiệt/chu kỳ → sai lệch **nhân (multiplicative)** chứ không chỉ cộng.
- **Nhiệt độ:** điện trở nhạy nhiệt → baseline và gain đều đổi.
- **Lắp ráp (fitting):** áp lực lắp đặt đế, điện cực, keo dẫn ảnh hưởng đáp ứng và độ lặp lại.
- **Session-to-session variation:** cùng cảm biến, khác ngày/session → đáp ứng khác.

> Hệ quả: **đọc ADC/điện trở thô không thể đổi trực tiếp ra lực (Fz) tin cậy** nếu chưa hiệu chuẩn theo hệ thống; đây là giới hạn đo lường, không phải lỗi mã.

### 2.3 Phân loại drift (mô hình đơn giản) 🟡
Mô hình tuyến tính xấp xỉ của tín hiệu đo `r(t)`:

```
r(t) = (1 + g(t)) · r_true(t) + b(t)
```

- `b(t)`: **baseline/offset drift** (cộng thêm, chậm).
- `g(t)`: **sensitivity/gain drift** (nhân, ảnh hưởng biên độ).

Ngoài ra còn drift do **hysteresis** (phụ thuộc lịch sử) và **creep** (phụ thuộc thời gian tải) không nằm gọn trong mô hình tuyến tính trên.

### 2.4 dP/dt — tác dụng và giới hạn 🟡/🟢
- **Tác dụng:** đạo hàm theo thời gian `dP/dt` **loại bỏ thành phần offset `b(t)` nếu nó biến thiên chậm** (đạo hàm của hằng số chậm ≈ 0). Vì vậy dP/dt giảm nhiễu do **baseline drift chậm** (nhiệt độ trôi từ từ).
- **Giới hạn (phải ghi rõ):**
  1. **Không loại được gain drift `g(t)`** (đạo hàm vẫn bị nhân bởi gain).
  2. **Không loại hysteresis/creep** — chúng tác động lên chính biên độ động học.
  3. **Khuếch đại nhiễu tần số cao** — cần lọc (low-pass) trước/sau đạo hàm; chọn tần số cắt hợp lý.
- ⚠️ Vì vậy từ ngữ đúng là **"giảm (attenuate) drift"**, **không** "triệt tiêu/loại bỏ drift".

---

## 3. Xử lý tín hiệu & mô hình drift

### 3.1 Ước lượng & trừ baseline 🟡
- **Baseline không tải:** đo khi không tải (hoặc tải tham chiếu) trước/sau mỗi phiên để ước lượng `b(t)`.
- **Reference cell:** một cell không chịu tải của người dùng làm tham chiếu nhiệt/bù trôi.
- **Low-pass của baseline:** trích thành phần chậm của tín hiệu nghỉ rồi trừ.

### 3.2 Hiệu chuẩn (calibration) & personal baseline 🟡
- **Per-sensor calibration:** ánh xạ R→F (hoặc ADC→F) riêng từng cell bằng tải đã biết.
- **Personal baseline:** thiết lập ngưỡng/tham chiếu **riêng từng cá nhân** (đặc điểm dáng đi, trọng lượng, hình dạng chân) → deviation đo tương đối so với chính người đó, không so với dân số chung.
- **Cross-session generalization:** mô hình huấn luyện ở phiên 1 phải giữ được sai số ở phiên N mà không retrain toàn bộ.

### 3.3 Phát hiện thay đổi (change detection) — tách nguồn biến thiên 🟡
Bài toán trung tâm:

```
Δ(đo lường dọc) = Δ_biology + Δ_sensor + Δ_environment
```

- **Δ_biology:** thay đổi thật của dáng đi (bệnh tiến triển, phục hồi, mệt mỏi…).
- **Δ_sensor:** drift/hysteresis/creep của Velostat, lắp ráp.
- **Δ_environment:** nhiệt độ, độ ẩm, giày, bề mặt đi.

**Công cụ ứng viên (🟡, chưa chọn):** statistical process control (CUSUM/EWMA), change-point detection, so sánh phân phối liên-phiên, metric **false change detection** (số lần báo "thay đổi" sai trên dữ liệu không đổi).

### 3.4 Killer experiment (thiết kế kiểm chứng) 🟡
| Nhánh | Dự đoán | Metric |
|---|---|---|
| Không drift correction | error ↑ theo phiên | cross-session RMSE/MAE, drift rate |
| Có drift correction | error ≈ hằng số | như trên |
| So sánh change detection | false detection ↓ | false-change rate trên dữ liệu ổn định |

---

## 4. Mô hình hoá không gian–thời gian (graph & GNN)

### 4.1 Trường áp lực P(x,y,t) 🟢
Ma trận cảm biến cho **trường áp lực dưới bàn chân theo thời gian** `P(x,y,t)`. Dữ liệu có cấu trúc **không gian** (vị trí giải phẫu) + **thời gian** (chuỗi) → phù hợp mô hình không gian–thời gian.

### 4.2 Đồ thị giải phẫu bàn chân 🟡
Biểu diễn bàn chân như **graph**: node = vùng cảm biến/gải phẫu (gót, vòm, các khớp bàn–ngón, ngón…); cạnh = quan hệ giải phẫu/lân cận (adjacency). Lợi ích dự kiến: mô hình "biết" quan hệ không gian giữa các vùng thay vì coi chúng độc lập.

### 4.3 ST-GNN / GCN / ST-GCN 🟢/🟡
- **GCN (Graph Convolutional Network):** học biểu diễn node bằng lan truyền thông điệp trên cạnh.
- **ST-GCN:** kết hợp **spatial graph convolution** + **temporal convolution** (chuẩn trong nhận dạng hành động dựa trên skeleton).
- **ST-GNN** tổng quát: mô hình graph động theo thời gian.
- 🟡 **Cảnh báo quan trọng:** GNN/ST-GNN chỉ xứng đáng nếu **thắng baseline đơn giản hơn** trên cùng dữ liệu (xem 4.4). Với dữ liệu nhỏ, mô hình phức tạp dễ overfit.

### 4.4 Baseline & nguyên tắc so sánh 🟢
Thứ tự bắt buộc trước khi dùng GNN:
1. **Tuyến tính/ridge** (hồi quy từ vector áp lực → Fx/Fy/Fz/COP).
2. **CNN** (trên ảnh pressure map) và/hoặc **LSTM/TCN** (chuỗi thời gian).
3. Chỉ khi 1–2 chưa đủ mới thêm ST-GNN; so sánh trên **cùng train/val/test split**, báo **uncertainty**.

### 4.5 Uncertainty & chống leakage 🟢
- **Chống leakage:** tách dữ liệu **theo người tham gia** (leave-one-subject-out) và **theo phiên** (leave-one-session-out) — không tách mẫu ngẫu nhiên, nếu không cross-session claim sẽ bị vô hiệu.
- **Uncertainty:** báo khoảng tin cậy/độ phân tán, không chỉ điểm RMSE.

---

## 5. Chuẩn vàng & metrics

### 5.1 Force plate (chuẩn vàng) 🟢
- **Force plate** (tấm đo lực đa trục) đo trực tiếp Fx, Fy, Fz và moment → cho **COP** và **GRF ground truth** với độ chính xác cao. Đây là **điểm mạnh nhất của đề tài**: so sánh trực tiếp predicted ↔ measured.
- **Đối chiếu:** Predicted 3D-GRF ↔ force plate GRF; Predicted COP ↔ force plate COP.
- **Blocker:** chưa có force plate/load cell đa trục thì mọi báo cáo sai số 3D-GRF là **không kiểm chứng được** (xem `DECISION_LOG` DEC-INSOLE-006).

### 5.2 Metrics 🟢 (định nghĩa chuẩn — cần ghi rõ chuẩn hoá khi dùng)
| Metric | Định nghĩa | Lưu ý |
|---|---|---|
| **RMSE** | √(mean((ŷ−y)²)) | cùng đơn vị với y |
| **MAE** | mean(|ŷ−y|) | ít nhạy outlier hơn RMSE |
| **NRMSE** | RMSE / (đại lượng chuẩn hoá) | ⚠️ **phải ghi rõ chuẩn hoá theo gì** (range, mean, hay max) — NRMSE khác nhau theo cách chuẩn hoá |
| **R²** | 1 − SS_res/SS_tot | có thể âm khi mô hình tệ |
| **COP error** | khoảng cách Euclid ŷ_COP−y_COP (per-sample) và/hoặc theo quỹ đạo | báo cả bias hướng |
| **Temporal alignment** | độ lệch thời gian (lag) giữa chuỗi dự đoán & chuỗi thật | cross-correlation |
| **Drift** | residual sau tải tĩnh dài / tốc độ trôi baseline | đơn vị & khoảng thời gian cụ thể |
| **Cross-session error** | sai số trên phiên giữ lại (held-out session) | metric chính cho RQ1 |

---

## 6. Triển khai biên (edge deployment) 🟡/🔵

- **RK3588 / Orange Pi 5 Pro:** NPU công bố **~6 TOPS** (INT8) — 🔵 là **thông số nhà sản xuất**, chưa phải throughput đo được.
- **INT8 quantization:** giảm kích thước/tăng tốc suy luận, có thể đánh đổi chút độ chính xác → phải đo **accuracy drop** sau lượng tử hoá.
- **Chuẩn đo:** latency (ms), throughput (inference/s), công suất (W), bộ nhớ — trên mô hình thực tế, không ước lượng.
- **Chế độ suy luận:** theo cửa sổ/bước chân (per-step/per-window), không nhất thiết per-sample.

---

## 7. Khung theo dõi dọc (longitudinal) & tuyên bố an toàn

### 7.1 Chuỗi theo dõi 🟡
```
Personal baseline → longitudinal deviation → gait change detection → rehab response monitoring
```

### 7.2 Được phép vs bị cấm 🟢
| Được phép | Bị cấm |
|---|---|
| "hỗ trợ theo dõi thay đổi chức năng vận động" | "chẩn đoán OA" |
| "đánh giá đáp ứng phục hồi" | "điều trị OA" |
| "nguyên mẫu đo lường cơ sinh học" | "thiết bị y tế" |
| "so sánh với force plate (validation)" | "thay thế force plate/X-ray/MRI/bác sĩ" |

---

## 8. Câu hỏi mở & giả thuyết cần kiểm chứng

| # | Mục | Trạng thái | Bằng chứng cần |
|---|---|---|---|
| 1 | Độ lớn drift thực của mẫu Velostat (offset vs gain) theo nhiệt/tải/thời gian | 🔵 chưa đo | bench đặc trưng cảm biến |
| 2 | dP/dt giảm bao nhiêu % drift ở tần số/thời lượng nào | 🟡 | thí nghiệm tải dài |
| 3 | ST-GNN có thắng baseline không | 🟡 | so sánh cùng split |
| 4 | Cross-session generalization giữ được bao lâu | 🔵 | dữ liệu nhiều phiên |
| 5 | False change detection giảm bao nhiêu khi có drift correction | 🟡 | killer experiment |
| 6 | Prior art 2025–2026 ở đâu (gap thật nằm đâu) | 🔵 | `docs/03` gap analysis |
| 7 | NPU INT8 latency/throughput/công suất thực | 🔵 | benchmark |

> **Nguyên tắc:** mỗi dòng trên chỉ được chuyển thành kết quả khi có artifact đo/trích dẫn tương ứng trong `research/evidence/SOURCE_LEDGER.csv` và `research/claims/CLAIM_LEDGER.csv`.
