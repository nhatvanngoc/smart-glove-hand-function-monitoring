# Conversation archive — 2026-08-25 (đổi hướng đề tài)

> **Mục đích:** bản nén (lossy) hội thoại ra quyết định đổi hướng đề tài, lưu trữ bền vững trên GitHub để khôi phục ngữ cảnh mà không phụ thuộc trí nhớ hội thoại.
> **Phương pháp nén:** tóm tắt có cấu trúc + phụ lục chứa **nguyên văn** chỉ thị của chủ dự án (làm provenance). Bản tóm tắt là **hỗ trợ điều hướng**, không phải bằng chứng; nguồn chuẩn là `DECISION_LOG.md`, `PROJECT_SNAPSHOT.md` và các artifact gốc được trỏ tới.
> **Trạng thái:** chủ dự án cho biết sẽ gửi **thêm thông tin** sau — các mục "mở" dưới đây chờ cập nhật tiếp theo.

---

## 1. Tóm tắt nén (compressed)

### 1.1 Yêu cầu của chủ dự án (8 mục)

1. Vai trò AI: context lớn, điều phối sub-agent, **phản biện**.
2. Chuẩn bị & clone repo: academic-research-skills, PlotNeuralNet, Caffe, PGF/TikZ, MiKTeX.
3. Công cụ **tìm kiếm** + **sub-agent phản biện**.
4. **Nén token** cho ngữ cảnh lớn, **lưu truy vấn vào file**.
5. Kỹ năng nghiên cứu khoa học & phản biện **ngang tầm ISEF**, **giảm thiểu ảo giác**.
6. **Đổi hướng đề tài** (từ "đệm khí thích ứng" sang Smart Insole) — cập nhật lên GitHub.
7. **Nén hội thoại này** và lưu vào GitHub.
8. **Đổi tên repo GitHub**.

### 1.2 Đổi hướng đề tài (tóm tắt quyết định)

