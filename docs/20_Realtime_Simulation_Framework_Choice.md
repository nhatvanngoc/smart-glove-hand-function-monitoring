# Chon framework mo phong realtime cho Velostat + copper tape + heatmap

Ngay cap nhat: 2026-07-27

## Ket luan

Khong nen ep Gazebo/URDF de mo phong Velostat + copper tape. Gazebo manh ve robot rigid-body, joint, contact co ban, nhung khong phu hop de mo phong:

- Velostat la vat lieu dien tro phu thuoc ap luc;
- copper tape la dien cuc mem/det;
- tui silicone khi bien dang;
- ban do nhiet ap suat theo thoi gian.

Voi de tai hien tai, nen tach thanh 2 lop:

```text
Lop 1 - sensor/control realtime:
Python/NumPy/PyQtGraph/Matplotlib -> ADC -> pressure -> heatmap

Lop 2 - co hoc mem neu can nang cao:
SOFA Framework hoac Taichi mass-spring/FEM nhe
```

## Framework nen dung theo muc do

| Muc tieu | Framework khuyen nghi | Nhan xet |
|---|---|---|
| Demo realtime heatmap, thuat toan, ADC | Python + NumPy + Matplotlib/PyQtGraph | Nen dung ngay, de debug, gan voi phan cung that |
| App realtime dep hon | PyQtGraph / DearPyGUI / Plotly Dash | Tot cho dashboard live |
| Mo phong bien dang mem 2D/2.5D | Taichi | Nhanh, GPU, co the tu viet mang mem/tui khi |
| Mo phong y-sinh/vat lieu mem nghiem tuc | SOFA Framework | Phu hop soft-body/FEM, nhung hoc kho hon Python thuong |
| Robot rigid-body / van / frame | Gazebo / Webots / PyBullet | Chi nen dung de minh hoa co cau cung, khong nen dung cho Velostat |
| Visual dep | Blender | Tot de render/thuyet trinh, khong phai realtime sensor physics |
| High-fidelity offline | COMSOL / ANSYS / Abaqus / FEBio | Tot de nghien cuu vat lieu, khong phai demo realtime nhanh |

## Huong chon cho du an nay

### Giai doan hien tai

Dung Python realtime heatmap:

```text
simulation/realtime_velostat_heatmap.py
```

Chay:

```bash
python simulation/realtime_velostat_heatmap.py
```

Chuc nang:

- Mo phong 45 sensor Velostat cua ma tran 5 x 9.
- Mo phong ap luc nguoi nam ngua/nam nghieng.
- Mo phong Velostat R(P).
- Mo phong mach chia ap va ADC 12-bit.
- Tai tao pressure map.
- Ve heatmap realtime.
- Ve risk mask theo nguong mmHg.
- Co san mode doc serial 45 gia tri ADC tu STM32/Arduino sau nay.

### Neu muon doc phan cung that

STM32/Arduino gui moi frame 45 gia tri ADC:

```text
315,320,318,... tong 45 gia tri
```

Chay:

```bash
python simulation/realtime_velostat_heatmap.py --serial COM5 --baud 115200
```

### Neu muon mo phong co hoc mem

Dung SOFA hoac Taichi, nhung chi nen lam sau khi da co heatmap realtime chay on.

## Vi sao khong can Gazebo luc nay

Gazebo yeu cau URDF/SDF va robot link/joint. Trong khi bai toan nay chu yeu la:

```text
ap luc -> dien tro -> ADC -> heatmap -> thuat toan dieu khien
```

Gazebo khong biet Velostat co duong dac tinh dien tro theo ap luc neu ta khong viet plugin rieng. Neu viet plugin thi cong suc lon nhung gia tri thuc te khong cao bang viec dung Python sensor simulation.

## Neu van can mo phong CAD/co khi

De trinh bay co khi:

- Dung OpenSCAD de tao cell/baseplate/assembly.
- Dung Blender de render dep neu can.
- Dung Gazebo/Webots chi de minh hoa frame/valve/ong khi neu that su can.

De trinh bay sensor:

- Dung Python heatmap realtime.
- Dung du lieu ADC that khi co prototype.

## Roadmap khuyen nghi

1. Chay realtime simulator Python.
2. Lam 1 sensor Velostat + copper tape that.
3. Gui ADC cua 1 sensor vao Python.
4. Mo rong len 5 sensor mot hang.
5. Mo rong len 45 sensor qua 3 module CD74HC4067.
6. Hieu chuan ADC -> mmHg.
7. Neu can nang cao, moi them SOFA/Taichi de mo phong bien dang mem.

Day la huong thuc te nhat va it bi ket hon Gazebo/URDF.
