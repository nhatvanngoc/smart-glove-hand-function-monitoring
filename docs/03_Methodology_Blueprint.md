# METHODOLOGY BLUEPRINT — Phương pháp nghiên cứu (ARS Stage 1 → 2)
## Hệ thống đệm khí thích ứng tích hợp AAC phòng ngừa loét tì đè

> Theo ARS v3.12 framework: Research Question → Method → Artifact → Gate
> Ngày: 2026-06-14

---

## 1. Phương pháp tổng quát
**Design Science Research** (Hevner 2004) theo 7 giai đoạn:
1. Identify problem & motivate (đề cương)
2. Define objectives of solution (RQ brief)
3. Design & develop artifact (system architecture, hardware, software)
4. Demonstrate artifact (prototype, Gazebo simulation)
5. Evaluate (experiments với volunteer + load simulator)
6. Communicate (paper, hội thảo)

**Method triangulation:**
- *Quantitative:* đo áp suất, accuracy, BLEU
- *Qualitative:* phỏng vấn volunteer, UX score
- *Simulation:* Gazebo/ROS2 cho safety

---

## 2. Thiết kế nghiên cứu (Study Design)

### 2.1 Hardware Design (Repeated Measures)
| Yếu tố | Mức | Replicate |
|--------|-----|-----------|
| Loại cảm biến | Velostat thuần / Velostat + Piezocap. | 5 lần × 5 volunteer |
| Loại đệm | Passive alternating / Adaptive PTI / Adaptive + prediction | 5 lần × 5 volunteer |
| Tư thế | Supine / Lateral / Prone | 3 × replicate |

### 2.2 Software/ML Design
- **Within-subject:** Mỗi volunteer dùng 3 prototype theo thứ tự Latin-square.
- **Train/test split:** Pressure map dataset 70/15/15; CNN-LSTM theo leave-one-subject-out.
- **Eye-tracking:** 10 volunteer × 3 điều kiện ánh sáng × 5 target.
- **AAC:** 50 câu mẫu, BLEU-4 / chrF / human rating.

### 2.3 End-to-End Pipeline Test
- 3 tình huống giả lập: (a) tĩnh, (b) xê dịch, (c) tư thế thay đổi.
- Đo: peak pressure, time-over-threshold, eye-tracking accuracy, AAC latency.

---

## 3. Công cụ & môi trường

| Lớp | Công cụ |
|-----|---------|
| Embedded | STM32CubeIDE, ARM GCC, FreeRTOS |
| AI Edge | NVIDIA JetPack, TensorRT, ROS2 Humble |
| ML training | PyTorch (CPU fallback), scikit-learn, numpy/scipy |
| Simulation | Gazebo 11, ROS2 Humble, RViz2 |
| Dashboard | Streamlit, matplotlib |
| Version control | git, DVC cho dataset |
| Doc | Markdown, Mermaid, PlantUML |
| Reproducibility | Docker, repro_lock (ARS v3.3.5) |

---

## 4. Pipeline nghiên cứu (10-stage ARS adaptation)

```
Stage 0  INTAKE           ──► RQ Brief + scope
Stage 1  RESEARCH         ──► Lit Review + RGI
Stage 2  DESIGN           ──► Architecture + Hardware + Software + ML
Stage 3  PROTOTYPE        ──► Chế tạo ma trận, đệm, camera rig, ML models
Stage 4  INTEGRATION      ──► Tích hợp full pipeline trên Jetson
Stage 5  SIMULATION       ──► Gazebo/ROS2 test
Stage 6  EXPERIMENT       ──► Volunteer + load simulator
Stage 7  EVALUATION       ──► Metrics, statistical test
Stage 8  INTEGRITY GATE   ──► Reproducibility + claim audit (ARS v3.8)
Stage 9  REVIEW           ──► Self-review theo academic-paper-reviewer
Stage 10 FINALIZE         ──► Submission package, paper PDF
```

---

## 5. Variables & Measurements

