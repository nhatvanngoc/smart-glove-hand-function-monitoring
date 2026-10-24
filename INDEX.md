# INDEX — Sơ đồ file của dự án

> **Nguồn đề cương mới nhất — 2026-10-21:** [DE_CUONG_NOP_TRUONG.docx](https://docs.google.com/document/d/1VgzlaKYlQj55yCP45YoJ2KSRm10LV9m3/edit), bản chủ dự án tự sửa (`DEC-PROP-019`). Các bản trọng tâm v3/v4 trong repo là lịch sử, **không phải bản sao của tệp mới**. Ghi nhận tiếp nhận và mẫu giọng: [`research/reviews/2026-10-21_owner_draft_intake.md`](research/reviews/2026-10-21_owner_draft_intake.md). Không sửa bản lịch sử `docs/DE_CUONG_NOP_TRUONG.md` theo tên file Drive.

> **Hướng đề tài hiện hành:** găng hỗ trợ tập phục hồi vận động tinh sau đột quỵ; chức năng tiến triển từ gập–duỗi có trợ giúp, tự động chuyển AAN theo ngưỡng, tới phối hợp ba ngón gắp–nhấc–di chuyển–đặt thìa. Tên làm việc chưa phải tên cuối.
> **Cập nhật:** 2026-10-19 · Thẩm quyền: [`research/context/CURRENT_DESIGN_BASELINE.md`](research/context/CURRENT_DESIGN_BASELINE.md), `DEC-REHAB-001` và `DECISION_LOG.md`.
> **Cảm biến/hệ thống:** 3 Flex sensor (mỗi ngón cái–trỏ–giữa một chiếc) theo dõi gập–duỗi; Velostat ghi áp lực/tiếp xúc tương đối; camera theo dõi thìa/vùng đích/kết quả. Nếu cả 3 Flex cùng đi qua MUX 16 kênh thì còn tối đa 13 kênh cho Velostat/ô tham chiếu; map cuối mở. Orange Pi 5 Pro dự kiến xử lý thị giác; chưa benchmark; RL không thuộc phạm vi. Không yêu cầu KTV chuyển mode. Servo cuốn dây trực tiếp trên tang; an toàn, hồi/duỗi và điều khiển độc lập còn mở.
> **Bằng chứng:** bench/phantom trước; không thử bệnh nhân/claim hiệu quả lâm sàng/home use đã xác nhận. Các chỉ số kỹ thuật là mục tiêu tới khi có log; không tuyên bố novelty/“đầu tiên”. Hồ sơ đã nộp giữ nguyên.
> **Drive:** nguồn `11A2.docx` và PDF người dùng cung cấp vẫn nguyên trạng. DOCX review riêng dựa trên draft cũ, hiện không đại diện cho hướng mới.

---

## Cấu trúc hiện tại

```
.
├── README.md                      ← Tóm tắt định hướng và ranh giới hiện hành
├── INDEX.md                       ← File này
├── LICENSE
├── requirements.txt               ← numpy, matplotlib, scikit-learn
├── 3d_model/                          ← [Trọng tâm] Thiết kế cơ cấu cơ khí nẹp ngón tay (CAD & 3D Print)
│   ├── custom_exo/full_finger_modular/ ← Bộ 3 đốt module hóa Print-in-Place + Khớp rãnh trượt 13.5mm (STL/STEP/FCStd)
│   ├── custom_exo/fixation_mechanisms_benchmark/ ← 9 phương án cơ cấu đóng/mở nẹp 1 đốt (Mech 1-9), đã in thử thực tế; Mech 9 (hiện tại) CHƯA có file CAD — xem README trong thư mục
│   ├── generate_full_finger_modular.py ← Script FreeCAD Python sinh tham số toàn bộ ngón tay
│   └── render_full_finger.py          ← Script kết xuất đồ họa trực quan 4 góc nhìn
├── de_cuong/
│   ├── DE_CUONG_NGHIEN_CUU.pdf / .docx (= _BAN_MOI, MD5 trùng) ← bản 2026-10-03, lịch sử; phần AAN/lực/phantom-only superseded bởi baseline 2026-10-19
│   ├── DE_CUONG_NGHIEN_CUU_COBROWSE.docx ← bản rút gọn/khác (40 KB, chưa đọc chi tiết)
│   └── build_docx.py / make_figures.py / make_plots.py / write_section1.py / figures/ / tikz/ ← script dựng bản PDF/docx ở trên
├── docs/
│   ├── DE_CUONG.pdf / DE_CUONG.txt    ← [Trọng tâm] BẢN ĐÃ NỘP TRƯỜNG (15 tr., 2026-09-26) + trích text tra cứu
│   ├── DE_CUONG_NOP_TRUONG.md         ← Đề cương nộp trường (bản md; danh tính đã điền từ PDF)
│   ├── 01_Topic_Definition.md         ← Định nghĩa đề tài hiện hành theo baseline 2026-10-19
│   ├── 02_Theoretical_Foundation.md   ← Lý thuyết tham khảo; định nghĩa project-specific cũ đã superseded
│   ├── 03_Literature_Gap_Analysis_Plan.md ← Hồ sơ prior-art nội bộ; không dùng để tuyên bố novelty trong đề cương
│   ├── 04_Hardware_Architecture.md    ← Kiến trúc cảm biến; mô tả actuator AAN cũ đã superseded
│   ├── 05_De_Cuong_Dang_Ky_DRAFT.md   ← Outline cũ — superseded, giữ để truy vết
│   ├── 06_Co_Cau_Co_Khi_Exoskeleton.md ← Khung/nẹp CAD; không xác nhận actuator AAN
│   ├── 07_Vision_TaskState_Architecture.md ← [MỚI 2026-10-19, ĐỀ XUẤT] Đặc tả nhánh camera Gate 3: detector cắm được (OpenCV cổ điển trước), ánh xạ nhãn T_*, hiệu chuẩn, phiếu benchmark còn trống
│   ├── 08_Software_Firmware_Roadmap.md ← [MỚI 2026-10-19, ĐỀ XUẤT] Lộ trình phần mềm/firmware F0–F6; CHƯA viết code, bắt đầu sau khi Gate 0 được duyệt
│   ├── DE_CUONG_A_B_C_DRAFT_2026-10-19.md ← Bản A/B/C đang cập nhật theo lộ trình rehab + AAN tự động + bài tập thìa; chưa duyệt/nộp
│   ├── DE_CUONG_A_B_C_DRAFT_2026-10-19.md ← (cập nhật lần 3, 2026-10-20: PA-2 · M3 · ba tang)
│   ├── DE_CUONG_A_B_C_BAN_NOP_2026-10-20.md ← **BẢN ĐỂ NỘP** (sạch, không nhãn kiểm toán): A 7 mục theo báo cáo mẫu cấp quốc gia · B 7 mục · C 5 mục · TLTK [1]–[15]; **7.934 từ, 129 đoạn, 5 bảng, 157 đoạn DOCX**; ước tính **~15,9 trang (vượt trần 14)**, biến thể 13 pt/1,15 ≈ **13,2 trang vừa trần** (`DEC-PROP-013`); máy trạng thái đã thu về **3 pha** (`DEC-AAN-003`); Mech 9 **chưa bấm giờ**, rút con số 22 giây (`DEC-MECH-009`); Flex **phải mua ở mốc 1**, CD74HC4067 đã chạy thử, ADS1115 chưa xác nhận (`DEC-HW-007`)
│   ├── MO_TA_DU_AN_NGON_NGU_TU_NHIEN_2026-10-20.md ← [MỚI 2026-10-20] **BẢN MÔ TẢ DỰ ÁN BẰNG NGÔN NGỮ TỰ NHIÊN** theo bố cục báo cáo cấp quốc gia 2024–2025 mà chủ dự án cung cấp: A 7 mục · B 7 mục · C 5 mục · TLTK [1]–[15]; 9.050 từ, 142 đoạn, 5 bảng, ~18 trang; thuật ngữ được giải thích bằng lời; **không** chịu trần 14 trang của bản nộp; bìa để trống (`DEC-PROP-012`)
│   ├── DE_CUONG_A_B_C_BAN_TRONG_TAM_2026-10-20.md ← **BẢN TRỌNG TÂM v3 — LỊCH SỬ, trước bản chủ dự án sửa 21/10 (`DEC-PROP-019`); Anti-slop v2 (`DEC-PROP-018`)**: 8 mục sửa đã áp dụng; bìa/mục lục/nội dung, bỏ bảng metadata, B kể theo vấn đề, C.8 văn xuôi, 1 bảng B↔C, phương pháp đo cạnh số liệu, 7 hình chuyển thành câu dẫn + phụ lục. Markdown **9.288 từ**, DOCX **8.987 từ / 7 bảng**; 14 tests + 2 DOCX PASS. Drive **`1jd22OBFOiyv2Fvd3au_cWn2HT8wl4WfQ`**. Chưa xác nhận trần 14 trang; xem `research/reviews/2026-10-20_anti_slop_v2.md`.
│   │   └── lịch sử: v2 `1uGVmpj9eB4U-MPPqKgo7x9wlSMwwm4e4` (`DEC-PROP-017`, 9.349 từ) được thay bằng v3; bình luận `AAACI4Z4AB4`. Bản kho chưa viết lại theo Anti-slop v2.
│   │   └── trước khi dọn văn phong (`DEC-PROP-016`, bản v1 trên Drive): đúng trạng thái ghép cặp trước khi bung (B 8 mục ↔ C 9 mục, A 7 mục) **+1 câu giới hạn phạm vi** ở C.8 (trợ lực theo nhu cầu không phải của đề tài); **9.832 từ / 156 đoạn / 5 bảng / 7 HÌNH → ~19,0 trang @14 pt, ~15,7 trang @13 pt**; DOCX `--check` PASS 188 đoạn/6 bảng/9.662 từ; Drive `13Ii3YG9hXsNPt-v5OdYivkHVws9zPonF` (bình luận `AAACG9bNHBQ` trên v4). **Vẫn vượt trần 14 trang** — ba đường xử lý chưa chốt
│   ├── DE_CUONG_A_B_C_GHEP_CAP_B_C_2026-10-20.md ← [MỚI 2026-10-20] **BẢN GHÉP CẶP B ↔ C THEO ĐỐI TƯỢNG** (chủ dự án đề xuất, `DEC-PROP-014`): B 8 mục với *Cơ sở lý thuyết* + *Thiết kế* cho từng đối tượng và con trỏ sang C; C đổi tên **KIỂM TRA VÀ KIỂM THỬ**, 9 mục trong đó C.1–C.6 cặp 1–1 với B.3–B.8; 8 quy trình đo phân về đúng đối tượng; **ĐÃ BUNG HẾT theo chỉ đạo 2026-10-20 (`DEC-PROP-015`)** → **B 9 mục** (thêm B.9 kiến trúc phần mềm, firmware, lộ trình bảy pha từ `docs/08`) · **C 10 mục** (thêm C.7 kiểm thử phần mềm/mô phỏng/nhật ký phiên; C.8 có thêm **bảng 11 rủi ro + dự phòng**) · **PHỤ LỤC A–F** (thuật ngữ; 13 nhãn tác vụ; cửa sổ thăm dò + 4 phương án đối chiếu; bản đồ 16 kênh; nhật ký phiên tối thiểu; nguồn chờ xác minh) · **18.656 từ / 231 đoạn / 12 bảng / 7 HÌNH → ~35,1 trang @14 pt, ~28,5 trang @13 pt**; DOCX `--check` PASS 271 đoạn/13 bảng/18.091 từ. **Trần 14 trang không còn ràng buộc bản này** — đây là kho nội dung để chủ dự án cắt rồi gửi lại; **bản nộp `…BAN_NOP…` không đụng tới, vẫn giống hệt v4 trên Drive**
│   ├── DE_CUONG_A_B_C_BAN_NHAP_2026-10-20.md ← [MỚI 2026-10-20] **BẢN LÀM VIỆC NỘI BỘ** — cô đọng theo mật độ `11A2.pdf`, giữ nhãn kiểm toán (Phương án A; `DEC-PROP-005/006/007`): A.1–A.4 · B.1–B.7 · C.1–C.6 · TLTK [1]–[15]; **5.519 từ, ước tính 12,4 trang nội dung kể cả 7 hình, vừa trần 14 trang** (`DEC-PROP-006/008`); nhãn bằng chứng `[SƠ BỘ]`/`[MỤC TIÊU]`/`[TÍNH TOÁN]`/`OPEN`, bảng bằng chứng 3 cột, máy trạng thái 7 trạng thái, bảng đăng ký trước chỉ số. Lịch sử 3 lượt dựng + 5 chi tiết thư mục đã sửa: `research/reviews/2026-10-20_11A2_pdf_improvement_plan.md` §10
│   ├── (11A2_CAP_NHAT_DU_THAO_2026-10-19.docx) ← Bản Word review cũ — **KHÔNG lưu trong repo, chỉ có trên Drive** (ID `1YXvVbi53CPcrzXaJQAPZTQ3ugnsjhErd`); chưa đồng bộ hướng mới, không phải bản nộp
│   ├── OUTLINE_BAOCAO_VISEFD.md       ← Outline cũ — superseded
│   └── bao_cao/
│       ├── A1_ly_do_chon_de_tai.md    ← Tiêu chí A của ViSEF
│       ├── A2_muc_tieu.md
│       ├── A3_tieu_chi.md
│       ├── A4_doi_tuong_pham_vi.md
│       ├── A5_dia_diem.md
│       ├── A6_phuong_phap.md
│       └── GLOSSARY.md                ← Phân cấp thuật ngữ cảm biến + tuyên bố bị cấm
├── firmware/
│   └── mega_link_diagnostics/     ← Lưu ý: DI SẢN đề tài cũ (Mega ↔ Orange Pi bring-up). Xem ghi chú trong file
├── research/
│   ├── README.md                  ← Quy trình làm việc trong research/
│   ├── claims/CLAIM_LEDGER.csv    ← Claim + cấp bằng chứng + trạng thái
│   ├── evidence/SOURCE_LEDGER.csv ← Nguồn thật/candidate + trạng thái xác minh
│   ├── context/
│   │   ├── CURRENT_DESIGN_BASELINE.md ← Hướng chức năng hiện hành, AAN tự động, cảm biến/camera và ranh giới bằng chứng
│   │   ├── IMPLEMENTATION_PIPELINE.md   ← Pipeline triển khai/kiểm chứng đề xuất, thresholds vẫn mở
│   │   ├── DECISION_LOG.md        ← Quyết định chính thức (DEC-*), gồm lịch sử và supersession
│   │   ├── PROJECT_SNAPSHOT.md    ← Bản nén ngữ cảnh với cập nhật hiện hành đầu trang
│   │   ├── CONVERSATION_2026-08-25.md     ← Bản nén hội thoại (đề tài cũ, lịch sử)
│   │   └── CONVERSATION_2026-09-13.md     ← Bản nén hội thoại (pivot sang găng tay)
│   ├── protocols/
│   │   ├── 06_glove_hand_GATE_experiment.md   ← GATE đo; AAN cũ superseded, các GATE cần rà soát
│   │   ├── 09_AAN_spool_phantom_and_conditional_volunteer.md ← AAN hiện hành; khung thử có điều kiện
│   │   ├── 10_gate0_task_state_sheet.md ← [MỚI 2026-10-19, ĐỀ XUẤT] Gate 0: tác vụ thìa, nhãn T_*, máy trạng thái chế độ, 5 phương pháp tách vận động tự nguyện khỏi chuyển động do máy
│   │   ├── 10a_gate0_channel_map_and_acquisition_budget.md ← [MỚI 2026-10-19, ĐỀ XUẤT] Gate 0: 4 phương án phân bổ 16 kênh (PA-1/2/3a/3b), ngân sách quét [TÍNH TOÁN], 8 điểm kiểm tra trước khi cấp nguồn
│   │   ├── 10b_channel_map_proposed.csv ← [MỚI 2026-10-19, ĐỀ XUẤT] Bản đồ kênh CH0–CH15 dạng máy đọc được; mọi vị trí lắp còn OPEN
│   │   ├── ISEF_REVIEW_ORCHESTRATION.md       ← Phản biện 6-lane + adjudication
│   │   ├── 04_orangepi5pro_mega2560_bringup_tests.md ← Lưu ý: DI SẢN (Mega), giữ làm tham khảo
│   │   └── 05_velostat_stiffness_GATE_experiment.md  ← Lưu ý: SUPERSEDED (DFU) — không dùng
│   ├── prompts/REVIEWER_DISPATCH_TEMPLATE.md ← Template dispatch reviewer
│   ├── queries/QUERY_LOG.jsonl    ← Log truy vấn (auditable)
│   ├── bench/templates/           ← Template log đo bench
│   ├── reviews/00_EXPLORATION_SUMMARY.md ← Tổng kết hành trình săn đề tài
│   ├── reviews/2026-10-20_cut_list_triage.md ← [MỚI 2026-10-20] **THẨM ĐỊNH DANH SÁCH 16 MỤC CẮT GIẢM TRƯỚC HỘI ĐỒNG**: đồng ý và đã sửa 9 mục, **bác 2 mục có bằng chứng** (Flex không phải "linh kiện ảo"; trích dẫn Penfield/Hebb do chính chủ dự án viết), mục 2 sai một nửa (đúng về cơ chế delta-sigma nhưng **không được bỏ đọc nháp**), 4 mục chờ chủ dự án quyết; phát hiện thêm CD74HC4067 có thể thiếu và ngưỡng 180 mV cao hơn nhiễu nền
│   ├── reviews/2026-09-27_decuong_pdf_sync.md ← [Trọng tâm] ĐỐI CHIẾU BẢN NỘP với repo (F1–F14, G0↔C1, sổ I/L/R, 6 QĐ chờ chốt)
│   ├── reviews/2026-09-19_prior_art_novelty_gate1.md ← [Trọng tâm] KẾT QUẢ RÀ SOÁT PRIOR ART lượt 1 (ma trận + quyết định hạ/nâng novelty)
│   ├── reviews/archive/           ← ~20 báo cáo kill-test (đề tài cũ, lưu lịch sử)
│   ├── notebooklm_sync/           ← Lưu ý: Đồng bộ từ Google NotebookLM. `experiments/01-05` = log bring-up phần cứng thật (`DEC-PHASE-002`, chưa chính thức hoá GATE 0); `chat_transcripts/`, `studio/` = bản ghi chú nháp ban đầu, chỉ dùng để tham khảo nội bộ — không trích trực tiếp vào hồ sơ nộp
│   └── tooling/SETUP_STATUS.md    ← Trạng thái runtime/tooling
├── scripts/
│   ├── bootstrap_research_tooling.sh
│   ├── check_research_environment.py
│   ├── research_log.py
│   ├── tinyfish_search.py
│   ├── build_context_bundle.py
│   ├── build_abc_review_docx.py     ← [MỚI 2026-10-20] Markdown đề cương A/B/C → DOCX rà soát; có `--check` tự kiểm tra (cần `python-docx`)
│   └── install_miktex_debian.sh
├── exports/
│   ├── DE_CUONG_NOP_BAN_KHKT_2026-10-18.docx/.pdf ← bản dựng cho hạn nộp vòng trường 18/10 (`DEC-PROP-003`; lịch sử, không sửa)
│   ├── 11A2_CAP_NHAT_DU_THAO_2026-10-20.docx ← [MỚI 2026-10-20] **BẢN RÀ SOÁT**, dựng từ `docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md`; chưa duyệt toàn văn, không phải bản nộp. Bản sao trên Drive: `11A2_CAP_NHAT_DU_THAO_2026-10-20_BAN_RA_SOAT.docx` (thư mục `01_Cac_file_lam_viec`, ID `1j4D_fxomFLwh4a2Vmok__b77f3hwmi2O`)
│   ├── DE_CUONG_A_B_C_BAN_NOP_2026-10-20.docx ← [MỚI 2026-10-20] **Word BẢN NỘP** (5.723 từ, **143 đoạn ngắn đúng giọng bản mẫu**, 6 bảng, ~12,9 trang; không banner/meta; `--check` PASS). Drive: `DE_CUONG_A_B_C_BAN_NOP_2026-10-20_v2.docx`, ID `11UW8oIMmgNtZ87IWMWbxEO5P61UlaKd0`; bản lượt trước ID `1-jBcBMSKeA_a05STGboKMwXn7AMZYTJa` (bình luận `AAACJEo1aEk`)
│   └── DE_CUONG_A_B_C_BAN_NHAP_2026-10-20.docx ← [MỚI 2026-10-20] Word của bản **nội bộ cô đọng** (5.519 từ, 101 đoạn, 6 bảng; `--check` PASS). Bản sao Drive: `DE_CUONG_A_B_C_BAN_NOP_CO_DONG_2026-10-20_v2.docx`, ID `19cAEh8g02ruoBsPUOL_cj1ebtlZi9N1t` — **nay là bản nội bộ, không dùng để nộp** (bình luận `AAACI37XCmQ`; v1 `176tj3MWVVa6p6tkuw-GCsKzk6GzbdE70`). Bản **đầy đủ** 12.817 từ (ID `1PNVjezxgTSeur_nEdcLXu-BasvFIlLsr`) vẫn còn, giữ làm hồ sơ nội dung, **không dùng để nộp** (bình luận `AAACI3sp9I4`). **Chưa duyệt toàn văn, chưa điền bìa, chưa chèn 7 hình**
└── tools/research_sources.lock.json
```

*(`.tools/sources/`, `.venv/`, `research/{cache,downloads,generated,queries/private}/` là thư mục cục bộ, bị Git ignore.)*

---

## Nội dung chính từng nhóm

### `docs/` — Tài liệu đề tài

- **01_Topic_Definition** [Trọng tâm cao]: tên đề tài, vấn đề, khoảng trống, novelty trung thực, RQ 2 tầng, pipeline, killer experiment, phần cứng.
- **02_Theoretical_Foundation** [Trọng tâm cao] *(§9 "Xử lý tại biên và lượng tử hóa INT8" ĐÃ LOẠI BỎ — `DEC-EDGE-001`)*: phục hồi vận động sau đột quỵ, thang đo lâm sàng (FMA/ARAT/BBT), cơ sinh học bàn tay & lực ngón, vật lý piezoresistive của Velostat, hysteresis/creep/drift, phép đo vi sai, lượng tử hóa INT8, tuyên bố an toàn. Nhãn [Khả thi] chuẩn / [Chờ xử lý] giả thuyết / [Thông tin] cần kiểm chứng.
- **03_Literature_Gap_Analysis_Plan** [Trọng tâm vừa]: 10 nhóm chủ đề cần rà soát + ma trận theo dõi.
- **04_Hardware_Architecture** [Trọng tâm cao]: bố trí 12–24 kênh, MUX, ngân sách độ phân giải ADC, tốc độ khung hình, đường ống dữ liệu.

### `docs/bao_cao/` — Báo cáo theo mẫu ViSEF

- **A.1–A.6**: lý do chọn đề tài, mục tiêu, tiêu chí, đối tượng & phạm vi, địa điểm, phương pháp.
- **GLOSSARY**: phân cấp vật liệu → sensing element → mảng → hệ thống; danh sách **tuyên bố bị cấm**.

### `research/` — Hạ tầng nghiên cứu có kiểm chứng

- **Ledgers**: mọi tuyên bố, nguồn, quyết định, truy vấn đều có vết. Sau lượt rà soát 1 (2026-09-19): SOURCE_LEDGER 114 dòng (24 nguồn mới), QUERY_LOG +13 bản ghi, CLAIM_LEDGER 15 dòng (CLM-NOV-003 → `CONFLICTED`, thêm CLM-NOV-005 + CLM-MET-002).
- **Protocols**: GATE experiment cho đề tài hiện tại + phản biện ISEF 6-lane.
- **Context**: snapshot + nhật ký quyết định + bản nén hội thoại.

---

## Lưu ý: Lịch sử quan trọng (đã xử lý)

- **2026-10-20 (lượt 3–9 — đọc `11A2.pdf` và đề xuất cải thiện trước hạn nộp):** đối chiếu bản 12 trang với sổ quyết định hiện hành → **`research/reviews/2026-10-20_11A2_pdf_improvement_plan.md`**: 9 điểm P0 (trục đề tài vẫn là *"thiết bị đo"* EI/GAP/RAL + 16 ô Velostat + RL trong khi hướng đã chốt là hỗ trợ tập vận động tinh với PA-2 11 kênh + camera + bài tập thìa + ba tang + M3; Bảng 3 mục C.2 trình bày SNR 21,4 dB / R² 0,93 / 25 Hz / 0,00 mV như kết quả đã đạt **mà không có log trong kho** trong khi A.4 gọi chúng là mục tiêu và C.3 nói sẽ kiểm định 10/2026–01/2027; còn ngưỡng ≤ 5 N; Mech 9 "Đạt tối ưu" chưa có CAD; C.6 nói tới thử lâm sàng trên người bệnh) + 8 điểm P1 + ưu tiên cắt trang + 3 phương án bản nền + kế hoạch theo quỹ thời gian. Ghi nhận những chỗ PDF **đã tốt hơn** bản DOCX 17/10 (GAP đúng chiều, Manumeter đúng đại lượng, câu chặn về vỏ não, nguồn Penfield/Hebb). **`DEC-PROP-005` đã duyệt (Phương án A)** và **`DEC-PROP-006`** chốt ≤14 trang nội dung + 1 bìa cùng nguyên tắc "đề cương không phải báo cáo toàn văn" → đã dựng `docs/DE_CUONG_A_B_C_BAN_NHAP_2026-10-20.md` + `exports/DE_CUONG_A_B_C_BAN_NHAP_2026-10-20.docx` (builder PASS; `scripts/build_abc_review_docx.py` thêm cờ `--banner/--status/--meta/--spacing/--size`). Sau đó chủ dự án chỉ đạo **`DEC-PROP-007`** (*"viết hoàn thành B/C luôn đi, phần A tham khảo bản cũ"*) → B mở thành 10 tiểu mục, C thành 9 tiểu mục (12.817 từ, 8 bảng) và **đã tải lên Drive thành tệp mới**: `DE_CUONG_A_B_C_BAN_DAY_DU_2026-10-20.docx` (ID `1PNVjezxgTSeur_nEdcLXu-BasvFIlLsr`), `2026-10-20_11A2_pdf_improvement_plan.md` (ID `1viIe0njVXkH0TCaCQFlOzDXPwkJopTpw`), bình luận `AAACI4VCoFs` + `AAACJDB1Y4w`. **⚠ Bản đầy đủ ước tính 24–26 trang, vượt trần 14 trang** → chủ dự án chỉ ra nguyên nhân (*"quá nhiều câu xã giao"*) và ra **`DEC-PROP-008`**: viết lại cô đọng theo mật độ bản mẫu rồi nén câu thêm một lượt → **5.519 từ, ước tính 12,4 trang nội dung, vừa trần**; tệp để nộp trên Drive `DE_CUONG_A_B_C_BAN_NOP_CO_DONG_2026-10-20_v2.docx` (ID `19cAEh8g02ruoBsPUOL_cj1ebtlZi9N1t`), bản đầy đủ giữ lại làm hồ sơ nội dung (bình luận `AAACI3sp9I4`). Sáu quy tắc mật độ vào `research/tooling/WRITING_STYLE_PROFILE.md`. Rồi chủ dự án yêu cầu **bản chuẩn để nộp** và gạch các câu *"sặc mùi trợ lí"* → **`DEC-PROP-009`**: dựng tệp riêng `DE_CUONG_A_B_C_BAN_NOP_2026-10-20` bỏ mọi câu meta/kiểm toán, mã nội bộ và nhãn trạng thái (**5.627 từ, ~12,7 trang**); rồi chủ dự án chỉ ra vẫn **sai giọng văn** và đưa ví dụ tự viết → **`DEC-PROP-010`**: viết lại thành **143 đoạn ngắn (~43 từ/đoạn), 5.723 từ, ~12,9 trang**, Drive ID `11UW8oIMmgNtZ87IWMWbxEO5P61UlaKd0`; bản `…BAN_NHAP…` giữ làm bản nội bộ. Cùng ngày chủ dự án **loại bỏ vai trò edge-AI của Orange Pi 5 Pro** (`DEC-EDGE-001`): bỏ lượng tử hóa INT8/RKNN, suy luận NPU ≤ 20 ms, mô hình RL bù trôi/trễ (GATE EDGE/M6) và nhiệm vụ kiểm chứng thuật toán gắn nhãn "Nghi vấn"; Orange Pi 5 Pro chỉ còn nhánh thị giác, còn việc loại phiên đo lỗi chuyển sang trạng thái `INVALID`. 12 tài liệu còn sống đã gắn banner; tệp đã nộp/lịch sử không bị sửa. Vẫn phải **đếm trang thật trong Word**. **Không sửa `11A2.pdf`/`11A2.docx`; chưa commit.**
- **2026-10-20 (lượt 10 — thẩm định danh sách 16 mục "xem xét loại bỏ/cắt giảm" trước hội đồng ViSEF/ISEF):** chủ dự án đưa danh sách xếp 3 cấp độ rủi ro và link `11A2_ban_gop_hoan_thien.docx` (Drive ID `1f8zHjhmekds0TzaTcMi9UqzywXxLHb_B`) — đối chiếu cho thấy bản đó **ghép từ chính đề cương A/B/C** của dự án, nên phần lớn các mục nhắm vào câu chữ của bản ghép. Agent **đối chiếu từng mục với hồ sơ repo trước khi sửa**: **đồng ý và đã sửa 9 mục** → `research/reviews/2026-10-20_cut_list_triage.md` + `DEC-ACQ-002`/`DEC-MECH-008`/`DEC-PROP-011`: cơ chế đọc nháp ADS1115 viết lại đúng kiến trúc delta-sigma; **ngưỡng vùng chết 180 mV bị đặt lại thành chưa đạt** vì cao hơn nhiễu nền đã ghi nhận 50–135 mV nên có thể nuốt tín hiệu nỗ lực sớm và làm hỏng phép đo EI; bỏ "giám sát dòng servo" (không có điện trở shunt) và thu `FAULT` về các điều kiện phần mềm phát hiện được; bỏ ngụ ý servo tự nhả khi mất nguồn (hộp số tỉ số lớn không quay ngược được) và lấy chốt mở nhanh làm đường thoát an toàn; GAP nói rõ không do phần mềm găng tự xuất theo độ; kênh REF định vị lại thành cổng kiểm soát chất lượng về trôi nền/môi trường, **không** bù được dão tải của ngón; Mech 9 nếu không có biên bản thì 22 s và 50 chu kỳ chuyển thành chỉ tiêu của mốc 2; bỏ thuật ngữ "đăng ký trước/pre-registered" và "ablation study"; thêm đoạn tình trạng thiết bị ở C.3 và nói rõ **chưa có buổi đo nào trên giàn cơ học**; ≤ 20 ms làm rõ chỉ áp dụng cho đường cảm biến → lệnh servo (một chu kỳ phơi sáng ở 30 fps đã là 33,3 ms). **Bác 2 mục có bằng chứng:** mục 4 gọi 3 Flex là "linh kiện ảo do AI tự thêm" trong khi `PROJECT_SNAPSHOT` ghi *owner confirmed three Flex sensors* và chủ dự án đã duyệt PA-2 = 3 Flex + 6 Velostat + 2 REF; mục 7 đòi bỏ Penfield/Hebb trong khi chính chủ dự án viết đoạn A.2.1 đó và chữ "Dashboard" bị phê phán nằm ở bản ghép. **Mục 2 sai một nửa:** ADS1115 đúng là delta-sigma nhưng lần chuyển đổi đầu sau đổi kênh vẫn chứa mẫu kênh cũ nên **sửa giải thích và giữ đọc nháp**. **Phát hiện ngoài danh sách:** `EQUIPMENT_AND_ACCESS.md` ghi **CD74HC4067 "[Chưa xác định] — món duy nhất ở Lớp 1 có thể còn thiếu"**, ADS1115 cũng chưa xác nhận, và **không có dòng nào cho Flex**, trong khi toàn bộ cấu hình 11 kênh phụ thuộc chúng. Bản nộp tăng 5.723 → **6.315 từ**, 147 đoạn, ước tính **~13,9 trang**, chỉ còn ~0,1–0,2 trang dự phòng. `11A2_ban_gop_hoan_thien.docx` **không bị sửa** — 5 mục cần sửa ở bản ghép được liệt kê trong tệp thẩm định. **Chờ 4 quyết định của chủ dự án; chưa commit.**
- **2026-10-19 (lượt 2 — lượt tài liệu Gate 0):** theo chỉ đạo chủ dự án *"hoàn thiện đề cương rồi mới bắt đầu code"*, agent soạn bộ artifact Gate 0 (`protocols/10`, `10a`, `10b`), đặc tả nhánh camera (`docs/07`) và lộ trình phần mềm/firmware (`docs/08`), tất cả ở mức `PROPOSED`; bổ sung §C.4 (đăng ký trước chỉ số/ngưỡng) và §C.5 vào đề cương A/B/C; thêm 6 mã đề xuất `DEC-TASK-001/002`, `DEC-CHMAP-001`, `DEC-ACQ-001`, `DEC-VIS-001`, `DEC-IMPL-001/002` và 6 claim `CLM-TASK-001`, `CLM-ACQ-001/002`, `CLM-HW-006`, `CLM-VIS-002`, `CLM-IMPL-001`. **Không điền ngưỡng/thông số nào; không viết code; không chạy benchmark; không đo phần cứng; không sửa hồ sơ đã nộp hay file nguồn Drive; chưa commit GitHub.** Hai điểm kỹ thuật mới phát hiện cần kiểm tra: `CLM-HW-006` (giới hạn điện áp đầu vào ADS1115 so với ghi nhận "đọc 0–3,3 V") và `CLM-ACQ-002` (bảng tốc độ khung cũ ở `docs/04` §5 không áp dụng cho chuỗi ADS1115 hiện hành). Chi tiết: `research/reviews/2026-10-19_gate0_packet_and_abc_review.md`.
- **HISTORICAL — 2026-10-11 (phần phạm vi đã superseded 2026-10-19):** đồng bộ bản đề cương `de_cuong/DE_CUONG_NGHIEN_CUU.pdf` và ghi nhận AAN là trụ cột kỹ thuật (`DEC-SCOPE-006`), khi đó còn giới hạn phantom-only. Phạm vi thử hiện hành được thay bằng `DEC-SCOPE-007`/`DEC-AAN-002`: AAN là mục tiêu chính, servo cuốn dây trực tiếp, phantom trước và tình nguyện viên chỉ sau đánh giá an toàn/phê duyệt. Các ghi nhận khác về bring-up (`DEC-PHASE-002`) và hồ sơ/tên vẫn cần đọc trong decision log theo ngày. Cập nhật README (§1, §6.1 mới, §8, §10, §11, lịch sử), quy định an toàn (§2 ranh giới AAN + cảnh báo cấp bằng chứng của notebooklm_sync), DECISION_LOG (+5), CLAIM_LEDGER (+3), SOURCE_LEDGER (+6).
- **2026-08-25:** đề tài "đệm khí thích ứng + AAC" bị **xóa toàn bộ** theo DEC-TOPIC-003 (lịch sử còn trong git).
- **2026-08-26:** chốt Hướng C — lót giày Velostat theo dõi độ cứng mô gan chân (sàng lọc DFU).
- **2026-08-28:** **PIVOT** — bỏ DFU vì GATE 3 (Usefulness) yếu; chuyển sang **găng tay theo dõi chức năng bàn tay sau đột quỵ** (DEC-TOPIC-018).
- **2026-09-13:** chốt **tên đề tài chính thức** (DEC-TOPIC-019), chuyển phần cứng từ Arduino Mega 2560 sang **ESP32-S3 + CD74HC4067** (DEC-HW-003), chốt **bố trí kênh** (DEC-HW-004), cập nhật đồng bộ toàn repo + push GitHub.
- **2026-09-27:** đồng bộ **bản đã nộp `docs/DE_CUONG.pdf`** (15 tr., tạo 2026-09-26) → `research/reviews/2026-09-27_decuong_pdf_sync.md`: đội hình 2 người + GVHD Lê Công Long, lĩnh vực Nhúng, timeline 09/2026–01/2027; tên quay về `DEC-TOPIC-019` (README cũ ghi `DEC-TITLE-001` "chốt" là quá thẩm quyền — chưa từng vào log); `GAP = PROM − AROM`; ngưỡng C1.x; kiến trúc ADS1115+INA333; môi trường cài lại (10/11 check). 6 quyết định + 7 nguồn + 3 claim chờ nhóm thống nhất.
- **2026-09-19 (11):** `docs/DE_CUONG_NOP_TRUONG.md` = **bản đề cương nộp nhà trường** (13 mục + Phụ lục A): tính mới theo tiêu chí ViSEF/ISEF với bảng đối chiếu 8 công trình/sản phẩm, ảnh hưởng chia 3 loại, cơ sở lý thuyết + nguyên lý hoạt động, 10 ngưỡng đăng ký trước khi đo, ngân sách dự toán theo 4 lớp. `docs/05` thành outline nội bộ. Thêm `SRC-VN-STROKE-EPI-2025`, `SRC-COCHRANE-UE-2014`, `SRC-HENDRICKS-2002-MOTORRECOVER` (UNVERIFIED — ghi lại một chỗ **trích sai nguồn** trong A.1) và `CLM-BIO-003/-004`. *(2026-09-27: đã điền 4 ô danh tính từ bản PDF đã nộp.)*
- **2026-09-19 (10):** nhóm nghiên cứu chốt 2 việc — **`DEC-ROLE-001`: không nêu danh tính KTV trong hồ sơ nộp** (đã sửa `docs/05` §9.6, `protocols/07` §7; `A.5` còn nợ 1 chỗ) và **`DEC-PHASE-001`: vẫn pha lý thuyết** (không firmware, không script). Để GATE 0 vẫn chạy được: **`research/protocols/08a_gate0_bench_sheets.md`** — phiếu đo in được dùng toàn số nguyên + checklist 8 ảnh, và `protocols/08` thêm **G0.0** (chọn định nghĩa nhiễu A/B trước khi đo).
- **2026-09-19 (9):** nhóm nghiên cứu khai báo **đã có** Velostat + ESP32-S3 + Orange Pi 5 Pro + băng đồng và có **chị là KTV VLTL-PHCN 10 năm** → `DEC-RESOURCE-001` + `SRC-OWNER-2026-09-19-RESOURCES/-KTV10Y` + kiểm kê `research/context/EQUIPMENT_AND_ACCESS.md` + ranh giới sử dụng KTV ở `research/protocols/07` §7. Verdict đầu tư: **giải ngân được Lớp 0–1 về tiền**, nhưng **ngưỡng vẫn phải chốt trước khi đo** và **không đo trên người nhà**.
- **2026-09-19 (8):** đọc **toàn văn** báo cáo dự thi "Xe lăn tự hành ALS" (QG 2024–2025, lĩnh vực **Hệ thống nhúng**, 15 trang) do nhóm nghiên cứu cung cấp → `research/reviews/2026-09-19_benchmark_xe_lan_ALS_QG2025.md` + `SRC-XELAN-ALS-QG2025-REPORT` (READ_FULL) + `CLM-MET-004` (ngân sách hình thức). Kết luận: phương pháp của ta **trên** chuẩn thắng cuộc; vật thật + con số **dưới** (bằng 0). Khuyến nghị đổi lĩnh vực dự thi sang **Hệ thống nhúng**.
- **2026-09-19 (7):** nhóm nghiên cứu: thời gian **đủ** → lên kế hoạch cho cả 7 cổng (`DEC-PLAN-001`). Viết **`research/protocols/08_gate0_execution_plan.md`**: GATE 0 tách thành Q1 (độ nhạy `γ`) + Q2 (cửa sổ đọc được `R₀ ≤ R_max`), thêm thí nghiệm quét trở nguồn đo `R_max` + ENOB thật, log trôi ≥10 ngày, 9 ngưỡng **ĐỀ XUẤT — chờ nhóm nghiên cứu chốt**, cây quyết định khi fail, schema log. **Không viết script** theo chỉ thị.
- **2026-09-19 (6):** trả lời câu "đi xa được tới đâu" → **`research/reviews/2026-09-19_project_ceiling.md`** (trần theo 3 trục: hội thi / xuất bản / sản phẩm, 5 đòn bẩy, 5 rủi ro; 3 mục đã đưa vào `docs/05` §8c). Toàn bộ phán đoán ở đó là **judgment, không phải số đo**.
- **2026-09-19 (5):** làm mục (1)+(4) nhóm nghiên cứu yêu cầu → `docs/02` §5.5 (mô hình chuỗi đo + cửa sổ preload) và `GAP1 review §6` (sửa 3 lỗi danh tính nguồn, thêm `SRC-TW-SPASTICITY-2022` là đối thủ trực tiếp); tra bằng sáng chế theo phân loại = **bất khả thi** (ghi `docs/03` §7). Soạn **`docs/05_De_Cuong_Dang_Ky_DRAFT.md`** để nộp trường (chờ `DEC-SCOPE-004`).
- **2026-09-19 (4):** nhóm nghiên cứu chốt phạm vi **E4+E5+E6** (`DEC-SCOPE-003`) nhưng chỉ đạo *giai đoạn này tập trung vào cơ sở lý thuyết*: đã viết `docs/02` §1.4–§1.6/§3.4/§5.4/§7.3/§8.3; **hoãn** chốt ngưỡng GATE A′/RAL và **hoãn** viết script; không trích dự án tham chiếu ISEF 2025 vào hồ sơ nộp.
- **2026-09-19 (3):** xác minh chuẩn tham chiếu hội thi: `SRC-ISEF-2025-ROBO065T` (ISEF 2025, giải Tư, THPT thị xã Quảng Trị, thuần tích hợp YOLO11+Nav2+Gemma2+Telegram, 4 con số tự đo) → hiệu chỉnh khuyến nghị: **E5 nâng lên nên làm**, E3 bỏ vì đạo đức/thời gian chứ không phải vì novelty (`review §11–§13`, `DEC-SCOPE-002c`).
- **2026-09-19 (2):** nhóm nghiên cứu đề xuất hướng "tập chủ động có trợ lực (AAT)". Phân tích phạm vi + kiểm toán 12 tuyên bố + ma trận va chạm prior art (16 dòng nguồn mới, chưa đọc toàn văn) → `research/reviews/2026-09-19_active_assisted_scope_options.md`; bản nháp lý thuyết đã viết lại an toàn cho báo cáo → `docs/bao_cao/A7_AAT_rationale_DRAFT.md`. **Chờ `DEC-SCOPE-002`** (E1/E2-lite/E3).
- **2026-09-19:** **lượt rà soát prior art 1 (Gap 1)** — 3 nguồn `UNVERIFIED` đã xác minh danh tính; 24 nguồn mới vào ledger; kết quả: **hạ bậc novelty A** (nguyên lý vách→hướng đã có 2015; ART-Glove 2026 làm vỏ cứng + da áp điện trở), **nâng C lên trọng tâm**; thêm mốc y văn (STEF MDC 12,7; Manumeter MDC ~31%) vào GATE B/C **không đổi ngưỡng**. Chờ `DEC-NOV-001`. Chi tiết: `research/reviews/2026-09-19_prior_art_novelty_gate1.md`.

Các file trong `research/reviews/archive/`, `research/protocols/04-05`, `firmware/mega_link_diagnostics/` là **di sản** của các đề tài đã bị loại. **Không dùng làm cơ sở cho đề tài hiện tại.**
