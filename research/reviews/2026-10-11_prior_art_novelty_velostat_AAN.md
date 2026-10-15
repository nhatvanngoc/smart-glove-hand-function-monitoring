# GAP 2 — Rà soát prior art / patent cho tổ hợp "Velostat + mảng vi sai hai vách + exoskeleton ngón tay + AAN"

> **Ngày:** 2026-10-11 · **Người thực hiện:** nhóm nghiên cứu
> **Lý do:** sau khi chốt `CLM-HW-005` (tổng hợp 5 trục lý do chọn Velostat làm trụ cột AAN, xem `docs/02_Theoretical_Foundation.md` §7.3 + §10 mục 8), nhóm nghiên cứu yêu cầu **tách riêng bước thứ hai**: "chạy research tìm bằng chứng novelty" cho đúng tổ hợp mà đề tài định claim — không dừng ở văn献 chung chung.
> **Quan hệ với tài liệu trước:** đây là **tiếp nối** của `research/reviews/2026-09-19_prior_art_novelty_gate1.md` (Ứng viên A/B/C/D), **không phải** một lượt rà soát độc lập từ đầu. Mọi kết luận của gate1 (đặc biệt bảng mục 0 và `CLM-NOV-003`/`CLM-NOV-004`) vẫn có hiệu lực; file này chỉ **bổ sung** bằng chứng mới tìm được cho đúng góc "Velostat" + "AAN" mà `CLM-HW-005` vừa nêu.
> **Cảnh báo bằng chứng (bắt buộc đọc):** đây là **web_search qua Google-indexed patent pages (Google Patents cơ bản) + bài báo học thuật**, **KHÔNG PHẢI** một lượt tra cứu bằng sáng chế có hệ thống qua Espacenet/WIPO Patentscope/USPTO advanced search theo mã IPC/CPC. Mục 2 trong danh sách "bắt buộc" của gate1 (tra IPC A61B5/11, A61B5/22, A61B5/10, G01L1/14, A61H1/02 một cách có hệ thống) **vẫn CHƯA hoàn thành**. Không kết luận nào dưới đây được phép trình bày như "đã xác nhận novelty" hay dùng câu "chưa ai làm".

---

## 0. Câu hỏi rà soát

Tổ hợp cụ thể đề tài muốn kiểm tra (xuất phát từ `CLM-HW-005` + kiến trúc vách trong `docs/04_Hardware_Architecture.md`):

> "Dùng vật liệu **Velostat** (áp điện trở carbon-polymer), bố trí thành **mảng vi sai hai vách có preload** (ví dụ lưng/lòng hoặc hai bên đối xứng một đốt ngón), gắn trên khung cứng của một **hand/finger exoskeleton**, để tách tín hiệu **lực chủ động của người dùng** khỏi lực co cứng/co-contraction, phục vụ điều khiển **Assist-As-Needed (AAN)**."

## 1. Phương pháp tìm kiếm thực hiện lượt này

