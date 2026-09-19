# A.7 — Cơ sở khoa học của "tập chủ động có ý thức" và hệ quả measurement (BẢN NHÁP)

> **Trạng thái:** `DRAFT` — chủ dự án chốt giữ nguyên bản nháp (2026-09-19). Phạm vi đã duyệt là E4+E5+E6 (`DEC-SCOPE-003`), nhưng **giai đoạn này chỉ làm cơ sở lý thuyết**; bản chính thức sẽ viết sau khi §1.4–§7.3 của `docs/02` được duyệt nội dung.
> **Không** đưa ví dụ thành tích hội thi (ROBO065T/ISEF 2025) vào hồ sơ nộp — chỉ lưu trong `research/`.
> **Nguồn:** viết lại từ đề xuất của chủ dự án ngày 2026-09-19, sau khi kiểm toán từng tuyên bố tại
> `research/reviews/2026-09-19_active_assisted_scope_options.md` §2.
> **Quy tắc áp dụng:** không nâng mức bằng chứng; số nào có `(verify)` là **chưa được xác minh**, phải hoặc tìm nguồn hoặc bỏ.
> **Phạm vi thiết bị (nguyên trạng):** găng tay **đo và theo dõi**. Không có bộ phận chấp hành, không kéo/gập ngón tay hộ người bệnh.
> Nếu `DEC-SCOPE-002` chọn E3 (thêm động cơ) thì đoạn "Giới hạn" ở cuối phải viết lại **và** tên đề tài phải đổi theo.

---

## 1. Ba chế độ tập, phân biệt theo "ai phát lực"

| Chế độ | Ai tạo chuyển động | Ý nghĩa với hệ thần kinh |
|---|---|---|
| **Thụ động (Passive)** | Ngoại lực (người hoặc máy); người bệnh **không** cần phát lệnh | Duy trì tầm vận động khớp (PROM), mô mềm; tác động trung ương **kém hơn** |
| **Chủ động có trợ lực (Active-Assisted, AAT)** | Người bệnh **phát lệnh + phát lực**; thiết bị **chỉ bù phần còn thiếu** | Vừa có lệnh vận động đi ra, vừa có cảm giác bản thể dội về trong cùng một khoảnh khắc |
| **Chủ động kháng lực (Active-Resist)** | Người bệnh thắng thêm tải | Giai đoạn sau, không thuộc phạm vi đề tài |

**PROM vs AROM.** Tập thụ động giữ được **PROM** (khớp không dính). Mục tiêu của phục hồi chức năng bàn tay là chuyển PROM thành **AROM** — người bệnh **tự** làm được động tác. Khoảng cách giữa hai cái đó chính là thứ đề tài này đo (§4).

## 2. Vì sao "nỗ lực có ý thức" là điều kiện cần (viết ở mức bằng chứng cho phép)

```
[ Ý định vận động ở vỏ não vận động sơ cấp M1 + vùng tiền vận động ]
                     │   xung ly tâm (efferent) → tủy sống → đơn vị vận động
                     ▼
        [ Cơ ngón/cẳng tay co một phần ]  ──►  [ Cảm biến áp trở ghi nhận ]
                     │                                   │
                     ▼                                   ▼
        [ Ngón cử động thật ]  ◄── (phần còn thiếu do thiết bị/tay lành/tải bù)
                     │
                     ▼
[ Thụ thể bản thể: thoi cơ, gân Golgi, bao khớp ] ──► xung hướng tâm (afferent) ──► [ S1 ]
```

