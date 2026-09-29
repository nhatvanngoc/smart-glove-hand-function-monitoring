# OUTLINE BÁO CÁO TOÀN VĂN — ViSEF

## Đề tài: Nghiên cứu và phát triển găng tay thông minh hỗ trợ đánh giá và theo dõi chức năng vận động bàn tay trong phục hồi chức năng sau đột quỵ

> **Học sinh:** Văn Ngọc Nhật Anh (11A2) + Nguyễn Duy Quân (12A1) — THPT Quảng Trị · GVHD: Lê Công Long
> **Phiên bản:** v3.0 — 2026-09-29 (đồng bộ cấu hình đã nộp ADS1115+INA333; áp dụng checklist M-01..M-27; chốt đồ nghề + trần E2E; AI chuyển thành thực nghiệm đối chứng; bỏ mục tiêu 3D/clinical)
> **"Viên đạn":** Theo dõi định lượng chức năng bàn tay tại nhà, liên tục giữa các lần tái khám lâm sàng.
> **Lưu ý:** Mọi ô `[X]` chỉ được điền **sau** khi đo. Không bịa số. Xem `AGENTS.md`. Mọi claim vượt dữ liệu bị cấm — xem B.9.

---

## A. VẤN ĐỀ NGHIÊN CỨU

### 1. Lý do chọn đề tài

*(Bản văn ở `docs/bao_cao/A1_ly_do_chon_de_tai.md` — đã sửa cite theo M-22/M-23/M-24.)*

Cấu trúc đoạn:
- Gánh nặng đột quỵ + di chứng liệt/yếu tay; vì sao đây là vấn đề con người, không phải vấn đề kỹ thuật. Số "1,5 triệu di chứng" ghi rõ là **ước tính của nhóm từ [1]**, không phải số in trong [1] (M-22).
- Phục hồi bàn tay = luyện tập tại nhà; kỹ thuật viên chỉ gặp bệnh nhân mỗi 1–3 tháng → quãng giữa là **"hộp đen"**.
- Công cụ hiện tại (FMA, ARAT, Box and Block, lực kế Jamar, E-Link) là **ảnh chụp tại thời điểm đo**, chi phí cao, chủ yếu ở cơ sở y tế. Tự ghi chép thủ công sai số lớn (Manumeter 2022).
- Xác nhận độc lập: hội đồng chuyên gia quốc tế 2024 (DOI 10.1109/OJEMB.2024.3523442) + nghiên cứu OTHER 2026 🔵 verify + **tham khảo ẩn danh** KTV VLTL-PHCN (DEC-ROLE-001: không tên, không năm kinh nghiệm, không quan hệ).
- Câu chốt tên đề tài + một câu mô tả giải pháp (vi sai hai vách + EI/GAP/RAL + trạm biên).

### 2. Mục tiêu nghiên cứu

*(Bản chốt ở `docs/bao_cao/A2_muc_tieu.md`)*
- Chế tạo găng 3 ngón (cái/trỏ/giữa): 12 phần tử Velostat trên khung vách cứng tiền tải + 1 ô chuẩn + 1 IMU mu tay.
- Xây dựng chuỗi đo vi sai hai vách (lòng–mu) + auto-zero + **định lượng phần dư** (không nói "triệt tiêu hoàn toàn").
- Trích xuất bộ ba chỉ số EI/GAP/RAL kèm nhãn độ tin cậy (công thức EI viết tường minh trước khi thu dữ liệu — M-25).
- Xây dựng trạm biên: thu log → kiểm soát chất lượng → dashboard + timeline sự kiện → báo cáo tuần cho KTV từ xa.
- Kiểm định toàn bộ trên giàn + phantom theo ngưỡng đăng ký trước (M1–M6 + C1.1–C1.10) + 1 thực nghiệm đối chứng luật-thường-vs-ML.

### 3. Tiêu chí của dự án

*(Bản chốt ở `docs/bao_cao/A3_tieu_chi.md`; số đo điền sau khi có log)*

