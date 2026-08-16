# ML MODELS — Mô hình máy học (ARS Stage 2)
## PTI Engine, CNN-LSTM Forecaster, Qwen-LoRA AAC

> Ngày: 2026-06-14

---

## 1. PTI Engine (Pressure-Time-Intensity)

### 1.1 Định nghĩa toán học
PTI cho mỗi ô (i, j) tại thời điểm t:

```
PTI_{i,j}(t) = ∫₀ᵗ w_posture(τ) · (P_{i,j}(τ) / P_th_{i,j}(τ)) dτ
```

Trong đó:
- `P_{i,j}(τ)`: áp suất đo tại ô (i,j), mmHg
- `P_th_{i,j}(τ)`: ngưỡng (32 mmHg mặc định, ± theo vùng)
- `w_posture(τ)`: trọng số theo tư thế (supine=1.0, lateral=1.2, prone=1.1)

### 1.2 Threshold map (per cell)
| Vùng | P_th (mmHg) | Ghi chú |
|------|------------|---------|
| Sacrum | 32 | Vùng nguy cơ cao nhất |
| Heels | 30 | Mỏng, dễ tổn thương |
| Trochanter | 35 | Lateral nặng |
| Scapula | 35 | Prone nặng |
| Khác | 40 | Vùng thường |

### 1.3 Implementation (xem `src/pressure_model/pti_engine.py`)
```python
def compute_pti(p_history, posture_class):
    T, H, W = p_history.shape
    p_th = threshold_map(posture_class)  # (H,W)
    w = posture_weight(posture_class)
    ratio = p_history / p_th[None,...]
    weighted = np.clip(ratio * w, 0, 5)
    return weighted.sum(axis=0)  # (H,W)
```

### 1.4 Risk classification
- `low`: PTI < 1.0
- `moderate`: 1.0 ≤ PTI < 2.0
- `high`: 2.0 ≤ PTI < 3.0
- `critical`: PTI ≥ 3.0

---

## 2. CNN-LSTM Forecaster

### 2.1 Use case
Dự báo risk map 1–5 phút tới, cho phép cushion **proactive** điều chỉnh thay vì reactive.

### 2.2 Architecture
```
Input: 60 frames × (8×8 × 3 channels)
        │
        ▼
Conv2D(8 → 32, kernel 3, ReLU) ──► BatchNorm ──► MaxPool
        │
        ▼
Conv2D(32 → 64, kernel 3, ReLU) ──► BatchNorm ──► MaxPool
        │
        ▼
Flatten ──► Dense(128)
        │
        ▼
LSTM(2 layers, hidden=128) ──► Dropout(0.2)
        │
        ▼
Dense(64) ──► ReLU ──► Dense(1)
        │
        ▼
Output: predicted risk score (sigmoid)
```

### 2.3 Channels (per frame)
1. Pressure (mmHg) → chuẩn hóa về [0,1]
2. Risk binary (high/critical) → 0/1
3. Posture one-hot → 3 dims nhưng dùng 1 scalar

### 2.4 Loss
```python
loss = weighted_mse(y_true, y_pred, weight=sacrum_mask)
```
- `sacrum_mask`: ưu tiên vùng sacrum gấp 3 lần vùng khác.

### 2.5 Training
- Optimizer: Adam (lr=1e-3)
- Batch: 32
- Epochs: 50
- Early stopping: patience 10 trên val_loss
- Seed: 42 (deterministic)

### 2.6 Evaluation
- MAE, RMSE, AUC-ROC cho high-risk detection.
- Lead-time vs static threshold (target ≥ 30 min).

### 2.7 Implementation
Xem `src/pressure_model/cnn_lstm.py` và `experiments/exp03_cnn_lstm.py`.

---

## 3. Qwen-0.5B + LoRA cho AAC

