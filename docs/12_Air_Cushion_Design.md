# THIẾT KẾ CHI TIẾT ĐỆM KHÍ 64 Ô
## Cốt lõi kỹ thuật của hệ thống Adaptive Air Cushion

> **Tài liệu thiết kế cơ khí + cơ học chất lưu**
> Phiên bản: 1.0 — 2026-06-14
> Học sinh: Văn Ngọc Nhật Anh — THPT Quảng Trị

---

## 1. TỔNG QUAN HỆ THỐNG ĐỆM KHÍ

### 1.1 Chức năng
Đệm khí 64 ô điều khiển độc lập, tích hợp:
- **Ma trận cảm biến áp suất lai** 8×8 (Velostat phủ + 8 piezocapacitive anchors).
- **64 van solenoid** điều khiển áp suất từng ô.
- **1 bơm diaphragm** + reservoir cung cấp khí nén.
- **1 manifold** phân phối khí đến 64 ô.
- **Lớp foam** hỗ trợ tĩnh khi mất điện (passive safety).

### 1.2 Thông số kỹ thuật tổng quan
| Thông số | Giá trị |
|----------|---------|
| Kích thước tổng | 1000 × 800 × 80 mm |
| Số ô khí | 64 (8 × 8) |
| Kích thước mỗi ô | 100 × 100 × 30 mm |
| Áp suất vận hành | 0–80 mmHg (~0–10.7 kPa) |
| Áp suất tối đa an toàn | 120 mmHg (~16 kPa) |
| Đáp ứng (rise time) | < 2 s/ô (đạt 0.6 s) |
| Tổng lưu lượng khí | 6 L/min |
| Công suất bơm | 24V DC, 5W |
| Trọng lượng | ~3.5 kg |

---

## 2. THIẾT KẾ TỪNG Ô KHÍ (SINGLE CELL)

### 2.1 Hình học ô khí

```
┌─────────────────────────┐  ← Mặt trên (tiếp xúc bệnh nhân)
│   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   │
│   ▓▓ (Velostat) ▓▓▓    │  ← Lớp 1: Velostat sheet
│   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   │
├─────────────────────────┤
│ ░░░░░░░░░░░░░░░░░░░░░ │  ← Lớp 2: Silicone membrane (inflatable)
│ ░░░ air chamber ░░░░░░ │
│ ░░░░░░░░░░░░░░░░░░░░░ │
├─────────────────────────┤
│ ███████████████████████ │  ← Lớp 3: Base plate (PLA/PETG)
│ ████ valve mount ██████ │
│ ███████████████████████ │
└─────────────────────────┘
```

**Cấu tạo 3 lớp (top → bottom):**
1. **Lớp cảm biến (Velostat)** — dày 0.3 mm, phủ toàn bộ mặt trên.
2. **Lớp silicone inflatable** — dày 1.5 mm, chứa khí, có lỗ thoát nhỏ (0.5 mm) để trao đổi áp suất chậm.
3. **Lớp đế (Base plate)** — dày 8 mm, in 3D PETG, gắn valve.

### 2.2 Thông số hình học
| Thông số | Giá trị | Ghi chú |
|----------|---------|---------|
| Chiều dài ô | 100 mm | |
| Chiều rộng ô | 100 mm | |
| Chiều cao ô (collapsed) | 8 mm | khi xả hết khí |
| Chiều cao ô (inflated) | 30 mm | khi áp suất đạt max |
| Thể tích ô (max) | 100 × 100 × 30 = 300 cm³ | |
| Thể tích khí điều khiển | ~200 cm³ | dải làm việc 0–80 mmHg |
| Diện tích bề mặt | 100 cm² | 0.01 m² |
| Lực nâng tối đa | 0.01 m² × 80 mmHg × 133.32 Pa/mmHg ≈ 107 N | đủ nâng ~10 kg |

### 2.3 Tính toán cơ học

#### Lực nâng (lift force)
$$F_{lift} = P \cdot A = P \cdot 0.01 \text{ m}^2$$

- Tại P = 32 mmHg (4.27 kPa): F = 42.7 N (~4.3 kg)
- Tại P = 80 mmHg (10.7 kPa): F = 107 N (~10.9 kg)

