import sys
import os
import io
import math

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import FreeCAD
import Part

print("=== TEST MULTI-STEP RATCHET AND MULTI-DETENT SLOT ===")

def make_detent_slot_cutter(r_detent, r_waist, num_steps, step_pitch, p_start, dir_slot, dir_pin):
    total_len = (num_steps - 1) * step_pitch
    # 1. Waist corridor
    b_waist = Part.makeBox(24.0, 2 * r_waist, total_len, p_start - dir_pin * 12.0 - FreeCAD.Vector(0, r_waist, 0))
    cutter = b_waist
    # 2. Add circular detents at each step
    for i in range(num_steps):
        p_step = p_start + dir_slot * (i * step_pitch)
        c = Part.makeCylinder(r_detent, 24.0, p_step - dir_pin * 12.0, dir_pin)
        cutter = cutter.fuse(c)
    return cutter.removeSplitter()

# Test creating a fork with the detent slot cutter
doc = FreeCAD.newDocument("TestDetent")
fork_left = Part.makeBox(2.6, 5.4, 12.0, FreeCAD.Vector(-6.7, 10.0, 16.0))
fork_right = Part.makeBox(2.6, 5.4, 12.0, FreeCAD.Vector(4.1, 10.0, 16.0))
fork_solid = fork_left.fuse(fork_right)

cutter = make_detent_slot_cutter(
    r_detent=1.35, r_waist=1.1, num_steps=4, step_pitch=2.0,
    p_start=FreeCAD.Vector(0, 12.7, 18.5),
    dir_slot=FreeCAD.Vector(0, 0, 1),
    dir_pin=FreeCAD.Vector(1, 0, 0)
)
fork_with_slots = fork_solid.cut(cutter).removeSplitter()
print("Fork with 4-detent slots created successfully, volume =", fork_with_slots.Volume)
