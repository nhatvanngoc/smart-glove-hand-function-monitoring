# Re-check bản (7) — so với danh sách lỗi bản (6)

16/16 ảnh đều được render lại (kích thước lớn hơn), caption của Hình 3, 14, 15, 16 đã sửa theo.
Trạng thái từng lỗi cũ và các lỗi mới phát hiện khi soi bản (7):

## ĐÃ SỬA OK

| Hình | Lỗi cũ | Tình trạng bản (7) |
|------|--------|--------------------|
| 1(b) | Tráo nhãn 50%/80% | OK: cột 80→"80%", cột 50→"50% (phục hồi có ích)", cột 50→"50% (còn di chứng)" |
| 2 | Nhãn mũi tên 3 lệch | OK: "chỉ một thời điểm" nằm đúng cạnh mũi tên của nó |
| 3 | "GAP tại đỉnh" cắt trục trên; legend đè curve | OK: chú thích trong hộp trắng giữa trục; legend dời xuống vùng trống; y-label đổi "Góc gập quy đổi từ tín hiệu (độ)" khớp Hình 16; caption ghi chú quy ước màu |
| 4 | Lobe âm bị cắt; caption "d=0 chính giữa" sai | OK: ylim đối xứng, d=0 giữa khung, (b) thấy trọn lobe âm |
| 5 | Nhãn adapter đè hộp; 2 nhãn phải chồng nhau | OK: ghi chú nguồn đưa vào trong hộp Tầng 3; hai nhãn phải tách riêng |
| 6 | "hởdanh định", "đồng(hai dải"; F bị xuyên | OK: hết lỗi khoảng trắng; F sạch; thêm nhãn "nắp kẹp + vít kéo trước" |
| 7 | Tap giữa thân điện trở; dây + cắt qua R_dorsal; INA/ADC đè nhau | OK về mạch: V₁→+, V₂→− đi dây vòng đúng; INA ghi dưới, hộp ADC tách rời |
| 9(b) | 2 nhãn mép chồng thành đám | OK: tách trái/phải đúng neo (mép trái→dot trái, mép phải→dot phải) |
| 11 | Nhãn "kéo dãn 2 tốc độ" sai khối | OK: mũi tên xuống xuất phát từ khối vít me |
| 13 | Marker nằm trên đường 80% thay vì trên curve | OK: vòng mở nằm đúng điểm (60, ~89) và (120, ~98); caption chốt định nghĩa RAL |
| 14 | Không có hồi tiếp | OK: mũi tên đỏ GĐ4→GĐ1 + nhãn đỏ; chú thích lề có leader line |
| 15 | Nhánh lỗi ngõ cụt | OK: 2 vòng nét đứt khép về "Bắt đầu ghi phiên đo" và "Tính các chỉ số" |
| 16 | Điểm nghi vấn vẫn nằm trên trend | OK: tuần 3 bỏ khỏi đường, vẽ × đỏ rời; caption mô tả đúng |

## CÒN LỖI / LỖI MỚI

