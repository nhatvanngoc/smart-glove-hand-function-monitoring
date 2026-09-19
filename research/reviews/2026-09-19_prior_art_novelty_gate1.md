# GAP 1 — Kết quả rà soát prior art cho 4 ứng viên novelty

> **Ngày:** 2026-09-19 · **Người thực hiện:** agent phiên Arena (01a0b8f4)
> **Phạm vi:** `docs/03_Literature_Gap_Analysis_Plan.md` mục 1 (ứng viên A, B, C, D) + mục 6 (ngưỡng ra quyết định).
> **Trạng thái quy trình:** đây là **một lượt rà soát đơn-lever, sequential role review; KHÔNG phải independent multi-agent verification** (theo `AGENTS.md` §5). Chưa có lane R5 độc lập adjudicate.
> **Cảnh báo bằng chứng:** 24 nguồn mới thêm vào `SOURCE_LEDGER.csv`; chỉ 2 dòng được nâng lên `VERIFIED` (danh tính thư mục), còn lại ở mức `READ_ABSTRACT`/`UNVERIFIED` — **tức chưa đọc toàn văn**. Không một kết luận nào dưới đây được phép đưa vào báo cáo như "kết quả thực nghiệm" hay "chưa có ai làm".

---

## 0. Kết luận ngắn (đọc 30 giây)

| Ứng viên | Trước (docs/01) | **Sau rà soát — đề xuất** | Lý do chính |
|---|---|---|---|
| **A** — cảm biến hướng qua vách khung cứng, không IMU | "ứng viên chính (vật lý/cơ khí)" | ⬇️ **HẠ xuống "cải tiến ở tầng cài đặt phần tử + cách lập luận hướng khớp"** | Nguyên lý "phần tử piezoresistive trên **vách** → phân biệt hướng" đã có từ **2014–2015**; "vỏ cứng khớp nối + bề mặt chức năng phủ da áp điện trở" đã có **2026** (ART-Glove, nhưng dùng encoder đo góc) |
| **B** — suy luận hướng khớp / tái tạo 3D không cần IMU | "chưa thấy công bố" | ⚠️ **Giữ, nhưng phải phát biểu lại**: "suy luận **dấu** gập/duỗi **chỉ từ mẫu kích hoạt trên vách** (không IMU, không encoder, không camera)" | "Đo góc khớp không IMU" **tự nó không mới** (grating-strip 2021, stretch 2024, FBG, Hall) |
| **C** — theo dõi dọc tại nhà + tự kiểm tra độ tin cậy | "ứng dụng — khoảng trống được xác nhận" | ⬆️ **NÂNG thành ứng viên novelty chính**, với điều kiện: đọc toàn văn Shadow Monitor 2006 và chỉ ra khác biệt | Không tìm thấy công bố nào **kết hợp** (i) longitudinal + (ii) MDC/độ tin cậy + (iii) cờ từ chối kết luận, cho chức năng bàn tay sau đột quỵ |
| **D** — rẻ hơn dynamometer/E-Link | "kỹ thuật triển khai" | **Giữ nguyên** (so sánh bằng BOM + giá thiết bị thương mại có thật, không nói suông) | PPS TactileGlove II / VMG30 / CyberGlove là mốc so sánh thực |

**Hệ quả với câu định vị trước hội đồng:** không còn được nói "cái mới nằm ở **nguyên lý cơ chế**". Câu an toàn và vẫn mạnh:

> "Cái mới không phải 'găng tay + AI', cũng không phải 'dùng vách để đo hướng' — ý đó đã có trong cảm biến xúc giác từ 2015. Cái mới là **dùng đúng cấu trúc vách có kéo trước + đọc vi sai để lấy DẤU của gập/duỗi mà không cần IMU hay encoder**, rồi **kiểm chứng xem chỉ số đó có đủ ổn định để kết luận về tiến triển hay không**, và **tự nhận khi nó không đủ tin**."

---

## 1. Ba nguồn UNVERIFIED: đã xác minh xong

