# RÀNG BUỘC VẬT LIỆU ĐƠN: CHỈ PLA HOẶC ABS, KHÔNG THÊM CHI TIẾT PHỤ

> **Áp dụng từ:** 2026-10-07 (yêu cầu chủ dự án: *"chỉ có nhựa PLA hoặc ABS, cố gắng
> không thêm phần khác"*) — **thay thế** danh sách vật liệu cũ PETG + TPU 95A/85A trong
> các bản trước.
> **Phạm vi:** cả 3 ý tưởng trong `hardware/finger_fixation/`.
> **Bằng chứng chạy:** `reports/idea{1,2,3}_verify_{abs,pla}.txt`, `reports/mesh_qa_log.txt`,
> `reports/freecad_api_audit.txt`.

Mọi số trong tài liệu này là **ngân sách thiết kế** (tính từ mô hình), **không phải kết quả
đo**; nguồn tham chiếu ở §6. Chưa in, chưa thử trên người.

---

## 1. VÌ SAO THAY ĐỔI NÀY KHÓ HƠN BẢN CŨ

| Bản cũ (PETG + TPU) | Bản mới (một vật liệu cứng) |
|---|---|
| Đệm TPU 85A (E ≈ 4 MPa) đàn hồi **rất mềm**, tự ôm theo mô mềm | Nhựa cứng E = 2.000–3.500 MPa ⇒ **đệm đàn hồi phải làm bằng chính nhựa cứng**: rất mỏng + cung tự do dài |
| Đai TPU quấn 355°: lực kẹp sinh từ **biến dạng ε ≈ 6 %** | Đai nhựa cứng ε_cho phép 1–2 % ⇒ **không thể** dùng biến dạng để tạo lực kẹp ⇒ phải khoá bằng **căng cơ học + chêm tự hãm** |
| Gờ TPU bám/miết vào rãnh (nhờ mềm) | Form closure **hình học thuần**: gờ nhựa cứng cắm vào rãnh khoét (khe 0,30 mm) |
| Dán kết cấu đai–khung để chống trượt trục | **Bỏ keo**: tải trục đi qua **2 vai máng** (form closure, σ_bearing 0,19 MPa) |
| Đệm TPU rời, có thể thay | **Đệm cánh in liền** (petal pads) — cùng vật liệu, cùng một chi tiết in |

Hệ quả thiết kế bắt buộc: **mọi chỗ dựa vào ma sát phải chuyển thành form closure**; mọi
chỗ cần đàn hồi phải dùng **cánh mỏng ngàm một đầu có mặt chặn cứng** (hard stop), và mọi
tải phải được kiểm bằng **ứng suất cho phép σ_y/2,5**.

---

## 2. BẢNG VẬT LIỆU DÙNG TRONG THIẾT KẾ (`params.py` §6)

| Thông số | **PLA** | **ABS** | Nguồn/ghi chú |
|---|---|---|---|
| Khối lượng riêng ρ (g/cm³) | 1,24 | 1,04 | tài liệu nhà cung cấp nhựa in phổ thông |
| Mô đun đàn hồi E (MPa) | 3.500 | 2.000 | bảng tính chất FDM; ABS in ra thường ~0,8–1,0 GPa, PLA ~1,0–3,5 GPa ⇒ **dùng giá trị danh nghĩa trong tài liệu** |
| Giới hạn chảy σ_y (MPa) | 55 | 30 | PLA UTS 50–60 MPa; ABS σ_y 30–40 MPa |
| Biến dạng đứt ε | **1,0 %** (giòn) | **2,0 %** (dẻo hơn) | dùng để chọn giới hạn biến dạng cho chi tiết đàn hồi |
| σ_cho phép thiết kế = σ_y/2,5 | **22 MPa** | **12 MPa** | `P.sig_allow()`; FS 2,5 áp cho cả hai |
| μ với da — ngân sách thiết kế | 0,45 | 0,45 | Zhang & Mak: tổng thể 0,46 ± 0,15; PP–da 0,22–0,45 (giảm khi ướt) ⇒ giữ 0,45 |
| μ với da — kịch bản lạc quan | 0,60 | 0,60 | da khô/không lông + bề mặt in có vân |
| μ nhựa–nhựa (cho chêm tự hãm) = `mu_self` | **0,30 (CHƯA ĐO)** | **0,30 (CHƯA ĐO)** | ngân sách thiết kế — xem §5 |

**Hệ số an toàn 2,5** được chọn vì với chi tiết in FDM, σ_y danh nghĩa không phản ánh
khuyết tật lớp in, hướng in và mỏi; các mục kiểm in rõ FS đạt được.

---

## 3. QUY TẮC THIẾT KẾ ĐÃ ÁP VÀO CẢ 3 Ý TƯỞNG

1. **Chi tiết đàn hồi = công xôn mỏng, dài, có mặt chặn cứng.**
   σ_ngàm = 1,5·E·t·δ/L² ≤ σ_cho phép. Vì **E nhựa cứng lớn gấp ~500–900× TPU**, hành
   trình δ phải **nhỏ** (0,12–0,60 mm) và **L dài** (4,3–8,0 mm); bề dày chọn **theo vật
   liệu** (`ring_common.pick_leaf_t`).
2. **Không tin vào ma sát để chịu tải trục.** Lực trục 15–25 N được chặn bằng **hình học**:
   mặt chặn cứng (Ý tưởng 1), mặt răng đứng (Ý tưởng 2), vai máng + gờ móc (Ý tưởng 3).
3. **Đệm tì in liền (petal pads).** 4 cửa sổ × 46° tại φ = 33° / 147° / 216° / 288°
   (dorsolateral, **tránh** đường giữa-bên và **tránh vùng A1**); hành trình đàn hồi
   0,20 mm rồi **tì chặn cứng**; tường sau 0,60 mm.
4. **Khe in (printed clearance) chỉ nằm trong khoảng 0,03–0,45 mm**, luôn có mặt chặn
   cứng ở cuối hành trình ⇒ không có "khe tự do" trong trạng thái làm việc.
5. **Không keo, không đệm rời, không vít kim loại** — mỗi ý tưởng là **một (hoặc ba) chi
   tiết in** cùng vật liệu, có mục kiểm G1/G2 tự động.

---

## 4. TÁC ĐỘNG LÊN TỪNG Ý TƯỞNG (thay gì, kết quả ra sao)

| | Bản cũ (PETG + TPU) | Bản một vật liệu | Kết quả sau khi đổi |
|---|---|---|---|
| **Ý tưởng 1** | vòng PETG + 4 đệm TPU rời | 1 chi tiết in: vòng + 4 đệm cánh in liền (ABS 0,60 / PLA 0,50 mm) | **18/18 PASS × 2 vật liệu**; đệm tì 1,56 N, σ_tì 10,0 (ABS, FS 1,20) / 14,7 MPa (PLA, FS 1,49); lá chốt mềm ABS 0,40 × 0,15 mm ⇒ σ 9,7 (FS 1,2), PLA 0,50 × 0,12 mm ⇒ σ 17,0 (FS 1,3) |
| **Ý tưởng 2** | vòng PETG + lá 0,50 + 4 đệm TPU | 1 chi tiết in: thân + tay kẹp + con cóc + 4 đệm cánh in liền | **13/13 PASS × 2**; lá cóc 0,40 mm, công xôn 8,02 mm ⇒ k 0,55 (ABS)/0,96 N/mm (PLA), F_vượt nấc 0,27/0,48 N, σ FS ≈ 2,7/2,8 |
| **Ý tưởng 3** | đai TPU ε ≈ 6 % + keo kết cấu | khung + **đai nhựa cứng 0,80 mm** + **chêm 10° tự hãm**; bỏ keo | **13/13 PASS × 2**; T 9,0 N ⇒ ΣN 56,5 N, giữ trục 25,4 N, nhưng p 87,2 kPa — xem §5 hạng mục #1 |

**Các chỉ tiêu vẫn đạt của brief** (cả hai vật liệu): ΔX ≤ 2,0 mm/đốt (Ý1 −0,16 · Ý2 +0,43 ·
Ý3 +1,15) · Z 12–16 mm (14,03 / 14,00 / 13,00) · một khối hợp lệ, `isValid()=True` ·
ẩn nhiệt in ở nozzle 0,4 mm (mọi tường ≥ 0,40 mm; đai 0,80 = 2 đường).

---

## 5. HAI KẾT QUẢ ÂM ĐÃ GHI THẲNG (không giấu) + HẠNG MỤC PHẢI ĐO

1. **Một vòng P1 đơn độc KHÔNG giữ được 25 N ở ngân sách áp lực an toàn.**
   Với μ = 0,45 và p = 20 kPa (ngưỡng ngắt quãng của đề cương): Ý tưởng 1/2 giữ
   **2,91 N**; Ý tưởng 3 hoặc giữ **25,4 N ở 87,2 kPa**, hoặc giữ **5,8 N ở 20 kPa**.
   ⇒ **Kết luận hệ thống: phải chia tải qua P1 + P2** (2 vòng/hoặc đai rộng hơn). Đây là
   cái giá của ràng buộc nhựa cứng — bản TPU cũ "tránh" được bằng mô mềm nhưng lại cần
   chi tiết phụ, trái yêu cầu mới.
2. **μ(nhựa–nhựa) = 0,30 CHƯA ĐO** — chêm tự hãm của Ý tưởng 3 (10°, tan = 0,176 ≤
   0,231) chỉ là **ngân sách**. Phải đo: cùng vật liệu, cùng hướng in, có/không bụi in,
   có/không ẩm — trước khi tin vào khoá một chiều.
3. **Từ biến (creep):** PLA "nguội" từ biến đáng kể ở tải tĩnh vài giờ–vài ngày
   ⇒ lực đặt trước của lá/đệm có thể giảm. **Đo lại lực tì sau 24 h giữ tải** trên mẫu in
   trước khi kết luận "không lỏng lẻo" trên thực tế.
4. **Mỏi:** chưa kiểm số chu kỳ. Khuyến nghị in **≥ 4 đường** cho mọi tường chịu tải
   (≥ 1,2 mm cho chi tiết chịu chu kỳ) và thử 500 chu kỳ đeo/tháo trên chốt giả.

---

## 6. NGUỒN THAM CHIẾU ĐÃ DÙNG (mức đọc: tóm tắt/bảng dữ liệu)

- **Tính chất cơ học nhựa in FDM** (σ, E, ε; khuyến nghị chọn vật liệu cho snap-fit/living
  hinge; PLA cứng–giòn, ABS dẻo hơn): tổng hợp từ các trang dữ liệu in ấn phổ thông
  (forgelabs, xometry, partmfg, tonerplastics) và một số bài PMC đối chiếu PLA/PETG
  (PMC6926899: PLA σ_y 60 MPa, ε_đứt ~6 %, E 3.600 MPa; PMC10880662: UTS PLA 59,9 ± 2,9).
  ⇒ **giá trị trong `params.py` được làm tròn xuống bảo thủ**, không dùng số cao nhất.
- **Ma sát da**: Zhang & Mak (1999) μ tổng thể da người–vật liệu 0,46 ± 0,15 (silicone
  0,61; nylon 0,37; gan bàn tay 0,62 ± 0,22); nghiên cứu PP–da 0,22–0,45 (thấp hơn khi
  ướt). ⇒ Dùng **0,45 ngân sách, 0,60 lạc quan**; **không** dùng số TPU/dẻo của bản cũ.
- **Ngưỡng áp lực mô mềm**: 8 kPa (liên tục) / 20 kPa (ngắt quãng) — từ ngân sách thiết kế
  mô mềm của đề cương (vùng 80–100 mmHg vẫn duy trì tưới máu).
- **Giải phẫu ngón (ngân sách an toàn)**: bó mạch-dây thần kinh sống ở ~3,96 mm (ngón,
  min 2,97) tính từ mặt da phía volar theo trục giữa — **thiết kế đệm dorsolateral**;
  nhánh cảm giác lưng mu có thể tách ra tại/ngay trên ròng rọc A1 trong ~62 % ca.

---

## 7. CÁCH CHẠY LẠI TOÀN BỘ (để tự kiểm)

```bash
cd hardware/finger_fixation
python headless/run_verify.py                     # ABS (mặc định) → 44/44 PASS
FF_MAT=PLA python headless/run_verify.py          # PLA → 44/44 PASS
python headless/mesh_qa.py $(ls stl/*/*.stl)      # QA cả 10 lưới
python headless/freecad_api_audit.py --write      # audit API FreeCAD
```

Kết quả mong đợi: **3/3 script PASS**, **10 STL** (`stl/ideaN` = ABS, `stl/ideaN_pla` =
PLA), QA lưới "TẤT CẢ LƯỚI STL ĐẠT".
