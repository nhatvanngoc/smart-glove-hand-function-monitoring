# 30 — Chuyển hướng đề tài: Smart Insole Edge-AI (3D-GRF & COP)

> **Ngày ghi nhận quyết định:** 2026-08-25
> **Học sinh:** Văn Ngọc Nhật Anh — THPT Quảng Trị
> **Trạng thái:** Quyết định của chủ dự án (owner directive) — đã ghi vào `research/context/DECISION_LOG.md` (DEC-TOPIC-001). Tài liệu này là khung định hướng, **không phải** tuyên bố kết quả đã được kiểm chứng.

---

## 1. Quyết định đổi hướng (tóm tắt)

Dự án **chính thức từ bỏ** ý tưởng "đệm khí thích ứng (adaptive air cushion) + AAC" do có quá nhiều rủi ro đồng thời:

- Cơ khí khí nén (pneumatic): phức tạp chế tạo, rủi ro rò khí, bảo trì.
- Cảm biến Velostat dùng để đo áp lực tĩnh tuyệt đối (mmHg) — kém tin cậy do trôi dạt (drift), trễ (hysteresis), creep và nhạy nhiệt.
- Kiểm chứng lâm sàng đòi hỏi quy mô, thời gian và IRB/SRC vượt quá phạm vi một dự án ISEF.

Thay vào đó, dự án chuyển sang đề tài có **chiều sâu khoa học và tính khả thi cao hơn**:

> **Hệ thống lót giày thông minh (Smart Insole) sử dụng Edge-AI để ước lượng lực phản lực mặt đất 3 chiều (3D-GRF) và quỹ đạo tâm áp lực (COP).**
>
> **Smart Insole with Edge-AI for 3D Ground Reaction Force (3D-GRF) and Center-of-Pressure (COP) trajectory estimation.**

Toàn bộ tài liệu `docs/01`–`29`, `cad/`, `simulation/` (khí nén/SOFA) và phần AAC/eye-tracking thuộc đề tài cũ được giữ nguyên làm **kho lưu trữ lịch sử (historical archive)** để bảo toàn provenance, **không** được hợp nhất ngầm vào kiến trúc mới (xem `AGENTS.md` quy tắc 2).

---

## 2. Trọng tâm khoa học của đề tài mới

### 2.1 Vấn đề cốt lõi

Cảm biến áp lực giá rẻ (Velostat/Linqstat) có đáp ứng **phi tuyến, trễ (hysteresis), trôi dạt (drift)** theo nhiệt độ và biến dạng vật liệu, và trôi dạt **tăng dần qua nhiều phiên đo**. Vì vậy, đọc trực tiếp điện trở/ADC rồi đổi ra áp lực tĩnh tuyệt đối là **không đáng tin cậy**.

### 2.2 Giả thuyết nghiên cứu (chưa kiểm chứng)

1. **Kháng trôi dạt qua đạo hàm (drift-resistance via dP/dt).** Thay vì đo áp lực tĩnh, hệ thống dùng **đạo hàm biến thiên áp lực theo thời gian dP/dt** để giảm ảnh hưởng của thành phần trôi dạt chậm (offset drift). Lưu ý: đây là **giảm (attenuation)**, không phải **triệt tiêu (elimination)** — drift còn gây nhiễu lên biên độ (gain/sensitivity drift) và phải được đặc trưng hoá bằng thực nghiệm.
2. **Suy ra lực trượt ngang (Fx, Fy) từ áp lực dọc (Fz).** Kiến trúc đề xuất là **Spatio-Temporal Graph Neural Network (ST-GNN)** mô hình hoá bàn chân như một **đồ thị giải phẫu** (các vùng gót, vòm, khớp bàn–ngón, ngón chân là node; cạnh theo quan hệ giải phẫu/cơ sinh học), từ chuỗi áp lực 16+ kênh suy ra Fx, Fy, Fz và quỹ đạo COP. ST-GNN là **một phương án**, phải so với baseline đơn giản hơn (hồi quy tuyến tính, CNN, LSTM) trước khi được chấp nhận.

### 2.3 Phần cứng phối hợp

| Thành phần | Vai trò | Lưu ý kiểm chứng |
|---|---|---|
| **Arduino Mega (ATmega2560)** | Thu thập dữ liệu 16 kênh ADC tốc độ cao | 16 ngõ analog; nếu ma trận >16 ô phải multiplex → đánh đổi tần số lấy mẫu. Cần đo tần số thực tế. |
| **Orange Pi 5 Pro (RK3588S)** | Suy luận mô hình AI tại biên (edge inference) | NPU ~6 TOPS là **thông số nhà sản xuất**; phải benchmark latency/throughput/năng lượng thực tế sau khi lượng tử hoá (INT8). |
| **Ma trận Velostat trong đế giày** | Cảm biến áp lực dọc (Fz) | Số ô, hình học điện cực, dây dẫn, độ bền khi gập — chưa chốt. |

---

## 3. Câu hỏi nghiên cứu (bản nháp — chờ chủ dự án chốt)

