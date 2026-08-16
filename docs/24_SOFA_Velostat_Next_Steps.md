# Buoc 3 tro di - Ke hoach SOFA Velostat heatmap

Ngay cap nhat: 2026-07-27

## Muc tieu cuoi

Xay dung pipeline nghiem tuc:

```text
SOFA mechanical model
    -> pressure field tren Velostat patch
    -> piezoresistive sensor model R(P)
    -> voltage divider / ADC model
    -> heatmap 5 x 9
    -> risk map va pressure-time index
```

## Buoc 3 - Single patch SOFA model

Tao scene:

```text
simulation/sofa/scenes/single_velostat_patch.py
```

Thanh phan:

```text
rigid indenter / load plate
cover fabric layer
upper copper electrode region
Velostat 50 x 50 x 0.1 mm
lower copper electrode region
silicone/airbag elastic support
fixed boundary/frame
```

Output can lay:

```text
contact force
indentation depth
pressure distribution P(x,y)
mean pressure on patch
max pressure on patch
```

## Buoc 4 - Sensor electrical coupling

Tu SOFA pressure field:

```text
P(x,y,t)
```

Tinh:

```text
P_eff(t) hoac G_total(t)
R_velostat(t)
Vout(t)
ADC(t)
```

Ban dau co the dung:

```text
P_eff = mean(P tren vung electrode overlap)
R = R_min + (R_max - R_min) / (1 + (P_eff/P50)^gamma)
```

Sau khi hieu chuan that, thay R_min/R_max/P50/gamma bang du lieu fit.

## Buoc 5 - Calibration experiment

Lam 1 sensor that:

```text
copper tape tren
Velostat 50 x 50 mm
copper tape duoi
R_fixed 47 kOhm
ADC 12-bit
```

Tai trong goi y:

```text
0 kg
0.25 kg
0.50 kg
1.00 kg
1.50 kg
2.00 kg
2.50 kg
```

Moi tai trong ghi:

```text
mass_kg, pressure_mmHg, resistance_ohm, adc_count, time_s
```

Fit duong:

```text
R(P)
```

## Buoc 6 - 3 x 3 SOFA model

Mo rong tu 1 patch sang 3 x 3:

```text
9 cell / 9 sensor
```

Muc tieu:

```text
kiem tra crosstalk co hoc
kiem tra ap suat lan tu cell nay sang cell khac
kiem tra do on dinh cua heatmap khi load lech tam
```

## Buoc 7 - 5 x 9 reduced-order model

Mo rong thanh cau hinh cuoi:

```text
5 x 9 = 45 sensor
```

Khong can mesh sieu min cho toan bo 45 cell ngay tu dau. Co the dung:

```text
moi patch = mot vung lay mau ap suat
moi cell = elastic support co tham so rieng
body load = phan bo theo vai-lung-mong-dui
```

Output:

```text
45 gia tri P_eff
45 gia tri R
45 gia tri ADC
heatmap 9 x 5
```

## Buoc 8 - Doi chung mo phong va thuc nghiem

So sanh:

```text
SOFA predicted pressure
ADC measured pressure
calibrated pressure heatmap
```

Chi so danh gia:

```text
MAE / RMSE ap suat
correlation voi tai trong
repeatability
hysteresis loading/unloading
response time
pressure-time index sai khac
```

## Chien luoc cong bo/thuyet phuc hoi dong

Nen trinh bay theo tam giac:

```text
1. Model co hoc SOFA
2. Model dien tro Velostat da hieu chuan
3. Prototype thuc nghiem co heatmap realtime
```

Neu 3 phan nay khop nhau, de tai se thuyet phuc hon nhieu so voi chi co demo Python heatmap.
