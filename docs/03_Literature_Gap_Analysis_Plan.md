# 03 — Kế hoạch phân tích khoảng trống nghiên cứu (2011–2026)

> **Ngày:** 2026-09-19 (lượt rà soát 1) · **Trạng thái:** **ĐÃ CHẠY LƯỢT ĐẦU — CHƯA HOÀN TẤT.**
> Kết quả lượt 1: `research/reviews/2026-09-19_prior_art_novelty_gate1.md` (ma trận §5 đã điền, 24 nguồn mới vào ledger, 3 nguồn `UNVERIFIED` đã xác minh danh tính thư mục).
> **Chưa hoàn tất** vì: (i) cả 24 nguồn mới đều chưa đọc toàn văn (20 `READ_ABSTRACT`, 4 `UNVERIFIED` = mới thấy snippet); (ii) tra bằng sáng chế mới ở mức 1 truy vấn, **chưa** tra theo IPC; (iii) chưa có lane R5 độc lập adjudicate.
> **Lệnh cấm vẫn còn hiệu lực:** chưa được viết bất kỳ câu nào khẳng định "chưa có ai làm".
> **Nguyên tắc chống ảo giác:** "không tìm thấy trong một truy vấn" chỉ cho phép ghi `UNVERIFIED`, **không** chứng minh "chưa có ai làm". Một nguồn chỉ vào `research/evidence/SOURCE_LEDGER.csv` sau khi đã xác minh tiêu đề/tác giả/venue/năm/DOI/URL **và** đọc được đoạn văn hỗ trợ đúng claim.

---

## 1. Mục tiêu

Xác định **mức prior art** của 4 ứng viên novelty của đề tài găng tay, theo thứ tự quan trọng:

| Ưu tiên | Ứng viên novelty | Câu hỏi prior-art cần trả lời |

|---|---|---|
| **A (cao nhất)** | Cảm biến **hướng** qua vách khung cứng: dùng áp lực lên vách cơ khí để mã hóa **hướng chuyển động của lóng ngón**, không dùng IMU | Đã có ai dùng khung cứng + piezoresistive để suy hướng khớp chưa? Bằng sáng chế nào? |
| **B** | Suy luận hướng khớp từ trường lực rời rạc → **tái tạo bàn tay 3D** không cần IMU | Có công bố nào tái tạo pose không dùng IMU/camera? Sai số bao nhiêu? |
| **C** | **Longitudinal monitoring** chức năng bàn tay tại nhà giữa các lần tái khám, có **tự kiểm tra độ tin cậy** | Đã có hệ thống nào theo dõi bàn tay tại nhà theo tuần và tự báo "dữ liệu không đáng tin"? |
| **D** | Hạ chi phí so với dynamometer/E-Link bằng vật liệu piezoresistive giá rẻ | Ngưỡng giá của các giải pháp hiện có; có sản phẩm thương mại nào < 50 USD? |

**Điều kiện để A được xem là "chưa bị chiếm":** phải tìm và đọc được công bố/sáng chế gần nhất theo cùng nguyên lý, rồi chỉ ra được **khác biệt cụ thể**, không phải chỉ "khác về ứng dụng".

---

## 2. Mười nhóm chủ đề tìm kiếm

