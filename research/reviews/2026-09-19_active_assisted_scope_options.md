# SCOPE PROPOSAL — "Tập chủ động có trợ lực (AAT)": phân tích trước khi chấp nhận

> **Ngày:** 2026-09-19 · **Người đề xuất:** chủ dự án (văn bản gửi trong phiên Arena) · **Người phân tích:** agent phiên `01a0b8f4`
> **Trạng thái:** **PROPOSED — chưa được chấp thuận.** Liên kết `DEC-SCOPE-002` (PROPOSED) trong `research/context/DECISION_LOG.md`.
> **Quy tắc của phiên này:** agent chỉ phân tích + đề xuất; không tự đổi phạm vi đề tài, không tự sửa tên đề tài, không sửa ngưỡng GATE, **không commit/push**.
> **Bằng chứng:** mọi dòng `SRC-AAT-*` / `SRC-RAT-*` mới thêm vào `research/evidence/SOURCE_LEDGER.csv` đều ở mức `READ_ABSTRACT` hoặc `UNVERIFIED` → **không** được trích nguyên văn số liệu vào báo cáo cho tới khi đọc toàn văn.

---

## 0. Kết luận ngắn (đọc 2 phút)

**NỖI LO ĐÚNG — HIỆU LỆNH BAN ĐẦU CỦA EM SAI CHUẨN.** Chủ dự án phản hồi (2026-09-19): ở ViSEF/ISEF, thắng bằng **cách đặt vấn đề khác + tái tổ hợp đồ có sẵn + bằng chứng tự làm**, không bằng nguyên lý mới; phân tích kiểu IEEE journal là tự loại mình khỏi sân chơi này. **Em chấp nhận phản hồi đó** và viết lại khuyến nghị ở **§9–§10** (E4/E5). Những gì ở §1–§4 vẫn giữ giá trị nhưng **đổi vai trò**: chúng không còn là "lý do bác", mà là **ranh giới an toàn + danh sách câu hỏi hội đồng sẽ hỏi** — và E4/E5 được thiết kế đúng để né hết ranh giới đó.

(Bản gốc §0 dưới đây giữ nguyên, không xoá, để hồ sơ trung thực về cả hai lần hiệu chỉnh.)

---

## 0-cũ. Kết luận ngắn (giữ nguyên để đối chiếu)

 Thêm động cơ + Bowden + thuật toán AAN không làm đề tài *sâu* hơn trong mắt hội đồng; nó làm đề tài **rộng hơn mà vẫn chưa có số liệu nào**, và đúng phần rộng đó là phần **đông đúc nhất** của cả lĩnh vực.

Tách bản đề xuất thành hai phần, vì hai phần có số phận khác nhau:

| Phần | Nội dung | Đánh giá | Việc nên làm |
|---|---|---|---|
| **Lý thuyết** (mục 1–4 của bản đề xuất: Hebbian, closed-loop, learned non-use, PROM→AROM, AAN) | Giải thích *vì sao* nỗ lực chủ động mới là thứ quyết định hồi phục | **NÊN NHẬN** — nó vá đúng lỗ hổng lớn nhất hiện nay của tài liệu: `docs/01`/`docs/02` giải thích vì sao phải *đo*, nhưng chưa giải thích vì sao *tín hiệu nào trong lúc đo* mới đáng kể | Viết lại 5 câu đang quá tuyệt đối (xem §2), đặt vào `docs/02` + `A.1` + appendix `A.7` |
| **Thiết bị chấp hành** (mục 5: servo/Bowden, "Spasticity Filter", digital twin 3D) | Biến găng đo thành găng kéo | **KHÔNG NÊN NHẬN NGUYÊN TRẠNG** — vì 3 lý do có bằng chứng ở §1 + §3 | Nếu vẫn muốn: chỉ theo phương án **E2-lite** (§5), hoặc chấp nhận E3 với 4 điều kiện cứng |

Ba lý do không nhận phần "thiết bị chấp hành" nguyên trạng:

1. **Không tăng novelty — ngược lại.** Chuỗi "cảm biến phát hiện nỗ lực → động cơ bù phần lực còn thiếu → dừng khi đạt" (chính là mục 3.2 của bản đề xuất) là một **lĩnh vực điều khiển đã trưởng thành**, có bài báo dùng **đúng công thức** mà bản đề xuất viết như ý tưởng của mình: `F_Assistive = F_Ref − F_EMG` (`SRC-AAN-EMG-2024`). Và người ta đã phải viết bài mới (2026) để **sửa** AAN vì AAN cổ điển *không* triệt tiêu được slacking (`SRC-MPC-AAN-2026`).
2. **Chạm ngay 2 dự án Việt Nam đã công bố**, cả hai đều là "găng có trợ lực kéo gập/duỗi": ĐH Bách khoa Đà Nẵng (PneuNet, ~4,5–5 triệu, đã cho bệnh nhân BV Đa khoa Đà Nẵng dùng thử) và **ĐH Thủy lợi (18/09/2026)** — mô tả trên báo đúng là *"bộ khung trợ lực … điều khiển bộ phận trợ lực để kéo mở hoặc gập các ngón tay theo biên độ phù hợp"* + theo dõi từ xa. Nếu đề tài mình đi hướng này, em trở thành **bản sao ý tưởng của người lớn hơn**, thay vì khác biệt.
3. **Đổi loại rủi ro, trong khi nền móng chưa xong.** Hiện repo **chưa có một dòng firmware ESP32-S3 nào**, `GATE 0` chưa chạy được, số liệu thực nghiệm = 0. Thêm chấp hành lực lên bàn tay co cứng sau đột quỵ kéo theo: an toàn mô-men, dừng khẩn, nguồn áp/driver, vòng điều khiển, hiệu chuẩn — và **mọi thử nghiệm trên người (kể cả người lành) đều phải chờ IRB/SRC** (`AGENTS.md` §4, `DEC-ETHICS-001` = PENDING).

