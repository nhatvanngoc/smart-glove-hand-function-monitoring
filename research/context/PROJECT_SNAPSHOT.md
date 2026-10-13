# Project snapshot — 2026-09-19 (lượt rà soát prior art 1) · nền 2026-09-13 · cập nhật 2026-10-13 (DEC-GATE-002, hai nhánh GATE + tách RL khỏi nhiệm vụ Orange Pi)

> Bản nén ngữ cảnh để phiên sau khôi phục trạng thái **bằng artifact**, không dựa vào trí nhớ hội thoại.
> Chỉ chứa **sự kiện bền vững**. Quyết định đầy đủ: `DECISION_LOG.md`. Đề tài: `docs/01_Topic_Definition.md`.

> **2026-10-13 (`DEC-GATE-002`):** hệ GATE tái cấu trúc thành **hai nhánh song song, mỗi nhánh một cổng sống còn ⭐** — Đo (GATE 0→A→B→C⭐, không đổi) và Trợ lực-AAN (GATE AAN-1→AAN-2⭐→AAN-3, mới). **GATE F (INT8/NPU) tạm hoãn**, thay bằng "GATE EDGE — đang chọn" (ứng viên ưu tiên: camera+ArUco nâng thành kênh tự kiểm tra 2 chiều độc lập cho GATE E). Thuật toán multi-armed bandit để rút ngắn số lượt thử dò RAL (GATE AAN-2) **đã tách hẳn khỏi câu chuyện Orange Pi 5 Pro** — đây là một quyết định về phương pháp thí nghiệm, không phải nhiệm vụ phần cứng; không cần NPU, không cần gắn với bất kỳ thiết bị cụ thể nào. Chi tiết: `research/protocols/06_glove_hand_GATE_experiment.md` §0/§4; `research/protocols/07_ral_phantom_and_ktv_interview.md` §2-3b. Tất cả ngưỡng số của nhánh AAN và của GATE EDGE **CHƯA CHỐT** (`DEC-METRIC-001`).

---


## 1. Đề tài (CHỐT nội dung — DEC-TOPIC-019; CHỐT tên hiển thị — DEC-TITLE-003, 2026-10-11)

> ⚠️ **2026-09-27:** README ngày 2026-09-19 ghi "tên chốt `DEC-TITLE-001`" nhưng quyết định này **không có trong `DECISION_LOG.md`**
> và file `2026-09-19_title_options.md` không tồn tại. **Bản đã nộp `docs/DE_CUONG.pdf` (§1.1) dùng tên cũ** → repo quay về tên cũ,
> chờ `DEC-TITLE-002` (hủy `DEC-TITLE-001`).
>
> **Đội hình đã nộp (PDF §1, chờ `DEC-TEAM-001`):** Văn Ngọc Nhật Anh (11A2) + Nguyễn Duy Quân (12A1), THPT Quảng Trị;
> GVHD **Lê Công Long**; lĩnh vực **Hệ thống nhúng**; timeline **09/2026–01/2027**; địa điểm phòng sáng tạo trường + nhà riêng.

> **2026-10-11 (`DEC-TITLE-003`):** tên hiển thị đổi để nêu bật AAN là trụ cột thứ 4 (`DEC-SCOPE-006`). Hồ sơ đã nộp (`docs/DE_CUONG.pdf` 26/09, `de_cuong/DE_CUONG_NGHIEN_CUU.pdf` 03/10) vẫn dùng tên cũ `DEC-TOPIC-019` cho tới khi nộp lại.

**Tiếng Việt (hiển thị hiện hành, từ `DEC-TITLE-003`):**

> **Nghiên cứu và phát triển găng tay hỗ trợ đánh giá, theo dõi và hỗ trợ vận động bàn tay trong phục hồi chức năng sau đột quỵ**

**Tiếng Việt (tên đã nộp, `DEC-TOPIC-019`, không đổi hồi tố):**

> Nghiên cứu và phát triển găng tay thông minh hỗ trợ đánh giá và theo dõi chức năng vận động bàn tay trong phục hồi chức năng sau đột quỵ

**Tiếng Anh (cập nhật theo `DEC-TITLE-003`):**

> A glove with directional piezoresistive sensing for quantitative hand motor-function assessment, longitudinal monitoring, and assist-as-needed movement support (bench/phantom-verified) in post-stroke rehabilitation.

**"Viên đạn" — 1 câu:**

> Theo dõi định lượng chức năng bàn tay **tại nhà**, liên tục **giữa các lần tái khám lâm sàng**.

**Loại sản phẩm:** thiết bị **đánh giá & theo dõi**. **KHÔNG** phải robot/găng tập phục hồi chức năng. **KHÔNG** chẩn đoán, **KHÔNG** thay thế đánh giá lâm sàng.

