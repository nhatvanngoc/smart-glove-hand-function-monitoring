# Research workspace

Thư mục này giữ ngữ cảnh dài hạn, provenance truy vấn, claim/evidence ledger và quy trình phản biện. Mục tiêu là làm cho mỗi lần tiếp tục dự án có thể phục hồi trạng thái bằng artifact thay vì dựa vào trí nhớ hội thoại.

## Cấu trúc

```text
research/
├── claims/CLAIM_LEDGER.csv                 # claim, cấp bằng chứng, trạng thái, hành động
├── context/PROJECT_SNAPSHOT.md             # bản nén ngữ cảnh do người/agent kiểm tra
├── context/DECISION_LOG.md                  # quyết định có ngày, chủ sở hữu, trạng thái
├── evidence/SOURCE_LEDGER.csv               # nguồn thật/candidate và trạng thái verification
├── protocols/ISEF_REVIEW_ORCHESTRATION.md  # vai trò phản biện + quality gates
├── prompts/REVIEWER_DISPATCH_TEMPLATE.md    # prompt dispatch role độc lập/adjudicator
├── queries/QUERY_LOG.jsonl                  # log truy vấn audit được
├── reviews/2026-08-16_baseline_intake.md   # rà soát sơ bộ tài liệu đầu vào
└── tooling/{SETUP_STATUS,SMOKE_TESTS}.md     # trạng thái runtime và kiểm thử
```

Các đường dẫn `research/cache/`, `downloads/`, `generated/`, và `queries/private/` bị Git ignore. Không lưu API key, dữ liệu định danh người tham gia, consent form đã ký, hay raw health data vào Git.

## Quy trình mỗi phiên

1. Đọc `context/PROJECT_SNAPSHOT.md`, các decision còn mở và claim `BLOCKED/CONFLICTED`.
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
- Mọi con số y khoa, hiệu suất, latency, accuracy, cost và novelty phải có source/evidence ID.
- `32 mmHg` không phải universal cutoff.
- Không thử nghiệm người tham gia trước IRB/SRC pre-approval hợp lệ.
- Không gọi review nội tuyến hoặc nhiều vai trò trong cùng context là “independent multi-agent review”.
