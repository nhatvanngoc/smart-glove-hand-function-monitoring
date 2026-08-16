// ====================================================================
// BASEPLATE - FINAL 5x9 MATRIX, 45 TUBE HOLES
// ====================================================================
// Final cushion matrix:
//   5 columns across body, 9 rows along body
//   98x98 mm cells on 100 mm pitch
//   baseplate size = 500 x 900 mm
//
// Render modes:
//   view_mode = 0: full baseplate
//   view_mode = 1: one row strip, 500 x 100 mm
//   view_mode = 2: one 5x3 section, 500 x 300 mm
// ====================================================================

view_mode = 0;      // [0:Full 5x9, 1:Single row strip, 2:5x3 section]
row_to_show = 0;    // [0:8]
section_to_show = 0;// [0:2]

cols = 5;
rows = 9;
cell_pitch = 100;
plate_thickness = 8;
cell_hole_d = 4;
mount_hole_d = 3.2;

plate_width = cols * cell_pitch;
plate_depth = rows * cell_pitch;

$fn = 32;

function hole_x(c) = c * cell_pitch + cell_pitch / 2;
function hole_y(r) = r * cell_pitch + cell_pitch / 2;

module tube_hole_at(c, r) {
    translate([hole_x(c), hole_y(r), -1])
        cylinder(d=cell_hole_d, h=plate_thickness + 2);
}

module full_baseplate() {
    difference() {
        cube([plate_width, plate_depth, plate_thickness]);
        for (r = [0:rows-1])
        for (c = [0:cols-1])
            tube_hole_at(c, r);
    }
}

module row_strip(row_id) {
    difference() {
        cube([plate_width, cell_pitch, plate_thickness]);
        for (c = [0:cols-1])
            translate([hole_x(c), cell_pitch/2, -1])
                cylinder(d=cell_hole_d, h=plate_thickness + 2);
    }
}

module section_5x3(section_id) {
    difference() {
        cube([plate_width, 3 * cell_pitch, plate_thickness]);
        for (rr = [0:2])
        for (c = [0:cols-1])
            translate([hole_x(c), rr * cell_pitch + cell_pitch/2, -1])
                cylinder(d=cell_hole_d, h=plate_thickness + 2);
    }
}

// ====================================================================
// TOP-LEVEL RENDER
// ====================================================================
if (view_mode == 0) {
    full_baseplate();
}
if (view_mode == 1) {
    row_strip(row_to_show);
}
if (view_mode == 2) {
    section_5x3(section_to_show);
}
