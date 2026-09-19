# Research workspace

Thư mục này giữ ngữ cảnh dài hạn, provenance truy vấn, claim/evidence ledger và quy trình phản biện. Mục tiêu: mỗi lần tiếp tục dự án có thể phục hồi trạng thái bằng artifact thay vì dựa vào trí nhớ hội thoại.

## Cấu trúc

```text
research/
├── claims/CLAIM_LEDGER.csv                 # claim, cấp bằng chứng, trạng thái, hành động
├── context/PROJECT_SNAPSHOT.md             # bản nén ngữ cảnh do người/agent kiểm tra
├── context/DECISION_LOG.md                  # quyết định có ngày, chủ sở hữu, trạng thái
├── context/CONVERSATION_2026-08-25.md      # bản nén hội thoại (đề tài cũ — lịch sử)
├── context/CONVERSATION_2026-09-13.md      # bản nén hội thoại (pivot sang găng tay)
├── evidence/SOURCE_LEDGER.csv               # nguồn thật/candidate và trạng thái verification
├── protocols/ISEF_REVIEW_ORCHESTRATION.md  # vai trò phản biện 6-lane + quality gates
├── protocols/06_glove_hand_GATE_experiment.md # ⭐ GATE experiment CHO ĐỀ TÀI HIỆN TẠI
├── protocols/04_* 05_*                      # ⚠️ DI SẢN đề tài đã bị loại — không dùng
├── prompts/REVIEWER_DISPATCH_TEMPLATE.md    # prompt dispatch role độc lập/adjudicator
├── queries/QUERY_LOG.jsonl                  # log truy vấn audit được
├── reviews/00_EXPLORATION_SUMMARY.md        # tổng kết hành trình săn đề tài
├── reviews/archive/                         # ~20 báo cáo kill-test (lịch sử)
└── tooling/SETUP_STATUS.md                   # trạng thái runtime và tooling
```

Các đường dẫn `research/cache/`, `downloads/`, `generated/`, và `queries/private/` bị Git ignore. Không lưu API key, dữ liệu định danh người tham gia, consent form đã ký, hay raw health data vào Git.

## Quy trình mỗi phiên

1. Đọc `context/PROJECT_SNAPSHOT.md`, các decision còn mở và claim `BLOCKED/CONFLICTED/UNVERIFIED`.
2. Log truy vấn trước hoặc ngay sau khi tìm kiếm:

   ```bash
   python scripts/research_log.py \
     --kind search \
     --engine web \
     --query 'exact search terms' \
     --purpose 'claim or gap being checked' \
     --status complete \
     --summary 'what was and was not established' \
     --sources SRC-ID-1 SRC-ID-2
   ```

3. Tìm kiếm có thể chạy qua `scripts/tinyfish_search.py`; script tự log truy vấn và lưu raw candidate results vào thư mục ignored. Dùng `--private-log` nếu nội dung tìm kiếm không phù hợp để commit. API key chỉ đọc từ environment.
4. Đưa nguồn được chọn vào `evidence/SOURCE_LEDGER.csv`; ghi rõ `VERIFIED`, `PARTIAL`, `UNVERIFIED`, hoặc `REJECTED`.
5. Cập nhật claim ledger. Không nâng trạng thái nếu nguồn chỉ hỗ trợ claim gần giống.
6. Với thay đổi lớn, chạy review protocol và giữ dissent cho đến bước adjudication.
7. Cập nhật snapshot, rồi tạo packet giới hạn kích thước:

   ```bash
   python scripts/build_context_bundle.py --budget-chars 40000
   ```

   Output ở `research/generated/context_bundle.md` (không commit). Packet dùng để định tuyến context, không phải bằng chứng. Đặt `SOURCE_DATE_EPOCH=<unix-seconds>` để tạo output byte-for-byte lặp lại từ cùng source state.

## Quy tắc chống ảo giác tối thiểu

- “Không tìm thấy trong một truy vấn” chỉ cho phép gắn `UNVERIFIED`, không chứng minh nguồn không tồn tại.
- Kết quả synthetic luôn kèm nhãn synthetic/simulation.
- Mọi con số hiệu suất, latency, accuracy, cost và novelty phải có source/evidence ID.
- Giá trị chuẩn giáo trình (GRF, phần trăm pha dáng đi…) phải đối chiếu chương/trang gốc trước khi trích dẫn trong bài nộp.
- Với đề tài găng tay (2026-09-19): cặp đối xứng + ô tham chiếu chỉ **giảm** drift đồng pha, không "triệt tiêu"; mọi giá trị lực/góc khớp là **suy luận** và phải qua hiệu chuẩn từng kênh với load cell tham chiếu — không phải hằng số vật liệu Velostat.
- Không chẩn đoán đột quỵ/mức độ liệt; không thay thế FMA/ARAT/BBT; không "lực hướng ⇒ tiến triển lâm sàng" khi chưa qua GATE C.
- **Prior art:** "không tìm thấy" ≠ "chưa ai làm". Sau lượt rà soát 1 (2026-09-19) thì **cấm** các câu: "hệ thống đầu tiên theo dõi tại nhà", "đo hướng bằng vách là nguyên lý mới", "không dùng IMU nên mới" — xem `research/reviews/2026-09-19_prior_art_novelty_gate1.md`.
- Không thử nghiệm người tham gia trước IRB/SRC pre-approval hợp lệ.
- Không gọi review nội tuyến hoặc nhiều vai trò trong cùng context là “independent multi-agent review”.