- **Nguyên lý Hebb (1949):** "neurons that fire together, wire together". Tái tổ chức khớp nối thần kinh xảy ra khi tín hiệu *lệnh* và tín hiệu *phản hồi* đến **đồng thời**. AAT tạo đúng điều kiện đồng thời đó; tập thụ động chỉ có nửa sau (afferent).
- **Vòng phản hồi khép kín:** người bệnh cố gắng → tay cử động thật → mắt thấy + tay cảm nhận → não ghi nhận "thành công". Đây là cơ chế khiến **phản hồi thị giác tức thời** có giá trị, kể cả khi **không** có động cơ (đề tài khai thác đúng phần này — xem §4.4).
- **"Bất hoạt do học được" (learned non-use):** nếu lệnh phát ra mà chi thể không đáp ứng lặp đi lặp lại, vùng biểu diễn có xu hướng co lại và bị chức năng lân cận lấn chiếm (maladaptive plasticity). Đây là lý do phải **phát hiện được nỗ lực** chứ không chỉ phát hiện được chuyển động hoàn chỉnh.
- **Giới hạn trung thực:** đề tài **không** đo hoạt động vỏ não (không EEG/fNIRS/TMS). Toàn bộ suy luận trên là **cơ sở lý thuyết để chọn chỉ số đo**, không phải kết quả thực nghiệm của đề tài.

## 3. "Hỗ trợ theo nhu cầu" (Assist-as-Needed) — và một hiệu ứng phải nêu

- **Định nghĩa:** thiết bị chỉ can thiệp khi (1) có nỗ lực vượt ngưỡng nền, (2) nỗ lực đó không đủ để đạt mục tiêu trong cửa sổ thời gian cho phép, (3) mức bù **giảm dần** khi người bệnh làm được nhiều hơn.
- **Công thức thường gặp** trong tài liệu điều khiển: `F_trợ_giúp = F_mục_tiêu − F_người_bệnh` (bù **trừ**, không phải "tỉ lệ nghịch"); bản đầy đủ còn thêm trọng lực và ma sát cơ cấu. Tiền lệ: `SRC-AAN-EMG-2024` (ước lượng lực người bằng EMG rồi trừ khỏi lực tham chiếu), `SRC-IRONHAND-2018` (lực đỡ tỉ lệ với lực người dùng, kèm logic nhận ý định).
- **Hiệu ứng ỷ lại (motor slacking):** y văn mô tả đây là **thích nghi học được** — người bệnh học rằng máy sẽ lo phần còn lại nên giảm dần nỗ lực — **không phải** phản xạ tự động tức thời. Quan trọng hơn: **bản thân AAN đo theo sai số quỹ đạo không triệt tiêu được slacking**; tài liệu 2026 phải tách thành **hai kênh điều khiển** (độ lợi trợ giúp + độ lợi phản ánh mức tham gia) mới giữ được nỗ lực (`SRC-MPC-AAN-2026`).
- **Hệ quả cho đề tài (đây là chỗ đề tài có phần riêng):** muốn chống ỷ lại thì phải **đo được mức tham gia**, và việc đo mức tham gia **không cần động cơ**.

## 4. Ba chỉ số đề tài đo được, lấy cảm hứng trực tiếp từ AAT (không cần bộ chấp hành)

| Chỉ số | Định nghĩa thao tác | Đơn vị | Trạng thái |
|---|---|---|---|
| **Effort Index** | Tín hiệu vách trong cửa sổ "cố phát lực nhưng ngón chưa di chuyển" | mẫu ADC đã chuẩn hóa | **Giả thuyết** — phải qua `GATE A′` |
| **Gap AROM − PROM** | `ROM_thụ_động − ROM_chủ_động`, đo **cùng phiên**, cùng mảng cảm biến | chỉ số suy luận hướng (không quy đổi ra độ) | cần KTV chốt protocol |
| **RAL (Required Assistance Level)** *(chờ GATE A′/RAL — `research/protocols/07`)* | Tải hỗ trợ rời rạc **nhỏ nhất** (lò xo/tải trọng, thụ động) để động tác hoàn thành; vẽ đường cong *tải – tỷ lệ hoàn thành* | gram + tỷ lệ % | ứng viên novelty C′ |