> **CẬP NHẬT 2026-10-11 (`DEC-SCOPE-006`, `DEC-SYNC-002`):** phát hiện bản đề cương mới hơn chưa đồng bộ — `de_cuong/DE_CUONG_NGHIEN_CUU.pdf` (16tr, tạo 2026-10-03) vs bản đã nộp trường `docs/DE_CUONG.pdf` (15tr, 2026-09-26). Bản mới bổ sung Mục 10: cơ cấu **AAN (Assist-as-Needed)** nay là **trụ cột kỹ thuật chính thức thứ 4** của đề tài (chủ dự án nêu minh thị). AAN chỉ chạy trên **giàn đo + mô hình tay giả phantom**, tuyệt đối không tác động lực lên người thật — ranh giới `DEC-SCOPE-003` không đổi. Đồng thời ghi nhận (`DEC-PHASE-002`): chủ dự án đã **tự thực hiện** bring-up phần cứng thật (ESP32-S3+ADS1115+INA333+CD74HC4067, log `research/notebooklm_sync/experiments/`), nhưng **chưa chính thức hoá** thành log GATE 0 hợp lệ. Tên đề tài **chưa đổi** (`DEC-TITLE-003` đề xuất 4 phương án, chờ chọn).

---

## 2. Vấn đề & khoảng trống

- Sau đột quỵ, phục hồi bàn tay phụ thuộc luyện tập chủ động tại nhà; kỹ thuật viên chỉ gặp bệnh nhân mỗi **1–3 tháng**.
- Khoảng giữa hai lần tái khám là **"hộp đen"** (nguyên văn KTVVLTL-PHCN): không biết tập đúng không, đủ không, có tiến triển không.
- Tập sai/không duy trì trong thời gian dài → co cứng, đau, chững lại; nặng hơn: biến dạng khớp, co rút, chèn ép thần kinh ngoại vi.
- Công cụ hiện tại (FMA, ARAT, Box and Block, Jamar, E-Link) = **ảnh chụp tại một thời điểm**, tại cơ sở y tế, chi phí cao.

## 3. Bằng chứng xác nhận khoảng trống

| Nguồn | Vai trò |
|---|---|
| Amin K.R. et al., *Remote Monitoring for the Management of Spasticity*, IEEE OJEMB (2024), DOI 10.1109/OJEMB.2024.3523442 | Hội đồng chuyên gia: công cụ đánh giá hiện tại chỉ dùng được ở phòng khám; theo dõi định lượng giữa các lần tái khám "có ý nghĩa thay đổi cuộc sống và tiết kiệm chi phí"; là bài toán chung của nhiều lĩnh vực PHCN. **Lưu ý:** đối tượng là *spasticity* → chỉ dùng để chứng minh khoảng trống chung |
| OTHER study (2026), DOI 10.1080/09638288.2026.2643929, PMID 41918405 | Theo dõi hoạt động tại nhà + coaching từ xa cải thiện chức năng sinh hoạt và tự quản lý sau đột quỵ |
| DEC-CLINICAL-001 (phỏng vấn KTVVLTL-PHCN, 2026-08-28) | Xác nhận pain point: ảnh chụp rời rạc; "hộp đen"; thiết bị tại nhà chỉ hữu ích nếu chỉ số có ý nghĩa lâm sàng + đủ tin cậy + đơn giản + **bổ sung chứ không thay thế** |
| DEC-CLINICAL-002 (chuyên gia PHCN tại phcn-online.com) | Xác nhận độc lập thứ hai: đề tài đáng nghiên cứu |
| Phỏng vấn KTV phần 2 (2026-09-13) | KTV nêu rõ: giải pháp cần là **đánh giá**, không phải phục hồi chức năng trực tiếp; và lưu ý mức độ khó của bài tập (thụ động dễ → cầm nắm/bấm/xoay cổ tay khó, không đảm bảo an toàn nếu làm tự động) |

## 4. Novelty (trung thực — mức ViSEF)

> ⚠️ **CẬP NHẬT 2026-09-19 — lượt rà soát prior art 1** (`research/reviews/2026-09-19_prior_art_novelty_gate1.md`). Mức novelty bên dưới đã **dịch chuyển**: A bị hạ một bậc, C được nâng lên trọng tâm. **Chưa chốt** — chờ `DEC-NOV-001` + lane R5.

