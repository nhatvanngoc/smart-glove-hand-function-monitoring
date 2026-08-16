// ====================================================================
// Valve Bracket - Single + Array modes
// ====================================================================
// PURPOSE: Mount solenoid valve (16mm dia) to aluminum frame below cushion
//
// DESIGN (FIXED):
//   - 4 mount holes (M3) are THROUGH-HOLES (visible from both top & bottom)
//   - 1 valve stem hole in CENTER (only top portion, 12mm depth)
//   - Screws can come from either top OR bottom of bracket
//
// USAGE:
//   - Open in OpenSCAD, F5/F6
//   - Customizer -> view_mode:
//       0 = Single bracket (centered at origin)
//       1 = 4x4 array (16 brackets)
// ====================================================================

/* [View] */
view_mode = 0; // [0:Single bracket, 1:4x4 array (16 pieces)]

/* [Bracket dimensions] */
bracket_width = 30;
bracket_depth = 30;
bracket_height = 15;

/* [Holes] */
valve_d = 16;   // valve stem diameter (16mm)
mount_d = 3.2;  // M3 screw clearance (3.2mm)

/* [Render] */
$fn = 32;

// ====================================================================
// SINGLE BRACKET MODULE
// ====================================================================
module valve_bracket() {
    difference() {
        // Main body (centered at origin, from z=0 to z=bracket_height)
        translate([-bracket_width/2, -bracket_depth/2, 0])
            cube([bracket_width, bracket_depth, bracket_height]);
        
        // === CENTRAL VALVE STEM HOLE ===
        // From z=3 (above base) to z=bracket_height (top)
        // This is where the valve sits - only TOP portion is hollow
        translate([0, 0, 3])
            cylinder(d=valve_d, h=bracket_height);
        
        // === 4 MOUNT HOLES (M3) - THROUGH-HOLES ===
        // From z=-1 (below base) to z=bracket_height+1 (above top)
        // Visible from BOTH top and bottom
        translate([-bracket_width/2 + 4, -bracket_depth/2 + 4, -1])
            cylinder(d=mount_d, h=bracket_height + 2);
        translate([-bracket_width/2 + 4,  bracket_depth/2 - 4, -1])
            cylinder(d=mount_d, h=bracket_height + 2);
        translate([ bracket_width/2 - 4, -bracket_depth/2 + 4, -1])
            cylinder(d=mount_d, h=bracket_height + 2);
        translate([ bracket_width/2 - 4,  bracket_depth/2 - 4, -1])
            cylinder(d=mount_d, h=bracket_height + 2);
    }
}

// ====================================================================
// TOP-LEVEL RENDER
// ====================================================================
if (view_mode == 0) {
    // SINGLE - centered at origin
    color("#37474F") valve_bracket();
}
if (view_mode == 1) {
    // 4x4 ARRAY - 16 pieces
    color("#37474F")
    for (r = [0, 1, 2, 3])
    for (c = [0, 1, 2, 3])
        translate([(c - 1.5) * 40, (r - 1.5) * 40, 0])
            valve_bracket();
}