| ID | Kết quả |
|---|---|
| `SRC-ZHU-2017-GLOVE` | **VERIFIED** — Liu H. et al., "A Glove-based System for Studying Hand-Object Manipulation **via Joint Pose and Force Sensing**", IROS 2017, tr. 6617–6624, DOI 10.1109/IROS.2017.8206575. Đúng như repo ghi: **15 IMU BNO055 @20 Hz cho pose; 6 cụm Velostat (26 taxel) @40 Hz chỉ đo lực tiếp xúc**. Bổ sung quan trọng: hướng vector lực trong bài đó được **gán** vuông góc với lóng ngón theo pose do IMU — tức hướng đến từ IMU, không đến từ vách. |
| `SRC-RECONFIG-GLOVE-2023` | **VERIFIED** — Liu H. et al., *Engineering* 2024;32(1):217-232, DOI 10.1016/j.eng.2023.01.009 (arXiv:2301.05821). **Sửa repo:** đây là tạp chí **Engineering**, không phải "Science China". Vẫn dùng mạng IMU chung làm backbone → không phải prior art cho B. Số trang giữa các nguồn khác nhau (217–232 vs 202–216) → phải đối chiếu PDF gốc. |
| `SRC-SMARTGLOVE-REVIEW-2026` | **READ_ABSTRACT / VERIFIED về danh tính** — Mohammed A., Ali A.M., *Journal of Engineering and Applied Science* **73**:246 (2026), DOI 10.1186/s44147-026-01084-6. 101 bài 2011–2025, PRISMA 2020; **72% dùng fusion flex+IMU**; accuracy 82–99%; kết luận: thiếu benchmark chuẩn hóa, thiếu kiểm chứng lâm sàng, cần edge-AI + dataset chuẩn. → Chỉ dùng để mô tả **tình trạng ngành**, không dùng để chứng minh khoảng trống riêng của đề tài. |

---

## 2. Prior art gần nhất cho từng ứng viên (ma trận `docs/03` §5 — bản điền đầu tiên)

Ký hiệu: **Dir.** = có suy hướng/dấu chuyển động không; **IMU?** = có dùng IMU/camera không; **Long.** = có theo dõi dọc không; **Self-chk** = có tự kiểm tra độ tin cậy không.

### 2.1 Ứng viên A — "hướng qua vách khung cứng, piezoresistive"

| Nguồn | Loại | Cơ chế | Dir. | IMU? | Long. | Self-chk | Khác biệt còn lại của đề tài |
|---|---|---|---|---|---|---|---|
| `SRC-SIDEWALL-PIEZO-2015` — *Piezoresistive Tactile Sensor Discriminating Multidirectional Forces*, Sensors 15(10), DOI 10.3390/s151025463 | bài báo | Lõi linh hoạt + **4 vách elastomer** chứa phần tử CNT/PDMS khóa liên động; kênh nào đổi điện trở ⇒ hướng shear | ✅ (4 hướng) | ❌ | ❌ | ❌ | Đây là **một phần tử xúc giác đơn lẻ cho da nhân tạo**, không gắn lên khung từng lóng ngón; không suy hướng khớp, không ứng dụng PHCN |
| `SRC-INTERLOCKED-MICRODOME-2014` — ACS Nano, DOI 10.1021/nn505953t | bài báo | Mảng microdome piezoresistive khóa liên động → phân biệt normal/shear/bending/twisting | ✅ | ❌ | ❌ | ❌ | Cùng họ nguyên lý; chưa đọc toàn văn → chưa đánh giá hết mức trùng |
| `SRC-ARTGLOVE-2026` — **ART-Glove**, arXiv:2606.16370 | bài báo (preprint) | **Găng vỏ cứng khớp nối: 16 "rigid functional surfaces"** phủ ngón/cái/lòng bàn + **da áp điện trở 2048 taxel @120 Hz**; 22 khớp có **encoder** | ✅ (qua encoder) | ❌ IMU, ✅ encoder | ❌ | ❌ | Họ **đo góc bằng encoder**, không suy từ mẫu vách; mục đích thu dữ liệu cho robot learning; độ phức tạp/giá cao hơn nhiều |
| `SRC-CN116954366A-ARRAYGLOVE` (bằng sáng chế CN) | patent | 20 phần tử áp điện trở đặt tại 14 khớp ngón + lòng bàn, 2 lớp flex circuit, phân áp, MCU | ⚠️ chỉ "cảm nhận trạng thái vận động" | ❌ | ❌ | ❌ | Không có vách khung + preload; không suy hướng khớp có dấu; không vì PHCN |
| `SRC-OPENPAD-FINGER-2020` — Sensors 20(1):4 | bài báo | 2 phần tử **hai bên** (radial/ulnar) đốt ngón để tách thành phần lực theo DoF | ✅ (tách thành phần) | ❌ | ❌ | ❌ |dùng điện dung (không phải piezoresistive); đọc 2 bên **đã có tiền lệ** → càng không được claim cặp đối xứng |
| `SRC-TW201533608A-PRESSUREGLOVE` (patent, đã ABANDONED 2017) | patent | Áp kế ở mặt tiếp xúc ngón + accel + gyro | ❌ | ✅ | ❌ | ❌ | Không liên quan vách; note: abandoned |

