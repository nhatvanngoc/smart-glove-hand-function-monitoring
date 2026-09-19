# 07 — Rig RAL (phantom có tải chỉnh được) + phiếu hỏi KTVVLTL-PHCN

> **Ngày soạn:** 2026-09-19 · **Trạng thái:** **CHỜ GIAI ĐOẠN RIG** — chủ dự án đã duyệt phạm vi E4+E5+E6 (`DEC-SCOPE-003`) nhưng **hoãn chốt ngưỡng** và **hoãn viết script**; giai đoạn hiện tại chỉ làm **cơ sở lý thuyết** (`docs/02` §1.4–§1.6, §3.4, §5.4, §7.3, §8.3). File này để nguyên bản nháp, **không** coi là ngưỡng đã chốt.
> **Vì sao có file này:** đề xuất "tập chủ động có trợ lực (AAT)" của chủ dự án chỉ thành nội dung khoa học nếu **đo được** nỗ lực và mức trợ giúp cần thiết.
> **Nguyên tắc bắt buộc (giống `06`):** mọi số liệu trong file này là **trên rig/phantom** → **không cần IRB**; **cấm** tác động lực lên người cho tới khi có phê duyệt đạo đức.
> **Ngưỡng PASS/FAIL chốt TRƯỚC khi đo; cấm chỉnh sau khi thấy số.**

---

## 1. Định nghĩa chỉ số (bản nháp — chờ duyệt)

| Chỉ số | Định nghĩa thao tác | Đơn vị | Cấm |
|---|---|---|---|
| **Effort signal** `E` | Biên độ tín hiệu vách trong cửa sổ `[t_0, t_0+T_attempt]` khi ngón **chưa** vượt ngưỡng dịch chuyển | mẫu ADC chuẩn hóa (z-score so với nền nghỉ) | KHÔNG đổi thành N, KHÔNG đổi thành %MVC |
| **Effort Index** `EI` | `E / (E + E_nền)`, trung vị 10 nhịp | không thứ nguyên 0–1 | không gọi là "lực chủ động" |
| **RAL** | Tải treo nhỏ nhất (trong nấc đã hiệu chuẩn) để ≥ 80% nhịp trong phiên hoàn thành đích | gam + bậc tải | không suy ra "mô-men co cứng" |
| **Gap AROM−PROM** | `dịch_chủ_động − dịch_thụ_động` (cùng phiên, cùng mảng cảm biến) | mẫu ADC chuẩn hóa | không quy đổi ra độ |
| **Participation ratio** | tỷ lệ dịch chuyển do người tạo ra trong tổng dịch chuyển (học từ `SRC-MPC-AAN-2026`) | % | không diễn giải thành điểm lâm sàng |

## 2. GATE A′ — "có phát hiện được nỗ lực khi ngón chưa di chuyển không?"

**Thiết kế (trên rig):** giữ ngón ở góc cố định bằng chốt; treo các tải 0/20/40/80/120 g; mỗi tải 20 nhịp "kéo cố ý" + 20 nhịp nghỉ, xen kẽ ngẫu nhiên.
**Số phải ghi:** phổ biên độ nhóm cố ý vs nghỉ, `σ_noise` của giai đoạn nghỉ, AUC, tỷ lệ báo nhầm, độ trễ phát hiện (ms).

**Ngưỡng ĐỀ XUẤT — CHƯA CHỐT (chủ dự án hoãn, 2026-09-19):** AUC ≥ **0,85**; báo nhầm ≤ **10%**; độ trễ ≤ **300 ms**; lặp lại được trên ≥ **8** mẫu cảm biến.
**Nếu FAIL:** bỏ Effort/EI khỏi đề tài; AAT chỉ còn là phần *động lực* trong `docs/02`; **không** được viết "phát hiện ý định vận động".

## 3. GATE RAL — "đường cong tải–hoàn thành có dùng làm chỉ số theo dõi được không?"

**Thiết kế:** với mỗi mức "sức cơ" của rig (tắt/bật 1 servo trợ lực theo luật AAN), ghi tỷ lệ hoàn thành theo tải 0→120 g, 3 phiên cách nhau ≥ 24 h.
**Ngưỡng ĐỀ XUẤT — CHƯA CHỐT:** đơn điệu 100% (không được có điểm nghịch hướng); **ICC ≥ 0,75** giữa phiên 1 và 3 trên cùng tải; biến thiên giữa-phiên nhỏ hơn khoảng cách 2 bậc tải.
**Nếu FAIL:** RAL chỉ là thông số bench, **không** được quảng bá thành chỉ số lâm sàng.

