# THIẾT KẾ VELOSTAT DRAPE — Sensor tuân theo hình cell

> **Tài liệu kỹ thuật bổ sung** — giải quyết vấn đề: Velostat phải ở trên cùng (gần da) **VÀ** tuân theo hình dạng khi cell inflate.

---

## 1. Vấn đề

**Yêu cầu:** Velostat (pressure sensor) phải tiếp xúc gần nhất với da bệnh nhân để có độ chính xác cao nhất.

**Thách thức:** Khi silicone cell inflate (z=0 → z=22 mm), hình dạng thay đổi. Nếu Velostat là **1 tấm phẳng cố định**, sẽ:
- Bị tension → hỏng sensor
- Hoặc bị nâng lên đều → không tuân theo hình

**Yêu cầu phụ:** Dễ thêm node/sensor sau này → không gắn cứng vào 1 board lớn.

---

## 2. Giải pháp: Per-cell Velostat patch với DRAPE

### 2.1 Nguyên lý

Thay vì 1 tấm Velostat lớn (800×1000 mm), dùng **64 patches RIÊNG** (50×50 mm), mỗi cái:
- Đặt giữa cell tương ứng
- Gắn **LỎNG** ở 4 góc (chỉ 4 điểm cố định)
- Mép patch được tự do drape xuống khi cell inflate

### 2.2 Cơ chế DRAPE

Khi silicone cell inflate:
- **4 góc** patch (gắn cố định) → cao thấp theo baseplate
- **Tâm patch** → tự do rơi theo hình dạng cell

Kết quả: patch tạo hình **paraboloid** (cao ở giữa, thấp ở mép), tuân theo hình silicone membrane.

### 2.3 Kích thước

| Thông số | Giá trị | Ghi chú |
|----------|---------|---------|
| Cell | 100 × 100 mm | Cố định |
| Velostat patch | 50 × 50 mm | Nhỏ hơn cell → có drape gap |
| Drape gap (khi inflate) | ~22 mm | Độ cao tối đa |
| Gap giữa patches | 50 mm | Đủ rộng cho wires |

### 2.4 So sánh với thiết kế cũ

| | Thiết kế cũ | Thiết kế mới |
|--|-------------|--------------|
| Velostat sheet | 1 tấm lớn 800×1000 | 64 patches 50×50 |
| Tuân theo hình | ❌ Không | ✅ Có (drape paraboloid) |
| Thêm node | ❌ Khó (cần thay tấm) | ✅ Dễ (thêm 1 patch) |
| Khoảng cách đến da | ~22 mm | ~1-2 mm |
| Độ chính xác | Trung bình | Cao |

---

## 3. Wire routing (64 wires)

### 3.1 Vấn đề

64 patches × 2 wires = 128 wires. Cần routing gọn gàng về STM32.

### 3.2 Giải pháp: Wire channels giữa các cells

- **Gap giữa 2 cells liền kề:** ~2 mm (do Velostat patch chỉ 50mm trong cell 100mm)
- **Mỗi patch** có wires chạy ra mép → vào **channel gap** → chạy dọc theo chiều cushion
- **Tất cả 64 wires** gom về **1 đầu nối** → SPI MUX → STM32

### 3.3 Routing topology

```
[Patches] → [Gap channels] → [Edge connector] → [STM32]
                                 ↑
                          (SPI MUX 74HC4051)
```

### 3.4 Lợi ích

- **Dễ thay thế** 1 patch hỏng (không cần tháo cả tấm)
- **Dễ thêm** node cảm biến mới (ví dụ: thêm cảm biến nhiệt độ trên 1 patch)
- **Không gãy wire** do cell inflate (wire có độ dự trữ)
- **Test riêng từng cell** dễ dàng

---

## 4. Ưu/nhược điểm so với thiết kế cũ

| Ưu điểm | Nhược điểm |
|---------|-----------|
| ✅ Chính xác hơn (gần da 1-2mm) | ❌ Phức tạp hơn (64 patches vs 1 sheet) |
| ✅ Tuân theo hình cell | ❌ Tốn công lắp 64 patches |
| ✅ Dễ thêm/thay sensor | ❌ Cần 128 wires thay vì ~10 wires |
| ✅ Test riêng từng cell | ❌ Routing wires phức tạp hơn |
| ✅ Không hỏng do tension | |

---

## 5. Thiết kế cơ khí

### 5.1 Per-cell assembly

Mỗi cell (100×100 mm) gồm:

