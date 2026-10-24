# Nhật ký nghiên cứu bổ sung — 2026-10-20: ba quyết định của chủ dự án (PA-2 · M3 · ba tang) và bản Word rà soát

**Đề tài:** Nghiên cứu và phát triển găng tay hỗ trợ phục hồi chức năng sau đột quỵ cho vận động tinh *(tên làm việc, chưa chốt tên nộp cuối cùng — `DEC-TITLE-003`)*.
**Nhóm thực hiện:** Văn Ngọc Nhật Anh (11A2) + Nguyễn Duy Quân (12A1).
**Giáo viên hướng dẫn (GVHD):** Lê Công Long — THPT thị xã Quảng Trị.
**Căn cứ lập:** Điều 14 Quy chế ban hành kèm Thông tư 84/2026/TT-BGDĐT (nhật ký nghiên cứu, dữ liệu gốc và minh chứng quá trình).
**Quan hệ với các sổ khác:** đây là **mục bổ sung** cho `2026-10-12_SO_TAY_NHAT_KY_NGHIEN_CUU_TOM_TAT.md` (mục 14) và cho `2026-10-19_NHAT_KY_BO_SUNG_GATE0_VA_KE_HOACH_CODE.md`. Không thay thế sổ tay gốc, không sửa các bản đã nộp.

---

## 14. 2026-10-20 — Chủ dự án duyệt ba hạng mục Gate 0/Gate 2; dựng lại bản Word để rà soát

### 14.1. Nội dung công việc

Ngày 2026-10-20, chủ dự án trả lời trực tiếp ba câu hỏi đang chờ và chỉ đạo việc tiếp theo. Nội dung đã duyệt:

1. **Bản đồ kênh cảm biến — chọn PA-2 (`DEC-CHMAP-001` ADOPTED).**
   Ba cảm biến gập (Flex) đọc qua bộ chuyển mạch 16 kênh + **sáu** ô áp lực Velostat bố trí **theo cặp lòng/mu cho mỗi ngón** cái–trỏ–giữa + **hai** ô tham chiếu không chịu tải = **11 kênh phải quét**, còn 5 kênh dự phòng (kênh cuối nối mass để kiểm tra nhiễu chéo).
   Lý do chọn: cặp lòng/mu giúp phân biệt "ép vào nẹp" với "tiếp xúc vật", là điều kiện để không diễn giải sai tín hiệu.
   Các phương án PA-1 (tối thiểu 7 kênh), PA-3a (Flex đọc thẳng vào ngõ vào còn trống của bộ chuyển đổi ADC ngoài), PA-3b (Flex vào ADC nội của vi điều khiển) **không được chọn**. PA-3a chỉ còn là **kiểm tra phần cứng tuỳ chọn** — nếu bo mạch có sẵn chân hàn thì có thể dời Flex sang đó để lấy lại 3 kênh, nhưng muốn áp dụng phải duyệt lại.

2. **Phương pháp phân biệt vận động tự nguyện với chuyển động do máy tạo ra — chọn M3 (`DEC-TASK-002` ADOPTED).**
   M3 là **cửa sổ "thăm dò tự nguyện"**: bộ điều khiển tạm ngưng trợ lực trong một khoảng ngắn rồi đo đáp ứng của người tập trong khoảng đó.
   Đây là **chọn phương pháp làm việc, không phải quy tắc đã kiểm chứng**: độ dài cửa sổ, tần suất mở, tiêu chí nhận diện đáp ứng, hành vi khi không thấy đáp ứng, số lần lặp trước khi chuyển chế độ **đều còn trống**; bắt buộc rà an toàn trước bất kỳ lần chạy có cấp nguồn nào; và M3 **không phát hiện được nỗ lực không tạo ra chuyển động** (gồng mà không dịch chuyển), nên có thể cần thêm M1 (đối chứng có/không trợ lực trên mô hình tay giả) hoặc M4 (pha tác vụ từ camera) làm lớp kiểm tra chéo — **chưa duyệt** việc kết hợp này.