**Phần đáng giá nhất của bản đề xuất lại không cần động cơ:** biến AAT thành **chỉ số đo được** — *gap AROM−PROM* và *mức trợ giúp cần thiết* (RAL). Đó là phương án **E2-lite** (§5) và là ứng viên novelty **mạnh hơn** cả ứng viên A đã bị hạ ở `research/reviews/2026-09-19_prior_art_novelty_gate1.md`.

---

## 1. Ba ràng buộc hiện hành mà bản đề xuất va phải (phải xử lý *trước*, không phải sau)

| Ràng buộc | Nguồn trong repo | Va chạm với đề xuất |
|---|---|---|
| Tên đề tài **đã chốt**: "…hỗ trợ **đánh giá và theo dõi** chức năng vận động bàn tay…" | `DEC-TOPIC-019` (2026-09-13), `docs/01` §1 | "Tập chủ động có trợ lực" = thiết bị **can thiệp**. Đổi hướng = **đổi đề tài**, chỉ chủ dự án quyết; hồ sơ đã viết theo trục đánh giá |
| Báo cáo đã ghi **giới hạn phạm vi**: "Hệ thống … **không phải thiết bị tập phục hồi chức năng** … chỉ theo dõi" | `docs/bao_cao/A4_doi_tuong_pham_vi.md` | Nhận đề xuất = phải viết lại A.4 **và** A.1 **và** A.2, nếu không hồ sơ tự mâu thuẫn trước hội đồng |
| Cấm thu dữ liệu trên người trước khi có phê duyệt IRB/SRC; ưu tiên staged (phantom → người lành mô phỏng → pilot bệnh nhân **chỉ khi** có ethics + bệnh viện + IRB) | `AGENTS.md` §4 (dòng 60–65), `DEC-ETHICS-001` = OPEN/PENDING | AAT chỉ có ý nghĩa khi chứng minh được nó **đang bù đúng lúc**; không có bệnh nhân thì không chứng minh được → phần "ưu việt lâm sàng" sẽ phải trình bày dạng **giả thuyết**, không phải kết quả |

Hệ quả thực tế: nếu nhận E3 (có động cơ), **bắt buộc** lùi hoặc chia nhỏ hạn nộp; nếu không lùi được, E3 biến thành "robot chưa có số liệu" — câu hỏi đầu tiên của giám khảo sẽ là *"anh có đo được gì không?"*, và lúc đó phần thưởng kỳ vọng thấp hơn cả hiện tại.

---

## 2. Kiểm toán từng tuyên bố khoa học trong bản đề xuất

Không có dòng nào dưới đây được thêm vào báo cáo nếu còn ở cột "Phải làm". Cột "Bằng chứng" ghi **id ledger + mức độ thật của việc đọc**.