```
┌─────────────────────────────────────┐  z = base + 22 + 1 = 31 mm
│  ████ Velostat patch (50×50mm) ████ │  ← LOOSE, 4 corners fixed
│  ██       (DRAPED shape)        ██  │     paraboloid: high center
│  ████                          ████  │
└─────────────────────────────────────┘  z = base + 22 = 30 mm
┌─────────────────────────────────────┐  ← Silicone membrane (inflated)
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │     1.5mm thick
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │     air chamber
└─────────────────────────────────────┘  z = base + 0 = 8 mm
┌─────────────────────────────────────┐  ← PETG base plate
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │     tube hole + 4 wire holes
└─────────────────────────────────────┘  z = 0
```

### 5.2 Stack tổng thể

```
Frame (z=0-20)
Valve brackets + Valves (z=8-23)
Tubes (z=24-40) đi qua baseplate
Baseplate (z=32-40)
Silicone cells (z=40-62)
Velostat patches DRAPED (z=62-84)
Patient (z=63+)
```

### 5.3 BOM bổ sung

| Hạng mục | Số lượng | Chi phí |
|----------|---------|---------|
| Velostat patches (50×50mm) | 64 | ~$15 (cắt từ 1 tấm lớn) |
| Wires (32 AWG) | 128 wires × 200mm | ~$5 |
| Wire connectors | 64 + 1 | ~$10 |
| Flexible epoxy (gắn patch) | 1 | ~$3 |
| **Tổng thêm** | | **~$33** |

---

## 6. Cách lắp ráp

### 6.1 Chuẩn bị patches

1. Cắt Velostat sheet (1000×1000 mm) thành 64 patches 50×50 mm (cắt thủ công bằng dao rọc giấy chính xác).
2. Mỗi patch hàn 2 wires (V_out, GND) — wires dài ~200 mm, đầu kia connector.

### 6.2 Gắn patches lên cells

1. Đặt baseplate lên khung.
2. Lắp 64 silicone cells (đã đúc từ khuôn single_cell.scad).
3. **Quan trọng:** Gắn Velostat patch **sau khi** cell đã dán lên baseplate.
4. Mỗi patch gắn **4 góc** bằng **1 giọt epoxy** nhỏ (~2mm²) — chỉ 4 chấm nhỏ, không phải toàn bộ patch.
5. **KHÔNG** dán ở giữa patch → phải để trống để drape.

### 6.3 Routing wires

1. Wires từ 4 góc patches → đi vào gap channel (giữa 2 cells).
2. Gom wires theo hàng/cột → chạy về 1 cạnh cushion.
3. Dùng **flexible PCB** hoặc **connector ribbon** để gom.
4. Connector cuối → SPI MUX 74HC4051 × 8 → STM32.

### 6.4 Test

1. **Test áp suất:** bơm cell → đo voltage Velostat → so sánh với reference.
2. **Test DRAPE:** quan sát bằng mắt — patch có tuân theo hình cell không?
3. **Test wire:** kiểm tra continuity từ patch → connector → STM32.

---

## 7. Hình minh họa

Xem các file:
- **`cad/drawings/velostat_drape_cross_section.png`** — 3 mức inflate (xẹp/nửa/max)
- **`cad/drawings/full_assembly_with_drape_3d.png`** — full 3D với patches drape
- **`cad/drawings/velostat_wire_routing.png`** — routing 64 wires
- **`cad/drawings/top_view_with_velostat_patches.png`** — top view 64 patches

---

## 8. So sánh với thiết kế thương mại

| | Đề tài này | Đệm alternating (Hillrom) | Smart cushion (Stryker) |
|--|-------------|---------------------------|------------------------|
| Pressure sensor | ✅ 64 Velostat patches (per-cell) | ❌ Không có | ✅ 1 tấm sensor lớn |
| Tuân theo hình | ✅ Drape design | n/a | ❌ Fixed shape |
| Accuracy | ✅ Cao (gần da, drape) | Thấp | Trung bình |
| Thêm sensor | ✅ Dễ (per-cell) | ❌ | ❌ Khó |
| Cost | ~$1,100 | ~$3,000 | ~$15,000 |

→ Đề tài này có **2 ưu điểm vượt trội**: per-cell sensor + drape design.

---

## 9. Rủi ro & giảm thiểu

| Rủi ro | Giảm thiểu |
|--------|-----------|
| Patch tuột khỏi 4 góc (cell inflate nhiều) | Dùng epoxy dẻo (flexible); chỉ gắn 4 chấm nhỏ |
| Wire gãy do inflate nhiều lần | Để dư 30% chiều dài wire |
| Drape gap quá rộng (>22mm) → patch chạm đáy | Giới hạn inflate_max = 22 mm (firmware) |
| Velostat mỏng (0.3mm) → dễ rách | Lamination thêm 1 lớp silicone mỏng (0.05mm) bảo vệ |

---

*Tài liệu kỹ thuật bổ sung — phiên bản 1.0.*