## 4. Rig E5 (tuỳ chọn) — 1 servo, chỉ kéo phantom

- Servo + puli + tải; luật điều khiển: bù khi `E > Th_trigger` **và** chưa đạt đích sau `T_window`; dừng khi đạt hoặc khi lực căng cáp vượt `F_max`.
- **An toàn cứng (bắt buộc, kể cả khi chỉ kéo phantom):** giới hạn mô-men trong firmware + công tắc khẩn + giới hạn hành trình cơ khí. Lý do phải có ngay từ đầu: để khi có phê duyệt đạo đức thì lớp an toàn đã được kiểm chứng, không phải viết sau.
- Ghi log: `timestamp, tải, E, đã_đích, trợ_lượng, cờ_bất_thường`.

## 5. PHIẾU HỎI KTVVLTL-PHCN (1 trang, gửi trước buổi hẹn ~3 ngày)

**Bối cảnh (đọc cho KTV):** "Em đang làm găng tay đo chức năng bàn tay sau đột quỵ. Em muốn thêm 2 thứ mà KTV dùng hằng ngày nhưng chưa có số: (1) bao nhiêu *nỗ lực* thì bệnh nhân tự cử động được, (2) cần *trợ giúp bao nhiêu* thì động tác hoàn thành. Em đo trên **thiết bị mô hình**, không trên bệnh nhân."

1. Anh/chị đánh giá "tự làm được" vs "làm được khi đỡ" bằng gì trong hồ sơ bệnh án hiện nay? Có con số nào không, hay chỉ mô tả (được/một phần/không)?
2. Trong một phiên, anh/chị đặt ngưỡng nào để **dừng** bài tập kéo duỗi (dấu hiệu nào báo là đang kéo quá)?
3. Với ngón tay đang co cứng, thao tác kéo duỗi **nhanh** và **chậm** khác nhau thế nào về kết quả và về rủi ro?
4. Nếu một thiết bị báo "hôm nay bệnh nhân tự gập được 40°, cần đỡ nhẹ ở 30° cuối" — con số đó có thay đổi quyết định gì của anh/chị không? Thay đổi gì?
5. Chỉ số nào sau đây **có** ý nghĩa với anh/chị nhất để theo dõi tại nhà (chọn 1–2): tầm chủ động / tầm thụ động /gap giữa hai cái / số lần hoàn thành bài / mức trợ giúp cần thiết / tốc độ hoàn thành / độ mượt?
6. Mức trợ giúp nên biểu diễn thế nào để dùng được: % lực đỡ, số quả cân, số nấc lò xo, hay thang của anh/chị?
7. Trong bao nhiêu tuần thì một thay đổi của gap chủ động–thụ động là **thật** (không phải dao động trong ngày)?
8. Anh/chị có ngại gì nếu bệnh nhân tự đeo thiết bị **chỉ đo** (không kéo) tại nhà? Điều gì khiến anh/chị **cấm** dùng?
9. (Nếu E3 được cân bằng sau này) Ai nên được phép chỉnh giới hạn lực? Cần hồ sơ an toàn gì trước khi thử trên người?
10. Anh/chị có thể xem rig của em trong ~20 phút để phản hồi tính hợp lệ của quy trình không?

**Đầu ra mong muốn:** bảng chốt (a) giao thức 2 pha *tự* / *thụ động* cho Gap; (b) nấc tải cho RAL; (c) ngưỡng an toàn khi kéo duỗi; (d) 1–2 chỉ số chính cho báo cáo tuần. Ghi âm/ghi biên bản → lưu vào `research/evidence/` dưới dạng `SRC-OWNER-*`/phỏng vấn, **có ngày + tên người trả lời** (xin phép trước khi ghi).

---

## 6. Việc của từng bên