| # | Tuyên bố (rút gọn từ bản đề xuất) | Đánh giá | Bằng chứng đã tìm | Cách viết an toàn / Việc phải làm |
|---|---|---|---|---|
| 1 | Đồng kích hoạt lệnh-vận-động + phản-hồi-cảm-giác củng cố kết nối thần kinh (Hebb 1949) | Chấp nhận như nguyên lý chung | nguyên lý chuẩn trong ngành; chưa cần nguồn mới | Giữ, nhưng **không** suy rộng thành "thiết bị của em tái lập bản đồ vỏ não" — em không đo vỏ não |
| 2 | "Nếu chỉ tập thụ động, chuỗi liên kết đứt gãy **vì thiếu** tín hiệu ly tâm" | **Đúng một nửa** | `SRC-RAT-META-2022`: chế độ *patient-passive* **không** cho lợi ích thêm (FM-UE SMD −0,09; p = 0,85) trong khi *passive-active* và *patient-active* có lợi ích | Viết: "bằng chứng cho thấy lợi ích bổ sung của thụ động đơn thuần **nhỏ hơn rõ rệt**, không phải bằng 0" |
| 3 | "Thụ động: gần như **không** tái cấu trúc được synap" | **Quá tuyệt đối — bỏ** | `SRC-ACTIVE-PASSIVE-2025`: **cả hai** nhóm (thụ động và chủ động) đều cải thiện FMA và MEP có ý nghĩa (p < 0,01); nhóm chủ động tốt hơn | Viết: "tác động lên thần kinh trung ương của tập thụ động **kém hơn và bằng chứng mỏng hơn**" |
| 4 | "Não **tự động** cắt giảm tối đa nỗ lực khi máy làm thay" (slacking) | **Sai cơ chế, đúng hiện tượng** | `SRC-MPC-AAN-2026`: slacking được mô tả là **hiện tượng thích nghi học được** qua tương tác lặp lại, không phải phản xạ tức thời; và error-based AAN *che giấu* slacking chứ không triệt tiêu | Viết: "khi thiết bị luôn hoàn thành phần còn thiếu, người bệnh **học** rằng không cần nỗ lực → mức tham gia giảm dần. Vì vậy thuật toán phải theo dõi **cả mức tham gia**, không chỉ sai số quỹ đạo" |
| 5 | `F_assist = F_target − F_patient`, "lực trợ giúp **tỉ lệ nghịch** với lực tự thân" | **Sai thuật ngữ + đã có người làm** | `SRC-AAN-EMG-2024` (Complex Intell Syst 10:1917–1926): đúng dạng `F_Assistive = F_Ref − F_EMG`, MYO armband 200 Hz, NN ước lượng lực, găng mềm | Nếu dùng: gọi là **bù trừ theo mức tham gia** (không phải "tỉ lệ nghịch"); thêm số hạng trọng lực + ma sát cơ cấu; **bắt buộc** trích `SRC-AAN-EMG-2024` khi nói tới ý tưởng này |
| 6 | "Velostat phát hiện nỗ lực qua biến thiên áp lực rất nhỏ do co cơ, **trước khi** ngón cử động" | **UNVERIFIED với thiết kế hiện tại — đây là điểm sống còn** | chưa có; `docs/01` §77 đã tự cấm claim "đo lực tuyệt đối/hoạt động cơ" | Phải thành **GATE A′** (§5, bước 4) với ngưỡng chốt trước. Nếu attempt isometric không tách được khỏi nhiễu + co cứng nền → cả mục 5.1 của bản đề xuất sụp |
| 7 | "Bộ lọc triệt co cứng: phân biệt xung chủ động (tăng dần) vs co giật ngoại tháp (biên độ cao đột ngột, tần số rung)" | **Chưa có cơ sở; sai dấu hiệu** | `SRC-KAPS-2017`: co cứng được định lượng bằng **quan hệ tốc độ–lực cản** trong kéo giãn thụ động (velocity-dependent, catch & creep), không phải "biên độ đột ngột" | Viết lại bộ lọc theo **tính phụ thuộc vận tốc + quan hệ lực–vận tốc**; mọi đặc trưng "tần số rung giật" phải có nguồn hoặc bị bỏ |
| 8 | "Máy thụ động tiếp tục kéo bất chấp co cứng → **rách vi thể sợi cơ, giãn bao khớp, đứt gân**, gây co quắp dữ dội hơn" | **Không đủ căn cứ ở mức tuyệt đối** | `SRC-SCIRE-PASSIVE-STRETCH` (tổng quan bằng chứng mức 4): vận động/kéo giãn thụ động nhịp nhàng **giảm** trương lực ngắn hạn; `SRC-STRETCH-CTRL-2021`: rủi ro thật là khi **đặt máy quá mạnh / không kiểm soát mô-men cản** | Viết: "rủi ro xuất hiện khi thiết bị **không giới hạn mô-men và vận tốc**; vì mọi thiết bị chấp hành của đề tài (nếu có) phải có giới hạn cứng + dừng khẩn cơ khí" |
| 9 | "Mất tới **40–50% khối lượng cơ** sau vài tháng bất động" | **Số chưa có nguồn — hoặc bỏ hoặc tìm nguồn gốc** | chưa xác minh được (tôi **không** đoán số thay) | Tạm thay bằng phát biểu định tính: "teo cơ do bất động (disuse atrophy) và xơ hóa mô kẽ là có thật, tài liệu tham khảo sẽ được bổ sung" |
| 10 | "Qua giai đoạn này: **tập luyện vô tác dụng**, chỉ còn phẫu thuật cắt gân"; "M1 teo biến, mất hoàn toàn phản xạ" | **Quá tuyệt đối, và mâu thuẫn với chính y văn** | `SRC-EMG-SOFT-HAND-2021`: bệnh nhân **mạn tính** (n = 16, 20 phiên) cải thiện ARAT/FMA-UE/BBT; `SRC-RATULS-2019` (Lancet): cải thiện vẫn xảy ra ở **cả ba** nhánh, gồm chăm sóc thường quy | Viết: "kỳ hồi phục chậm hơn và trần thấp hơn sau cửa sổ hồi phục sớm; **không có** bằng chứng cho rằng tập luyện vô tác dụng" |
| 11 | "Giai đoạn vàng 3–6 tháng đầu" | Cần nguồn; con số phổ biến nhưng em chưa có trích dẫn trong repo | chưa xác minh | Dùng "pha hồi phục sớm (thường được nhắc là vài tháng đầu)" và đặt footnote `*(verify)*` như cách A.1 đang làm |
| 12 | "Digital twin / mô hình 3D thời gian thực" để phản hồi thị giác | **Nguy cơ over-claim của chính đề tài** | `docs/01` §77 + `CLAIM_LEDGER`: hệ thống **không** đo góc khớp tuyệt đối | Chỉ được hiện **chỉ số/suy luận hướng** đã được gắn nhãn độ tin cậy; nếu avatar khớp ngón thì **phải** qua GATE B trước, và ghi rõ "minh họa" |

> Ghi chú quy trình: 12/12 dòng trên đều chạm `AGENTS.md` — "không nâng mức bằng chứng", "một lần không tìm thấy = `UNVERIFIED`". Vì vậy ở §2 tôi **không** kết luận "sai", tôi kết luận "chưa đủ căn cứ để in vào báo cáo", kèm đường thoát (bỏ / làm mềm / test ở GATE).

---

## 3. Ma trận va chạm prior art cho hướng "active-assisted" (lượt 1, chưa đọc toàn văn)

### 3.1 Quốc tế — phần "thiết bị kéo + phát hiện ý định" đã rất đông

