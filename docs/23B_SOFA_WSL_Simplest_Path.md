# Cach don gian nhat: Cai SOFA trong WSL2 Ubuntu

Ngay cap nhat: 2026-07-27

## Ket luan

Neu Anaconda tren Windows khong dung duoc, co the dung WSL2. Day la huong minh khuyen:

```text
Windows 11/10
  -> WSL2 Ubuntu 22.04
  -> Miniforge rieng trong WSL
  -> conda env sofa-velostat
  -> sofa-app + sofa-python3
```

Luu y: Khong dung Anaconda Windows nua. Miniforge trong WSL la moi truong rieng, sach hon va de sua loi hon.

## Buoc 1 - Cai WSL2 Ubuntu

Mo PowerShell bang quyen Administrator, chay:

```powershell
wsl --install -d Ubuntu-22.04
```

Neu may da co WSL, chay:

```powershell
wsl --list --verbose
```

Neu can set WSL2:

```powershell
wsl --set-default-version 2
```

Restart may neu Windows yeu cau.

## Buoc 2 - Mo Ubuntu va cap nhat

Mo ung dung:

```text
Ubuntu 22.04
```

Trong terminal Ubuntu, chay:

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y git wget curl build-essential cmake ninja-build mesa-utils libgl1 libglu1-mesa libxrender1 libxext6 libxi6 libxrandr2 libxcursor1 libxinerama1
```

## Buoc 3 - Cai Miniforge trong WSL

Chay:

```bash
cd ~
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
bash Miniforge3-Linux-x86_64.sh
```

Khi hoi:

```text
Do you wish to update your shell profile?
```

chon:

```text
yes
```

Dong Ubuntu terminal, mo lai Ubuntu.

Kiem tra:

```bash
conda --version
```

## Buoc 4 - Tao environment SOFA

```bash
conda create -n sofa-velostat python=3.12 -y
conda activate sofa-velostat
```

Neu Python 3.12 loi package, dung Python 3.10:

```bash
conda create -n sofa-velostat python=3.10 -y
conda activate sofa-velostat
```

## Buoc 5 - Cai SOFA + SofaPython3

```bash
conda install sofa-app sofa-python3 --channel https://prefix.dev/sofa-framework --channel conda-forge -y
```

## Buoc 6 - Test SofaPython3

```bash
python -c "import Sofa; import SofaRuntime; print('SofaPython3 OK')"
```

Neu hien:

```text
SofaPython3 OK
```

la thanh cong phan Python.

## Buoc 7 - Test GUI SOFA

```bash
runSofa -l SofaImGui -g imgui -l SofaPython3
```

Neu cua so SOFA hien len la thanh cong.

Neu GUI khong hien, van gui loi cho minh. Co the do WSLg/OpenGL, khong phai loi SOFA.

## Lenh tom tat copy mot lan trong Ubuntu

Neu WSL da cai xong va chua cai Miniforge:

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y git wget curl build-essential cmake ninja-build mesa-utils libgl1 libglu1-mesa libxrender1 libxext6 libxi6 libxrandr2 libxcursor1 libxinerama1
cd ~
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
bash Miniforge3-Linux-x86_64.sh
```

Sau do dong/mo lai Ubuntu, roi chay:

```bash
conda create -n sofa-velostat python=3.12 -y
conda activate sofa-velostat
conda install sofa-app sofa-python3 --channel https://prefix.dev/sofa-framework --channel conda-forge -y
python -c "import Sofa; import SofaRuntime; print('SofaPython3 OK')"
runSofa -l SofaImGui -g imgui -l SofaPython3
```

## Neu loi thi gui minh 3 thong tin

```text
1. Windows 10 hay Windows 11?
2. Ket qua lenh: wsl --list --verbose
3. Nguyen van loi khi chay: python -c "import Sofa; import SofaRuntime; print('SofaPython3 OK')"
4. Nguyen van loi khi chay: runSofa -l SofaImGui -g imgui -l SofaPython3
```

Sau khi cai xong, ta bat dau tao scene:

```text
simulation/sofa/scenes/single_velostat_patch.py
```