**Xét theo ngưỡng `docs/03` §6:** điều kiện "tìm thấy **một** công bố đã làm **đúng** khung cứng + piezoresistive → suy hướng khớp → tái tạo 3D" **chưa xảy ra**. Nhưng đã tìm thấy (a) **đúng nguyên lý phần tử** (2014–2015) và (b) **đúng kiến trúc vỏ cứng + da áp điện trở trên bề mặt chức năng** (2026). ⇒ **Phải hạ mức A** theo tinh thần §6: từ "nguyên lý vật lý/cơ khí mới" xuống "**cải tiến cấu hình + phương pháp lập luận**", và bắt buộc trích dẫn 4 nguồn trên.

### 2.2 Ứng viên B — "không cần IMU/camera vẫn suy được hướng khớp"

| Nguồn | Cách làm | Hệ quả cho đề tài |
|---|---|---|
| `SRC-GRATING-GLOVE-2021` (Sensors, PMC8304804) | 14 đơn vị dải cách tử + đầu dò quang ở mặt lưng, **không IMU**, không camera; model gỗ: nonlinearity 1.31%, hysteresis 0.86%, repeatability 0.57%, precision 1.67% FS; PIP RMS < 3.29° | "không dùng IMU" **không phải điểm mới**. Đồng thời đặt **thước đo phải vượt**: sai số của họ đã ở mức vài độ, nhưng họ dùng cơ cấu dẫn hướng — còn ta chỉ có vách |
| `SRC-STRETCH-GLOVE-2024` (Nat. Commun.) | Cảm biến giãn lỏng-kim-loại → độ dài xương + góc khớp → FK; không camera/IMU | Như trên — pose reconstruction không IMU là một dòng nghiên cứu lớn |
| `SRC-CUSTOMGLOVE-REVIEW-2024` (arXiv:2405.15417) | Review 6 dòng: flex / gia tốc / vision / Hall / stretch / từ; flex ≈ 2× IMU về số bài; flex chỉ 1 DoF, có **inter-joint crosstalk**, cần hiệu chuẩn | Dùng để viết đoạn "vì sao chọn vách + áp điện trở" và **tự khai hạn chế** crosstalk/calibration của ta |
| `SRC-FUNCASSESS-2016` (Measurement) | Bend + force sensor, "hand function assessment"; sai số góc ±6°, ICC 0.956–0.988 | Tiền lệ trực tiếp cho framing "găng = công cụ **đánh giá**"; MAE ≤ 15° (GATE B) là **chuẩn thấp** so với ±6° → phải giải thích tại ta chọn ngưỡng đó (proof-of-concept trên phantom) |

⇒ **Cách phát biểu B an toàn và còn sống:** "*dấu* của chuyển động gập/duỗi được suy ra **chỉ** từ mẫu kích hoạt trên các vách có kéo trước của một khung cứng — không encoder, không IMU, không camera — và được kiểm chứng chống lại góc đặt trước trên phantom."

### 2.3 Ứng viên C — "longitudinal tại nhà + tự biết khi dữ liệu không đáng tin"