| # | Truy vấn | Công cụ | Kết quả chính |
|---|---|---|---|
| 1 | `patent differential piezoresistive sensor array finger exoskeleton assist-as-needed stroke rehabilitation glove` | web_search | US 12,728,520 (EPFL); US11986033B2 (Virginia Tech); AU2018364613A1 (EPFL, họ bằng sáng chế dẫn chiếu Bioservo/GM/Kyushu/UT Austin) |
| 2 | `Velostat force sensitive resistor patent hand rehabilitation exoskeleton glove finger` | web_search | US20180335842A1; US20250255767A1 (differential **magnetometer**, không phải áp điện trở); US11141341B2; bài báo FAU (báo chí) |
| 3 | `patents.google.com/?q=(velostat) AND (glove OR exoskeleton OR finger)` | fetch_page (Google Patents) | **Không trả về kết quả bằng sáng chế nào khớp trực tiếp** — xem mục 3 (diễn giải thận trọng bên dưới) |
| 4 | `patent "differential" piezoresistive sensor pair dorsal palmar finger bending direction exoskeleton preload` | web_search | Bài báo Wiley 2026 (Zheng et al., differential piezoresistive cho **góc** khớp); WO2015095459A1 (UT Austin, "differential" theo nghĩa toán học/SEA, không phải cảm biến); US9261423B2 (load cell áp điện trở đa hướng, không phải glove) |
| 5 | `preloaded antagonistic piezoresistive sensor pair finger exoskeleton bidirectional force sensing patent "opposing" walls` | web_search | **Dickmann et al. 2021** (Frontiers Robot AI) — 2 cảm biến FSR đo lực hai chiều trong khung cứng một finger exoskeleton; bài Sensors 2015 (đã có trong ledger: `SRC-SIDEWALL-PIEZO-2015`) |
| 6 | `site:patents.google.com velostat` | web_search | **CA3048964A1** — Velostat dùng ở cấu hình "interdigitated hoặc opposing" (đối xứng/vi sai) cho đo huyết áp qua vòng cổ tay; 2 bằng sáng chế khác về Velostat không liên quan (dây đeo chống tĩnh điện, thảm sàn) |

## 2. Bằng chứng mới, xếp theo mức độ gần với tổ hợp cần kiểm tra

### 2.1 Gần nhất: `SRC-FINGER-EXO-BIDIR-FSR-DICKMANN-2021`

Dickmann T. et al., *"An Adaptive Mechatronic Exoskeleton for Force-Controlled Finger Rehabilitation"*, Front. Robot. AI 2021;8:716451 (PMC8514640). Dùng **2 cảm biến kiểu FSR** gắn trong một **khung cơ khí tuỳ biến (custom-built mechanical enclosure)** ở khớp để đo **lực hai chiều (bidirectional force)**, phục vụ điều khiển theo lực cho phục hồi chức năng (đối tượng CRPS). Đây là tiền lệ **gần nhất** tìm được tới nay cho ý tưởng "cặp cảm biến áp điện trở kiểu FSR đối xứng/vi sai đo lực trên khung cứng của một finger exoskeleton", dùng đúng luận cứ "FSR rẻ, dễ tích hợp hơn strain-gauge" mà `CLM-HW-005` cũng nêu.

**Khác biệt chưa loại trừ được** (vì mới đọc abstract/snippet, chưa đọc toàn văn Results): (a) không rõ vật liệu có phải Velostat (carbon-polymer film) hay FSR thương mại kiểu Interlink (polymer thick-film trên lưới ngón tay — nguyên lý tương tự nhưng cấu trúc vật lý khác); (b) không rõ bố trí "2 cảm biến" có đúng dạng "hai vách đối diện có preload bao quanh đốt ngón" như kiến trúc của đề tài hay là 2 cảm biến điểm đơn (point sensors) gắn ở hai vị trí khác nhau trên cơ cấu truyền động; (c) mục tiêu của họ là đo **lực tương tác actuator-khớp** để điều khiển lực hỗ trợ nói chung, không tường minh nói về tách **active effort vs. spasticity/co-contraction** như khung AAN của đề tài.

### 2.2 Liên quan nhưng khác mục đích: `SRC-DIFFPIEZO-ANGLE-ZHENG-2026`

Zheng H. et al., *"A Compact Multijoint Finger Motion Sensing Module for Flexible Exoskeleton Applications"*, Adv. Intell. Syst. 2026, DOI 10.1002/aisy.70497 (xuất bản 2026-08-25 — **cùng năm với đề tài**). Dùng **"differential piezoresistive sensing configuration"** + mạch khuếch đại bù offset để đo **góc khớp** (không phải lực) tại 8 vị trí khớp trên một flexible hand exoskeleton. Xác nhận: nguyên lý "đọc vi sai bằng phần tử áp điện trở gắn trên khung exoskeleton ngón tay" **vẫn là một hướng nghiên cứu đang hoạt động ngay trong 2026**, không chỉ có tiền lệ cũ 2014–2015 như gate1 đã ghi. Vì đối tượng đo là **động học (kinematics/góc)** chứ không phải **động lực học (kinetics/lực, AAN)**, nguồn này không trực tiếp phủ định tổ hợp của đề tài, nhưng **thu hẹp thêm** không gian còn lại để claim "đọc vi sai áp điện trở trên khung exoskeleton ngón tay" là mới ở tầng nguyên lý tín hiệu.