- **Bỏ** "đệm khí thích ứng + AAC" (rủi ro cơ khí, cảm biến, kiểm chứng lâm sàng quá cao).
- **Chuyển sang** "Smart Insole dùng Edge-AI ước lượng **3D-GRF** và quỹ đạo **COP**".
- **Trọng tâm đột phá:** khắc phục điểm yếu của Velostat giá rẻ (trôi dạt, trễ) bằng **dP/dt** (đạo hàm áp lực theo thời gian) + mô hình **ST-GNN** (bàn chân = đồ thị giải phẫu), suy Fx/Fy từ Fz.
- **Phần cứng:** Arduino Mega (16 kênh ADC, tần số cao) + Orange Pi 5 Pro (NPU ~6 TOPS, suy luận tại biên).
- **Khoảng trống:** giả thuyết "chưa có giải pháp giá rẻ xử lý triệt để drift qua nhiều phiên cho Velostat" — **cần kiểm chứng** bằng rà soát có lưu vết.
- **Phản biện:** 5 ghế (Cơ sinh học, Nhúng, AI, Đạo đức, Devil's Advocate) + chiến lược trả lời 5 câu hỏi "chí mạng".

### 1.3 Việc đã thực hiện trong phiên này

- Clone + ghim 5 nguồn vào `.tools/sources/` (không commit, đúng lock file): academic-research-skills `6837b4d`, PlotNeuralNet `e96bc85`, Caffe `9b89154`, PGF `0a859c8`, MiKTeX `76d1b3d`.
- Tạo skill links `.claude/skills/` (deep-research, academic-paper, academic-paper-reviewer, academic-pipeline).
- Environment check: 7/11 — `pdflatex`/`miktexsetup` chưa cài (cần installer MiKTeX trên máy thật), numpy/matplotlib/scikit-learn chưa cài (cần `.venv`).
- Ghi quyết định đổi hướng vào `DECISION_LOG.md` (DEC-TOPIC-001; đóng các quyết định kiến trúc cũ).
- Tạo `docs/30_TOPIC_PIVOT_Smart_Insole.md`, `research/protocols/SMART_INSOLE_CRITIQUE_5_SEATS.md`, `research/reviews/2026-08-25_smart_insole_redteam.md`.
- Cập nhật `README.md`, `AGENTS.md`, `PROJECT_SNAPSHOT.md`, `INDEX.md`, `research/README.md`, `build_context_bundle.py`.
- **Đổi tên repo GitHub** → `smart-insole-edge-ai` (xem mục 1.4).

### 1.4 Đổi tên GitHub

- Tên cũ: `nhatvanngoc/adaptive_cushion_aac`.
- Tên mới: `nhatvanngoc/smart-insole-edge-ai`.
- Branch làm việc của phiên giữ nguyên: `arena/01a0372f-adaptive-cushion-aac` (ràng buộc nền tảng; không đổi tên branch).

### 1.5 Mở — chờ thông tin tiếp theo từ chủ dự án

- Số ô cảm biến/layout điện cực Velostat trong đế giày (và cách vượt giới hạn 16 kênh ADC).
- Chuẩn vàng (force plate/load cell) cho Fx, Fy, Fz, COP — blocker số 1.
- Phạm vi novelty chốt cuối (sau systematic review).
- Quyết định ST-GNN vs baseline sau khi có dữ liệu.
- Tên repo cuối cùng (nếu muốn đổi khác) và bất kỳ thông tin bổ sung nào.

---

## 2. Phụ lục — nguyên văn chỉ thị của chủ dự án (provenance)

<details>
<summary>Raw owner message (2026-08-25)</summary>

```
Để chuẩn bị cho 1 large project, tôi cần bạn là 1 ai có context windows lớn, có khả năng điều phối sub agent làm việc, và phản biện. Sau đó clone cho tôi 1 số repo để chuẩn bị và triển khai, setup.

1. https://github.com/Imbad0202/academic-research-skills.git
2. https://github.com/HarisIqbal88/PlotNeuralNet.git
3. https://github.com/BVLC/caffe.git
4. https://github.com/pgf-tikz/pgf.git
5. MiKTeX
6. Tool search, sub agent phản biện
7. Nén token để chứa lượng ngữ cảnh lớn, lưu truy vấn vào file.
8. Kĩ năng nghiên cứu khoa học, phản biện ngang tầm cuộc thi ISEF. Giảm tính ảo giác nhất có thể.

Có sự thay đổi về đề tài, bạn cập nhật ở github. Cụ thể như sau:

Quá trình nghiên cứu đã chuyển hướng từ một dự án "Đệm khí thích ứng" quá tham vọng và rủi ro cao sang một đề tài có chiều sâu khoa học và tính khả thi cao hơn: "Hệ thống lót giày thông minh (Smart Insole) sử dụng Edge-AI để ước lượng lực phản lực mặt đất 3 chiều (3D-GRF) và quỹ đạo tâm áp lực (COP)". Trọng tâm đột phá của đề tài là giải quyết điểm yếu cố hữu của cảm biến giá rẻ Velostat (trôi dạt, trễ) bằng các thuật toán toán học và mô hình AI tiên tiến, chạy trực tiếp trên thiết bị nhúng (Orange Pi 5 Pro). Một kế hoạch chi tiết đã được xây dựng để người dùng tận dụng tối đa thời gian chờ vật liệu, nhằm thuần thục phần cứng (Arduino Mega, Orange Pi) và chuẩn bị hạ tầng kỹ thuật sẵn sàng cho việc phát triển và kiểm chứng đề tài.

Các điểm chính:
- Chuyển hướng chiến lược: từ bỏ "đệm khí" do quá nhiều rủi ro về cơ khí, cảm biến và kiểm chứng lâm sàng; chuyển sang "lót giày thông minh".
- Trọng tâm "kháng trôi dạt" (Drift-Resistant): dùng đạo hàm biến thiên áp lực theo thời gian (dP/dt) để triệt tiêu ảnh hưởng của trôi dạt do nhiệt độ và biến dạng vật liệu của Velostat.
- Ứng dụng mô hình AI tiên tiến: ST-GNN mô hình hoá bàn chân như đồ thị giải phẫu, suy ra lực trượt ngang (Fx, Fy) từ dữ liệu áp lực dọc (Fz).
- Phần cứng + phần mềm phối hợp: Arduino Mega thu 16 kênh ADC tần số cao; Orange Pi 5 Pro (NPU 6 TOPS) suy luận AI tại biên.
- Đã xác định khoảng trống nghiên cứu: chưa có giải pháp giá rẻ nào giải quyết triệt để drift qua nhiều phiên đo cho Velostat.
- Chuẩn bị phản biện: quy trình 5 "ghế" (Cơ sinh học, Nhúng, AI, Đạo đức, Devil's Advocate) + chiến lược trả lời 5 câu hỏi "chí mạng".

Sau đó nén cuộc trò chuyện này, lưu trữ vào github. Rồi đổi tên github như nào luôn. Bạn cứ làm đi còn thông tin nữa mà tôi sẽ gửi sau.
```

</details>

---

## 3. Cách dùng tệp này

- **Khôi phục ngữ cảnh:** đọc mục 1, sau đó mở `DECISION_LOG.md` + `PROJECT_SNAPSHOT.md`.
- **Truy xuất nguồn gốc:** mục 2 (nguyên văn) là nguồn chuẩn cho mọi diễn giải ở mục 1; nếu khác nhau, nguyên văn thắng.
- **Cập nhật:** khi chủ dự án gửi thông tin mới, append tệp hội thoại mới `CONVERSATION_YYYY-MM-DD.md` và cập nhật DECISION_LOG/SNAPSHOT, không sửa ngược lịch sử.