→ Mỗi ô đủ nâng 4–10 kg, đáp ứng yêu cầu phân tán tải cơ thể người.

#### Độ cứng silicone
Silicone membrane dày 1.5 mm:
- Độ đàn hồi E_silicone ≈ 5 MPa
- Tại áp suất 80 mmHg, biến dạng < 5% — an toàn.

#### Đáp ứng (response time)
Thời gian đạt áp suất target:
$$t_{response} = \frac{V \cdot \Delta P}{Q \cdot P_{atm}}$$

Trong đó:
- V = 200 cm³ (thể tích ô)
- ΔP = 80 mmHg = 10.7 kPa
- Q = 6 L/min = 100 cm³/s (lưu lượng bơm chia cho 64 ô)
- P_atm = 101.3 kPa

→ t ≈ (200 × 10.7) / (100 × 101.3) ≈ 0.21 s (cho 1 ô)

Với valve orifice 1.5 mm và chiều dài tube 200 mm:
- Lưu lượng thực ~60 cm³/s/ô → t ≈ 0.36 s ✅ (đáp ứng target < 2 s)

**Mô phỏng thực tế:** rise time = 0.600 s (đạt target).

---

## 3. SƠ ĐỒ BỐ TRÍ 64 Ô (LAYOUT)

### 3.1 Ma trận 8×8
```
       Col 0  Col 1  Col 2  Col 3  Col 4  Col 5  Col 6  Col 7
Row 0  ┌────┬────┬────┬────┬────┬────┬────┬────┐
       │ 0  │ 1  │ 2  │ 3  │ 4  │ 5  │ 6  │ 7  │  ← đầu
       ├────┼────┼────┼────┼────┼────┼────┼────┤
Row 1  │ 8  │ 9  │10  │11  │12  │13  │14  │15  │  ← vai
       ├────┼────┼────┼────┼────┼────┼────┼────┤
Row 2  │16  │17  │18  │19  │20  │21  │22  │23  │  ← lưng trên
       ├────┼────┼────┼────┼────┼────┼────┼────┤
Row 3  │24  │25  │26  │27♠│28♠│29♠│30  │31  │  ← SACRUM zone
       ├────┼────┼────┼────┼────┼────┼────┼────┤     (♠ = piezocap.)
Row 4  │32  │33  │34  │35♠│36♠│37♠│38  │39  │  ← SACRUM zone
       ├────┼────┼────┼────┼────┼────┼────┼────┤
Row 5  │40  │41  │42  │43♠│44♠│45♠│46  │47  │  ← mông
       ├────┼────┼────┼────┼────┼────┼────┼────┤
Row 6  │48  │49  │50  │51  │52  │53  │54  │55  │  ← đùi
       ├────┼────┼────┼────┼────┼────┼────┼────┤
Row 7  │56  │57  │58  │59  │60  │61  │62  │63  │  ← gót chân
       └────┴────┴────┴────┴────┴────┴────┴────┘
```

### 3.2 Vùng chức năng (per posture)
| Vùng | Ô (index) | Threshold (mmHg) | Posture priority |
|------|----------|-----------------|------------------|
| **Sacrum** | 27, 28, 29, 35, 36, 37, 43, 44, 45 | 32 (lowest) | Supine |
| **Heels** | 56–63 | 30 | All |
| **Trochanter** | 25, 26, 33, 34 | 30 | Lateral |
| **Scapula** | 0–7 | 32 | Prone |
| **Knees** | 48–55 | 32 | Prone |
| **Other** | còn lại | 40 | Default |

### 3.3 Piezocapacitive anchor positions
- 8 anchors đặt tại: `[(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,5)]`
  - Đây là vùng **sacrum**, nơi nguy cơ cao nhất.
- Mỗi anchor cảm biến trực tiếp áp suất thực tại vùng này.
- Velostat 64 ô phủ toàn bộ, được hiệu chuẩn bằng 8 anchors này.

---

## 4. HỆ THỐNG KHÍ NÉN (PNEUMATIC CIRCUIT)

