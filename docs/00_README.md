# Adaptive Air Cushion + Eye-Tracking AAC — Dự án Khoa học Kỹ thuật

> **Đề tài:** Nghiên cứu và phát triển hệ thống đệm khí thích ứng dựa trên mô hình áp suất – thời gian tích hợp giao tiếp hỗ trợ người hạn chế vận động trong phòng ngừa loét tì đè
>
> **Học sinh:** Văn Ngọc Nhật Anh — Lớp 11A2, THPT Quảng Trị
> **Lĩnh vực:** Hệ thống nhúng (Embedded Systems)
> **Cuộc thi:** Khoa học Kỹ thuật — Năm học 2026–2027
> **Phiên bản:** 1.0.0 — 2026-06-14

---

## Tổng quan dự án

Hệ thống **tích hợp hai chức năng cốt lõi** cho bệnh nhân hạn chế vận động:
1. **Phòng ngừa loét tì đè** — đệm khí 64 ô tự điều chỉnh theo pressure map & PTI.
2. **Hỗ trợ giao tiếp bằng ánh mắt (AAC)** — stereo eye-tracking + Qwen-0.5B LoRA.

Cùng với **vòng lặp tự cải tiến** cá nhân hóa theo từng người dùng.

---

## Cấu trúc repo

```
adaptive_cushion_aac/
├── README.md                        ← File này
├── docs/                            ← Tài liệu academic (ARS Codex pipeline)
│   ├── 01_RQ_Brief.md
│   ├── 02_Literature_Review.md
│   ├── 03_Methodology_Blueprint.md
│   ├── 04_System_Architecture.md
│   ├── 05_Hardware_Design.md
│   ├── 06_Software_Design.md
│   ├── 07_ML_Models.md
│   ├── 08_Experimental_Protocol.md
│   ├── 09_Risk_Register.md
│   └── 10_References.md
├── diagrams/                        ← Sơ đồ kỹ thuật
│   ├── 01_system_block_diagram.png
│   ├── 02_hardware_schematic.png
│   ├── 03_software_architecture.png
│   ├── 04_data_pipeline.png
│   ├── 05_ml_model_architecture.png
│   ├── 06_pressure_map_flow.png
│   ├── 07_eye_tracking_flow.png
│   ├── 08_aac_ui_mockup.png
│   └── 09_deployment_diagram.png
├── src/                             ← Source code
│   ├── stm32_firmware/              ← STM32 reference firmware
│   ├── jetson_pipeline/             ← Jetson AI pipeline
│   ├── pressure_model/              ← PTI + CNN-LSTM
│   ├── eye_tracking/                ← Eye tracking pipeline
│   ├── aac_assistant/               ← Qwen-LoRA AAC
│   └── integration/                 ← Full integration
├── experiments/                     ← Các thí nghiệm
│   ├── exp01_hybrid_calibration.py
│   ├── exp02_pti_model.py
│   ├── exp03_cnn_lstm.py
│   ├── exp04_eye_tracking.py
│   ├── exp05_pipeline_e2e.py
│   └── exp06_qwen_lora.py
├── data/                            ← Dataset (synthetic + script)
├── pipeline/                        ← End-to-end pipeline scripts
│   ├── stage0_intake.py
│   ├── stage1_research.py
│   ├── stage2_design.py
│   ├── stage3_prototype.py
│   ├── stage4_evaluation.py
│   └── stage5_submission.py
├── tests/                           ← Unit + integration tests
└── outputs/                         ← Generated artifacts
    ├── figures/
    ├── logs/
    └── reports/
```

---

## Pipeline nghiên cứu (ARS v3.12 adaptation)

| Stage | Name | Output |
|-------|------|--------|
| 0 | INTAKE | RQ Brief + scope (docs/01) |
| 1 | RESEARCH | Lit review + RGI (docs/02) |
| 2 | DESIGN | Architecture + HW + SW + ML (docs/04–07) |
| 3 | PROTOTYPE | Code + diagram (src/, diagrams/) |
| 4 | INTEGRATION | Pipeline scripts (pipeline/) |
| 5 | SIMULATION | Gazebo + synthetic data |
| 6 | EXPERIMENT | Volunteer + load simulator (experiments/) |
| 7 | EVALUATION | Metrics, statistical test |
| 8 | INTEGRITY GATE | Reproducibility + claim audit |
| 9 | REVIEW | Self-review (academic-paper-reviewer) |
| 10 | FINALIZE | Submission package |

---

## Công nghệ sử dụng

| Layer | Stack |
|-------|-------|
| Embedded | STM32F407, FreeRTOS, SPI, UART |
| Edge AI | Jetson Orin Nano, JetPack 5.1.3, TensorRT |
| AI/ML | PyTorch, scikit-learn, MediaPipe, Qwen-0.5B + LoRA |
| Robotics | ROS2 Humble, Gazebo 11 |
| Vision | OpenCV 4.5, OpenCV GStreamer |
| Web UI | Streamlit |
| Reproducibility | Docker, repro_lock (ARS v3.3.5) |

---

## Cách chạy nhanh

### 1. Cài đặt
```bash
cd adaptive_cushion_aac
pip install -r requirements.txt
```

### 2. Chạy pipeline end-to-end (synthetic)
```bash
python pipeline/stage4_evaluation.py
python experiments/exp05_pipeline_e2e.py
```

### 3. Generate figures
```bash
python pipeline/stage3_prototype.py  # tạo diagrams
```

### 4. Build docs
```bash
cd docs && pandoc 01_RQ_Brief.md -o 01_RQ_Brief.pdf
```

---

## Tài liệu academic

Toàn bộ tài liệu được viết theo chuẩn **ARS Codex academic-pipeline v3.12.0**:
- RQ Brief chuẩn Socratic
- Lit Review PRISMA-style với 3-Layer citation
- Methodology với reproducibility lock
- Architecture với safety gate
- ML models với failure mode checklist

Xem chi tiết ở `docs/00_README.md` và các file `01_*.md` → `10_*.md`.

---

## Liên hệ
- Học sinh: Văn Ngọc Nhật Anh
- Trường: THPT Quảng Trị
- Giáo viên hướng dẫn: (cập nhật)

---

## Ghi chú phát triển
- Dự án dùng skill suite **academic-research-suite** (ARS Codex v0.1.12) cho việc viết paper.
- Mọi file Markdown tuân theo Google style docstring.
- Mọi code Python ≥ 3.10; STM32 firmware C99.