3. **Cơ cấu truyền động — ba tang cuốn riêng + servo nhả dây chủ động (`DEC-MECH-007` ADOPTED).**
   Mỗi ngón cái/trỏ/giữa có **một tang cuốn riêng**; duỗi ngón bằng cách **servo nhả dây chủ động**; giữ nguyên định hướng Giai đoạn 7 là **không** dùng lò xo hồi vị và **không** dùng khớp bốn khâu.
   Lý do chọn: ba ngón cần hành trình độc lập để tạo dạng kẹp ba chấu trên cán thìa; một tang chung sẽ ràng buộc cả ba ngón.
   **Còn trống:** một động cơ kéo ba tang trên cùng trục hay ba động cơ riêng; đường kính tang, hành trình tối đa, giới hạn an toàn, cách lấy lại dây chùng; **hành vi khi mất nguồn** (dây có tự nhả hay phải có cơ cấu nhả cơ khí — đây là câu hỏi cơ khí, phần mềm không thay được); khối lượng cụm đeo 80–120 g **chưa được cân lại** cho phương án ba tang; dự toán chi phí **chưa cập nhật**; chưa có thiết bị đo lực/căng dây độc lập.

4. **Việc tiếp theo được chỉ đạo: dựng lại bản Word (DOCX) để rà soát** từ bản đề cương A/B/C dạng Markdown.

### 14.2. Phương pháp thực hiện

- Ghi từng quyết định vào sổ quyết định (`research/context/DECISION_LOG.md`) **trước**, rồi mới lan toả sang các tài liệu kỹ thuật liên quan — để mọi tài liệu đều trỏ về một nguồn có ngày tháng, không sửa rải rác theo trí nhớ.
- Với mỗi quyết định, ghi kèm **danh sách những gì vẫn còn trống** ngay trong cùng dòng quyết định, để việc "đã duyệt" không bị đọc nhầm thành "đã xong".
- Đổi trạng thái từng dòng trong bản đồ kênh dạng bảng (`research/protocols/10b_channel_map_proposed.csv`) từ `PROPOSED`/`OPEN_*` sang `ADOPTED_PA2_*`, giữ nguyên nhãn bằng chứng và ghi chú vị trí lắp còn mở; ba dòng thuộc PA-3a đổi thành `NOT_SELECTED_2026-10-20`.
- Cập nhật sổ luận điểm (`research/claims/CLAIM_LEDGER.csv`): sửa trạng thái và việc cần làm tiếp của hai luận điểm cũ, thêm hai luận điểm mới cho M3 và cho phương án ba tang — cả hai đều ghi rõ là **quyết định thiết kế, chưa có phép đo**.
- Dựng bản Word bằng một **script chuyển đổi** (`scripts/build_abc_review_docx.py`) đọc trực tiếp tệp Markdown, thay vì gõ lại nội dung: nội dung Word luôn khớp nội dung Markdown, không có chỗ nào được viết thêm bằng tay.
  Script giữ quy ước trình bày sẵn có của repo (Times New Roman 14, khổ A4, lề 3/2/2/2 cm, giãn dòng 1,35, tiêu đề 14 pt in đậm), giữ nguyên số thứ tự danh sách như bản Markdown, và **không tạo hyperlink** để tránh liên kết gãy trong bản Word.
- Script có chế độ tự kiểm tra `--check`: dò cú pháp Markdown còn sót, dò lỗi cắt nhầm đường dẫn, đếm số dòng/số cột của bảng đăng ký chỉ số, kiểm tra ngày dựng và kiểm tra mọi đề mục A/B/C của nguồn đều có mặt. Lần dựng này **PASS**.

### 14.3. Kết quả từng giai đoạn

