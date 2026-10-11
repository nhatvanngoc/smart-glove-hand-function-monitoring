import sys
import os
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import FreeCAD
import Part

print("=== TEST LATERAL SNAP-PIVOT GEOMETRY ===")

doc = FreeCAD.newDocument("TestSnapPivot")

# Arm on Phalanx 1 (Forward lateral arm with 3 snap holes)
# X at left arm = -14.0mm, thickness 2.0mm (-15.0 to -13.0)
arm_left = Part.makeBox(2.0, 5.0, 12.0, FreeCAD.Vector(-15.0, -2.5, 16.0))
# 3 snap socket holes phi 3.2mm spaced 2.5mm apart along Z
for i in range(3):
    z_hole = 18.5 + i * 2.5
    hole = Part.makeCylinder(1.6, 4.0, FreeCAD.Vector(-16.0, 0, z_hole), FreeCAD.Vector(1, 0, 0))
    # Add a 45-degree lead-in chamfer for smooth snap-in
    lead_in = Part.makeCone(1.6, 2.2, 0.8, FreeCAD.Vector(-13.8, 0, z_hole), FreeCAD.Vector(-1, 0, 0))
    arm_left = arm_left.cut(hole).cut(lead_in)

print("Arm left volume =", arm_left.Volume)

# Stud on Phalanx 2 (Rear lateral lug with outward stud phi 3.0mm x 1.6mm)
# Stud base on lateral side X = -12.8mm, stud extends outward to X = -14.6mm
lug = Part.makeBox(2.0, 5.0, 8.0, FreeCAD.Vector(-12.8, -2.5, -8.0))
stud = Part.makeCylinder(1.5, 1.8, FreeCAD.Vector(-12.8, 0, -5.5), FreeCAD.Vector(-1, 0, 0))
# Chamfer tip of stud
stud_tip = Part.makeCone(1.5, 1.0, 0.6, FreeCAD.Vector(-14.0, 0, -5.5), FreeCAD.Vector(-1, 0, 0))
stud_solid = stud.cut(stud_tip)
lug_complete = lug.fuse(stud).removeSplitter()

print("Lug with outward stud volume =", lug_complete.Volume)
print("=== TEST LATERAL SNAP-PIVOT OK ===")