### 3.1 Mục tiêu
Sinh câu hoàn chỉnh từ chuỗi từ khóa do bệnh nhân chọn qua gaze.
Ví dụ: `["tôi", "khát", "nước"]` → `"Tôi đang khát nước, làm ơn cho tôi một ly."`

### 3.2 Base model
- `Qwen/Qwen2-0.5B-Instruct` (500M params, context 32k).
- License: research OK.

### 3.3 LoRA configuration
```yaml
r: 8
alpha: 16
target_modules: [q_proj, v_proj]
dropout: 0.05
```

### 3.4 Training dataset
- 50 mẫu câu do bệnh nhân/nhân viên y tế cung cấp.
- Format: prompt = keyword list, response = complete sentence.
- Augmentation: thêm variations, paraphrase.

### 3.5 Training script (xem `experiments/exp04_qwen_lora.py`)
```python
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer

model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2-0.5B-Instruct")
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2-0.5B-Instruct")
lora_config = LoraConfig(r=8, lora_alpha=16, target_modules=["q_proj","v_proj"], lora_dropout=0.05)
model = get_peft_model(model, lora_config)
# ... train ...
```

### 3.6 Quantization
- Post-training INT8 quantization.
- TensorRT engine cho Jetson (target latency < 300 ms).

### 3.7 Evaluation
- BLEU-4 vs ground truth.
- chrF.
- Human rating (1–5) về ngữ cảnh.
- Latency (ms).

---

## 4. Eye-tracking ML

### 4.1 Pupil detection
- MediaPipe Face Mesh (468 landmarks) — robust.
- Backup: OpenCV blob detector cho trường hợp fail.

### 4.2 Stereo triangulation
- Camera matrix K1, K2 (intrinsic), distortion D1, D2.
- Baseline 60 mm.
- Rectify → disparity → 3D pupil position.
- Gaze vector = (pupil - cornea_center) projected.

### 4.3 Calibration
- 5-point calibration (center + 4 corners).
- Mỗi user calibrate 1 lần lúc đầu.
- Lưu vào `user_calib.yaml`.

### 4.4 Accuracy target
- Top-1 icon selection > 80% (5×3 grid).
- Drift < 1° trong 30 phút.

---

## 5. Self-Improving Loop

### 5.1 Contextual bandit
- **State s_t:** (mean peak pressure trend, AAC success rate, comfort score)
- **Action a_t:** (Δ P_threshold, Δ PID gain, Δ AAC top-k)
- **Reward r_t:** w₁·(1 - normalized_peak) + w₂·success_rate + w₃·comfort

### 5.2 Algorithm
- LinUCB với d = 8 features.
- Exploration ε = 0.1 giảm dần.

### 5.3 Safety guard
- Reward clamp [-1, 1].
- Action space bounded (±10% tham số hiện tại).
- Human override luôn ưu tiên.

### 5.4 Implementation
Xem `src/jetson_pipeline/self_improve/bandit.py`.

---

## 6. MLOps

### 6.1 Versioning
- Model artifacts: `models/<name>/<version>/`.
- Dataset: DVC.

### 6.2 CI
- Lint (ruff), unit test, training smoke test.
- Publish metrics dashboard (optional).

### 6.3 Reproducibility
- `repro_lock.yaml` declare seeds + env (xem `docs/03_Methodology`).
- Docker image.

---

## 7. Failure mode handling (ARS M1–M7)
| Mode | Risk | Mitigation |
|------|------|-----------|
| M1 Implementation bug | CNN-LSTM wrong | Unit test + validation MAE |
| M2 Hallucinated citation | (n/a in ML) | – |
| M3 Hallucinated result | Fake BLEU | Always run real test set |
| M4 Shortcut reliance | Pressure → 0 | Add adversarial test |
| M5 Bug as novelty | Sensor mis-cal | Cross-cal verification |
| M6 Method fabrication | Pretend ITER | Report sample size honestly |
| M7 Frame-lock | Wrong posture model | Test 3 postures |
