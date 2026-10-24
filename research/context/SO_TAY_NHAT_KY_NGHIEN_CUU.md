
### 2026-10-20 — bung hết bản ghép cặp (`DEC-PROP-015`)

Chủ dự án trả lời cho câu hỏi về trần trang: *"Cứ bung hết đi, rồi tôi sẽ cắt và chỉnh sửa sau đó gửi lại cho bạn."* Vậy bản ghép cặp chuyển vai trò: **không phải bản nộp**, mà là **kho nội dung** để cắt. Đã thêm B.9 (kiến trúc phần mềm, firmware, lộ trình bảy pha, 8 nguyên tắc bất biến khi viết mã) từ `docs/08`; C.7 (kiểm thử phần mềm, bộ mô phỏng, bốn phép kiểm tính chất của bộ giám sát pha, nhật ký phiên) và đánh số lại C.8–C.10; mở rộng B.8 và C.6 từ `docs/07` (giả định cảnh, bộ nhận biết cắm được, xử lý ảnh cổ điển trước, hiệu chuẩn camera, giao tiếp hai bo, phiếu đo chín chỉ số); hái **lý thuyết** từ `docs/bao_cao/A7_AAT_rationale_DRAFT.md` (**SUPERSEDED** — chỉ lấy cơ sở Hebb, bất hoạt do học được, ba điều kiện trợ lực theo nhu cầu, hiệu ứng ỷ lại; **không** lấy phạm vi, công thức lực, hay cách nói "GAP không quy đổi ra độ" của bản đó); phần A đầy đủ hơn từ `docs/MO_TA_DU_AN_…` (hai kịch bản khi không có công cụ theo dõi, bảng ba chế độ tập theo ai phát lực, PROM→AROM); phụ lục A–F từ `GLOSSARY.md`, `protocols/10`, `10a`, `10b`; và bảng 11 rủi ro kèm phương án dự phòng.

Hai bài học kỹ thuật ghi lại: **hoán đổi cả một phần giữa hai tệp làm rớt placeholder hình** của phần đó (⟨HÌNH 1⟩ mất, đã khôi phục) và **làm hỏng anchor** đã chép từ trước khi hoán đổi (chèn A.1 hụt một lần vì bản mới viết "chọn chế tạo một chiếc găng tay"). Từ nay: **đếm lại HÌNH và số từ ngay sau mỗi lần ghép**, và **chép anchor bằng grep sau khi hoán đổi**.

Trạng thái: 18.656 từ / 231 đoạn / 12 bảng / 7 HÌNH; DOCX 14 pt và 13 pt đều `--check` PASS (271 đoạn, 13 bảng, 18.091 từ). Không mã nội bộ, không ký tự ngoài tiếng Việt. **Chưa tải lên Drive** — chờ bản cắt của chủ dự án để khỏi sinh thêm một phiên bản phải khai báo vượt.

### 2026-10-20 — bản trọng tâm lên Drive (`DEC-PROP-016`)

Chủ dự án đổi hướng: không tự cắt bản 35 trang, mà *"chỉ cần các phần trọng tâm trong đề cương để đẩy lên drive để tôi làm tiếp"*. Vậy bản trọng tâm được lấy **nguyên trạng từ bản ghép cặp trước khi bung** (`/tmp/ghepcap_v1_9785.md`), chỉ thêm một câu ở C.8 để giữ ranh giới phạm vi: trợ lực theo nhu cầu là nền tảng có sẵn trong y văn, không phải ý tưởng của đề tài. Không tự cắt thêm nội dung nào, vì nguyên tắc đã ghi từ trước là *rút độ dài nhưng không cắt nội dung* — phần cắt là việc của chủ dự án, và mọi thứ đã cắt đều còn trong bản bung hết để rút lại.

Bài học quy trình: khi chủ dự án nói "bung hết rồi tôi cắt", họ vẫn có thể đổi sang "đưa tôi bản trọng tâm" — nên **luôn giữ bản trước khi bung ở `/tmp` và ở một tệp riêng**, để bản trọng tâm có sẵn mà không phải dựng lại. Lần này làm được là nhờ `/tmp/ghepcap_v1_9785.md` và nhờ bản bung nằm ở tệp khác chứ không ghi đè.

Trạng thái: 9.832 từ / 156 đoạn / 5 bảng / 7 HÌNH; DOCX 14 pt và 13 pt đều `--check` PASS (188 đoạn, 6 bảng, 9.662 từ). Drive: `13Ii3YG9hXsNPt-v5OdYivkHVws9zPonF` trong `01_Cac_file_lam_viec`; bình luận `AAACG9bNHBQ` trên v4. Chưa tải biến thể 13 pt. Chưa commit.