### 2.3 Khác lĩnh vực nhưng đúng vật liệu + đúng cấu hình: `SRC-PATENT-VELOSTAT-OPPOSING-CA3048964`

Bằng sáng chế CA3048964A1, *"Blood pressure measurement system using force resistive sensor array"*. Dùng **trực tiếp Velostat (và Linqstat)** làm nền áp điện trở, đặt cặp điện cực theo cấu hình **"interdigitated hoặc opposing"** (đối xứng/vi sai) để tạo mảng cảm biến lực cho một **vòng đeo cổ tay đo huyết áp** — không phải hand/finger exoskeleton, không phải AAN. Đây là bằng chứng quan trọng: **"Velostat + cấu hình đối xứng/vi sai"** tự nó **không phải ý tưởng mới** — đã có bằng sáng chế (dù khác lĩnh vực ứng dụng — đo huyết áp, không phải phục hồi chức năng bàn tay). Phân loại CPC: A61B5/021 (đo huyết áp), A61B5/68 (gắn trên cơ thể), G01L23/G01L9 (đo lực/áp suất) — **không trùng** với các mã IPC đề tài đã gắn cờ trong `docs/03` (G06F3/014, A41D19/00, G01L1/20).

### 2.4 Không tìm thấy

Truy vấn trực tiếp Google Patents cho `(velostat) AND (glove OR exoskeleton OR finger)` **không trả về bằng sáng chế nào khớp** (chỉ là diễn giải lại câu truy vấn, không có danh sách kết quả hiển thị qua `fetch_page`). Diễn giải thận trọng: đây **có thể** là tín hiệu "chưa có bằng sáng chế nào kết hợp đúng 2 từ khoá này", nhưng **cũng có thể** chỉ là do trang Google Patents cần JavaScript để hiển thị danh sách kết quả và `fetch_page` không render được — **không được coi là bằng chứng "không có patent"**, chỉ được coi là "công cụ tìm kiếm này không cho câu trả lời đáng tin ở đây", cần làm lại bằng giao diện tra cứu patent có hệ thống (xem mục 4).

## 3. Đối chiếu với kết luận gate1 (2026-09-19) — có đổi gì không?

**Không đổi kết luận cốt lõi**, chỉ **củng cố thêm bằng chứng** cho hướng đã chọn:

- `CLM-NOV-003` (nguyên lý "vách áp điện trở → suy hướng/lực" không còn là nguyên lý mới): **giữ nguyên CONFLICTED**, bổ sung 2 nguồn mới (Dickmann 2021 cho LỰC; Zheng 2026 cho GÓC) — càng củng cố rằng đây là một không gian thiết kế đã được nhiều nhóm độc lập khai thác (2014, 2015, 2020, 2021, 2026), không phải phát minh đơn lẻ của đề tài.
- `CLM-NOV-004` (đọc vi sai bằng cặp phần tử đối xứng không mới): **giữ nguyên SUPPORTED** (không mới), bổ sung Dickmann 2021 làm tiền lệ thứ 3 (sau dummy-gauge 1997 và open-pad 2020).
- **Phần còn sống** cho đề tài claim (như gate1 đã nêu): tổ hợp **vách có preload + đọc vi sai → lấy DẤU gập/duỗi KHÔNG IMU/encoder/camera**, cho mục đích theo dõi chức năng bàn tay sau đột quỵ tại nhà, **kèm khung thống kê MDC/ICC + cờ từ chối kết luận**. Chưa tìm thấy một nguồn nào (lượt này hay gate1) khớp **toàn bộ** tổ hợp này — nhưng quan trọng: **đây không phải vì tổ hợp "Velostat cho AAN"**, mà vì tổ hợp "đo chức năng bàn tay tại nhà + thống kê độ tin cậy" (Ứng viên C của gate1). **AAN riêng** (dùng lực đo được để trợ lực "vừa đủ") thì vật liệu + cấu hình cảm biến **không phải là chỗ còn trống** — phần "AAN" của thuật toán điều khiển (force-sharing, target-actual) mới là nơi cần so sánh kỹ hơn với Dickmann 2021 (người này cũng làm force-controlled rehab).

