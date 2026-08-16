# HARDWARE DESIGN — Thiết kế phần cứng (ARS Stage 2)
## Hệ thống đệm khí thích ứng tích hợp AAC

> Ngày: 2026-06-14

---

## 1. Bo mạch vi điều khiển STM32

### 1.1 Vi điều khiển chính
- **IC:** STM32F407VGT6
- **Tốc độ:** 168 MHz
- **Flash:** 1 MB; **RAM:** 192 KB
- **GPIO:** 100 chân; **ADC:** 3× 12-bit (24 kênh)
- **SPI:** 3 (dùng cho sensor MUX)
- **UART:** 6 (dùng 1 cho ROS2)
- **Timer PWM:** 12 (8 cho valve, 4 cho arm mini)
- **Watchdog:** Independent + Window

### 1.2 Sơ đồ nguyên lý (xem `diagrams/02_hardware_schematic.png`)
- Nguồn 24V → buck 5V → LDO 3.3V
- Sensor matrix → SPI MUX (74HC4051 × 8) → STM32 SPI2
- ADC backup cho piezocapacitive (12 kênh)
- Valve driver: ULN2803 + 12V solenoid
- CAN/Ethernet cho ROS2 bridge
- Status LED + emergency stop button

### 1.3 Pinout (tóm tắt)
```
PA0..PA7  →  SPI MUX select
PB0..PB9  →  PWM valve (8 cell group × 2 phase)
PC0..PC11 →  ADC (piezocapacitive backup)
PD0,PD1   →  UART → ROS2
PE0       →  Emergency stop
PE1       →  Watchdog reset
PF0..PF15 →  Status LED + keypad
```

---

## 2. Ma trận cảm biến áp suất lai 8×8

### 2.1 Velostat sheet
- Lớp phủ rộng, phủ kín 64 ô.
- Đọc qua ADC đa kênh (1 ô = 1 điện trở tỷ lệ nghịch áp lực).
- V_out = V_ref × R_fix / (R_velostat + R_fix)

### 2.2 Piezocapacitive nodes
- 8 node đặt tại các vị trí "anchor" (sacrum, heels, trochanter, scapula).
- Đọc qua dedicated ADC, I2C backup.

### 2.3 Cross-calibration (xem code `src/pressure_model/cross_calibration.py`)
- V_t = f(P_t | θ_velostat)  // Velostat raw
- P_t = f(V_t | θ_pz)        // Calibrate using piezocap. anchor
- Online update mỗi 5 phút (Kalman-filter style).

### 2.4 PCB layout (xem `diagrams/02b_sensor_pcb.png`)
- Sensor rows: 8 đường dọc cách nhau 5 cm.
- Sensor cols: 8 đường ngang cách nhau 5 cm.
- Piezocap. đặt tại giao điểm hàng 3-6, cột 3-6.

---

## 3. Hệ thống khí nén

### 3.1 Specifications
- **Pump:** 24V DC diaphragm, 6 L/min.
- **Reservoir:** 2 L (buffer).
- **Valves:** 64× 12V solenoid NO/NC, orifice 1.5 mm.
- **Pressure sensor:** 1× board-level 0–100 mmHg (cho closed-loop).
- **Air cells:** 64 ô silicone, 5×5×3 cm, lỗ thở nhỏ 0.5 mm.

### 3.2 Topology
```
Pump ──► Reservoir ──► Manifold (64) ──► Air cells
                              ▲
                              └── Pressure sensor
```
- Mỗi ô có 1 valve intake + 1 valve exhaust.
- PID local cho mỗi ô.

### 3.3 Control loop (per cell)
```
setpoint_p(i,t)  ──►  PID_i  ──►  PWM duty ──►  Valve
                                              ▲
                                              └── Pressure sensor
```
- Update rate: 10 Hz.
- Anti-windup: clamping + back-calculation.

---

## 4. Camera rig + Robot arm

