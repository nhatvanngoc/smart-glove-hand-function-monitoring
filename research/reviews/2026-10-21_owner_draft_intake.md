# Tiếp nhận bản chủ dự án tự sửa — 2026-10-21

## Nguồn làm việc mới nhất

Chủ dự án gửi: “Rồi tôi đã chỉnh sửa qua văn phong của tôi, bản mới nhất tôi để ở…” và chỉ định [DE_CUONG_NOP_TRUONG.docx](https://docs.google.com/document/d/1VgzlaKYlQj55yCP45YoJ2KSRm10LV9m3/edit).

- Drive ID: `1VgzlaKYlQj55yCP45YoJ2KSRm10LV9m3`.
- Tệp Word lưu trên Drive, không phải tài liệu Google Docs gốc.
- Thư mục: `01_Cac_file_lam_viec`, ID `102Ua4MQn-zwVSscCZIdRWvJaeFZh6YaL`.
- Lần sửa ghi trong metadata: `2026-10-21T09:31:56.509Z` (16:31:56 giờ Việt Nam).
- Dung lượng: 1.654.271 byte; MD5 Drive: `c8ade1c15d9a5d9f7cbc2cd53fc25ba7`. Kiểm tra lại cuối lượt đọc: không đổi.
- Nguồn ledger: `SRC-OWNER-PROPOSAL-2026-10-21`; quyết định tiếp nhận: `DEC-PROP-019`.

Đã đọc văn bản trích xuất, gồm các phần A/B/C và danh mục tham khảo. Công cụ cắt phần giữa của câu trả lời dài, nên đã đọc nối qua các giới hạn 8.000–17.000, 19.000 ký tự và phần cuối của bản đầy đủ. Không coi kết quả trích xuất là bản sao định dạng; chưa tải byte gốc, xem ảnh hay dàn lại Word. Mục lục ghi tài liệu tham khảo ở trang 13, **không dùng dòng này để xác nhận số trang thật**.

Chỉ tiếp nhận và học cách viết. Không sửa, bình luận, ghi đè hay tải bản mới lên Drive trong lượt này. Không dựng DOCX, không sửa bản đề cương local, không commit/push. Tên file này không đồng nghĩa đã nộp chính thức, và không đồng nhất với `docs/DE_CUONG_NOP_TRUONG.md` lịch sử trong repo.

## Những thay đổi nhìn thấy so với bản trọng tâm v3

| Mặt trình bày | Bản chủ dự án gửi |
|---|---|
| Phần A | 5 mục; cơ sở y sinh trở về A.2, gồm đại diện vỏ não/Hebb và GAP/độ tin cậy |
| Phần B | I. Tổng quan; II. Bất cập và giải pháp; III. Nguyên lý/cơ chế, tách 3.1 sơ đồ khối và 3.2.1–3.2.6 theo cơ chế |
| Phần C | “Kế hoạch chế tạo và thử nghiệm”, 7 mục; kết thúc bằng tích hợp bài tập thìa, không giữ khung C.8/C.9 của v3 |
| Đơn vị trình bày | đoạn mở ngắn nêu mục đích/lựa chọn, sau đó gạch đầu dòng cho thành phần, bước xử lý hoặc phép đo |
| Tiêu chí | dùng ≥, ≤, CV, SEM, MDC và đơn vị trực tiếp thay cho diễn giải bằng câu dài |
| Hình | văn bản có chú thích Hình 1–9 theo dạng “Hình n: …”; không còn phụ lục yêu cầu 7 hình của v3 |
| Tham khảo | đánh số lại; Kapandji ở [12], Hopkins ở [15]; không được áp bảng số trích dẫn của v3 vào bản này |
| Bìa | chủ dự án đã điền trường, thành viên, lớp và GVHD; đây là dữ liệu từ bản chủ dự án, không phải agent tự điền |

## Bài học văn phong, dùng cho các lượt sửa sau

1. **Không ép mọi ý thành văn xuôi.** Câu mở nêu vấn đề, các dòng sau chia thao tác/thuộc tính cụ thể. Ví dụ B.3.2.6: “Flex và Velostat không cho biết người tập có thao tác đúng với vật thật hay không, nên nhóm bổ sung một kênh quan sát độc lập bằng camera.” Sau đó là các dòng về bố trí, nhãn và vai trò.
2. **Giữ chủ thể tại chỗ ra quyết định.** “Nhóm quyết định”, “nhóm chọn”, “nhóm sẽ kiểm” đủ để dẫn; không cần thêm chủ ngữ đó vào từng dòng đặc tả.
3. **Tiêu đề song song có chức năng, không tự động là slop.** “Nghiên cứu…” ở A.3 và “Xây dựng cơ chế…” ở B.3.2 tổ chức các việc ngang hàng. Không làm câu vòng vèo chỉ để tránh lặp từ.
4. **Viết đúng thể loại đề cương.** C là kế hoạch chế tạo/thử nghiệm, có ghi phần đã làm ở đúng chỗ như C.2(a) và kế hoạch kiểm ở C.2(b); không tự thêm kết luận dài, lịch mốc hay bảng trạng thái từ kho cũ.
5. **Giữ ký hiệu và thuật ngữ chuyên ngành hữu ích.** ADC, PGA, EMA, I²C, assist-as-needed và chú giải tiếng Anh được dùng khi làm rõ cơ chế. Anti-slop không có nghĩa là dịch bỏ mọi thuật ngữ hoặc viết mọi bất đẳng thức bằng lời.
6. Giữ cách viết của chủ dự án (“lí do”, “kĩ thuật”, “tỉ lệ”, “xử lí” ở các đoạn đã sửa) khi biên tập cục bộ; không tự chuẩn hóa lại toàn bài hoặc sửa ngược theo giọng v3.

## Những khác biệt nội dung phải tách khỏi đánh giá văn phong

Đây là ghi nhận để không nhầm bản mới với một lượt thay từ đơn thuần; **chưa sửa các chỗ dưới đây hoặc đổi trạng thái bằng chứng**:

- **DSP 2 nhánh, B.3.2.3:** Velostat có bám nền/vùng chết/EMA; Flex dùng EMA và hồi quy hiệu chuẩn góc, không dùng vùng chết. Đây là nội dung thiết kế mới so với cách mô tả chung ở v3. Câu C.3 nói vòng 2 kết hợp “thuật toán 2 nhánh” cần phân biệt với nhật ký chạy thử Velostat đã có và việc hiệu chuẩn Flex còn theo kế hoạch (`DEC-HW-007`).
- **Vùng chết 180 mV:** bản mới dùng câu “vẫn bảo toàn tuyến tính khi phát lực”. Không lấy câu này để đóng rủi ro mất tín hiệu nỗ lực nhỏ đã ghi ở lần rà 20/10. Giá trị 5°–10° trong nhánh Flex cũng chưa có dữ liệu hiệu chuẩn được cung cấp trong lượt này.
- **Đọc nháp:** mô tả “đọc nháp 1 lần để xả điện tích dư” cần rà cơ chế lấy mẫu/chuyển kênh theo cấu hình thật; không tự thay bằng một khẳng định tuyệt đối khác về bộ lọc delta–sigma. Khoảng 35 khung/s vẫn là tính toán (`CLM-ACQ-002`), không được tự đổi sang số đo.
- **C.2(a):** chủ dự án ghi đã bố trí Velostat trên nẹp đốt đơn và bước đầu thử nguyên lý. Ghi nhận phạm vi đốt đơn; không suy ra đã chế tạo/hiệu chuẩn đủ cấu hình 11 kênh.
- **Tài liệu tham khảo:** Penfield [5] trong bản mới là 389–443, khác 389–440 đang dùng ở `SRC-PENFIELD-1937-HOMUNCULUS`; Kapandji [12] là mục mới cần đối chiếu trước khi tái sử dụng. Chưa sửa hoặc xác minh lại thư mục tài liệu tham khảo.

Không dùng việc tiếp nhận văn phong để duyệt ngưỡng, xác nhận hiệu quả lâm sàng hay coi một phép thử dự kiến đã thực hiện. Các bản v3/v4/kho cũ chỉ dùng đối chiếu lịch sử; bản Drive chủ dự án gửi là điểm xuất phát cho lần sửa tiếp theo.
