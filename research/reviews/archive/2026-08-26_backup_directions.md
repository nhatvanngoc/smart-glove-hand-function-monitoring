# Dự phòng: các hướng sống sót sau kill-test (2026-08-26)

## Hướng 2 — "Longitudinal Gait Variability as Early Marker for Neuromuscular Decline in Aging" (DỰ PHÒNG)

### Kill-test: novelty claim bị đánh bại ở 2/3 chân
- **"Gait variability là early marker của decline" → ĐÃ THIẾT LẬP, không mới:**
  - Gait variability = "salient biomarker of impaired neuromuscular control", nhạy hơn mean-level (bioRxiv 2026, SPPB stratification).
  - Step-width/stride-time variability **dự đoán fall risk & mobility disability** (Sci Rep 2025).
  - **Longitudinal prospective:** gait variability **dự đoán chuyển hóa PD ~4.5 năm trước chẩn đoán** (Neurology 2019, PMID 31294853); stride-time variability → **frailty** (Healthcare 2025).
- **"Longitudinal personal-baseline monitoring" → ĐÃ LÀM:**
  - AMBIENT vision sensor theo dõi gait dọc ở dementia (2019).
  - **ElderNet** (npj Digital Medicine 2026): **self-supervised learning** wrist accelerometer, theo dõi gait liên tục, "earlier detection of mobility decline", "personalized interventions informed by an individual's unique mobility patterns" → trúng cả "personal baseline" + "SSL" + "decline".
- **Chân novelty THẬT = "drift-robust separation: biological variability vs sensor drift vs noise"** → **đây CHÍNH LÀ candidate measurement-integrity cũ** (CLM-NOV-003). Không phải ý mới; chỉ là khoác áo ứng dụng gait-variability-aging.

### Rủi ro kỹ thuật
- Gait variability thường đo bằng **IMU spatiotemporal** (stride time/length), KHÔNG phải "kinetic variability" từ áp lực. Dùng Velostat (vốn drift) để đo **kinetic variability tinh vi** là **tự mâu thuẫn** (sensor drift có thể lớn hơn biological variability cần phát hiện).

### Xếp loại
- Hướng 2 = **measurement-integrity candidate** + ứng dụng gait-variability-aging. Novelty thật nằm ở drift-robust separation (như cũ). Biomarker + monitoring **không mới** → đừng claim.
- Giữ làm **dự phòng**, KHÔNG phải hướng mới.

## Hội tụ quan trọng (nói thật với owner)
Cả 2 hướng sống sót (C và 2) đều quy về **MỘT lõi novelty duy nhất**:
> **"Biến đặc tính trôi/trễ VỐN là điểm yếu của cảm biến giá rẻ thành TÍN HIỆU hữu ích"** — C dùng nó để đo độ cứng mô; Hướng 2 dùng nó để tách drift khỏi biến thiên sinh học.

Đây chính là measurement-integrity angle mình đã tìm ra từ đầu. Các ứng dụng (tissue stiffness / gait variability / gait monitoring) đều đã có người làm; **cái lõi "repurpose sensor flaw" mới là phần chưa bị chiếm trọn**, và nó cần **1 thí nghiệm gate** để chứng minh khả thi.

## Hai lựa chọn còn lại (owner quyết)
1. **Hướng C** — máy sàng lọc **độ cứng mô gan chân** giá rẻ (ứng dụng loét chân tiểu đường). Gate: Velostat có phân giải được độ cứng mô trên nền drift của nó không?
2. **Hướng 2** — theo dõi **gait variability** drift-robust ở người già. Gate: tách được biological variability khỏi sensor drift không?

Cả hai đều **bench-testable** (phantom), **human-urgent**, và novelty nằm ở lõi "repurpose sensor flaw" — KHÔNG nằm ở ứng dụng.
