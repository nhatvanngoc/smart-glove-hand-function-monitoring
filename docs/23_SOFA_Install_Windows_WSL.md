# Buoc 2 - Cai dat SOFA Framework tren Windows hoac WSL

Ngay cap nhat: 2026-07-27

## 0. Khuyen nghi chon moi truong

Cho du an nay, nen uu tien thu tu sau:

```text
Lua chon 1 - Windows + Miniforge/Conda + SOFA packages
Lua chon 2 - Windows binary official neu chi can GUI nhanh
Lua chon 3 - WSL2 Ubuntu + Conda neu can build/chay script Linux
Lua chon 4 - Build SOFA tu source chi khi cac cach tren loi hoac can plugin rat rieng
```

Ly do:

- Ban can SofaPython3 de viet scene bang Python va lay du lieu pressure/contact.
- Cai bang conda de quan ly SOFA + SofaPython3 thuong gon hon build tu source.
- WSL co the dung duoc nhung GUI/OpenGL va duong dan Windows co the gay loi kho debug.

## 1. Cach A - Windows + Miniforge/Conda, khuyen nghi truoc

### 1.1 Cai Miniforge

Tai Miniforge cho Windows tu:

```text
https://github.com/conda-forge/miniforge
```

Sau khi cai, mo:

```text
Miniforge Prompt
```

Khong nen dung PowerShell thuong neu chua init conda.

### 1.2 Tao environment rieng

```bat
conda create -n sofa-velostat python=3.12 -y
conda activate sofa-velostat
```

Neu Python 3.12 gap loi voi package tai thoi diem cai, dung Python 3.10:

```bat
conda create -n sofa-velostat python=3.10 -y
conda activate sofa-velostat
```

### 1.3 Cai SOFA app va SofaPython3

Thu lenh sau truoc:

```bat
conda install sofa-app sofa-python3 --channel https://prefix.dev/sofa-framework --channel conda-forge -y
```

Neu muon cai them cac plugin hay dung cho soft robotics/model reduction:

```bat
conda install sofa-app sofa-python3 sofa-stlib sofa-modelorderreduction sofa-beamadapter sofa-softrobots sofa-cosserat --channel https://prefix.dev/sofa-framework --channel conda-forge -y
```

Ghi chu: Kenh conda cua SOFA co huong dan cai `sofa-app` va `sofa-python3`, va lenh chay GUI voi SofaPython3 la `runSofa -l SofaImGui -g imgui -l SofaPython3`.

### 1.4 Test GUI SOFA

Chay:

```bat
runSofa -l SofaImGui -g imgui
```

Neu mo duoc cua so SOFA la buoc GUI da on.

### 1.5 Test SofaPython3 plugin

Chay:

```bat
runSofa -l SofaImGui -g imgui -l SofaPython3
```

Neu SOFA mo duoc va khong bao loi plugin, SofaPython3 da san sang.

### 1.6 Test import Python module

Trong Miniforge Prompt:

```bat
python -c "import Sofa; import SofaRuntime; print('SofaPython3 OK')"
```

Neu cau lenh nay OK, ta co the bat dau viet scene Python.

## 2. Cach B - Windows official binary, de xem GUI nhung khong uu tien cho lap trinh Python

Tai binary tu trang release SOFA:

```text
https://github.com/sofa-framework/sofa/releases
```

Cach nay phu hop de:

- mo SOFA GUI nhanh;
- xem scene mau;
- lam quen interface.

Nhung voi du an nay, ban can SofaPython3 va coupling Python. Binary GUI doi khi khac version Python hoac plugin, nen neu bi loi plugin thi quay lai Cach A bang conda.

## 3. Cach C - WSL2 Ubuntu + Conda

### 3.1 Cai WSL2 Ubuntu

Trong PowerShell Admin:

```powershell
wsl --install -d Ubuntu-22.04
```

Restart may neu Windows yeu cau.

### 3.2 Cap nhat Ubuntu