- **KHÔNG** claim "găng tay + AI/TinyML" là mới; **KHÔNG** claim "đo lực bóp" là mới; **KHÔNG** claim "không dùng IMU" là mới (đã có găng grating/optic 2021, stretch 2024).
- ~~Ứng viên chính: cảm biến hướng qua vách khung cứng~~ → **sau lượt rà soát 1: chỉ còn là "cải tiến cấu hình + phương pháp lập luận"**, vì:
  - `SRC-SIDEWALL-PIEZO-2015` (Sensors 15(10), DOI 10.3390/s151025463): **1 lõi + 4 vách elastomer**, phần tử CNT/PDMS khóa liên động, phân biệt pháp tuyến + shear 4 hướng **không cần xử lý tín hiệu phức tạp** → nguyên lý "vách mã hóa hướng" có từ 2015.
  - `SRC-ARTGLOVE-2026` (arXiv:2606.16370): **găng vỏ cứng khớp nối, 16 bề mặt chức năng, da áp điện trở 2048 taxel @120 Hz** — nhưng 22 DoF đo bằng **encoder**.
  - `SRC-CN116954366A-ARRAYGLOVE`: bằng sáng chế găng 20 phần tử áp điện trở tại 14 khớp ngón + lòng bàn.
- **Ứng viên chính mới (đề xuất): C** = chỉ số chức năng bàn tay từ lực hướng, kèm **khung MDC/ICC** và **cờ từ chối kết luận**, dùng tại nhà giữa hai lần tái khám. Giao điểm này **chưa thấy ai làm đủ**, nhưng **cấm** nói "hệ thống đầu tiên theo dõi tại nhà": đã có `SRC-LOWCOST-GLOVE-2006` (găng extended monitoring + functional hand assessment, 2006) và `SRC-MULTITOUCH-APP-2021` (app tablet n=88, có SEM/MDC, hội tụ FMA-UE/JTT/BBT/NHPT).
- **KHÔNG mới (phải trích dẫn prior art):** đọc vi sai/ô tham chiếu để bù drift (thêm bằng chứng `SRC-OPENPAD-FINGER-2020`: 2 phần tử hai bên đốt ngón để tách thành phần lực, từ 2020); INT8 quantization.
- **Prior art đã xác minh danh tính 2026-09-19:** `SRC-ZHU-2017-GLOVE` = Liu H. et al., IROS 2017, tr. 6617–6624, DOI 10.1109/IROS.2017.8206575 (đúng như mô tả cũ; bổ sung: hướng vector lực **gán theo pose từ IMU**, không suy từ vách). `SRC-RECONFIG-GLOVE-2023` = Liu H. et al., **Engineering** 2024;32(1):217-232, DOI 10.1016/j.eng.2023.01.009 — **sửa**: không phải "Science China". `SRC-SMARTGLOVE-REVIEW-2026` = Mohammed A., Ali A.M., *J. Eng. Appl. Sci.* 73:246 (2026), DOI 10.1186/s44147-026-01084-6 (101 bài 2011–2025; 72% fusion flex+IMU).
- **Rủi ro trùng trong nước (mức học sinh):** `SRC-VNM-HS-GLove-2026` — học sinh Lâm Đồng làm "găng tay thông minh tích hợp AI" có **cảm biến lực + áp suất khí**, theo dõi tiến độ phục hồi, **giải nhất cấp tỉnh 2026**; `SRC-VNM-ANNAM-2022` (găng mềm PneuNet, giải Nhất EPICS 2022); `SRC-VNM-TL-GLOVE-2026` (găng robot + theo dõi từ xa). **Toàn bộ đều là máy tập/hỗ trợ chủ động**, không phải thiết bị đánh giá có kiểm chứng độ tin cậy → phải nêu trong mục "bất cập của giải pháp hiện tại".
- **Gap 1 chưa hoàn tất.** Còn: (i) đọc **toàn văn** 5 nguồn (`SRC-ARTGLOVE-2026`, `SRC-SIDEWALL-PIEZO-2015`, `SRC-GRATING-GLOVE-2021`, `SRC-LOWCOST-GLOVE-2006`, `SRC-MANUMETER-RCT-2022`); (ii) tra bằng sáng chế theo IPC A61B5/11 · A61B5/22 · A61B5/10 · G01L1/14 · A61H1/02 (lượt vừa rồi mới 1 truy vấn web, **không đủ** để kết luận); (iii) lane R5 adjudicate; (iv) `DEC-NOV-001` do owner chốt.

## 5. Phần cứng (CHỐT — DEC-HW-002/003/004)

