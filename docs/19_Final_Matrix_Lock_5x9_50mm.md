# Chot cau hinh ma tran dem khi va cam bien Velostat

Ngay cap nhat: 2026-07-27

## Cau hinh da chot

```text
Ma tran dem:       5 x 9
So cell:           45
Kich thuoc cell:   98 x 98 mm
Pitch lap rap:     100 mm
Kich thuoc module: xap xi 500 x 900 mm
Velostat patch:    50 x 50 mm moi cell
So tam Velostat:   6 tam 28 x 28 cm
```

## Y nghia hinh hoc

- 5 cell theo chieu ngang co the: trai -> phai.
- 9 cell theo chieu doc co the: vai -> lung -> mong/cung cut -> dui tren.
- Moi cell co mot patch Velostat rieng, dat gan tam cell.
- Khong trai Velostat thanh mot tam lon lien tuc vi se lam mo ban do ap luc va noi cau co hoc giua cac cell.

## Kich thuoc tong the

Voi cell 98 x 98 mm va khe lap rap 2 mm:

```text
Pitch = 98 + 2 = 100 mm
Ngang = 5 x 100 = 500 mm
Doc   = 9 x 100 = 900 mm
```

Day la ti le hinh chu nhat hop ly hon 8 x 8, vi co the nguoi nam co dang dai theo truc vai-den-dui.

## Tinh Velostat 28 x 28 cm

1 tam Velostat:

```text
28 x 28 cm = 280 x 280 mm
```

Neu cat patch 50 x 50 mm:

```text
floor(280 / 50) = 5 patch moi chieu
5 x 5 = 25 patch / tam
```

Can cho 45 cell:

```text
45 / 25 = 1.8 -> can toi thieu 2 tam
```

Neu mua 6 tam:

```text
6 x 25 = 150 patch
```

So bo 5 x 9 co the lam:

```text
150 / 45 = 3 bo day du, con 15 patch du phong
```

Ket luan: 6 tam la phuong an an toan cho thu nghiem fail, cat loi, hieu chuan va lam lai cum cam bien.

## Dien cuc copper tape / conductive fabric

Phuong an khuyen nghi cho ban chinh:

```text
Lop vai/TPU phu tren
Dien cuc tren bang copper tape hoac vai dan dien
Velostat 50 x 50 mm
Dien cuc duoi bang copper tape hoac vai dan dien
Nen PET/Kapton/vai mong
Tui khi silicone
```

Khuyen nghi kich thuoc dien cuc:

```text
Velostat patch:     50 x 50 mm
Dien cuc tren:      40-45 x 40-45 mm
Dien cuc duoi:      40-45 x 40-45 mm
```

Khong nen de dong tran tiep xuc truc tiep voi da. Tat ca phai nam duoi lop vai/TPU phu.

## So kenh dien tu

Voi 45 sensor doc lap:

```text
45 sensor = 45 kenh analog
```

Khuyen nghi dung:

```text
3 x CD74HC4067 analog multiplexer
```

Vi:

```text
1 module = 16 kenh
3 module = 48 kenh
```

Du cho 45 sensor va con 3 kenh du phong.

## File da cap nhat/them

```text
cad/full_assembly.scad
cad/full_assembly_5x9.scad
cad/baseplate_5x9.scad
simulation/velostat_heatmap_sim.py
outputs/figures/velostat_pressure_heatmap_sim.png
outputs/figures/velostat_sensor_curve.png
cad/drawings/final_5x9_50mm_velostat_layout.png
cad/drawings/final_5x9_50mm_velostat_layout.svg
```

## Chot ky thuat

Cau hinh 5 x 9 voi patch 50 x 50 mm la diem can bang tot giua:

- do phu co the;
- so cell/valve hop ly;
- chi phi Velostat chap nhan duoc;
- du du lieu de ve heatmap ap luc;
- de mo rong ve sau neu them module got chan rieng.
