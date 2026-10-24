# Ghi nhận quyết định của chủ dự án (2026-10-20) và việc dựng lại bản Word rà soát

> **Ngày:** 2026-10-20 · **Loại:** ghi nhận quyết định + nhật trình dựng tài liệu (không phải phản biện độc lập).
> **Bối cảnh:** tiếp nối lượt tài liệu 2026-10-19 ([`2026-10-19_gate0_packet_and_abc_review.md`](2026-10-19_gate0_packet_and_abc_review.md)). Chủ dự án được hỏi 4 câu có lựa chọn sẵn và đã trả lời trực tiếp trong phiên làm việc; sau đó chỉ đạo việc tiếp theo là dựng lại bản Word để rà soát.
> **Ranh giới:** ba quyết định dưới đây là **lựa chọn phương án của chủ dự án**, không phải kết quả đã chế tạo/đã đo/đã kiểm chứng an toàn.

---

## 1. Ba quyết định đã duyệt

| Mã | Nội dung duyệt | Trạng thái | Còn `OPEN` (không được tự điền) |
|---|---|---|---|
| `DEC-CHMAP-001` | **PA-2** — 3 Flex qua CD74HC4067 + 6 Velostat (cặp lòng/mu mỗi ngón cái–trỏ–giữa) + 2 ô tham chiếu = **11 kênh quét**, 5 kênh dự phòng | ADOPTED 2026-10-20 | vị trí lắp từng phần tử; dải điện trở Flex thật + điện trở phân áp; tốc độ khung/SPS/N thật (`DEC-ACQ-001`); 8 kiểm tra phần cứng trước khi cấp nguồn; PA-3a chỉ là kiểm tra tuỳ chọn, muốn đổi phải duyệt lại |
| `DEC-TASK-002` | **M3** — cửa sổ "thăm dò tự nguyện": tạm ngưng trợ lực một khoảng ngắn rồi đo đáp ứng | ADOPTED 2026-10-20 (chọn phương pháp, **chưa kiểm chứng**) | độ dài cửa sổ; tần suất mở; tiêu chí nhận diện đáp ứng; hành vi khi không thấy đáp ứng; số lần lặp trước khi chuyển `ASSIST→AAN`; **rà an toàn bắt buộc**; M3 không thấy nỗ lực không tạo chuyển động → M1/M4 làm lớp đối chiếu **chưa duyệt** |
| `DEC-MECH-007` (mã mới) | **Ba tang cuốn riêng** (mỗi ngón một tang) + **servo nhả dây chủ động** để duỗi; không lò xo hồi vị/SEA, không khớp bốn khâu | ADOPTED 2026-10-20 (hướng cơ khí) | một động cơ ba tang trên cùng trục hay ba động cơ riêng; đường kính tang/hành trình/giới hạn/cách lấy lại dây chùng; **hành vi nhả khi mất nguồn**; khối lượng 80–120 g chưa cân lại; dự toán chi phí chưa cập nhật; chưa có tham chiếu lực/căng dây độc lập |

Việc thứ tư được chỉ đạo: **dựng lại DOCX review** từ đề cương A/B/C dạng Markdown (mục 3).

**Không được duyệt trong phiên này** (vẫn `PROPOSED`): `DEC-TASK-001` (thông số bài tập thìa — cần đo vật thật), `DEC-VIS-001` (kiến trúc nhánh camera), `DEC-IMPL-001` (lộ trình F0–F6), `DEC-IMPL-002` (nơi đặt mode supervisor), `DEC-ACQ-001` (tốc độ khung — phải đo). **Chưa viết code/firmware nào.**

## 2. Những tệp đã sửa để ghi nhận quyết định