```
Sensing element : Velostat + copper tape + cấu trúc sandwich + lớp cơ khí (tự chế tạo)
Khung           : găng in 3D (PLA/PETG + TPU), vách ép tạo hướng
Cấu hình 1      : 12 kênh (11 đo + 1 tham chiếu) — 1× CD74HC4067 — bring-up, GATE 0/A
Cấu hình 2      : 24 kênh, mỗi khớp 1 CẶP đối xứng → đọc vi sai — 2× CD74HC4067 — GATE A/B/C/D/E
MCU             : ESP32-S3 (ADC1 12-bit + trung bình N mẫu, BLE 5, logic 3.3 V)
                  [thay Arduino Mega 2560 — DEC-HW-003]
Edge            : Orange Pi 5 Pro RK3588 (NPU ~6 TOPS) — nhiệm vụ cụ thể CHƯA CHỐT (DEC-GATE-002,
                  GATE EDGE); ứng viên ưu tiên = camera+ArUco làm kênh tự kiểm tra 2 chiều cho GATE E
Tham chiếu bench: load cell + HX711  (GATE A trở đi; GATE 0 dùng **khối lượng chuẩn**, F = m·g)
Sở hữu   (2026-09-19, DEC-RESOURCE-001): Velostat + copper tape + ESP32-S3 + Orange Pi 5 Pro = ĐÃ CÓ;
           còn thiếu cho GATE 0: CD74HC4067?, DMM 4 dây?, khối lượng chuẩn, in 3D  → kiểm kê: research/context/EQUIPMENT_AND_ACCESS.md
```

Ngân sách độ phân giải/tốc độ khung (dự kiến, **phải đo lại**): ~11 bit hiệu dụng sau trung bình 16 mẫu; tốc độ khung mục tiêu 45–100 Hz; đủ cho động tác 0,5–2 Hz. Chi tiết: `docs/04_Hardware_Architecture.md`.

## 6. GATE — tiêu chí sống còn (tái cấu trúc 2026-10-13, `DEC-GATE-002`)

`research/protocols/06_glove_hand_GATE_experiment.md` + `07_ral_phantom_and_ktv_interview.md`. Hai nhánh song song:

**Nhánh Đo (không đổi):**
- **GATE 0** lặp lại (CV ≤ 5% trong phiên, ICC ≥ 0,75 giữa phiên)
- **GATE A** phân biệt hướng (4 hướng ≥ 85%; cặp đối lập ≥ 90%)
- **GATE B** tái tạo 3D (MAE ≤ 15°, r ≥ 0,8)
- **GATE C ⭐ SỐNG CÒN** Δ giữa các mức chức năng ≥ 2σ_noise; Cohen's d ≥ 0,8; MDC < mức chênh liền kề — **fail ⇒ dừng cả đề tài**

**Nhánh Trợ lực - AAN (mới, ngang hàng, ngưỡng CHƯA CHỐT):**
- **GATE AAN-1** (đổi tên từ "GATE A′") — phát hiện nỗ lực trước khi ngón di chuyển (AUC≥0,85/báo nhầm≤10%/trễ≤300ms, ĐỀ XUẤT)
- **GATE AAN-2 ⭐** (đổi tên + nâng cấp từ "GATE RAL") — cổng sống còn của nhánh AAN: đường cong tải-hoàn thành ổn định (ICC≥0,75) **+** participation ratio không xói mòn về 0 (chống ỷ lại) — **fail ⇒ không dừng đề tài, chỉ hạ nhãn AAN xuống "trợ lực cố định phân bậc"**
- **GATE AAN-3** (mới) — chính thức hoá an toàn chấp hành lực: `F_assist` đúng công thức trong `F_max≤5N`/`t_delay≤1,2s`, fail-safe khi lỗi cảm biến (liên kết GATE E)

**Dùng chung:** GATE D (không báo động giả, ≤10%/≥10 ngày), GATE E (tự phát hiện lỗi ≥90%/báo nhầm≤5%).

**GATE F (INT8/NPU) TẠM HOÃN** → thay bằng **"GATE EDGE — đang chọn"**: ứng viên ưu tiên cao nhất là nâng camera+ArUco (đã test OK) thành kênh tự kiểm tra 2 chiều độc lập chạy liên tục cho GATE E; ứng viên phụ là INT8 phân loại hướng gốc. Thuật toán bandit rút ngắn lượt thử dò RAL (cho GATE AAN-2) **đã tách khỏi quyết định này** — là phương pháp thí nghiệm độc lập với phần cứng, không cần NPU.

**Ngưỡng phải chốt trước khi đo (DEC-METRIC-001).** GATE C fail ⇒ dừng đề tài, báo cáo trung thực.

> ⚠️ **2026-09-27 — ngưỡng ĐÃ NỘP là M1–M6 + C1.1–C1.10** (PDF §5.2/§11.1, `CLM-MET-005`, chờ `DEC-METRIC-002` phê chuẩn):
> R² ≥ 0,90 (thay 0,95) · liên ngày CV ≤ 8 % trên phantom (thay ICC ≥ 0,75) · hys ≤ 18 % (thay 15 %) ·
> creep ≤ 8 % giữ 60 s@5 N (thay creep_2dec ≤ 3 %) · trôi/tín hiệu ≤ 2,0/10 ngày qua auto-zero (bỏ điều kiện ΔV@1N) ·
> M6 = phát hiện đeo lỏng ≥ 80 % qua V_base (thay fault-injection ≥ 4/5).
> Định nghĩa đã nộp (`CLM-DEF-001`): **GAP = PROM − AROM** (độ, theo giao thức) · **RAL** = nấc tải (g) nhỏ nhất đạt P_complete ≥ 80 % ·
> **EI** = trung vị biến thiên phổ vi sai chuẩn hóa vận tốc góc (công thức tường minh còn nợ).
> Bảng đối chiếu: sync review §4. `protocols/08` §7 giữ 10 ô chờ chốt — agent không tự chốt.

