# SOFA batch/headless workflow cho WSL

Ngay cap nhat: 2026-07-27

## Ket luan

Neu GUI SOFA trong WSL khong on, khong sao. Voi du an nghien cuu nghiem tuc, batch/headless con tot hon GUI vi:

- de lap lai ket qua;
- de ghi CSV/log;
- de chay nhieu case tham so;
- de dua vao pipeline bao cao;
- khong phu thuoc OpenGL/WSLg;
- phu hop chay tren server/GPU/CI ve sau.

GUI chi can de xem nhanh hinh dang. Phan tinh toan chinh nen chay batch.

## File batch da tao

```text
simulation/sofa/scenes/single_velostat_patch_batch.py
simulation/sofa/run_single_patch_batch.py
scripts/run_sofa_single_patch_batch.sh
```

Scene batch khong dung:

```text
OglModel
MeshOBJLoader
Sofa.GL
GUI rendering
```

Nen no nhe va it loi hon trong WSL.

## Cach chay khuyen nghi

Trong WSL, vao project:

```bash
cd /duong/dan/toi/adaptive_cushion_aac
conda activate sofa-velostat
python simulation/sofa/run_single_patch_batch.py --steps 300
python simulation/sofa/postprocess_single_patch.py --batch
```

Hoac chay script:

```bash
bash scripts/run_sofa_single_patch_batch.sh
```

## Output

CSV:

```text
simulation/sofa/outputs/single_velostat_patch_batch_timeseries.csv
```

PNG:

```text
simulation/sofa/outputs/single_velostat_patch_batch_response.png
```

## Cach chay bang runSofa batch neu muon

Co the thu:

```bash
runSofa -l SofaPython3 -g batch -n 300 simulation/sofa/scenes/single_velostat_patch_batch.py
```

Neu lenh nay loi option `-n` do version SOFA, dung Python runner o tren la cach on dinh hon.

## Vi sao batch van nghiem tuc

Trong bai bao/de tai, ta khong can GUI de chung minh mo hinh. Ta can:

```text
input parameters
solver settings
mesh/model
CSV output
postprocess plots
validation voi thuc nghiem
```

Batch mode dap ung tot hon GUI cho cac muc nay.

## Buoc tiep theo

Sau khi batch v0 chay duoc:

1. Tao parameter sweep: 0.25 kg, 0.5 kg, 1 kg, 1.5 kg, 2 kg.
2. Xuat duong force-pressure-ADC.
3. Nang cap tu distributed force sang contact plate.
4. Them silicone support mechanical layer.
5. Mo rong 3 x 3.
