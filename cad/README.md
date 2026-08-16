# CAD Files — 3D Printable Parts

> Các file OpenSCAD cho các chi tiết in 3D của đệm khí.

## File overview

| File | Part | Material | Print time | Qty |
|------|------|----------|-----------|-----|
| `single_cell.scad` | Silicone membrane mold (per cell) | PETG | ~30 min | 64 |
| `baseplate.scad` | Base plate 8×8 (chia 4 quadrant để in) | PETG | ~30 h total | 1 set |
| `manifold.scad` | Pneumatic manifold block | PETG or Al CNC | ~6 h | 1 |
| `valve_bracket.scad` | Mount solenoid valve | PETG | ~3 min | 64 |

## Cách sử dụng

### Cài OpenSCAD
```bash
# Linux (Debian/Ubuntu)
sudo apt install openscad

# macOS
brew install openscad

# Windows
# Download từ https://openscad.org
```

### Render STL để in 3D

**Base plate** (chia thành 4 quadrant):
```bash
openscad -D '$fn=32' -o baseplate_q1.stl cad/baseplate.scad
# Mở file .scad, uncomment `baseplate_quadrant(0, 0);` rồi render
```

**Single cell mold**:
```bash
openscad -o single_cell.stl cad/single_cell.scad
```

**Manifold**:
```bash
openscad -o manifold.stl cad/manifold.scad
```

**Valve bracket**:
```bash
openscad -o valve_bracket.stl cad/valve_bracket.scad
```

### Print settings
- **Material:** PETG (chống ẩm, dễ in, an toàn thực phẩm)
- **Layer height:** 0.2 mm (draft) hoặc 0.15 mm (chi tiết)
- **Infill:** 30% (brackets), 50% (base plate)
- **Walls:** 3-4 perimeters
- **Top/bottom layers:** 5
- **Support:** Yes cho manifold + baseplate
- **Bed temp:** 80°C (PETG), 60°C (PLA)
- **Hotend:** 230°C (PETG), 210°C (PLA)

## CAD Drawings (SVG + PNG)

Render từ `drawings.py`:
```bash
python cad/drawings.py
```

Output trong `cad/drawings/`:
- `cushion_top_view_8x8.svg` — Top view 8×8 (1000×800 mm)
- `cushion_cell_cross_section.svg` — Cross-section 1 cell
- `cushion_manifold.svg` — Manifold block layout
- `cushion_pneumatic_circuit.svg` — ISO 1219 pneumatic circuit
- `cushion_exploded_assembly.svg` — Exploded view
- `cushion_pressure_response.svg` — Pressure time-response
- `cushion_force_balance.svg` — Body weight distribution (70 kg)

## Kích thước tổng hợp

| Lớp | Độ dày | Ghi chú |
|-----|--------|---------|
| Anti-shear fabric | 1 mm | Tiếp xúc bệnh nhân |
| Velostat sheet | 0.3 mm | Cảm biến áp suất |
| Silicone membrane | 1.5 mm | Ô khí inflate |
| PETG base plate | 8 mm | Mang valve + manifold |
| Foam support | 50 mm | Passive safety |
| **Tổng** | **~63 mm** | |

## Test in 3D

Khi có máy in 3D, in thử nghiệm theo thứ tự:
1. **Valve bracket** (1 cái, ~3 min) — kiểm tra kích thước có khớp valve.
2. **Single cell mold** (1 cái, ~30 min) — kiểm tra silicone membrane có seal đúng.
3. **Manifold** (1 cái, ~6 h) — kiểm tra áp suất có đều giữa 64 cổng.
4. **Base plate quadrant** (1 quadrant, ~8 h) — lắp 16 valve, kiểm tra tube routing.

## Lưu ý an toàn

- PETG/PLA dùng cho prototype research — KHÔNG dùng trên bệnh nhân thật mà không qua FDA/CE approval.
- Silicone membrane phải là FDA-grade (chịu nhiệt, không độc).
- Test rò rỉ 100% trước khi dùng với mannequin/volunteer.
