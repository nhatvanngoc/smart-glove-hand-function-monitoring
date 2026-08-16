# RISK REGISTER — Sổ rủi ro & Giảm thiểu (ARS Stage 2)
## Hệ thống đệm khí thích ứng tích hợp AAC

> Ngày: 2026-06-14

---

## Rủi ro kỹ thuật

| ID | Rủi ro | L | I | Mitigation | Owner |
|----|--------|---|---|-----------|-------|
| R-T1 | STM32 firmware bug gây treo | M | H | Unit test + WDT + HIL | Student |
| R-T2 | Velostat sensor drift | H | M | Cross-cal + re-cal 30' | Student |
| R-T3 | Piezocapacitive mismatch | M | M | Lab calibration | Student |
| R-T4 | Pump quá nhiệt | L | M | Thermal cut-off 60°C | Student |
| R-T5 | Valve kẹt cơ khí | M | M | Test endurance 100h | Student |
| R-T6 | Camera cable lỏng | M | L | Cable gland + strain relief | Student |
| R-T7 | Robot arm mất bước | M | M | Encoder + stall detect | Student |
| R-T8 | Jetson OOM | M | M | Model quantization + swap | Student |
| R-T9 | Pressure sensor vượt 80 mmHg | L | H | Firmware limit + alarm | Student |

## Rủi ro ML/AI

| ID | Rủi ro | L | I | Mitigation |
|----|--------|---|---|-----------|
| R-M1 | CNN-LSTM overfit | M | H | LOSO CV + dropout + early stop |
| R-M2 | Qwen-LoRA hallucination | H | M | Constrained decoding + ground-truth test |
| R-M3 | Eye-tracking sai khi khuôn mặt quay | M | M | Robot arm recenter |
| R-M4 | Pupil detection fail (mắt nhắm) | M | L | Detect blink → reset |
| R-M5 | PTI false positive | M | M | Threshold conservative |
| R-M6 | Self-improve vượt safety | L | H | Action clamp ±10% + human override |

## Rủi ro nghiên cứu

| ID | Rủi ro | L | I | Mitigation |
|----|--------|---|---|-----------|
| R-R1 | Volunteer injury | L | H | Mannequin trước + informed consent |
| R-R2 | Sample size nhỏ | M | M | n=15 + power analysis |
| R-R3 | Volunteer bias | M | L | Within-subject + Latin square |
| R-R4 | Data leak giữa train/test | M | H | LOSO + no future in past |
| R-R5 | Metric cherry-pick | M | M | Pre-register metrics |

## Rủi ro quản lý dự án

| ID | Rủi ro | L | I | Mitigation |
|----|--------|---|---|-----------|
| R-P1 | Linh kiện thiếu/đắt | H | M | Đặt sớm + backup plan |
| R-P2 | Lịch thi ngắt quãng | M | M | Gantt chart + buffer |
| R-P3 | Thiếu mentor kỹ thuật | M | H | Tìm mentor cộng đồng online |
| R-P4 | Không đạt acceptance criteria | M | H | Iterate sớm + reviewer sớm |

## Rủi ro an toàn & đạo đức

| ID | Rủi ro | L | I | Mitigation |
|----|--------|---|---|-----------|
| R-E1 | Lộ dữ liệu bệnh nhân | L | H | On-device only + encrypt at rest |
| R-E2 | Misuse trên bệnh nhân thật | M | H | Label "research prototype only" |
| R-E3 | Bệnh nhân phụ thuộc quá | M | M | Training + family support |
| R-E4 | AAC sai ngữ cảnh gây hiểu nhầm | M | M | Human-in-the-loop confirm |

## Rủi ro pháp lý & quy định

| ID | Rủi ro | L | I | Mitigation |
|----|--------|---|---|-----------|
| R-L1 | Thiết bị y tế cần FDA/CE | H | H | Rõ ràng "research only", không medical claim |
| R-L2 | Quyền sở hữu trí tuệ | M | M | Tuân thủ license OSS (Qwen, ROS2) |
| R-L3 | Bảo hiểm thiết bị lỗi | L | H | Disclaimer + emergency stop |

---

## Risk review cadence
- Weekly self-review
- Monthly mentor review
- Final integrity gate (ARS Stage 8)

## Mitigation status tracking
- Mỗi risk có owner + due date + status (open / mitigated / closed).
- Lưu ở `outputs/reports/risk_status.md`.
