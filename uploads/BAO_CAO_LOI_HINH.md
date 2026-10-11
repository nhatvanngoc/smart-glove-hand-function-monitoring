# Kiểm tra lỗi 16 hình trong DE_CUONG_NGHIEN_CUU (6).docx

Phương pháp: giải nén `word/media/*` (16 PNG), ánh xạ theo thứ tự xuất hiện trong `document.xml`
(rId10→Hình 1 … rId25→Hình 16), soi từng hình bằng vision (kèm crop phóng to vùng nghi vấn:
Hình 6, 7, 9, 10) và đo pixel chiều dài cột ở Hình 1(b).

## A. Lỗi nội dung / dữ liệu (nặng)

| # | Hình | Lỗi |
|---|------|-----|
| A1 | Hình 1(b) | **Nhãn và chiều dài cột tráo nhau**: cột 1 vẽ ≈ 80% nhưng ghi "50% (còn di chứng)"; cột 3 vẽ ≈ 50% nhưng ghi "80%". Đối chiếu正文: tổn thương chi trên giai đoạn sớm ≈ 80%, còn vấn đề bàn tay sau 4 năm ≈ 50% → nhãn đúng phải là 80% / 50% / 50%. |
| A2 | Hình 4(b) | Đường d (xanh lá) ở khung (b) **bị cắt cụt** bởi cạnh dưới khung hình (ylim không đối xứng quanh 0); caption nói "đường nét đứt d = 0 nằm chính giữa ở cả ba khung" nhưng trong hình nó nằm sát mép dưới → caption sai so với hình. |
| A3 | Hình 7 | **Điểm đấu dây sai**: dây vào ngõ "+" tapping vào *giữa thân* zigzag của R_palmar (không phải node V₁) rồi **cắt ngang qua thân R_dorsal** của nhánh phải; dây vào ngõ "−" tapping vào giữa R_ref nhánh phải (không phải node V₂). Hai chấm node V₁, V₂ không nối đi đâu. Sai hẳn so với caption "đưa hai điểm giữa V₁, V₂ vào hai ngõ vào riêng". |
| A4 | Hình 13 | Hai vòng tròn đánh dấu RAL nằm **trên đường ngưỡng 80%** chứ không nằm trên điểm dữ liệu: tại 60 g đường cam ≈ 88%, tại 120 g đường lam ≈ 82% → người đọc dò sẽ thấy mâu thuẫn. (Giá trị RAL = 60 g / 120 g thì đúng theo quy tắc nấc ≥ 80%.) |
| A5 | Hình 16 | Điểm tuần 3 bị khoanh đỏ "SỐ LIỆU NGHI VẤN (loại khỏi xu hướng)" nhưng **đường trend và dải tin cậy vẫn đi qua nó**, và bản thân điểm đó không hề lệch khỏi xu hướng → minh hoạ tự mâu thuẫn. Đơn vị trục y "độ" cũng lệch với Hình 3 ("tín hiệu cảm biến quy đổi"). |
| A6 | Hình 9(b) | Hai chú thích "mép trái: giới hạn ổn định…" và "mép phải: giới hạn nhạy…" **chồng lên nhau thành một đám chữ không đọc được**, và vị trí neo nhìn bị tráo (chữ "mép phải" lại nằm bên trái). |
| A7 | Hình 10 | Vòng tự kiểm tra nét đứt **bị dangling**: một đoạn nét đứt cộc nằm dưới hộp ESP32-S3 không nối vào đâu; chú thích "đối chiếu ô tham chiếu" không trỏ vào phần tử ô tham chiếu nào. |
| A8 | Hình 14, 15 | Lưu đồ **không khép vòng**: nhánh "BÁO: CẦN KIỂM TRA / nhắc đeo lại găng" và "BÁO: SỐ LIỆU NGHI VẤN / đo lại" là ngõ cụt (không có mũi tên quay lại đo lại); ghi chú đỏ Hình 14 "nếu chưa ổn, hiệu chỉnh rồi đo lại" cũng không có cạnh hồi tiếp. |
| A9 | Hình 12 | Cạnh hồi tiếp nét đứt kết thúc ở hộp **Servo** nhưng nhãn lại mô tả vòng của con người ("người tập nhìn → tăng nỗ lực") → khép vòng sai ngữ nghĩa (assist-as-needed phải đóng vòng từ tín hiệu nỗ lực, còn vòng thị giác là về phía người tập). |

## B. Lỗi va chạm nhãn / bố cục (đặc sản TikZ đặt toạ độ tay)