### 5.1 Independent Variables
- `sensor_mode ∈ {velostat_only, hybrid}`
- `control_mode ∈ {alternating, adaptive_pti, adaptive_cnnlstm}`
- `posture ∈ {supine, lateral, prone}`
- `light_condition ∈ {dim, normal, bright_ir}`
- `aac_model ∈ {keyword_only, qwen_lora}`

### 5.2 Dependent Variables
| Biến | Đơn vị | Công cụ đo |
|------|--------|-----------|
| Peak pressure | mmHg | Tekscan FSA, ma trận 8×8 |
| Time over threshold (TOT) | phút | timestamp log |
| PTI score | dimensionless | PTI engine |
| Eye-tracking accuracy | % | ground-truth board |
| AAC latency | ms | system clock |
| BLEU-4 / chrF | 0–100 | nltk/sacrebleu |
| Subjective comfort | Likert 1–7 | questionnaire |

### 5.3 Confounders & Controls
- *Volunteer body mass:* cố định theo nhóm BMI (≤ 4 mức).
- *Ambient temperature:* 22–26°C (theo dõi DHT22).
- *Calibration drift:* re-cal mỗi 30 phút.
- *Lighting:* dimmer + lux meter.

---

## 6. Statistical Plan
- **Power analysis:** n ≥ 15 volunteer để phát hiện effect size d = 0.5, α = 0.05, power = 0.80.
- **Test:** Repeated-measures ANOVA cho pressure; paired t-test cho accuracy; Wilcoxon cho subjective.
- **Multiple comparison:** Holm-Bonferroni.
- **Reporting:** Mean ± SD, 95% CI, p-value, effect size (Cohen's d).

---

## 7. Reproducibility Plan (ARS `repro_lock`)
```yaml
repro_lock:
  environment:
    python: "3.11"
    jetson_pack: "5.1.3"
    ros2: "humble"
    pytorch: "2.3.0"
    qwen_model: "Qwen/Qwen2-0.5B-Instruct"
  stochasticity_declaration: |
    Pressure map: deterministic (no RNG).
    CNN-LSTM training: seed=42, deterministic=True.
    Qwen LoRA: seed=42, deterministic=True.
    Eye-tracking: deterministic via OpenCV.
  dataset:
    pressure_synthetic: "data/synthetic_pressure_v1"
    eye_tracking_ground_truth: "data/eye_gt_v1"
  commands:
    train: "python experiments/exp02_pti_model.py"
    eval: "python experiments/exp05_pipeline_e2e.py"
  container: "docker/Dockerfile"
```

---

## 8. Risk Register (trích)
| ID | Risk | Likelihood | Impact | Mitigation |
|----|------|-----------|--------|-----------|
| R1 | STM32 firmware bug | Medium | High | Unit test + hardware-in-loop |
| R2 | Pressure sensor drift | High | Medium | Cross-calibration + re-cal |
| R3 | Patient privacy | Medium | High | On-device LLM; no cloud upload |
| R4 | Eye-tracking lạc face ROI | Medium | Medium | Robot arm auto-recenter |
| R5 | AAC latency > 2s | Medium | High | Quantized Qwen + caching |
| R6 | Volunteer injury | Low | Critical | IRB-equivalent + load simulator trước |

---

## 9. Deliverables
- ✅ Đề cương (đã nộp)
- ⏳ Prototype vật lý
- ⏳ Dataset + pipeline scripts
- ⏳ Paper (PDF)
- ⏳ Slide thuyết trình
- ⏳ Video demo
- ⏳ Poster A0

---

## 10. Timeline (12 tuần)
| Tuần | Công việc |
|------|-----------|
| 1–2 | Literature + mua linh kiện + layout schematic |
| 3–4 | STM32 firmware + ma trận cảm biến |
| 5–6 | Jetson pipeline + eye-tracking |
| 7 | Qwen LoRA + AAC |
| 8 | Tích hợp + Gazebo |
| 9–10 | Thực nghiệm volunteer + load simulator |
| 11 | Phân tích số liệu + viết báo cáo |
| 12 | Hoàn thiện poster + slide + nộp bài |
