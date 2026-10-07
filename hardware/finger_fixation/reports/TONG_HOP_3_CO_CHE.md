# TỔNG HỢP 3 CƠ CHẾ CỐ ĐỊNH KHUNG CỨNG LÊN ĐỐT GẦN NGÓN TAY (P1, Ø20–24 mm)

> **Vị trí:** `hardware/finger_fixation/reports/TONG_HOP_3_CO_CHE.md`
> **Ràng buộc chốt:** ΔX ≤ 2,0 mm/đốt · tải trục 15–25 N · đeo/tháo một tay < 3 s ·
> FDM nozzle 0,4 mm, không CNC · **chỉ PLA hoặc ABS, không thêm chi tiết phụ** (2026-10-07).
> **Trạng thái:** cả 3 bộ sinh STL chạy **44/44 mục PASS ở cả ABS và PLA**;
> **10 lưới STL** kín/định hướng/1 mảnh; **chưa in, chưa đo** — mọi số là ngân sách thiết kế.

---

## 1. BA CƠ CHẾ — BA HỌ NGUYÊN LÝ KHÁC NHAU

| | **Ý tưởng 1** | **Ý tưởng 2** | **Ý tưởng 3** |
|---|---|---|---|
| **Tên** | Vòng khoá quá tâm "móc có mặt dốc" (Side Toggle Clasp) | Vòng khoá cóc một chiều (Ratchet Cinch) | Đai quấn siết cơ học + chêm tự hãm |
| **Họ nguyên lý** | **Đòn bẩy + quá tâm + nêm tự hãm** | **Bánh cóc một chiều + lá lò xo** | **Màng căng (ΣN = 2πT) + nêm 10° tự hãm** |
| **Lực giữ khe** | Mặt chặn cứng chịu tải ép thêm (tự gia cường) | Mặt răng ĐỨNG (form closure) | Lực căng đai + gờ móc cắm rãnh |
| **Đàn hồi dùng ở đâu** | Lá mỏng tại chốt mềm A: 0,40 mm (ABS) / 0,50 (PLA), chỉ 0,15/0,12 mm hành trình | Lá con cóc 8,8 × 0,40, công xôn 8,02 mm | Không dùng — đai chỉ chịu căng dọc |
| **Số chi tiết in** | **1** | **1** | **3** (khung + đai + chêm, cùng vật liệu) |
| **Độ phân giải điều chỉnh** | Liên tục nhờ mặt dốc 2,34 mm | 0,255 mm/ nấc (9 rãnh ⇒ ΔØ 2,04 mm/cỡ in) | Liên tục nhờ chêm trượt |
| **Điểm mạnh riêng** | Chỉ 1 chi tiết; nhả bằng 1 ngón cái (4,64 N, 34°) | Cảm nhận "tách" rõ; không thể siết quá cỡ | Áp lực phân bố **liên tục 355°**, A_tiếp xúc **649 mm² (2,01×)** |
| **Điểm yếu riêng** | Cần chốt Ø3 + mặt dốc chính xác; 4 điểm tì rời | Cần 2 cỡ in cho Ø20–24; răng nhỏ cần gap-fill OFF | 3 chi tiết; phụ thuộc μ(nhựa–nhựa) của chêm |

Cả ba **cùng dùng chung** thân/tay kẹp/lá bản lề sống (`ring_common.py`) và **cùng một
giải pháp mô mềm**: **4 đệm cánh in liền** (0,20 mm đàn hồi → tì chặn cứng, tường 0,60 mm)
tại φ = 33° / 147° / 216° / 288° — **dorsolateral**, tránh đường giữa-bên và vùng A1.

---

## 2. SỐ CHỐT (ngân sách thiết kế) — ABS / PLA

| Đại lượng | Ý tưởng 1 | Ý tưởng 2 | Ý tưởng 3 |
|---|---|---|---|
| Số mục kiểm PASS | **18/18** | **13/13** | **13/13** |
| ΔX sườn (ngân sách 2,0) | −0,16 mm | +0,43 mm | +1,15 mm |
| Z dài trục (12–16 mm) | 14,03 mm | 14,00 mm | 13,00 mm |
| Khối lượng ngân sách | 2,53 g / 3,04 g | 2,10 g / 2,52 g | 1,12 g / 1,35 g (3 chi tiết) |
| Ứng suất chính (FS so với σ_cho phép) | lá 9,7 (1,2) / 17,0 MPa (1,3); đệm 10,0 (1,2) / 14,7 (1,5) | 11,2 (2,68) / 19,6 MPa (2,81) | σ_đai 1,25 MPa; τ_gờ 2,08 ≤ 4,0; σ_bearing 0,19 MPa |
| Thao tác nhả | cần gạt 34°, ngón cái 2,46 mm, 4,64 N | mấu nhả 0,73 / 1,28 N | miết ngược chêm (1 động tác) |
| Lực giữ trục (μ 0,45, 20 kPa) | 2,91 N | 2,91 N | 5,8 N (hoặc 25,4 N ở 87,2 kPa) |
| STL | `stl/idea1/Ring_ABS.stl`, `stl/idea1_pla/Ring_PLA.stl` | `stl/idea2/Ring_ABS.stl`, `stl/idea2_pla/Ring_PLA.stl` | `stl/idea3/{Ring,Band,Wedge}_ABS.stl`, `stl/idea3_pla/{...}_PLA.stl` |

