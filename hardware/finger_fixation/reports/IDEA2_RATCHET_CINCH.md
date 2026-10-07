# Ý TƯỞNG 2 — VÒNG KHOÁ CÓC MỘT CHIỀU (RATCHET CINCH RING)

> **Vị trí tài liệu:** `hardware/finger_fixation/reports/IDEA2_RATCHET_CINCH.md`
> **Mã nguồn sinh STL:** `hardware/finger_fixation/build_idea2_ratchet_cinch.py`
> (+ `ring_common.py` cho thân/tay kẹp/lá bản lề/đệm cánh in liền)
> **Log kiểm chứng:** `hardware/finger_fixation/reports/idea2_verify_abs.txt` ·
> `hardware/finger_fixation/reports/idea2_verify_pla.txt`
> **STL xuất ra:** `stl/idea2/Ring_ABS.stl` (ABS) · `stl/idea2_pla/Ring_PLA.stl` (PLA)
> **Ràng buộc áp dụng:** CHỈ PLA hoặc ABS, **một chi tiết in duy nhất**, không đệm
> rời, không keo kết cấu (yêu cầu chủ dự án 2026-10-07 — xem
> `reports/MATERIAL_SINGLE_PLA_ABS.md`).

**Trạng thái kiểm tự động: TẤT CẢ PASS — 13/13 mục (A3–A11, G1, G2) ở CẢ HAI vật liệu.**
Mọi con số dưới đây là **ngân sách thiết kế** tính từ mô hình hình học/ứng suất, **chưa in,
chưa đo** (AGENTS.md).

---

## 1. CƠ CHẾ & NGUYÊN LÝ LÀM VIỆC

**Họ nguyên lý: khoá MỘT CHIỀU bằng bánh cóc — KHÁC Ý tưởng 1 (đòn bẩy quá tâm) và
Ý tưởng 3 (căng đai bằng chêm).** Không có khớp quá tâm, không dùng lực đàn hồi của đai.

Vòng P1 vẫn gồm **THÂN** (giữ 4 đệm tì + vách cảm biến) và **TAY KẸP**, nối nhau bằng
**lá bản lề sống** (`ring_common.py`) đúng như Ý tưởng 1. Khác biệt nằm ở **cơ cấu khoá khe**:

| Chi tiết | Thuộc | Chức năng |
|---|---|---|
| **LƯỠI RĂNG** (u = −3,00 → +6,85 ≈ 9,9 mm) | TAY KẸP (u<0) | Mang **9 rãnh**, bước **0,80 mm/nấc**, mặt răng **đứng** |
| **CON CÓC** = lá lò xo 8,8 × 0,40 mm + **mũi cóc 2 bậc** + **mấu nhả** | THÂN (u>0) | Leo dốc 45° khi siết — rơi vào rãnh — **chặn ngược bằng mặt đứng** |

Chuỗi vận hành:

1. **Đóng**: bấm tay kẹp chạy theo +u. Mũi cóc **leo dốc 45°** (công vượt nấc
   **0,27 N** ở ABS / 0,48 N ở PLA — ngón tay cảm nhận rõ tiếng "tách"), rơi vào rãnh kế
   tiếp ⇒ **0,255 mm đường kính mỗi nấc**; dải 0,45 → 6,85 mm khe = **ΔØ 2,04 mm cho
   mỗi cỡ in** (cần **2 cỡ in** để phủ đủ Ø20–24 — xem §6).
2. **Giữ**: mặt răng **ĐỨNG** (0,55 mm) tì vào mặt đứng của mũi cóc ⇒ **form closure,
   KHÔNG nhờ ma sát** ⇒ `khe in tại nấc = 0,03 mm`, đúng nghĩa "không lỏng lẻo".
   Mặt răng đứng cao 0,55 mm; **ăn sâu 0,50 mm** (kiểm A7 ≥ 0,35 mm).
