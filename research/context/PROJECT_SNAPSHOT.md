# Project snapshot — current summary 2026-10-19 (owner update)

> **Cập nhật giai đoạn 2026-10-23:** chủ dự án xác nhận đề cương đã hoàn tất; nguồn final là `LV1_11A2_12A1 ky.signed.pdf` (`DEC-PROP-020`, `SRC-OWNER-FINAL-2026-10-23`). Dùng [nguồn hiện hành](CURRENT_SUBMISSION_2026-10-17.md) và phần đầu [kiểm kê](EQUIPMENT_AND_ACCESS.md) thay cho các ghi chú cũ bên dưới. Bước tiếp theo là Flex/camera và bố trí nguyên mẫu. Hộp đeo hông + servo trên tay mới là đề xuất; chưa chốt phân bố bo mạch, vị trí camera hay nguồn. Không sửa PDF final, không tự xác nhận kết quả thử nghiệm từ việc chốt đề cương.

> **Nguồn đề cương cập nhật 2026-10-21:** chủ dự án chỉ định [DE_CUONG_NOP_TRUONG.docx](https://docs.google.com/document/d/1VgzlaKYlQj55yCP45YoJ2KSRm10LV9m3/edit) là bản mới nhất sau khi tự sửa văn phong (`DEC-PROP-019`). Dùng tệp này cho các lượt biên tập tiếp theo; các bản Markdown/DOCX do agent dựng trước đó không phải bản phản chiếu của nó. Lượt này chỉ đọc và cập nhật nguồn/profile, không xác nhận thêm kết quả thử nghiệm. Cập nhật thiết kế DSP 2 nhánh trong văn bản mới được ghi nhận riêng tại `research/reviews/2026-10-21_owner_draft_intake.md`; các câu hỏi thiết bị/an toàn/bằng chứng vẫn theo hồ sơ đã có.

> **Current authority:** `research/context/CURRENT_DESIGN_BASELINE.md` and the latest owner decisions in `research/context/DECISION_LOG.md`, including `DEC-REHAB-001`. Historical entries below are retained for traceability; do not treat superseded proposals as active instructions.
>
> **Current functional direction:** a glove intended to support fine-motor rehabilitation practice for middle-aged people after stroke, with home practice as a design target (not validated home use). The intended progression is assisted finger flexion/extension → automatic threshold-based transition to AAN → coordinated thumb/index/middle spoon grasp, lift, transfer and placement at a defined target. No KTV/therapist action is required to switch modes. Exact features/thresholds/windows/hysteresis/fallback remain OPEN.
>
> **Sensor and vision roles:** owner confirmed three Flex sensors, one per thumb/index/middle finger, for bend/posture; Velostat provides local pressure/contact-related relative evidence, not semantic intent, angle or absolute force; camera follows spoon/target/task completion and provides immediate visual feedback. Orange Pi 5 Pro is the proposed vision-compute platform; no vision/depth/latency benchmark or RL capability is claimed. If all sensors share the 16-channel CD74HC4067, reserve 3 Flex channels and at most 13 remain for Velostat/reference inputs; exact map is open. **Cập nhật 2026-10-20 (chủ dự án xác nhận):** 3 cảm biến Flex **chưa có**, phải mua ở mốc 1; thiết kế vẫn giữ 3 Flex + 6 Velostat + 2 REF nên cấu hình 11 kênh không đổi. Bộ chuyển mạch CD74HC4067 **đã có và đã chạy thử**. Tình trạng ADS1115 vẫn chưa xác nhận.
>
> **AAN/mechanics:** primary control objective; servo winds fishing line directly on a spool, no spring/SEA or four-bar linkage. Return/release and active extension, three-finger actuation independence, force reference and thresholds are unresolved (2026-10-20: direction adopted — three separate spools with active servo release, `DEC-MECH-007`; motor count, travel, unpowered release, mass and force reference still open). Velostat not Newton; old `F_assist` equation and 5 N criterion withdrawn.
>
> **Evidence boundary:** bench/phantom first. Powered healthy-volunteer tests only conditional after safety assessment/required approvals. No patient testing, clinical-effectiveness, neuroplasticity, validated home-use, safety certification or novelty/“first” claim. Task measures (placement success, time, drops/retries, transition behavior, vision accuracy) are engineering outcomes, not clinical recovery results. Working title is provisional. Active A/B/C draft: `docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md`; source Drive files and submitted documents remain unchanged.

> **Lượt tài liệu 2026-10-19 (agent thực hiện theo chỉ đạo chủ dự án: hoàn thiện hồ sơ trước, code sau).** Đã soạn bộ artifact Gate 0 và hồ sơ thiết kế đi kèm, tất cả ở mức `PROPOSED`: `research/protocols/10_gate0_task_state_sheet.md` (thông số tác vụ thìa, nhãn trạng thái `T_*`, máy trạng thái chế độ, 5 phương pháp phân biệt vận động tự nguyện vs do actuator tạo, sơ đồ ngón↔cảm biến↔actuator), `10a_gate0_channel_map_and_acquisition_budget.md` + `10b_channel_map_proposed.csv` (4 phương án phân bổ 16 kênh, bản đồ CH0–CH15, ngân sách quét nhãn `[TÍNH TOÁN]`, 8 câu hỏi kỹ thuật phải kiểm tra trước khi cấp nguồn), `docs/07_Vision_TaskState_Architecture.md` (detector cắm được, OpenCV cổ điển trước, phiếu benchmark để trống), `docs/08_Software_Firmware_Roadmap.md` (lộ trình F0–F6). Đề cương `docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md` được bổ sung §C.4 (đăng ký trước chỉ số/ngưỡng, mọi ô ngưỡng `OPEN`) và §C.5 (thứ tự triển khai công cụ). **Không một ngưỡng hay thông số tác vụ nào được điền; không chạy code/firmware/benchmark; không đo phần cứng; không sửa hồ sơ đã nộp hay file nguồn trên Drive; chưa commit GitHub theo yêu cầu chủ dự án.** Việc mới phát hiện cần kiểm tra: giới hạn điện áp đầu vào ADS1115 so với ghi nhận "đọc 0–3,3 V" (`CLM-HW-006`), và bảng tốc độ khung cũ ở `docs/04` §5 không áp dụng cho chuỗi ADS1115 hiện hành (`CLM-ACQ-002`).

> **2026-10-20 (ba quyết định của chủ dự án trong session).** (1) `DEC-CHMAP-001` **ADOPTED = PA-2**: 3 Flex qua CD74HC4067 + 6 Velostat (cặp lòng/mu cho cái–trỏ–giữa) + 2 ô tham chiếu = 11 kênh quét, 5 kênh dự phòng; PA-3a chỉ còn là kiểm tra phần cứng tuỳ chọn. (2) `DEC-TASK-002` **ADOPTED = M3**: cửa sổ "thăm dò tự nguyện" (tạm ngưng trợ lực một khoảng ngắn rồi đo đáp ứng) — là **chọn phương pháp**, chưa kiểm chứng; độ dài cửa sổ, tiêu chí dừng và rà an toàn còn `OPEN`. (3) `DEC-MECH-007` **ADOPTED**: **ba tang cuốn riêng** + **servo nhả dây chủ động** để duỗi, không lò xo/khớp bốn khâu; chưa quyết một động cơ hay ba động cơ, chưa cân lại khối lượng 80–120 g. Theo chỉ đạo, DOCX review đã được dựng lại từ `docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md` → `exports/11A2_CAP_NHAT_DU_THAO_2026-10-20.docx` (script `scripts/build_abc_review_docx.py`); **đây là bản rà soát, không phải bản duyệt toàn văn, không phải bản nộp**. `DEC-TASK-001`, `DEC-VIS-001`, `DEC-IMPL-001/002`, `DEC-ACQ-001` vẫn chờ; **chưa viết code/firmware nào**.

> **HISTORICAL — superseded for current proposal scope on 2026-10-19.** Notes below preserve earlier owner decisions and technical proposals; follow the current authority above when they conflict.

---

# Project snapshot — 2026-09-19 (lượt rà soát prior art 1) · nền 2026-09-13 · cập nhật 2026-10-13 (DEC-GATE-002, DEC-ARCH-001: AAN + Velostat + RL + Orange Pi 5 Pro Edge Intelligence)

> Bản nén ngữ cảnh để phiên sau khôi phục trạng thái **bằng artifact**, không dựa vào trí nhớ hội thoại.
> Chỉ chứa **sự kiện bền vững**. Quyết định đầy đủ: `DECISION_LOG.md`. Đề tài: `docs/01_Topic_Definition.md`.

> **2026-10-13 (`DEC-ARCH-001`, `DEC-GATE-003`, `DEC-GATE-004`, `DEC-GATE-005`):** Xác lập kiến trúc tích hợp sâu & tinh gọn hệ thống GATE: (1) AAN + Velostat là trụ cột cốt lõi không thể tách rời theo nguyên lý Hebbian đóng kín vòng phản hồi cảm giác-vận động. (2) Reinforcement Learning (RL) giải quyết 2 bài toán chuyên sâu: Bù trừ phi tuyến động (Hysteresis/Creep/Drift) cho Velostat dạng MDP (RL Inversion), và học chính sách trợ lực AAN thích ứng chống ỷ lại (Anti-Slacking Actor-Critic). (3) Orange Pi 5 Pro (RK3588, NPU 6 TOPS) làm Trạm Y Sinh Biên (Edge Medical Intelligence Station), chạy mô hình `.rknn` INT8 thời gian thực (trễ $\le 20\text{ ms}$) và bảo mật dữ liệu y tế độc lập. (4) **Zero-Camera Policy (`DEC-GATE-005`):** Loại bỏ hoàn toàn camera và ArUco, 100% xử lý bằng cảm biến nội tại. (5) Loại bỏ GATE D, E, AAN-3 (`DEC-GATE-003`), hủy GATE B và gộp vào GATE A (`DEC-GATE-004`). Hệ GATE chuẩn chốt đúng 6 cổng: `GATE 0 → GATE A → GATE C (trọng tâm)` (Nhánh Đo); `GATE AAN-1 → GATE AAN-2` (Nhánh AAN); `GATE EDGE` (Trạm biên AI). Chi tiết: `research/protocols/06_glove_hand_GATE_experiment.md`.

---


## 1. Đề tài (CHỐT nội dung — DEC-TOPIC-019; CHỐT tên hiển thị — DEC-TITLE-003, 2026-10-11)

> **Lưu ý: 2026-09-27:** README ngày 2026-09-19 ghi "tên chốt `DEC-TITLE-001`" nhưng quyết định này **không có trong `DECISION_LOG.md`**
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

> **CẬP NHẬT 2026-10-11 (`DEC-SCOPE-006`, `DEC-SYNC-002`):** phát hiện bản đề cương mới hơn chưa đồng bộ — `de_cuong/DE_CUONG_NGHIEN_CUU.pdf` (16tr, tạo 2026-10-03) vs bản đã nộp trường `docs/DE_CUONG.pdf` (15tr, 2026-09-26). Bản mới bổ sung Mục 10: cơ cấu **AAN (Assist-as-Needed)** nay là **trụ cột kỹ thuật chính thức thứ 4** của đề tài (nhóm nghiên cứu nêu minh thị). AAN chỉ chạy trên **giàn đo + mô hình tay giả phantom**, tuyệt đối không tác động lực lên người thật — ranh giới `DEC-SCOPE-003` không đổi. Đồng thời ghi nhận (`DEC-PHASE-002`): nhóm nghiên cứu đã **tự thực hiện** bring-up phần cứng thật (ESP32-S3+ADS1115+INA333+CD74HC4067, log `research/notebooklm_sync/experiments/`), nhưng **chưa chính thức hoá** thành log GATE 0 hợp lệ. Tên đề tài **chưa đổi** (`DEC-TITLE-003` đề xuất 4 phương án, chờ chọn).

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

> **Lưu ý: CẬP NHẬT 2026-09-19 — lượt rà soát prior art 1** (`research/reviews/2026-09-19_prior_art_novelty_gate1.md`). Mức novelty bên dưới đã **dịch chuyển**: A bị hạ một bậc, C được nâng lên trọng tâm. **Chưa chốt** — chờ `DEC-NOV-001` + lane R5.

- **KHÔNG** claim "găng tay + AI/TinyML" là mới; **KHÔNG** claim "đo lực bóp" là mới; **KHÔNG** claim "không dùng IMU" là mới (đã có găng grating/optic 2021, stretch 2024).
- ~~Ứng viên chính: cảm biến hướng qua vách khung cứng~~ → **sau lượt rà soát 1: chỉ còn là "cải tiến cấu hình + phương pháp lập luận"**, vì:
  - `SRC-SIDEWALL-PIEZO-2015` (Sensors 15(10), DOI 10.3390/s151025463): **1 lõi + 4 vách elastomer**, phần tử CNT/PDMS khóa liên động, phân biệt pháp tuyến + shear 4 hướng **không cần xử lý tín hiệu phức tạp** → nguyên lý "vách mã hóa hướng" có từ 2015.
  - `SRC-ARTGLOVE-2026` (arXiv:2606.16370): **găng vỏ cứng khớp nối, 16 bề mặt chức năng, da áp điện trở 2048 taxel @120 Hz** — nhưng 22 DoF đo bằng **encoder**.
  - `SRC-CN116954366A-ARRAYGLOVE`: bằng sáng chế găng 20 phần tử áp điện trở tại 14 khớp ngón + lòng bàn.
- **Ứng viên chính mới (đề xuất): C** = chỉ số chức năng bàn tay từ lực hướng, kèm **khung MDC/ICC** và **cờ từ chối kết luận**, dùng tại nhà giữa hai lần tái khám. Giao điểm này **chưa thấy ai làm đủ**, nhưng **cấm** nói "hệ thống đầu tiên theo dõi tại nhà": đã có `SRC-LOWCOST-GLOVE-2006` (găng extended monitoring + functional hand assessment, 2006) và `SRC-MULTITOUCH-APP-2021` (app tablet n=88, có SEM/MDC, hội tụ FMA-UE/JTT/BBT/NHPT).
- **KHÔNG mới (phải trích dẫn prior art):** đọc vi sai/ô tham chiếu để bù drift (thêm bằng chứng `SRC-OPENPAD-FINGER-2020`: 2 phần tử hai bên đốt ngón để tách thành phần lực, từ 2020); INT8 quantization.
- **Prior art đã xác minh danh tính 2026-09-19:** `SRC-ZHU-2017-GLOVE` = Liu H. et al., IROS 2017, tr. 6617–6624, DOI 10.1109/IROS.2017.8206575 (đúng như mô tả cũ; bổ sung: hướng vector lực **gán theo pose từ IMU**, không suy từ vách). `SRC-RECONFIG-GLOVE-2023` = Liu H. et al., **Engineering** 2024;32(1):217-232, DOI 10.1016/j.eng.2023.01.009 — **sửa**: không phải "Science China". `SRC-SMARTGLOVE-REVIEW-2026` = Mohammed A., Ali A.M., *J. Eng. Appl. Sci.* 73:246 (2026), DOI 10.1186/s44147-026-01084-6 (101 bài 2011–2025; 72% fusion flex+IMU).
- **Rủi ro trùng trong nước (mức học sinh):** `SRC-VNM-HS-GLove-2026` — học sinh Lâm Đồng làm "găng tay thông minh tích hợp AI" có **cảm biến lực + áp suất khí**, theo dõi tiến độ phục hồi, **giải nhất cấp tỉnh 2026**; `SRC-VNM-ANNAM-2022` (găng mềm PneuNet, giải Nhất EPICS 2022); `SRC-VNM-TL-GLOVE-2026` (găng robot + theo dõi từ xa). **Toàn bộ đều là máy tập/hỗ trợ chủ động**, không phải thiết bị đánh giá có kiểm chứng độ tin cậy → phải nêu trong mục "bất cập của giải pháp hiện tại".
- **Gap 1 chưa hoàn tất.** Còn: (i) đọc **toàn văn** 5 nguồn (`SRC-ARTGLOVE-2026`, `SRC-SIDEWALL-PIEZO-2015`, `SRC-GRATING-GLOVE-2021`, `SRC-LOWCOST-GLOVE-2006`, `SRC-MANUMETER-RCT-2022`); (ii) tra bằng sáng chế theo IPC A61B5/11 · A61B5/22 · A61B5/10 · G01L1/14 · A61H1/02 (lượt vừa rồi mới 1 truy vấn web, **không đủ** để kết luận); (iii) lane R5 adjudicate; (iv) `DEC-NOV-001` do trưởng nhóm chốt.

## 5. Phần cứng (CHỐT — DEC-HW-002/003/004/005/006)

```
Sensing element : Màng Velostat + cuộn dây đồng mạ niken (cấu trúc Sandwich chống oxy hóa)
Khung           : Găng in 3D (PLA/PETG + TPU), vách ép tạo hướng (Mech 9 khóa ngàm xoay)
Mạch thu nhận   : 
  - Vòng lặp 1 (bring-up): INA333 G ≈ 6.5 + ADS1115 + CD74HC4067 (bị bão hòa khi siết ốp cơ khí)
  - Vòng lặp 2 (tối ưu hóa - DEC-HW-006): MUX CD74HC4067 (Settling 300 µs + Dummy read)
    -> Đọc trực tiếp qua PGA 16-bit nội bộ ADS1115 (0 - 3.3V, 0.125 mV/LSB)
    -> ESP32-S3: Bộ lọc số DSP 4 bước (Dummy read -> Dead-band 180 mV -> Adaptive drift tracking -> EMA & F_net vi sai)
MCU             : ESP32-S3 (ngắt phần cứng ALRT 100 Hz, BLE 5, logic 3.3 V)
Edge            : Orange Pi 5 Pro RK3588 — [ĐÃ LOẠI BỎ vai trò Trạm Y Sinh Biên / RL Inversion / INT8 — DEC-EDGE-001, 2026-10-20]
                  chỉ còn nhánh thị giác: thìa/vùng đích, nhãn trạng thái tác vụ, phản hồi thị giác
Tham chiếu bench: Load cell + HX711 (GATE A trở đi; GATE 0 dùng khối lượng chuẩn, F = m·g)
Zero-Camera     : 100% cảm biến nội tại, không dùng camera ngoài (DEC-GATE-005)
```

## 6. Hệ thống GATE kiểm chứng (chốt 2026-10-13 với 6 cổng — DEC-GATE-002, 003, 004, 005; **nay còn 5 cổng** sau khi bỏ GATE EDGE theo DEC-EDGE-001, 2026-10-20)

> **ĐÃ LOẠI BỎ KHỎI PHẠM VI (2026-10-20, `DEC-EDGE-001`):** vai trò "trạm trí tuệ biên" của Orange Pi 5 Pro (lượng tử hóa INT8/RKNN, suy luận NPU ≤ 20 ms, mô hình RL bù trôi/trễ — GATE EDGE/M6) và nhiệm vụ "kiểm chứng thuật toán tự động gắn nhãn 'Nghi vấn'" **không còn trong phạm vi đề tài**. Orange Pi 5 Pro chỉ đảm nhận nhánh thị giác: nhận biết thìa/vùng đích, gán nhãn trạng thái tác vụ và phản hồi thị giác (`CURRENT_DESIGN_BASELINE.md`, `DEC-VIS-001`), xử lý ảnh cổ điển trước, chỉ dùng mô hình học sâu nếu benchmark trên đúng phần cứng không đạt. Việc loại phiên đo lỗi vẫn giữ nhưng dưới dạng trạng thái `INVALID` kèm ghi lý do, không phải một thuật toán gắn nhãn tự động. Nội dung bên dưới được giữ nguyên để tra cứu lịch sử, không phải việc sẽ làm.


Chi tiết tại `research/protocols/06_glove_hand_GATE_experiment.md`:

**Nhánh Đo (Assessment):**
- **GATE 0** (M1): Đặc tính cơ lý thô gốc & cửa sổ làm việc Velostat ($CV \le 5\%$, $ICC \ge 0,75$, đường cong trôi/trễ).
- **GATE A** (M2): Nhận diện hướng gập/duỗi vi sai ($\ge 90\%$) & Bản đồ kích hoạt nỗ lực động ($\ge 85\%$).
- **GATE C (CỔNG SỐNG CÒN)** (M3): $\Delta_{signal} \ge 2\sigma_{noise}$; Cohen's $d \ge 0,8$; $MDC < \Delta_{step}$ — **fail ⇒ dừng cả đề tài**.

**Nhánh Trợ lực - AAN (Movement Support):**
- **GATE AAN-1** (M4): Nhận diện nỗ lực tĩnh sớm trước khi ngón di chuyển ($EI$, $AUC \ge 0,85$, $t_{detect} \le 300\text{ ms}$).
- **GATE AAN-2 (CỔNG SỐNG CÒN NHÁNH AAN)** (M5): Đường cong tải $RAL$ ổn định ($ICC \ge 0,75$) & Triệt tiêu hiện tượng ỷ lại ($PR \ge 50\%$) — **fail ⇒ không dừng đề tài, chỉ hạ nhãn AAN xuống "trợ lực cố định phân bậc"**.

**Trạm Y Sinh Biên (Edge Medical Intelligence Station - Orange Pi 5 Pro):**
- **GATE EDGE** (M6) — **ĐÃ LOẠI BỎ 2026-10-20 (`DEC-EDGE-001`)**, nội dung cũ giữ để tra cứu: chạy mô hình RL bù động trôi/trễ Velostat (MDP Inversion) và suy luận chính sách AAN thời gian thực ($\le 20\text{ ms}$ INT8 `.rknn`) — 100% cảm biến nội tại, không dùng camera.

> **Đã loại bỏ:** GATE D, GATE E, GATE AAN-3 và **GATE EDGE/M6** (`DEC-EDGE-001`, 2026-10-20 — lượng tử hóa INT8, suy luận NPU và mô hình RL trên Orange Pi 5 Pro) (thuộc thẩm quyền kiểm định y tế lâm sàng độc lập — `DEC-GATE-003`); hủy GATE B cũ gộp vào GATE A (`DEC-GATE-004`).

> **Lưu ý: 2026-09-27 — ngưỡng ĐÃ NỘP là M1–M6 + C1.1–C1.10** (PDF §5.2/§11.1, `CLM-MET-005`, chờ `DEC-METRIC-002` phê chuẩn):
> R² ≥ 0,90 (thay 0,95) · liên ngày CV ≤ 8 % trên phantom (thay ICC ≥ 0,75) · hys ≤ 18 % (thay 15 %) ·
> creep ≤ 8 % giữ 60 s@5 N (thay creep_2dec ≤ 3 %) · trôi/tín hiệu ≤ 2,0/10 ngày qua auto-zero (bỏ điều kiện ΔV@1N) ·
> M6 = phát hiện đeo lỏng ≥ 80 % qua V_base (thay fault-injection ≥ 4/5).
> Định nghĩa đã nộp (`CLM-DEF-001`): **GAP = PROM − AROM** (độ, theo giao thức) · **RAL** = nấc tải (g) nhỏ nhất đạt P_complete ≥ 80 % ·
> **EI** = trung vị biến thiên phổ vi sai chuẩn hóa vận tốc góc (công thức tường minh còn nợ).
> Bảng đối chiếu: sync review §4. `protocols/08` §7 giữ 10 ô chờ chốt — chờ nhóm họp chốt.

## 7. Ngôn ngữ bắt buộc (DEC-MSG-001)

| Dùng | Không dùng |
|---|---|
| suy luận hướng gập/duỗi | đo góc khớp |
| giảm ảnh hưởng drift | loại bỏ drift / drift-free |
| găng tay đánh giá và theo dõi | robot/găng tập phục hồi chức năng |
| sensing element chế tạo từ vật liệu Velostat | cảm biến Velostat |
| bổ sung cho đánh giá lâm sàng | thay thế Fugl-Meyer/ARAT |

## 8. Tuyên bố bị cấm

- [Không làm/Ngoài phạm vi] Chẩn đoán đột quỵ / mức độ liệt / tiên lượng
- [Không làm/Ngoài phạm vi] Thay thế FMA / ARAT / Box and Block / đánh giá của chuyên gia
- [Không làm/Ngoài phạm vi] "Đo chính xác lực tuyệt đối" / "đo góc khớp"
- [Không làm/Ngoài phạm vi] "Đã kiểm chứng lâm sàng" / "chứng minh hiệu quả"
- [Không làm/Ngoài phạm vi] Thử trên người tham gia (kể cả người khỏe) trước khi có IRB/SRC (`DEC-ETHICS-001` vẫn OPEN; bản nộp §7.2/§12 giới hạn ở **tự thử trên chính người thực hiện, chế độ đo, không tác động lực, tự nguyện + quy tắc dừng** — không mở rộng sang người khác/bệnh nhân)
- [Không làm/Ngoài phạm vi] Điền số `[X]` vào A.3 hoặc mục C khi chưa có log đo thật

## 9. Việc tiếp theo (theo thứ tự)

-2. [Đạt] **ĐÃ LÀM 2026-10-13 (phiên này, `DEC-GATE-003`, `DEC-GATE-004`, `DEC-GATE-005`):** 
   - Tinh gọn dứt khoát hệ thống cổng kiểm chứng thành đúng **6 GATE**:
     * Nhánh Đo: `GATE 0 (M1) → GATE A (M2) → GATE C (trọng tâm) (M3)`
     * Nhánh Trợ lực: `GATE AAN-1 (M4) → GATE AAN-2 (M5)`
     * Trạm Y Sinh Biên: `GATE EDGE (M6)`
   - Loại bỏ GATE D, GATE E, GATE AAN-3 vì thẩm quyền kiểm định y tế lâm sàng thuộc phòng kiểm chuẩn độc lập, học sinh không tự cấp chứng nhận (`DEC-GATE-003`).
   - Hủy bỏ GATE B (tái tạo góc 3D do phi thực tế), gộp toàn bộ vào GATE A mới (nhận diện hướng gập/duỗi vi sai $\ge 90\%$ & bản đồ kích hoạt nỗ lực động $\ge 85\%$) (`DEC-GATE-004`).
   - Chốt Hướng 1: M1/GATE 0 làm baseline cơ lý thô trên băng thử, M6/GATE EDGE chạy RL Inversion trên Orange Pi 5 Pro để bù trừ trôi/trễ thời gian thực — **nội dung này đã bị loại bỏ ngày 2026-10-20 (`DEC-EDGE-001`)**.
   - Chốt **Zero-Camera Policy**: Không dùng camera ngoài hay marker ArUco; 100% cảm biến nội tại (`DEC-GATE-005`).
   - Đã đồng bộ toàn bộ vào `research/context/DECISION_LOG.md`, `research/protocols/06_glove_hand_GATE_experiment.md`, `docs/DE_CUONG_NOP_BAN_KHKT_2026-10-18.md` và git (`origin/main`).
   5. **Nợ đồng bộ xuyên repo (phát hiện khi rà soát, chưa sửa):** nhiều file khác vẫn còn nhắc tên
      GATE cũ, không phải lỗi số liệu — chỉ là tên gọi/cấu trúc GATE chưa theo kịp `DEC-GATE-002`:
      - còn nhắc **"GATE F"** kiểu cũ (coi là cổng cam kết cứng, không phải "GATE EDGE — đang chọn"):
        `tài liệu nội bộ`, `README.md`, `docs/01_Topic_Definition.md`.
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

-1. [Đạt] **ĐÃ LÀM 2026-10-13 (`DEC-PROP-003`):** Ban KHKT ra thông báo chính thức khuôn đề cương nộp
   vòng trường (6 mục: Tên dự án/Lý do/Mục tiêu/Ý tưởng-nội dung/Sản phẩm dự kiến/Tính khả thi),
   **hạn nộp 17h 18/10/2026**, nộp Word/PDF qua link sẽ có ở nhóm Zalo CLB KHKT. Đã soạn
   `docs/DE_CUONG_NOP_BAN_KHKT_2026-10-18.md` theo đúng khuôn này (tái dùng nội dung từ
   `docs/DE_CUONG_NGAN_5-7_TRANG_DRAFT.md`/`docs/DE_CUONG_NOP_TRUONG.md`). Phát hiện khi soạn mục
   Tính khả thi: theo `protocols/08` thì GATE 0 (~3 tuần) + GATE C (≥28 ngày trôi) khiến đề tài
   **không thể xong toàn bộ GATE 0→F trước cuối tháng 11/2026** — đã viết trung thực hướng này
   thay vì hứa hẹn, nhưng **chưa qua nhóm thống nhất cách đóng khung**.
   [ ] **CẦN NHÓM CHỐT (gấp, hạn 18/10):** duyệt nội dung + cách đóng khung "Tính khả thi";
   điền 3 ô danh tính; xác nhận link nộp khi Ban KHKT công bố; xuất file sang .docx/.pdf để nộp.
0. [Đạt] **ĐÃ LÀM 2026-10-11:** đọc toàn bộ repo + xác nhận setup môi trường (venv/pip/bootstrap/check --strict 10/11/context bundle); đọc toàn văn `research/notebooklm_sync/` (10 file: README, 5 experiment log, 1 chat transcript 402 dòng, 3 file studio) và phát hiện bản đề cương chưa đồng bộ `de_cuong/DE_CUONG_NGHIEN_CUU.pdf` (2026-10-03, 16tr). Theo chỉ đạo minh thị của nhóm nghiên cứu: `DEC-SYNC-002` (công nhận bản mới) + `DEC-SCOPE-006` (AAN = trụ cột thứ 4, ranh giới an toàn không đổi) + `DEC-PHASE-002` (ghi nhận bring-up phần cứng thật do nhóm nghiên cứu tự làm, chưa chính thức hoá GATE 0) + `DEC-TITLE-003` (4 phương án tên, PROPOSED). Cập nhật README §1/§6.1/§8/§10/§11, +6 nguồn/+3 claim/+5 quyết định.
   [ ] **Kế hoạch cần chốt của nhóm:** chọn phương án tên (`DEC-TITLE-003`); xác nhận `de_cuong/DE_CUONG_NGHIEN_CUU.pdf` có phải bản sẽ nộp lại; chính thức hoá log bring-up thành GATE 0 hợp lệ; xác nhận đổi tên cảm biến SHT30→AHT20.
0. [Đạt] **ĐÃ LÀM 2026-09-27:** đồng bộ bản nộp `docs/DE_CUONG.pdf` (2026-09-26) → `research/reviews/2026-09-27_decuong_pdf_sync.md`;
   môi trường cài lại (venv + skills OK, 10/11 check); +7 nguồn ledger (147), +3 claim (27), +2 truy vấn xác minh [15]/[18] (81, đều `UNVERIFIED`);
   sửa README (tên/đội hình/ngưỡng), `docs/04` §8 + `docs/02` §11 mới, điền danh tính `DE_CUONG_NOP_TRUONG.md`.
   [ ] **Kế hoạch cần chốt của nhóm:** 6 quyết định `DEC-SYNC-001`/`DEC-TEAM-001`/`DEC-TITLE-002`/`DEC-HW-005`/`DEC-METRIC-002`/`DEC-SCOPE-005` + duyệt 7 nguồn/3 claim mới.
0. [Đạt] **ĐÃ LÀM 2026-09-19:** lượt rà soát prior art 1 → `research/reviews/2026-09-19_prior_art_novelty_gate1.md`; 24 nguồn vào ledger (20 `READ_ABSTRACT`, 4 `UNVERIFIED` — chưa đọc toàn văn); 3 claim cập nhật + 2 claim mới; GATE A/C có thêm mốc so sánh y văn. [ ] **CÒN NỢ:** đọc toàn văn 5 nguồn, tra IPC bằng sáng chế, `DEC-NOV-001`.
0.5 [ ] **NGANG HÀNG QUAN TRỌNG (mới 2026-09-19):** nhóm nghiên cứu chốt `DEC-SCOPE-002` cho đề xuất "tập chủ động có trợ lực" — E1 (chỉ lý thuyết) / E2-lite (chỉ số Effort+gap AROM−PROM+RAL, không động cơ, **khuyến nghị**) / E3 (động cơ + Bowden, 8–15 tuần, đổi trục + rủi ro an toàn + IRB). **CẬP NHẬT: sau phản hồi của nhóm nghiên cứu về chuẩn ViSEF, khuyến nghị mới là E4+E5+E6 (rig phantom + RAL + 1 servo kéo phantom + tầng kê đơn), **đã xác minh chuẩn tham chiếu ISEF 2025 ROBO065T (THPT thị xã Quảng Trị, giải Tư, thuần tích hợp + 4 số tự đo)** -> xem `DEC-SCOPE-002b/c` và `research/protocols/07_ral_phantom_and_ktv_interview.md`. **Chưa chốt → không bắt tay vào cơ khí chấp hành, không đổi docs/01 §1, không đổi A.4.**
1. [ ] **GIAI ĐOẠN HIỆN TẠI (chỉ thị 2026-09-19): CƠ SỞ LÝ THUYẾT.** Đã xong 2 việc nhóm nghiên cứu yêu cầu: (1) **mô hình chuỗi đo** → `docs/02` §5.5 (dự toán đơn bậc độ lớn: `F_p ≤ 68·γ·ΔF`, cửa sổ làm việc 2 đầu, yêu cầu rig có ≥2 tốc độ kéo); (4) **đối chiếu toàn văn/danh tính** → sửa 3 lỗi nguồn (Engineering 32:202–216; ironHand = J Rehabil Assist Technol Eng **2016**; US20150233779A1 = Abandoned + CPC) và **phát hiện đối thủ mới** `SRC-TW-SPASTICITY-2022`. Tra cứu bằng sáng chế theo phân loại: **bất khả thi trong môi trường này** — phương pháp + lối thoát ghi ở `docs/03` §7. Hồ sơ nộp: đã soạn `docs/05_De_Cuong_Dang_Ky_DRAFT.md` + đánh giá trần đề tài `research/reviews/2026-09-19_project_ceiling.md` (nhóm nghiên cứu điền tên/GVHD/timeline, duyệt DEC-SCOPE-004).  Đã viết vào `docs/02` §1.4–§1.6 (ba chế độ tập, Hebbian có điều kiện, learned non-use + bẫy slacking), §3.4 (co cứng theo quan hệ tốc độ–lực cản), §5.4 (điều kiện đo nỗ lực khi chưa cử động), §7.3 (định nghĩa Effort Index / Gap AROM−PROM / RAL + bảng cấm quy đổi đơn vị), §8.3 (tầng đo được vs tầng suy ra lâm sàng). **Chưa làm:** chốt ngưỡng GATE A′/RAL + 9 ngưỡng GATE 0 (`protocols/08` §7), viết script thống kê, chế tạo jig/phantom. Nhóm nghiên cứu cho biết **thời gian đủ** (`DEC-PLAN-001`). Nhóm nghiên cứu khai báo đã có thiết bị + KTV 10 năm phản biện (`DEC-RESOURCE-001`) ⇒ **Lớp 0–1 giải ngân được về tiền**; blocker duy nhất còn lại là 9 ngưỡng `protocols/08` §7. **2026-09-19 (11):** bản **nộp được** đã ra đời: `docs/DE_CUONG_NOP_TRUONG.md` (`DEC-PROP-001`); `docs/05` → outline nội bộ. Số liệu dịch tễ đã kiểm (`CLM-BIO-003/-004`); phát hiện A.1 gán con số 80% cho Hendricks 2002 trong khi nguồn đã kiểm là Cochrane 2014 — **nhóm nghiên cứu sửa A.1** (nay là **10** ô: thêm `G0.0` chọn định nghĩa nhiễu). Nhóm nghiên cứu chốt: **giữ pha lý thuyết** — không firmware/không script (`DEC-PHASE-001`) → đã phát hành phiếu đo in được `protocols/08a`; và **không nêu danh tính người tham khảo** trong hồ sơ (`DEC-ROLE-001`). Kiểm kê + việc tuần này: `research/context/EQUIPMENT_AND_ACCESS.md`. Benchmark hình thức từ báo cáo QG 2024–2025 (15 tr., 17 hình/3 bảng, 0 thống kê) → `2026-09-19_benchmark_xe_lan_ALS_QG2025.md` → kế hoạch giữ đủ 7 cổng; `protocols/08` đã sẵn sàng chạy ngay khi §7 được chốt.
1. [ ] Chốt cấu hình kênh 1 → 2 (hay làm thẳng cấu hình 2).
2. [ ] Chốt giao thức bài tập chuẩn cùng KTVVLTL-PHCN.
3. [ ] Rà soát prior art **nửa còn lại** theo `docs/03` → chốt mức novelty qua `DEC-NOV-001`.
4. [ ] Chế tạo sensing element → đo `R_sensor`/tải → chọn `R_f`.
5. [ ] Chạy GATE 0 → GATE A/B → **GATE C** → GATE D/E/F.
6. [ ] Điền số thật vào A.3 + mục C của outline.
7. [ ] Nhóm nghiên cứu đổi tên repo (DEC-REPO-001) và (nếu cần) đổi tên thư mục cục bộ.

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