| # | Hình | Lỗi |
|---|------|-----|
| B1 | Hình 3 | Chú thích "GAP tại đỉnh" **cắt đứt trục trên** (spine) của khung; hộp legend chạm đường AROM quanh x ≈ 0,45–0,55. |
| B2 | Hình 5 | Nhãn nghiêng "Tầng 3: adapter 5 V riêng" **đè lên cạnh trái và nội dung** hộp Tầng 3; bên phải, nhãn xám "hướng dẫn + theo dõi" **chồng lên** nhãn nghiêng "phản hồi thời gian thực". |
| B3 | Hình 6 | Chữ "F" **bị mũi tên hai đầu ngang xuyên qua**; các leader line bên trái/trái phải chen sát nhau. |
| B4 | Hình 7 | Cụm chữ "INA128 / INA333" đè lên đỉnh ra của tam giác op-amp và cạnh hộp ADC; hộp ADC **trùm lên đầu tam giác**; nhãn "cặp R_ref matched…" đè lên dây nhánh phải. |
| B5 | Hình 10 | Hai nhãn nghiêng "tự cân chỉnh điểm 0 (auto-zero)" và "đối chiếu ô tham chiếu" **in đè lên ba hộp hàng dưới** (EI·GAP·RAL, Orange Pi, ESP32-S3). |
| B6 | Hình 12 | Nhãn "kéo gân kéo dần" có nền trắng **cắt mép hộp Servo và hộp Mô hình tay giả**. |
| B7 | Hình 2 | Nhãn mũi tên thứ ba "chỉ một thời điểm" trôi sang trái mũi tên của nó (minor). |

## C. Lỗi chính tả / chuỗi ký tự trong hình

| # | Hình | Lỗi |
|---|------|-----|
| C1 | Hình 6 | "mặt ép (khe **hởdanh** định)" thiếu khoảng trắng; "điện cực lá **đồng(hai** dải trên/dưới)" thiếu khoảng trắng trước ngoặc. |
| C2 | Hình 7 | "cặp R_ref **matchedsai** số 0,1%" thiếu khoảng trắng. |
| C3 | Hình 1(b) | Cụm "50% (còn di chứng)" không khớp chữ dùng trong báo cáo (80% giai đoạn sớm). |
| C4 | Hình 12 | Cụm "kéo gân kéo dần" tối nghĩa (có lẽ muốn nói "dây gân kéo dần"?). |

## D. Định dạng / nhất quán liên-hình

- Xuất PNG raster (RGBA, ~150–200 dpi hiệu dụng); Hình 14 (484×843) và Hình 15 (725×1026) khổ dọc hẹp → cắm theo chiều ngang trang chữ sẽ bé, chữ ~8 px không đọc được khi in.
- Ngữ nghĩa màu đụng nhau: Hình 3 lam/cam = PROM/AROM, còn Hình 4 & 8 lam/cam = vách lòng/vách mu → dễ đọc nhầm khi lật qua lại.
- Hình 14: ba chú thích lề (stage 1/4/6) không có leader line, chỉ "để gần" hộp.
- Hình 11: nhãn "kéo dãn 2 tốc độ" treo ở mũi tên từ hộp "Trục trượt + ổ bi", trong khi hai tốc độ sinh ra từ khối "vít me 2 tốc độ" (minor ngữ nghĩa).
- Hình 8: khối ghi chú "đọc vi sai: d = S_lòng − S_mu" đặt sát/khẽ chạm cạnh dưới hộp legend (minor).

## E. Đề xuất làm lại "ổn hơn"

1. **Giữ TikZ nhưng đổi pipeline xuất bản**: biên dịch standalone (LuaLaTeX để gõ tiếng Việt thật) → PDF vector → nhúng Word dạng EMF/SVG hoặc PNG 600 dpi; chốt cỡ chữ ≥ 8 pt tại kích thước cuối (15–16 cm).
2. **Vẽ plot từ một nguồn số liệu duy nhất** (CSV → `pgfplots table`): dùng `nodes near coords` để nhãn cột tự sinh từ độ cao cột (diệt lỗi tráo nhãn kiểu Hình 1b); dùng thư viện `intersections` để đặt marker đúng giao điểm đường–ngưỡng (Hình 13); marker "loại trừ" thì phải cắt thật khỏi chuỗi vẽ (Hình 16).
3. **Hình 7 vẽ lại bằng `circuitikz`**: anchor linh kiện tự khớp, không còn tap giữa thân điện trở; thêm node junction rõ ràng cho V₁, V₂.
4. **Sơ đồ khối / lưu đồ (5, 10, 12, 14, 15)**: dùng thư viện `graphs`/`chains`/`positioning` với anchor đặt tên, nhãn cạnh dùng `auto/swap`; tuyệt đối không toạ độ tuyệt đối; thêm cạnh hồi tiếp khép vòng (đo lại / hiệu chỉnh rồi đo lại).
5. **pgfplots chỉnh kỷ luật khung**: `ylabel near ticks`, `legend style={at={(...)}}` đặt legend vùng trống; chú thích dùng `pin`/`label` kèm `fill=white, inner sep=1pt` để không cắt spine (Hình 3, 9); `ymin/ymax` đối xứng quanh 0 cho Hình 4.
6. **Vòng QA trước khi nộp**: render từng hình → phóng 200% soát chồng chữ; checklist liên-hình: quy ước dấu d = S_lòng − S_mu (Hình 4, 7, 8, 10), màu vách lòng/mu, đơn vị GAP, cặp nhãn–chiều dài cột.
7. Trong Word: caption dùng field SEQ để tự đánh số "Hình X"; ảnh chèn chiều rộng cố định để không vỡ bố cục.
