# SYSTEM ARCHITECTURE — Kiến trúc hệ thống (ARS Stage 2)
## Adaptive Air Cushion + Eye-Tracking AAC cho phòng ngừa loét tì đè

> Ngày: 2026-06-14
> Tuân theo: ARS-Codex academic-pipeline v3.12.0 (Stage 2 WRITE)

---

## 1. Tầm nhìn hệ thống (System Vision)

Hệ thống là một **thiết bị y tế thông minh** gồm 4 lớp chức năng:

```
┌─────────────────────────────────────────────────────────────┐
│  L4. SELF-IMPROVING LOOP      │ Cá nhân hóa theo user     │
├─────────────────────────────────────────────────────────────┤
│  L3. AI SERVICES               │ PTI, CNN-LSTM, Qwen-LoRA │
├─────────────────────────────────────────────────────────────┤
│  L2. CONTROL & ACTUATION       │ PID 64 ô, robot arm     │
├─────────────────────────────────────────────────────────────┤
│  L1. SENSING & PERCEPTION      │ Pressure map, Eye-track  │
└─────────────────────────────────────────────────────────────┘
```

**Nguyên lý thiết kế (Design Principles):**
1. *Safety-first:* Mọi quyết định AI đều qua safety gate.
2. *Modularity:* Tách cảm biến, điều khiển, AI, AAC để test độc lập.
3. *On-device:* Không upload dữ liệu bệnh nhân lên cloud.
4. *Personalization:* Vòng lặp tự cải tiến thích nghi từng user.

---

## 2. Sơ đồ khối tổng quan (System Block Diagram)

Xem file: `diagrams/01_system_block_diagram.png` (sẽ tạo ở Phase 2).

**Các khối chính:**
- **Edge AI (Jetson Orin Nano):** chạy CNN-LSTM, Qwen-LoRA, eye-tracking.
- **MCU (STM32F407):** điều khiển thời gian thực, đọc cảm biến, xuất PWM cho van khí.
- **Hybrid Sensor Matrix 8×8:** 64 Velostat + 8 piezocapacitive nodes (anchor).
- **Pneumatic Manifold:** 64 valve + 1 pump + 1 pressure reservoir.
- **Stereo Camera Rig:** 2× Global Shutter + IR LED + robot arm 3 DOF.
- **UI/UX:** màn hình cảm ứng + AAC keyboard + audio output.

---

## 3. Luồng dữ liệu (Data Flow)

### 3.1 Sensing Pipeline
```
Pressure cells (64) ──► STM32 ADC (12-bit) ──► UART ──► Jetson
                                                       │
                              ┌────────────────────────┘
                              ▼
                       Cross-calibration
                              │
                              ▼
                       Pressure map (8×8, Hz)
                              │
                              ▼
                       PTI engine ──► Risk map
                              │
                              ▼
                       CNN-LSTM ──► Forecast (1–5 min ahead)
                              │
                              ▼
                       PID controller ──► 64 PWM van khí
```

### 3.2 Eye-Tracking & AAC Pipeline
```
Stereo cameras ──► Frame sync ──► Pupil detection (OpenCV/dlib)
                                          │
                                          ▼
                                  Gaze vector (3D)
                                          │
                                          ▼
                            Robot arm control (face ROI)
                                          │
                                          ▼
                              AAC grid (cells)
                                          │
                                          ▼
                          Keyword sequence ──► Qwen-LoRA ──► Sentence
                                          │
                                          ▼
                                    TTS + Display
```

### 3.3 Self-Improving Loop
```
(Observations, Action, Outcome) ──► Reward function ──► Update PID + Threshold + AAC priors
```

---

## 4. Hardware Architecture

### 4.1 Bo mạch chính
| Thành phần | Spec | Vai trò |
|------------|------|---------|
| STM32F407VGT6 | 168 MHz, 1 MB Flash | Real-time control |
| Jetson Orin Nano | 40 TOPS, 8 GB | Edge AI |
| Pressure sensor | 64 Velostat + 8 piezocap. | Pressure map |
| Valve manifold | 64× 12V solenoid | Air cell control |
| Camera | 2× Global shutter 640×480 @ 60 Hz | Stereo eye-track |
| Robot arm | 3 DOF (pan-tilt-roll) | Camera positioning |
| Display | 10" touchscreen | UI/AAC |
| Audio | Speaker + mic | TTS / wake word |
| Power | 24V/5A + UPS | Backup 30 min |

### 4.2 Bus & Protocol
- **STM32 ↔ Jetson:** USB-UART @ 921600 baud hoặc Ethernet (ROS2).
- **Camera ↔ Jetson:** MIPI CSI-2 (Jetson native).
- **Sensor matrix ↔ STM32:** SPI multiplexed (8 channel MUX).
- **Valve ↔ STM32:** 8× TLC59401 PWM driver.

### 4.3 Safety
- *Watchdog timer* ở STM32; auto-deflate khi MCU lỗi.
- *Pressure limit:* Mỗi ô < 80 mmHg (safety cap).
- *Emergency stop:* Hardware button → cut-off 24V.
- *Redundant sensor:* Piezocapacitive validate Velostat.