### 4.1 Sơ đồ nguyên lý
```
                     ┌──── Pressure sensor (0–100 mmHg)
                     │
                     ▼
┌────────┐     ┌────────────┐     ┌─────────────────┐
│ Pump   │────►│ Reservoir  │────►│ Manifold 64-way  │──── 64 tubes ────┐
│ 24V DC │     │ 2 L buffer │     │ (manifold block) │                  │
│ 6 L/m  │     └────────────┘     └─────────────────┘                  │
└────────┘                                                           │
                                                                     ▼
                                              ┌──── Valve (×64) ──── Air cell (×64)
                                              │      (12V NO)            │
                                              │                          │
                                              └── Pressure sensor (×1 per cell, optional)
```

### 4.2 Thông số chi tiết

#### 4.2.1 Bơm (Pump)
- **Model:** KNF NMP 30 (diaphragm) hoặc tương đương
- **Lưu lượng:** 6 L/min @ 0 bar
- **Áp suất max:** 0.5 bar (~375 mmHg) — đủ cho cushion
- **Điện áp:** 24V DC
- **Công suất:** 5W
- **Tuổi thọ:** 5,000 giờ (continuous) ≈ 200 ngày
- **Noise:** < 35 dB

#### 4.2.2 Reservoir
- **Thể tích:** 2 L
- **Vật liệu:** Nhựa PC (polycarbonate) trong suốt
- **Áp suất làm việc:** 0–0.5 bar
- **Van an toàn:** xả khi > 0.6 bar
- **Cảm biến áp suất:** 1× board-level 0–100 mmHg (MPX5700)

#### 4.2.3 Manifold (manifold block)
- **Kích thước:** 200 × 100 × 30 mm
- **Vật liệu:** PETG in 3D hoặc nhôm CNC
- **64 cổng ra:** ống silicone 4 mm ID, 6 mm OD
- **1 cổng vào:** ống silicone 8 mm ID
- **Lưu lượng mỗi cổng:** 100 cm³/s @ 0.1 bar
- **Áp suất drop across manifold:** < 5 mmHg (at 6 L/min)

#### 4.2.4 Valve (×64)
- **Model:** SMC VDW31 (12V DC, NO, 1.5 mm orifice)
- **Điện áp:** 12V DC
- **Dòng:** 100 mA
- **Response time:** < 10 ms
- **Orifice:** 1.5 mm
- **Cv:** 0.04 (lưu lượng hệ số)
- **Tuổi thọ:** 10 triệu chu kỳ

#### 4.2.5 Tube routing
- **Từ manifold → valve:** silicone 4×6 mm, dài 100 mm
- **Từ valve → cell:** silicone 4×6 mm, dài 150 mm
- **Cell inlet fitting:** push-in connector 4 mm
- **Tổng chiều dài tube:** ~16 m (64 × 250 mm)

### 4.3 Tính toán cơ học chất lưu

#### 4.3.1 Lưu lượng cần thiết
- Mỗi ô thể tích tối đa: 200 cm³ (khí điều khiển)
- Thời gian bơm đầy 1 ô: target 1 s
- → Lưu lượng cần: 200 cm³/s = 12 L/min (1 ô)

**Vì bơm 6 L/min phải chia cho nhiều ô:**
- Nếu chỉ 1 ô hoạt động → đủ
- Nếu 6 ô cùng lúc → 1 L/min/ô → t_response ≈ 12 s (chậm)
- **Giải pháp:** Reservoir đệm + valve logic — ưu tiên ô nguy cơ cao trước.

#### 4.3.2 Áp suất drop trong tube
Hagen-Poiseuille cho tube dài 250 mm, đường kính 4 mm:
$$\Delta P = \frac{128 \mu L Q}{\pi d^4}$$

Trong đó:
- μ (air viscosity) = 1.8×10⁻⁵ Pa·s
- L = 0.25 m
- Q = 100 cm³/s = 1×10⁻⁴ m³/s
- d = 0.004 m

→ ΔP ≈ 0.36 Pa = 0.003 mmHg → negligible ✅

#### 4.3.3 Thời gian đáp ứng tổng
- Valve switching: 10 ms
- Tube filling: 0.4 s (per cell)
- Cell membrane compliance: 0.5 s
- **Tổng: < 1 s** ✅ (target < 2 s)

