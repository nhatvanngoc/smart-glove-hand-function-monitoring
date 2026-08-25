# Red-team review — Smart Insole Edge-AI (first pass)

> **Ngày:** 2026-08-25
> **Phạm vi đọc:** docs/30_TOPIC_PIVOT_Smart_Insole.md, quyết định DEC-TOPIC-001/DEC-INSOLE-*, chỉ thị chủ dự án (nguyên văn).
> **Cách thức:** **sequential role review** — các ghế chạy tuần tự trong cùng context. **Không** phải independent multi-agent verification.
> **Mục đích:** nêu blocker ngay từ đầu để tránh đầu tư sai hướng. Không phải phán quyết "đạt/trượt".

---

## Verdict tổng hợp: REVISE (được phép tiếp tục, có blocker phải đóng)

| # | Finding | Severity | Bản chất | Bằng chứng giải quyết |
|---|---|---|---|---|
| F1 | Chưa xác định **chuẩn vàng** cho Fx, Fy, Fz, COP | BLOCKER | Không có force plate/load cell đa trục thì mọi tuyên bố sai số 3D-GRF là không thể kiểm chứng | Ký mượn/thuê force plate hoặc load cell đa trục; hoặc thu hẹp phạm vi về Fz+COP |
| F2 | "dP/dt triệt tiêu drift" là phát biểu quá mạnh | MAJOR | dP/dt chỉ giảm offset drift; drift còn làm nhiễu biên độ (gain/sensitivity). "Triệt tiêu" = hallucination nếu chưa đo | Thí nghiệm đặc trưng drift (nhiệt + tải dài + chu kỳ) trong miền dP/dt; báo biên định lượng |
| F3 | Novelty chưa được chứng minh; lĩnh vực rất đông | MAJOR | Smart insole/GRF-from-insoles là lĩnh vực đông (thương mại + hàn lâm); "chưa tìm thấy" ≠ "chưa tồn tại" | Systematic review có lưu vết; bảng so sánh prior art; thu hẹp novelty (Velostat giá rẻ + drift cross-session + Fx/Fy từ áp lực đơn thuần) |
| F4 | ST-GNN được đặt trước khi có baseline | MAJOR | Chưa có lý do bằng chứng rằng ST-GNN thắng baseline tuyến tính/LSTM; dữ liệu nhỏ dễ overfit | Chạy baseline trước, cùng split, báo uncertainty; chỉ giữ ST-GNN nếu cải thiện có ý nghĩa |
| F5 | Tuyên bố hiệu năng phần cứng chưa đo | MAJOR | "16 kênh ADC tần số cao", "NPU 6 TOPS" là spec/ý định, chưa phải số đo | Đo tần số lấy mẫu thực (kể cả khi multiplex >16 ô) và latency/throughput/năng lượng sau INT8 |
| F6 | Ma trận cảm biến vs 16 kênh ADC chưa khớp | MAJOR | Arduino Mega chỉ có 16 ngõ analog; ma trận >16 ô cần multiplex → giảm tần số, thêm nhiễu | Chốt số ô + sơ đồ multiplex + tần số lấy mẫu mỗi kênh; hoặc dùng ADC ngoài (ADS1x15/MCP) |
| F7 | Phạm vi y khoa/an toàn người tham gia | BLOCKER (có điều kiện) | Không được kết luận chẩn đoán; thử người phải IRB/SRC trước | Giữ nhãn "nguyên mẫu đo lường cơ sinh học"; bench/mannequin trước; hồ sơ IRB/SRC khi cần |
| F8 | Thuật ngữ "triệt tiêu"/"đột phá" cần kiểm soát | MINOR | Ngôn ngữ quảng cáo dễ bị ban giám khảo phản bác | Thay bằng ngôn ngữ đo lường được: "giảm", "biên định lượng", "so với baseline" |

---

## Ghi chú theo ghế

- **G1 Cơ sinh học:** hợp lệ về hướng (GRF/COP là đại lượng chuẩn của phân tích dáng đi). Lưu ý: Fx (trước–sau) và Fy (trong–ngoài) có biên độ nhỏ hơn Fz nhiều; suy từ áp lực pháp tuyến là bài toán ngược nhiễu cao — cần chuẩn vàng nhạy đủ.
- **G2 Nhúng:** Orange Pi 5 Pro (RK3588S, NPU ~6 TOPS) là lựa chọn hợp lý; điểm nghẽn thật sự là **ADC/multiplexing** và **nguồn/dây đế giày**. Cần đo trước khi hứa "real-time".
- **G3 AI/ML:** cần giao thức chống leakage (tách theo người tham gia, không chỉ tách mẫu ngẫu nhiên), báo uncertainty, và baseline tuần tự.
- **G4 Đạo đức:** giữ nguyên tắc IRB/SRC; không tuyên bố thiết bị y tế.
- **G5 Devil's Advocate:** câu hỏi gai nhất là "vì sao không dùng insole thương mại có sẵn sensor chất lượng cao?" — câu trả lời trung thực là **chi phí + khả năng can thiệp vào lớp hiệu chỉnh drift + đóng góp dữ liệu/phương pháp mở**, và điều đó chỉ đứng vững nếu novelty hẹp được chứng minh.

---

## Kết luận hành động ngay

1. **Chốt chuẩn vàng** (F1) trước khi mua thêm bất kỳ linh kiện nào — đây là blocker cứng.
2. Đổi ngôn ngữ "triệt tiêu drift" → "giảm drift với biên định lượng" trong toàn bộ tài liệu.
3. Lập systematic review có lưu vết cho novelty (F3) trước khi ghi claim `SUPPORTED`.
4. Chạy baseline tuyến tính/LSTM trước ST-GNN (F4).
5. Cập nhật `DECISION_LOG.md`/`CLAIM_LEDGER.csv` khi từng blocker được đóng.
