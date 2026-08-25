# 01 — Định nghĩa đề tài (tinh chỉnh lần 2)

> **Ngày cập nhật:** 2026-08-25 (chỉ thị chủ dự án, phần 2)
> **Học sinh:** Văn Ngọc Nhật Anh — THPT Quảng Trị
> **Nguồn gốc quyết định:** `research/context/CONVERSATION_2026-08-25.md` (phần 2) + `research/context/DECISION_LOG.md`.
> **Trạng thái bằng chứng:** tài liệu **định hướng**. Mọi tuyên bố novelty, hiệu năng, độ chính xác đang ở mức **giả thuyết** cho đến khi có kiểm chứng. Không có gì ở đây là kết quả đã đo.

---

## 1. Tên đề tài

**Tiếng Việt:** Hệ thống lót giày Edge-AI ước lượng liên tục lực phản lực mặt đất 3 chiều (3D-GRF) và quỹ đạo tâm áp lực (COP) có khả năng chống trôi dạt, để phát hiện sớm sự thay đổi động học dáng đi và theo dõi đáp ứng phục hồi ở người có nguy cơ hoặc mắc thoái hóa khớp gối (knee OA).

**Tiếng Anh:** Drift-robust wearable plantar sensing with Edge-AI for continuous 3D-GRF and COP estimation, toward longitudinal gait-change detection and rehabilitation-response monitoring in knee osteoarthritis.

**Pitch 1 câu (nói với giáo viên):**
> "Em không làm một chiếc lót giày chỉ để đo lực. Em muốn giải quyết **drift của cảm biến áp lực** để biến smart insole thành hệ thống đo động học **liên tục và ổn định theo thời gian**, từ đó theo dõi thay đổi thật của dáng đi qua nhiều ngày và hỗ trợ phát hiện sớm suy giảm chức năng cũng như đánh giá hiệu quả phục hồi ở người có nguy cơ thoái hóa khớp gối."

---

## 2. Mục tiêu ba tầng + tuyên bố bị cấm

| Tầng | Mục tiêu |
|---|---|
| **Khoa học** | Continuous **drift-robust** 3D kinetic estimation from wearable plantar sensing. |
| **Ứng dụng** | Longitudinal detection of abnormal gait changes. |
| **Y sinh** | Hỗ trợ theo dõi thay đổi chức năng vận động và đáp ứng phục hồi ở người có nguy cơ/mắc knee OA. |

**Tuyên bố bị cấm (sẽ làm mất điểm + sai khoa học):**
- ❌ chẩn đoán OA; ❌ điều trị OA; ❌ thay thế bác sĩ; ❌ thay thế X-ray/MRI/force plate; ❌ "GRF ⇒ OA".
- ❌ "triệt tiêu drift" — chỉ được nói "giảm drift" kèm biên định lượng.

---

## 3. Vì sao đề tài xuất hiện (tóm tắt lịch sử)

Đã thử nhiều hướng (phantom hồi sức sơ sinh, cầm máu cấp cứu, AAC, hỗ trợ nuôi ăn, tactile sensing, orthosis, rehabilitation, smart phantom…). Vấn đề chung: **human impact tốt nhưng novelty yếu**, hoặc **clinical proxy khó / IRB khó / mechanical complexity / prior art quá đông / khó chứng minh "tốt hơn cái đang có"**.

Sau khi reverse-engineer các dự án ISEF/ViSEF, nguyên tắc thống nhất là **không bắt đầu từ "người yếu thế cần gì?"** mà từ:

> **Bottleneck khó → biến ẩn khó đo → phương pháp mới → benchmark định lượng → impact.**

---

## 4. Insight quan trọng nhất (novelty)

> ❌ **"Velostat + GNN để dự đoán 3D-GRF" chưa đủ mới.** Literature 2025–2026 đã có: smart insole + ML ước lượng 3D-GRF; pressure insole + IMU + ML; spatiotemporal GCN cho continuous 3D-GRF; GRF liên quan knee OA. Nếu chỉ làm vậy, dự án có nguy cơ rơi về ~70–80 điểm.

Trọng tâm khoa học thật sự là:

> **Longitudinal, drift-robust kinetic monitoring** — theo dõi liên tục sự thay đổi động học dáng đi của **một cá nhân trong thời gian dài**, đồng thời **phân biệt thay đổi sinh học thật với drift của cảm biến và biến thiên giữa các ngày**.