| # | Nhóm | Truy vấn gợi ý (tiếng Anh) | Trạng thái |
|---|---|---|---|
| 1 | Găng tay cảm biến cho phục hồi chức năng | `smart glove stroke rehabilitation hand function monitoring` · `data glove piezoresistive hand therapy` | ĐÃ LÀM MỘT PHẦN — `SRC-SMARTGLOVE-REVIEW-2026` (đã verify), `SRC-CUSTOMGLOVE-REVIEW-2024`, `SRC-VMG30-APPLSCI-2023`. Chưa rà hết dòng găng PHCN thương mại. |
| 2 | Đo **hướng** lực / mô-men bằng vật liệu áp điện trở | `directional force sensing piezoresistive glove` · `shear force glove sensor` | ĐÃ LÀM — KẾT QUẢ BẤT LỢI: nguyên lý vách + piezoresistive suy ra hướng đã có từ 2014-2015 (`SRC-SIDEWALL-PIEZO-2015`, `SRC-INTERLOCKED-MICRODOME-2014`). Phải đọc toàn văn. |
| 3 | Tái tạo pose bàn tay không dùng camera/IMU | `hand pose reconstruction without IMU` · `glove kinematic reconstruction force sensor` | ĐÃ LÀM MỘT PHẦN — đã có găng suy pose không IMU bằng dải cách tử/quang (`SRC-GRATING-GLOVE-2021`) và cảm biến giãn (`SRC-STRETCH-GLOVE-2024`). "Không dùng IMU" không còn là novelty tự thân. |
| 4 | Khung cứng / exoskeleton mềm và cảm biến tích hợp | `rigid exoskeleton frame finger force sensing` · `finger segment displacement sensor` | ĐÃ LÀM — KẾT QUẢ BẤT LỢI: ART-Glove 2026 = vỏ cứng khớp nối + 16 bề mặt chức năng phủ da áp điện trở (`SRC-ARTGLOVE-2026`), nhưng đo góc bằng encoder. Prior art phần cứng gần nhất; phải đọc toàn văn. |
| 5 | Theo dõi tại nhà sau đột quỵ | `home monitoring upper limb stroke wearable longitudinal` | ĐÃ LÀM MỘT PHẦN — `SRC-LOWCOST-GLOVE-2006` (extended monitoring + functional hand assessment, 2006), `SRC-MANUMETER-RCT-2022`, `SRC-MULTITOUCH-APP-2021`. Khoảng trống C chỉ còn ở giao điểm hẹp (review §2.3). |
| 6 | Thang đo lâm sàng & MDC | `Fugl-Meyer ARAT minimal detectable change upper extremity` | ĐÃ LÀM MỘT PHẦN — đã xác minh `SRC-STEF-MDC-2026` (ICC 0,98; MDC95 = 12,7 điểm; n=53). "MDC của ARAT ~4 điểm" VẪN UNVERIFIED. |
| 7 | Lực ngón và chức năng | `finger force grip pinch correlation Fugl-Meyer` | CÒN NỢ — `SRC-RCT-FORCEHAND-2024`, `SRC-FINGERUSE-2023` mới READ_ABSTRACT; chưa trích được số tương quan nào. |
| 8 | Đặc tính vật liệu Velostat | `Velostat characterization hysteresis creep drift pressure sensor` | CHƯA LÀM LẠI — và ĐÂY LÀ CHỐT CHỐT của mô hình docs/02 §5.5 (cần γ, R(p), R_max(ADC+MUX) để mở/đóng cửa sổ preload) — `SRC-HOPKINS-2020-VELOSTAT-SOCKET` và `SRC-HOPKINS-2020-IEEEJS` là hai dòng của cùng một bài (phải gộp); số liệu hysteresis/creep phải lấy từ bản gốc. |
| 9 | Tự kiểm tra/hiệu chuẩn cảm biến | `sensor self-validation reference cell drift compensation` · `self-calibration piezoresistive` | ĐÃ LÀM MỘT PHẦN — thêm bằng chứng đọc hai bên để tách thành phần đã có tiền lệ (`SRC-OPENPAD-FINGER-2020`) → càng không được claim cặp đối xứng là mới. |
| 10 | Edge-AI cho thiết bị đeo y tế | `INT8 quantization wearable healthcare NPU on-device inference` | CHƯA LÀM — cần một lượt riêng cho RKNN/INT8 trên RK3588 và các công bố wearable INT8 y tế. |
| 11 | Bằng sáng chế liên quan | `patent glove force sensor hand rehabilitation monitoring` (Google Patents, WIPO, USPTO) **+ (mới 2026-10-12, nhóm nghiên cứu đề xuất) module "Thông tin Sở hữu công nghiệp" của `sti.gov.vn`** (Sáng chế/Kiểu dáng/Nhãn hiệu/Giải pháp hữu ích, 821.046 bản ghi, Bộ KH&CN/NASATI) — phủ riêng không gian đăng ký SHTT trong nước mà Espacenet/WIPO không chắc đã lập chỉ mục đầy đủ (đặc biệt "Giải pháp hữu ích" là loại hình riêng của Việt Nam) | ĐÃ ĐỌC 2 HỒ SƠ (2026-09-19): US20150233779A1 **Abandoned**; CN116954366A **Pending** (SEU, 20 phan tu ap tro). CHƯA HOÀN TẤT: tra cứu theo phân loại qua Google Patents XHR **bất khả thi trong môi trường này** (xem §7). → cần Espacenet CQL / Lens / PatentsView với tài khoản. `SRC-TW201533608A-PRESSUREGLOVE`, `SRC-CN116954366A-ARRAYGLOVE`. **sti.gov.vn đã thử 2026-10-12 — xem §7b: không tra được theo từ khoá từ môi trường này (SPA), chưa tìm thấy bản ghi liên quan đề tài qua `site:` search, và phát hiện dấu hiệu dữ liệu demo/placeholder trong danh sách mặc định — cần người thật tự tra trực tiếp trên trình duyệt + đối chiếu ipvietnam.gov.vn trước khi dùng bất kỳ kết quả nào làm bằng chứng.** |
| 12 | Đề tài trong nước đã có | `đồ án găng tay cảm biến phục hồi chức năng` · các đề tài ViSEF/ISEF/thi KHKT đã đạt giải **+ (mới 2026-10-12) module "Công bố khoa học và trích dẫn" của `sti.gov.vn`** (655.699 bản ghi công bố trong nước, có trích dẫn) và "Nhiệm vụ KH&CN" (47.794 bản ghi đề tài/nhiệm vụ cấp bộ/tỉnh) | ĐÃ PHÁT HIỆN RỦI RO — 3 hàng xóm trong nước đều là máy tập: `SRC-VNM-HS-GLove-2026` (HS Lâm Đồng, giải nhất cấp tỉnh 2026 — gần nhất về mức học sinh), `SRC-VNM-ANNAM-2022`, `SRC-VNM-TL-GLOVE-2026`. Mới có báo chí, chưa có báo cáo gốc. **sti.gov.vn chưa tra được bằng từ khoá tự động (xem §7b) — nếu nhóm nghiên cứu tự vào trình duyệt tra trực tiếp (giao diện JS hoạt động bình thường cho người dùng thật), có thể tìm được báo cáo/đề tài gốc của 3 hàng xóm trên hoặc đề tài trong nước khác chưa phát hiện.** |
| 13 | **Găng tập có trợ lực / AAN / an toàn khi co cứng** (mở rộng theo đề xuất 2026-09-19) | `assist-as-needed soft robotic glove EMG stroke` · `intention detection hand exoskeleton safety torque limit` · `spasticity velocity-dependent resistance robotic assessment` | ĐÃ LÀM MỘT PHẦN (lượt 1) — 16 dòng vào ledger; kết quả: **hướng này KHÔNG còn trống** (`SRC-IRONHAND-2018`, `SRC-AAN-EMG-2024`, `SRC-THUMB-AAN-2026`) + trùng 2 dự án VN. Bắt buộc đọc toàn văn 4 bài nền + tra IPC `A61H1/02`, `A61H3/01` trước khi nhóm nghiên cứu chốt `DEC-SCOPE-002` |

