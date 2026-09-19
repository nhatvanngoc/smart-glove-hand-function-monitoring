# Đánh giá "khả năng đi xa" của đề tài — mức trần theo từng trục (2026-09-19)

> **Loại tài liệu:** nhận định nội bộ, **phục vụ quyết định**, không phải nội dung nộp.
> **Quy tắc áp dụng:** mọi mức dưới đây là **phán đoán có căn cứ (judgment), không phải số đo**. Đề tài **chưa có một kết quả thực nghiệm nào**
> (`docs/01`, `PROJECT_SNAPSHOT` §1) → không được biến bất kỳ dòng nào ở đây thành "kết quả" trong báo cáo.
> Mỗi kết luận ghi rõ **dùng chuẩn nào**: ⚑ = chuẩn hội thi học sinh (ViSEF/ISEF), ⚐ = chuẩn xuất bản khoa học (tạp chí/hội nghị), ⚐⚐ = chuẩn sản phẩm y tế.

---

## 0. Trả lời ngắn

- **Trục hội thi (⚑): trần cao, nhưng chưa chạm.** Với đúng thiết kế hiện tại, nếu `GATE C` **pass** và có bộ 6 con số tự đo, đề tài đủ sức đi **vòng trường → vòng tỉnh/sở → vòng quốc gia ViSEF**, và có **cửa thật** ở sân chơi quốc tế (hồ sơ ISEF-style) — thứ khiến nó khác đa số là *phương pháp có thể kiểm chứng*, không phải độ bóng của demo. Nếu `GATE C` **fail**, trần rơi xuống mức "báo cáo phương pháp + kết quả âm tính trung thực" (vẫn là một báo cáo tốt, hiếm khi đi xa ở vòng cao).
- **Trục khoa học (⚐): trần hiện tại = technical note / workshop / case report**, vì dữ liệu chỉ có phantom + rig. Muốn lên mức article phải có IRB + n ≥ 20 bệnh nhân + agreement với FMA/ARAT/MAS — tức **12–24 tháng và một viện đối tác**, nằm ngoài phạm vi một đề tài học sinh (và ngoài `A.4`).
- **Trục sản phẩm (⚐⚐): không phải trần của đề tài này, mà là trần của đề tài *sau* nó.** Khoảng cách từ nguyên mẫu sang thiết bị y tế được minh hoạ bởi chính các đối thủ: Manumeter phải chạy RCT trong phòng thí nghiệm đại học, iHand cần đa trung tâm + industrial partner, NEOFECT là công ty nhiều năm (giá ~1.925 USD/bộ vẫn `UNVERIFIED`/nhà sản xuất). Đề tài này bán được **phương pháp + bộ dữ liệu mở + thiết kế cơ khí**, không bán được thiết bị.
- **Trục cá nhân (⚑⚐): đây là trục trần cao nhất và chắc chắn nhất.** Kỷ luật hồ sơ (ledger có mức-đã-đọc, claim ledger, cổng sống/chết viết trước khi đo) là thứ rất hiếm ở cấp học sinh và có giá trị sử dụng lâu hơn cả con găng.

---

## 1. Vị trí hiện tại trên thang đo (sự thật, không tô)

| Trục | Đã có | Chưa có |
|---|---|---|
| Lý thuyết & định vị | `docs/02` 387 dòng (10 mục + §5.5 mô hình chuỗi đo); `docs/01` chốt tên + 7 GATE; `docs/05` đề cương | — |
| Bằng chứng thứ cấp | `SOURCE_LEDGER` **134 dòng** có trạng thái đọc; 13 nhóm tìm kiếm trong `docs/03`; **4 lỗi danh tính nguồn đã bắt ra và sửa** trong 2 ngày | Tra bằng sáng chế theo phân loại = **bất khả thi** ở đây (`docs/03` §7); `SRC-IRONHAND-2018` mới đọc Methods |
| Tuyên bố | `CLAIM_LEDGER` 21 dòng, mỗi dòng có status + evidence level | `DEC-NOV-001` (chốt novelty) vẫn mở — **đúng**, vì chưa có dữ liệu |
| Sản phẩm | 1 sketch Arduino **DI SẢN — không áp dụng** (`firmware/mega_link_diagnostics`, 48 dòng, của đề tài insole cũ); 3 template CSV **chỉ có dòng header** | **0** firmware ESP32-S3, **0** CAD/STL, **0** sensing element chế tạo, **0** rig, **0** bản đo, **0** log |
| Lịch sử repo | 1 commit (merge từ đề tài cũ); toàn bộ phần việc 2026-08→09 đang ở working tree | quy trình commit/backup — **rủi ro mất việc**, xem §4 R5 |

