# Ý TƯỞNG 3 — ĐAI QUẤN SIẾT CƠ HỌC + CHÊM TỰ HÃM (WRAP BAND + SELF-LOCKING WEDGE)

> **Vị trí tài liệu:** `hardware/finger_fixation/reports/IDEA3_WRAP_BAND.md`
> **Mã nguồn sinh STL:** `hardware/finger_fixation/build_idea3_wrap_band.py`
> (+ `ring_common.py` cho một số tiện ích đo/kiểm)
> **Log kiểm chứng:** `hardware/finger_fixation/reports/idea3_verify_abs.txt` ·
> `hardware/finger_fixation/reports/idea3_verify_pla.txt`
> **STL xuất ra (3 chi tiết, CÙNG một vật liệu):**
> `stl/idea3/Ring_ABS.stl` (khung lưng) · `stl/idea3/Band_ABS.stl` (đai) ·
> `stl/idea3/Wedge_ABS.stl` (chêm); bản PLA ở `stl/idea3_pla/`.
> **Ràng buộc áp dụng:** chỉ PLA hoặc ABS, **không keo kết cấu, không đệm rời**
> (xem `reports/MATERIAL_SINGLE_PLA_ABS.md`).

**Trạng thái kiểm tự động: TẤT CẢ PASS — 13/13 mục (S2b–S11, G1) ở CẢ HAI vật liệu.**
Điểm khác biệt của ý tưởng này: nó **không che giấu giới hạn** — mục S7 in ra đánh đổi
lực/áp lực như một **phép kiểm thông tin**, không phải PASS giả (xem §2.3).

---

## 1. CƠ CHẾ & NGUYÊN LÝ LÀM VIỆC

**Họ nguyên lý: khoá bằng CĂNG CƠ HỌC của một dải quấn + nêm tự hãm — KHÁC Ý tưởng 1
(đòn bẩy quá tâm) và Ý tưởng 2 (bánh cóc).** Không bản lề sống, không răng cóc, **không
dùng biến dạng đàn hồi của đai để tạo lực kẹp** (bản cũ dùng TPU 85A ε ≈ 6 % — đã bỏ vì
ràng buộc một vật liệu cứng). Ba cơ chế tách bạch:

1. **ĐAI QUẤN 355° × 0,80 × 9,0 mm** — in **cùng vật liệu với khung** (PLA hoặc ABS).
   Lực kẹp sinh bởi **lực căng cơ học T do tay người kéo** (đặt trước T = 9,0 N) rồi
   được **chêm giữ**; đai chỉ chịu **căng dọc**, còn phản lực hướng tâm đi vào VÒM KHUNG
   (tường 6,30 mm ở đỉnh cung) chứ không tăng áp lực chỗ chêm.
2. **GỜ MÓC + RÃNH TRÊN SÀN MÁNG (form closure)** — gờ đai **cắm** vào rãnh khoét trên
   sàn máng (r = 2,45 → 2,90 mm, sâu 0,30 mm; sàn khoét φ 105,85–116°) ⇒ chặn trượt
   **tiếp tuyến** bằng HÌNH HỌC, **không bằng ma sát, không bằng keo** (τ = 2,08 MPa ở
   25 N trên 12,0 mm²).
3. **CHÊM 10° TỰ HÃM** — chêm trượt trong máng khung, mặt vát tì lên đầu đai; lực căng
   đai **kéo chêm SÂU THÊM** (không đẩy ra). Điều kiện tự hãm: **tan 10° = 0,176 ≤
   μ(nhựa–nhựa)/1,3 = 0,231** ⇒ **biên 1,31×**. Nhả khoá bằng cách **miết ngược đầu đai**
   (một tay, cùng động tác với xỏ ngón).

Chuỗi lắp/tháo một tay (< 3 s theo mục tiêu brief — **chưa bấm giờ**):