## 7. Ngôn ngữ bắt buộc (DEC-MSG-001)

| Dùng | Không dùng |
|---|---|
| suy luận hướng gập/duỗi | đo góc khớp |
| giảm ảnh hưởng drift | loại bỏ drift / drift-free |
| găng tay đánh giá và theo dõi | robot/găng tập phục hồi chức năng |
| sensing element chế tạo từ vật liệu Velostat | cảm biến Velostat |
| bổ sung cho đánh giá lâm sàng | thay thế Fugl-Meyer/ARAT |

## 8. Tuyên bố bị cấm

- ❌ Chẩn đoán đột quỵ / mức độ liệt / tiên lượng
- ❌ Thay thế FMA / ARAT / Box and Block / đánh giá của chuyên gia
- ❌ "Đo chính xác lực tuyệt đối" / "đo góc khớp"
- ❌ "Đã kiểm chứng lâm sàng" / "chứng minh hiệu quả"
- ❌ Thử trên người tham gia (kể cả người khỏe) trước khi có IRB/SRC (`DEC-ETHICS-001` vẫn OPEN; bản nộp §7.2/§12 giới hạn ở **tự thử trên chính người thực hiện, chế độ đo, không tác động lực, tự nguyện + quy tắc dừng** — không mở rộng sang người khác/bệnh nhân)
- ❌ Điền số `[X]` vào A.3 hoặc mục C khi chưa có log đo thật

## 9. Việc tiếp theo (theo thứ tự)

-2. ✅ **ĐÃ LÀM 2026-10-13 (phiên này, `DEC-GATE-002`):** tái cấu trúc hệ GATE thành 2 nhánh song
   song (Đo: 0→A→B→C⭐ không đổi; Trợ lực-AAN: AAN-1→AAN-2⭐→AAN-3 mới) trong `06_glove_hand_GATE_
   experiment.md` + `07_ral_phantom_and_ktv_interview.md`; tạm hoãn GATE F (INT8/NPU), thay bằng
   "GATE EDGE — đang chọn" với 2 ứng viên (camera+ArUco 2 kênh ưu tiên cao nhất / INT8 phân loại
   hướng phụ); tách thuật toán multi-armed bandit rút ngắn lượt thử dò RAL ra khỏi câu chuyện Orange
   Pi — nay là M9, một đóng góp phương pháp độc lập cho GATE AAN-2, không gắn phần cứng cụ thể. Đã
   cập nhật `docs/DE_CUONG_NOP_BAN_KHKT_2026-10-18.md` (bảng M1–M9, sơ đồ khối, kế hoạch thời gian),
   `DECISION_LOG.md` (+`DEC-GATE-002`), file này (§5/§6). Đã xuất lại .docx/.pdf và re-upload Drive
   (`tai_lieu_KHKT_2027`): docx id mới `1Zs-nSopzDPQ9mz-iqL006H55wJehP3Oz`, pdf id mới
   `1-nQsGN-5u2ruOhYnT8lLLiYcvzunBGiC` — 2 bản cũ (docx `1gBNoJJSPfkl8W5Sj5n7m2SnKMKZcs9pa`, pdf
   `1E3hhbf_QstPE9kIHQJ18zNGbfRB2DBda`, và một cặp trung gian tạo rồi trash cùng phiên) **đã bị
   trash**, không còn là bản hiện hành.
   ☐ **CHỜ OWNER — CHƯA XONG, liệt kê đủ để không lặp lại/quên ở phiên sau:**
   1. `docs/DE_CUONG_NOP_BAN_KHKT_2026-10-18.md` vẫn tự ghi trạng thái **"DỰ THẢO — chưa chốt, chờ
      chủ dự án duyệt trước khi nộp"** — owner **chưa xác nhận lần cuối** để nộp thật (hạn 17h
      18/10/2026, còn ít ngày tính từ lúc soạn). Cũng chưa có xác nhận link nộp chính thức từ Ban
      KHKT (chỉ mới có ảnh chụp thông báo).
   2. Ngưỡng số của nhánh AAN hoàn toàn **CHƯA CHỐT**: GATE AAN-2 (participation ratio không được
      giảm quá X% trong ≥Y% số phiên — X,Y để trống) và GATE AAN-3 (dung sai thực tế quanh
      `F_max≤5N`/`t_delay≤1,2s`, tiêu chí fail-safe cụ thể) đều đang chờ owner — agent cố ý không tự
      điền theo `DEC-METRIC-001`.
   3. **GATE EDGE (nhiệm vụ Orange Pi 5 Pro) chưa chốt ứng viên cuối cùng** — mới dừng ở mức phân
      tích + khuyến nghị (ưu tiên camera+ArUco). Khi chốt, phải viết lại §4 của `06_...` thành tiêu
      chí PASS/FAIL thật, không còn là "đang chọn".
   4. **M9 (bandit cho GATE AAN-2) mới là PROPOSED**, chưa có quyết định owner có nhận hướng này
      không; nếu nhận, còn phải thiết kế phép so sánh công bằng (bandit vs quét cố định) và chốt
      ngưỡng % cải thiện tối thiểu trước khi chạy — chưa làm.
   5. **Nợ đồng bộ xuyên repo (phát hiện khi rà soát, chưa sửa):** nhiều file khác vẫn còn nhắc tên
      GATE cũ, không phải lỗi số liệu — chỉ là tên gọi/cấu trúc GATE chưa theo kịp `DEC-GATE-002`:
      - còn nhắc **"GATE F"** kiểu cũ (coi là cổng cam kết cứng, không phải "GATE EDGE — đang chọn"):
        `AGENTS.md`, `README.md`, `docs/01_Topic_Definition.md`.
      - còn nhắc tên cũ **"GATE A′"/"GATE RAL"** (chưa đổi thành AAN-1/AAN-2): `INDEX.md`,
        `docs/02_Theoretical_Foundation.md`, `docs/bao_cao/A7_AAT_rationale_DRAFT.md`.
      - `docs/05_De_Cuong_Dang_Ky_DRAFT.md` cũng còn "GATE F" kiểu cũ.
      - **KHÔNG được sửa** (đã nộp/đóng băng theo quy ước không hồi tố — `DEC-TITLE-003` tiền lệ):
        `docs/DE_CUONG_NOP_TRUONG.md` (đã nộp trường 2026-09-26), `docs/DE_CUONG_NGAN_5-7_TRANG_
        DRAFT.md`, `research/reviews/2026-09-19_active_assisted_scope_options.md` (review lịch sử,
        giữ nguyên làm hồ sơ).
      - Việc nên làm ở phiên tới: một lượt quét-sửa có chủ đích các file **được phép sửa** ở trên để
        tên GATE nhất quán toàn repo, tránh người đọc lẫn giữa bản cũ/mới.
   6. Vẫn **chưa có bất kỳ dữ liệu bench thật nào** cho nhánh AAN hay cho GATE EDGE — hai mảng này
      toàn bộ còn ở giai đoạn giao thức/lý thuyết; nhánh Đo (GATE 0/A/B) là mảng duy nhất có khả
      năng ra số liệu thật trước cuối 11/2026 (xem §9 phần `-1.` bên dưới về GATE C cần ≥28 ngày).