### 2026-10-20 — dọn văn phong "phòng vệ AI" (`DEC-PROP-017`)

Chủ dự án chỉ ra đúng chỗ yếu của các bản do agent viết: *"loại bỏ, DỌN DẸP VĂN PHONG VÀ THUẬT NGỮ 'PHÒNG VỆ AI' và AI trong báo cáo mà bình thường không gặp"*. Đọc lại toàn bộ bản trọng tâm thì thấy dấu vết nằm ở năm chỗ, và chúng đều là **thói quen của người viết sợ nói sai**, không phải nội dung: một hệ thống nhãn bằng chứng ba mức tuyên bố ở đầu phần rồi lặp trong từng ô bảng; những câu phủ định chồng ba mệnh đề ("không chứng minh X, không chứng minh Y, không thay thế Z"); thuật ngữ mượn từ công nghệ phần mềm (mã băm, cờ, cắm được, bring-up, log, firmware); câu tự nói về bố cục tài liệu; và mã nội bộ của repo lọt ra ngoài (Mech 9, CH15, REF_1).

Cách dọn: **không xóa thông tin, chỉ xóa sự lặp lại và đổi từ**. Ranh giới đã đo và chưa đo vẫn phải còn, vì đó là kỷ luật của hồ sơ nghiên cứu, nhưng chỉ nói một lần ở chỗ tự nhiên nhất thay vì dán vào every ô bảng. Bảng C.3 mất một cột vì cả bảy ô của cột đó đều ghi "chưa có" — một cột không có thông tin thì không phải là trung thực, chỉ là ồn. Câu tự tuyên bố "không nhận tính mới" bị bỏ hẳn: không tuyên bố tính mới là đủ, phủ định nó mới là giọng của máy.

Kết quả: 93 lượt thay, 9.832 → 9.349 từ, ~19,0 → ~18,2 trang ở 14 pt; DOCX `--check` PASS; grep lại sạch `Mech`, `CH15`, `REF_`, `mã băm`, `log`, `cắm được`, `bring-up`, `firmware`, và sạch ký tự ngoài tiếng Việt. **Không một con số nào bị đổi.** Bộ quy tắc đã chép vào `research/tooling/WRITING_STYLE_PROFILE.md` để bản sau không tái phạm; bản kho (bung hết) cũng được dọn cùng lúc, để khi rút khối nội dung từ đó sang thì không mang theo giọng cũ.

Drive: v2 `1uGVmpj9eB4U-MPPqKgo7x9wlSMwwm4e4`; v1 `13Ii3YG9hXsNPt-v5OdYivkHVws9zPonF` đã có bình luận `AAACJEmcTGQ` khai báo vượt. Bản nộp v4 cũ vẫn nguyên trạng (byte-identical). Chưa commit.

### 2026-10-20 — áp dụng Anti-slop v2 (`DEC-PROP-018`)

Chủ dự án đưa đối sánh với báo cáo xe lăn và bộ 7 nguyên tắc, kèm 8 vị trí sửa trực tiếp. Lượt này viết lại mạch B.3–B.8, không chỉ xóa nhãn. C.8 chuyển thành văn xuôi về lựa chọn khóa và 2 vòng thử mạch; việc tiếp theo về C.9/C.7. Quy ước số liệu còn một câu đầu C, giới hạn chung một đoạn ở C.9. Dòng trỏ lặp thay bằng bảng ghép B↔C. Bảng tham số/kết quả thêm cách kiểm chứng và phương pháp đo. Bảy hình có câu dẫn và phụ lục tư liệu cần bổ sung.

Phát hiện lỗi công cụ: dù trước đó truyền banner/status/meta rỗng, builder vẫn tạo bảng vận hành. Đã thêm `--no-meta` và kiểm tra XML DOCX. Đồng thời sửa lỗi cỡ chữ 13 pt chỉ áp vào style, còn run vẫn 14 pt. Bản sạch tách bìa, mục lục, nội dung; phiên bản ở chân bìa. Chế độ rà soát nội bộ giữ metadata.

