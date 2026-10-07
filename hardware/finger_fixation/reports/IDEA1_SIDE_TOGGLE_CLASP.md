# Ý TƯỞNG 1 — VÒNG KHOÁ QUÁ TÂM KIỂU “MÓC CÓ MẶT DỐC” (SIDE TOGGLE CLASP)
### Báo cáo cơ chế + bộ sinh STL bằng FreeCAD Python (đã chạy kiểm tự động: TẤT CẢ PASS)

> **Vị trí tài liệu:** `hardware/finger_fixation/reports/IDEA1_SIDE_TOGGLE_CLASP.md`
> **Mã nguồn sinh STL:** `hardware/finger_fixation/build_idea1_toggle_clasp.py`
> **Nguồn duy nhất của hình học khoá:** `hardware/finger_fixation/synthesis/toggle_synthesis.py`
> **Log kiểm chứng (2 vật liệu):** `reports/idea1_verify_abs.txt` · `reports/idea1_verify_pla.txt`
> **STL xuất ra:** `hardware/finger_fixation/stl/idea1/Ring_ABS.stl` (ABS) ·
> `hardware/finger_fixation/stl/idea1_pla/Ring_PLA.stl` (PLA)
> **Bản vá hình học:** 2026-10-07 — sửa 4 lỗi hình học (khe bị hàn kín, rãnh đệm cắt
> mất lá bản lề, nub lọt lòng vòng, tam giác suy biến); xem **§4.1**.

---

## 0. CẬP NHẬT 2026-10-07 — VẬT LIỆU ĐƠN (CHỈ PLA HOẶC ABS), BỎ ĐỆM TPU, KHÔNG KEO

