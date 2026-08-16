# EXPERIMENTAL PROTOCOL — Giao thức thực nghiệm (ARS Stage 3)
## Hệ thống đệm khí thích ứng tích hợp AAC

> Ngày: 2026-06-14

---

## 1. Mục tiêu thực nghiệm
1. Đánh giá hybrid sensor matrix vs Velostat thuần.
2. Đánh giá PTI engine vs static threshold.
3. Đánh giá CNN-LSTM lead-time.
4. Đánh giá đệm 64 ô PID duy trì sacrum < 32 mmHg.
5. Đánh giá eye-tracking accuracy.
6. Đánh giá Qwen-LoRA AAC sentence quality.
7. Đánh giá self-improving loop Δ reward.

---

## 2. Setup

### 2.1 Thiết bị
- Prototype (đệm, sensor, camera, Jetson, STM32).
- Load simulator (Tekscan FSA + mannequin 70 kg).
- Laptop quan sát (chạy dashboard).
- Stopwatch + lux meter + thermometer.

### 2.2 Volunteer
- 15 người khỏe mạnh, 18–60 tuổi.
- BMI 18–30.
- Không vết thương vùng lưng.
- Ký informed consent (ARS ethics_review_agent).
- Có thể rút lui bất cứ lúc nào.

### 2.3 Load simulator
- Tekscan FSA 9801 calibration.
- Mannequin 70 kg, phân bố trọng lực theo BMI.
- Đặt trên đệm prototype trong 4 giờ (mô phỏng patient nằm lâu).

---

## 3. Thí nghiệm

### 3.1 EXP-01: Hybrid Calibration
**Mục đích:** So sánh Velostat thuần vs Hybrid.

**Protocol:**
- Với mỗi volunteer (n=15):
  - Đặt mannequin lên đệm, 30 phút.
  - Sensor mode 1: Velostat only.
  - Sensor mode 2: Hybrid (Velostat + piezocap).
  - Reference: Tekscan FSA.

**Metrics:**
- RMSE so với Tekscan.
- Drift sau 30 phút.
- PTI error reduction (%).

**Pass criteria:** Hybrid RMSE < Velostat RMSE × 0.8.

### 3.2 EXP-02: PTI Engine
**Protocol:**
- Mannequin nằm 4 giờ, ghi nhận pressure mỗi 1 s.
- Tính PTI per cell mỗi 5 phút.
- So sánh với static threshold (32 mmHg).

**Metrics:**
- Lead-time (phút) cảnh báo critical.
- False positive rate.
- AUC-ROC.

**Pass:** Lead-time ≥ 30 min với FPR ≤ 10%.

### 3.3 EXP-03: CNN-LSTM Forecast
**Protocol:**
- Dataset: 50k frames synthetic + 5k frames thực từ mannequin.
- Leave-one-subject-out CV.
- So sánh với persistence baseline (next frame = current).

**Metrics:**
- MAE, RMSE.
- AUC-ROC cho high-risk (PTI ≥ 2).
- Forecast horizon: 1, 3, 5 phút.

**Pass:** MAE < 0.15, AUC > 0.85.

### 3.4 EXP-04: 64-cell PID Control
**Protocol:**
- Volunteer nằm trên đệm 4 giờ.
- 3 mode: (a) passive alternating (control), (b) adaptive PTI, (c) adaptive + CNN-LSTM.

**Metrics:**
- Mean sacrum pressure (mmHg).
- Peak pressure anywhere.
- Time over threshold (TOT) per cell.

**Pass:** Sacrum < 32 mmHg, TOT < 5% thời gian.

### 3.5 EXP-05: Eye-Tracking Accuracy
**Protocol:**
- 10 volunteer × 3 light condition (dim, normal, bright IR).
- Mỗi turn: 5 target trên grid, dwell 1s.
- Ghi ground-truth (target thực) vs gaze-derived target.

**Metrics:**
- Top-1 accuracy.
- Mean angular error.

**Pass:** Top-1 > 80%, angular error < 2°.

### 3.6 EXP-06: AAC Sentence Quality
**Protocol:**
- 20 volunteer × 10 keyword sequences.
- Sinh câu bằng 2 mode: (a) keyword-only echo, (b) Qwen-LoRA.
- 3 người đánh giá độc lập (Likert 1–5).

**Metrics:**
- BLEU-4 vs ground truth (50 câu mẫu).
- chrF.
- Mean rating.
- Latency (ms).

**Pass:** BLEU ≥ 0.30, rating ≥ 3.5/5, latency ≤ 800 ms.

### 3.7 EXP-07: Self-Improving Loop
**Protocol:**
- 5 volunteer × 4 giờ/người.
- Log (state, action, reward) mỗi 10 phút.

**Metrics:**
- Δ reward after N=24 episodes.
- Stability (variance).

**Pass:** Δ reward ≥ 10%, variance giảm.

---

## 4. Statistical Analysis

### 4.1 Sample size
- n=15 volunteer đạt power 0.80 cho d=0.5, α=0.05.

### 4.2 Tests
- Repeated-measures ANOVA (pressure).
- Paired t-test (accuracy, latency).
- Wilcoxon (subjective rating).
- Holm-Bonferroni cho multiple comparisons.

### 4.3 Reporting
- Mean ± SD, 95% CI.
- Effect size Cohen's d.
- p-value.
- Visualizations: boxplot, time-series, confusion matrix.

---

## 5. Safety & Ethics

### 5.1 IRB equivalent
- Thông báo cho Hội đồng Khoa học kỹ thuật THPT Quảng Trị.
- Informed consent mẫu (Vietnamese).
- Quyền rút lui.
- Bảo mật dữ liệu (no cloud upload).

### 5.2 Physical safety
- Mỗi volunteer khỏe mạnh, không thử trên bệnh nhân thật.
- Mannequin simulator trước khi test volunteer.
- Emergency stop luôn sẵn.

### 5.3 Data privacy
- Dữ liệu volunteer: anonymize thành V01–V15.
- Lưu local trên Jetson, encrypted at rest (LUKS).
- Không upload cloud.

---

## 6. Data management

### 6.1 Collection
- Pressure: log raw + calibrated + PTI per second.
- Eye-tracking: gaze + ROI hit log.
- AAC: keyword + sentence + rating.
- Self-improve: state + action + reward.

### 6.2 Storage
- `/home/aac/data/<volunteer_id>/<date>/`.
- Backup USB drive (encrypted).

### 6.3 Sharing
- Dataset cho cộng đồng: chỉ synthetic + aggregated.
- Volunteer raw data: chỉ trong team.

---

## 7. Timeline

| Tuần | EXP |
|------|-----|
| 8 | EXP-01 (hybrid) |
| 9 | EXP-02, EXP-03 (PTI, CNN-LSTM) |
| 10 | EXP-04, EXP-05 (cushion, eye) |
| 11 | EXP-06, EXP-07 (AAC, self-improve) |
| 12 | Phân tích + báo cáo |

---

## 8. Deliverables

- `outputs/reports/exp_results.md`
- `outputs/figures/*.png`
- `outputs/logs/raw/`
- Báo cáo PDF
