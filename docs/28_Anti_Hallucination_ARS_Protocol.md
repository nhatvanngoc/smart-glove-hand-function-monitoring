# Quy trình chống ảo giác cho nghiên cứu Velostat + SOFA

Ngày cập nhật: 2026-07-28

## 1. Nguyên tắc chung

Từ giai đoạn này, mọi khẳng định kỹ thuật quan trọng trong dự án phải được phân loại thành một trong bốn nhóm:

| Nhóm | Ý nghĩa | Cách dùng trong báo cáo |
|---|---|---|
| Đã xác minh | Có nguồn tin cậy hoặc dữ liệu thực nghiệm của dự án | Có thể viết như kết luận có điều kiện |
| Có bằng chứng hỗ trợ | Có tài liệu/paper hỗ trợ nhưng chưa đo trên prototype của ta | Viết như cơ sở tham khảo |
| Giả định mô phỏng | Tham số chưa có dữ liệu, dùng để chạy mô hình ban đầu | Phải ghi rõ là giả định |
| Chưa xác minh | Chưa có nguồn hoặc dữ liệu | Không dùng làm kết luận |

Không dùng dữ liệu mô phỏng placeholder để khẳng định định lượng về phần cứng thật.

## 2. Cách áp dụng ARS skill

Dự án sẽ dùng các vai trò từ Academic Research Suite theo dạng inline role-prompt:

1. **Source Verification Agent**
   - kiểm tra nguồn;
   - phân loại chất lượng bằng chứng;
   - đánh dấu thông tin chưa xác minh.

2. **Devil's Advocate Agent**
   - phản biện giả định;
   - tìm điểm yếu;
   - kiểm tra khả năng kết luận bị vượt quá bằng chứng.

3. **Experiment Agent**
   - lập kế hoạch thí nghiệm;
   - kiểm tra tính tái lập;
   - phân biệt mô phỏng, đo thực nghiệm và kết luận.

4. **Synthesis Agent**
   - chỉ tổng hợp sau khi nguồn đã được kiểm tra;
   - không được biến giả định thành sự thật.

## 3. Cơ chế phản biện nhiều vai trò

Mỗi mô hình hoặc quyết định kỹ thuật sẽ đi qua ba vai trò phản biện:

```text
Agent A - Người ủng hộ mô hình
Agent B - Người phản biện điện tử/cảm biến
Agent C - Người phản biện cơ học/SOFA
Agent D - Người phản biện học thuật/clinical relevance
```

Sau đó mới có phần:

```text
Consensus / Quyết định tạm thời
Danh sách điều kiện phải kiểm chứng
```

Lưu ý: trong môi trường hiện tại, đây là cơ chế phản biện nội tuyến dựa trên ARS role prompts, không phải nhiều model độc lập. Nếu cần cross-model thật, phải cấu hình API riêng và xin xác nhận trước khi gửi nội dung ra ngoài.

## 4. Quy tắc dùng TinyFish API

Không ghi API key vào file dự án.

Script an toàn đã tạo:

```text
scripts/tinyfish_search.py
```

Cách chạy trong WSL:

```bash
export TINYFISH_API_KEY='YOUR_KEY_HERE'
python scripts/tinyfish_search.py "velostat" outputs/reports/tinyfish_velostat.json
```

Sau khi có file JSON, dữ liệu sẽ được đưa vào source verification matrix.

## 5. Quy tắc trích dẫn

Mọi claim lấy từ nguồn ngoài phải đi kèm:

```text
nguồn URL
loại nguồn: datasheet / product page / peer-reviewed paper / preprint / blog
mức độ tin cậy
ngày truy cập
claim được hỗ trợ
claim không được hỗ trợ
```

## 6. Quy tắc cho Velostat

Các claim đã đủ an toàn ở thời điểm hiện tại:

1. Velostat/Linqstat là vật liệu dẫn điện nhạy áp; khi ép thì điện trở giảm.
2. Tấm đang xét có kích thước 280 × 280 mm, dày 0.1 mm theo product page.
3. Có thể dùng copper tape làm điện cực sandwich trên/dưới Velostat.
4. Velostat có tính phi tuyến, hysteresis và drift; cần hiệu chuẩn thực nghiệm.

Các claim chưa được phép khẳng định định lượng:

1. Đường R(P) chính xác của sensor 50 × 50 mm.
2. Sai số áp suất mmHg của hệ thống thật.
3. Độ bền lâu dài trong môi trường đệm khí.
4. Độ chính xác y sinh/clinical grade.

## 7. Cổng chất lượng trước khi viết báo cáo

Trước khi đưa một kết luận vào báo cáo, phải trả lời:

```text
Nguồn nào hỗ trợ?
Có nguồn nào phản đối hoặc cảnh báo không?
Đây là dữ liệu từ datasheet, mô phỏng hay thực nghiệm của ta?
Nếu là mô phỏng, tham số nào là giả định?
Nếu là thực nghiệm, cỡ mẫu và điều kiện đo là gì?
Kết luận có vượt quá dữ liệu không?
```