Trong Ubuntu terminal:

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y git wget curl build-essential cmake ninja-build mesa-utils libgl1 libglu1-mesa
```

### 3.3 Cai Miniforge trong WSL

```bash
cd ~
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
bash Miniforge3-Linux-x86_64.sh
```

Dong/mo lai terminal, hoac:

```bash
source ~/.bashrc
```

### 3.4 Tao environment

```bash
conda create -n sofa-velostat python=3.12 -y
conda activate sofa-velostat
```

Neu gap loi package:

```bash
conda create -n sofa-velostat python=3.10 -y
conda activate sofa-velostat
```

### 3.5 Cai SOFA + SofaPython3

```bash
conda install sofa-app sofa-python3 --channel https://prefix.dev/sofa-framework --channel conda-forge -y
```

Hoac ban day du plugin:

```bash
conda install sofa-app sofa-python3 sofa-stlib sofa-modelorderreduction sofa-beamadapter sofa-softrobots sofa-cosserat --channel https://prefix.dev/sofa-framework --channel conda-forge -y
```

### 3.6 Test OpenGL trong WSL

```bash
glxinfo -B
```

Neu khong co `glxinfo`, cai:

```bash
sudo apt install -y mesa-utils
```

### 3.7 Test SOFA GUI trong WSL

```bash
runSofa -l SofaImGui -g imgui -l SofaPython3
```

Neu GUI khong hien, van co the chay scene headless sau nay, nhung de debug ban nen uu tien Windows native truoc.

## 4. Cau truc thu muc SOFA trong du an

Trong project se dung thu muc:

```text
simulation/sofa/
    scenes/
    controllers/
    calibration/
    outputs/
```

De tao:

```bash
mkdir -p simulation/sofa/scenes simulation/sofa/controllers simulation/sofa/calibration simulation/sofa/outputs
```

## 5. File test scene dau tien

Sau khi cai xong, ta se tao scene Python dau tien:

```text
simulation/sofa/scenes/single_velostat_patch.py
```

Muc tieu scene dau tien:

```text
rigid indenter
fabric/copper/Velostat/copper stack
elastic silicone support
contact pressure output
```

Ban chua can scene phuc tap ngay. Muc tieu dau la:

```text
SOFA chay duoc
scene Python load duoc
co vat the mem bien dang duoi indenter
lay duoc force/contact/pressure de dua sang heatmap
```

## 6. Cac loi thuong gap

### Loi 1 - `SofaPython3` plugin not found

Cach xu ly:

```text
1. Kiem tra da cai sofa-python3 chua.
2. Chay dung environment conda.
3. Chay runSofa voi -l SofaPython3.
4. Neu dung binary Windows va loi plugin, chuyen sang cach conda.
```

### Loi 2 - GUI/OpenGL loi trong WSL

Cach xu ly:

```text
1. Cap nhat driver GPU tren Windows.
2. Kiem tra WSLg hoat dong.
3. Test glxinfo -B.
4. Neu van loi, dung Windows native conda de tranh mat thoi gian.
```

### Loi 3 - Python version mismatch

Cach xu ly:

```text
1. Dung environment rieng sofa-velostat.
2. Thu Python 3.12 truoc.
3. Neu loi, tao lai env Python 3.10.
4. Khong dung chung Python system voi SOFA.
```

### Loi 4 - Chay scene tu duong dan co dau cach/Unicode

Nen de project o duong dan ngan, khong dau, khong ky tu dac biet, vi SOFA/plugin/CMake doi khi loi path.

Vi du tot:

```text
C:\\sofa_projects\\adaptive_cushion_aac
```

Tranh:

```text
C:\\Users\\Windows\\Downloads\\full_assembly (1).scad
```

## 7. Lenh cai dat tom tat nhanh

### Windows Miniforge Prompt

```bat
conda create -n sofa-velostat python=3.12 -y
conda activate sofa-velostat
conda install sofa-app sofa-python3 --channel https://prefix.dev/sofa-framework --channel conda-forge -y
runSofa -l SofaImGui -g imgui -l SofaPython3
python -c "import Sofa; import SofaRuntime; print('SofaPython3 OK')"
```

### WSL Ubuntu

```bash
sudo apt update
sudo apt install -y git wget curl build-essential cmake ninja-build mesa-utils libgl1 libglu1-mesa
conda create -n sofa-velostat python=3.12 -y
conda activate sofa-velostat
conda install sofa-app sofa-python3 --channel https://prefix.dev/sofa-framework --channel conda-forge -y
runSofa -l SofaImGui -g imgui -l SofaPython3
python -c "import Sofa; import SofaRuntime; print('SofaPython3 OK')"
```

## 8. Sau khi cai xong can bao lai

Sau khi ban cai xong, gui cho minh 3 ket qua:

```text
1. Lenh runSofa co mo GUI khong?
2. Lenh python import Sofa co OK khong?
3. Ban dung Windows native hay WSL?
```

Neu co loi, copy nguyen thong bao loi. Minh se sua theo loi cu the, khong doan mo.