---

## 3. Nguồn gốc đã có (từ giai đoạn trước — phải đọc lại toàn văn)

Các tài liệu dưới đây đã **gặp trong quá trình tra cứu** nhưng chưa được đưa vào `SOURCE_LEDGER.csv` với trạng thái `READ_FULL`. Trước khi trích dẫn, phải đọc toàn văn và ghi lại số trang/bảng số cụ thể.

- Systematic review: *AI-based smart glove for hand movement recognition and rehabilitation monitoring* (Springer, 2026 — 101 bài 2011–2025). (cần xác minh) lại tạp chí, số, DOI.
- *Wearable technology to capture arm use of stroke survivors in home and community settings* (medRxiv 2023 / PMC9901039).
- *Tracking Upper Limb Motion via Wearable Solutions* — systematic review (JMIR 2024).
- *Occupational Therapy at Home E-Rehabilitation (OTHER)* — DOI 10.1080/09638288.2026.2643929, PMID 41918405.
- Amin K.R. et al., *Remote Monitoring for the Management of Spasticity: Challenges, Opportunities and Proposed Technological Solution* — IEEE OJEMB, early access 30/12/2024, DOI 10.1109/OJEMB.2024.3523442. (Lưu ý: đối tượng là **spasticity**, không phải trực tiếp chức năng bàn tay → chỉ dùng để chứng minh **khoảng trống chung** về theo dõi giữa các lần tái khám.)
- Zhu lab (UCLA), *A Glove-based System for Studying Hand-Object Manipulation* (IROS 2017) — 15 IMU + 6 cảm biến Velostat lực tiếp xúc. **Prior art gần nhất, phải differentiate rõ.**
- *A Reconfigurable Data Glove for Reconstructing Physical and Virtual Grasps* (2023) — mạng IMU + Velostat.
- *Development of an Instrumented Glove for Palmar Pressure Assessment in Kayakers* (Sensors 2026) — Velostat trong găng, bối cảnh thể thao.
- *Design of a flexible data glove for gesture recognition* (2025) — mảng piezoresistive 5×4, nhận dạng cử chỉ.
- Hopkins M. et al., đặc tính Velostat — IEEE Sensors Journal 2020 ((cần xác minh) lại tên bài/DOI).
- *Effect of task-oriented training assisted by force feedback hand rehabilitation robot on finger grasping function in stroke patients with hemiplegia* (2024, PMC11092254) — RCT, cho thấy lực bóp/AROM/FMA-Hand/ARAT cải thiện; dùng làm bằng chứng **lực ngón có ý nghĩa lâm sàng**.
- *Quantitative measurement of finger usage in stroke hemiplegia using ring-shaped wearable devices* (2023, PMC10242812) — tỷ lệ sử dụng ngón tương quan với FMA-UE/ARAT/STEF.