| Nguồn | Đã làm gì | Va chạm với bản đề xuất |
|---|---|---|
| `SRC-IRONHAND-2018` (JNER, găng mềm dẫn động gân) | **Intention-detection logic** để chỉ kích hoạt lực đỡ khi người dùng thực sự có ý định; lực đỡ **tỉ lệ với** lực gập của người dùng; người dùng chủ động đóng góp vào động tác | Trùng **toàn bộ** mục 3.2 (AAN) ở tầng khái niệm. Khác: của họ là **gập** để cầm nắm (ADL), không phải duỗi thụ động để tập, không có đo hướng qua vách |
| `SRC-AAN-EMG-2024` (Complex Intell Syst) | AAN cho găng mềm, ước lượng lực người bằng **EMG + NN**, công thức `F_Assistive = F_Ref − F_EMG` | Trùng **đúng công thức** mục 3.2(3) |
| `SRC-EMG-SOFT-HAND-2021` (J Stroke Cerebrovas Dis) | Găng mềm **dẫn động EMG**, 20 phiên × 1 giờ, n = 16 bệnh nhân mạn tính: cải thiện ARAT, FMA-UE, FMA-WH, BBT, lực bóp; ghi nhận giới hạn ở người **co cứng nặng** | Là bằng chứng lâm sàng cho cơ chế đề xuất — và cũng là bằng chứng rằng **co cứng nặng thì thiết bịหมด tác dụng** (điều bản đề xuất không nói) |
| `SRC-BIDIR-SRG-2023` (JNER 10.1186/s12984-023-01250-4) | Găng vải **hai chiều** (gập + duỗi), mô-men duỗi đỉnh **2,8 N·m**, n = 8, cải thiện Open-Hand Tasks (p = 0,018) | Số liệu "lực bao nhiêu là đủ để thắng co cứng" đã có — mục 5 của em phải viện dẫn, không được tự đặt |
| `SRC-MAG-GLOVE-DEVICE-2024` (*Device*) | Găng mềm điều khiển bằng **từ**, tại nhà, **BOM 423 USD** (chưa điện tử: 22 USD); nêu khoảng giá hệ thống PHCN tại nhà đã được FDA chấp thuận: **~350–6.000 USD** | Pháclaim "rẻ" nếu em chỉ so với thiết bị ngoại nhập: **chuẩn chi phí đã bị chiếm** |
| `SRC-THUMB-AAN-2026` (găng cườm bàn cái, origami đôi buồng) | Đầu ngón **18 N ≈ gấp đôi** mức cần để thắng co cứng sau đột quỵ; cảm biến lực + IMU; app chọn chế độ; bộ tối ưu **hỗ trợ ở mức thấp nhất** để tối đa hóa sự tham gia | Đây là **SOTA của chính ý tưởng** em vừa đề xuất (2026). Mọi câu "chưa ai làm AAN cho ngón tay" là sai |
| `SRC-RATULS-2019` (Lancet, RATULS) | RCT đa trung tâm lớn: tập **có robot** (MIT-Manus) **không** hơn chăm sóc thường quy về **chức năng** (ARAT) ở 3 tháng; chỉ hơn nhẹ ở impairment (FMA) | Câu phản-bác mạnh nhất mà giám khảo có thể hỏi: "thêm robot thì tốt hơn ở chỗ nào?" — phải trả lời được, không được lờ đi |
| `SRC-MPC-AAN-2026` | AAN dựa trên sai số **che giấu** slacking; cần **hai kênh** (độ lợi trợ giúp + độ lợi phản ánh mức tham gia) + ràng buộc năng lượng để chống slacking | Cho thấy mục 4 "Bị triệt tiêu slacking" là **sai**; và cho em một **chỉ số** đáng giá: *tỷ lệ tham gia của người bệnh* (thứ đo được bằng… cảm biến, không cần động cơ) |
| `SRC-NEOFECT-SMARTGLOVE` | Găng **chỉ cảm biến** (132 g, flex + 9-DoF) + **game phản hồi hình-ảnh-tiếng** + số liệu hiệu suất cho chuyên gia; chỉ định gồm người **sau đột quỵ**; dùng tại nhà; ~1.925 USD (hoặc thuê 99 USD/tháng) | Đúng hình dạng **E2-lite**: vòng khép kín bằng **phản hồi thị giác**, không bằng mô-tơ. Vừa là hậu thuẫn, vừa là prior art phải trích |

### 3.2 Trong nước — hướng này **đã có người làm**, và làm ở mức đại học

| Nguồn | Nội dung theo báo chí (mức `UNVERIFIED`) | Hệ quả |
|---|---|---|
| `SRC-VNM-ANNAM-2022` + `SRC-VNM-REHABTECH-GD-2022` | Nhóm ANNAM/RehabTech, ĐH Bách khoa Đà Nẵng: găng **PneuNet silicon 5 ngón**, bơm khí → co, hút khí → duỗi, **có** chức năng duỗi; hở lòng bàn tay để kích thích xúc giác; **đã cho bệnh nhân + KTV BV Đa khoa Đà Nẵng dùng thử**; chi phí ~4,5–5 triệu; giải Nhất EPICS 2022 | Đây **chính là** "active-assisted glove" phiên bản Việt. Nếu em chọn E3, em vào sau và trùng ý tưởng |
| `SRC-VNM-TL-GLOVE-2026` (Báo Thanh Niên, 18/09/2026) | ĐH Thủy lợi: 5 SV, găng robot **"bộ khung trợ lực"**, "điều khiển bộ phận trợ lực để **kéo mở hoặc gập các ngón tay** theo biên độ phù hợp", nhiều chế độ tập, **theo dõi từ xa**, xử lý ảnh + điều khiển giọng nói + app | Trùng **cả hai**: trợ lực cơ học **và** theo dõi từ xa. Ngày công bố 18/09/2026 — ngay trước phiên này |
| `SRC-VNM-HS-GLove-2026` | Học sinh THPT (Tuyên Quang, 07/2026): găng "cảm biến lực và áp suất khí đo lực bóp, co giãn ngón", theo dõi % phục hồi, điều chỉnh chế độ luyện tập; giải Nhất cấp tỉnh | Đối thủ **cùng sân chơi**, đã có chữ "tập + theo dõi" |

**Kết luận §3:** "AAT + phát hiện nỗ lực + bù lực" **không phải chỗ trống**. Chỗ trống *còn lại* — khớp với kết luận của `research/reviews/2026-09-19_prior_art_novelty_gate1.md` — là ở **lớp đo**: *(i)* suy ra dấu hướng gập/duỗi từ vách có preload mà không encoder/IMU; *(ii)* tự gắn cờ `UNRELIABLE`; *(iii)* **định lượng mức trợ giúp cần thiết như một chỉ số theo dõi dọc** — thứ mà các găng có động cơ ở trên **không báo cáo** theo cách đó (họ báo cáo ROM/lực/ARAT), và thứ mà găng cảm biến thuần (Neofect) không đo.

---

## 4. Nếu vẫn làm E3 (động cơ): chi phí kỹ thuật thật