**Dịch:** trên trục hồ sơ, đề tài đã đi **xa hơn hầu hết đề tài học sinh cùng thời điểm**; trên trục vật lý, nó đang ở **số 0**. Cả hai đều bình thường ở giai đoạn này — nhưng trần **không** nhúc nhích cho tới khi GATE 0 chạy.

---

## 2. Điều kiện để chạm từng mức trần (⚑)

| Mức | Điều kiện cần (đo được, không phải hùng biện) | Điều kiện đủ để *không* bị loại sớm |
|---|---|---|
| Vòng trường / sở | GATE 0 có số (CV trong phiên, ICC giữa phiên, hysteresis, creep) + ít nhất 1 ngón hoạt động trên phantom | Nói rõ "chưa thử trên người" ngay trang đầu (biến giới hạn thành điểm trung thực) |
| ViSEF quốc gia | GATE A (hướng) + GATE B (tầm chỉ số so với góc cơ khí đã biết) pass theo ngưỡng đã chốt **trước** + đường cong 3 mức × ≥5 phiên × ≥3 ngày cho GATE C | Bảng phân biệt 7 dòng ở `docs/05` §4 được đưa lên slide 1; 6 con số tự đo của `…_scope_options.md` §12 có mặt đầy đủ |
| ISEF/ quốc tế (⚑ cao nhất) | Toàn bộ GATE D/E/F + demo chạy **thời gian thực** + dữ liệu thô công khai + người trình bày trả lời được "vì sao không dùng IMU" và "vì sao chưa có bệnh nhân" | Có **thứ mà hội đồng không tự chế được**: một rig cho ra con số chuẩn hoá (E4/E5 với tải đã hiệu chuẩn) và một cờ `UNRELIABLE` mà họ có thể bấm thử tại chỗ |

Lưu ý về **mẫu số so sánh** (⚑): dự án đoạt giải cao ở cấp này thường = **không có nguyên lý mới + tái tổ hợp khéo + số tự đo** (xem `research/reviews/2026-09-19_active_assisted_scope_options.md` §9 và benchmark nội bộ ROBO065T — *chỉ dùng trong `research/`, không trích trong hồ sơ nộp*). Đề tài này khớp mẫu số đó **nếu** ô "số tự đo" được điền.

---

## 3. Năm đòn bẩy, xếp theo tác dụng trên trần

| # | Đòn bẩy | Trần nó nâng | Giá (ước lệ) |
|---|---|---|---|
| 1 | **GATE 0**: đo `R(p)`, γ, hysteresis/creep trên 5 phần tử, ≥3 ngày | Trả lời câu hỏi "cửa sổ làm việc 2 đầu có rỗng không" (`docs/02` §5.5) → quyết định **đề tài có tồn tại hay không** | 1–2 tuần, chi phí vật liệu thấp |
| 2 | **GATE C**: 3 mức chức năng mô phỏng × ≥5 phiên × ≥3 ngày | Biến đề cương thành bằng chứng; là **điều kiện cần** cho mọi mức ⚑ từ vòng quốc gia trở lên | 2–3 tuần (chủ yếu chờ ngày) |
| 3 | **Phỏng vấn KTV** theo phiếu `research/protocols/07` (10 câu) | Cho con số địa phương thật (tần suất hẹn, số người bệnh/phòng) thay vì số suy diễn → tăng mạnh sức nặng mục "vấn đề" | 1–2 tuần, không tốn tiền |
| 4 | **Rig E4/E5** (phanh tải đã hiệu chuẩn, ≥2 tốc độ kéo) | Chỉ số `RAL` bằng cơ khí tự chế — thứ đối thủ học thuật cũng phải nể vì nó **kiểm chứng được tại chỗ** | 2–4 tuần + cơ khí |
| 5 | **Rà lại prior art trong nước + lane R5** (đề tài ViSEF 2024–2026 cùng mảng) | Tránh "đối thủ" ở chính sân nhà; 3 hàng xóm Việt Nam hiện mới có báo chí, chưa có báo cáo gốc (`SRC-VNM-*`) | 1 tuần |