---

## 4. Quy trình thực hiện

1. Với mỗi nhóm chủ đề, chạy tối thiểu **3 truy vấn khác cách diễn đạt** (thuật ngữ chuyên ngành, thuật ngữ thương mại, thuật ngữ bằng sáng chế).
2. Log mọi truy vấn vào `research/queries/QUERY_LOG.jsonl` bằng `scripts/research_log.py` (kèm mục đích và kết luận đạt/không đạt).
3. Chỉ ghi nguồn vào `SOURCE_LEDGER.csv` khi đã xác minh **tiêu đề + tác giả + venue + năm + DOI/URL** và **đoạn văn hỗ trợ đúng claim**.
4. Điền vào **ma trận theo dõi** dưới đây, mỗi dòng một công bố/sáng chế.
5. Kết thúc: viết một đoạn **"prior art gần nhất và khác biệt cụ thể"** cho từng ứng viên novelty. Nếu không tìm được khác biệt → **hạ mức novelty**, không được giữ nguyên câu claim.

> **Cập nhật 2026-09-19 (2):** Nhóm 13 được mở vì nhóm nghiên cứu đề xuất thêm hướng "tập chủ động có trợ lực". Kết quả + phương án xử lý: `research/reviews/2026-09-19_active_assisted_scope_options.md`. Trạng thái: PROPOSED — chờ `DEC-SCOPE-002`.

## 5. Ma trận theo dõi (điền dần)