## 4. Việc còn thiếu trước khi được coi là "đã rà soát novelty" (bổ sung vào danh sách gate1 mục 3)

1. [ ] Đọc toàn văn `SRC-FINGER-EXO-BIDIR-FSR-DICKMANN-2021` (đặc biệt phần Methods/Hình 9 nói về "custom-built mechanical enclosure") để xác nhận có phải kiến trúc "hai vách đối diện + preload" hay không, và đối chiếu thuật toán điều khiển lực của họ với thuật toán AAN (force-sharing) của đề tài.
2. [ ] Tra cứu có hệ thống qua **Espacenet** hoặc **WIPO Patentscope** (không chỉ Google-indexed web_search) với tổ hợp từ khoá `velostat OR "piezoresistive film"` + `exoskeleton OR glove` + `finger OR hand` + mã IPC/CPC đã gắn cờ: `G06F3/014`, `A41D19/00`, `G01L1/20`, và bổ sung `A61H1/02` (thiết bị phục hồi chức năng chi trên), `A61B5/11` (đo chuyển động cơ thể).
3. [ ] Kiểm tra trạng thái pháp lý (legal status) của CA3048964A1 — pending/granted/abandoned — trước khi trích dẫn chính thức trong hồ sơ.
4. [ ] Đưa kết quả này vào lane R5 (Novelty challenger) cùng với gate1, theo đúng quy trình `research/protocols/ISEF_REVIEW_ORCHESTRATION.md`, trước khi nhóm nghiên cứu chốt `DEC-NOV-001`.

## 5. Kết luận ngắn (trung thực — để báo cáo cho nhóm nghiên cứu)

- **KHÔNG tìm thấy** một nguồn (bài báo hoặc bằng sáng chế) nào mô tả **chính xác** tổ hợp "Velostat + mảng vi sai hai vách có preload + hand/finger exoskeleton + điều khiển AAN tách lực chủ động/co-contraction" — tính tới lượt tìm kiếm này.
- **NHƯNG** từng thành phần của tổ hợp đó đều **đã có tiền lệ riêng lẻ**: Velostat trong cấu hình đối xứng/vi sai (CA3048964A1 — khác lĩnh vực: huyết áp); cặp cảm biến áp điện trở kiểu FSR đo lực hai chiều trên khung cứng finger exoskeleton (Dickmann 2021 — rất gần, chưa rõ chi tiết hình học); đọc vi sai áp điện trở trên flexible hand exoskeleton (Zheng 2026 — khác đại lượng đo, là góc chứ không phải lực).
- Đây là tình huống **novelty tổ hợp** (combination novelty) kinh điển: không có nguyên lý vật lý đơn lẻ nào mới, nhưng **có thể** (chưa chắc chắn, cần tra cứu sâu hơn) chưa ai ghép đúng các mảnh này lại cho đúng bài toán AAN ở phục hồi chức năng bàn tay sau đột quỵ.
- **Không được** dùng kết quả này để viết câu "chưa ai làm" hay "mới hoàn toàn" trong hồ sơ — chỉ được dùng để viết câu dạng "chưa tìm thấy công bố nào ghép đúng A+B+C+D cho đúng ứng dụng E" kèm trích dẫn đầy đủ, và phải nêu rõ giới hạn tìm kiếm (mục 4) mỗi khi dùng.
