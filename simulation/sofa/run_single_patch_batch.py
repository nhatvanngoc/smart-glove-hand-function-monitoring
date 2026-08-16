"""
Pure Python headless runner for the SOFA single Velostat patch scene.

This avoids SOFA GUI completely. Use it in WSL if runSofa GUI is unstable.

Run:
    conda activate sofa-velostat
    python simulation/sofa/run_single_patch_batch.py --steps 300

Then plot:
    python simulation/sofa/postprocess_single_patch.py --batch
"""
from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path

import Sofa
import Sofa.Core
import Sofa.Simulation
import SofaRuntime


ROOT = Path(__file__).resolve().parents[2]
SCENE_PATH = ROOT / "simulation" / "sofa" / "scenes" / "single_velostat_patch_batch.py"


def load_scene_module(path: Path):
    spec = importlib.util.spec_from_file_location("single_velostat_patch_batch", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load scene module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", type=int, default=300, help="Number of SOFA animation steps")
    parser.add_argument("--dt", type=float, default=None, help="Override root dt if needed")
    args = parser.parse_args()

    # Import SofaPython3 runtime plugin explicitly.
    # Component plugins are loaded by RequiredPlugin in the scene.
    try:
        SofaRuntime.importPlugin("SofaPython3")
    except Exception:
        # If already imported or not needed, do not stop immediately.
        pass

    scene = load_scene_module(SCENE_PATH)
    root = Sofa.Core.Node("root")
    scene.createScene(root)
    if args.dt is not None:
        root.dt.value = args.dt

    print("Initializing SOFA scene...")
    Sofa.Simulation.init(root)

    print(f"Running headless simulation: steps={args.steps}, dt={root.dt.value}")
    for i in range(args.steps):
        Sofa.Simulation.animate(root, root.dt.value)
        if (i + 1) % 50 == 0 or i == 0:
            print(f"  step {i + 1}/{args.steps}, time={root.time.value:.3f}s")

    # Close CSV controller cleanly if available.
    for obj in root.objects:
        if hasattr(obj, "close"):
            try:
                obj.close()
            except Exception:
                pass

    Sofa.Simulation.unload(root)
    print("Done.")
    print("CSV output:")
    print("  simulation/sofa/outputs/single_velostat_patch_batch_timeseries.csv")
    print("Plot with:")
    print("  python simulation/sofa/postprocess_single_patch.py --batch")


if __name__ == "__main__":
    main()