| Nguồn | Nội dung | Mức đe dọa |
|---|---|---|
| `SRC-LOWCOST-GLOVE-2006` (J. Neurosci. Methods, "Shadow Monitor") | **Găng giá rẻ cho "extended monitoring and functional hand assessment"** đã có từ 2006 | **Cao nhất** cho C. Phải đọc toàn văn; nếu họ đã làm extended + assessment → C chỉ còn khác ở (i) đối tượng đột quỵ tại nhà + dashboard KTV, (ii) tự kiểm tra độ tin cậy, (iii) lực hướng |
| `SRC-MULTITOUCH-APP-2021` (J. NeuroEng. Rehabil., n=88) | App đánh giá độ khéo/lực nắm **trên tablet**: hội tụ với FMA-UE/JTT/BBT/NHPT, ICC, SEM, **MDC** đã tính, độ nhạy theo mức liệt | Làm **yếu** câu "chưa có công cụ rẻ dùng tại nhà nào cho dữ liệu định lượng". Vẫn khác: không đo lực cơ học, cần tablet, không đo trong bài tập tại nhà |
| `SRC-MANUMETER-RCT-2022` (Sensors 22(18):6938, n=20, 3 tuần) | Đeo tại nhà + phản hồi thời gian thực; **MDC ≈ 31%** mức dùng tay trung bình ngày; false-positive 100–200 count/h; không cải thiện lâm sàng sau 3 tuần | Vừa là prior art vừa là **chuẩn thống kê phải đối chiếu** ở GATE C/D |
| `SRC-STEF-MDC-2026` (Top Stroke Rehabil, n=53) | STEF: ICC 0,98; **MDC95 = 12,7 điểm**; MIC neo 7,9–16,6; theo COSMIN | **Thay thế** con số "MDC của ARAT ~4 điểm" (vẫn UNVERIFIED) làm mốc tham chiếu |
| `SRC-VNM-HS-GLove-2026`, `SRC-VNM-ANNAM-2022`, `SRC-VNM-TL-GLOVE-2026` | Trong nước: găng "AI + cảm biến lực/áp suất khí, theo dõi tiến độ phục hồi" (HS Lâm Đồng, giải nhất cấp tỉnh 2026); găng mềm PneuNet (Bách khoa Đà Nẵng); găng robot + theo dõi từ xa (Thủy lợi, 09/2026) | Đều là **máy tập/hỗ trợ chủ động**, không phải thiết bị đánh giá có kiểm chứng độ tin cậy. Nhưng chúng là **hàng xóm gần nhất ở đúng sân chơi học sinh** → phải nêu trong "bất cập của giải pháp hiện tại" |

**Kết luận C:** khoảng trống **còn sống**, nhưng chỉ ở giao điểm hẹp: *chỉ số chức năng bàn tay từ lực hướng + khung thống kê MDC/ICC + cờ từ chối kết luận, dùng được tại nhà giữa hai lần tái khám*. Mọi câu dạng "hệ thống đầu tiên theo dõi tại nhà" → **cấm** (đã có Shadow Monitor 2006, Manumeter, app 2021).

### 2.4 Ứng viên D — chi phí

Cần bảng so **giá có thật**, không nói "giá thấp". Mốc hiện có: PPS TactileGlove II (65 phần tử, linearity >98%, min 0.04 N — thông số **nhà sản xuất tự công bố**, không phải kết quả đo độc lập) (`SRC-TACTILEGLOVE-II`); VMG30/CyberGlove (`SRC-VMG30-APPLSCI-2023`); nhóm AnNam tự khai ~4,5–5 triệu VNĐ cho nguyên mẫu (`SRC-VNM-ANNAM-2022`). Việc phải làm: nhập giá thực tế từng mục BOM + một giá tham chiếu cho từng thiết bị so sánh, ghi vào `research/evidence/` kèm provenance.

---

## 3. Việc **bắt buộc** trước khi được phép coi Gap 1 (prior art) là "hoàn tất"

1. ☐ Đọc **toàn văn** và ghi trang/bảng cho 5 nguồn hệ trọng: `SRC-ARTGLOVE-2026`, `SRC-SIDEWALL-PIEZO-2015`, `SRC-GRATING-GLOVE-2021`, `SRC-LOWCOST-GLOVE-2006`, `SRC-MANUMETER-RCT-2022`. (Hiện mới ở mức abstract → kết luận trên là **tạm thời**.)
2. ☐ **Tra cứu bằng sáng chế tử tế** — lượt vừa rồi chỉ là 1 truy vấn qua web search, chưa đủ để kết luận. Phải tra Google Patents/Espacenet theo IPC **A61B5/11**, **A61B5/22**, **A61B5/10**, **G01L1/14**, **A61H1/02** với từ khóa `rigid shell / cage / wall / abutment` + `piezoresistive / flexible pressure` + `finger joint` + `kinematics`. Ghi mỗi truy vấn + tổ hợp từ khóa vào `QUERY_LOG`.
3. ☐ Kiểm tra đề tài dự thi trong nước (ViSEF vòng quốc gia 2024–2026, Nafosted, luận văn VN) cho cả từ khóa "găng tay + đột quỵ" và "găng tay + phục hồi chức năng" — `SRC-VNM-*` mới là **bài báo chí**, chưa phải báo cáo khoa học.
4. ☐ Chạy lane **R5 (Novelty challenger)** độc lập theo `research/protocols/ISEF_REVIEW_ORCHESTRATION.md`, đưa file này + `docs/03` §5 làm packet đóng băng; **chỉ khi R5 xác nhận** mới cập nhật `docs/01` §4 thành mức novelty chốt.
5. ☐ Chủ dự án quyết định **DEC-NOV-001** (xem `DECISION_LOG.md`): chấp nhận hạ A / nâng C hay giữ nguyên và chịu rủi ro.