Ước lượng cho **một** ngón cái + **một** ngón trỏ (không phải 5 ngón), trên giả định mọi thứ chạy ngay từ đầu — thực tế luôn dài hơn:

| Hạng mục | Việc bắt buộc | Thời gian tối thiểu | Rủi ro chính |
|---|---|---|---|
| Cơ khí | truyền động (linear servo hoặc PneuNet + bơm), bowden/cáp, khớp neo, tăng đưa, in 3D ≥ 2 vòng lặp | 3–5 tuần | misalignment khớp; ma sát cáp phi tuyến làm **chính tín hiệu Velostat bị nhiễu** |
| Điện | driver, nguồn 12–24 V, đo dòng, **dừng khẩn cơ khí**, watchdog | 1–2 tuần | runaway; mất điện khi ngón đang bị kéo |
| Điều khiển | vòng vị trí/lực, limiter mô-men, policy AAN (2 kênh như `SRC-MPC-AAN-2026`), hiệu chuẩn theo người | 3–6 tuần | không ổn định khi co cứng thay đổi trong phiên |
| An toàn | giới hạn mô-men theo KTV, test phantom tới hỏng, hồ sơ rủi ro | 1–2 tuần (cứng, không được bỏ) | **chấn thương thật** nếu bỏ |
| Đo kiểm | bench mô-men/góc; pilot người → **chờ IRB/SRC** | không xác định | dự án đứng ở đây |
| **Tổng** | | **8–15 tuần** cho bản demo tối thiểu, **chưa tính** phần đo hiện có | |

Cộng dồn vào trạng thái thật của repo: **0 dòng firmware ESP32-S3**, `GATE 0` chưa chạy được, `perturbation_log.csv` còn là template mang hình hài đề tài cũ (đế lót chân). E3 không phải "thêm một tính năng"; E3 là **đổi đề tài**.

Tác dụng phụ về khoa học: thêm chấp hành làm **mất sự sạch của phép đo** (dòng điện động cơ + rung cơ cấu lọt vào kênh áp trở), tức là đe dọa chính GATE A/B/C mà `DEC-METRIC-001` đã chốt ngưỡng.

---

## 5. Ba phương án — khuyến nghị là **E2-lite**

### E1 — Nhận **lý thuyết**, bỏ **thiết bị** (0 dòng code; ~1 tuần)
Chép mục 1–4 (sau khi sửa §2) vào `docs/02` + `A.1`; mục 5 ghi là *Future work*.
- Được: trả lời giám khảo câu "vì sao cái em đo lại quan trọng về thần kinh".
- Mất: không tăng novelty; vẫn là "găng đánh giá".

### E2-lite (KHUYẾN NGHỊ) — Lý thuyết E1 + biến AAT thành **chỉ số đo được, không động cơ** (~3–5 tuần)
Nguyên tắc: lấy đúng *phần đo được* của AAN, bỏ phần *tác động lực*.

1. **Chỉ số nỗ lực (Effort Index).** Ghi tín hiệu vách trong cửa sổ "cố phát lực nhưng ngón **chưa** di chuyển" (isometric attempt). Đây là phép kiểm duy nhất biến "ý định vận động" thành số — và là giả thuyết **chưa được kiểm chứng** → phải qua **GATE A′**.
2. **Gap AROM − PROM.** Hai protocol trong **cùng một phiên**, cùng mảng cảm biến: (a) người bệnh tự gập/duỗi; (b) KTV (hoặc chính tay lành) đưa thụ động qua tầm. Đơn vị: **mẫu ADC đã chuẩn hóa / chỉ số suy luận hướng** — **không** quy đổi ra độ (cấm theo `AGENTS.md`). `Gap = ROM_thụ_động − ROM_chủ_động`.
3. **RAL — Required Assistance Level, không cần mô-tơ.** Dùng **lò xo kéo / ròng rọc có tải biết trước** (thụ động, không nguồn, không nguy hiểm) làm "mức trợ giúp" rời rạc (0 g, m₁ g, m₂ g, m₃ g). Với mỗi mức, ghi **tỷ lệ hoàn thành động tác**. Đường cong *mức trợ giúp – tỷ lệ hoàn thành* xấp xỉ chính đường cong lực–khớp mà AAN cần để điều khiển, nhưng **không** đưa động cơ vào tay bệnh nhân. Đây là điểm có thể thành **ứng viên novelty C′**: *lượng hóa mức trợ giúp cần thiết + tự gắn cờ độ tin cậy, để theo dõi dọc tại nhà.*
4. **Phản hồi thị giác (không phải digital twin).** Cho người bệnh thấy **thanh nỗ lực** và **số lần hoàn thành** ngay trong phiên → đóng vòng closed-loop bằng mắt, thứ mà `SRC-NEOFECT-SMARTGLOVE` đã thương mại hóa (nên phải trích, không được claim).
5. **GATE mới cần chủ dự án chốt số** (tôi để `TBD-chủ-dự-án`, không tự đặt ngưỡng):
   - `GATE A′`: phân biệt "attempt isometric" vs "nghỉ" trên ≥ 8 mẫu × ≥ 3 tư thế; metric AUC + tỷ lệ báo nhầm; **nếu không tách được → bỏ mục 1** (và bỏ luôn lập luận "phát hiện ý định" trong `A.7`).
   - `GATE RAL`: đường cong trợ giúp đơn điệu + ICC giữa 2 phiên; ngưỡng trùng khung MDC/ICC đã dùng ở GATE C để nhất quán thống kê.
6. **Việc bắt buộc trước khi viết khác biệt:** đọc toàn văn `SRC-IRONHAND-2018`, `SRC-AAN-EMG-2024`, `SRC-THUMB-AAN-2026`, `SRC-KAPS-2017`; tra IPC `A61H1/02`, `A61H3/01`, `A47G21/04` cho găng trợ lực.