| Tệp | Sửa gì |
|---|---|
| `research/context/DECISION_LOG.md` | `DEC-CHMAP-001`, `DEC-TASK-002` → ADOPTED kèm danh sách còn `OPEN`; thêm dòng mới `DEC-MECH-007`; cập nhật 3 mục trong checklist chờ duyệt |
| `research/claims/CLAIM_LEDGER.csv` | `CLM-ACQ-001` → `ADOPTED_PA2_2026-10-20`; `CLM-TASK-001` cập nhật việc tiếp theo; thêm `CLM-TASK-002` (M3 đã chọn, chưa kiểm chứng) và `CLM-MECH-007` (ba tang, chưa chế tạo, khối lượng/chi phí chưa cập nhật) |
| `research/protocols/10a_…md` | trạng thái đầu tệp → `ADOPTED (PA-2)`; ghi chú kết quả duyệt ở §2; tiêu đề PA-2 và §3 đổi sang "đã duyệt"; việc 1 và việc 6 ở §9 đánh dấu đã xong (việc 6 còn nợ nhãn `layout_revision`) |
| `research/protocols/10b_channel_map_proposed.csv` | cột `status` → `ADOPTED_PA2_OPEN_POSITION` / `…_OPEN_PLACEMENT` / `…_REF` / `…_SPARE`; 3 dòng PA-3a → `NOT_SELECTED_2026-10-20`; `evidence_label` → `OWNER_APPROVED_PA2_2026-10-20; POSITION_OPEN` |
| `research/protocols/10_gate0_task_state_sheet.md` | tiêu đề §5 → "đã chọn M3, chưa kiểm chứng"; thêm **§5.1** (6 thông số M3 còn `OPEN` + ràng buộc an toàn + giới hạn đã biết); 4 dòng trong bảng `OPEN` §8 (mục 4, 5, 6, 8) cập nhật phần đã chốt/phần còn mở |
| `docs/06_Co_Cau_Co_Khi_Exoskeleton.md` | thêm `DEC-MECH-007` vào dòng quyết định liên quan và một ghi chú cập nhật 2026-10-20 (nêu rõ **CAD bên dưới chưa cập nhật theo quyết định này**) |
| `docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md` | cập nhật lần 3: ghi ba quyết định vào §B.2 (phân bổ kênh), §B.3 (M3 + ba tang), §B.4 (khối lượng/chi phí **lập trước** khi chốt ba tang nên chưa phản ánh phương án mới); sửa 2 dòng trong bảng §C.4 (chuyển mode, khối lượng); ghi việc dựng lại DOCX ở đầu tệp |
| `research/context/IMPLEMENTATION_PIPELINE.md` | Gate 0: thêm khối "Owner decisions 2026-10-20" và khẳng định **Gate 0 vẫn chưa đạt**; Gate 2: thêm `DEC-MECH-007` + danh sách còn mở; cập nhật dòng trạng thái cuối §4 |
| `research/context/PROJECT_SNAPSHOT.md` | thêm khối ghi chú 2026-10-20; sửa dòng AAN/mechanics để trỏ tới `DEC-MECH-007` |
| `README.md`, `INDEX.md`, `research/README.md`, `research/tooling/SETUP_STATUS.md` | đăng ký tệp mới và trạng thái mới |
| `research/notebook/…` | sổ tay (mục 14), bảng tổng hợp thay đổi (4 dòng mới cho Giai đoạn 7 + cập nhật mục chờ quyết định), và bản bổ sung riêng `2026-10-20_NHAT_KY_QUYET_DINH_PA2_M3_BA_TANG_VA_DUNG_LAI_DOCX.md` |

## 3. Bản Word rà soát