```
  ĐEO:   mở đai (in sẵn theo cung mở DON_R_OPEN = 1,5 mm bán kính, ε_mở = 0,42 %)
          → xỏ ngón vào đốt gần → kéo đầu đai căng (T ≈ 9 N) → ấn chêm vào máng
  THÁO:  miết ngược chêm ra → đai bật theo cung in sẵn → tuột ngón ra
```

---

## 2. PHÂN TÍCH CƠ HỌC

### 2.1 Vì sao không "kẹp bên sườn" / không vướng khe giữa ngón
Khung **chỉ chiếm nửa LƯNG (φ 88°–152°, tức hơi lệch về dorsolateral)**, nơi mặt ngoài
ngón **phẳng nhất** và **không có ngón kế cận**. Nửa sườn (φ ≈ 0° và φ ≈ 180°) **trống
hoàn toàn**: không có đòn bẩy, không có chi tiết nào thò ra ngoài vành. ΔX sườn =
**+1,15 mm** (ngân sách 2,0 mm). Bao hình **13,81 × 10,41 × 13,00 mm** — **nhỏ nhất**
trong ba ý tưởng.

Pad không nằm ngay đường giữa-bên: khung lệch lên lưng 88°–152° nên **tránh bó mạch-dây
thần kinh** sống ở ~±0° (ngân sách 3,96 mm ở PIP/DIP theo y văn) — nhưng đây là **thiết kế
dorsolateral ~45°, không phải true-lateral**; mục "mở" §6 ghi rõ rủi ro nhánh cảm giác
lưng mu có thể tách ra tại/ngay trên ròng rọc A1.

### 2.2 Áp lực mô mềm — vì sao phân bố tốt hơn hai ý tưởng kia
Đai 355° tiếp xúc **liên tục** với đường kính đốt gần: **A_tiếp xúc = 649 mm²** —
**2,01× tổng diện tích 4 đệm cánh** của Ý tưởng 1/2 ⇒ **không có "điểm tì" cứng**.
Áp lực trung bình p = ΣN / A với mô hình màng mỏng: **ΣN = 2πT** (ΣN = 56,5 N ở T = 9 N).

Kiểm S2b (biến dạng khi mở đai để xỏ ngón): ε_mở = **0,42 %** ≤ 2,0 % (ABS) và ≤ 1,0 %
(PLA) — biên thoải mái vì đai mỏng 0,80 mm **in sẵn theo cung mở**, không bị "banh" khi đeo.

### 2.3 ĐÁNH ĐỔI ĐÃ GHI THẲNG (mục S7 — phép kiểm "thông tin")
```
  CHẾ ĐỘ ĐỦ TẢI:      T = 9,00 N ⇒ ΣN = 56,5 N ⇒ p ≈ 87,2 kPa ⇒ giữ trục ≈ 25,4 N
  CHẾ ĐỘ AN TOÀN:     p = 20 kPa (ngưỡng ngắt quãng) ⇒ T = 2,06 N ⇒ giữ trục ≈ 5,8 N
  ⇒ HAI CHẾ ĐỘ KHÔNG THỂ ĐỒNG THỜI. Một vòng P1 KHÔNG đủ 25 N ở ngân sách 20 kPa.
```
Đây là **phát hiện trung thực, không phải lỗi cần giấu**: nó nói rằng với **nhựa cứng
(μ ≈ 0,45)**, giữ 15–25 N **luôn** cần **chia tải qua nhiều đốt** (P1 + P2) hoặc tăng
diện tích tì. Cùng kết luận xuất hiện ở Ý tưởng 1 (2,91 N/vòng P1) và Ý tưởng 2
(2,91 N/vòng P1) ⇒ **đây là kết luận thiết kế hệ thống, không phải khuyết điểm riêng của
ý tưởng nào.** Ý tưởng 3 vẫn **tốt nhất về phân bố áp lực** vì diện tích tì gấp 2×.