| Mã | Chỉ tiêu | Ngưỡng (đăng ký trước) |
|---|---|---|
| M1/C1.2 | SNR tại ΔF = 1 N (≥10/12 kênh) | ≥ 18 dB |
| M2/C1.3 | γ, R² (dải 0,5–10 N) | γ ≥ 0,25; R² ≥ 0,90 |
| M3/C1.4/C1.5 | CV nội phiên / liên ngày | ≤ 5% / ≤ 8% |
| M4/C1.8 | Trôi/tín hiệu sau 10 ngày (+ auto-zero) | ≤ 2,0 |
| M5/C1.10 | fs toàn 12 kênh / trễ hệ thống | ≥ 20 Hz (danh định — M-02) / ≤ 500 ms |
| M6 | Phát hiện đeo sai (cửa sổ V_base, N = 20–30) | tỷ lệ phát hiện ≥ 80% |
| C1.1 | Sàn nhiễu / 5.000 mẫu tĩnh | Vpp ≤ 5 mV |
| C1.6/C1.7 | Hysteresis / creep (60 s @ 5 N) | h ≤ 18% / ≤ 8% |
| C1.9 | Đồng đều giữa các kênh | ≤ ±40% (+ bảng chuẩn hóa) |

### 4. Đối tượng và phạm vi nghiên cứu

*(Bản chốt ở `docs/bao_cao/A4_doi_tuong_pham_vi.md`)*
- **Kỹ thuật (đã nộp):** 12 phần tử + ô chuẩn + 1 IMU; cầu vi sai → INA333 → 2×CD74HC4067 → MCP6001 → ADS1115 → ESP32-S3 → BLE → Orange Pi 5 Pro (trạm dùng chung của trường).
- **Y sinh:** di chứng yếu/liệt tay sau đột quỵ — nghiên cứu nền; giai đoạn này chỉ bench/phantom.
- **Người đeo (M-26, TODO):** ghi rõ ai đeo (kể cả thành viên nhóm), khi nào, biện pháp an toàn (pin, cách ly, không lực tác động lên người).
- **Giới hạn:** không chẩn đoán; không can thiệp/vận động hộ trên người (AAN chỉ trên phantom); không thay thế đánh giá lâm sàng; không claim lâm sàng.

### 5. Địa điểm nghiên cứu và thực nghiệm

*(Bản chốt ở `docs/bao_cao/A5_dia_diem.md`)*
- Phòng thực hành vật lý, phòng sáng tạo trường THPT Quảng Trị, và tại nhà (09/2026–02/2027).
- Tham khảo thực tiễn: **01 KTV VLTL-PHCN (ẩn danh)** phản biện giao thức đo trên giấy — bằng chứng **nhu cầu**, không phải bằng chứng **kết quả**.

### 6. Phương pháp nghiên cứu

*(Bản chốt ở `docs/bao_cao/A6_phuong_phap.md`)*
- **Tổng quan tài liệu:** prior art găng cảm biến; công cụ đánh giá tay; đặc tính Velostat; hệ thống theo dõi tại nhà.
- **Tham khảo ý kiến:** KTV VLTL-PHCN (phiếu + ghi chép, ẩn danh) + chuyên gia độc lập.
- **Thực nghiệm bench:** chuẩn lực tĩnh = **quả cân đã cân (F = m·g)**; DMM chính FNIRSI 2C23T (spec datasheet) + scope/gen của máy + load cell 5 kg (sau khi có HX711); C1.1 đo bằng ADS1115 tự log + scope chứng kiến.
- **Thống kê (đăng ký trước):** CV, R², h, creep, tỷ số trôi, recall/precision (M6, E1–E4). Không hạ chuẩn sau khi thấy số.

---

## B. GIẢI PHÁP VÀ THIẾT KẾ

### 1. Tổng quan đề tài

**Sơ đồ pipeline (chốt theo cấu hình đã nộp + M-04/M-16/M-17):**