-1. ✅ **ĐÃ LÀM 2026-10-13 (`DEC-PROP-003`):** Ban KHKT ra thông báo chính thức khuôn đề cương nộp
   vòng trường (6 mục: Tên dự án/Lý do/Mục tiêu/Ý tưởng-nội dung/Sản phẩm dự kiến/Tính khả thi),
   **hạn nộp 17h 18/10/2026**, nộp Word/PDF qua link sẽ có ở nhóm Zalo CLB KHKT. Đã soạn
   `docs/DE_CUONG_NOP_BAN_KHKT_2026-10-18.md` theo đúng khuôn này (tái dùng nội dung từ
   `docs/DE_CUONG_NGAN_5-7_TRANG_DRAFT.md`/`docs/DE_CUONG_NOP_TRUONG.md`). Phát hiện khi soạn mục
   Tính khả thi: theo `protocols/08` thì GATE 0 (~3 tuần) + GATE C (≥28 ngày trôi) khiến đề tài
   **không thể xong toàn bộ GATE 0→F trước cuối tháng 11/2026** — đã viết trung thực hướng này
   thay vì hứa hẹn, nhưng **chưa qua owner duyệt cách đóng khung**.
   ☐ **CHỜ OWNER (gấp, hạn 18/10):** duyệt nội dung + cách đóng khung "Tính khả thi";
   điền 3 ô danh tính; xác nhận link nộp khi Ban KHKT công bố; xuất file sang .docx/.pdf để nộp.