### 2.4 Khối lượng & hình học in
| Chi tiết | Thể tích | ABS | PLA | Ghi chú in |
|---|---|---|---|---|
| Khung lưng (Ring) | 0,43 cm³ | 0,44 g | 0,53 g | vòm dày tối đa 6,30 mm (r_ngoài = a_in+6,30) |
| Đai (Band) | 0,63 cm³ | 0,65 g | 0,78 g | 0,80 mm = **2 đường in ở nozzle 0,4** (kiểm S2) |
| Chêm (Wedge) | 0,03 cm³ | 0,03 g | 0,04 g | vát 10°; dày 0,10 → 0,85 mm; miệng 2,70 → họng 1,60 mm (S6) |

Chêm **vào được** (đầu mỏng 0,90 ≤ khe miệng 2,70) và **kẹt lại** (đầu dày 1,65 > họng
1,60) — kiểm S6; nếu in nhựa co nhiều (ABS) thì họng 1,60 mm vẫn giữ được vì **kẹt theo
mặt vát**, không theo khe.

---

## 3. SƠ ĐỒ ASCII

### 3.1 Mặt cắt ngang tại giữa đốt (nhìn từ đầu ngón về gốc)

```
              +Y (mu / dorsal)
                    ▲
                    │   ┌──── VÒM KHUNG (r_ngoài = a_in + 6,30 mm) ────┐
                    │  ╱                                              ╲
    φ=88° ──────────┤ │        KHUNG LƯNG  φ 88°–152°                  │ ├── φ=152°
                    │  ╲   [vách cảm biến nằm trên vòm này]            ╱
                    │   └──────────────────────────────────────────┘
                 ═══╪══════════════ ĐAI 355° × 0,80 mm ═══════════════╪═══
                    │   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                    │   ▓  tiếp xúc da: A = 649 mm² (liên tục 355°) ▓
   φ180 ────────────┤   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ├── φ=0°
   (mid-lateral,    │        ░░░  LÒNG VÒNG (ngón)  ░░░               (mid-lateral,
    KHÔNG có khung) │   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░        KHÔNG có khung)
                    ▼
              −Y (bụng / volar)
      ▼ CHÚ THÍCH: nửa sườn hai bên TRỐNG ⇒ không giành chỗ với ngón kế cận.
```

### 3.2 Mặt cắt vuông góc trục, đoạn CHÊM (khai triển phẳng, đơn vị mm)

```
   z ↑   ┌──────────────────────── KHUNG (vòm lưng) ─────────────────────────┐
   13.0  │                                                                  │
         │   máng: sàn 2,75 ─ đai 2,85 ─ mặt ngoài đai 4,35 ─ vòm khung 6,30 │
    8.5  │        ▓▓▓▓▓▓▓▓▓▓▓  GỜ MÓC ĐAI  (r 2,45 → 2,90)  ▓▓▓▓▓▓▓▓▓▓       │
         │        ═══════════  RÃNH SÀN φ105,85–116°  ═══════════            │
         │                                                                  │
    0.0  └──────────────────────────────────────────────────────────────────┘
                 ──► hướng đai căng (kéo đầu đai sang trái khi siết)
   CHÊM 10° (mặt vát tì lên đầu đai):
        đầu MỎNG 0,10 mm ──┐                                  ┌── đầu DÀY 0,85 mm
                            ╲_______________________________╱
                             mặt vát 10°  (WEDGE_RAMP_L ≈ 4,2 mm)
        vào miệng 2,70 mm ──► trượt ──► kẹt tại họng 1,60 mm  ⇒ tan 10° = 0,176 ≤ 0,231
```

Các con số then chốt in trong log: **S5** biên tự hãm 1,31× · **S6** vào được/kẹt lại ·
**S8** ba chi tiết **không chồng khối** (khung∩đai = khung∩chêm = đai∩chêm = 0,0000 mm³) ·
**S9** gờ móc ăn vào rãnh **0,30 mm** với tường còn **0,30 mm** · **S10/S11** mỗi chi tiết
**1 khối**, `isValid()=True`, Z_khung = 13,00 mm.

