# Buoc 1 - Trich tham so Velostat/Linqstat tu datasheet

Ngay cap nhat: 2026-07-27

## 1. Thong tin vat lieu tu datasheet nguoi dung cung cap

Vat lieu:

```text
Conductive pressure-sensitive sheet
Ten thuong mai: Velostat / Linqstat
```

Kich thuoc moi tam:

```text
11 x 11 inch = 28 x 28 cm = 280 x 280 mm
```

Do day:

```text
4 mil = 0.1 mm
```

Khoi luong moi tam:

```text
18.66 g
```

Nhiet do lam viec:

```text
-45 degC den 65 degC
```

Tinh chat:

```text
Heat sealable: yes
```

Dien tro suat the tich:

```text
Volume resistivity < 500 ohm-cm
```

Dien tro mat:

```text
Surface resistivity < 31,000 ohm/sq.cm theo datasheet
```

Luu y: Ky hieu `ohm/sq.cm` cua nha ban hang khong phai cach ghi chuan cua sheet resistance. Trong mo phong nen doc la thong tin dinh huong, khong coi la duong dac tinh R(P) day du.

## 2. Thong so hinh hoc patch da chot

Cau hinh cam bien cua du an:

```text
Ma tran dem:          5 x 9
So sensor/cell:       45
Kich thuoc Velostat:  50 x 50 mm moi cell
Do day Velostat:      0.1 mm
```

Doi don vi cho mo phong:

```text
patch_w = 50 mm = 5.0 cm = 0.05 m
patch_h = 50 mm = 5.0 cm = 0.05 m
area    = 25 cm^2 = 0.0025 m^2
thick   = 0.1 mm = 0.01 cm = 1e-4 m
```

## 3. Tinh so patch tu 6 tam Velostat

Mot tam 280 x 280 mm, cat patch 50 x 50 mm:

```text
floor(280 / 50) = 5 patch moi chieu
5 x 5 = 25 patch / tam
```

Voi 6 tam:

```text
6 x 25 = 150 patch
```

Ma tran 5 x 9 can:

```text
45 patch / bo
```

So bo day du:

```text
150 / 45 = 3 bo day du, du 15 patch
```

Ket luan: 6 tam la du an toan cho cat loi, che tao lai, hieu chuan va mau thu.

## 4. Dieu quan trong: datasheet nay chua co duong R(P)

Datasheet hien tai chi cho biet vat lieu co tinh chat pressure-sensitive va cac gioi han dien tro suat. No chua cho bang/duong:

```text
Force/pressure -> resistance
```

Do do, trong SOFA ta co the mo phong co hoc de tinh:

```text
P(x,y,t) tren patch Velostat
```

nhung quan he:

```text
P(x,y,t) -> R(t)
```

van phai lay tu:

1. datasheet day du hon neu co;
2. tai lieu Handcrafting Sensors neu co duong test;
3. hieu chuan thuc nghiem bang qua can.

## 5. Can than voi dien tro suat the tich

Neu lay truc tiep cong thuc vat lieu dong nhat:

```text
R = rho * L / A
```

voi:

```text
rho < 500 ohm-cm
L = 0.01 cm
A = 25 cm^2
```

thi:

```text
R < 500 * 0.01 / 25 = 0.2 ohm
```

Gia tri nay khong phu hop voi cam bien Velostat thuc te ma ta thuong do bang mach chia ap, vi tin hieu thuc te bi chi phoi boi:

- dien tro tiep xuc giua copper tape va Velostat;
- phan bo luc khong dong deu;
- cau truc carbon-loaded polymer;
- dien tro mat/sheet resistance;
- hysteresis va creep;
- do nham, keo dan, lop phu;
- cach bo tri dien cuc.

Vi vay khong duoc dung so 0.2 ohm lam dien tro cam bien trong mach ADC.

## 6. Model tam thoi cho mo phong

Truoc khi co du lieu hieu chuan, dung model piezoresistive dang Hill/logistic:

```text
R(P) = R_min + (R_max - R_min) / (1 + (P / P50)^gamma)
```

Trong do:

```text
P       = ap suat trung binh hoac ap suat hieu dung tren patch
R(P)    = dien tro cam bien do duoc giua 2 dien cuc
R_max   = dien tro khi khong tai
R_min   = dien tro khi tai cao
P50     = muc ap suat tai diem chuyen tiep
Gamma   = do doc duong cong
```

Gia tri ban dau chi dung de test phan mem:

```text
R_max = 900 kOhm
R_min = 4 kOhm
P50   = 32 mmHg
Gamma = 1.45
```

Sau khi co mau that, bat buoc thay cac tham so nay bang ket qua hieu chuan.

## 7. Hieu chuan thuc nghiem bat buoc

Voi patch 50 x 50 mm:

```text
A = 0.05 * 0.05 = 0.0025 m^2
```

Ap suat tu vat nang:

```text
P(Pa) = m * 9.81 / A
P(mmHg) = P(Pa) / 133.322
```

Bang tai trong goi y:

| Khoi luong | Ap suat tren patch 50 x 50 mm |
|---:|---:|
| 0.25 kg | 7.4 mmHg |
| 0.50 kg | 14.7 mmHg |
| 1.00 kg | 29.4 mmHg |
| 1.50 kg | 44.1 mmHg |
| 2.00 kg | 58.9 mmHg |
| 2.50 kg | 73.6 mmHg |

Tai moi muc:

1. Dat vat nang qua tam phang cung kich thuoc 50 x 50 mm.
2. Cho on dinh 5-10 giay.
3. Ghi ADC/R trung binh 3-5 giay.
4. Lap lai 3-5 lan de danh gia repeatability.
5. Fit lai R(P).

## 8. Dau vao cho SOFA

Tu datasheet hien tai, SOFA scene nen dung cac thong so co hoc/hinh hoc sau:

```text
Velostat thickness = 0.1 mm
Velostat patch     = 50 x 50 mm
Temperature range  = -45..65 degC, chi de ghi chu dieu kien van hanh
```

Cac tham so chua co, can gia dinh/fit:

```text
Young modulus cua Velostat
Poisson ratio cua Velostat
Young modulus cua silicone bag
Poisson ratio cua silicone
Friction/contact coefficient
R(P) hoac Rs(P)
Hysteresis/creep theo thoi gian
```

## 9. Ket luan buoc 1

Da co du thong so hinh hoc de bat dau SOFA single-patch simulation:

```text
50 x 50 x 0.1 mm Velostat patch
sandwich electrode
elastic support/silicone bag
rigid indenter/load
```

Nhung chua du thong so dien-de-ap-suat de cong bo dinh luong. Can hieu chuan thuc nghiem hoac datasheet chi tiet hon de xay dung R(P) chinh xac.