---

## 5. CẢM BIẾN ÁP SUẤT (PRESSURE SENSOR LAYER)

### 5.1 Velostat sheet
- **Vật liệu:** Velostat (linqstat) — polymer dẫn điện có điện trở thay đổi theo áp lực
- **Kích thước:** 800 × 600 mm (phủ toàn bộ cushion)
- **Độ dày:** 0.3 mm
- **Dải áp suất:** 0–100 mmHg (tuyến tính ±15%)
- **Điện trở:** 1–100 kΩ (thay đổi theo áp lực)
- **Drift:** ~5 mmHg/giờ (cần cross-cal)

### 5.2 Mạch đọc Velostat
- **64 ô × 1 ADC channel** → Multiplexer 74HC4051 × 8 → STM32 SPI/ADC
- **Mạch cầu phân áp:**
  ```
  V_ref (3.3V) ──[R_fix 10kΩ]──┬──[Velostat]── GND
                                │
                                └──► ADC (12-bit)
  ```
- **Công thức:**
  $$V_{ADC} = V_{ref} \cdot \frac{R_{velostat}}{R_{fix} + R_{velostat}}$$
  $$P_{mmHg} = f(V_{ADC})$$ (qua cross-cal)

### 5.3 Piezocapacitive anchor (×8)
- **Model:** TE Connectivity FSR 402 hoặc Murata PS-A01
- **Vị trí:** 8 điểm sacrum (xem layout §3.3)
- **Đọc qua:** I2C ADC (ADS1115 × 1) → STM32
- **Drift:** < 0.5 mmHg/giờ (gấp 10× chính xác hơn Velostat)

### 5.4 Cross-calibration
Xem `src/pressure_model/cross_calibration.py`:
- Online Kalman filter cập nhật mỗi 5 phút.
- Velostat scale (a, b) được fit từ 8 anchor readings.
- Drift giảm từ ~5 mmHg/h xuống ~0.5 mmHg/h.

---

## 6. CẤU TRÚC CƠ KHÍ (MECHANICAL ASSEMBLY)

### 6.1 Cấu tạo các lớp (top → bottom)

```
┌──────────────────────────────────────┐  ← 1. Sensor mat (Velostat + wires)
├──────────────────────────────────────┤
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │  ← 2. Silicone membrane cells (×64)
│ ░░░░░░ 64 air cells ░░░░░░░░░░░░░░░ │
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
├──────────────────────────────────────┤
│ ████████████████████████████████████ │  ← 3. Base plate (PETG 8 mm)
│ ████ 64 valve mounts + manifold ████ │
│ ████████████████████████████████████ │
├──────────────────────────────────────┤
│ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ │  ← 4. Foam support layer (5 cm)
│ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ │     (passive safety khi mất điện)
├──────────────────────────────────────┤
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │  ← 5. Frame giường (optional)
└──────────────────────────────────────┘
```

### 6.2 Đế base plate (in 3D)
- **Kích thước:** 1000 × 800 × 8 mm
- **Vật liệu:** PETG (PET-G) hoặc ABS
- **Lỗ:** 64 × hole 4 mm (cho tube) + 8 × hole 6 mm (piezocap)
- **Mount points:** 4 × M4 corner + 12 × M3 mid
- **Channel routing:** rãnh 4 mm cho tube + dây (in ngầm)
- **Tổng trọng lượng:** ~800 g

### 6.3 Frame giường (frame integration)
- **Vật liệu:** Nhôm V-slot 20×20
- **Kích thước:** 2100 × 1000 mm (full giường)
- **Cushion location:** 1000 × 800 mm trung tâm
- **Wire routing:** cable tray ở chân giường

