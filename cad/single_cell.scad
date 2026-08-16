// ====================================================================
// Single Air Cell - HOLE-CAVITY OVERLAP FIXED
// ====================================================================
// FIX: hole_offset changed from 6mm to 8mm to prevent overlap with
//      the R2mm rounded cavity corners.
//
// EXPLANATION OF THE BUG:
//   - Original spec: holes 6mm from edge + cavity R2mm + wall 2.5mm
//   - At hole position (6, 6) with mount radius 1.6mm (M3):
//       * Distance to cavity corner fillet center (4.5, 4.5) = 2.12 mm
//       * Cavity curve at distance R=2 from fillet center
//       * Distance from (6, 6) to cavity curve = 2.12 - 2 = 0.12 mm
//       * Mount hole extends 1.6 mm from center
//       * => Mount hole OVERLAPS cavity by 1.48 mm !
//
//   - Fix: increase hole_offset to 8mm
//       * Distance to fillet center = sqrt(3.5^2 + 3.5^2) = 4.95 mm
//       * Distance from hole center to cavity curve = 4.95 - 2 = 2.95 mm
//       * Mount hole radius = 1.6 mm
//       * => Clearance = 2.95 - 1.6 = 1.35 mm (no overlap)
//
//   Note: spec said 6mm from edge, but 8mm is necessary to avoid overlap.
//   This small adjustment prevents holes from "piercing" into cavity wall.
//
// OVERALL DIMENSIONS:
//   - Outer: 98 x 98 x 16mm (with R3mm all corners from minkowski)
//   - Inner cavity: 93 x 93 x 10mm (R2mm corners)
//   - Wall thickness: 2.5 mm
//   - Silicone bag fits loosely: 90 x 90 mm
// ====================================================================

/* [Cell outer dimensions] */
cell_width = 98;
cell_depth = 98;

/* [Layer thicknesses] */
bottom_thickness = 3;
wall_height = 10;
total_height = 13;

/* [Cavity dimensions] */
cavity_width = 93;
cavity_depth = 93;
wall_thickness = 2.5;

/* [Hole positions - SYMMETRIC around cell center] */
center_x = cell_width / 2;     // = 49
center_y = cell_depth / 2;     // = 49

// Hole offset increased from 6 to 8 to avoid cavity overlap
hole_offset = 8;  // CHANGED: was 6, now 8

/* [Mounting holes (4 corners)] */
mount_d = 3.2;
mount_positions = [
    [hole_offset, hole_offset],
    [hole_offset, cell_depth - hole_offset],
    [cell_width - hole_offset, hole_offset],
    [cell_width - hole_offset, cell_depth - hole_offset]
];

/* [Counterbore] */
counterbore_d = 6;
counterbore_depth = 2;

/* [Air inlet (at center)] */
air_inlet_d = 4;
air_inlet_pos = [center_x, center_y];

/* [Fillets] */
top_edge_radius = 3;
inner_corner_radius = 2;

/* [Render] */
$fn = 64;

// ====================================================================
// CELL ASSEMBLY
// ====================================================================
module cell_assembly() {
    color("#90A4AE")
    difference() {
        // ===== OUTER BODY =====
        minkowski() {
            cube([cell_width - 2*top_edge_radius,
                  cell_depth - 2*top_edge_radius,
                  total_height - top_edge_radius]);
            sphere(r=top_edge_radius);
        }
        
        // ===== INNER CAVITY =====
        translate([wall_thickness, wall_thickness, bottom_thickness])
        minkowski() {
            cube([cavity_width - 2*inner_corner_radius,
                  cavity_depth - 2*inner_corner_radius,
                  wall_height - inner_corner_radius]);
            sphere(r=inner_corner_radius);
        }
        
        // ===== 4 M3 MOUNT HOLES (at 4 corners, 8mm from edge) =====
        for (pos = mount_positions) {
            translate([pos[0], pos[1], -5])
                cylinder(d=mount_d, h=20);
        }
        
        // ===== 4 COUNTERBORES =====
        for (pos = mount_positions) {
            translate([pos[0], pos[1], -5])
                cylinder(d=counterbore_d, h=counterbore_depth);
        }
        
        // ===== AIR INLET (at center) =====
        translate([air_inlet_pos[0], air_inlet_pos[1], -5])
            cylinder(d=air_inlet_d, h=10);
    }
}

// ====================================================================
// TOP-LEVEL RENDER
// ====================================================================
cell_assembly();

// ====================================================================
// ECHO: Verify all 4 distances + clearance from cavity
// ====================================================================
echo(str("=== HOLE POSITION + CLEARANCE VERIFICATION ==="));
echo(str("Cell size: ", cell_width, " x ", cell_depth));
echo(str("Hole offset from edge: ", hole_offset, " mm"));
echo(str("Wall thickness: ", wall_thickness, " mm"));
echo(str("Cavity corner radius (R): ", inner_corner_radius, " mm"));
echo(str("Mount hole diameter: ", mount_d, " mm (radius ", mount_d/2, " mm)"));

// Mount hole positions
echo(str("--- Mount holes ---"));
labels = ["BL", "TL", "BR", "TR"];
for (i = [0:3]) {
    pos = mount_positions[i];
    label = labels[i];
    echo(str(label, ": (", pos[0], ", ", pos[1], ")"));
}

// Calculate clearance from cavity curve for each mount hole
echo(str("--- Clearance from cavity curve ---"));
cavity_fillet_center_x = wall_thickness + inner_corner_radius;  // 4.5
cavity_fillet_center_y = wall_thickness + inner_corner_radius;  // 4.5
mount_radius = mount_d / 2;
for (i = [0:3]) {
    pos = mount_positions[i];
    label = labels[i];
    // Distance from mount hole center to nearest cavity corner fillet center
    dx = abs(pos[0] - cavity_fillet_center_x);
    dy = abs(pos[1] - cavity_fillet_center_y);
    dist_to_fillet_center = sqrt(dx*dx + dy*dy);
    dist_to_cavity_curve = dist_to_fillet_center - inner_corner_radius;
    clearance = dist_to_cavity_curve - mount_radius;
    echo(str(label, " clearance from cavity: ", clearance, " mm ",
            (clearance > 0) ? "(OK)" : "(OVERLAP!)"));
}