- **RQ chính:** Với phần cứng giá rẻ (Velostat + Arduino Mega + Orange Pi 5 Pro), có thể ước lượng 3D-GRF và quỹ đạo COP ở độ chính xác nào, và chiến lược dP/dt + mô hình không–thời gian cải thiện độ ổn định qua nhiều phiên đo ra sao so với baseline?
- **SQ1 (drift):** dP/dt làm giảm sai số trôi dạt qua phiên đo bao nhiêu (định lượng bằng residual drift so với nền tĩnh dài)?
- **SQ2 (mô hình):** ST-GNN có vượt trội hơn baseline tuyến tính/LSTM một cách có ý nghĩa trên cùng dữ liệu không?
- **SQ3 (độ trễ/năng lượng):** Suy luận trên NPU đạt bao nhiêu Hz, độ trễ và công suất?
- **SQ4 (đối chứng):** Sai số so với chuẩn vàng (force plate / load cell đa trục) là bao nhiêu cho Fx, Fy, Fz, COP?

---

## 4. Khoảng trống nghiên cứu & tính mới (đang ở mức GIẢ THUYẾT)

> ⚠️ Các mục dưới đây là **giả thuyết về khoảng trống**, được nêu ra từ rà soát sơ bộ của chủ dự án. Chúng **chưa** được xác nhận bằng systematic review. Theo `AGENTS.md`, chỉ sau khi rà soát tài liệu có bằng chứng mới được ghi thành claim `SUPPORTED`.

- **Gap-1 (drift qua nhiều phiên):** giả thuyết rằng chưa có giải pháp **giá rẻ** nào giải quyết triệt để drift qua nhiều phiên cho Velostat. Cần kiểm chứng: tìm các bài về "Velostat/Linqstat drift compensation", "piezoresistive insole long-term drift", "dP/dt pressure insole".
- **Gap-2 (Fx/Fy từ áp lực đơn thuần):** suy lực trượt ngang từ cảm biến chỉ đo áp lực pháp tuyến là bài toán khó; cần xác định mức prior art (các nghiên cứu GRF-from-pressure-insoles, ví dụ dùng insole thương mại + machine learning).
- **Gap-3 (edge deployment giá rẻ):** triển khai mô hình không–thời gian lượng tử hoá trên NPU giá rẻ với độ trễ thấp.

**Rủi ro novelty:** lĩnh vực smart insole rất đông (thương mại: Nurvv, Sensoria, Moticon, Digitsole, Plantiga…; nghiên cứu GRF-from-insoles tồn tại). Tính mới phải được **thu hẹp rõ ràng** và chứng minh bằng rà soát có lưu vết, không phải bằng "chưa tìm thấy bài tích hợp".

---

## 5. Kế hoạch kiểm chứng (dự kiến — chưa chốt)

1. **Đặc trưng hoá cảm biến:** đo đạc drift/hysteresis/creep của Velostat theo nhiệt độ và thời gian tải dài; xây bộ dữ liệu chuẩn.
2. **Chuẩn vàng:** xác định hệ quy chiếu Fx, Fy, Fz, COP — force plate (tấm đo lực) hoặc load cell đa trục. **Đây là blocker số 1**: không có chuẩn vàng thì không thể định lượng sai số 3D-GRF.
3. **Thu thập dữ liệu:** bộ dữ liệu bước chân (walking/standing/transition) với nhãn chuẩn.
4. **Baseline trước, ST-GNN sau:** huấn luyện baseline (tuyến tính → CNN/LSTM) rồi mới ST-GNN; so sánh trên cùng train/val/test split, báo cáo uncertainty.
5. **Edge benchmark:** xuất ONNX/TFLite, lượng tử hoá INT8, đo latency/throughput/năng lượng trên Orange Pi 5 Pro.
6. **Phản biện:** chạy giao thức 5 ghế (`research/protocols/SMART_INSOLE_CRITIQUE_5_SEATS.md`) và 6-lane orchestration hiện có trước khi nộp.

---

## 6. Đạo đức & ISEF

- Đây là **nguyên mẫu đo lường cơ sinh học**, **không** phải thiết bị y tế; **không** đưa ra kết luận chẩn đoán/lâm sàng.
- Mọi thử nghiệm có người tham gia chỉ bắt đầu sau **IRB/SRC pre-approval** hợp lệ của hội thi trực thuộc; chữ ký mentor **không** thay thế IRB.
- Ưu tiên thử nghiệm **mannequin/bench** trong khi chờ phê duyệt.
- An toàn điện: đế giày tiếp xúc cơ thể — kiểm tra cách điện, nguồn pin, nhiệt.

---

## 7. Tệp liên quan

- `research/context/DECISION_LOG.md` — DEC-TOPIC-001, DEC-INSOLE-001..003 (quyết định chính thức).
- `research/context/PROJECT_SNAPSHOT.md` — snapshot ngữ cảnh mới.
- `research/protocols/SMART_INSOLE_CRITIQUE_5_SEATS.md` — phản biện 5 ghế + 5 câu hỏi chí mạng.
- `research/reviews/2026-08-25_smart_insole_redteam.md` — lượt red-team phản biện đầu tiên.
- `research/context/CONVERSATION_2026-08-25.md` — bản nén hội thoại ra quyết định đổi hướng.
