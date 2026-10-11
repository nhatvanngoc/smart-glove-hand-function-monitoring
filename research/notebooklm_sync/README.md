# NotebookLM Research & Technical Knowledge Base Sync

Thư mục này đồng bộ toàn bộ tài liệu nghiên cứu, nhật ký thực nghiệm phần cứng, sản phẩm Studio và biên bản thảo luận học thuật từ Google NotebookLM:
- **Notebook:** `Stroke Rehabilitation and Robotic Glove`
- **ID:** `b7170836-6696-4e0f-8985-dafd233d135f`
- **Tổng số nguồn tài liệu:** 43 nguồn (Y học phục hồi chức năng, cảm biến áp điện trở Velostat, cơ cấu AAN, vi sai 2 vách, ART-Glove 2026, chuẩn đo lường lâm sàng).

## Cấu trúc thư mục

```
research/notebooklm_sync/
├── experiments/             # 5 tài liệu nhật ký & báo cáo thực nghiệm đo kiểm phần cứng
│   ├── 01_tong_ket_ky_thuat_chuoi_phan_cung_da_kenh.md
│   ├── 02_ket_qua_thuc_nghiem_quet_da_kenh_cd74hc4067_ina333_ads1115.md
│   ├── 03_danh_gia_dang_song_quet_da_kenh_sau_toi_uu_toc_do.md
│   ├── 04_ky_thuat_ghep_noi_ina333_ads1115_esp32s3_cho_velostat.md
│   └── 05_nhat_ky_thuc_nghiem_do_kiem_ina333_ads1115_cd74hc4067.md
├── studio/                  # Báo cáo tổng hợp, Sơ đồ tư duy, Bảng thuật ngữ, Trắc nghiệm
│   ├── Stroke Rehabilitation and Robotic Glove.md
│   ├── Bảng Tổng Hợp Thuật Ngữ và Thông Số Dự Án Găng Tay Thông Minh.csv
│   ├── Sơ đồ tư duy Dự án Găng tay Thông minh Phục hồi Chức năng.json
│   ├── Tai biến Sơ đồ tư duy.json
│   └── Găng tay Trắc nghiệm.json
├── chat_transcripts/        # Toàn văn đối thoại phản biện học thuật & thiết kế mạch
│   └── 2026-10_chat_transcript_stroke_rehab_notebooklm.md
└── audio/                   # Audio Overviews tóm tắt dự án (.m4a - gitignored)
```

## Các điểm nhấn kỹ thuật quan trọng đã xác thực:
1. **INA333:** Thiết lập mốc tĩnh $V_{REF} \approx 1.65\text{V}$ (Virtual Ground), $G \approx 6.5$ lần, dải động an toàn $0.06\text{V} - 1.62\text{V}$.
2. **ADS1115 + ESP32-S3:** Ngắt phần cứng chân `ALRT` nối GPIO 10 (`Falling Edge ISR`), Continuous Mode 860 SPS triệt tiêu jitter và rớt mẫu.
3. **CD74HC4067:** Chèn thời gian trễ xác lập `delayMicroseconds(120)` sau mỗi lần chuyển kênh triệt tiêu nhớ áp ký sinh trên chân SIG.
4. **Auto-Tare:** Lấy trung bình 100 mẫu baseline sau 500 ms đầu khởi động để tự động cân bằng mốc 0 về $0.0\text{ mV}$.