3. **Mở**: mũi cóc bị mặt răng giữ cứng; muốn mở phải **đè MẤU NHỜ** (một ngón cái,
   **0,73 N** ở ABS / **1,28 N** ở PLA; biên trên mô hình đòn cứng 1,09 / 1,92 N ≤ 8 N)
   để nhấc mũi cóc 0,65 mm.
4. **Giới hạn siết — không thể siết quá cỡ**: hành trình lớn nhất của tay kẹp là khi
   **khe in 0,45 mm đóng hết**; hai mặt đầu **không thể chồng lên nhau** ⇒ mọi vị trí
   khoá đều nằm trong 9 rãnh (kiểm A8).

**Vì sao ổn định (chống rơ) dù in FDM 0,4 mm:** cơ cấu khoá là **hai mặt phẳng đứng tì
nhau**, không phải tiếp xúc điểm-trên-dốc. Khe hở in 0,03 mm bị **lực đệm cánh ép kín**
khi đeo (đệm cánh in liền: lực tì 1,56 N ở ABS — kiểm G1) ⇒ trong trạng thái làm việc
đường truyền lực là **cứng**, không có khe tự do.

---

## 2. PHÂN TÍCH CƠ HỌC

### 2.1 Vì sao không "kẹp bên sườn" / không vướng khe giữa ngón
Bao hình **25,26 × 29,60 × 14,00 mm**; **ΔX sườn = +0,43 mm** (ngân sách 2,0 mm/đốt).
Toàn bộ cơ cấu khoá (lưỡi răng + con cóc + mấu nhả) nằm **trên cung lưng-bên (φ33°–288°
theo `PAD_PHI`)**, tức nửa dorsal/dorsolateral; **nửa sườn φ≈0° và φ≈180° trống** ⇒
không giành chỗ với ngón kế cận. Con cóc và lưỡi chạy **theo phương tiếp tuyến**, không
thò ra ngoài vành (kiểm A9: đáy lưỡi thấp hơn mặt ngoài vành **0,35 mm**; khe hở in hai
bên khe 0,08 mm).

### 2.2 Vì sao không gây biến dạng mô mềm (kế thừa + cải tiến so với Ý tưởng 1)
- **4 đệm cánh in liền** (0,60 mm ABS / 0,50 mm PLA; cung tự do L = 6,93 mm; k = 7,8 N/mm
  ABS / 8,0 N/mm PLA) tại φ = 33°, 147°, 216°, 288° — **lệch khỏi đường giữa-bên 45°**
  (bó mạch-dây thần kinh sống ở ~±0°), và **có mặt chặn cứng** ngay sau 0,20 mm hành
  trình ⇒ áp lực không bao giờ vượt mức: σ_tì = **10,0 MPa** (ABS, FS 1,20 so với
  σ_cho phép 12) / **14,7 MPa** (PLA, FS 1,49 so với 22).
