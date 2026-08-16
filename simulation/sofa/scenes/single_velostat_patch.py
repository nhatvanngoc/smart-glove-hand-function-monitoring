# -*- coding: utf-8 -*-
"""
SOFA single Velostat patch scene - first serious mechanical/electrical coupling step.

Run from project root in WSL/Linux:
    runSofa -l SofaImGui -g imgui -l SofaPython3 simulation/sofa/scenes/single_velostat_patch.py

Purpose:
    1. Create a 50 x 50 x 0.1 mm Velostat layer as a deformable hexahedral slab.
    2. Apply a controlled vertical load to the top surface.
    3. Export pressure proxy, deformation, placeholder R(P), Vout and ADC.

Important:
    This is v0: force-controlled single-patch model.
    Datasheet has geometry/resistivity, but no full pressure-resistance curve.
    Therefore R(P) below is a placeholder and must be replaced by calibration data.
"""

from __future__ import annotations

import csv
import math
import os
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

# Initial Velostat mechanical placeholders.
# These are NOT from the provided datasheet. They are placeholders for v0.
# They must be justified/replaced by material tests or literature values later.
VELOSTAT_YOUNG_MODULUS = 5.0e6
VELOSTAT_POISSON = 0.35
VELOSTAT_MASS_KG = 0.00030

# Force ramp: 2.0 N on 50x50 mm => about 6.0 mmHg.
# Increase max_force_N in the controller if you want higher pressure.
DEFAULT_MAX_FORCE_N = 18.0  # 18 N on 50x50 mm => about 54 mmHg
DEFAULT_RAMP_TIME_S = 4.0

# Placeholder electrical model, same family as previous Python simulator.
VCC = 3.3
ADC_MAX = 4095.0
R_FIXED_OHM = 47_000.0
R_MAX_OHM = 900_000.0
R_MIN_OHM = 4_000.0
P50_MMHG = 32.0
GAMMA = 1.45


class VelostatPatchController(Sofa.Core.Controller):
    """Update load and export a pressure/electrical time series."""

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

    def __del__(self):
        try:
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
        # Smooth ramp to avoid numerical shock.
        alpha = min(max(t / self.ramp_time_s, 0.0), 1.0)
        alpha = 0.5 - 0.5 * math.cos(math.pi * alpha)
        force_N = self.max_force_N * alpha

        # ConstantForceField totalForce is applied over its selected top nodes.
        self.forcefield.totalForce.value = [0.0, 0.0, -force_N]

    def onAnimateEndEvent(self, event):
        t = float(self.root.time.value)
        fz = abs(float(self.forcefield.totalForce.value[2]))
        pressure_pa = fz / PATCH_AREA_M2 if PATCH_AREA_M2 > 0 else 0.0
        pressure_mmhg = pressure_pa / PA_PER_MMHG

        # Mean deformation proxy from mechanical DOFs.
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


def add_visual_obj(parent, name, filename, color):
    node = parent.addChild(name)
    node.addObject("MeshOBJLoader", name="loader", filename=str(filename))
    node.addObject("OglModel", name="visual", src="@loader", color=color)
    return node


def createScene(rootNode):
    # -----------------------------------------------------------------
    # Plugins. Keep explicit for SOFA 25.x conda packages.
    # -----------------------------------------------------------------
    rootNode.addObject("RequiredPlugin", pluginName=[
        "Sofa.Component.AnimationLoop",
        "Sofa.Component.Constraint.Projective",
        "Sofa.Component.Engine.Select",
        "Sofa.Component.LinearSolver.Iterative",
        "Sofa.Component.Mass",
        "Sofa.Component.ODESolver.Backward",
        "Sofa.Component.SolidMechanics.FEM.Elastic",
        "Sofa.Component.SolidMechanics.Spring",
        "Sofa.Component.StateContainer",
        "Sofa.Component.Topology.Container.Grid",
        "Sofa.Component.IO.Mesh",
        "Sofa.GL.Component.Rendering3D",
    ])

    rootNode.name = "VelostatSinglePatch"
    rootNode.gravity = [0.0, 0.0, 0.0]
    rootNode.dt = 0.02

    rootNode.addObject("DefaultAnimationLoop")
    rootNode.addObject("VisualStyle", displayFlags="showBehaviorModels showForceFields showVisualModels")

    # -----------------------------------------------------------------
    # Visual context: silicone support, copper electrodes and load plate.
    # These are visual aids in v0. Mechanical model is Velostat slab.
    # -----------------------------------------------------------------
    scene_dir = Path(__file__).resolve().parent
    assets = scene_dir.parent / "assets"
    add_visual_obj(rootNode, "SiliconeSupportVisual", assets / "silicone_support_90x90x15.obj", [0.4, 0.8, 1.0, 0.35])
    add_visual_obj(rootNode, "LowerCopperVisual", assets / "copper_bottom_44x44.obj", [0.84, 0.45, 0.10, 1.0])
    add_visual_obj(rootNode, "UpperCopperVisual", assets / "copper_top_44x44.obj", [0.84, 0.45, 0.10, 1.0])
    add_visual_obj(rootNode, "RigidLoadPlateVisual", assets / "indenter_50x50.obj", [0.75, 0.75, 0.75, 0.65])

    # -----------------------------------------------------------------
    # Deformable Velostat patch.
    # Coordinates are in mm. Thickness is 0.1 mm from datasheet.
    # -----------------------------------------------------------------
    velostat = rootNode.addChild("VelostatPatch_50x50x0p1mm")
    velostat.addObject("EulerImplicitSolver", name="odesolver", rayleighStiffness=0.05, rayleighMass=0.02)
    velostat.addObject("CGLinearSolver", name="linearSolver", iterations=80, tolerance=1e-10, threshold=1e-10)

    velostat.addObject(
        "RegularGridTopology",
        name="grid",
        nx=11,
        ny=11,
        nz=2,
        xmin=-PATCH_W_MM/2,
        xmax= PATCH_W_MM/2,
        ymin=-PATCH_H_MM/2,
        ymax= PATCH_H_MM/2,
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

    # Fix bottom surface to mimic support from lower electrode/silicone in v0.
    velostat.addObject(
        "BoxROI",
        name="bottomROI",
        box=[-PATCH_W_MM/2 - 0.1, -PATCH_H_MM/2 - 0.1, -0.001,
             PATCH_W_MM/2 + 0.1,  PATCH_H_MM/2 + 0.1,  0.001],
        drawBoxes=True,
    )
    velostat.addObject("FixedConstraint", indices="@bottomROI.indices")

    # Select top surface and apply controlled load.
    velostat.addObject(
        "BoxROI",
        name="topROI",
        box=[-PATCH_W_MM/2 - 0.1, -PATCH_H_MM/2 - 0.1, VELOSTAT_THICKNESS_MM - 0.001,
             PATCH_W_MM/2 + 0.1,  PATCH_H_MM/2 + 0.1, VELOSTAT_THICKNESS_MM + 0.001],
        drawBoxes=True,
    )
    top_load = velostat.addObject(
        "ConstantForceField",
        name="TopDistributedLoad",
        indices="@topROI.indices",
        totalForce=[0.0, 0.0, 0.0],
    )

    # -----------------------------------------------------------------
    # Controller: ramp load, export pressure and placeholder electrical data.
    # -----------------------------------------------------------------
    project_root = scene_dir.parents[2]
    output_csv = project_root / "simulation" / "sofa" / "outputs" / "single_velostat_patch_timeseries.csv"
    rootNode.addObject(VelostatPatchController(rootNode, top_load, dofs, output_csv))

    return rootNode