---

## 3. HAI KẾT QUẢ ÂM CẦN NÓI RÕ VỚI HỘI ĐỒNG (theo AGENTS.md)

1. **Một vòng P1 đơn độc không đủ 15–25 N ở ngân sách áp lực 20 kPa.** Cả ba ý tưởng đều
   cho thấy điều này (2,9–5,8 N/vòng P1). **Hướng xử lý thiết kế hệ thống:** chia tải qua
   **P1 + P2**, hoặc mở rộng diện tích tì (đai rộng hơn / thêm đệm), hoặc hạ mức tải an
   toàn cho P1 và đo lại **hệ số ma sát nhựa–da thực** (0,45 là ngân sách, có thể lên 0,60
   với bề mặt in có vân ⇒ tăng lực giữ mà **không** tăng áp lực).
2. **Chêm tự hãm 10° phụ thuộc μ(nhựa–nhựa) = 0,30 — CHƯA ĐO.** Điều kiện tự hãm cần
   μ ≥ 0,18; nếu μ thực thấp hơn (bụi in, ẩm, PLA bóng), khoá một chiều có thể trượt.
   **Phải đo trên băng thử trước khi tin.**

Ba hạng mục kỹ thuật khác: (a) **in thử** để xác nhận khe 0,03–0,45 mm với **gap-fill TẮT**;
(b) **từ biến PLA** — đo lại lực tì sau 24 h; (c) **Ý tưởng 2 cần 2 cỡ in** cho Ø20–24 mm.

---

## 4. KHUYẾN NGHỊ THỨ TỰ TRIỂN KHAI (trung thực, không hứa hẹn)

1. **In Ý tưởng 1 trước** — đúng yêu cầu ưu tiên "chính xác, không lỗi, không lỏng lẻo",
   chỉ **1 chi tiết**, hình học khoá **suy ra từ `synthesis/toggle_synthesis.py`** (không
   chép tay số), và đã có bằng chứng mặt cắt OCCT:
   `reports/figures/idea1_petal_pads_section.png`.
2. **In Ý tưởng 2** để so sánh trực tiếp cảm giác bấm/nhả và độ bền nấc (1 chi tiết).
3. **Ý tưởng 3 để sau cùng** — mạnh nhất về áp lực nhưng **3 chi tiết** và phụ thuộc μ
   chưa đo; chỉ nên đẩy lên khi đã có số đo μ và quyết định chia tải P1+P2.

---

## 5. BẢN ĐỒ TỆP

```
hardware/finger_fixation/
├── params.py                       # §6 Mat/MATS: PLA & ABS; FF_MAT=ABS|PLA; μ_self 0.30
├── ring_common.py                  # thân/tay kẹp/lá bản lề + petal pads in liền + finish() xuất STL
├── build_idea1_toggle_clasp.py     # Ý 1 — 18 mục kiểm
├── build_idea2_ratchet_cinch.py    # Ý 2 — 13 mục kiểm
├── build_idea3_wrap_band.py        # Ý 3 — 13 mục kiểm
├── synthesis/toggle_synthesis.py   # suy ra hình học khoá Ý 1 (nguồn duy nhất)
├── headless/                       # run_verify.py · mesh_qa.py · freecad_api_audit.py · freecad_compat.py
├── reports/
│   ├── IDEA1_SIDE_TOGGLE_CLASP.md  # báo cáo chi tiết Ý 1 (+ cập nhật vật liệu đơn)
│   ├── IDEA2_RATCHET_CINCH.md      # báo cáo chi tiết Ý 2
│   ├── IDEA3_WRAP_BAND.md          # báo cáo chi tiết Ý 3
│   ├── MATERIAL_SINGLE_PLA_ABS.md  # ràng buộc vật liệu, bảng tính chất, quy tắc, kết quả âm
│   ├── TONG_HOP_3_CO_CHE.md        # tài liệu này
│   ├── idea{1,2,3}_verify_{abs,pla}.txt  # log PASS/FAIL theo vật liệu
│   ├── mesh_qa_log.txt · freecad_api_audit.txt · api_audit_log.txt
│   └── figures/idea1_petal_pads_section.png  # mặt cắt OCCT: tường liền z=1 vs 4 cửa sổ đệm z=7
└── stl/idea1|idea2|idea3 (ABS) · stl/idea1_pla|... (PLA)
```

---

## 6. CÁCH TÁI LẬP TOÀN BỘ KẾT QUẢ

```bash
cd hardware/finger_fixation
python headless/run_verify.py                # ABS → 44/44 PASS, xuất STL vào stl/idea*
FF_MAT=PLA python headless/run_verify.py     # PLA → 44/44 PASS, xuất STL vào stl/idea*_pla
python headless/mesh_qa.py $(ls stl/*/*.stl) # QA 10 lưới
python headless/freecad_api_audit.py --write # audit API FreeCAD 0.21.2
freecadcmd build_idea1_toggle_clasp.py       # trên FreeCAD thật (máy có cài)
```

**Ghi chú trung thực (AGENTS.md):** chưa chế tạo, chưa đo, chưa thử trên người; các ngưỡng
sinh lý (3,96 mm; 8/20 kPa) là **trích dẫn y văn dùng làm ngân sách thiết kế**; mọi mục
"PASS" là **kiểm hình học/ứng suất tự động trên mô hình**, không phải kết quả thực nghiệm.