6. ☐ **Chưa có nguồn mới nào được đọc toàn văn.** 24 dòng mới vào ledger gồm 20 `READ_ABSTRACT` + 4 `UNVERIFIED` (`SRC-INTERLOCKED-MICRODOME-2014`, `SRC-SAFE-GLOVE-2015`, `SRC-TACTILEGLOVE-II`, `SRC-VNM-TL-GLOVE-2026` — mới thấy snippet tìm kiếm). Bốn dòng `UNVERIFIED` **không** được trích trong báo cáo cho tới khi xác minh; các dòng `READ_ABSTRACT` chỉ được dùng cho đúng những gì abstract nói.

## 4. Điều **không** thay đổi (đã được kiểm tra và vẫn đúng)

- `docs/01` §10.2, §10.3: cấm "thay thế FMA/ARAT", cấm nói "đo chính xác" khi chưa hiệu chuẩn — vẫn là kỷ luật đúng.
- Cặp đối xứng + ô tham chiếu: `CLM-NOV-004` giữ nguyên giá trị — bằng chứng ngày càng rõ (dummy-gauge 1997; open-pad 2 bên 2020) rằng đây **không phải** điểm mới.
- Toàn bộ GATE 0–F vẫn bench/phantom, không cần IRB; và GATE A/B càng trở nên quan trọng vì novelty A đã bị thu hẹp → nếu GATE A fail thì đề tài mất luôn phần lập luận cơ chế còn lại.
- Định vị "thiết bị **đánh giá & theo dõi**, không phải máy tập" càng có giá trị sau lượt rà soát: **toàn bộ** đối thủ trong nước (3/3) đều là máy tập.

---

## 5. Hai mức "an toàn" khác nhau — đừng nhầm (bổ sung 2026-09-19, sau phản hồi của chủ dự án)

Lượt rà soát này áp **chuẩn trích dẫn của bài báo** cho toàn bộ 4 ứng viên. Điều đó đúng ở một chỗ và **không** đúng ở chỗ khác:

| Việc | Mức áp dụng | Hệ quả thực hành |
|---|---|---|
| Viết phần **Cơ sở lý thuyết / Differentiation / Table so sánh** trong hồ sơ KHKT | **chuẩn journal** (mức em đã dùng ở §1–§4) | bắt buộc trích sidewall 2015, ART-Glove 2026, grating 2021…; cấm viết "chưa ai làm"; giữ nguyên kết luận hạ bậc A |
| Quyết định **có được làm tính năng đó không** | **chuẩn hội thi** | prior art **không** cấm mình làm; nó chỉ buộc mình nói rõ mình khác ở đâu. Chứng cứ: `SRC-ISEF-2025-ROBO065T` — dự án giải Tư ISEF 2025 (THPT thị xã Quảng Trị) cấu tạo 100% từ đồ có sẵn (YOLO11 + Nav2 + SLAM Toolbox + Gemma2 + Telegram), claim "first fully integrated … for ALS patients", và thắng bằng **4 con số tự đo** (97,11% / 0,12 m / 93,33% / < 5,33 s) |

⇒ Kết luận §0 của file này **giữ nguyên về mặt trích dẫn**, nhưng đổi một câu: "hạ bậc novelty" nghĩa là *bỏ chữ "đầu tiên/nguyên lý mới"*, **không** nghĩa là *bỏ tính năng*. Hồ sơ xử lý đề xuất AAT ghi chi tiết ở `2026-09-19_active_assisted_scope_options.md` §11–§13.

---

## 6. Kết quả đọc toàn văn/đối chiếu (2026-09-19, lượt 2) — 3 lỗi danh tính đã bắt ra

