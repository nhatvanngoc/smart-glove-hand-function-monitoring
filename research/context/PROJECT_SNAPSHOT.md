# Project snapshot — 2026-09-19 (lượt rà soát prior art 1) · nền 2026-09-13

> Bản nén ngữ cảnh để phiên sau khôi phục trạng thái **bằng artifact**, không dựa vào trí nhớ hội thoại.
> Chỉ chứa **sự kiện bền vững**. Quyết định đầy đủ: `DECISION_LOG.md`. Đề tài: `docs/01_Topic_Definition.md`.

---

## 1. Đề tài (CHỐT — DEC-TOPIC-019)

**Tiếng Việt:**

> **Nghiên cứu và phát triển găng tay thông minh hỗ trợ đánh giá và theo dõi chức năng vận động bàn tay trong phục hồi chức năng sau đột quỵ**

**Tiếng Anh:**

> A low-cost smart glove with directional piezoresistive sensing for quantitative hand motor-function assessment and longitudinal monitoring in post-stroke rehabilitation.

**"Viên đạn" — 1 câu:**

> Theo dõi định lượng chức năng bàn tay **tại nhà**, liên tục **giữa các lần tái khám lâm sàng**.

**Loại sản phẩm:** thiết bị **đánh giá & theo dõi**. **KHÔNG** phải robot/găng tập phục hồi chức năng. **KHÔNG** chẩn đoán, **KHÔNG** thay thế đánh giá lâm sàng.

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
Edge            : Orange Pi 5 Pro RK3588 (NPU ~6 TOPS), mô hình INT8 (RKNN)
Tham chiếu bench: load cell + HX711  (GATE A trở đi; GATE 0 dùng **khối lượng chuẩn**, F = m·g)
Sở hữu   (2026-09-19, DEC-RESOURCE-001): Velostat + copper tape + ESP32-S3 + Orange Pi 5 Pro = ĐÃ CÓ;
           còn thiếu cho GATE 0: CD74HC4067?, DMM 4 dây?, khối lượng chuẩn, in 3D  → kiểm kê: research/context/EQUIPMENT_AND_ACCESS.md
```

Ngân sách độ phân giải/tốc độ khung (dự kiến, **phải đo lại**): ~11 bit hiệu dụng sau trung bình 16 mẫu; tốc độ khung mục tiêu 45–100 Hz; đủ cho động tác 0,5–2 Hz. Chi tiết: `docs/04_Hardware_Architecture.md`.

## 6. GATE — tiêu chí sống còn

`research/protocols/06_glove_hand_GATE_experiment.md`. Tóm:

- **GATE 0** lặp lại (CV ≤ 5% trong phiên, ICC ≥ 0,75 giữa phiên)
- **GATE A** phân biệt hướng (4 hướng ≥ 85%; cặp đối lập ≥ 90%)
- **GATE B** tái tạo 3D (MAE ≤ 15°, r ≥ 0,8)
- **GATE C ⭐ SỐNG CÒN** Δ giữa các mức chức năng ≥ 2σ_noise; Cohen's d ≥ 0,8; MDC < mức chênh liền kề
- **GATE D** không báo động giả (≤ 10% số phiên qua ≥ 10 ngày)
- **GATE E** tự phát hiện lỗi (≥ 90%, báo động giả ≤ 5%)
- **GATE F** INT8 trên NPU (≤ 50 ms, mất mát ≤ 2%)

**Ngưỡng phải chốt trước khi đo (DEC-METRIC-001).** GATE C fail ⇒ dừng đề tài, báo cáo trung thực.

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
- ❌ Thử trên người tham gia (kể cả người khỏe) trước khi có IRB/SRC
- ❌ Điền số `[X]` vào A.3 hoặc mục C khi chưa có log đo thật

## 9. Việc tiếp theo (theo thứ tự)

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