1. **Hình 10 (lỗi cũ CHƯA sửa, nặng nhất còn lại):** nhãn nghiêng "tự cân chỉnh điểm 0 · đối chiếu ô tham chiếu (từ ESP32 quay về đầu chuỗi)" vẫn **in đè lên hàng hộp dưới** (đè dòng "+ mức tin cậy" của hộp EI, "học máy INT8 – NPU" của hộp Orange Pi, "trung bình mẫu · BLE" của hộp ESP32); đoạn nét đứt ngang của vòng tự kiểm tra chạy **lẩn sau các hộp** (chỉ lộ ở khe hở) và còn một mẩu nét đứt cộc trong/duới hộp ESP32 → vòng đọc như đứt đoạn.
2. **Hình 12 (mới):** gán nhãn sai cạnh: "số đo nỗ lực và biên độ" treo trên mũi tên dọc *trợ giúp thụ động → mô hình tay giả* (đúng ra thuộc cạnh *phantom → phản hồi thị giác*, hiện đang để trống); "giảm tải từng nấc" lơ lửng sát mép dưới hộp phantom (đúng ra thuộc mũi tên dọc phía trên); mũi tên dọc đâm xuyên chữ "số đo nỗ lực và biên độ"; hai nhãn "kéo dây gân khi thiếu lực" và "tín hiệu nỗ lực (chưa đạt mục tiêu)" **chồng lên nhau** trên cùng cung nét đứt.
3. **Hình 16 (mới):** chú thích đỏ "BÁO: SỐ LIỆU NGHI VẤN / tuần 3 loại khỏi xu hướng" **đè lên mục legend "khoảng tin cậy"** (chữ đỏ và chữ đen xen nhau không đọc được).
4. **Hình 8 (mới):** khung legend/ghi chú quá nhỏ nên chữ **tràn ra ngoài khung**: "chấm cam = vách mặt lưng (mu)" và "là 2 khớp × 2 vách = 4 kênh" vượt cạnh phải; "đọc vi sai:" nằm cưỡi lên cạnh dưới, công thức d = … rơi ra ngoài hộp; leader chấm mờ hàng PIP cọ vào tiêu đề "ngón cái".
5. **Hình 13 (mới, nhẹ):** nhãn "RAL = 120 g" bị **spine trên của khung đâm xuyên chữ**; mũi tên trỏ từ nhãn này cắt đường cam (và sém ô vuông cam tại 100 g); đoạn cuối đường lam 79→98 dốc bất thường và cụm marker cam–lam tại 120 g gần chồng nhau.
6. **Hình 7 (mới, nhẹ):** nhãn node "V₁ (lòng)" và "V₂ (mu)" nằm **trên chính sợi dây** (chữ bị gạch ngang); leader của "cặp R_ref matched, sai số 0,1%" đâm xuyên ký hiệu ground giữa rồi mới chạm ray dưới (và nên trỏ vào hai điện trở R_ref thay vì ray).
7. **Hình 6 (mới, nhẹ):** nhãn "vùng nén A_c" **trùm lên mép phải stack**; leader của "mặt ép của ngón" và "nắp kẹp + vít kéo trước" kết thúc ở khoảng trống phía trên stack (neo sai); dải highlight vùng nén (màu cam nhạt) nằm trên hàng nắp kẹp thay vì hàng màng Velostat như caption mô tả.
8. **Hình 9(b) (sót):** khối nhãn "mép phải…" tràn qua spine phải ra lề; nhãn xanh "khoảng tiền tải khả dụng" cọ đường cam; đường cam còn gãy khúc ở ~33 N.
9. **Hình 4 (sót, rất nhẹ):** nhãn "d = 0" ngồi lên đường nét đứt ở cả ba khung (hơi gạch chữ).

## Gợi ý sửa nhanh đợt này (giữ TikZ)

- Hình 10: dắt vòng nét đứt theo một "lane" trống dưới hàng hộp dưới (y cố định ngoài bounding box), nhãn đặt giữa lane, `anchor=north`; không route xuyên vùng có hộp.
- Hình 12: dùng `edge node={node[auto]{...}}` để nhãn tự bám đúng cạnh; xoay nhãn mũi tên dọc 90° (`sloped`) để không bị đâm xuyên.
- Hình 16: dời chú thích đỏ xuống dưới legend hoặc đặt `legend style={at={(0.5,0.98)}, anchor=north}` còn chú thích ở `(0.35,0.85)`; kiểm tra bằng mắt vùng giao nhau.
- Hình 8: bỏ khung cố định, để legend tự sized (`node[draw, inner sep=6pt]` bọc quanh nội dung) hoặc đưa khối ghi chú ra ngoài làm caption phụ.
- Hình 13: đặt nhãn RAL bằng `pin` hướng vào trong khung (`pin above` bên dưới spine) thay vì node tuyệt đối trên spine.
- Hình 7: `label={left:$V_1$}` gắn vào node junction thay vì node trôi; leader "cặp R_ref" dùng `pin={[pin edge={gray}]270:...}` từ giữa hai R_ref.
- Hình 6: neo leader vào coordinate đặt tên (`\coordinate (matEp) at ...`) và vẽ dải vùng nén trên hàng màng.
- Hình 9(b): cho nhãn mép phải `anchor=north east` trong khung; làm mượt đường cam (thêm mẫu hoặc hàm mượt).