0. ✅ **ĐÃ LÀM 2026-10-11:** đọc toàn bộ repo + xác nhận setup môi trường (venv/pip/bootstrap/check --strict 10/11/context bundle); đọc toàn văn `research/notebooklm_sync/` (10 file: README, 5 experiment log, 1 chat transcript 402 dòng, 3 file studio) và phát hiện bản đề cương chưa đồng bộ `de_cuong/DE_CUONG_NGHIEN_CUU.pdf` (2026-10-03, 16tr). Theo chỉ đạo minh thị của chủ dự án: `DEC-SYNC-002` (công nhận bản mới) + `DEC-SCOPE-006` (AAN = trụ cột thứ 4, ranh giới an toàn không đổi) + `DEC-PHASE-002` (ghi nhận bring-up phần cứng thật do chủ dự án tự làm, chưa chính thức hoá GATE 0) + `DEC-TITLE-003` (4 phương án tên, PROPOSED). Cập nhật README §1/§6.1/§8/§10/§11, AGENTS.md §2, +6 nguồn/+3 claim/+5 quyết định.
   ☐ **CHỜ OWNER:** chọn phương án tên (`DEC-TITLE-003`); xác nhận `de_cuong/DE_CUONG_NGHIEN_CUU.pdf` có phải bản sẽ nộp lại; chính thức hoá log bring-up thành GATE 0 hợp lệ; xác nhận đổi tên cảm biến SHT30→AHT20.
0. ✅ **ĐÃ LÀM 2026-09-27:** đồng bộ bản nộp `docs/DE_CUONG.pdf` (2026-09-26) → `research/reviews/2026-09-27_decuong_pdf_sync.md`;
   môi trường cài lại (venv + skills OK, 10/11 check); +7 nguồn ledger (147), +3 claim (27), +2 truy vấn xác minh [15]/[18] (81, đều `UNVERIFIED`);
   sửa README (tên/đội hình/ngưỡng), `docs/04` §8 + `docs/02` §11 mới, điền danh tính `DE_CUONG_NOP_TRUONG.md`.
   ☐ **CHỜ OWNER:** 6 quyết định `DEC-SYNC-001`/`DEC-TEAM-001`/`DEC-TITLE-002`/`DEC-HW-005`/`DEC-METRIC-002`/`DEC-SCOPE-005` + duyệt 7 nguồn/3 claim mới.