### E3 — Full active-assisted (động cơ + vòng kín AAN): **chỉ khi** chủ dự án chấp nhận cả bốn
(i) đổi `DEC-TOPIC-019` + viết lại `A.1`/`A.2`/`A.4`; (ii) lùi hoặc chia nhỏ hạn nộp theo §4; (iii) demo **chỉ trên phantom + người tình nguyện khỏe mạnh sau khi có phê duyệt**, tuyệt đối không trên bệnh nhân khi `DEC-ETHICS-001` còn PENDING; (iv) giới hạn mô-men cứng do KTV chốt + dừng khẩn cơ khí, hồ sơ rủi ro.
Nếu thiếu một trong bốn → tôi khuyến nghị **không** chọn.

---

## 6. "Đủ tầm" — nói thẳng một câu

Ở ViSEF, phần làm hội đồng tin là **số liệu + cách tự kiểm chứng**, không phải số bộ phận. Một đề tài có robot nhưng **0 kết quả đo** yếu hơn một đề tài **chỉ đo** nhưng có: MDC/ICC cạnh tranh được với y văn (`SRC-STEF-MDC-2026`: MDC95 = 12,7 điểm; `SRC-MANUMETER-RCT-2022`: MDC ≈ 31%), ngưỡng GATE chốt trước, và tự gắn cờ dữ liệu không tin cậy được. E2-lite tăng **độ sâu** (thêm một chỉ số lâm sàng có tên, có định nghĩa, có gate) mà không đổi **loại rủi ro**. Đó là cách rẻ nhất để đề tài "đủ tầm" hơn.

---

## 7. Em (agent) đã ghi gì vào repo trong lượt này — **chưa commit, chưa push**

- `docs/03`: thêm **Nhóm 13** "găng tập có trợ lực / AAN / an toàn co cứng" + trạng thái và việc nợ.
- `SOURCE_LEDGER.csv`: thêm 16 dòng `SRC-AAT-*`/`SRC-RAT-*`/`SRC-VNM-*` — **tất cả** ở mức `READ_ABSTRACT`/`UNVERIFIED`/`UNVERIFIED`, ghi rõ chưa đọc toàn văn.
- `CLAIM_LEDGER.csv`: `CLM-BIO-002` (cơ sở thần kinh của AAT so với thụ động) = `PARTIALLY_CONTESTED`; `CLM-SCOPE-001` (đổi phạm vi sang thiết bị can thiệp) = `PROPOSED_NEEDS_OWNER`.
- `DECISION_LOG.md`: `DEC-SCOPE-002` **PROPOSED** (E1 / E2-lite / E3) + 3 open items mới.
- `docs/bao_cao/A7_AAT_rationale_DRAFT.md`: bản **viết lại an toàn** của mục 1–4 cho báo cáo — bảng đã sửa (bản gốc bị vỡ markdown + lẫn link tự động `[não.Kh](http://não.Kh)`), LaTeX `$...$` đã thay bằng ký tự thường vì GitHub/báo cáo không render, mọi câu quá tuyệt đối đã thay bằng câu có điều kiện + `(verify)` footnote.
- `QUERY_LOG.jsonl`: +7 bản ghi tìm kiếm (mục 6).
- **Không** đổi `docs/01` §1 (tên đề tài), **không** đổi `A.4`, **không** đổi ngưỡng GATE, **không** commit/push.

---

## 8. Bốn câu hỏi cần chủ dự án trả lời

1. Chọn **E1**, **E2-lite** (khuyến nghị), hay **E3**? Nếu E3: chấp nhận lùi hạn nộp bao lâu?
2. E2-lite cần **KTV chốt bộ đôi protocol** "tự gập/duỗi" vs "thụ động qua tầm" + bảng tải lò xo cho RAL — anh có đường lấy ý kiến KTV trong 2 tuần tới không?
3. Có cho phép tôi đưa `A.7_AAT_rationale_DRAFT.md` vào outline báo cáo (mục B — cơ sở lý thuyết) **với điều kiện** giữ nguyên các footnote `(verify)` và các câu điều kiện?
4. Số "40–50% khối lượng cơ" và "giai đoạn vàng 3–6 tháng": anh muốn (a) tôi tìm nguồn gốc có DOI, hay (b) bỏ khỏi báo cáo? Mặc định an toàn = **(b)**.

---

## 9. Hiệu chuẩn lại theo chuẩn thật của cuộc thi (phản hồi của chủ dự án)

Chủ dự án đúng ở 4 điểm, và em ghi thành nguyên tắc làm việc:

1. **Novelty ở ViSEF/ISEF là novelty ở tầng *bài toán + cách tổ hợp*, không phải tầng *nguyên lý*.** Yêu cầu "chưa ai từng làm cơ chế này" là tiêu chuẩn bài báo; nó **loại** các dự án học sinh và cũng không phải thứ giám khảo chấm.
2. **Giám khảo chấm cái họ nhìn thấy trong 7 phút:** câu chuyện sắc, thiết bị chạy thật, số liệu tự đo, và một demo tái lập được. Một nguyên lý mới mà thiết bị không chạy = điểm thấp hơn một tái tổ hợp chạy tốt.
3. **"Kết nối đồ có sẵn" là chiến lược thắng hợp lệ** — với điều kiện phần kết nối đó **được trình bày như một hệ thống có lập luận**, không phải đống module. Đã xác minh được ví dụ (xem **§11**): dự án ISEF 2025 của chính học sinh THPT thị xã Quảng Trị, 100% đồ có sẵn, **giải Tư**.
4. Vì vậy câu hỏi đúng **không phải** "cái này đã có ai làm chưa?" mà là "**phần nào của cái đã có đó, em làm khác đi và chứng minh được bằng số liệu của chính em?**"

Điều **không** đổi vì hiệu chuẩn này (vì đây là luật của cuộc thi, không phải chuẩn journal): an toàn + phê duyệt đạo đức khi có tác động lực lên người, và không được tuyên bố vượt quá số liệu em tự đo.