Tức là tách:
```
ΔCOP = Δ_biology + Δ_sensor + Δ_environment
```
và tìm cách cô lập **Δ_biology** khỏi **Δ_sensor**.

---

## 5. Mục tiêu tối thượng

Không phải "đo GRF" (GRF chỉ là **phương tiện**). Mục tiêu là:

> Biến phép đo động học vốn phải làm trong phòng lab bằng force plate thành **phép đo wearable liên tục**, đủ **ổn định theo thời gian** để phát hiện thay đổi thật trong dáng đi của từng cá nhân — *"mang phòng lab đi cùng người bệnh"*.

| Trước (phòng lab) | Sau (đề xuất) |
|---|---|
| Người bệnh → phòng lab → force plate → vài bước → 1 phép đo | Smart insole → GRF+COP → **hàng nghìn bước** → **nhiều ngày/tuần** → gait trajectory theo thời gian |

---

## 6. Liên hệ knee OA (và giới hạn suy luận)

Knee OA không chỉ là hình ảnh cấu trúc khớp; còn liên quan đến cách chịu tải, phân bố lực, braking/propulsion, bất đối xứng hai chân, biến đổi COP, thay đổi gait mechanics. Chuỗi hợp lệ:

```
Gait → GRF/COP → Knee loading pattern
```

Nhưng **không** được claim `GRF ⇒ OA` hay "hệ thống chẩn đoán thoái hóa khớp" — claim quá mạnh. Mối liên hệ với tải khớp gối (vd qua Knee Adduction Moment — KAM) là **gián tiếp**; xem `docs/02_Theoretical_Foundation.md` mục 2.4.

---

## 7. Câu hỏi nghiên cứu (2 tầng)

**RQ1 (lõi — novelty nằm ở đây):**
> Liệu một hệ thống lót giày dựa trên cảm nhận áp lực có thể duy trì ước lượng 3D-GRF/COP **đủ ổn định qua nhiều phiên sử dụng** để phân biệt **sự thay đổi động học thực sự của dáng đi** với **drift cảm biến** và **biến thiên thông thường** hay không?

**RQ2 (ứng dụng):**
> Liệu các thay đổi động học được phát hiện có thể được dùng để theo dõi sự **suy giảm hoặc cải thiện** chức năng vận động liên quan đến knee OA hay không?

---

## 8. DNA của đề tài

```
Wearable pressure sensing
        ↓
3D-GRF + COP
        ↓
Drift-aware estimation
        ↓
Personal baseline
        ↓
Longitudinal kinetic change
        ↓
Early functional warning
        ↓
Rehabilitation monitoring
```

---

## 9. Pipeline dự kiến

```
        SMART INSOLE
             │  Velostat pressure
             ▼
       ADC / Arduino (thu thập, quét, sampling, preprocessing)
             ▼
   Spatial pressure map P(x,y,t)
             ▼
 Spatio-temporal graph
             ▼
       Edge-AI / GNN (INT8, RK3588)
      ┌──────┴──────┐
      ▼             ▼
   3D-GRF          COP
      │             │
      └──────┬──────┘
             ▼
    Drift correction
             ▼
   Personal baseline
             ▼
 Longitudinal deviation
             ▼
   Gait change detection
             ▼
 Rehabilitation monitoring
```

---

## 10. Killer experiment (cốt lõi novelty — phải làm được để đứng vững)

Không chỉ báo "RMSE 5%". Phải chứng minh được:

| Điều kiện | Kết quả kỳ vọng |
|---|---|
| **Không** drift correction | error ↑ theo số phiên |
| **Có** drift correction | error ≈ hằng số |
| Quan trọng hơn | **False Change Detection ↓** |

**Giả thuyết:** sau ~30 ngày sử dụng, phương pháp đề xuất giảm sai lệch liên-phiên và giảm false gait-change detection đáng kể so với calibration thông thường.

---

## 11. Các ứng viên novelty (A–E) và lựa chọn

