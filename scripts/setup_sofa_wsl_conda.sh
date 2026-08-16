#!/usr/bin/env bash
set -e
ENV_NAME=sofa-velostat

echo "============================================================"
echo "Installing basic Ubuntu packages"
echo "============================================================"
sudo apt update
sudo apt install -y git wget curl build-essential cmake ninja-build mesa-utils libgl1 libglu1-mesa

echo "============================================================"
echo "Creating conda env: $ENV_NAME"
echo "============================================================"
conda create -n "$ENV_NAME" python=3.12 -y || conda create -n "$ENV_NAME" python=3.10 -y
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "$ENV_NAME"

echo "============================================================"
echo "Installing SOFA app + SofaPython3"
echo "============================================================"
conda install sofa-app sofa-python3 --channel https://prefix.dev/sofa-framework --channel conda-forge -y

echo "============================================================"
echo "Testing Python imports"
echo "============================================================"
python -c "import Sofa; import SofaRuntime; print('SofaPython3 OK')"

echo "============================================================"
echo "Done. Test GUI with:"
echo "  conda activate $ENV_NAME"
echo "  runSofa -l SofaImGui -g imgui -l SofaPython3"
echo "============================================================"
