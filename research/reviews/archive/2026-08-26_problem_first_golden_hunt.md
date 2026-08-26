# Golden-filter hunt (problem-first) — 2026-08-26

Bộ lọc vàng mới của owner: **săn problem trước, không săn novelty trước**; system-novelty (không cần thuật toán mới); prototype-first; kill-test sớm; chấm 5 tiêu chí (Human impact / Novelty / Feasibility / Measurability / ViSEF–ISEF fit). **Không nhét Velostat/Orange Pi/Arduino vào trước.**

## Bước 1 — Beneficiary
**Người khuyết tật vận động (SCI/tứ chi, bại não, sau đột quỵ, ALS) + người già yếu.** (Giàu pain point sensing/embedded; đúng gu đề tài ISEF đoạt giải của VN: thiết bị hỗ trợ người khuyết tật.)

## Bước 2 — Cào 20 pain point CỤ THỂ
1. Ngồi xe lăn không với tới đồ trên kệ cao / dưới sàn.
2. Chuyển tư thế (xe lăn↔giường↔bồn cầu) không an toàn → té (nguyên nhân tử vong hàng đầu ở người >65).
3. Không tự vệ sinh cá nhân / đi toilet.
4. Đau vai do tự đẩy xe lăn lâu năm.
5. Không tự mặc quần áo.
6. Không đủ lực tay mở nắp chai / hộp thuốc.
7. Rơi đồ xuống đất mà không nhặt lên được.
8. Không tự nấu / chuẩn bị bữa ăn.
9. Điều khiển xe lăn kém chính xác khi mệt hoặc run.
10. Không giao tiếp được (ALS/nói khó) → bị cô lập.
11. Không cầm được thìa/đũa → không tự ăn (run tay).
12. Không với tới công tắc điện / ổ cắm.
13. Ở một mình, té mà không ai biết / không gọi được trợ giúp.
14. Run tay làm đổ thức ăn/nước uống.
15. Không cầm bút / dụng cụ để viết, vẽ.
16. Không điều khiển được TV/điện thoại/đèn (thiết bị môi trường).
17. Quên uống thuốc / uống nhầm liều.
18. Không giữ được tư thế ngồi vững (trượt, ngã khỏi ghế).
19. Di chuyển ngoài trời: bậc thang, vỉa hè, địa hình xấu.
20. Ngồi/nằm lâu → loét tỳ đè mà không cảm nhận được.

## Bước 3+6 — Lọc 5 → kill-test 3 (bằng chứng prior art)

### Lọc 5 (problem rõ + prototype được + đo được + system-novelty):
A(1+7), B(2), C(11+14), D(20), E(16).

### Kill-test 3:
| # | Pain point | Hiện có gì | Vì sao thất bại (bằng chứng) | Sống? |
|---|---|---|---|---|
| **A** | Không với tới đồ | Kẹp gậy thủ công ($10–60: Vive, RMS, Grip-Free, QUADTOOLS); tay robot gắn xe lăn Jaco (~$40k), iArm (~$25k) | Kẹp thủ công **cần lực tay + khéo** (người tay yếu không bóp/không kẹp được vật nhỏ — review thật của C5/C6 tetraplegic); kẹp quá ngắn/quá dài; tay robot thì **quá đắt + cần joystick chính xác** | **SỐNG** — gap thật: thiết bị **vừa túi tiền** cho người **không có chức năng tay** |
| **B** | Chuyển tư thế không an toàn | Hoyer/trần, ván chuyển, ghế nâng, xe lăn chuyển ($1400+), robot tay vịn (UR10e, NSF) | **Cần người chăm sóc hoặc thiết bị nặng/đắt**; chưa hệ nào làm an toàn+độc lập | Sống-nhưng-khó — giải pháp thiên về **cơ khí nặng**, khó prototype; hướng sensing/feedback thì cần định nghĩa rõ |
| **C** | Run tay khi ăn | Thìa nặng, thìa xoay, **Liftware (Google, khử run chủ động)**, Gyenno, găng Steadi-3 | Đã **rất chật + hiệu quả còn tranh cãi** (AJOT 2019: thiết bị khử run **không vượt** thìa nặng) | **CHẾT** (đông prior art, efficacy contested) |

(D = loét tỳ đè: đã biết rất chật từ các vòng trước → không đào lại. E = điều khiển thiết bị môi trường: AAC/smart-home, cần kill-test sau.)

## Bước 7 — Chấm 5 tiêu chí (thang 20/tiêu chí, ước lượng bảo thủ)

| Candidate | Human impact | Novelty | Feasibility (bench) | Measurability | ViSEF–ISEF fit | Tổng /100 |
|---|---:|---:|---:|---:|---:|---:|
| **A. Với/lấy đồ cho người tay yếu** | 18 | 12 | 17 | 18 | 18 | **83** |
| B. Chuyển tư thế an toàn | 19 | 12 | 9 | 12 | 14 | 66 (feasibility thấp) |
| C. Dụng cụ chống run | 16 | 8 | 14 | 16 | 12 | 66 (novelty thấp, đã kill) |

## Candidate thắng (đề xuất): **A**

**Câu vàng:**
> "Tôi giải quyết vấn đề **lấy/với đồ ngoài tầm tay** cho **người ngồi xe lăn có chức năng tay kém/không**, vì **kẹp gậy thủ công cần lực bóp tay mà họ không có, còn tay robot thì quá đắt và cần điều khiển joystick chính xác**; hệ thống của tôi là **cánh tay gắn xe lăn giá thấp, điều khiển bằng khả năng còn lại của người dùng (chỉ 1 công tắc / giọng nói / nghiêng đầu) + camera AI tự căn chỉnh để gắp (shared autonomy)**; tôi chứng minh bằng **tỉ lệ lấy đồ thành công + thời gian hoàn thành trên bench (kệ mô phỏng nhiều độ cao), so với kẹp thủ công và điều khiển thủ công**."

- **System novelty (không cần thuật toán mới):** kết hợp sensing (camera) + AI (edge, tự căn vật) + cơ cấu (tay 3–4 bậc rẻ) + interaction (điều khiển bằng khả năng còn lại) để xử lý failure "không có tay + không tiền".
- **Prototype-first:** test trên bench với vật thật + kệ mô phỏng; người test **mô phỏng** tay yếu (găng hạn chế) — **không cần bệnh nhân/IRB**.
- **Phần cứng:** KHÔNG bắt buộc Velostat; cần servo + camera + Orange Pi (đã có). → đúng luật "đừng để linh kiện dắt mũi".

## Việc phải làm trước khi khóa A (kill-test vòng 2)
1. Đọc kỹ prior art **shared-autonomy / vision-assisted robotic arm cho wheelchair** + **assistive arm điều khiển bằng switch/sip-puff/EOG** — để khẳng định "rẻ + điều khiển bằng khả năng tối thiểu + AI tự căn" chưa bị chiếm trọn.
2. Chốt failure-mode thật (lấy số liệu từ cộng đồng SCI nếu được) để tránh "giải vấn đề không ai đau".
3. Thiết kế bench + metric định lượng + baseline.
4. Chống "quá sức học sinh": phạm vi vừa phải, nêu rõ phần tự làm.