**4.4 Phản hồi.** Trong phiên đo, người bệnh thấy *thanh nỗ lực* và *số lần hoàn thành* → đóng vòng phản hồi bằng thị giác. Không dựng avatar 3D theo góc khớp khi chưa qua `GATE B`; nếu dựng thì ghi rõ "hình minh họa".

**4.5 Trần kỳ vọng (nêu thẳng trong báo cáo).** Thiết bị thương mại **chỉ cảm biến + game** cho cùng mục đích đã tồn tại (`SRC-NEOFECT-SMARTGLOVE`, ~1.925 USD, có chỉ định dùng cho người sau đột quỵ). Đề tài **không** cạnh tranh tính "đã thương mại hóa"; đề tài cạnh tranh ở **chi phí phần cứng + cách suy luận hướng + tự gắn cờ độ tin cậy + RAL**.

## 5. Hai kịch bản không có công cụ theo dõi (bản đã hạ nhiệt so với đề xuất gốc)

**5.1 Không can thiệp sớm.** Nguy cơ là chuỗi: teo cơ do bất động → xơ hóa mô kẽ → mất cân bằng nhóm gập/duỗi → co rút, dính khớp, viêm loét da kẽ ngón; kèm teo rút vùng biểu diễn bàn tay trên vỏ não (maladaptive plasticity). **Bỏ** hai phát biểu "tập luyện vô tác dụng, chỉ còn phẫu thuật" và "mất hoàn toàn phản xạ" — y văn cho thấy bệnh nhân **mạn tính** vẫn cải thiện (`SRC-EMG-SOFT-HAND-2021`: n = 16, 20 phiên, cải thiện ARAT/FMA-UE/BBT). **ĐÃ BỎ** số "40–50% khối lượng cơ" và cụm "giai đoạn vàng 3–6 tháng" theo chỉ thị 2026-09-19 (không có nguồn gốc).

**5.2 Chỉ có thụ động máy kéo (CPM).** Kéo thụ động nhịp nhàng **có** tác dụng ngắn lên trương lực (`SRC-SCIRE-PASSIVE-STRETCH`, bằng chứng mức thấp) — nên **không** được viết là "vô dụng" hay "gây đứt gân". Rủi ro thật sự nằm ở **thiếu kiểm soát mô-men/vận tốc** (`SRC-STRETCH-CTRL-2021`). Cái mà CPM **không** làm được: biến PROM thành AROM, và không cho kỹ thuật viên biết bệnh nhân **tự** làm được bao nhiêu so với tầm thụ động — đúng khoảng trống §4.

## 6. Bảng so sánh (bản đã sửa lỗi định lượng của đề xuất gốc)

| Tiêu chí | Thụ động đơn thuần | Chủ động có trợ lực (AAT) |
|---|---|---|
| Kích hoạt lệnh vận động từ M1 | thấp/không ổn định | **bắt buộc** — là định nghĩa của chế độ |
| Bằng chứng lợi ích bổ sung | nhỏ hơn; meta-analysis: chế độ patient-passive **không** có lợi ích thêm so với chứng (`SRC-RAT-META-2022`) | lớn hơn; passive-active và patient-active có lợi ích (`SRC-RAT-META-2022`, `SRC-ACTIVE-PASSIVE-2025`) |
| Hiệu ứng ỷ lại | cao | **thấp hơn, nhưng chỉ khi** thuật toán theo dõi mức tham gia (`SRC-MPC-AAN-2026`) |
| Kết quả cơ học | duy trì PROM | hướng tới AROM + kỹ năng cầm nắm |
| Rủi ro | thấp nếu có giới hạn mô-men; tăng khi đặt máy quá mạnh | cần giới hạn lực + giám sát; phụ thuộc mức co cứng (co cứng nặng làm giảm hiệu quả — `SRC-EMG-SOFT-HAND-2021`) |
| **Có bằng chứng hơn về CHỨC NĂNG so với điều trị thường quy?** | — | **CHƯA** ở các thiết bị cánh tay có robot: RATULS không thấy khác biệt ARAT ở 3 tháng (`SRC-RATULS-2019`) → đề tài **không** được suy ra "có trợ lực = tốt hơn về chức năng" |