Bản điền đầu tiên (lượt 1) nằm trong **`research/reviews/2026-09-19_prior_art_novelty_gate1.md` §2.1–§2.4**, đúng 9 cột của mẫu, gồm 14 công bố/bằng sáng chế/nguồn trong nước.

| ID | Nguồn | Loại | Đo gì | Cảm biến | Đối tượng | Theo dõi dọc? | Tự kiểm tra lỗi? | Khác biệt với đề tài |
|---|---|---|---|---|---|---|---|---|
| → xem file review §2 (không điền trùng ở đây để tránh hai bản lệch nhau) | | | | | | | | |

## 6. Ngưỡng ra quyết định

- Nếu tìm thấy **một công bố hoặc bằng sáng chế đã làm đúng** "khung cứng + piezoresistive → suy hướng khớp + tái tạo 3D": **hạ novelty A xuống mức "cải tiến"**, dồn trọng tâm sang C (longitudinal + self-validation).
- Nếu tìm thấy hệ thống theo dõi bàn tay tại nhà theo tuần đã có sản phẩm: **hạ novelty C**, dồn sang A.
- Nếu **cả A và C đều bị chiếm**: dừng, báo thẳng, không viết báo cáo như thể còn mới.

### 6.1 — Áp dụng ngưỡng sau lượt rà soát 1 (2026-09-19)

| Nhánh | Điều kiện trong §6 | Đã xảy ra chưa | Hệ quả đang áp dụng |
|---|---|---|---|
| Hạ A | Có **một** công bố/patent làm **đúng** "khung cứng + piezoresistive → suy hướng khớp → tái tạo 3D" | [Không đạt] chưa (ART-Glove 2026 đúng vỏ cứng + da áp điện trở nhưng đo góc bằng encoder; chưa đọc toàn văn) | A bị **hạ một bậc**: từ "nguyên lý vật lý/cơ khí mới" → "cải tiến cấu hình + phương pháp lập luận", vì nguyên lý phần tử vách→hướng đã có từ 2014–2015. Chưa rơi hẳn vào nhánh "dồn sang C". |
| Hạ C | Đã có **sản phẩm** theo dõi bàn tay tại nhà theo tuần | Lưu ý: một phần: nguyên mẫu học thuật từ 2006 + app đã chuẩn hóa MDC (2021); chưa thấy sản phẩm thương mại cho PHCN đột quỵ tại nhà | Chưa kích hoạt. Nhưng **cấm** mọi câu "hệ thống đầu tiên theo dõi tại nhà". |
| Dừng | **Cả** A và C đều bị chiếm | [Không đạt] | Tiếp tục. GATE A và GATE C vẫn là hai cổng quyết định. |

**Bản novelty — ĐÃ CHỐT bởi nhóm nghiên cứu (`DEC-NOV-001`, 2026-10-11)**, bổ sung bằng chứng lượt 2 (`research/reviews/2026-10-11_prior_art_novelty_velostat_AAN.md`); lane R5 độc lập + tra IPC có hệ thống **vẫn còn nợ**:

- **A** = cải tiến cấu hình + cách lập luận hướng khớp; bắt buộc trích `SRC-SIDEWALL-PIEZO-2015`, `SRC-INTERLOCKED-MICRODOME-2014`, `SRC-ARTGLOVE-2026`, `SRC-CN116954366A-ARRAYGLOVE`.
- **B** = phát biểu lại: "dấu gập/duỗi suy ra **chỉ** từ mẫu kích hoạt trên vách có preload — không encoder, không IMU, không camera".
- **C** = **ứng viên chính**, giới hạn trong giao điểm hẹp: lực hướng + khung MDC/ICC + cờ từ chối kết luận, dùng tại nhà giữa hai lần tái khám.
- **D** = chỉ được nói "rẻ hơn" khi có bảng giá BOM thật so với `SRC-TACTILEGLOVE-II` / Jamar / E-Link.

## 7. Kiểm soát bằng sáng chế — phương pháp đã dùng, thất bại đã gặp, lối thoát (2026-09-19)