### 6.4 Các chi tiết in 3D khác
- **Valve bracket:** 64 × (mount valve lên base plate)
- **Sensor mat frame:** 1 × (giữ Velostat căng)
- **Manifold housing:** 1 × (chứa manifold + pressure sensor)
- **Pump bracket:** 1 × (gắn bơm vào frame)
- **UI mount:** 1 × (giá treo 10" touchscreen)
- **Camera arm bracket:** 1 × (gắn robot arm)

### 6.5 BOM cơ khí (Mechanical BOM)
| # | Item | Qty | Material | Spec | Cost (USD) |
|---|------|-----|----------|------|-----------|
| 1 | Silicone membrane sheet 1.5mm | 1 m² | Silicone FDA-grade | 1000×1000 mm | 35 |
| 2 | Velostat sheet | 1 m² | Linqstat | 1000×1000 mm | 25 |
| 3 | Base plate (in 3D) | 1 | PETG | 1000×800×8 mm | 50 (filament) |
| 4 | Foam support | 1 | PU foam | 1000×800×50 mm | 20 |
| 5 | Manifold block (in 3D) | 1 | PETG | 200×100×30 mm | 15 |
| 6 | Valve brackets (×64) | 64 | PETG | 30×20×15 mm | 30 (filament) |
| 7 | Push-in connectors 4mm | 70 | POM plastic | 4 mm ID | 35 |
| 8 | Silicone tube 4×6 mm | 20 m | Silicone | 4 mm ID | 25 |
| 9 | Silicone tube 8×10 mm | 2 m | Silicone | 8 mm ID (pump→reservoir) | 8 |
| 10 | Frame nhôm 20×20 | 10 m | Al 6063 | 20×20 mm V-slot | 80 |
| 11 | Fasteners (M3, M4) | 200 | Stainless | assorted | 20 |
| 12 | Cable ties + tray | lot | Nylon | assorted | 10 |
| **Tổng cơ khí** | | | | | **~353 USD** |

---

## 7. QUY TRÌNH CHẾ TẠO (MANUFACTURING PROCESS)

### 7.1 Chuẩn bị
1. **In 3D base plate + brackets** (PETG, infill 30%, layer 0.2 mm) — ~30 giờ in.
2. **Cắt silicone membrane** theo kích thước 64 ô (laser cutter hoặc dao CNC).
3. **Cắt Velostat sheet** theo kích thước 1000×1000 mm.
4. **Hàn dây Velostat** (64 wires → SPI MUX).

### 7.2 Lắp ráp (assembly sequence)
1. **Bước 1:** Gắn 64 valve brackets lên base plate (M3×8).
2. **Bước 2:** Lắp 64 solenoid valve vào brackets (push-fit).
3. **Bước 3:** Kết nối tube manifold → valve (push-in connector).
4. **Bước 4:** Kết nối valve → air cell inlet (push-in).
5. **Bước 5:** Dán silicone membrane lên base plate (silicone sealant FDA-grade).
6. **Bước 6:** Đặt Velostat sensor mat lên trên silicone (căng, không nhăn).
7. **Bước 7:** Kết nối 64 wire từ Velostat → SPI MUX → STM32.
8. **Bước 8:** Gắn 8 piezocapacitive anchor tại vùng sacrum.
9. **Bước 9:** Test áp suất (bơm 80 mmHg, check rò rỉ).

### 7.3 Test acceptance (per cell)
- [ ] Bơm đến 80 mmHg trong < 2 s.
- [ ] Giữ áp suất 30 phút → drop < 5 mmHg (no leak).
- [ ] Xả hết trong < 3 s.
- [ ] Đo áp suất bằng reference gauge → sai số < 5 mmHg.

### 7.4 Test tổng (system test)
- [ ] 64 ô bơm đồng thời → manifold giữ áp suất ổn định.
- [ ] 1 ô rò rỉ 1 mm/min → phát hiện qua pressure sensor.
- [ ] Mất điện → foam support đảm bảo bệnh nhân không chạm đáy cứng.

---

## 8. TIÊU CHUẨN AN TOÀN (SAFETY STANDARDS)

### 8.1 Cơ khí
- Không có cạnh sắc — tất cả góc R ≥ 2 mm.
- Không có chất liệu gây dị ứng — silicone FDA-grade, PETG biocompatible.
- Trọng lượng tối đa bệnh nhân: 150 kg (tương đương ~30 kg/ô).

### 8.2 Điện
- 24V DC isolation, không dùng AC trực tiếp trên giường.
- Watchdog + emergency stop (hardware).
- Fuse 5A ở nguồn chính.
- ESD protection cho STM32 + Jetson.

### 8.3 Khí nén
- Van an toàn ở reservoir (xả khi > 0.6 bar).
- Mỗi ô giới hạn 80 mmHg (firmware limit).
- Pump thermal cutoff 60°C.

### 8.4 Quy định
- Label "RESEARCH PROTOTYPE — NOT A MEDICAL DEVICE".
- Không dùng cho bệnh nhân thật mà không có IRB approval.
- Tuân thủ quy định về thiết bị y tế của Bộ Y tế Việt Nam.

---

## 9. BẢO TRÌ (MAINTENANCE)

### 9.1 Định kỳ
| Tần suất | Công việc |
|---------|-----------|
| Mỗi 30 phút (auto) | Re-cal Velostat từ 8 anchors |
| Mỗi 1 tuần | Test rò rỉ 64 ô |
| Mỗi 1 tháng | Thay filter bơm (nếu có) |
| Mỗi 3 tháng | Kiểm tra tuổi thọ valve (cycles) |
| Mỗi 6 tháng | Thay silicone tube (nếu vàng) |
| Mỗi 1 năm | Thay Velostat sheet (nếu drift > 10%) |

### 9.2 Troubleshooting
- **Ô không bơm được:** check valve (có thể kẹt), check tube (có thể gãy).
- **Pressure drift nhanh:** check Velostat (có thể rách), re-cal.
- **Pump yếu:** check filter (bẩn), check tube (rò rỉ).
- **Bệnh nhân nóng:** check airflow (có thể tắc nghẽn), thêm lỗ thoát.

---

## 10. MÔ PHỎNG (SIMULATION)

Xem `simulation/` directory:
- **`urdf/cushion_simple.urdf`** — Mô hình URDF cho RViz + Gazebo.
- **`sdf/cushion.sdf`** — Mô hình SDF cho Gazebo (với plugin dynamics).
- **`plugins/cushion_dynamics_simulator.py`** — Python dynamics simulator (first-order ODE).
- **`plugins/cushion_controller_node.py`** — ROS2 controller node.
- **`launch/cushion_test.launch.py`** — ROS2 launch file test.
- **`scenarios/test_supine.py`** — Test scenario mannequin supine.
- **`scenarios/test_lateral.py`** — Test scenario mannequin lateral.
- **`scenarios/test_pressure_response.py`** — Test step response 1 ô.

### 10.1 Kết quả mô phỏng
| Test | Acceptance | Achieved |
|------|-----------|----------|
| Step response rise time | < 2s | 0.6s ✅ |
| Step response fall time | < 3s | < 3s ✅ |
| Overshoot | < 10% | 0% ✅ |
| Supine sacrum | < 32 mmHg | 14.99 mmHg ✅ |
| Supine peak | < 80 mmHg | 27.95 mmHg ✅ |
| Supine TOT | < 10% | 0% ✅ |
| Lateral trochanter | < 32 mmHg | 13.21 mmHg ✅ |

→ **Tất cả 7/7 acceptance criteria PASS.**

### 10.2 Mục tiêu mô phỏng
- Verify pressure distribution khi mannequin nằm.
- Test PID control 64 ô đáp ứng < 2 s.
- Test cross-calibration trong mô phỏng.
- Risk-free testing trước khi build hardware thật.

---

## 11. PHỤ LỤC

### A. Bảng tính (calculation sheet)
Xem `docs/12_Air_Cushion_Design.md` §2.3, §4.3.

### B. CAD drawings
- **`cad/single_cell.scad`** — OpenSCAD single cell (parametric).
- **`cad/manifold.scad`** — Manifold block.
- **`cad/baseplate.scad`** — Base plate 1000×800×8 mm.
- **`cad/valve_bracket.scad`** — Valve bracket.
- **`cad/drawings/cushion_*.svg/png`** — 7 bản vẽ kỹ thuật.

### C. Reference
- Silicone membrane datasheet (FDA-grade).
- SMC VDW31 valve datasheet.
- KNF NMP 30 pump datasheet.
- Velostat/Linqstat pressure sensing — Adafruit tutorial.

---

*Tài liệu thiết kế phiên bản 1.0 — cập nhật khi có prototype v1 thực tế.*
