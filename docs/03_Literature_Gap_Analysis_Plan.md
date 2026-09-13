# 03 — Kế hoạch phân tích khoảng trống nghiên cứu (2011–2026)

> **Ngày:** 2026-09-13 · **Trạng thái:** KẾ HOẠCH — **chưa hoàn tất rà soát**. Phải chạy xong **trước khi** viết bất kỳ câu nào khẳng định "chưa có ai làm".
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
| 1 | Găng tay cảm biến cho phục hồi chức năng | `smart glove stroke rehabilitation hand function monitoring` · `data glove piezoresistive hand therapy` | ☐ |
| 2 | Đo **hướng** lực / mô-men bằng vật liệu áp điện trở | `directional force sensing piezoresistive glove` · `shear force glove sensor` | ☐ |
| 3 | Tái tạo pose bàn tay không dùng camera/IMU | `hand pose reconstruction without IMU` · `glove kinematic reconstruction force sensor` | ☐ |
| 4 | Khung cứng / exoskeleton mềm và cảm biến tích hợp | `rigid exoskeleton frame finger force sensing` · `finger segment displacement sensor` | ☐ |
| 5 | Theo dõi tại nhà sau đột quỵ | `home monitoring upper limb stroke wearable longitudinal` | ☐ |
| 6 | Thang đo lâm sàng & MDC | `Fugl-Meyer ARAT minimal detectable change upper extremity` | ☐ |
| 7 | Lực ngón và chức năng | `finger force grip pinch correlation Fugl-Meyer` | ☐ |
| 8 | Đặc tính vật liệu Velostat | `Velostat characterization hysteresis creep drift pressure sensor` | ☐ |
| 9 | Tự kiểm tra/hiệu chuẩn cảm biến | `sensor self-validation reference cell drift compensation` · `self-calibration piezoresistive` | ☐ |
| 10 | Edge-AI cho thiết bị đeo y tế | `INT8 quantization wearable healthcare NPU on-device inference` | ☐ |
| 11 | Bằng sáng chế liên quan | `patent glove force sensor hand rehabilitation monitoring` (Google Patents, WIPO, USPTO) | ☐ |
| 12 | Đề tài trong nước đã có | `đồ án găng tay cảm biến phục hồi chức năng` · các đề tài ViSEF/ISEF/thi KHKT đã đạt giải | ☐ |

---

## 3. Nguồn gốc đã có (từ giai đoạn trước — phải đọc lại toàn văn)

Các tài liệu dưới đây đã **gặp trong quá trình tra cứu** nhưng chưa được đưa vào `SOURCE_LEDGER.csv` với trạng thái `READ_FULL`. Trước khi trích dẫn, phải đọc toàn văn và ghi lại số trang/bảng số cụ thể.

- Systematic review: *AI-based smart glove for hand movement recognition and rehabilitation monitoring* (Springer, 2026 — 101 bài 2011–2025). 🔵 xác minh lại tạp chí, số, DOI.
- *Wearable technology to capture arm use of stroke survivors in home and community settings* (medRxiv 2023 / PMC9901039).
- *Tracking Upper Limb Motion via Wearable Solutions* — systematic review (JMIR 2024).
- *Occupational Therapy at Home E-Rehabilitation (OTHER)* — DOI 10.1080/09638288.2026.2643929, PMID 41918405.
- Amin K.R. et al., *Remote Monitoring for the Management of Spasticity: Challenges, Opportunities and Proposed Technological Solution* — IEEE OJEMB, early access 30/12/2024, DOI 10.1109/OJEMB.2024.3523442. (Lưu ý: đối tượng là **spasticity**, không phải trực tiếp chức năng bàn tay → chỉ dùng để chứng minh **khoảng trống chung** về theo dõi giữa các lần tái khám.)
- Zhu lab (UCLA), *A Glove-based System for Studying Hand-Object Manipulation* (IROS 2017) — 15 IMU + 6 cảm biến Velostat lực tiếp xúc. **Prior art gần nhất, phải differentiate rõ.**
- *A Reconfigurable Data Glove for Reconstructing Physical and Virtual Grasps* (2023) — mạng IMU + Velostat.
- *Development of an Instrumented Glove for Palmar Pressure Assessment in Kayakers* (Sensors 2026) — Velostat trong găng, bối cảnh thể thao.
- *Design of a flexible data glove for gesture recognition* (2025) — mảng piezoresistive 5×4, nhận dạng cử chỉ.
- Hopkins M. et al., đặc tính Velostat — IEEE Sensors Journal 2020 (🔵 xác minh lại tên bài/DOI).
- *Effect of task-oriented training assisted by force feedback hand rehabilitation robot on finger grasping function in stroke patients with hemiplegia* (2024, PMC11092254) — RCT, cho thấy lực bóp/AROM/FMA-Hand/ARAT cải thiện; dùng làm bằng chứng **lực ngón có ý nghĩa lâm sàng**.
- *Quantitative measurement of finger usage in stroke hemiplegia using ring-shaped wearable devices* (2023, PMC10242812) — tỷ lệ sử dụng ngón tương quan với FMA-UE/ARAT/STEF.

---

## 4. Quy trình thực hiện

1. Với mỗi nhóm chủ đề, chạy tối thiểu **3 truy vấn khác cách diễn đạt** (thuật ngữ chuyên ngành, thuật ngữ thương mại, thuật ngữ bằng sáng chế).
2. Log mọi truy vấn vào `research/queries/QUERY_LOG.jsonl` bằng `scripts/research_log.py` (kèm mục đích và kết luận đạt/không đạt).
3. Chỉ ghi nguồn vào `SOURCE_LEDGER.csv` khi đã xác minh **tiêu đề + tác giả + venue + năm + DOI/URL** và **đoạn văn hỗ trợ đúng claim**.
4. Điền vào **ma trận theo dõi** dưới đây, mỗi dòng một công bố/sáng chế.
5. Kết thúc: viết một đoạn **"prior art gần nhất và khác biệt cụ thể"** cho từng ứng viên novelty. Nếu không tìm được khác biệt → **hạ mức novelty**, không được giữ nguyên câu claim.

## 5. Ma trận theo dõi (điền dần)

| ID | Nguồn | Loại | Đo gì | Cảm biến | Đối tượng | Theo dõi dọc? | Tự kiểm tra lỗi? | Khác biệt với đề tài |
|---|---|---|---|---|---|---|---|---|
| *chờ điền* | | | | | | | | |

## 6. Ngưỡng ra quyết định

- Nếu tìm thấy **một công bố hoặc bằng sáng chế đã làm đúng** "khung cứng + piezoresistive → suy hướng khớp + tái tạo 3D": **hạ novelty A xuống mức "cải tiến"**, dồn trọng tâm sang C (longitudinal + self-validation).
- Nếu tìm thấy hệ thống theo dõi bàn tay tại nhà theo tuần đã có sản phẩm: **hạ novelty C**, dồn sang A.
- Nếu **cả A và C đều bị chiếm**: dừng, báo thẳng, không viết báo cáo như thể còn mới.