```
Bàn tay (3 ngón: cái/trỏ/giữa) · 2 khớp/ngón × 2 vách = 12 phần tử + 1 ô chuẩn
      ↓ [kênh = phần tử đơn; mỗi khớp = 1 cặp vi sai d = S_lòng − S_mu]
Cầu chia áp (R_ref = 10 kΩ 0,1%) → INA333 (G = [X] sau M-01) → 2×CD74HC4067
      ↓ [Vex = [X] TODO M-17]
MCP6001 → ADS1115 (16-bit, LSB 62,5 µV) → ESP32-S3 (lọc, auto-zero, BLE 20 Hz)
      ↓
Orange Pi 5 Pro — TRẠM ĐO (trường đã có):
  ├─ Thu log + database phiên đo
  ├─ Kiểm soát chất lượng 2 vòng lặp (V_base + phương sai phiên)
  ├─ Trích xuất EI/GAP/RAL + nhãn tin cậy
  ├─ Dashboard + timeline sự kiện + báo cáo tuần (PDF)
  ├─ Camera đối chứng góc (P1) + thực nghiệm E1–E4 rules-vs-ML (P1)
  └─ Không suy luận gập/duỗi bằng ML (dấu vi sai đã làm việc đó — M-08)
      ↓ [file báo cáo chuyển tay — không claim cloud]
KTV xem từ xa → duyệt cờ đỏ → quyết định chuyên môn (AI sàng lọc, người quyết định)
```

**Nguyên lý cơ khí (điểm kỹ thuật trung tâm):**
ngón tì vào vách khung → nén phần tử trên vách đó → cặp vi sai lòng–mu cho dấu hướng (d > 0 gập, d < 0 duỗi) + biên độ lực; IMU mu tay bù nghiêng + chuẩn hóa vận tốc góc. Drift đồng pha **giảm** ở tầng vi sai + auto-zero, **phần dư định lượng** qua C1.8.

### 2. Bất cập của các giải pháp hiện tại và giải pháp đề tài

| Giải pháp hiện tại | Bất cập | Giải pháp của đề tài |
|---|---|---|
| Lực kế Jamar | Chỉ đo tổng lực bóp, một thời điểm, cần người đo | Theo dõi tại nhà, nhiều ngón, theo thời gian |
| Hệ thống E-Link | Chi phí cao, chỉ ở cơ sở y tế | Linh kiện rẻ, dùng được tại nhà |
| Găng tay IMU/flex thương mại | Đắt theo số trục, trôi, cồng kềnh | Vách khung + vật liệu piezoresistive, mã hóa cả hướng và lực |
| Găng tay phục hồi chức năng chủ động (robot găng) | Gây phụ thuộc máy, rủi ro an toàn, cần người có chuyên môn | **Không can thiệp vào vận động** — chỉ đánh giá/theo dõi |
| Đeo cảm biến ở cổ tay | Không ghi được chuyển động ngón; không phân biệt vận động có mục đích | Đo tại từng khớp ngón |
| Phần mềm mô phỏng (RehabReach và tương tự) | Mô phỏng, thiếu vi cử động và không tương tác thực | Đo trực tiếp; 🔵 cần xác minh thông tin RehabReach trước khi đưa vào báo cáo |

> **Khoảng trống thật:** chưa có hệ thống nào **vừa rẻ, vừa tại nhà, vừa tạo ra dữ liệu định lượng chức năng bàn tay theo tuần**, dùng được bởi người không chuyên môn và theo dõi được bởi kỹ thuật viên từ xa — **và tự biết khi nào dữ liệu của mình không còn đáng tin**.

### 3. Thiết kế phần cứng

*(Chi tiết đầy đủ: `docs/04_Hardware_Architecture.md` §8)*

| STT | Linh kiện | SL | Chức năng | Trạng thái |
|---|---|---|---|---|
| 1 | Velostat + băng đồng (điện cực) | đủ 12 + chuẩn | Phần tử áp trở sandwich | đã có |
| 2 | Khung ốp ngón PETG + vít tiền tải Fp | 3 ngón | Vách cứng + cửa sổ preload | cần chế tạo |
| 3 | R_ref 10 kΩ 0,1% + INA333 (duy nhất — M-16) | 1 bộ | Cầu vi sai + khuếch đại (G sau M-01) | **mua chính hãng (P0)** |
| 4 | CD74HC4067 + MCP6001 + ADS1115 | 2+1+1 | Quét 13 đầu vào + ADC 16-bit | mua (P0) |
| 5 | ESP32-S3 | 1 | Lọc, auto-zero, BLE 20 Hz | đã có |
| 6 | LSM6DS3 (hoặc thay thế có ghi nhận) + SHT30 | 1+1 | Bù nghiêng + log T/RH | mua (P0) |
| 7 | TP4056 + HT7333 + LiPo 3,7 V | 1 bộ | Nguồn đeo cách ly lưới | mua (P0) |
| 8 | Orange Pi 5 Pro (trạm dùng chung) | 1 | Trạm đo + dashboard + báo cáo | **trường đã có** |
| 9 | Giàn: nhôm 2020 + ray + vít me + servo + khớp cứng + lò xo + quả cân | 1 | Kiểm định RAL/GAP/E1–E4 (bỏ phanh — M-20) | dựng (P0/P1) |
| 10 | Load cell 5 kg + HX711 + phantom silicone | 1 | Chuẩn động + tay giả | cell đã có; **HX711 mua ngay** |
| 11 | Thước đo góc + ẩm-nhiệt kế + camera USB | 1 | Góc chuẩn chính + T/RH + đối chứng (P1) | mua |

