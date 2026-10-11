import sys
import os
import io
import math

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import FreeCAD
import Part

print("=== TEST 5-STEP RATCHET RACK & CLAW ===")

rx = 11.8 + 1.7 # ~13.5mm
length_z = 16.0
num_steps = 5
step_pitch = 1.2

# Ratchet rack on dorsal shell
rack_len_y = num_steps * step_pitch + 1.8
rack_base = Part.makeBox(2.4, rack_len_y, length_z, FreeCAD.Vector(rx, 0.0, 0.0))

cutter_all = None
for i in range(num_steps):
    y_tooth = 0.6 + i * step_pitch
    # Cut a ratchet notch: 1.8mm wide along X, 0.8mm deep along Y
    groove = Part.makeBox(2.2, 0.75, length_z + 2.0, FreeCAD.Vector(rx + 0.5, y_tooth, -1.0))
    if cutter_all is None:
        cutter_all = groove
    else:
        cutter_all = cutter_all.fuse(groove)

rack_with_teeth = rack_base.cut(cutter_all).removeSplitter()
print("Ratchet rack with 5 teeth created, volume =", rack_with_teeth.Volume)

# Claw on swing arm
knuckle_height = 10.8
knuckle_z_min = 2.6
snap_arm_out = Part.makeBox(1.6, rack_len_y + 1.5, knuckle_height, FreeCAD.Vector(rx + 2.5, -1.5, knuckle_z_min))
tooth_claw = Part.makeBox(1.5, 1.0, knuckle_height, FreeCAD.Vector(rx + 1.0, 0.6, knuckle_z_min))
bridge_r = Part.makeBox(3.0, 1.8, knuckle_height, FreeCAD.Vector(rx - 0.5, -1.8, knuckle_z_min))
thumb_tab = Part.makeBox(3.8, 2.4, knuckle_height, FreeCAD.Vector(rx + 3.5, rack_len_y - 1.0, knuckle_z_min))

claw_solid = snap_arm_out.fuse(tooth_claw).fuse(bridge_r).fuse(thumb_tab).removeSplitter()
print("Claw with thumb release created, volume =", claw_solid.Volume)