| ID | Hướng | Ghi chú |
|---|---|---|
| A | Drift-resistant estimation | giữ accuracy sau nhiều session |
| B | Cross-session generalization | train ngày 1 vẫn đúng ngày 30 |
| C | Personal baseline | không retrain toàn bộ khi đổi người |
| D | Longitudinal change detection | phát hiện thay đổi nhỏ trước ngưỡng rõ ràng |
| E | Biology-vs-sensor change separation | tách "người đổi" khỏi "sensor đổi" |

**Lựa chọn chiến lược:** **E + D** là hướng hấp dẫn nhất (theo chủ dự án). Novelty phải được xác lập bằng **literature gap analysis 2025–2026** trước khi claim — xem `docs/03`.

---

## 12. Phần cứng tái sử dụng & vai trò

| Thành phần | Vai trò dự kiến | Trạng thái kiểm chứng |
|---|---|---|
| **Velostat** | ma trận cảm nhận áp lực | cần đặc trưng drift/hysteresis/creep (chưa đo) |
| **Arduino Mega** | acquisition, quét, sampling, preprocessing | 16 ngõ analog — nếu >16 ô phải multiplex (đánh đổi tần số) |
| **Orange Pi 5 Pro / RK3588** | signal processing, GNN inference, INT8 quantization, real-time edge, logging | NPU ~6 TOPS là **spec**, chưa benchmark |

---

## 13. Đối tượng & lộ trình nghiên cứu theo tầng (giảm rủi ro IRB)

| Giai đoạn | Đối tượng | Mục tiêu |
|---|---|---|
| 1 | Healthy participants / phantom / controlled loading | đặc trưng cảm biến + dữ liệu |
| 2 | Validation với force plate | sai số 3D-GRF/COP |
| 3 | Nghiên cứu gait patterns | biến thiên liên-phiên |
| 4 | (nếu đủ điều kiện đạo đức & đối tác) người có knee OA | theo dõi dọc |

> Không nhất thiết tuyển bệnh nhân ngay từ đầu — điều này giảm đáng kể rủi ro IRB.

---

## 14. Điểm mạnh / điểm yếu

**Mạnh:** (1) ground truth tốt (force plate → validation định lượng); (2) Embedded Systems rất tự nhiên (sensor → acquisition → signal processing → edge inference → real-time); (3) ML thật (dữ liệu P(x,y,t) phù hợp graph/spatiotemporal); (4) có biomechanics thật; (5) human impact (rehab + knee OA); (6) mở rộng được (stroke, Parkinson, gait asymmetry, sports, fall-risk).

**Yếu (phải nhớ):** novelty **chưa đủ** nếu chỉ là "Velostat → GNN → 3D-GRF → OA".

---

## 15. Điểm dự kiến (đánh giá chiến lược — KHÔNG phải điểm thật của ban giám khảo)

| Đề tài | Tốt | Ceiling nếu làm cực tốt |
|---|---|---|
| Smart insole 3D-GRF/COP + drift robustness | 78–82 | 90–93+ |
| (các đề tài cũ đã cân nhắc) | 58–80 | 80–89 |

> Đây là đánh giá chiến lược novelty+validation+impact+feasibility, để định hướng ưu tiên — không trích dẫn làm kết quả.

---

## 16. Bước tiếp theo (bắt buộc)

**Đừng vội build hardware.** Việc kế tiếp là **literature gap analysis 2025–2026** quanh các chủ đề:

Velostat + plantar pressure · 3D-GRF estimation · COP estimation · sensor drift/hysteresis · cross-session generalization · personal calibration · longitudinal gait monitoring · knee OA biomechanics · GNN/ST-GCN cho gait · Edge/INT8 deployment.

Mục tiêu: tìm một **khoảng trống đủ sâu** để biến "smart insole" thành nghiên cứu khoa học, không phải sản phẩm IoT/AI. Quy trình & ma trận theo dõi: `docs/03_Literature_Gap_Analysis_Plan.md`.

---

## 17. Tài liệu liên quan

- `docs/02_Theoretical_Foundation.md` — cơ sở lí thuyết (cơ sinh học, cảm biến, drift, GNN, metrics, edge).
- `docs/03_Literature_Gap_Analysis_Plan.md` — kế hoạch rà soát gap.
- `research/protocols/SMART_INSOLE_CRITIQUE_5_SEATS.md` — phản biện 5 ghế (đã cập nhật killer experiment).
- `research/context/DECISION_LOG.md` — quyết định chính thức.