### 4. Nguyên lý sensing element và trích đặc trưng

**4.1 Cơ chế piezoresistive**
- Velostat: điện trở giảm khi nén; quan hệ **phi tuyến**, có hysteresis, creep, drift, phụ thuộc nhiệt-ẩm.
- Hệ quả: **không** chuyển ADC thành Newton; chỉ dùng đặc trưng **tương đối** và **động**; R(F) đo thật là nút M-01.

**4.2 Bố trí kênh (M-04)**
- 3 ngón × 2 khớp × 2 vách = **12 phần tử** + 1 ô chuẩn = 13 đầu vào ADC, tạo **6 cặp vi sai**.
- Bài tập chuẩn: gập/duỗi từng ngón, chụm, bóp, chạm ngón (thứ tự chốt cùng KTV).

**4.3 Bù drift + nhiệt (bản hẹp)**
- Cặp đối xứng → hiệu `d` giảm thành phần đồng pha; ô chuẩn + auto-zero đầu phiên.
- Nhiệt: **không chương riêng** — log T/RH mọi phiên (SHT30) + 1 đồ thị trôi-vs-T + hệ số r từ dữ liệu C1.8 + trích y văn.
- Cấm chữ "loại bỏ/triệt tiêu hoàn toàn drift" (M-10).

### 5. Luật thường trước, ML đối chứng (thay thế mục "Mô hình học máy" cũ)

- **Luật 0-tham-số gánh chính:** dấu vi sai → hướng; EI/GAP/RAL = phép tính số học + thống kê cổ điển.
- **Thực nghiệm đối chứng duy nhất (P1):** phân loại sự kiện E1–E4 (spike/rung/tuột/bão hòa — định nghĩa ở mức tín hiệu, không dùng từ y khoa) trên dữ liệu giàn + sự kiện giả lập cơ học; phe A luật ngưỡng (scope) vs phe B ML (RF/NN nhỏ); chia test theo phiên; metric chính recall + precision kèm baseline (M-08 chỉ sống lại dưới dạng benchmark đo thật).
- **Cấm:** phân loại MAS/chẩn đoán (M-15), góc từ tín hiệu (M-13), suy nguyên nhân GAP (M-14).

### 6. Đo góc độc lập cho GAP (thay thế mục "Tái tạo 3D" cũ)

- Chuẩn chính: **thước đo góc/goniometer** gắn trên giàn (P0). Đối chứng P1: camera + marker ArUco trên Pi (xử lý ảnh đã test OK).
- Tái tạo 3D đầy đủ + EKF + IMU từng đốt → **hướng phát triển**, không phải mục tiêu giai đoạn này.

### 7. Dashboard và theo dõi từ xa

- Người tập: hướng dẫn bài tập + thanh EI phản hồi tức thời.
- KTV (ngồi nhà): timeline sự kiện E1–E4 + đường cong tuần + **báo cáo PDF tự động**; bấm vào cờ đỏ xem sóng tín hiệu; chuyển file thủ công (USB/nhắn tin) — **không claim cloud/app**.
- Cảnh báo: chỉ khi vượt ngưỡng **và** dữ liệu ở trạng thái hợp lệ (không bị gắn "Nghi vấn").

### 8. Ngân sách (viết đúng phạm vi — M-21)