---

## 5. Software Architecture

### 5.1 Module layout (Jetson side)
```
/opt/aac_cushion/
├── core/
│   ├── ros2_node.py          # ROS2 entry
│   ├── state_machine.py      # System state
│   └── safety_gate.py        # Hard safety checks
├── perception/
│   ├── pressure_map.py       # Pressure + PTI
│   ├── eye_tracker.py        # Pupil + gaze
│   └── camera_positioner.py  # Robot arm
├── control/
│   ├── pid_cushion.py        # 64 PID loops
│   └── servo_arm.py          # Arm kinematics
├── ai/
│   ├── cnn_lstm.py           # Risk forecast
│   ├── qwen_lora.py          # AAC sentence gen
│   └── feature_extractor.py
├── aac/
│   ├── grid.py               # AAC UI state
│   ├── predictor.py          # Word prediction
│   └── tts.py                # Text-to-speech
├── self_improve/
│   ├── reward.py
│   ├── bandit.py
│   └── updater.py
└── utils/
    ├── config.py
    ├── logger.py
    └── repro.py
```

### 5.2 STM32 firmware layout
```
stm32_firmware/
├── Core/Src/
│   ├── main.c
│   ├── adc_dma.c
│   ├── spi_mux.c
│   ├── pwm_valve.c
│   ├── uart_ros.c
│   └── watchdog.c
├── Core/Inc/
└── Drivers/
```

### 5.3 ROS2 Topics
| Topic | Type | Rate | Producer → Consumer |
|-------|------|------|---------------------|
| `/pressure/raw` | Float32MultiArray | 10 Hz | STM32 → Jetson |
| `/pressure/calibrated` | Float32MultiArray | 10 Hz | Jetson |
| `/risk/map` | Float32MultiArray | 1 Hz | Jetson |
| `/cushion/cmd` | Float32MultiArray | 10 Hz | Jetson → STM32 |
| `/gaze/vector` | Vector3 | 30 Hz | Jetson |
| `/aac/grid` | Image | 30 Hz | Jetson → UI |
| `/aac/sentence` | String | event | Jetson → TTS |
| `/arm/cmd` | JointState | 10 Hz | Jetson → Arm MCU |
| `/system/safety` | Bool | 50 Hz | Jetson → All |

### 5.4 Quality attributes
- *Latency:* pressure→valve < 200 ms; gaze→action < 100 ms.
- *Throughput:* 64 pressure @ 10 Hz; 2× camera @ 30 fps.
- *Reliability:* MTBF > 1000 h.
- *Privacy:* Không gửi patient data ra ngoài thiết bị.

---

## 6. ML Model Architecture

### 6.1 PTI Engine (Pressure-Time-Intensity)
```
PTI(t) = ∫₀ᵗ (P(τ)/P_th(τ)) · w_posture(τ) dτ
```
- Đầu vào: pressure map (8×8), posture class (3), time window (60 s).
- Đầu ra: PTI per cell + risk map (8×8).

### 6.2 CNN-LSTM Forecaster
```
Input: 60 frames × (8×8 + posture one-hot)  ──► CNN (8×8 → features) ──► LSTM(2 layers, 128 hidden) ──► Dense ──► Risk(1–5 min ahead)
```
- Loss: weighted MSE (ưu tiên vùng sacrum).
- Train: leave-one-subject-out.

### 6.3 Qwen-0.5B + LoRA
- Base: `Qwen/Qwen2-0.5B-Instruct`
- LoRA: r=8, alpha=16, target=q_proj+v_proj
- Dataset: 50 mẫu câu AAC Việt-Anh do bệnh nhân/nhân viên y tế ghi âm.
- Quantization: INT8 cho Jetson.

### 6.4 Self-Improving (Contextual Bandit)
- State: (peak pressure trend, AAC success rate, user comfort)
- Action: (ΔP threshold, ΔPID gain, ΔAAC top-k)
- Reward: composite (low peak + low TOT + high comfort).

---

## 7. Deployment Topology

Xem `diagrams/09_deployment_diagram.png`.

```
┌─────── Bedside ───────┐  ┌─────── Cloud (optional) ──────┐
│ Jetson + STM32 + mat  │  │ Update LoRA weights, datasets│
│ + camera + arm + UI   │  │ (only when user consent)     │
└───────────────────────┘  └────────────────────────────────┘
```

---

## 8. Verification & Validation

### 8.1 Unit test (theo ARS evidence rules)
- Mỗi module có ≥ 1 unit test pass CI.
- Coverage ≥ 70%.

### 8.2 Integration test
- Pipeline e2e: sensor → AI → control → UI (xem `experiments/exp05_pipeline_e2e.py`).

### 8.3 Validation
- Volunteer thử nghiệm (≥ 5 người khỏe mạnh).
- Load simulator (Tekscan FSA calibration).

### 8.4 Safety
- Failure mode checklist theo ARS M1–M7 (xem `docs/03_Methodology`).