**Đã làm (thật):** đọc trang Google Patents của 2 hồ sơ và ghi lại **CPC thực tế** của chúng:

| Hồ sơ | Trạng thái pháp lý | CPC được gán |
|---|---|---|
| `US20150233779A1` / `TW201533608A` — "Gloves with pressure sensors" (Waltop International Corp) | **Abandoned** (không còn hiệu lực) | G01L1/20, G01L1/22, G01L1/205, G01L5/009, G01P15/00, G01C19/02 |
| `CN116954366A` — "Touch perception glove based on sensor array" (Đông Nam University) | **Pending** | **G06F3/014** (găng dữ liệu), A41D19/00 |

**Kết luận về phương pháp (quan trọng hơn kết luận về nội dung):** các bằng sáng chế "găng áp trở" được phân loại ở
**G06F3/014 / A41D19/00 / G01L1-20x**, chứ không nằm ở A61B5/A61H. → Bộ mã truy vấn cũ của file này
(A61B5/11, A61B5/22, A61B5/10, G01L1/14, A61H1/02, A61H3/01) là **thiếu**; phải thêm
`G06F3/014`, `A41D19/00`, `G01L1/20`, `G01L1/205`, `G01L5/009` rồi mới được nói đến "đã rà bằng sáng chế".

**Thất bại cần ghi lại để phiên sau khỏi làm lại:** trong môi trường làm việc này **không** truy vấn theo phân loại qua Google Patents được:
- `https://patents.google.com/xhr/query?url=q%3D…%26cpc%3DA61H3%2F01…` trả về `total_num_results: 0` ở 3 biến thể (có/không `status`, có/không `language`);
- một biến thể khác trả `HTTP 500`. Trong khi đó trang chi tiết từng bằng sáng chế (`/patent/<id>/en`) đọc bình thường.
→ Để hoàn tất tra cứu theo phân loại, cần **Espacenet CQL** (`cpc=(G06F3/014) and txt=(piezoresistive glove)`), **Lens.org** hoặc **PatentsView API** —
cả ba đều **cần tài khoản/API key**, không làm được trong phiên này. **Không** được viết "đã tra cứu IPC" trong bất kỳ tài liệu nộp nào cho tới khi một trong ba đường đó chạy xong.

**Hệ quả cho hồ sơ (nên nói thẳng, vì đây là điểm trung thực chứ không phải điểm yếu):** mục "kiểm soát bằng sáng chế" trong đề tài ở mức
*rà soát sơ bộ 2 hồ sơ gần nhất + ghi rõ giới hạn phương pháp*, không phải một cuộc tra cứu FTO đầy đủ.

## 7b. Thử nguồn mới `sti.gov.vn` (nhóm nghiên cứu đề xuất 2026-10-12) — kết quả thử nghiệm

**Nguồn:** `https://sti.gov.vn/` — "Hệ thống thông tin quốc gia về khoa học, công nghệ và đổi mới sáng tạo", do Bộ Khoa học và Công nghệ (NASATI) vận hành. Xác nhận là cổng **chính thức** (liên kết chéo với `mst.gov.vn`, Cổng Dịch vụ công Bộ KH&CN, VJOL, VISTA), gồm 9 module, hai module liên quan trực tiếp tới việc rà soát prior art còn nợ:

- **Thông tin Sở hữu công nghiệp** (`/so-huu-cong-nghiep`) — 821.046 bản ghi Sáng chế/Kiểu dáng/Nhãn hiệu/Giải pháp hữu ích đã nộp tại Việt Nam. Có tiềm năng bổ sung cho Espacenet/WIPO vì bao phủ riêng không gian đăng ký SHTT trong nước — đặc biệt "Giải pháp hữu ích" là một loại hình bảo hộ SHTT của Việt Nam, không chắc Espacenet/WIPO lập chỉ mục đầy đủ.
- **Công bố khoa học và trích dẫn** (`/publication`) — 655.699 bản ghi công bố trong nước, có kèm trích dẫn. Có tiềm năng tìm được báo cáo gốc của các đề tài trong nước ở hàng #12 (hiện mới chỉ có qua báo chí).