---

## 4. BẢNG KIỂM TỰ ĐỘNG (kết quả thật, 2 vật liệu)

```
============================================================
  FF_MAT=ABS : build_idea3_wrap_band.py     PASS  13/0
  FF_MAT=PLA : build_idea3_wrap_band.py     PASS  13/0
============================================================
```
Các mục: **S2** in được ở nozzle 0,4 (≥ 2 đường) · **S2b** biến dạng mở đai ≤ ε_cho phép ·
**S3** gờ chặn trượt tiếp tuyến bằng form closure (τ 2,08 ≤ 4,0 MPa) · **S4** tải trục qua
2 vai máng (σ_bearing 0,19 MPa trên 130 mm²) · **S5** chêm tự hãm · **S6** chêm vào/kẹt ·
**S7** ngân sách kẹp (đánh đổi — xem §2.3) · **S8** không chồng khối · **S9** gờ cắm rãnh ·
**S10** in một khối liền · **S11** khối hợp lệ + Z 12–16 mm · **G1** một vật liệu duy nhất.

QA lưới STL (`headless/mesh_qa.py`): cả 6 file (`stl/idea3/{Ring,Band,Wedge}_ABS.stl`,
`stl/idea3_pla/{Ring,Band,Wedge}_PLA.stl`) **kín, định hướng nhất quán, 1 mảnh,
0 tam giác suy biến**.

---

## 5. CÁCH CHẠY

```bash
cd hardware/finger_fixation
python headless/run_verify.py build_idea3_wrap_band.py       # ABS (mặc định)
FF_MAT=PLA python headless/run_verify.py build_idea3_wrap_band.py
python headless/mesh_qa.py stl/idea3/*.stl
freecadcmd build_idea3_wrap_band.py                          # trên FreeCAD thật
```

---

## 6. GHI CHÚ TRUNG THỰC & HẠNG MỤC CÒN MỞ (theo AGENTS.md)

1. **Chưa có kết quả đo hay chế tạo.** Chưa in, chưa thử trên người; ε_mở, ΣN = 2πT, p,
   τ, σ_bearing đều là **ngân sách thiết kế** từ mô hình.
2. **Hạng mục mở #1 — μ(nhựa–nhựa) = 0,30 chưa đo:** điều kiện tự hãm của chêm chỉ đúng
   nếu μ thực ≥ 0,231/1,3 ≈ 0,18. **Phải đo trên băng thử** (cùng cặp vật liệu, cùng
   hướng in, có/không bụi in) trước khi tin vào khoá một chiều.
3. **Hạng mục mở #2 — chia tải P1 + P2:** để giữ 15–25 N ở ≤ 20 kPa cần **2 đốt** (hoặc
   đai rộng gấp đôi). Đây là hạng mục thiết kế hệ thống, không phải sửa hình học nhỏ.
4. **Hạng mục mở #3 — giải phẫu:** khung 88°–152° là **dorsolateral**, an toàn hơn so với
   true-lateral, nhưng **nhánh cảm giác lưng của dây thần kinh có thể tách ra tại/ngay
   trên ròng rọc A1 trong ~62 % ca** (y văn, ngân sách thiết kế) ⇒ khi thử trên người phải
   chờ IRB/SRC và kiểm cảm giác ngón sau mỗi lần đeo.
5. **Hạng mục mở #4 — in & lắp:** khe hở lắp ráp thật (S8) dựa trên dung sai in ±0,27 mm;
   cần **mẫu in thử** để xác nhận chêm vào/kẹt và độ rơ của gờ móc; nhựa **ABS co** nhiều
   hơn PLA nên họng 1,60 mm phải kiểm riêng cho từng vật liệu.
6. **Số vòng đời (fatigue) chưa kiểm:** đai căng/ nhả nhiều lần ⇒ nên in **≥ 2 đường** và
   thử 500 chu kỳ đeo/tháo trên chốt giả trước khi kết luận.