- Diện tích tì **A_tiếp xúc = 323 mm²** (ABS) ⇒ ở ngân sách áp lực **20 kPa** (ngắt
  quãng) vòng giữ được **2,91 N** lực trục trên **một đốt P1**; ở 8 kPa (liên tục) giữ
  **1,16 N**. **Đây là giới hạn thật của một vòng P1 đơn độc** — không đủ 15–25 N
  (xem §6, hạng mục mở #1).
- **Không nhấp nhả theo răng**: khi đã khoá, mũi cóc nằm trong rãnh với khe 0,03 mm bị
  ép kín; các vị trí trung gian **không tồn tại** (khoá là nhị phân, không phải ma sát
  trượt như đai quấn).

### 2.3 Ứng suất & khả năng đàn hồi của lá cóc
σ ở ngàm lá khi nhả: **9,3 MPa** (ABS, t = 0,40 mm, L = 8,02 mm, δ = 0,60 mm) và
**11,2 MPa** khi mũi leo dốc; σ_y(ABS) = 30 MPa ⇒ **FS ≈ 2,68**. Với PLA (E gấp 1,75×),
cùng hình học cho σ_nhả = 16,3 MPa / σ_nấc = 19,6 MPa, σ_y(PLA) = 55 MPa ⇒ **FS ≈ 2,81** —
vẫn đạt, nhưng PLA **dòn + từ biến** nên với lá lò xo **ABS là lựa chọn ưu tiên**
(xem `MATERIAL_SINGLE_PLA_ABS.md` §4).

---

## 3. SƠ ĐỒ ASCII

### 3.1 Mặt cắt ngang tại giữa đốt (nhìn từ đầu ngón về gốc) — CHUNG khung với Ý tưởng 1

```
              +Y (mu / dorsal)
                    ▲
        ...         │         φ=90°  [VÁCH CẢM BIẾN φ74–106° + RÃNH GÂN]
         ██████████████████████
      φ147 ░░░░░░░░░░░░░░░░░░░░░ φ33        █ = nhựa (thân/tay kẹp) — MỘT vật liệu
        ░░░░░░░░░░░░░░░░░░░░░░░░░                 ░ = đệm cánh in liền (khe 0,20 mm)
     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
   φ180░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░φ0  ◄── ĐƯỜNG GIỮA-BÊN (mid-lateral)
     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░        NV bundle cách ≈ 3,96 mm (ngón)
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░     ╔══ KHE 0,45 mm (φ=61°) — ĐẶT CHẾCH RA SAU
      φ213 ░░░░░░░░░░░░░░░░░░░░░ φ327   ║
         ██████████████████████        ║   ◄── LƯỠI RĂNG 9 nấc chạy DỌC khe
                    │                 ║
                    ▼                 ▼
              −Y (bụng / volar)      [LÁ BẢN LỀ SỐNG φ=336°]
```

### 3.2 Mặt cắt KHAI TRIỂN (trải thẳng) vùng khoá — đúng kích thước thiết kế (mm)

```
   u →  −3.0  −2.4      −0.3  −0.20 0.02                            +6.85
        │      │         │      │    │                               │
   TAY  │██████│  lưỡi răng LƯỢN theo cung  ─────── 9 rãnh, 0,80 mm/nấc ───────►
   KẸP  │ chân │        └─ mặt răng ĐỨNG cao 0,55, ăn sâu 0,50 mm
        │ ngàm │            ┃      ┃      ┃      ┃      ┃      ┃      ┃
   ═════╪══════╪═══════════╪══════╪══════╪══════╪══════╪══════╪══════╪════ khe 0,45
        │      │           │ rãnh 0,25 mm (đáy V=2,05)
   THÂN │      │      ┌────┴── mũi cóc: ngón 0,20 ≤ rãnh 0,25 (A6)
        │      │      │  đáy ngón V=2,10 (cách mặt rãnh 0,05)
        │   TRỤ ĐẾ   ─┴── LÁ LÒ XO 8,8 × 0,40 (ngàm ở trụ đế, L=8,02)
        │   (ngàm lá)      ╲
        │                    ╲__ MẤU NHỜ (đè XUỐNG bằng ngón cái, 0,73 N)  ─►
        └─ V=…      V_ROOF 2,05   V_TIP 2,60 = đỉnh răng
            (v = lệch kính RA NGOÀI so với mặt ngoài vành; v = 0 là mặt vành)
```

Các khoảng then chốt (in trong log kiểm): mũi cóc ↔ rãnh **0,20 ≤ 0,25**; ăn khớp mặt
răng đứng **0,50 ≥ 0,35**; lưỡi bay qua khe với khe hở **0,35 mm**; chân lưỡi **ngàm
1,15 mm** trong tường tay kẹp (hết phần ngàm ở u = −0,30, qua khe −0,23).

### 3.3 Hành trình & khối lượng

| Đại lượng | ABS | PLA |
|---|---|---|
| k công xôn con cóc | 0,55 N/mm | 0,96 N/mm |
| Lực vượt nấc | 0,27 N | 0,48 N |
| Lực nhả (một ngón cái) | 0,73 N (biên 1,09) | 1,28 N (biên 1,92) |
| Z dài trục / ΔX | 14,00 mm / +0,43 mm | 14,00 mm / +0,43 mm |
| Khối lượng (ngân sách in) | 2,02 cm³ ≈ **2,10 g** | 2,03 cm³ ≈ **2,52 g** |

---

## 4. BẢNG KIỂM TỰ ĐỘNG (kết quả thật, 2 vật liệu)

```
============================================================
  FF_MAT=ABS : build_idea2_ratchet_cinch.py   PASS  13/0
  FF_MAT=PLA : build_idea2_ratchet_cinch.py   PASS  13/0
============================================================
```
Các mục: **A3** lực vượt nấc ≤ 2,2 N · **A4** lực nhả ≤ 8 N · **A5** σ ≤ σ_y/2,5 ·
**A6** ngón cóc lọt rãnh · **A7** ăn khớp mặt đứng ≥ 0,35 mm · **A8** giới hạn siết = khe
đóng hết · **A9** lưỡi bay qua khe ≥ 0,30 mm · **A10** chân lưỡi ngàm trong tường ·
**A11** 1 khối liền, `isValid()=True`, Z 12–16 mm, khe thật 0,450 mm · **G1** một vật
liệu duy nhất + không đệm rời/keo · **G2** độ cứng bấm ≤ 2,5 N ở vật liệu đang chọn.

QA lưới STL (`headless/mesh_qa.py`): **kín, định hướng nhất quán, 1 mảnh,
0 tam giác suy biến** cho `stl/idea2/Ring_ABS.stl` và `stl/idea2_pla/Ring_PLA.stl`.

---

## 5. CÁCH CHẠY

```bash
cd hardware/finger_fixation
python headless/run_verify.py build_idea2_ratchet_cinch.py    # ABS (mặc định)
FF_MAT=PLA python headless/run_verify.py build_idea2_ratchet_cinch.py
python headless/mesh_qa.py stl/idea2/Ring_ABS.stl
freecadcmd build_idea2_ratchet_cinch.py                       # trên FreeCAD thật
```

Script dùng **đúng API FreeCAD** (`Part.makePolygon → Part.Face → extrude → cut/fuse →
Mesh.export`); `headless/freecad_compat.py` chỉ là lớp thay thế App/Part/Mesh chạy trên
**cùng nhân OCCT** khi máy chưa cài FreeCAD.

---

## 6. GHI CHÚ TRUNG THỰC & HẠNG MỤC CÒN MỞ (theo AGENTS.md)

1. **Chưa có kết quả đo hay chế tạo.** Chưa in, chưa thử trên người, chưa đo lực; mọi số
   là ngân sách thiết kế từ mô hình.
2. **Hạng mục mở #1 — độ phân giải đường kính:** một cỡ in chỉ phủ **ΔØ 2,04 mm**; phủ
   đủ **Ø20–24 mm** cần **2 cỡ in** (ví dụ 20,0–22,0 và 22,0–24,0) — hoặc tăng số nấc.
3. **Hạng mục mở #2 — lực giữ trục:** một vòng P1 đơn độc chỉ giữ được **2,91 N** ở
   ngân sách 20 kPa (< 15–25 N của brief). Hướng xử lý: **thêm vòng P2/đốt giữa** hoặc
   mở rộng cung tì; xem §2.2.
4. **Hạng mục mở #3 — răng nhỏ ở nozzle 0,4 mm:** rãnh 0,25 mm và khe hở in 0,03 mm cần
   in với **gap-fill TẮT**; phải kiểm bằng mẫu in thử trước khi kết luận (thông số slicer,
   không phải hình học đã chứng minh).
5. **μ(nhựa–nhựa) = 0,30 là NGÂN SÁCH THIẾT KẾ**, chưa đo trên băng thử; chỉ dùng cho
   các chỗ dựa vào ma sát (ở Ý tưởng 2: hầu như không — khoá là form closure).
6. **Từ biến & mỏi:** PLA được ghi nhận dòn + từ biến; nếu in PLA, nên in **≥ 4 đường
   (1,6 mm)** cho mọi tường chịu tải và kiểm mẫu sau 24 h tải tĩnh.