**Không phải đòn bẩy** (đã đọc lợi ích biên): đọc thêm tài liệu lý thuyết, thêm hedging, thêm tính năng phần cứng (IMU/EMU/camera) — mỗi cái đều kéo đề tài ra khỏi cái làm nên giá trị của nó.

---

## 4. Bốn rủi ro hạ trần, và kịch bản nếu nó xảy ra

- **R1 — Cửa sổ preload rỗng (`docs/02` §5.5).** Trở nguồn `R₀` ở preload thấp vượt khả năng drive của ESP32-S3 ADC + CD74HC4067 → tín hiệu không ổn định; còn tăng preload để cải thiện SNR thì **nuốt luôn** nỗ lực cần đo. *Lối thoát đã biết:* đệm trở nguồn bằng follower op-amp, tăng thời gian lấy mẫu/giảm trở nguồn, hạ `V_FS` bằng divider có buffer, hoặc **đổi từ đo nỗ lực sang đo biên độ**. *Ai quyết:* chủ dự án tại GATE 0 — không phải bây giờ.
- **R2 — Drift > thay đổi chức năng mô phỏng.** Velostat có trễ/bò (`SRC-HOPKINS-2020-VELOSTAT-SOCKET`, `SRC-HOPKINS-2020-IEEEJS`; `docs/02` §4.2 + §6); đó chính là lý do GATE C tồn tại. Đã gắn 3 lớp giảm (cặp đối xứng đồng pha, ô tham chiếu → `UNRELIABLE`, baseline **cá nhân** + đoạn drift-only ≥10 ngày). Nếu vẫn fail → **trần là báo cáo phương pháp**; và nói thẳng là đề tài **đã** fail ở tiêu chí sống còn — theo `AGENTS.md`, đó vẫn là kết quả hợp lệ.
- **R3 — Thời gian.** **Không có ngày nộp nào trong repo** (`docs/05` §7 để trống `[điền]`). Kịch bản: `<3 tháng` → cắt M6 (INT8) + 3D, chỉ làm 1–2 ngón, mục tiêu GATE 0+A+B; `3–6 tháng` → đủ GATE 0→C với 3 ngón; `6–12 tháng` → đủ cả 7 cổng + demo. Đây là biến số **lớn nhất** trong toàn bộ câu hỏi "đi xa được không".
- **R4 — Bị nhận xét "găng đo lực đã có nhiều".** Có thật: `SRC-CN116954366A-ARRAYGLOVE` (20 phần tử áp trở, nêu ứng dụng theo dõi PHCN), `SRC-TW-SPASTICITY-2022` (19 IMU + bóng áp lực, n=14, IRB), `SRC-ARTGLOVE-2026` (2048 taxel). *Phòng thủ:* khác biệt không nằm ở cảm biến mà ở **vách cứng có preload → suy hướng không cần encoder/IMU** + **AROM − PROM cùng phiên** + **RAL cơ khí** + **khung MDC/ICC/cờ phiên**; tức là bảng `docs/05` §4.
- **R5 — Mất việc (vận hành).** Toàn bộ 18 tệp sửa đổi vẫn ở working tree, repo có 1 commit. Không nằm trong phạm vi tôi được phép tự xử (chỉ thị "đừng push"), nhưng đây là rủi ro **thực và tức thời** nhất trong danh sách này → chủ dự án nên tự snapshot/backup sớm theo cách của mình.