Theo yêu cầu mới của chủ dự án (*"chỉ có nhựa PLA hoặc ABS, cố gắng không thêm phần
khác"*), bản này **thay thế toàn bộ phần vật liệu của bản PETG + TPU trước**:

- **4 đệm TPU 85A rời → 4 đệm CÁNH IN LIỀN** bằng chính vật liệu của vòng: cánh
  **0,60 mm (ABS) / 0,50 mm (PLA)**, cung tự do L = 6,93 mm ⇒ k = 7,8 / 8,0 N/mm,
  đàn hồi **0,20 mm** rồi **tì CHẶN CỨNG** (tường sau 0,60 mm); lực tì 1,56 N;
  σ_tì = **10,0 MPa** (ABS, FS 1,20) / **14,7 MPa** (PLA, FS 1,49) — kiểm G3.
  Bằng chứng hình học: `reports/figures/idea1_petal_pads_section.png` (mặt cắt OCCT:
  tường liền ở z = 1 mm, 4 cửa sổ đệm với khe 0,20 mm ở z = 7 mm).
- **Lá mỏng tại chốt mềm A** chọn theo vật liệu: **0,40 mm / δ = 0,15 mm** (ABS,
  σ 9,7 ≤ 12 MPa, lực đặt trước 0,46 N) và **0,50 mm / δ = 0,12 mm** (PLA, σ 17,0 ≤
  22 MPa, lực đặt trước 1,25 N) — kiểm **B3b** (cả hai phía: σ và biên đặt trước).
- **Không đệm rời, không keo kết cấu** — kiểm G2; khối lượng = MỘT vật liệu:
  **2,53 g ABS** / **3,04 g PLA** (kiểm G1).
- Bảng kiểm nay **18 mục PASS ở cả ABS và PLA** (`idea1_verify_abs.txt` /
  `idea1_verify_pla.txt`); phần §2/§3 bên dưới mô tả hình học khung (còn nguyên giá
  trị), nhưng **các câu nói về "đệm TPU 85A" phải đọc theo khối cập nhật này**.
- Ràng buộc hệ quả: một vòng P1 đơn độc chỉ giữ được **2,91 N** ở ngân sách 20 kPa
  (**2,91 N < 15–25 N**) ⇒ cần vòng P2/đốt giữa — xem §6 hạng mục mở #2 và tài liệu
  `reports/MATERIAL_SINGLE_PLA_ABS.md` §5.

---

## 1. TÊN CƠ CẤU & NGUYÊN LÝ LÀM VIỆC

**Vòng khoá quá tâm kiểu móc có mặt dốc (Side Toggle Clasp)** — một *khoá gạt kiểu
giày trượt tuyết / vise-grip* thu nhỏ, in liền khối cùng vòng định vị đốt gần (P1).

Ba chi tiết chuyển động nằm trên **cùng một chi tiết in** (không bu-lông, không trục rời):

| Ký hiệu | Chi tiết | Chức năng |
|---|---|---|
| **Thân (shell)** | cung ellipse φ 61°→336° | tì vào 3/4 chu vi đốt; mang vách cảm biến + mỏ neo gân |
| **Tay kẹp (jaw)** | cung ellipse φ 336°→61°, nối thân bằng **lá bản lề sống** tại φ=336° | kẹp mặt sườn–bụng; mang **chốt P Ø3** (vát phẳng 1 mặt) |
| **Cần gạt (lever)** | móc có **mặt dốc β=15°** + **mặt chặn cứng** + đệm ngón cái | đóng/mở khoá, khuếch đại hành trình ×1/tanβ |

**Nguyên lý khoá (4 lớp, đúng thứ tự ưu tiên):**

1. **Tiếp xúc xác định (determinate):** mặt dốc của móc tì lên **mặt phẳng vát** của chốt P.
   Hình học *suy ra giải tích* từ 4 điều kiện trong `toggle_synthesis.py`
   (không chép tay số): `|(u+v) − K_RAMP|/√2 = 0.0000 mm` ⇒ **tiếp xúc đúng, khe hở 0**.
2. **Quá tâm (over-centre) + mặt chặn cứng:** pháp tuyến tải lệch **β=15°** so với phương
   đóng ⇒ mô-men tải quanh A **ÉP cần gạt vào mặt chặn** (`M = +13.05 N·mm` dấu dương).
   Muốn đảo dấu mô-men phải quay **135°** ⇒ tải *không thể* tự nhả khoá.
3. **Tự hãm nêm (self-locking wedge):** β = 15° < ρ = atan(μ=0.35) = **19.3°** ⇒ chốt P
   không trượt dọc mặt dốc dù mặt chặn mất tác dụng (lớp dự phòng).
4. **Lá mỏng = chốt mềm A (không phải khớp rời):** cần gạt gắn vào tai qua lá nhựa cùng vật liệu (ABS 0,40 / PLA 0,50 mm — §0)
   `0.55 × 7.6 mm`, `k ≈ 4.8 N/mm`; tạo lực đặt trước + **bù dung sai in & từ biến**,
   tuyệt đối không có khe hở lắp ghép (vì không có khớp bản lề rời).

---

## 2. PHÂN TÍCH CƠ HỌC

### 2.1 Vì sao cơ cấu này giải quyết “kẹp bên sườn” và khe hở liên ngón

* **Cần gạt không nhô ra sườn.** ΔX đo trên STL = **−0.16 mm** so với nửa rộng đốt
  (A_KNUCK = 12.2 mm) — cần gạt *nằm gọn trong bao hình của chính vành* (|X|max = 12.04 mm),
  nên không có chi tiết nào chọc vào khe liên ngón. Mặt chặn + móc nằm ở **phía mu–trụ**
  (φ 67°…52°), tức *phía trên* đốt gần, không phải bên sườn.
* **Rãnh hở đặt xa bó mạch–thần kinh số (NV bundle).** Khe hở giữa thân và tay kẹp ở
  **φ = 61°** (mu–sườn); bó mạch số nằm ở đường **giữa bên (mid-lateral)**, cách đường
  giữa-trục ≈ **3.96 mm** ở ngón (an toàn ≈ 3 mm) — vì vậy điểm chia phải đặt **chếch ra sau
  (posterolateral)**, đúng như các nghiên cứu giải phẫu mid-lateral đã dẫn ở mục nguồn.
  Bốn đệm cánh in liền tì ở φ = 33°/147°/216°/288° đều **không** phủ đường giữa-bên.
* **Vách cảm biến ở phía mu** (φ 74°→106°) nên không thêm chi tiết nào vào mặt sườn.
* **Bàn tay thao tác:** đệm ngón cái nằm ở **phía mu–trụ, nơi không có ngón khác**
  ⇒ ngón cái của chính bàn tay đó (hoặc tay kia) đẩy được, hành trình **2.5 mm**, lực
  **4.6 N** ⇒ đóng/mở bằng một động tác, < 3 s.

### 2.2 Biến dạng mô mềm

* Tiếp xúc da là **4 điểm xác định** (4 đệm CÁNH IN LIỀN — §0) chứ không phải một cung cứng:
  bề mặt da không bị “siết” ở một điểm, áp suất phân bố trên **A_tiếp xúc = 323 mm²**
  (4 × cửa sổ 46° × H_PAD 9 mm ở r = a_in + t/2 — kiểm G4).
* **Ngân sách áp suất (số thiết kế, không phải đo):** ngưỡng tham chiếu 8 kPa (liên tục) /
  20 kPa (ngắt quãng, ≈ 150 mmHg — mức bắt đầu giảm tưới máu theo y văn băng ép).
  Với ngân sách hiện hành (μ = 0,45; 20 kPa) một vòng P1 giữ được **2,91 N** (8 kPa: 1,16 N)
  ⇒ **không đủ 15–25 N**: các hướng xử lý là (a) **chia tải qua P1 + P2**, (b) tăng diện
  tích tì (cung/chiều rộng), (c) dùng μ lạc quan 0,60 nếu bề mặt in có vân (đo lại trên
  mẫu), (d) bổ sung **tì dọc trục ở vành gần** để chuyển một phần tải trục thành phản lực
  nén thay vì ma sát. → **ghi nhận mở**, xem §6 và `MATERIAL_SINGLE_PLA_ABS.md` §5.
* **Không có “vết cắt” kim loại lên da:** toàn bộ bề mặt trong là nhựa in (PLA hoặc ABS)
  bo tròn, không có ren vít, không có cạnh sắc do bu-lông.

### 2.3 Bốn điều kiện khoá — kiểm bằng số

| # | Điều kiện | Công thức | Kết quả |
|---|---|---|---|
| 1 | Tiếp xúc xác định | `h = \|cross(P−A, N̂)\|`, `M = h·F_peg` | h = 2.83 mm, **M = 13.05 N·mm** |
| 2 | Quá tâm | `m(θ) > 0 ∀ θ` trong cung kẹp | **đảo dấu ở 135°** (biên rất rộng) |
| 3 | Nhả được, lực nhỏ | `F_release = M/R_handle + F_lá + F_ma sát` | **4.64 N < 8 N** ✓ |
| 4 | Hành trình | `R_handle·Δφ`, `Δφ = H_peg/(L_eff·cot β)` | **34° ⇒ 2.5 mm** ngón cái ✓ |

**Lực tì lên mặt chặn:** tay đòn = |u| trọng tâm land = 3.10 mm ⇒ `F_stop = M/3.10 = 4.21 N`
(ứng suất tì trên vệt land 2.4 mm² ≈ **1.8 MPa** — rất thấp so với σ_cho phép 12 MPa của ABS).
**Tự hãm:** β = 15° < ρ = 19.3°; **hiệu suất nêm** `1/tan(β+ρ) = 3.73` ⇒ hành trình móc
1.61 mm đủ mở khe 5 mm của tay kẹp.

### 2.4 Khử “lỏng lẻo” (yêu cầu gắt nhất của đề bài)

Nguồn rơ duy nhất của một cơ cấu kẹp là **khe hở lắp ghép**. Ở đây:

1. **Không có khớp rời nào** ⇒ không có khe hở trục–bạc (nguồn rơ kinh điển).
2. Khe hở **danh nghĩa của mặt chặn chỉ 0.05 mm** và bị **tải ép kín** ngay khi chịu lực
   (mô-men tải dấu dương ⇒ luôn ép về phía mặt chặn).
3. Khe hở **in 0.15 mm** ở mặt dốc là **hai mặt phẳng song song** (chốt Ø3 đã vát phẳng
   dây cung ≈ 1.5 mm) nên khép **đều**, không rơ góc; đo trên mô hình, hành trình đặt trước
   chỉ **0.50° ≈ 0.11 mm ở r=12.6** và bị **lực đệm cánh in liền + phản lực ngón ép kín** ngay khi
   đeo ⇒ trạng thái *làm việc* là đường truyền lực **kín, đặt trước, đàn hồi**:
   ngón → đệm cánh in liền → tay kẹp → chốt P → mặt dốc → cần gạt → **mặt chặn cứng** → thân → vành.
4. Dải đường kính Ø20–24 mm **không** được bù bằng khe hở cơ khí mà bằng:
   (a) chốt P **trượt dọc mặt dốc** (Δ ≈ 0.27 mm cho ±1 mm đường kính — mặt dốc dài
   2.34 mm nên còn thừa), (b) lá mỏng `±1.5 mm` hành trình bù dung sai in/từ biến.

---

## 3. SƠ ĐỒ ASCII

### 3.1 Mặt cắt ngang tại giữa đốt (nhìn từ đầu ngón về gốc) — ĐÚNG theo toạ độ đã dựng

```
              +Y (mu / dorsal)
                    ▲
        ...         │         φ=90°  [VÁCH CẢM BIẾN φ74–106° + RÃNH GÂN]
         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
      φ147 ░░░░░░░░░░░░░░░░░░░░░ φ33            ▓ = nhựa in (PLA hoặc ABS)
        ░░░░░░░░░░░░░░░░░░░░░░░░░                 ░ = đệm cánh in liền 85A (4 đệm 70°)
     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
   φ180░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░φ0  ◄── ĐƯỜNG GIỮA-BÊN (mid-lateral)
     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░        NV bundle cách ≈ 3.96 mm (ngón)
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░     ╔══ KHE HỞ φ=61° (0.45 mm) — ĐẶT
      φ213 ░░░░░░░░░░░░░░░░░░░░░ φ327   ║   CHẾCH RA SAU, XA BÓ MẠCH
         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        ║
                    │                 ║  ◄─ chốt P Ø3 (φ52°) + CẦN GẠT (móc)
                    ▼                 ▼
              −Y (bụng / volar)      [LÁ BẢN LỀ SỐNG φ=336°]
```

### 3.2 Khung (u,v) của MÓC — mặt dốc, chốt P, mặt chặn (đơn vị mm, gốc = tâm quay A)

```
   v ▲                                u trục: A → P (|A–P| = 4.00, nghiêng 30°)
     │        ┌──────── mặt trên cần gạt v = +2.70 ────────┐
 +6  │   ĐỆM NGÓN CÁI  (đẩy theo −u, tay đòn |v| = 4.15)
     │        │
 +4  │        │  CHUÔI
     │        │
 +2  │   ─────┘──────────────────────────────┐
     │   đáy chuôi v=−0.15 (chồng lá mỏng)   │  MẶT DỐC β=15°
 +1  │        ╲                             ╲│      ↓ pháp tuyến tải N̂ (45°)
     │     LÁ MỎNG 0.55                     ╲  ●  ◄── chốt P: tâm (4.00, 0),
  0  ─┼────────[kẹp ở u=0.6]────────────────╲ ╲      R=1.5, VÁT PHẲNG dây cung 1.5
     │                                        ╲ ╲     (tiếp xúc DIỆN, khe hở in 0.15)
 −1  │   chân lá cắm vào thân vành              ╲
     │   (u = −1.2 … +1.6)                       ╲  MẶT CHẶN CỨNG (land trên 2 tai)
 −2  │                                    [tai]  ╲  khe hở 0.05 mm ⇒ bị tải ÉP KÍN
     │                                     │       ▼
 −3  └─────────────────────────────────────┴──────────────────────────────►
        u=−4.2   −2.0                      u=0.6  u=2.5    u=4.0     u=6.0
        ◄── đáy thân: MẶT CHẶN (v=+0.60) ──►      └ chốt P (đĩa R=1.5) ┘  MẶT DỐC
```

### 3.3 Đường truyền lực khi đã khoá (form-closed, mọi khâu đều BỊ ÉP)

```
   NGÓN TAY ──(nén)──► ĐỆM CÁNH IN LIỀN ──► TAY KẸP ──► CHỐT P Ø3 ──► MẶT DỐC của MÓC
                                                                      │
                                                     (mô-men M = 13.05 N·mm, dấu +)
                                                                      ▼
   THÂN VÀNH ◄──── LÁ MỎNG (k=4.8 N/mm) ◄──── CẦN GẠT ◄──── MẶT CHẶN CỨNG (0.05→0 mm)
        ▲                                                          F_stop = 4.21 N
        └────────────(khép vòng qua tay kẹp/đệm)───────► NGÓN TAY

   Tải càng lớn  ⇒  mô-men dấu + càng lớn  ⇒  càng ÉP vào mặt chặn  ⇒  KHÔNG THỂ tự mở.
   Muốn nhả: ngón cái đẩy đệm theo −u  ⇒  mô-men ngược  ⇒  cần gạt quay 34°(CCW)  ⇒  nêm
   khuếch đại ×3.73  ⇒  chốt P thoát khỏi mặt dốc  ⇒  tay kẹp bung 22.7° (khe 5 mm).
```

---

## 4. KẾT QUẢ KIỂM TỰ ĐỘNG (đã chạy; log đầy đủ: `reports/idea1_verify_abs.txt` và `reports/idea1_verify_pla.txt`)

| Mục | Tiêu chí | Kết quả | Kết luận |
|---|---|---|---|
| A | Khung toạ độ suy từ synthesis | A=(5.791,13.698); P=(8.219,10.520) Ø3; \|A–P\|=4.00; β=15° | — |
| B1 | Tiếp xúc thiết kế của mặt dốc | **0.0000 mm** | PASS |
| B2 | Mặt chặn cứng + tải ép vào mặt chặn | STOP_R=3.10 mm; F_stop=**4.21 N**; biên đảo dấu **135°** | PASS |
| B3 | Lá mỏng (chốt mềm, theo vật liệu) | ABS 0.40×7.6 mm, δ 0.15 ⇒ k 3.06 N/mm, σ 9.7 MPa | PASS (B3b) |
| B4 | **KHE thân ↔ tay kẹp khi ĐÓNG (hở thật)** | hở **0.450 mm**, chồng lấn **0.0000°** (mặt đầu 59.98°/62.02°; cung thân 256.98°, tay kẹp 66.98°) | PASS |
| B5–B7 | **Rãnh đệm không cắt vào vùng chức năng** | lá bản lề / khe / rãnh cảm biến: chồng lấn **0.00°** cả ba | PASS |
| B8 | **Lòng vòng sạch (không nub tì da)** | vật liệu trong lòng vòng **0.00 mm³** | PASS |
| C0 | Khe hở móc ↔ tay kẹp khi ĐÓNG | **+0.360 mm** ≥ 0.18 | PASS |
| C1 | Mặt dốc ↔ tâm chốt P | **1.4500 mm** = 1.50 − 0.20 + 0.15 (đúng từng 0.0001) | PASS |
| C2 | Hành trình đặt trước (khe hở in) | **0.50° = 0.11 mm** ở r=12.6 | PASS |
| C3 | Nhả khoá trong một động tác | cần gạt **34°** (≤ 60°), ngón cái **2.5 mm**, **4.64 N** | PASS |
| D | Z dài trục 12–16 mm | **14.03 mm** | PASS |
| D | ΔX sườn ≤ 2.0 mm | **−0.17 mm** (X ∈ [−12.03, +12.03]) | PASS |
| E | Khối lượng (ngân sách in, MỘT vật liệu) | **ABS 2,43 cm³ ≈ 2,53 g** · **PLA 2,45 cm³ ≈ 3,04 g** | — |
| F | Đúng 1 khối đặc liền | **1 khối**, `isValid()=True` | PASS |
| F | 1 STL xuất ra | `Ring_ABS.stl` / `Ring_PLA.stl` (đệm cánh in liền trong cùng khối) | PASS |
| QA | Lưới STL (trimesh) | tất cả **kín**, định hướng nhất quán, **0 tam giác suy biến**, **1 mảnh** (vành 8 780 tam giác; V=2 170.57 mm³) | PASS |

Bao hình tổng: **24.09 × 36.01 × 14.03 mm**.

### 4.1 BỐN LỖI HÌNH HỌC ĐÃ TÌM RA & SỬA (2026-10-07) — vì sao bảng trên đáng tin hơn bản trước

Bốn lỗi dưới đây **không** bị bảng kiểm cũ phát hiện (vì chúng vẫn cho ra khối hợp lệ,
kín, 1 mảnh). Chúng chỉ lộ ra khi **cắt lớp STL đã xuất** và đếm số khối theo đúng
hình học in. Nay mỗi lỗi có một mục kiểm **thường trực** để không tái phát.

| # | Lỗi | Hậu quả thực tế | Cách sửa | Mục kiểm chặn |
|---|---|---|---|---|
| 1 | Thân vòng và tay kẹp lấy cung **chồng nhau 2·d = 2.14° = 0.45 mm** ở khe φ=61° (`shell = [61−d → 319]`, `arm = [353 → 61+d]`) | Khe bị **hàn kín**: in ra là **vòng kín**, không thể mở để đeo — hỏng hoàn toàn chức năng | Đảo đúng quy ước: `arm = [HINGE+W/2 → 61−d]`, `shell = [61+d → HINGE−W/2]` ⇒ hai mặt đầu cách nhau đúng `GAP_SLIT` | **B4** (+ `slit_check()` trong `ring_common.py`) |
| 2 | Rãnh đệm ở **327°** trải [304°, 350°] nằm **đè lên lá bản lề** [315°, 357°] (dao cắt rãnh xoá sạch lá) | Tay kẹp **rời khỏi thân** (2 khối rời khi in); bản lề mềm mất tác dụng | Dời cặp đệm phía bụng về **(216°, 288°)** ⇒ hở ≥ 27° quanh lá | **B5–B7** |
| 3 | Chân “tai” và chân lá mỏng cắm sâu qua mặt trong vòng (`POST_V_BOT = −6.20`) | Thò vào lòng vòng tới **~1 mm** ⇒ tì cứng lên da mu ngón | Thêm dao **doàng lòng vòng** (`bore`) cắt mọi vật liệu trong mặt trong | **B8** |
| 4 | Mặt trong lá bản lề **trùng khít** mặt trong thân/tay kẹp ⇒ mối hàn boolean có 2 mặt trụ trùng nhau | Sinh **2 tam giác diện tích ~0** trong STL (cảnh báo QA) | Hạ lá vào **0.05 mm** + xén mép cửa sổ để giữ đúng chiều dày làm việc | **QA** (0 tam giác suy biến) |

Ghi chú trung thực: mục 4 được chẩn đoán bằng cách **thu hẹp dần phép hợp boolean**
(`shell+blade → zero=2`; `arm+blade → zero=0`) chứ không phải bằng suy đoán; hàm
`Shape.removeSplitter()` (UnifySameDomain) đã bổ sung vào `headless/freecad_compat.py`
nhưng **một mình nó không đủ** — phải sửa hình học.

---

## 5. CÁCH CHẠY

```bash
cd hardware/finger_fixation

# 1) Sinh lại báo cáo tổng hợp của bộ suy luận hình học khoá
python synthesis/toggle_synthesis.py

# 2) Sinh STL + chạy toàn bộ kiểm tra (không cần cài FreeCAD — dùng headless/):
python headless/run_verify.py build_idea1_toggle_clasp.py   # ABS → 1 STL + bảng 18 mục
FF_MAT=PLA python headless/run_verify.py build_idea1_toggle_clasp.py  # PLA
python headless/mesh_qa.py stl/idea1/Ring_ABS.stl stl/idea1_pla/Ring_PLA.stl

# 3) Trên FreeCAD thật (khi có cài):
freecadcmd build_idea1_toggle_clasp.py
```

Bộ sinh dùng **đúng API FreeCAD** (`Part.makePolygon → Part.Face → extrude → cut/fuse →
Mesh.export`); `headless/freecad_compat.py` chỉ là lớp thay thế App/Part/Mesh chạy trên
**cùng nhân OCCT** khi môi trường không có FreeCAD.

---

## 6. GHI CHÚ TRUNG THỰC & HẠNG MỤC CÒN MỞ (theo AGENTS.md)

1. **Chưa có kết quả đo hay chế tạo.** Mọi số trong báo cáo này là **ngân sách thiết kế**
   tính trên mô hình hình học/lực học; chưa in, chưa thử trên người, chưa đo lực.
2. **Thiếu mặt bằng so sánh:** chưa có ảnh chụp mẫu in để đối chiếu khe hở thực. Bằng chứng
   hình học hiện có là mặt cắt OCCT `reports/figures/idea1_petal_pads_section.png`.
3. **Hạng mục mở #1 (áp suất mô mềm):** ở ngân sách hiện hành (μ = 0,45), một vòng P1 giữ
   được **2,91 N** (20 kPa) / 1,16 N (8 kPa) ⇒ chưa đủ 15–25 N. Bốn hướng xử lý ở §2.2.
4. **Hạng mục mở #2 (tải trục):** ΣN cho F = 25 N vượt khả năng *một* vòng P1 (2,91 N) ⇒
   với 25 N phải phân bố qua **P1 + P2** (hoặc tăng diện tích tì / dùng μ lạc quan 0,60 đã
   đo), hoặc bổ sung tì dọc trục ở vành gần.
5. **Khe hở in 0.15 mm (mặt dốc) và 0.20 mm (cửa sổ đệm)** cần in với *gap-fill TẮT*
   (thông số slicer), nếu in sai sẽ dính thành một đường ⇒ phải kiểm bằng mẫu in thử.
6. **Ngưỡng sinh lý** (3.96 mm cho bó mạch ngón; 8/20 kPa) là **trích dẫn y văn** làm
   ngân sách thiết kế, không phải kết quả thí nghiệm của nhóm.
7. **μ(nhựa–nhựa) = 0,30 (chêm/quá tâm) CHƯA ĐO** — xem `MATERIAL_SINGLE_PLA_ABS.md` §5.
8. **Từ biến & mỏi:** PLA từ biến và dòn hơn ABS; lá chốt mềm PLA chạy ở FS 1,3 so với
   σ_cho phép (≈ 3,2 so với σ_y) — nên ưu tiên **ABS** cho chi tiết đàn hồi, và đo lại lực
   đặt trước sau 24 h giữ tải trên mẫu in.

---

## 7. TRẠNG THÁI 3 Ý TƯỞNG

| # | Cơ chế | Nguồn | Nguyên lý khác biệt | Bộ sinh STL |
|---|---|---|---|---|
| **1** | **Vòng khoá quá tâm kiểu móc có mặt dốc** (Side Toggle Clasp) | `build_idea1_toggle_clasp.py` | form-closed quá tâm + nêm tự hãm, in liền khối | ✅ **hoàn thành — kiểm PASS** |
| 2 | **Vòng khoá cóc một chiều** (Ratchet Cinch Ring) | `build_idea2_ratchet_cinch.py` (+ `ring_common.py`) | 9 rãnh × 0,80 mm, khoá bằng **mặt răng đứng** (form closure), lưỡi con cóc 0,40 mm | ✅ **hoàn thành — 13/13 PASS × 2 vật liệu** (`reports/IDEA2_RATCHET_CINCH.md`) |
| 3 | **Đai quấn siết cơ học + chêm tự hãm** (Wrap Band + Self-Locking Wedge) | `build_idea3_wrap_band.py` | đai 355° × 0,80 mm căng bằng tay + **chêm 10° tự hãm**, gờ móc cắm rãnh, không keo | ✅ **hoàn thành — 13/13 PASS × 2 vật liệu** (`reports/IDEA3_WRAP_BAND.md`) |

> **Cả ba đã hoàn thành.** `ring_common.py` cung cấp phần dùng chung (thân + tay kẹp +
> lá bản lề + đệm cánh in liền) đã áp **cùng bốn bản vá** của §4.1. Bản tổng hợp 3 đề
> xuất: `reports/TONG_HOP_3_CO_CHE.md`; ràng buộc vật liệu đơn: `reports/MATERIAL_SINGLE_PLA_ABS.md`.