Không biến ví dụ văn phong thành dữ liệu: khóa 9 chỉ đã in, không viết “khả thi nhất” như kết quả thực nghiệm; không thêm 10 phiên đo nhiễu hoặc kể rằng nhóm đã làm đối chứng ép nẹp/tiếp xúc vật. Giữ các giá trị số và 15 tham khảo; sửa cách mô tả 33,3 ms thành khoảng cách khung ảnh, tách sai lệch góc khỏi CV trong phép kiểm GAP. Các phương pháp sẽ thực hiện vẫn được viết như kế hoạch.

Kết quả: Markdown 9.288 từ (A/B/C 8.358 từ); 2 DOCX 8.987 từ, 7 bảng, kiểm tra đạt. Bộ kiểm tra tự động **14/14 đạt**; bản nộp v4 byte-identical. Chưa có bộ dàn trang Word/LibreOffice, nên chưa xác nhận trần 14 trang và không công bố lại ước tính cũ.

Drive v3 `1jd22OBFOiyv2Fvd3au_cWn2HT8wl4WfQ`, 59.940 byte; bình luận `AAACI4Z4AB4` trên v2. Bản 13 pt (59.923 byte) ở workspace. Quy tắc v2 lưu trong profile; ghi chú đối chiếu đủ 8 mục ở `research/reviews/2026-10-20_anti_slop_v2.md`. Bản kho, bản mô tả và bản nộp v4 không viết lại trong lượt này. Không commit/push.

### 2026-10-21 — tiếp nhận bản chủ dự án tự sửa (`DEC-PROP-019`)

Chủ dự án cho biết đã sửa theo văn phong của mình và gửi `DE_CUONG_NOP_TRUONG.docx` (`1VgzlaKYlQj55yCP45YoJ2KSRm10LV9m3`). Đã đọc văn bản qua Drive, kiểm tra metadata trước/sau không đổi: 1.654.271 byte, MD5 `c8ade1c15d9a5d9f7cbc2cd53fc25ba7`, sửa lúc 16:31:56 ngày 21/10 giờ Việt Nam. Đây là nguồn làm việc mới nhất; chưa có xác nhận đã nộp chính thức.

Điểm cần học không chỉ là từ ngữ: A còn 5 mục và có cơ sở y sinh ở A.2; B tổ chức thành tổng quan, bất cập và các cơ chế; C là kế hoạch chế tạo/thử nghiệm 7 mục. Câu dẫn ngắn nêu lựa chọn rồi chia gạch đầu dòng; dùng ký hiệu định lượng và thuật ngữ chuyên ngành khi cần. Không áp máy móc cấu trúc C.8/C.9 hoặc 7 hình của v3 vào bản này. DSP Flex/Velostat tách 2 nhánh là thay đổi nội dung, cần phân biệt với việc chỉ sửa văn phong.

Cập nhật nguồn hiện hành, INDEX, profile và source ledger; ghi nhận chi tiết ở `research/reviews/2026-10-21_owner_draft_intake.md`. Không tạo bản sao giả định là mirror, không sửa Drive hay các đề cương local, không comment/upload và không commit/push.

### 2026-10-21 — phương án tăng vai trò nhánh thị giác (`DEC-VIS-002`, chưa duyệt)

Chủ dự án muốn Camera + Orange Pi có nhiệm vụ ảnh hưởng lớn hơn, gợi ý Depth Anything. Đã đối chiếu nguồn đề cương mới, vai trò từng cảm biến và tài liệu mô hình chính thức. Đề xuất trọng tâm là đo chất lượng cầm–giữ–thả vật và đối chiếu với tín hiệu ngón, sau đó điều phối mức khó bài tập bằng quy tắc. Theo dõi vai/thân là hướng khác nhưng có nguy cơ mở rộng khỏi vận động tinh.

Độ sâu phải tạo được đại lượng có ích hơn nhãn 2D; kiểm bằng nâng thực/kéo trượt/tuột vật/đặt–nhả trên bàn thử và phantom. V2 có trọng số relative và metric riêng; chữ metric không tự xác nhận độ chính xác trên thìa. RKNN3 có DA3 nhưng nền tảng RK3588 trong bảng dùng RK1820/RK1828 bổ sung, không phải chứng cứ cho NPU tích hợp bo hiện có. Chưa có benchmark, model/camera cuối hay ngưỡng số.

Ghi phương án tại `research/reviews/2026-10-21_camera_role_options.md`, thêm `CLM-VISION-002`, 4 nguồn tài liệu và 4 truy vấn. Quyết định ở mức **PROPOSED**; nguồn Drive của chủ dự án, các đề cương local, firmware/vision code và nhánh RL đã loại không bị thay đổi. Không commit/push.
