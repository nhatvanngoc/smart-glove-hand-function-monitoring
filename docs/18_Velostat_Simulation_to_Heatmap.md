# Mo phong Velostat + copper tape va dung ban do nhiet ap suat

Ngay cap nhat: 2026-07-24

## Muc tieu

Mo phong chuoi sau:

```text
Ap suat tren tung cell
    -> dien tro Velostat thay doi
    -> mach chia ap tao dien ap analog
    -> ADC doc gia tri so
    -> tai tao ap suat
    -> ve heatmap ap suat
```

File mo phong da tao:

```text
simulation/velostat_heatmap_sim.py
```

Chay:

```bash
python3 simulation/velostat_heatmap_sim.py
```

Ket qua:

```text
outputs/figures/velostat_pressure_heatmap_sim.png
outputs/figures/velostat_sensor_curve.png
outputs/reports/velostat_true_pressure.csv
outputs/reports/velostat_adc_counts.csv
outputs/reports/velostat_reconstructed_pressure.csv
```

## 1. Cach hieu dung ve mo phong

Khong can mo phong FEA/COMSOL ngay tu dau. Voi ban dau, nen mo phong he thong theo muc sensor-cell:

```text
moi cell khi = 1 sensor Velostat doc lap
```

Voi ma tran 5 x 9:

```text
5 cot ngang than nguoi x 9 hang doc than nguoi = 45 diem do
```

Moi diem do co:

- 1 patch Velostat 45-50 mm;
- 2 dien cuc bang copper tape/vai dan dien;
- 1 kenh ADC hoac 1 kenh multiplexer analog.

## 2. Mo hinh ap suat -> dien tro

Velostat khong phai cam bien tuyen tinh. Khi ap luc tang, dien tro giam.

Mo hinh tam dung trong code:

```text
R(P) = R_min + (R_max - R_min) / (1 + (P / P50)^gamma)
```

Trong do:

```text
P       = ap suat, don vi mmHg
R(P)    = dien tro Velostat
R_max   = dien tro khi gan nhu khong bi ep
R_min   = dien tro khi bi ep manh
P50     = ap suat tai vung chuyen tiep
Gamma   = do doc cua duong cong
```

Gia tri hien tai trong code chi la gia tri gia lap:

```text
R_max = 900 kOhm
R_min = 4 kOhm
P50   = 32 mmHg
Gamma = 1.45
```

Sau khi co mau that, phai hieu chuan lai bang qua can/ta trong.

## 3. Mo hinh mach chia ap

Mach khuyen nghi:

```text
3.3V ---- Velostat ---- ADC node ---- R_fixed ---- GND
```

Trong code dang dung:

```text
R_fixed = 47 kOhm
ADC     = 12 bit
Vcc     = 3.3 V
```

Dien ap ADC:

```text
Vout = Vcc * R_fixed / (R_velostat + R_fixed)
```

Vi ap luc tang lam R_velostat giam, nen:

```text
ap luc tang -> Vout tang -> ADC count tang
```

Neu ban lap mach nguoc lai:

```text
3.3V ---- R_fixed ---- ADC node ---- Velostat ---- GND
```

thi chieu tin hieu se nguoc:

```text
ap luc tang -> ADC count giam
```

## 4. Mo phong copper tape nhu the nao?

Trong ban mo phong dau tien, khong can ve tung duong dong bang CAD/FEA. Ta chi can dua anh huong hinh hoc dien cuc vao he so dien tro.

### Dien cuc sandwich

Cau truc:

```text
Dien cuc tren
Velostat
Dien cuc duoi
```

Gan dung:

```text
R ~ rho(P) * thickness / area
```

Dien cuc/pad cang lon thi dien tro do duoc cang nho.

### Dien cuc rang luoc/interdigitated

Cau truc:

```text
A: cac ngon dong
B: cac ngon dong xen ke
Velostat phu len tren
```

Gan dung:

```text
conductance ~ so_khe * chieu_dai_ngon / khoang_cach_khe
R ~ 1 / conductance
```

Trong code co tham so don gian de doi giua:

```bash
python3 simulation/velostat_heatmap_sim.py --electrode sandwich
python3 simulation/velostat_heatmap_sim.py --electrode interdigitated
```

## 5. Dung heatmap ap suat

Sau khi co ADC, code se:

1. Chuyen ADC ve dien ap.
2. Tinh nguoc ra R_velostat.
3. Tinh nguoc ra ap suat uoc luong.
4. Ve anh heatmap.

Heatmap co 3 panel:

```text
Panel 1: ap suat that mo phong
Panel 2: ADC doc duoc
Panel 3: ap suat tai tao tu ADC
```

Trong he thong that, panel 1 khong co. Ta chi co ADC va ap suat tai tao sau hieu chuan.

## 6. Neu doc phan cung that

Du lieu tu STM32/Arduino/ESP32 nen gui ve may tinh theo dang CSV:

```text
time_ms,row,col,adc
0,0,0,315
0,0,1,340
...
```

Sau do Python ghep lai thanh ma tran:

```text
pressure_map[row, col]
```

roi ve bang:

```python
plt.imshow(pressure_map, cmap="inferno")
```

## 7. Buoc hieu chuan that

Can lam it nhat 5-7 muc tai trong:

```text
0 mmHg
10 mmHg
20 mmHg
32 mmHg
40 mmHg
60 mmHg
80 mmHg
```

Voi moi muc:

1. Dat vat nang/qua can len patch qua mot tam phang co dien tich biet truoc.
2. Tinh ap suat: P = F / A.
3. Ghi ADC trung binh trong 3-5 giay.
4. Fit duong cong ADC -> ap suat.

Luu y doi don vi:

```text
1 mmHg = 133.322 Pa
P(Pa) = m * 9.81 / A(m^2)
P(mmHg) = P(Pa) / 133.322
```

Vi du patch 50 x 50 mm:

```text
A = 0.05 * 0.05 = 0.0025 m^2
m = 1 kg
P = 1 * 9.81 / 0.0025 = 3924 Pa = 29.4 mmHg
```

## 8. Khuyen nghi cho de tai

Ban nen trinh bay theo 3 muc:

1. Mo phong sensor:
   ap suat -> dien tro -> ADC.

2. Mo phong ma tran:
   45 sensor tao thanh heatmap 5 x 9.

3. Hieu chuan thuc nghiem:
   dung qua can de thay tham so mo phong bang du lieu that.

Day la cach vua dung ky thuat, vua phu hop voi de tai nghien cuu ung dung.