0. ✅ **ĐÃ LÀM 2026-09-19:** lượt rà soát prior art 1 → `research/reviews/2026-09-19_prior_art_novelty_gate1.md`; 24 nguồn vào ledger (20 `READ_ABSTRACT`, 4 `UNVERIFIED` — chưa đọc toàn văn); 3 claim cập nhật + 2 claim mới; GATE A/C có thêm mốc so sánh y văn. ☐ **CÒN NỢ:** đọc toàn văn 5 nguồn, tra IPC bằng sáng chế, `DEC-NOV-001`.
0.5 ☐ **NGANG HÀNG QUAN TRỌNG (mới 2026-09-19):** chủ dự án chốt `DEC-SCOPE-002` cho đề xuất "tập chủ động có trợ lực" — E1 (chỉ lý thuyết) / E2-lite (chỉ số Effort+gap AROM−PROM+RAL, không động cơ, **khuyến nghị**) / E3 (động cơ + Bowden, 8–15 tuần, đổi trục + rủi ro an toàn + IRB). **CẬP NHẬT: sau phản hồi của chủ dự án về chuẩn ViSEF, khuyến nghị mới là E4+E5+E6 (rig phantom + RAL + 1 servo kéo phantom + tầng kê đơn), **đã xác minh chuẩn tham chiếu ISEF 2025 ROBO065T (THPT thị xã Quảng Trị, giải Tư, thuần tích hợp + 4 số tự đo)** -> xem `DEC-SCOPE-002b/c` và `research/protocols/07_ral_phantom_and_ktv_interview.md`. **Chưa chốt → không bắt tay vào cơ khí chấp hành, không đổi docs/01 §1, không đổi A.4.**
1. ☐ **GIAI ĐOẠN HIỆN TẠI (chỉ thị 2026-09-19): CƠ SỞ LÝ THUYẾT.** Đã xong 2 việc chủ dự án yêu cầu: (1) **mô hình chuỗi đo** → `docs/02` §5.5 (dự toán đơn bậc độ lớn: `F_p ≤ 68·γ·ΔF`, cửa sổ làm việc 2 đầu, yêu cầu rig có ≥2 tốc độ kéo); (4) **đối chiếu toàn văn/danh tính** → sửa 3 lỗi nguồn (Engineering 32:202–216; ironHand = J Rehabil Assist Technol Eng **2016**; US20150233779A1 = Abandoned + CPC) và **phát hiện đối thủ mới** `SRC-TW-SPASTICITY-2022`. Tra cứu bằng sáng chế theo phân loại: **bất khả thi trong môi trường này** — phương pháp + lối thoát ghi ở `docs/03` §7. Hồ sơ nộp: đã soạn `docs/05_De_Cuong_Dang_Ky_DRAFT.md` + đánh giá trần đề tài `research/reviews/2026-09-19_project_ceiling.md` (chủ dự án điền tên/GVHD/timeline, duyệt DEC-SCOPE-004).  Đã viết vào `docs/02` §1.4–§1.6 (ba chế độ tập, Hebbian có điều kiện, learned non-use + bẫy slacking), §3.4 (co cứng theo quan hệ tốc độ–lực cản), §5.4 (điều kiện đo nỗ lực khi chưa cử động), §7.3 (định nghĩa Effort Index / Gap AROM−PROM / RAL + bảng cấm quy đổi đơn vị), §8.3 (tầng đo được vs tầng suy ra lâm sàng). **Chưa làm:** chốt ngưỡng GATE A′/RAL + 9 ngưỡng GATE 0 (`protocols/08` §7), viết script thống kê, chế tạo jig/phantom. Chủ dự án cho biết **thời gian đủ** (`DEC-PLAN-001`). Chủ dự án khai báo đã có thiết bị + KTV 10 năm phản biện (`DEC-RESOURCE-001`) ⇒ **Lớp 0–1 giải ngân được về tiền**; blocker duy nhất còn lại là 9 ngưỡng `protocols/08` §7. **2026-09-19 (11):** bản **nộp được** đã ra đời: `docs/DE_CUONG_NOP_TRUONG.md` (`DEC-PROP-001`); `docs/05` → outline nội bộ. Số liệu dịch tễ đã kiểm (`CLM-BIO-003/-004`); phát hiện A.1 gán con số 80% cho Hendricks 2002 trong khi nguồn đã kiểm là Cochrane 2014 — **chủ dự án sửa A.1** (nay là **10** ô: thêm `G0.0` chọn định nghĩa nhiễu). Chủ dự án chốt: **giữ pha lý thuyết** — không firmware/không script (`DEC-PHASE-001`) → đã phát hành phiếu đo in được `protocols/08a`; và **không nêu danh tính người tham khảo** trong hồ sơ (`DEC-ROLE-001`). Kiểm kê + việc tuần này: `research/context/EQUIPMENT_AND_ACCESS.md`. Benchmark hình thức từ báo cáo QG 2024–2025 (15 tr., 17 hình/3 bảng, 0 thống kê) → `2026-09-19_benchmark_xe_lan_ALS_QG2025.md` → kế hoạch giữ đủ 7 cổng; `protocols/08` đã sẵn sàng chạy ngay khi §7 được chốt.
1. ☐ Chốt cấu hình kênh 1 → 2 (hay làm thẳng cấu hình 2).
2. ☐ Chốt giao thức bài tập chuẩn cùng KTVVLTL-PHCN.
3. ☐ Rà soát prior art **nửa còn lại** theo `docs/03` → chốt mức novelty qua `DEC-NOV-001`.
4. ☐ Chế tạo sensing element → đo `R_sensor`/tải → chọn `R_f`.
5. ☐ Chạy GATE 0 → GATE A/B → **GATE C** → GATE D/E/F.
6. ☐ Điền số thật vào A.3 + mục C của outline.
7. ☐ Chủ dự án đổi tên repo (DEC-REPO-001) và (nếu cần) đổi tên thư mục cục bộ.

## 10. Lịch sử pivot (giữ để không lặp lại sai lầm)

| Đề tài | Số phận | Lý do |
|---|---|---|
| Đệm khí thích ứng + AAC | Bỏ (2026-08-25) | Đã có sản phẩm thương mại; validate khó |
| Smart insole 3D-GRF/COP + knee OA | Bỏ | Prior art dày; cần force plate (không có) |
| Lót giày theo dõi độ cứng mô gan chân (DFU) | Bỏ (2026-08-28) | **GATE 3 (Usefulness) yếu** — stiffness proxy chưa có bằng chứng longitudinal đủ mạnh |
| Loét tì đè | Bỏ | Prior art dày hơn DFU |
| CPR trên bề mặt mềm | Bỏ | Đã được giải quyết bằng 2 accelerometer (PMC5143701) |
| Đánh giá spasticity | Bỏ | Trùng chức năng phụ của đề tài exoskeleton Quảng Trị (giải nhì quốc gia) |
| **Găng tay theo dõi chức năng bàn tay** | **ĐANG LÀM** | Khoảng trống được xác nhận bởi hội đồng chuyên gia 2024 + KTV trong nghề; chưa có đề tài trong tỉnh đụng vào **tay** sau đột quỵ (đề tài exoskeleton Quảng Trị làm **chân**) |

## 11. Điều kiện để đề tài bị coi là thất bại (phải nói thẳng nếu xảy ra)

- GATE C không đạt: chỉ số không đủ nhạy để phân biệt thay đổi chức năng mô phỏng.
- GATE A không đạt: không suy luận được hướng → mất phần "tính mới" chính, chỉ còn là găng đo lực đơn thuần (prior art dày).
- Rà soát prior art tìm ra công bố/sáng chế đã làm đúng cơ chế này.
