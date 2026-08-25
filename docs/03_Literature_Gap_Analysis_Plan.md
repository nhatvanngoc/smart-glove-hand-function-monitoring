# 03 — Kế hoạch phân tích khoảng trống nghiên cứu (2025–2026)

> **Ngày:** 2026-08-25 · **Trạng thái:** KẾ HOẠCH — **chưa có kết quả rà soát**. Đây là quy trình phải chạy **trước khi build hardware** và **trước khi claim bất kỳ novelty nào**.
> **Nguyên tắc chống ảo giác:** "không tìm thấy trong một truy vấn" chỉ cho phép ghi `UNVERIFIED`, **không** chứng minh "chưa có ai làm". Mọi nguồn vào `research/evidence/SOURCE_LEDGER.csv` chỉ sau khi xác minh tiêu đề/tác giả/venue/năm/DOI/URL và đoạn văn hỗ trợ đúng claim.

---

## 1. Mục tiêu

Tìm một **khoảng trống đủ sâu** để biến "smart insole" thành nghiên cứu khoa học — cụ thể là xác định mức prior art của **4 ứng viên novelty chính**:

- **E + D (ưu tiên):** tách Δ_biology khỏi Δ_sensor + phát hiện thay đổi dọc (longitudinal change detection).
- **A:** drift-resistant estimation qua nhiều phiên.
- **B:** cross-session generalization (train ngày 1 → đúng ngày 30).
- **C:** personal baseline (không retrain toàn bộ khi đổi người).

---

## 2. Chủ đề tìm kiếm (10 nhóm — từ chỉ thị chủ dự án)

| # | Nhóm | Truy vấn gợi ý (tiếng Anh) |
|---|---|---|
| 1 | Velostat + plantar pressure | `Velostat insole pressure sensor characterization` |
| 2 | 3D-GRF estimation | `smart insole machine learning 3D ground reaction force estimation` |
| 3 | COP estimation | `center of pressure estimation insole machine learning` |
| 4 | sensor drift / hysteresis | `Velostat drift hysteresis long-term`, `piezoresistive sensor drift compensation` |
| 5 | cross-session generalization | `wearable gait model cross-session generalization calibration` |
| 6 | personal calibration | `personal calibration insole pressure GRF` |
| 7 | longitudinal gait monitoring | `longitudinal gait monitoring wearable drift` |
| 8 | knee OA biomechanics | `knee osteoarthritis gait ground reaction force center of pressure` |
| 9 | GNN / ST-GCN cho gait | `spatio-temporal graph convolution gait ground reaction force` |
| 10 | Edge/INT8 deployment | `RK3588 NPU INT8 inference latency gait` |

---

## 3. Quy trình mỗi nhóm

1. **Log truy vấn** trước khi tìm (auditable):
   ```bash
   python scripts/research_log.py --kind search --engine web \
     --query '...' --purpose 'gap analysis nhóm N' --status complete \
     --summary '...' --sources SRC-...
   ```
2. **Thu thập candidate** (web search, Google Scholar, arXiv, PubMed) — ghi raw vào `research/cache/` (ignored).
3. **Xác minh 5 yếu tố** mỗi nguồn: tiêu đề, tác giả, venue, năm, DOI/URL + **đoạn văn hỗ trợ đúng claim**.
4. Ghi vào `research/evidence/SOURCE_LEDGER.csv` với `verification_status ∈ {VERIFIED, PARTIAL, UNVERIFIED, REJECTED}` và `verified_scope`.
5. Cập nhật ma trận dưới đây (mục 5).
6. Đối với mỗi ứng viên novelty, kết luận một trong: **GAP confirmed (có bằng chứng) / OVERLAP (prior art đã có) / UNRESOLVED (chưa đủ dữ liệu)**.

---

## 4. Tiêu chí "gap đủ sâu"

Một khoảng trống chỉ được claim khi **cả 3** điều kiện sau có bằng chứng:
1. Các công trình gần nhất được trích dẫn đầy đủ và **được đọc đúng phạm vi** (không chỉ abstract).
2. Chỉ ra **khác biệt cụ thể** (về drift handling, cross-session, cost, deployment) chứ không phải "chưa thấy bài tích hợp".
3. Khác biệt đó **có thể đo được** bằng benchmark định lượng (vd: cross-session error, false-change rate).

---

## 5. Ma trận theo dõi (điền dần — hiện trống)

| Nhóm | Số nguồn candidate | Số VERIFIED | Phát hiện chính | Ảnh hưởng novelty (E/D/A/B/C) | Trạng thái |
|---|---|---|---|---|---|
| 1 Velostat+plantar | 0 | 0 | — | — | CHƯA LÀM |
| 2 3D-GRF | 0 | 0 | — | — | CHƯA LÀM |
| 3 COP | 0 | 0 | — | — | CHƯA LÀM |
| 4 drift/hysteresis | 0 | 0 | — | — | CHƯA LÀM |
| 5 cross-session | 0 | 0 | — | — | CHƯA LÀM |
| 6 personal calib | 0 | 0 | — | — | CHƯA LÀM |
| 7 longitudinal | 0 | 0 | — | — | CHƯA LÀM |
| 8 knee OA | 0 | 0 | — | — | CHƯA LÀM |
| 9 GNN/ST-GCN | 0 | 0 | — | — | CHƯA LÀM |
| 10 edge/INT8 | 0 | 0 | — | — | CHƯA LÀM |

---

## 6. Kết luận tạm thời (đã biết từ chỉ thị chủ dự án — vẫn phải xác minh)

> Literature 2025–2026 **đã có** smart insole + ML ước lượng 3D-GRF; pressure insole + IMU + ML; spatiotemporal GCN cho continuous 3D-GRF; GRF liên quan knee OA. Do đó **"Velostat + GNN → 3D-GRF" không đủ novelty** — đây là cảnh báo chiến lược của chủ dự án, sẽ được kiểm chứng bằng quy trình trên (chưa phải kết luận có bằng chứng).

---

## 7. Đầu ra mong đợi

- `research/evidence/SOURCE_LEDGER.csv` cập nhật.
- Bảng tổng hợp prior art (sensor, ground-truth, drift handling, model, cost) trong một tài liệu rà soát `research/reviews/20XX-XX-XX_literature_gap.md`.
- Kết luận novelty cho E/D/A/B/C + cập nhật `research/claims/CLAIM_LEDGER.csv` (SUPPORTED/UNVERIFIED/CONTRADICTED).
- Quyết định chính thức của chủ dự án về novelty cuối cùng trong `research/context/DECISION_LOG.md`.