- **Tệp ra:** `exports/11A2_CAP_NHAT_DU_THAO_2026-10-20.docx` (~3.670 từ, 2 bảng).
- **Nguồn duy nhất:** `docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md` (bản cập nhật lần 3). Không gõ lại nội dung bằng tay.
- **Script:** `scripts/build_abc_review_docx.py` — chuyển Markdown → DOCX theo quy ước trình bày sẵn có của repo (`de_cuong/build_docx.py`): Times New Roman 14, A4, lề 3/2/2/2 cm, giãn dòng 1,35, tiêu đề 14 pt in đậm (Heading 3 in đậm nghiêng), bảng `Table Grid`, số trang ở chân trang. Giữ nguyên số thứ tự danh sách của Markdown (không dùng đánh số tự động để tránh nhảy số), và **không tạo hyperlink** — liên kết nội bộ render thành "chữ (đường dẫn repo)".
- **Khối metadata ở đầu bản Word:** dòng cảnh báo **"BẢN RÀ SOÁT — KHÔNG PHẢI BẢN NỘP"**, nguồn Markdown, ngày dựng (tính theo giờ Việt Nam UTC+7), tên script, trạng thái nội dung, và quy tắc bằng chứng (mọi ô `OPEN` để trống có chủ đích; script không sinh ra con số nào).
- **Phụ thuộc:** `python-docx` — **không** thêm vào `requirements.txt` (tệp đó dành cho mô phỏng/đồ thị); ghi trong `research/tooling/SETUP_STATUS.md`.

### Kiểm tra đã chạy (`python3 scripts/build_abc_review_docx.py --check`) → **PASS**

