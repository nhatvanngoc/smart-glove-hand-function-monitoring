# SOFA scene dau tien - Single Velostat patch 50 x 50 mm

Ngay cap nhat: 2026-07-27

## Muc tieu

Sau khi cai SOFA thanh cong, buoc tiep theo la chay scene dau tien:

```text
simulation/sofa/scenes/single_velostat_patch.py
```

Scene nay la mo hinh v0 cho mot cam bien:

```text
rigid load plate / indenter visual
upper copper electrode visual
Velostat patch 50 x 50 x 0.1 mm, deformable FEM grid
lower copper electrode visual
silicone support visual
```

Luu y: day la scene v0, force-controlled. No chua phai contact simulation day du. Muc tieu dau tien la:

```text
SOFA scene Python chay duoc
Velostat layer bien dang duoi tai trong
xuat du lieu pressure proxy theo thoi gian
couple sang R(P), Vout, ADC placeholder
```

Sau khi scene nay on, ta moi nang cap sang contact mechanics that su va 3 x 3 / 5 x 9.

## File da tao

```text
simulation/sofa/scenes/single_velostat_patch.py
simulation/sofa/assets/copper_top_44x44.obj
simulation/sofa/assets/copper_bottom_44x44.obj
simulation/sofa/assets/silicone_support_90x90x15.obj
simulation/sofa/assets/indenter_50x50.obj
simulation/sofa/postprocess_single_patch.py
```

Output khi chay SOFA:

```text
simulation/sofa/outputs/single_velostat_patch_timeseries.csv
```

Postprocess output:

```text
simulation/sofa/outputs/single_velostat_patch_response.png
```

## Cach chay trong WSL

Vao thu muc project trong WSL. Neu project nam trong o C Windows, duong dan thuong la:

```bash
cd /mnt/c/Users/<ten_user>/Downloads/adaptive_cushion_aac
```

Neu project nam trong home WSL:

```bash
cd ~/adaptive_cushion_aac
```

Kich hoat environment:

```bash
conda activate sofa-velostat
```

Chay scene:

```bash
runSofa -l SofaImGui -g imgui -l SofaPython3 simulation/sofa/scenes/single_velostat_patch.py
```

Trong SOFA GUI, bam:

```text
Animate / Play
```

Chay vai giay de no ghi CSV.

## Xem ket qua CSV

Sau khi chay, kiem tra:

```bash
ls simulation/sofa/outputs/
head simulation/sofa/outputs/single_velostat_patch_timeseries.csv
```

File CSV co cac cot:

```text
time_s
applied_force_N
pressure_Pa
pressure_mmHg
mean_z_mm
min_z_mm
R_ohm_placeholder
Vout_V_placeholder
ADC12_placeholder
```

## Ve do thi ket qua

Chay:

```bash
python simulation/sofa/postprocess_single_patch.py
```

Ket qua:

```text
simulation/sofa/outputs/single_velostat_patch_response.png
```

## Y nghia cua scene v0

Scene nay dang ap luc theo kieu:

```text
applied_force_N / area_patch
```

Voi patch:

```text
50 x 50 mm = 0.0025 m^2
```

Ap suat:

```text
P(Pa) = F / A
P(mmHg) = P(Pa) / 133.322
```

Mac dinh scene ramp toi:

```text
F = 18 N
```

nen:

```text
P = 18 / 0.0025 = 7200 Pa
P = 7200 / 133.322 = 54 mmHg
```

Day la dải ap suat co y nghia vi vuot nguong tham chieu 32 mmHg.

## Luu y ve R(P)

Datasheet ban gui chua co duong:

```text
pressure -> resistance
```

Nen scene dang dung placeholder:

```text
R(P) = R_min + (R_max - R_min) / (1 + (P/P50)^gamma)
```

Thong so placeholder:

```text
R_max = 900 kOhm
R_min = 4 kOhm
P50   = 32 mmHg
gamma = 1.45
```

Phan nay bat buoc se thay bang hieu chuan thuc nghiem sau.

## Neu chay bi loi

Gui minh nguyen van loi. Cac loi co the gap:

### Loi thieu plugin

Vi du:

```text
Object type HexahedronFEMForceField not found
```

Gui lai loi de minh bo sung/sua `RequiredPlugin`.

### Loi MeshOBJLoader/OglModel

Neu loi visual, co the tam thoi comment cac visual object. Phan quan trong nhat la node VelostatPatch.

### Loi ConstantForceField totalForce

Neu SOFA version cua ban dung data name khac, minh se sua sang `forces` hoac cach ap force khac.

## Buoc tiep theo sau khi scene v0 chay

1. Xac nhan scene chay duoc va xuat CSV.
2. Nang cap support tu fixed-bottom sang silicone elastic support.
3. Them contact plate that su thay vi force-controlled.
4. Lay pressure/contact field khong chi pressure trung binh.
5. Mo rong thanh 3 x 3 sensor.
6. Cuoi cung mo rong 5 x 9.