---

## 5. Kết luận một câu

**Đề tài đang có trần cao trên trục hội thi và trục phương pháp, trần trung bình trên trục xuất bản, trần thấp trên trục sản phẩm — và toàn bộ ba trần đó hiện cách nhau bởi đúng hai việc: GATE 0 và GATE C.** Nói cách khác: "đi xa được không" hiện **không** phụ thuộc vào ý tưởng (đã đủ chắc, đã đối chiếu prior art tới mức 4 lỗi nguồn bị bắt) mà phụ thuộc vào **số đo** và **số tuần còn lại**.

> Bản này **không** đổi `DEC-NOV-001`, **không** nâng mức bằng chứng của bất kỳ claim nào, và **không** được trích nguyên văn vào hồ sơ nộp.

---

## 6. Định giá theo lớp đầu tư (trả lời câu "đã đủ điều kiện để đầu tư chưa?" — 2026-09-19)

> Quy ước: tiền dưới đây là **dải ước lệ để lập kế hoạch**, **không** phải báo giá. Mọi con số tiền đưa vào hồ sơ phải thay bằng hoá đơn/báo giá thật
> (đã xác minh 2026-09-19: repo KHÔNG có id `DECISION_D6`. Neo thật: chỉ thị **D6** trong `research/context/CONVERSATION_2026-09-13.md` — "yêu cầu tính toán để độ phân giải đủ tốt", mà `research/protocols/08_gate0_execution_plan.md` §3 là cách trả lời; và hàng "Rẻ hơn N lần so với thiết bị y tế → chưa có báo giá thật có hóa đơn" trong Phụ lục A `docs/05`). ⚑ = phán đoán theo chuẩn hội thi, không phải số đo.

| Lớp | Mua gì | Tiền (ước lệ) | Thời gian | **Điều kiện mở khoá** | Rủi ro mất tiền |
|---|---|---|---|---|---|
| **0** | Velostat + đồng tự dính + acrylic + jig in 3D + quả cân + DMM đo 4 dây | ~0,2–0,5 tr đ | 1–2 tuần | **chỉ cần** 9 ngưỡng `protocols/08` §7 được chốt | gần 0 — lớp này mua **thông tin**, không mua thiết bị |
| **1** | ESP32-S3 + CD74HC4067 + HX711/load cell + in TPU/PLA + dây | ~1,5–3 tr đ | 3–5 tuần | `G0.1` **pass** (cửa sổ preload không rỗng) **và** `G0.2` (γ đo được ở ≥ 4/5 phần tử) | trung bình — nếu phải bỏ vì R1 thì mất ~2 tr đ, nhưng đã biết sớm |
| **2** | Orange Pi 5 Pro (NPU) + rig E4/E5 (phanh tải, ≥2 tốc độ) + phantom + encoder góc cơ khí | ~7–12 tr đ | 4–8 tuần | `GATE A` + `GATE B` **pass** trên ≥ 1 ngón | cao — **đừng** mua trước khi có 1 ngón chạy được. **`DECISION_LOG` chưa có dòng nào ủy quyền việc mua board** (đã rà 25 id `DEC-*`, không có id ngân sách) → khoản chi này *chưa hợp lệ về mặt quy trình* |
| **3** | Người thật: IRB/SRC + bệnh viện đối tác + thu mẫu n ≥ 20 | tiền ít, **thời gian & quan hệ** nhiều | 3–6 tháng+ | `GATE C` pass + `CLM-SAFE-001` VERIFIED + văn bản phê duyệt | không phải đầu tư tiền — là đầu tư uy tín/giới thiệu (`docs/01` §9 tầng 5–6) |

**Kết cấu khuyến nghị:** giải ngân ngay **Lớp 0** (1–2 tuần, ~0,3 tr đ), vì đó là quyền chọn rẻ nhất: vài buổi đo trả lời được "cơ chế có tồn tại không" và "GATE C còn cửa hay không" (qua `drift_ratio`). **Chưa** giải ngân Lớp 1–2; việc mua board hiện **không có quyết định nào ủy quyền** ⇒ giữ nguyên *chưa mua* cho tới khi GATE 0 xong — đúng tinh thần lộ trình theo tầng của `docs/01` §9.