## 10. **E4 + E5 (KHUYẾN NGHỊ MỚI)** — lấy trọn câu chuyện AAT, không động cơ trên người

Ý tưởng cốt: **đưa bộ chấp hành vào… con rối thử nghiệm (phantom), không đưa vào bàn tay bệnh nhân.** Toàn bộ vòng AAT chạy và được đo; người duy nhất đeo găng là người **không** bị máy kéo.

### E4 — Rig "bàn tay có co cứng chỉnh được" + chỉ số RAL (nền tảng, ~2–3 tuần)
- **Cấu tạo:** 1 lóng ngón in 3D trên trục có lò xo kéo về + **puli có tải treo** (quả cân 20/40/80/120 g) để đặt **mức cản chủ động** = mô phỏng mức co cứng/ yếu cơ theo nấc, **đo được bằng lực kế lò xo** (không cần cảm biến lực chuẩn y tế).
- **Việc đo được trên rig:** (i) găng có phân biệt được *nỗ lực* với *không nỗ lực* khi ngón **chưa** di chuyển hay không (**GATE A′**); (ii) tải nhỏ nhất để động tác hoàn thành (RAL) có đơn điệu và lặp lại giữa 2 phiên không (**GATE RAL**); (iii) bộ lọc co cứng hoạt động theo **quan hệ tốc độ–lực cản** (học từ `SRC-KAPS-2017`) có tách được "tải cao" khỏi "co cứng" không — đây là câu hỏi khoa học thật, và rig trả lời được.
- **Vì sao đây là "cách đi khác":** cả lĩnh vực AAN đo nỗ lực bằng **EMG**; em đo bằng **áp trở trên vách + tải cơ đã biết** → cùng một thông tin (mức tham gia) nhưng không cần điện cơ, không cần dán điện cực, dùng được tại nhà. Đó là *different angle, same problem* đúng như chủ dự án mô tả.
- **Không cần IRB:** mọi phép đo ở bước này là trên rig (`research/protocols/06` §"GATE 0–F chạy trên bench/phantom, không cần người tham gia").

### E5 — Một servo, kéo **phantom**, khép vòng AAT cho demo (~1 tuần, cộng thêm)
- Servo + puli trên rig, điều khiển theo đúng luật AAN đã nêu: phát hiện nỗ lực → nếu sau `T_window` chưa đạt đích thì bù dần → đạt thì dừng; kèm **giới hạn lực cứng** và nút dừng khẩn.
- Demo 5 phút cho hội đồng: *người đeo găng cố → máy chỉ kéo con rối song song → màn hình hiện "nỗ lực 62%, RAL giảm từ 120 g xuống 40 g sau 10 phiên"*. Câu chuyện active-assisted hiện đủ, mà **không có lực nào tác động lên người**.
- Cách nói với hội đồng (trung thực + vẫn mạnh): *"Vòng khép kín đã chứng minh trên rig chuẩn hoá. Đưa lên bệnh nhân cần phê duyệt đạo đức và thử nghiệm lâm sàng — em nêu rõ trong phần Hạn chế và Hướng phát triển."* Đây là điểm **cộng** chứ không trừ: cho thấy em biết ranh giới.
- Chi phí thêm: 1 servo (MG996S/DS3218) + driver + nguồn + puli/lò xo — **không** cần 5 ngón, **không** cần Bowden trên người, **không** cần cân bằng mô-men ngón.

### E6 (tuỳ chọn, 0 rủi ro, ~2–4 ngày code) — Tầng "kê đơn" phần mềm
Găng đo → sinh **liều tập trong tuần** theo quy tắc minh bạch (số lần/nỗ lực đạt/RAL hiện tại) + **báo cáo cho KTV** + tự gắn cờ phiên `UNRELIABLE`. Đây chính là "kết nối nhiều thứ có sẵn" mà chủ dự án muốn — và nó nằm gọn trong phần cứng đã chốt (ESP32-S3 + app).

### Thứ tự đề xuất
`E4 → GATE A′/RAL (chốt ngưỡng) → E5 cho demo → E6 nếu còn thời gian → A.7 vào báo cáo`.
**E3 (kéo trên người)** chỉ khi: có phê duyệt đạo đức + bệnh viện đồng hành + lùi hạn nộp ≥ 8 tuần. Không có ba thứ đó thì E3 = rủi ro bị loại hồ sơ, không phải điểm cộng.

### Việc cần chủ dự án duyệt (agent không tự đặt số)
1. `GATE A′` — ngưỡng attempt-vs-rest: đề xuất AUC ≥ 0,85 và tỷ lệ báo nhầm ≤ 10% trên ≥ 8 mẫu × 3 mức tải. **Chốt trước khi đo.**
2. `GATE RAL` — đề xuất: đường cong *tải–tỷ lệ hoàn thành* đơn điệu 100% + ICC ≥ 0,75 giữa 2 phiên trên cùng tải. **Chốt trước khi đo.**
3. Có chế tạo rig E4 không (in 3D + lò xo + puli + tải + 1 servo)? Ước lượng vật tư thấp; rủi ro kỹ thuật chính là độ rơ của puli.
4. Phiếu hỏi KTV (`research/protocols/07_ral_phantom_and_ktv_interview.md`, đã soạn sẵn) — anh gửi/bốc lịch trong 2 tuần như đã xác nhận.

---

## 11. Chuẩn tham chiếu đã xác minh: **ISEF 2025 ROBO065T** (Quảng Trị) — và bài toán của mình phải giống *hình dạng* này

Nguồn: trang chính thức của hội thi `isef.net/project/robo065t-autonomous-wheelchair-for-als-patients` (mã **VNM001 / ROBO065T**, mục *Robotics and Intelligent Machines*) + báo chí Việt Nam. Chủ dự án cùng trường cấp tỉnh với nhóm này (THPT thị xã Quảng Trị) → **đây là chuẩn tham chiếu tại chỗ, không phải ví dụ xa**.

