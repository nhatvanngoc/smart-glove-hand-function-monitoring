# Lua chon framework mo phong nghiem tuc: SOFA hay Taichi

Ngay cap nhat: 2026-07-27

## Ket luan chot

Voi muc tieu de tai khoa hoc nghiem tuc, co kha nang bao ve cap quoc gia/quoc te, nen chon:

```text
SOFA Framework = nen tang mo phong co hoc mem chinh
Python/PyQtGraph = hien thi realtime heatmap va doc du lieu
Taichi = cong cu phu neu can prototype nhanh mo hinh 2.5D/GPU
```

Khong nen chon Taichi lam nen tang chinh ngay tu dau, vi Taichi manh ve tu viet kernel mo phong nhanh, nhung ban se phai tu xay gan nhu toan bo pipeline vat lieu mem/contact/hieu chuan. SOFA phu hop hon de lam co so ly thuyet cho vat lieu mem, y sinh, soft robotics va mo phong contact/FEM.

## Vi sao SOFA phu hop hon cho de tai nay

Bai toan cua du an khong chi la ve heatmap. Bai toan that su la:

```text
co the nguoi / vat nang
    -> ep len lop vai + Velostat + copper tape + tui silicone
    -> sinh bien dang va phan bo ap suat
    -> Velostat doi dien tro theo ap suat/bien dang
    -> mach dien doc ADC
    -> tai tao pressure heatmap
```

Trong chuoi tren, phan kho nhat la:

```text
bien dang vat lieu mem + contact + phan bo ap suat
```

SOFA co loi the o phan nay.

## So sanh SOFA va Taichi cho du an

| Tieu chi | SOFA Framework | Taichi |
|---|---|---|
| FEM/vat lieu mem | Manh, co san nhieu thanh phan | Phai tu viet nhieu |
| Contact mechanics | Co san pipeline contact/collision | Phai tu xay hoac don gian hoa |
| Y sinh/soft robotics | Phu hop hon | Co the lam nhung phai custom |
| Tinh thuyet phuc hoc thuat | Cao hon neu thiet lap dung | Cao neu code rat tot, nhung de bi xem la custom/toy neu thieu kiem chung |
| Realtime | Co the realtime voi mo hinh vua phai | Rat nhanh, GPU tot |
| Do de hoc | Kho hon Python thuong | De bat dau hon neu quen Python/GPU |
| Mo phong dien tro Velostat | Can custom controller/plugin | Cung phai custom |
| Ve heatmap | Can Python bridge | Rat de |
| Rủi ro ky thuat | Cai dat/cau hinh kho | Tu viet physics sai/khong chuan |
| Vai tro khuyen nghi | Nen tang chinh | Cong cu phu/doi chung |

## Lua chon kien truc cuoi

Nen lam theo kien truc 3 lop:

```text
Lop A - SOFA mechanical simulation
    human load / indenter
    cover fabric
    Velostat patches
    copper electrode regions
    silicone air bag / elastic support
    contact pressure field

Lop B - Sensor-electrical transduction
    pressure field P(x,y,t)
    -> R_velostat(P) hoac sheet resistance Rs(P)
    -> electrode geometry factor
    -> voltage divider
    -> ADC

Lop C - Realtime heatmap dashboard
    ADC/P_estimated matrix 9 x 5
    -> heatmap
    -> risk map
    -> pressure-time index
    -> control signal cho valve/pump
```

SOFA phu trach Lop A. Python phu trach Lop B va Lop C. Taichi chi dung neu can Lop A nhanh hon/2.5D hon trong phien ban phu.

## Muc do mo phong nen lam

### Muc 1 - Nghiem tuc va kha thi

Dung SOFA de mo phong tung cell hoac ma tran nho 3 x 3 truoc:

```text
rigid indenter hoac pressure load
cover/fabric layer
Velostat patch 50 x 50 mm
copper electrode masks
elastic silicone support
```

Output:

```text
pressure distribution tren Velostat patch
mean pressure moi patch
max pressure moi patch
```

Sau do dung model dien de sinh ADC va heatmap.

### Muc 2 - Toan bo 5 x 9

Sau khi cell don le on, mo rong thanh 5 x 9:

```text
45 patch Velostat
45 cell/tui khi
body load phan bo theo vai-lung-mong-dui
```

Khong nhat thiet mesh that min cho toan bo 45 cell ngay tu dau. Co the dung:

- mesh chi tiet cho 1 cell;
- model reduced-order cho 45 cell;
- hoac hybrid: SOFA tinh pressure field, Python aggregate thanh 45 sensor readings.

### Muc 3 - Nang cao

Neu co du thoi gian:

- mo phong tui khi co ap suat noi bo thay doi theo valve;
- mo phong fatigue/hysteresis cua Velostat;
- mo phong dynamic pressure-time index;
- doi chung voi thuc nghiem qua can va nguoi tinh nguyen.

## Cach mo hinh hoa Velostat + copper tape

### Sandwich electrode

Voi ban dang chot, khuyen nghi mo phong sandwich:

```text
upper copper electrode
Velostat 50 x 50 mm
lower copper electrode
```

Co hoc:

- copper tape: lop rat mong, co the coi la electrode region/mask; khong can mesh cuc min neu chi quan tam tin hieu.
- Velostat: lop mem/piezoresistive; trong co hoc co the gan elastic material don gian.
- silicone/tui khi: elastic support hoac pressure cavity.

Dien:

```text
R(P) = model tu datasheet + hieu chuan thuc nghiem
```

Neu can chinh xac hon:

```text
G_total(t) = integral_over_electrode_area sigma(P(x,y,t)) dA / thickness
R_total = 1 / G_total
```

Sau do:

```text
Vout = Vcc * R_fixed / (R_velostat + R_fixed)
ADC = round(Vout / Vcc * 4095)
```

### Interdigitated electrode

Neu dung rang luoc thi phuc tap hon:

```text
G_total ~ integral sigma(P) * geometry_factor(x,y) dA
```

Hoac lap luoi resistor network 2D tren Velostat. Tuy nhien ban hien da chot patch 50 x 50 mm va nen di theo sandwich de co tinh lap lai va de mo phong.

## Ke hoach lam viec tiep theo sau khi co datasheet Velostat

Can lay tu datasheet/cung cap:

1. Dien tro tam/sheet resistance khi khong tai.
2. Duong R hoac conductance theo force/pressure.
3. Do day vat lieu.
4. Khoang pressure/force test cua nha san xuat.
5. Hysteresis/repeatability neu co.
6. Thoi gian dap ung/relaxation neu co.
7. Anh huong do am/nhiet neu co.

Sau khi co datasheet, se lam:

```text
B1. Trich duong R(P) tu datasheet.
B2. Fit model R(P) hoac Rs(P).
B3. Viet SOFA scene cho single sensor patch.
B4. Coupling SOFA pressure -> R -> ADC.
B5. Ve heatmap single sensor / 3x3.
B6. Mo rong 5x9.
```

## Ket luan

Chon SOFA lam nen tang mo phong chinh la hop ly nhat neu muc tieu la nghiem tuc va thuyet phuc. Taichi rat dang gia, nhung nen giu lam cong cu phu de prototype nhanh hoac doi chung 2.5D, khong phai framework chinh cho bai bao/de tai luc nay.
