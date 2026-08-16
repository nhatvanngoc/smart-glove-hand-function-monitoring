#!/usr/bin/env bash
set -e

# Run from project root:
#   bash scripts/run_sofa_single_patch_batch.sh

if command -v conda >/dev/null 2>&1; then
  source "$(conda info --base)/etc/profile.d/conda.sh"
  conda activate sofa-velostat
fi

python simulation/sofa/run_single_patch_batch.py --steps 300
python simulation/sofa/postprocess_single_patch.py --batch

echo "Done. See: simulation/sofa/outputs/single_velostat_patch_batch_response.png"