1. Không còn cú pháp Markdown trong bản Word (`**`, `` ` ``, `](`, `~~`): 0 lần.
2. Không có đường dẫn bị cắt ký tự cuối (lỗi `.md` → `.m` đã phát hiện và sửa trong quá trình dựng): 0 lần.
3. Đủ bảng: bảng đăng ký trước chỉ số giữ **15 dòng × 6 cột** (1 tiêu đề + 14 chỉ số).
4. Ngày dựng hợp lệ theo định dạng ISO và đúng **2026-10-20**.
5. Mọi đề mục `##` của nguồn (A, B, C, Tài liệu tham khảo) đều có mặt trong bản dựng.
6. Độ dài hợp lý (3.668 từ) — không thiếu nội dung.

Ba lỗi được phát hiện và sửa trước khi lấy bản cuối: (a) ngày dựng lấy theo giờ UTC của máy nên bị lùi một ngày so với giờ Việt Nam; (b) danh sách có số thứ tự bị trộn giữa đánh số tự động và số chữ, khiến mục đầu tiên mất số; (c) bốn ghi chú đầu tệp bị gộp thành một đoạn; ngoài ra còn lỗi cắt ký tự đường dẫn liên kết nêu ở mục 2.

## 4. Những gì KHÔNG làm trong lượt này

- Không ghi đè, không chỉnh sửa `11A2.pdf`, `11A2.docx` hay `11A2_CAP_NHAT_DU_THAO_2026-10-19.docx` trên Google Drive. Bản 19/10 trên Drive **vẫn lỗi thời** và không được trình bày như bản hiện hành.
- Không ghi đè, không đổi tên, không di chuyển bất kỳ tệp nào đang có trên Drive. Hai tệp tải lên trong lượt này đều là **tệp mới** (xem mục 6).
- Không điền ngưỡng, thông số bài tập, kích thước thìa/vùng đích, thời gian giữ, số lần thử, giới hạn an toàn hay tốc độ khung mục tiêu.
- Không đo phần cứng, không chạy benchmark thị giác, không tạo log trong `research/bench/logs/`, không sinh dữ liệu mô phỏng.
- Không viết code/firmware cho pipeline hiện hành (`DEC-IMPL-001/002` vẫn chờ duyệt).
- Không commit/push GitHub, không mở PR (theo chỉ đạo phiên trước).
- Không sửa các hồ sơ đã nộp và tài liệu lịch sử.

## 5. Việc đang chờ

1. **4 mã quyết định:** `DEC-TASK-001` (cần đo thìa/vùng đích thật), `DEC-VIS-001`, `DEC-IMPL-001`, `DEC-IMPL-002`.
2. **Cơ khí:** một động cơ ba tang hay ba động cơ riêng; hành trình/giới hạn; hành vi nhả khi mất nguồn; cân lại khối lượng; lập lại dự toán chi phí.
3. **Phần cứng:** 8 kiểm tra trước khi cấp nguồn (`10a` §7), trong đó có đối chiếu datasheet cho giới hạn đầu vào ADC (cần tạo `SRC-ID`) và đo dải điện trở Flex.
4. **Đo:** tốc độ khung thật với 11 kênh PA-2 để chốt `DEC-ACQ-001`.
5. **M3:** thiết kế quy trình thử trên phantom (độ dài cửa sổ, tiêu chí dừng, rà an toàn) trước khi nói tới ngưỡng.
6. **Duyệt toàn văn** đề cương A/B/C; sau đó mới dùng bản Word cho mục đích nộp/trao đổi với GVHD.
7. **Drive:** bản Word rà soát và bản nhật ký 2026-10-20 **đã được tải lên** (mục 6). Nếu nhóm muốn đặt bản Word ở thư mục khác (ví dụ cạnh `11A2.docx` trong `08_Truy_vet_upload_drive`) thì cần nói rõ — hiện bản Word được đặt trong `01_Cac_file_lam_viec` để không nằm cạnh các tệp nguồn đã nộp, tránh nhầm lẫn.

---

## 6. Bản sao trên Google Drive (tải lên mới ngày 2026-10-20 — không ghi đè tệp nào)

| Tệp | Thư mục Drive | ID | Ghi chú |
|---|---|---|---|
| `2026-10-20_NHAT_KY_QUYET_DINH_PA2_M3_BA_TANG_VA_DUNG_LAI_DOCX.md` (11.519 B) | `04_So_tay_nhat_ky_nghien_cuu` | `1ja-Q3G-OM2tHIotD2f6w3bemZlUillCc` | mục bổ sung cho sổ tay; ô vai trò thành viên + ô GVHD để trống |
| `11A2_CAP_NHAT_DU_THAO_2026-10-20_BAN_RA_SOAT.docx` (49.407 B) | `01_Cac_file_lam_viec` | `1j4D_fxomFLwh4a2Vmok__b77f3hwmi2O` | cùng nội dung với `exports/11A2_CAP_NHAT_DU_THAO_2026-10-20.docx`; tên trên Drive có hậu tố `BAN_RA_SOAT` để không thể nhầm với bản nộp |

Bình luận để lại (không sửa nội dung tệp):

| Tệp được bình luận | ID tệp | ID bình luận | Nội dung chính |
|---|---|---|---|
| `2026-10-12_SO_TAY_NHAT_KY_NGHIEN_CUU_TOM_TAT.md` (Drive) | `1QL4Uh7z-zw119_OX0PEMoPYegvKXU5YI` | `AAACJEAXHn4` | mục 14 + ba quyết định + ghi chú §9.2 đã rút |
| `2026-10-12_BANG_TONG_HOP_THAY_DOI_CHINH_THUC.md` (Drive) | `1pHm09c7anTo7IFutZyv5-rNcVplYXX8E` | `AAACBEnB3HY` | 4 dòng mới của Giai đoạn 7 + mục chờ quyết định 9 (chốt một phần) và 11–13 |
| `11A2_CAP_NHAT_DU_THAO_2026-10-19.docx` (Drive, **lỗi thời**) | `1YXvVbi53CPcrzXaJQAPZTQ3ugnsjhErd` | `AAACI3RglQo` | cảnh báo không dùng làm bản hiện hành/bản nộp; trỏ tới bản rà soát 2026-10-20 |

Kiểm tra sau tải lên: đọc trích xuất văn bản của bản DOCX trên Drive — dòng đầu tiên là **"BẢN RÀ SOÁT — KHÔNG PHẢI BẢN NỘP"**, tức tệp nhị phân không bị hỏng khi tải lên. `11A2.pdf` (`1uJDGpTx_sR1P1VCsHM1fv6hrnCzMgDaJ`) và `11A2.docx` (`1VbI9CRPWsx7q0o54h7lAQ4bWq9nz50PO`) **không bị đụng tới**.
