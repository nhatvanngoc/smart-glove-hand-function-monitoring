# SOFTWARE DESIGN — Thiết kế phần mềm (ARS Stage 2)
## Hệ thống đệm khí thích ứng tích hợp AAC

> Ngày: 2026-06-14

---

## 1. Kiến trúc phần mềm (Jetson)

### 1.1 Sơ đồ phân lớp
```
┌────────────────────────────────────────────────────────┐
│  Presentation Layer   │  UI (Streamlit + AAC grid)    │
├────────────────────────────────────────────────────────┤
│  Application Layer    │  State machine + Orchestrator │
├────────────────────────────────────────────────────────┤
│  AI/ML Layer          │  CNN-LSTM, Qwen-LoRA, PTI     │
├────────────────────────────────────────────────────────┤
│  Perception Layer     │  Pressure map, Eye-tracker    │
├────────────────────────────────────────────────────────┤
│  Control Layer        │  PID 64 ô, Arm IK             │
├────────────────────────────────────────────────────────┤
│  HAL / Drivers        │  UART, SPI proxy, I2C         │
├────────────────────────────────────────────────────────┤
│  OS Layer             │  Ubuntu 20.04 + ROS2 Humble   │
└────────────────────────────────────────────────────────┘
```

### 1.2 ROS2 graph (xem `diagrams/03_software_architecture.png`)
- **Nodes:** `pressure_node`, `eye_node`, `arm_node`, `aac_node`, `safety_node`, `dashboard_node`.
- **Topics:** xem `docs/04_System_Architecture.md`.
- **Services:** `/calibrate_pressure`, `/reset_aac`, `/system_check`.
- **Actions:** `/apply_pressure_profile`, `/track_face`.

### 1.3 State machine
```
INIT ──► CALIBRATE ──► IDLE ──► MONITOR ──► ACTIVE ──► EMERGENCY
            │           │         │            │            ▲
            └─► FAULT ◄──┴─────────┴────────────┘────────────┘
```
- Mỗi state có entry/exit action + watchdog.

---

## 2. Module chi tiết

### 2.1 `pressure_node` (Jetson)
- Subscribe `/pressure/raw` (STM32 gửi).
- Cross-calibrate → `/pressure/calibrated`.
- Tính PTI → `/risk/map`.
- Publish `/cushion/cmd` (setpoints).

### 2.2 `eye_node`
- Đọc 2× camera (OpenCV GStreamer).
- Pupil detection: blob detector hoặc MediaPipe Face Mesh.
- Stereo triangulation → gaze vector.
- Publish `/gaze/vector` + điều khiển arm.

### 2.3 `arm_node`
- Inverse kinematics (3 DOF).
- PID servo position.
- Watchdog timeout → center pose.

### 2.4 `aac_node`
- Quản lý grid state.
- Nhận gaze → highlight cell.
- Selection → keyword → Qwen-LoRA → sentence → TTS.

### 2.5 `safety_node`
- Mỗi tick 20 Hz: check valve pressure, temperature, watchdog.
- Nếu fail → publish `/system/safety=false` + trigger EMERGENCY.

### 2.6 `dashboard_node`
- Streamlit UI.
- Hiển thị: pressure map, risk map, gaze overlay, AAC grid.

---

## 3. STM32 firmware (xem `src/stm32_firmware/`)

### 3.1 Architecture
- **Bare-metal + FreeRTOS** (option).
- Main loop:
  - DMA ADC đọc sensor matrix (continuous).
  - UART DMA gửi `/pressure/raw` mỗi 100 ms.
  - Nhận `/cushion/cmd` → cập nhật PWM.
  - Watchdog refresh mỗi 50 ms.

### 3.2 Tasks (RTOS mode)
- `Task_ADC`: đọc cảm biến, đẩy vào queue.
- `Task_Control`: tính PID, update PWM.
- `Task_Comm`: UART bridge ROS2.
- `Task_Watchdog`: refresh + safety check.

### 3.3 Build & flash
```bash
cd src/stm32_firmware
make -j
st-flash write build/main.bin 0x08000000
```

---

## 4. ML pipeline (xem `src/pressure_model/`, `src/aac_assistant/`)