**Điểm chuẩn từ benchmark vừa đọc:** dự án ALS thắng cuộc có chi phí báo chí nêu ~30 tr đ — nhưng thứ đưa nó lên đỉnh **không phải tiền**, mà là *máy chạy được + 5 con số tự đo*. Đừng dùng ngân sách để bù cho số đo: với Lớp 0+1 (~3 tr đ) và 6 con số tự đo, ta đã đứng trên mặt bằng đó về phương pháp.

### 6.0.1 CẬP NHẬT cùng ngày — sau khi chủ dự án khai báo thiết bị đã có (`DEC-RESOURCE-001`)
**Verdict đổi: ĐỦ để giải ngân Lớp 0 **và** Lớp 1 về tiền (board/MCU/vật liệu áp trở đã có sẵn: Velostat, ESP32-S3, Orange Pi 5 Pro, băng đồng).**
Ba điều vẫn **không** đổi vì có thiết bị:
1. **Ngưỡng vẫn phải chốt trước khi đo.** Rủi ro của việc "đã có đồ" không phải *không làm được*, mà là **làm ẩu vì thấy mọi thứ đã sẵn** —
   cụ thể là nhảy thẳng sang chế tạo cả găng rồi mới đo phần tử. `GATE 0` đứng trước là để chặn đúng việc đó.
2. **Không tự suy ra chi phí đề tài từ đồ đang có.** "Thiết bị đã có" phải ghi là *được cung cấp/tự có*, không phải *giá thành 0* (Phụ lục A `docs/05`).
3. **Chị KTV là cố vấn phản biện, không phải đối tượng đo** — ranh giới đầy đủ ở `research/protocols/07` §7, `DEC-ROLE-001`.

Khoản còn lại phải mua cho GATE 0 chỉ còn: CD74HC4067 (nếu chưa có) + vật tư in 3D + khối lượng chuẩn + DMM 4 dây → **vài trăm nghìn đồng**.
Bảng kiểm kê + việc cần làm tuần này: `research/context/EQUIPMENT_AND_ACCESS.md`.

### 6.1 Danh sách "đủ điều kiện" — khi ≥ 4/5 ô tích, tôi đổi kết luận thành **ĐỦ: giải ngân Lớp 1**
- ☐ 9 ngưỡng `protocols/08` §7 đã chốt **trước** khi bật nguồn (kèm ảnh chụp trang đó dán vào header log).
- ☐ `G0.1` pass: tồn tại `F_p` với `R₀ ≤ R_max` **và** `SNR ≥ 8 LSB` tại `ΔF = 1 N`.
- ☐ `G0.7` không fail: trôi 10 ngày < tín hiệu của `ΔF = 1 N` (ô này fail → **dừng ở Lớp 0**, vì GATE C đã chết trên giấy).
- ☐ 1 ảnh chụp phần tử + jig đang cho tín hiệu lên màn hình, kèm file log thô đầu tiên trong `research/bench/logs/`.
- ☐ Tạo + chốt **`DEC-BUDGET-001`** (id mới, chủ dự án): báo giá thật/hoá đơn cho ESP32-S3 → Orange Pi 5 Pro → load cell → vật liệu in, kèm **trần tiền** được phép chi cho từng lớp.

### 6.2 Khi nào phải nói "dừng"
Nếu `G0.1` fail **và** cả ba lối thoát ở `protocols/08` §8 (follower đệm trở nguồn / hạ yêu cầu bỏ Effort Index / đổi sang dải kéo) không mở được cửa sổ trong ≤ 3 tuần, thì theo `docs/01` §7 và `AGENTS.md`, khoản giải ngân tiếp theo **không** nên được duyệt. Kết luận "cơ chế vách + áp trở không đủ nhạy cho theo dõi dọc" vẫn là một kết quả hợp lệ, và vẫn có người đọc.