| Thứ họ làm | Chi tiết | Suy ra cho đề tài |
|---|---|---|
| **Không có nguyên lý mới** | YOLO11 (phát hiện đồng tử) + hồi quy đa thức (ước lượng điểm nhìn); **SLAM Toolbox + Nav2** + DWB controller đã chỉnh để tự lùi trong chỗ hẹp; joystick giả lập qua **DAC** + PID (8 hướng); **Gemma2 fine-tune** biến chọn từ → 3 câu, phát tiếng + **Telegram**; GUI hợp nhất | Em được phép dùng Velostat + ESP32-S3 + một mô hình nhỏ đã có. **Không** cần phát minh vật lý. Đây là bằng chứng rằng phần em lo ("sidewall đã có từ 2015") **không phải** điều kiện trúng giải |
| **Bài toán ghép** | Câu mở đầu của họ: "current smart wheelchairs are unable to *simultaneously* address both mobility and communication needs" — thắng ở chỗ **ghép 2 nhu cầu vào một hệ thống cho đúng một nhóm người dùng** | Đề tài phải nêu một câu ghép tương tự. Khớp nhất với E4/E5: *"cùng một chiếc găng đo được cả **tầm chủ động** và **tầm thụ động**, nên lượng hóa được **khoảng cách AROM−PROM** và **mức trợ giúp cần thiết** — thứ mà găng đo ROM chỉ làm một trong hai"* |
| **Câu claim là claim tích hợp** | "This solution represents the **first fully integrated** mobility-communication system engineered for ALS patients" | Format câu được thưởng ở ISEF = *"first integrated X + Y for [nhóm người dùng cụ thể]"*, **không phải** *"first to discover [nguyên lý]"*. Và họ vẫn dùng chữ "first" — có điều "first **integrated**", tức là giới hạn đúng phạm vi hệ thống của họ |
| **4 con số tự đo** | 97,11% accuracy điểm nhìn · 0,12 m sai số bám quỹ đạo · 93,33% điều hướng tự hành thành công · < 5,33 s sinh câu | **Punch list của em (§12)** — đây là mục duy nhất đề tài bắt buộc có số, và rig E4 tạo ra được số mà không cần bệnh nhân |
| **Không vướng đạo đức** | Đo hiệu năng **hệ thống** (accuracy, sai số, tỷ lệ thành công, độ trễ), không tuyên bố kết quả lâm sàng | E4/E5 giữ đúng khuôn này: số liệu trên rig + mô hình; mọi câu về bệnh nhân để ở mục *Giả thuyết / Future work*. **Không** phải tự kiểm duyệt — đây là khuôn đã được hội thi thưởng |

## 12. Punch list — bộ số liệu đề tài phải tự đo để chơi cùng chiếu

| # | Con số | Đo trên gì | Nguồn ngưỡng |
|---|---|---|---|
| 1 | AUC phân biệt *cố phát lực* vs *nghỉ* | Rig E4 (tải treo 0→120 g) | `GATE A′` — chủ dự án chốt |
| 2 | Bậc tải nhỏ nhất phân biệt được (độ phân giải RAL) + tỷ lệ hoàn thành theo bậc | Rig E4 | `GATE RAL` |
| 3 | Lặp lại giữa 2 phiên (ICC) của Effort Index & Gap | Rig E4, cùng cấu hình | khớp khung ICC đã dùng ở GATE C |
| 4 | Tỷ lệ phiên bị gắn cờ `UNRELIABLE` **đúng** khi em cố tình làm hỏng (gắn lệch/đứt dây/tải trôi) | Rig E4 + fault injection | GATE E (đã có) |
| 5 | Độ trễ từ nỗ lực → phản hồi hiển thị (ms) | Toàn mạch: ESP32-S3 → app | GATE F (đã có) |
| 6 | (Nếu E5) Sai số bám theo mốc đích của servo trên rig (mm/góc chuẩn hóa) + tỷ lệ chu kỳ hoàn thành | Rig E5 | ngưỡng mới, do chủ dự án chốt |

Điểm mấu chốt: **6 số này không cần bệnh nhân, không cần IRB, và không cần cảm biến y tế chuẩn.** rig + load cell/lực kế lò xo + đồng hồ bấm là đo được hết.

## 13. Hai câu em phải nói lại với anh (vì phát hiện mới này đổi khuyến nghị)

1. **E5 (một servo kéo phantom) không còn là "nice-to-have cho demo"** — nó chính là thứ tạo ra các số #6 và làm đề tài có "máy chạy thật" giống khuôn ROBO065T. Em nâng nó từ *tuỳ chọn* lên **nên làm**, chi phí ~1 tuần.
2. **E3 (kéo trên người) vẫn không nên** — nhưng lý do giờ **không còn** là "prior art đông". Lý do duy nhất còn lại là **đạo đức/an toàn + không có thời gian**. Nghĩa là: nếu anh muốn phần đó, cách đúng là chuẩn hoá hồ sơ ethis và để dành cho mùa sau — còn mùa này là rig.
3. Về `docs/03`/GAP 1: phát hiện này **không** thay đổi kết luận hạ bậc novelty A (vẫn phải trích sidewall 2015 + ART-Glove 2026 khi viết phần *khoa học*), nhưng **có** thay đổi *mức thiệt hại*: ở tầng hội thi, phần em lo là "đã có người làm" thực ra chỉ buộc mình **trích dẫn đúng**, không buộc mình **bỏ tính năng**. Em sẽ ghi rõ khác biệt giữa "mức an toàn khi trích dẫn" (journal) và "mức đủ để thi" (fair) trong `research/reviews/2026-09-19_prior_art_novelty_gate1.md` §4 để lần sau không nhầm nữa.