### 4.1 PTI Engine (`pressure_model/pti_engine.py`)
```python
def compute_pti(p_history, posture):
    """
    p_history: shape (T, 8, 8), mmHg
    posture: scalar ∈ {0,1,2}
    return: pti per cell, shape (8,8)
    """
    w = posture_weight(posture)
    p_th = threshold_map(posture)
    ratio = p_history / p_th
    weighted = (ratio * w).clip(0, 5)
    return weighted.sum(axis=0)
```

### 4.2 CNN-LSTM (`pressure_model/cnn_lstm.py`)
- Input: (60, 8, 8, 3)  ← pressure + risk_history + posture
- CNN: 3 conv blocks → (60, 64)
- LSTM: 2 layers, hidden 128
- Dense: → scalar (forecast risk)

### 4.3 Qwen-0.5B + LoRA (`aac_assistant/qwen_lora.py`)
- Load `Qwen/Qwen2-0.5B-Instruct`.
- Inject LoRA (r=8).
- Fine-tune trên 50 mẫu (5 epoch, lr=1e-4).
- Quantize INT8 sau train.

### 4.4 Training pipeline (xem `experiments/exp02_pti_model.py`)
- Synthetic data generator (50k frames).
- Train/val/test split 70/15/15.
- Save model + metrics.

---

## 5. Configuration & Secrets

### 5.1 Config file (`config.yaml`)
```yaml
system:
  pressure_rate_hz: 10
  camera_rate_fps: 30
  safety_tick_hz: 20

sensors:
  matrix_size: [8, 8]
  velostat_v_ref: 3.3
  piezocap_offset: 0.5

control:
  p_th_default: 32.0  # mmHg
  pid_p: 1.0
  pid_i: 0.1
  pid_d: 0.05

aac:
  grid_cols: 5
  grid_rows: 3
  lora_path: models/qwen_lora_v1
  tts_engine: espeak

safety:
  max_cell_pressure: 80.0
  watchdog_timeout_s: 5.0
  emergency_stop_gpio: 17
```

### 5.2 Secrets
- Không có cloud credentials (on-device only).
- Patient ID dùng UUID local.

---

## 6. Logging & Observability

### 6.1 Structured logs (JSON)
- Mỗi event: timestamp, level, component, message, ctx.
- Log rotation: 100 MB × 5.

### 6.2 Metrics (Prometheus format optional)
- Pressure mean, max per minute.
- AAC latency histogram.
- Safety gate violations counter.

### 6.3 Trace (optional)
- ROS2 topic snapshot mỗi 10s → `outputs/logs/trace.jsonl`.

---

## 7. Testing strategy

### 7.1 Unit test
- `pytest` cho mỗi module Python.
- `Ceedling` cho STM32 firmware.

### 7.2 Integration test
- `experiments/exp05_pipeline_e2e.py`: chạy full pipeline trên synthetic data.

### 7.3 Hardware-in-loop (HIL)
- STM32 firmware + simulated sensor (host-side script).

### 7.4 Reproducibility
- Docker image `docker/Dockerfile`.
- `repro_lock.yaml` declare seeds.

---

## 8. Build & deploy

### 8.1 Build
```bash
# STM32
cd src/stm32_firmware && make

# Jetson
cd src/jetson_pipeline && colcon build

# Models
python experiments/exp02_pti_model.py --train
python experiments/exp03_cnn_lstm.py --train
python experiments/exp04_qwen_lora.py --train
```

### 8.2 Deploy
- Copy artifacts lên Jetson qua `scp` hoặc USB.
- Service file: `systemd/aac_cushion.service`.
- Auto-start sau khi Jetson boot.

---

## 9. Documentation
- Code docstring (Google style).
- `docs/04_System_Architecture.md` (đã có).
- API doc auto-gen bằng `sphinx`.

---

## 10. Open-source stack
- ROS2 Humble (BSD)
- OpenCV 4.5 (Apache 2.0)
- PyTorch 2.3 (BSD)
- Transformers (Apache 2.0)
- Streamlit (Apache 2.0)
- MediaPipe (Apache 2.0)
- Qwen-0.5B (custom license, OK cho research)