**Đã thử (2026-10-12), xem chi tiết từng truy vấn trong `research/queries/QUERY_LOG.jsonl`:**

1. `fetch_page` trực tiếp `/so-huu-cong-nghiep` và `/publication` kèm tham số từ khoá (`?keyword=`, `?search=`) — **THẤT BẠI**: trang là SPA (ứng dụng một trang chạy JavaScript phía client), ô tìm kiếm thật gọi API nội bộ qua JS, không phản hồi với tham số truyền trên URL theo cách `fetch_page` (chỉ đọc HTML server-render) có thể kích hoạt. Kết quả trả về luôn là danh sách mặc định mới nhất (449.963 / 821.046 bản ghi), không lọc được theo từ khoá.
2. `web_search` giới hạn `site:sti.gov.vn` kèm từ khoá liên quan đề tài (găng tay/cảm biến/sáng chế) — chạy được, nhưng **chưa tìm thấy bản ghi nào liên quan trực tiếp đề tài** tại thời điểm tra cứu. Theo đúng nguyên tắc chống ảo giác của dự án: đây là `UNVERIFIED` (không tìm thấy trong 1 lượt tra), **không** phải bằng chứng "chưa có ai đăng ký sáng chế tương tự ở Việt Nam".
3. **Lưu ý trung thực quan trọng:** trong danh sách mặc định của module Sở hữu công nghiệp, một số bản ghi có dấu hiệu là dữ liệu demo/placeholder — ví dụ "Thiết kế chai nước EcoBottle", "Máy lọc nước thông minh AquaPro" (chủ đơn ghi tên nước ngoài "Stefano Caffarri" gắn với một giải pháp hữu ích nộp tại Việt Nam), và một "Số bằng: PAT-VN-2026-9964" có định dạng không khớp cách đánh số thật của Cục Sở hữu trí tuệ Việt Nam. Nghi ngờ nền tảng (còn khá mới) vẫn lẫn dữ liệu thử nghiệm/demo trong CSDL công khai. **Hệ quả: không được coi bất kỳ bản ghi đơn lẻ nào lấy từ `sti.gov.vn` là bằng chứng đã xác minh cho đến khi đối chiếu chéo với nguồn gốc chính thức** — Cục Sở hữu trí tuệ (`ipvietnam.gov.vn`) cho sáng chế/kiểu dáng/nhãn hiệu/giải pháp hữu ích, hoặc tạp chí/trường đại học gốc cho công bố khoa học.

**Kết luận và cách dùng tiếp theo:**

- **CHẤP NHẬN** `sti.gov.vn` làm **kênh bổ sung** (không thay thế) cho hàng #11 và #12 ở bảng §2 — hữu ích nhất cho phần phủ sóng trong nước (Giải pháp hữu ích VN, công bố/đề tài trong nước) mà Espacenet/WIPO/Google Scholar quốc tế không mạnh.
- **KHÔNG đóng được** khoản nợ "tra bằng sáng chế theo IPC có hệ thống" của `DEC-NOV-001` — vì giao diện SPA của trang yêu cầu thao tác trực tiếp trên trình duyệt. Khoản nợ đó **vẫn cần** Espacenet CQL / Lens / PatentsView như đã ghi ở trên.
- **Khuyến nghị cho nhóm nghiên cứu:** giao diện tìm kiếm trên `sti.gov.vn` là ứng dụng đơn trang (SPA) tương tác động phía trình duyệt — nhóm nghiên cứu tra cứu trực tiếp bằng từ khoá tiếng Việt (`găng tay cảm biến`, `áp điện trở ngón tay`, `cảm biến áp lực phục hồi chức năng`) ở cả hai module trên để tìm báo cáo gốc của 3 đề tài trong nước đã phát hiện qua báo chí (hàng #12).