### 4.1 Cameras
- 2× **OV9281** global shutter, 640×480 @ 60 fps.
- Lens: M12 mount, focal 3.6 mm.
- IR LED ring 850 nm cho điều kiện ánh sáng yếu.

### 4.2 Stereo geometry
- Baseline: 60 mm (đã calibrate).
- Depth: 30–80 cm từ mặt giường.

### 4.3 Robot arm
- 3 DOF (pan ±30°, tilt ±20°, roll ±10°).
- Driver: 3× servo (Dynamixel XL-330).
- Controller: STM32 mini (STM32G0) bridge tới Jetson qua UART.

### 4.4 Kinetics (xem `src/eye_tracking/camera_positioner.py`)
- IK đơn giản: 3 góc độc lập, không có ràng buộc chéo.
- Update rate: 10 Hz.

---

## 5. Nguồn & an toàn

### 5.1 Power
- Adapter 24V / 5A (Mean Well GST60E24).
- Buck 5V cho Jetson, LDO 3.3V cho STM32.
- UPS backup 12V/7Ah cho 30 phút an toàn.

### 5.2 Safety
- Emergency stop button → cắt 24V → tất cả valve xả.
- Watchdog STM32 → auto-deflate nếu Jetson mất kết nối > 5s.
- Pressure limit (firmware): mỗi ô < 80 mmHg.
- Thermal cutoff pump ở 60°C.
- Cách điện y tế IEC 60601-1 (mục tiêu).

---

## 6. Bo mạch AI Edge (Jetson Orin Nano)

### 6.1 Module
- Jetson Orin Nano 8 GB (40 TOPS).
- JetPack 5.1.3, Ubuntu 20.04.
- Carrier board: NVIDIA dev kit hoặc custom.

### 6.2 Interfaces
- 2× MIPI CSI-2 → cameras.
- USB 3.0 → STM32 (ROS2 over serial).
- HDMI → 10" touchscreen.
- GPIO → audio codec + LED.
- WiFi (optional, off by default).

### 6.3 Thermal
- Heatsink + fan (5V).
- Tj max 85°C; giám sát qua `/sys/thermal`.

---

## 7. Bo mạch hiển thị (UI / AAC)

### 7.1 Display
- 10" capacitive touchscreen 1280×800.
- Hiển thị: pressure map + AAC grid + status.

### 7.2 Layout (xem `diagrams/08_aac_ui_mockup.png`)
- Trên: pressure map heatmap + risk overlay.
- Dưới: AAC grid 5×3 (15 ô lớn, hover bằng gaze).

---

## 8. Bill of Materials (BOM)

| Item | Qty | Đơn giá (USD) | Tổng |
|------|-----|--------------|------|
| STM32F407VGT6 | 1 | 12 | 12 |
| Jetson Orin Nano 8GB | 1 | 250 | 250 |
| Velostat sheet (A4) | 4 | 8 | 32 |
| Piezocapacitive sensor | 8 | 6 | 48 |
| Solenoid valve 12V | 64 | 2.5 | 160 |
| Diaphragm pump | 1 | 25 | 25 |
| Camera OV9281 | 2 | 22 | 44 |
| Dynamixel XL-330 | 3 | 35 | 105 |
| Touchscreen 10" | 1 | 110 | 110 |
| Power supply | 1 | 30 | 30 |
| PCB + dây + connector | lot | 80 | 80 |
| Air cell silicone | 64 | 1 | 64 |
| Misc (LED, button, fuse) | lot | 30 | 30 |
| **Tổng ước tính** | | | **~990 USD** |

---

## 9. Mechanical (CAD)
- Frame giường: nhôm 20×20 V-slot, 200×100 cm.
- Cushion base: foam 5 cm + air cell layer 3 cm.
- Camera mount: bracket in nhựa PETG, in 3D.
- Wire routing: cable tray ở chân giường.