- Báo cáo ghi: **"thiết bị đeo < 1,5 triệu"** + **"trạm nhà dùng chung"** (Pi của trường, như máy tính KTV).
- Dự toán vận hành E2E < 10M (~5,5M: găng ~1,2M + giàn-đo ~3,2M + dự phòng ~1M) **chỉ nằm ở sổ tay** (`research/notebook/2026-09-29_measurability_M-checklist.md` §5), không vào báo cáo.

### 9. Những câu báo cáo sẽ KHÔNG nói (chống tái phạm M-10..M-15)

| Câu cấm | Thay bằng |
|---|---|
| "Triệt tiêu/triệt để drift/nhiệt" | "Giảm trôi đồng pha; phần dư định lượng qua C1.8" |
| "RAL giảm = bệnh cải thiện" | "RAL là đặc trưng giao thức kiểm định trên giàn" |
| "AI phát hiện co giật/co cứng/MAS…" | "AI gắn cờ sự kiện tín hiệu E1–E4; KTV diễn giải" |
| "Góc quy đổi từ tín hiệu" | "Góc đo độc lập (thước đo góc ± camera)" |
| "GAP do yếu cơ/co cứng" | "GAP ghi nhận chênh lệch; không tự suy nguyên nhân" |
| "AAN hỗ trợ tay người bệnh…" | Mọi câu AAN chỉ viết về phantom |
| "Suy luận INT8 < X ms" (chưa đo) | Chỉ ghi số đo thật + điều kiện đo |

---

## C. CHẾ TẠO MÔ HÌNH VÀ VẬN HÀNH THỬ NGHIỆM

*(Ma trận đo đầy đủ: notebook M-checklist §2; ngưỡng chốt trước khi đo — `research/protocols/08` §7.)*

### 1. Bench điện (M1/M2 + C1.1/C1.2/C1.3/C1.6/C1.7/C1.9)
- R(F) + γ + R² (DMM + quả cân) → **trả lời M-01/M-17** → tính lại G, Vex, chuỗi.
- SNR@1N (scope + log ADS1115); hys lên/xuống; creep 60 s; đồng đều kênh; Vpp 5.000 mẫu (phương pháp tách).

### 2. Lặp lại + drift + đeo (M3/M4/M6 + C1.4/C1.5/C1.8)
- CV nội phiên trên giàn; CV liên ngày tháo/đeo lại (3 ngày); drift 10 ngày 3 lần/ngày + T/RH.
- M6: cửa sổ V_base + 20–30 lần tháo/đeo, đếm phát hiện (đường lui: hạ thành quy trình thao tác).

### 3. Thời gian thực (M5/C1.10)
- fs toàn kênh ≥ 20 Hz (timestamp + scope kẹp DRDY); trễ đầu–cuối ≤ 500 ms (gen phát bước → GPIO mirror).

### 4. Giàn + phantom (RAL/GAP/EI)
- RAL: 10 chu kỳ/nấc, điểm cắt P_complete ≥ 80% (quả cân + đếm).
- GAP: kéo 2 vận tốc (PROM ω₁ ≈ 15°/s) + gập chủ động, góc đọc từ thước đo góc.
- EI: tính offline từ log theo công thức M-25; kiểm nhất quán giữa phiên.

### 5. Đối chứng + camera (P1)
- E1–E4: injector cơ học (búa/lò xo/nới vít) + spec sheet bằng scope → dataset → rules-vs-ML.
- Camera ArUco đối chứng góc vs thước đo góc (sai lệch cho phép vài độ, nếu không đạt thì camera chỉ minh họa).

### 6. Kết quả tích hợp hệ thống (ESP32-S3 ↔ Orange Pi)
- BLE 20 Hz thực đo, tỷ lệ lỗi/khung mất, trễ đầu–cuối, số phiên "Nghi vấn" đúng/sai.

### 7. Kết luận
- Bảng đối chiếu **A.3 → kết quả đo thật** (không ô trống, không claim vượt dữ liệu — M-05).
- Nêu rõ: proof-of-concept trên bench/phantom (+ người đeo ghi theo M-26); chưa thử trên bệnh nhân; không thay thế đánh giá lâm sàng.

### 8. Hướng phát triển
- Tái tạo 3D + EKF + IMU từng đốt; FPC/e-textile; app + cloud; ánh xạ lâm sàng (MAS…) **với đối tác bệnh viện + IRB**.