- **Sổ quyết định:** `DEC-CHMAP-001` và `DEC-TASK-002` chuyển từ đề xuất sang **đã duyệt**; thêm mã mới `DEC-MECH-007`. Danh sách việc chờ duyệt được cập nhật lại: đã xong 2 mục, còn 4 mã chờ (`DEC-TASK-001`, `DEC-VIS-001`, `DEC-IMPL-001`, `DEC-IMPL-002`) và 3 nhóm việc đo đạc/kiểm tra phần cứng.
- **Hồ sơ kỹ thuật:** tờ yêu cầu tác vụ (`protocols/10`) có thêm mục 5.1 liệt kê 6 thông số của M3 còn trống và ràng buộc an toàn; hồ sơ bản đồ kênh (`protocols/10a`) đổi trạng thái sang đã duyệt PA-2 và đánh dấu việc số 1 trong 6 việc đóng Gate 0 là đã xong; tài liệu cơ khí (`docs/06`) có ghi chú quyết định ba tang kèm danh sách còn mở; pipeline triển khai và ảnh chụp dự án được cập nhật tương ứng.
- **Đề cương A/B/C:** cập nhật lần 3 (2026-10-20) — ghi ba quyết định vào đúng chỗ (mục phân bổ kênh, mục nguyên lý trợ lực và chuyển chế độ, mục khối lượng–chi phí), và ghi rõ hai con số khối lượng/chi phí hiện tại **được lập trước khi chốt ba tang** nên chưa phản ánh phương án mới.
- **Bản Word rà soát:** `exports/11A2_CAP_NHAT_DU_THAO_2026-10-20.docx` (khoảng 3.670 từ, 2 bảng; bảng đăng ký trước chỉ số giữ đủ 15 dòng × 6 cột). Trang đầu có khung ghi rõ **"BẢN RÀ SOÁT — KHÔNG PHẢI BẢN NỘP"**, nguồn Markdown, ngày dựng, script và quy tắc bằng chứng.
- **Không làm:** không đo phần cứng, không chạy benchmark, không tạo dữ liệu thử, **không điền bất kỳ ngưỡng hay thông số bài tập nào**, **chưa viết code/firmware** cho pipeline hiện hành, **không ghi đè** bất kỳ tệp nào trên Drive (bản Word cũ ngày 19/10 trên Drive vẫn nguyên trạng và vẫn là bản lỗi thời), **không commit/push GitHub**.

### 14.4. Việc nhóm cần làm tiếp theo

1. Duyệt 4 mã còn chờ: `DEC-TASK-001` (thông số bài tập thìa — **phải đo vật thật**), `DEC-VIS-001` (kiến trúc nhánh camera), `DEC-IMPL-001` và `DEC-IMPL-002` (lộ trình phần mềm và nơi đặt bộ giám sát chế độ).
2. Quyết định phần cơ khí còn mở của `DEC-MECH-007`: **một động cơ ba tang hay ba động cơ riêng**; sau đó **cân lại cụm đeo** và **lập lại dự toán chi phí** theo phương án ba tang, ghi ngày và kèm ảnh/minh chứng.
3. Kiểm tra 8 điểm phần cứng trước khi cấp nguồn (`protocols/10a` §7), trong đó có đối chiếu **giới hạn điện áp đầu vào của bộ chuyển đổi ADC theo datasheet** với ghi nhận cũ "đọc toàn dải 0–3,3 V" (cần tạo mã nguồn `SRC-`), và đo **dải điện trở thật của Flex** để chọn điện trở phân áp.
4. Đo **tốc độ khung thật** của chuỗi chuyển mạch → ADC với 11 kênh PA-2 để chốt `DEC-ACQ-001`; con số tính trên giấy (≈35 lần/giây khi có đọc nháp) **không được trích như kết quả**.
5. Thiết kế quy trình thử **M3 trên mô hình tay giả** trước: độ dài cửa sổ ngưng trợ lực, tiêu chí dừng, và rà an toàn; chỉ sau đó mới nói tới ngưỡng chuyển chế độ.
6. Đọc lại bản Word rà soát và xác nhận nội dung; nếu đồng ý thì duyệt toàn văn đề cương A/B/C rồi mới coi đó là bản dùng cho hội thi.

### 14.5. Ghi chú trung thực

- Lượt làm việc này do **công cụ hỗ trợ (agent) soạn theo chỉ đạo và câu trả lời trực tiếp của chủ dự án**; nhóm nghiên cứu phải đọc lại, xác nhận và chịu trách nhiệm nội dung trước khi dùng vào hồ sơ.
- "Đã duyệt" ở đây nghĩa là **chủ dự án chọn phương án**, không phải phương án đó đã được chế tạo, đã chạy thử, đã đo hay đã an toàn. Cả ba quyết định đều **chưa có dữ liệu kiểm chứng**.
- Bản Word dựng ngày 2026-10-20 là **bản để rà soát**. Đề cương dạng Markdown **chưa được duyệt toàn văn**, nên bản Word này **không phải bản đã duyệt và không phải bản nộp**.
- Không có phép đo, thử nghiệm phần cứng, benchmark hay dữ liệu người nào được tạo ra trong lượt này; không có khẳng định nào về hiệu quả phục hồi, về sử dụng tại nhà đã được xác nhận, về an toàn đã được chứng nhận, hay về tính mới/"đầu tiên".

- **Vai trò thành viên:** ⟨nhóm tự điền — ai yêu cầu, ai đọc lại, ai duyệt từng mục⟩
- **Xác nhận GVHD:** ______________________ (ngày ___/___/2026)