| Nguồn | Lỗi trong repo | Đã sửa thành | Cách sửa |
|---|---|---|---|
| `SRC-RECONFIG-GLOVE-2023` | trang "217–232" (tranh cãi) + nghi "Science China" | **Engineering 32 (Jan 2024): 202–216**, PII S2095809923000978, OA CC BY-NC-ND | đối chiếu trang tạp chí ScienceDirect qua DOI |
| `SRC-IRONHAND-2018` | gán nhầm "J NeuroEng Rehabil 2018" | **Radder et al., J Rehabil Assist Technol Eng 2016;3:2055668316670553**, DOI 10.1177/2055668316670553 (PMC6453057); id giữ nguyên để không tạo tham chiếu treo | đọc PMC (chunk 0 + 2/7): Methods + Data analysis |
| `SRC-TW201533608A-PRESSUREGLOVE` | chỉ có snippet | xác nhận **Abandoned**; ghi CPC thật (G01L1/20, 1/22, 1/205, G01L5/009, G01P15/00) | đọc trang Google Patents |

Phát hiện mới làm thay đổi bang differentiate cua de tai:

- `SRC-TW-SPASTICITY-2022` (Sensors 22(19):7212) — **đối thủ trực tiếp** của ý tưởng "tách co cứng khỏi nỗ lực chủ động": 19 IMU + 1 bóng áp lực, n = 14, >1000 đặc trưng, MAS làm tham chiếu, IRB 11002-007, claim "first study … finger spasticity and voluntary movement". Phải trích ở cả 2 vai (bằng chứng khả thi + prior art).
- `SRC-CN116954366A-ARRAYGLOVE` — 20 phần tử áp trở tại 14 khớp + 6 lòng bàn tay, **có nêu "theo dõi phục hồi chức năng" làm ứng dụng**, phân loại G06F3/014 → khoảng cách còn lại của ta chỉ còn: *vách khung cứng có preload + suy luận hướng + khung MDC/ICC + cờ UNRELIABLE + RAL bằng tải cơ khí*.
- Kết luận về **mức novelty A/C/D: không đổi** so với §0; thay đổi duy nhất là cách nói: ở tầng hội thi, "đã có người làm" buộc ta **trích dẫn + chỉ rõ chỗ khác**, không buộc ta **bỏ tính năng** (xem `research/reviews/2026-09-19_active_assisted_scope_options.md` §5 và §11).
- **Phát hiện thứ 4 (conflation):** cụm "ironHand" là **≥2 bài** — JRATE 2016 (chức năng trợ giúp ADL, cái ta đã đọc) và *J Rehabil Med* 2018;50:598–606 (HandinMind, n = 5, 2 phiên, SUS + IMI + thời gian nhiệm vụ, "ease of use should be improved further"). Đã thêm `SRC-IRONHAND-JRM-2018` vào ledger và ghi cảnh báo vào `SRC-IRONHAND-2018`. Hệ quả cho hồ sơ: bảng A.1/A.7 không được ghi "ironHand (JNER 2018)" nữa.
- **Phát hiện thứ 4 (conflation):** cụm "ironHand" là **≥2 bài** — JRATE 2016 (chức năng trợ giúp ADL, cái ta đã đọc) và *J Rehabil Med* 2018;50:598–606 (HandinMind, n = 5, 2 phiên, SUS + IMI + thời gian nhiệm vụ, "ease of use should be improved further"). Đã thêm `SRC-IRONHAND-JRM-2018` vào ledger và ghi cảnh báo vào `SRC-IRONHAND-2018`. Hệ quả cho hồ sơ: bảng A.1/A.7 không được ghi "ironHand (JNER 2018)" nữa.
- **Phát hiện thứ 4 (conflation):** cụm "ironHand" là **≥2 bài** — JRATE 2016 (chức năng trợ giúp ADL, cái ta đã đọc) và *J Rehabil Med* 2018;50:598–606 (HandinMind, n = 5, 2 phiên, SUS + IMI + thời gian nhiệm vụ, "ease of use should be improved further"). Đã thêm `SRC-IRONHAND-JRM-2018` vào ledger và ghi cảnh báo vào `SRC-IRONHAND-2018`. Hệ quả cho hồ sơ: bảng A.1/A.7 không được ghi "ironHand (JNER 2018)" nữa.
- Tự do vận hành (freedom-to-operate): **vẫn UNVERIFIED** — xem `docs/03` §7 để biết tại sao tra theo phân loại không làm được ở đây và cần công cụ gì.
