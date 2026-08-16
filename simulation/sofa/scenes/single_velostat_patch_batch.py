# -*- coding: utf-8 -*-
"""
Headless/batch SOFA scene: single Velostat patch 50 x 50 x 0.1 mm.

This file intentionally contains NO GUI/OglModel/visual components.
Use it when SOFA GUI is unstable in WSL.

Run option A, through runSofa batch:
    runSofa -l SofaPython3 -g batch -n 300 simulation/sofa/scenes/single_velostat_patch_batch.py

Run option B, pure Python SofaPython3 driver:
    python simulation/sofa/run_single_patch_batch.py --steps 300

Output:
    simulation/sofa/outputs/single_velostat_patch_batch_timeseries.csv
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

import Sofa
import Sofa.Core


# ---------------------------------------------------------------------
# Geometry and material parameters
# ---------------------------------------------------------------------
PATCH_W_MM = 50.0
PATCH_H_MM = 50.0
VELOSTAT_THICKNESS_MM = 0.1
PATCH_AREA_M2 = (PATCH_W_MM / 1000.0) * (PATCH_H_MM / 1000.0)
PA_PER_MMHG = 133.322

# Placeholder mechanical parameters.
# Must be replaced/justified later using material tests/literature.
VELOSTAT_YOUNG_MODULUS = 5.0e6
VELOSTAT_POISSON = 0.35
VELOSTAT_MASS_KG = 0.00030

DEFAULT_MAX_FORCE_N = 18.0       # 18 N / 0.0025 m2 = ~54 mmHg
DEFAULT_RAMP_TIME_S = 4.0

# Placeholder electrical model. Replace after calibration.
VCC = 3.3
ADC_MAX = 4095.0
R_FIXED_OHM = 47_000.0
R_MAX_OHM = 900_000.0
R_MIN_OHM = 4_000.0
P50_MMHG = 32.0
GAMMA = 1.45


class VelostatBatchController(Sofa.Core.Controller):
    def __init__(self, root, forcefield, dofs, output_path, max_force_N=DEFAULT_MAX_FORCE_N, ramp_time_s=DEFAULT_RAMP_TIME_S):
        Sofa.Core.Controller.__init__(self)
        self.root = root
        self.forcefield = forcefield
        self.dofs = dofs
        self.output_path = Path(output_path)
        self.max_force_N = float(max_force_N)
        self.ramp_time_s = float(ramp_time_s)

        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self._csv_file = open(self.output_path, "w", newline="", encoding="utf-8")
        self._writer = csv.writer(self._csv_file)
        self._writer.writerow([
            "time_s",
            "applied_force_N",
            "pressure_Pa",
            "pressure_mmHg",
            "mean_z_mm",
            "min_z_mm",
            "R_ohm_placeholder",
            "Vout_V_placeholder",
            "ADC12_placeholder",
        ])

    def close(self):
        try:
            self._csv_file.flush()
            self._csv_file.close()
        except Exception:
            pass

    @staticmethod
    def pressure_to_resistance_placeholder(p_mmhg):
        p = max(float(p_mmhg), 0.0)
        return R_MIN_OHM + (R_MAX_OHM - R_MIN_OHM) / (1.0 + (p / P50_MMHG) ** GAMMA)

    @staticmethod
    def resistance_to_adc_placeholder(r_ohm):
        vout = VCC * R_FIXED_OHM / (r_ohm + R_FIXED_OHM)
        adc = round(vout / VCC * ADC_MAX)
        adc = max(0, min(4095, adc))
        return vout, adc

    def onAnimateBeginEvent(self, event):
        t = float(self.root.time.value)
        alpha = min(max(t / self.ramp_time_s, 0.0), 1.0)
        # cosine ramp to avoid numerical shock
        alpha = 0.5 - 0.5 * math.cos(math.pi * alpha)
        force_N = self.max_force_N * alpha
        self.forcefield.totalForce.value = [0.0, 0.0, -force_N]

    def onAnimateEndEvent(self, event):
        t = float(self.root.time.value)
        fz = abs(float(self.forcefield.totalForce.value[2]))
        pressure_pa = fz / PATCH_AREA_M2 if PATCH_AREA_M2 > 0 else 0.0
        pressure_mmhg = pressure_pa / PA_PER_MMHG

        try:
            pos = self.dofs.position.value
            zs = [float(p[2]) for p in pos]
            mean_z = sum(zs) / len(zs)
            min_z = min(zs)
        except Exception:
            mean_z = float("nan")
            min_z = float("nan")

        r_ohm = self.pressure_to_resistance_placeholder(pressure_mmhg)
        vout, adc = self.resistance_to_adc_placeholder(r_ohm)

        self._writer.writerow([
            f"{t:.6f}",
            f"{fz:.6f}",
            f"{pressure_pa:.6f}",
            f"{pressure_mmhg:.6f}",
            f"{mean_z:.6f}",
            f"{min_z:.6f}",
            f"{r_ohm:.3f}",
            f"{vout:.6f}",
            int(adc),
        ])
        self._csv_file.flush()


def createScene(rootNode):
    rootNode.addObject("RequiredPlugin", pluginName=[
        "Sofa.Component.AnimationLoop",
        "Sofa.Component.Constraint.Projective",
        "Sofa.Component.Engine.Select",
        "Sofa.Component.LinearSolver.Iterative",
        "Sofa.Component.Mass",
        "Sofa.Component.MechanicalLoad",
        "Sofa.Component.ODESolver.Backward",
        "Sofa.Component.SolidMechanics.FEM.Elastic",
        "Sofa.Component.StateContainer",
        "Sofa.Component.Topology.Container.Grid",
    ])

    rootNode.name = "VelostatSinglePatchBatch"
    rootNode.gravity = [0.0, 0.0, 0.0]
    rootNode.dt = 0.02
    rootNode.addObject("DefaultAnimationLoop")

    velostat = rootNode.addChild("VelostatPatch_50x50x0p1mm")
    velostat.addObject("EulerImplicitSolver", name="odesolver", rayleighStiffness=0.05, rayleighMass=0.02)
    velostat.addObject("CGLinearSolver", name="linearSolver", iterations=80, tolerance=1e-10, threshold=1e-10)

    velostat.addObject(
        "RegularGridTopology",
        name="grid",
        nx=11,
        ny=11,
        nz=2,
        xmin=-PATCH_W_MM / 2,
        xmax= PATCH_W_MM / 2,
        ymin=-PATCH_H_MM / 2,
        ymax= PATCH_H_MM / 2,
        zmin=0.0,
        zmax=VELOSTAT_THICKNESS_MM,
    )
    dofs = velostat.addObject("MechanicalObject", name="dofs", template="Vec3d")
    velostat.addObject("UniformMass", totalMass=VELOSTAT_MASS_KG)

    velostat.addObject(
        "HexahedronFEMForceField",
        name="VelostatElasticFEM_placeholder",
        youngModulus=VELOSTAT_YOUNG_MODULUS,
        poissonRatio=VELOSTAT_POISSON,
        method="large",
    )

    # Bottom fixed surface: v0 simplification for support/electrode/silicone.
    velostat.addObject(
        "BoxROI",
        name="bottomROI",
        box=[-PATCH_W_MM/2 - 0.1, -PATCH_H_MM/2 - 0.1, -0.001,
             PATCH_W_MM/2 + 0.1,  PATCH_H_MM/2 + 0.1,  0.001],
        drawBoxes=False,
    )
    velostat.addObject("FixedConstraint", indices="@bottomROI.indices")

    # Top selected nodes receive a distributed force.
    velostat.addObject(
        "BoxROI",
        name="topROI",
        box=[-PATCH_W_MM/2 - 0.1, -PATCH_H_MM/2 - 0.1, VELOSTAT_THICKNESS_MM - 0.001,
             PATCH_W_MM/2 + 0.1,  PATCH_H_MM/2 + 0.1, VELOSTAT_THICKNESS_MM + 0.001],
        drawBoxes=False,
    )
    top_load = velostat.addObject(
        "ConstantForceField",
        name="TopDistributedLoad",
        indices="@topROI.indices",
        totalForce=[0.0, 0.0, 0.0],
    )

    scene_dir = Path(__file__).resolve().parent
    project_root = scene_dir.parents[2]
    output_csv = project_root / "simulation" / "sofa" / "outputs" / "single_velostat_patch_batch_timeseries.csv"
    rootNode.addObject(VelostatBatchController(rootNode, top_load, dofs, output_csv))

    return rootNode