| Bên | Việc |
|---|---|
| **Chủ dự án** | Duyệt/chốt ngưỡng §2, §3; quyết định chế tạo rig E4/E5; duyệt `DEC-SCOPE-002` |
| **Agent** | (sau khi duyệt) lập danh sách vật tư rig + file in 3D; viết script thống kê ICC/AUC (hiện repo **chưa có** script thống kê nào); cập nhật `docs/02` + `A.7`; **không** tự đổi tên đề tài, **không** tự đổi A.4 |
| **KTV (chị chủ dự án, 10 năm VLTL-PHCN)** | Trả lời phiếu §5, chốt giao thức 2 pha + bảng tải; **phản biện trên giấy**, không tham gia đo |

---

## 7. Ranh giới sử dụng nguồn KTV (bổ sung 2026-09-19 — vì chủ dự án đã xác nhận có người nhà làm nghề)

**Bối cảnh mới:** chủ dự án có chị là KTV VLTL-PHCN 10 năm và đã xác nhận tính cấp thiết (`SRC-OWNER-2026-09-19-KTV10Y`).
⚠️ **`DEC-ROLE-001` (chủ dự án chốt 2026-09-19): không nêu danh tính người thân trong hồ sơ nộp.** Các ranh giới dưới đây vẫn áp dụng đầy đủ, chỉ khác ở cách diễn đạt

Đây là tài sản **lớn nhất** của đề tài ở vòng chấm, và cũng là **rủi ro đạo đức gần nhất** — vì người có khả năng đo hợp lệ lại ngồi ngay trong nhà.

| # | Điều được làm | Điều **không** được làm (và vì sao) |
|---|---|---|
| 7.1 | Gửi phiếu §5 + 1 trang quy trình, nhận phản biện bằng văn bản | Đo trên **tay chị** để "cho có số người thật" → vi phạm `AGENTS.md` + `A.4`: mọi đo trên người cần phê duyệt IRB/SRC, **không có ngoại lệ cho người nhà** |
| 7.2 | Nhờ chị chỉ ra chỗ chỉ số **vô nghĩa lâm sàng** (EI/GAP/RAL) | Nhờ chị "thu giúp 2–3 bệnh nhân" → đó là tuyển mẫu, thuộc phạm vi `DEC-ETHICS-001` (đang OPEN) |
| 7.3 | Ghi trong hồ sơ (theo `DEC-ROLE-001` — **không nêu danh tính**): "giao thức đo đã được **chuyên gia VLTL–PHCN phản biện**"; **không** viết "chị tác giả", **không** viết "10 năm" trong tài liệu nộp | Viết "được KTV chứng nhận hiệu quả" → **không tồn tại** bằng chứng hiệu quả; "xác nhận cấp thiết" ≠ "thiết bị hoạt động" |
| 7.4 | Dùng hiểu biết nghề để **thiết kế rig E4** (mức tải, thứ tự động tác, nghỉ bao lâu) | Cho người bệnh **đeo/mặc** bất kỳ thứ gì có bộ chấp hành (E5) — `docs/02` §10 mục 6: chấp hành chỉ tác động rig/phantom |
| 7.5 | Chốt hình thức đứng tên minh bạch (`DEC-ROLE-001`) | Để trống vai trò rồi sau này thêm vào "đồng tác giả" |

**Ba câu phải trả lời được nếu giám khảo hỏi về nguồn lực lâm sàng:**
1. "Bạn có làm việc trên người bệnh không?" → **Không.** Mọi số liệu ở giai đoạn này lấy từ phantom/rig; giao thức đã được một **chuyên gia VLTL–PHCN phản biện trên giấy** (không nêu danh tính).
2. "Nếu được phê duyệt đạo đức, bạn làm gì tiếp?" → Tầng B trong `docs/02` §8.3: n nhỏ, đo AROM/PROM + đối chiếu MAS, ngưỡng **đã viết trước**.
3. "Vì sao chưa xin IRB luôn cho xong?" → vì `GATE 0`/`GATE C` **chưa** chứng minh hệ đo có cửa sổ làm việc; đưa người vào một thiết bị chưa qua `GATE C` là **đạo đức kém hơn**, không phải tham vọng khoa học.

---

## 8. Liên kết

- Phiếu đo in được cho GATE 0 (không cần script/firmware): `08a_gate0_bench_sheets.md`.
- Bản in của §5 có thể gửi **riêng** cho người được tham khảo; câu trả lời lưu thành `research/reviews/2026-…-ktv-round3.md` (file nội bộ, tên người tham khảo **không** xuất hiện trong `docs/`).