## 7. Giới hạn phải đọc to khi bảo vệ

1. Đề tài **không** phải thiết bị tập, **không** tác động lực lên ngón tay (trừ khi `DEC-SCOPE-002` đổi phạm vi).
2. Không có số liệu lâm sàng: mọi phát biểu về neuroplasticity là **cơ sở chọn chỉ số**, không phải kết quả.
3. Effort Index và RAL **chưa được kiểm chứng**; nếu `GATE A′` fail, mục 4 loại bỏ chỉ số đó và báo cáo ghi rõ đã loại.
4. Không đo góc khớp tuyệt đối; không ADC → N, không ADC → độ (theo `AGENTS.md`).
5. Ý tưởng AAT/AAN **không phải của đề tài** — là nền tảng có sẵn trong y văn, đề tài dùng để **đo**, có trích dẫn ở mục Tài liệu tham khảo.

---

### Tài liệu tham khảo tạm thời của A.7 (mọi dòng chờ đọc toàn văn)

| id ledger | Mượn để nói gì | Mức đã đọc |
|---|---|---|
| `SRC-MPC-AAN-2026` | slacking là thích nghi học được; AAN theo sai số không đủ | `READ_ABSTRACT` |
| `SRC-AAN-EMG-2024` | công thức bù trừ lực + ước lượng nỗ lực bằng EMG | `READ_ABSTRACT` |
| `SRC-IRONHAND-2018` (= Radder, *J Rehabil Assist Technol Eng* **2016**; đã đọc Methods — id giữ nguyên cho khớp ledger) | logic nhận ý định + lực đỡ **tỉ lệ** với lực người dùng | `PARTIAL` |
| `SRC-IRONHAND-JRM-2018` (Radder, *J Rehabil Med* 2018;50:598–606) | khả thi HandinMind n=5, 2 phiên, SUS + IMI + thời gian nhiệm vụ | `READ_ABSTRACT` |
| `SRC-TW-SPASTICITY-2022` (Lin, *Sensors* 2022;22(19):7212) | 19 IMU + 1 bóng áp lực, n=14, tách co cứng khỏi chuyển động tự nguyện — **đối thủ trực tiếp** của mọi câu "tách nỗ lực/co cứng" | `READ_ABSTRACT` |
| `SRC-RAT-META-2022` | meta-analysis theo chế độ tập (passive vs active) | `UNVERIFIED` |
| `SRC-ACTIVE-PASSIVE-2025` | chủ động > thụ động nhưng thụ động ≠ 0 | `READ_ABSTRACT` |
| `SRC-RATULS-2019` | robot không hơn thường quy về chức năng | `UNVERIFIED` |
| `SRC-EMG-SOFT-HAND-2021` | bệnh nhân mạn tính vẫn cải thiện; co cứng nặng là giới hạn | `UNVERIFIED` |
| `SRC-SCIRE-PASSIVE-STRETCH` | bằng chứng mức thấp về kéo thụ động giảm trương lực ngắn hạn | `UNVERIFIED` |
| `SRC-STRETCH-CTRL-2021` | rủi ro nằm ở thiếu kiểm soát mô-men | `UNVERIFIED` |
| `SRC-KAPS-2017` | co cứng định lượng bằng quan hệ tốc độ–lực cản | `READ_ABSTRACT` |
| `SRC-NEOFECT-SMARTGLOVE` | trần thương mại của "cảm biến + phản hồi" | `UNVERIFIED` |
| `SRC-VNM-ANNAM-2022`, `SRC-VNM-REHABTECH-GD-2022`, `SRC-VNM-TL-GLOVE-2026` | prior art trong nước cho hướng có trợ lực | `UNVERIFIED` (báo chí) |