---

## TÀI LIỆU THAM KHẢO *(verify đầy đủ trước khi nộp — xem `research/evidence/SOURCE_LEDGER.csv`)*

- [ ] Tran M.C. et al., dịch tễ đột quỵ VN, *Global Epidemiology* 2025;9:100199 — đọc toàn văn (số 1,5M = nhóm tự nhân — M-22)
- [ ] Pollock A. et al., Cochrane 2014 — 80%/50% qua Background (← Langhorne 2009…); **không trích Hendricks 2002 cho 80%**
- [ ] Manumeter, *Sensors* 2022 — sai số tự ghi chép 🔵 đối chiếu mức đọc
- [ ] Amin K.R. et al., IEEE OJEMB 2024, DOI 10.1109/OJEMB.2024.3523442
- [ ] Găng từ tính, *Device* 2024 — **không ghi là Gloreha** (M-24)
- [ ] Lin B.-S. et al., *Sensors* 2022 — hệ đa cảm biến co cứng (n = 14, có IRB)
- [ ] ART-Glove, arXiv:2606.16370
- [ ] Liu et al., *A Reconfigurable Data Glove…*, *Engineering* 2024 — **không ghi IROS 2017** (M-24)
- [ ] ironHand 2016 + 2018
- [ ] *Custom Data Gloves* review, arXiv:2405.15417 🔵 xác minh bản IEEE Access nếu trích
- [ ] OTHER 2026, DOI 10.1080/09638288.2026.2643929 🔵 verify
- [ ] Velostat: MIT Media Lab 2012 (đã đọc) + Hopkins, IEEE Sensors J 2020 🔵 verify + bài Sensors & Actuators A 2018 🔵 verify ([18] cũ)
- [ ] Jamar + E-Link (giá/giới hạn) 🔵 bắt buộc đối chiếu lại
- [ ] Tham khảo KTV VLTL-PHCN (ẩn danh, phiếu + ghi chép) — ý kiến chuyên môn, **không** phải nghiên cứu định lượng
- [ ] Đồ nghề: FNIRSI 2C23T (spec theo datasheet/manual + Elektor 2024) — nêu tên máy + spec dùng trong báo cáo, chi tiết ở sổ tay

---

## GHI CHÚ CHO PHIÊN SAU

**Đã thay đổi trong v3.0 (2026-09-29):**
- ✅ Đồng bộ cấu hình đã nộp: cầu vi sai → INA333 → MUX → ADS1115 → ESP32-S3 → BLE → Pi (DEC-HW-005).
- ✅ Áp dụng checklist M-01..M-27: 20 Hz danh định, định nghĩa kênh, INA333 duy nhất, Vex TODO, tách ngân sách, cấm 7 nhóm câu (B.9).
- ✅ AI từ "đầu tàu" → 1 thực nghiệm đối chứng rules-vs-ML (P1); bỏ mục tiêu 3D/MAS/cloud khỏi giai đoạn này.
- ✅ Đồ nghề chốt (DEC-INST-001): 2C23T + DMM phụ + load cell 5 kg (HX711 P0); trần E2E <10M sổ tay-only (DEC-BUDGET-002).
- ✅ Ẩn danh KTV toàn bộ (DEC-ROLE-001); sửa cite epi/Cochrane/IROS/Gloreha (M-22..M-24).
- ✅ Viết lại A1/A2/A3/A4/A6 cho khớp.

**Còn chờ (không đo cho tới khi xong các mục 🔴):**
- [ ] 🔴 Viết công thức EI tường minh (M-25) + chốt 9 ngưỡng `protocols/08` §7.
- [ ] 🔴 Đo R(F) thật → trả lời M-01/M-17 (Vex, G, S, SNR).
- [ ] Ghi rõ người đeo + an toàn (M-26); lấy 5 số INT8 của owner (M-08).
- [ ] Shopping P0: HX711, ADS1115/INA333 chính hãng, SHT30, cân/quả cân, thước đo góc, ẩm-nhiệt kế.
- [ ] Xác minh nốt các cite 🔵 (OTHER, Hopkins, [18], RehabReach, Jamar/E-Link).
- [ ] Viết lại A7/GLOSSARY nếu còn dùng.
