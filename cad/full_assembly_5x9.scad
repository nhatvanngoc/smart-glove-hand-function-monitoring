// ====================================================================
// FULL ASSEMBLY - FINAL 5x9 MATRIX, 50x50 VELOSTAT PATCHES
// ====================================================================
// Stack, bottom -> top:
//   z=0-20:   support frame
//   z=8-23:   45 valve brackets
//   z=8-20:   45 solenoid valves
//   z=24-40:  45 air tubes through baseplate
//   z=32-40:  PETG baseplate, 45 tube holes
//   z=40-53:  printed cell holder/frame, 98x98 mm
//   z=43+:    silicone air bag inside holder, 90x90 mm
//   top:      copper/Velostat/copper sensing patch, 50x50 mm
// ====================================================================

// [View]
view_mode = 0; // [0:Full, 1:Exploded]

// [Show layers]
show_frame     = true;
show_brackets  = true;
show_valves    = true;
show_baseplate = true;
show_tubes     = true;
show_cells     = true;
show_velostat  = true;
show_manifold  = true;
show_patient   = true;

// [Inflation]
inflate = 0.7; // 0=deflated, 1=max

// [Final matrix]
cols = 5;                 // across body: left -> right
rows = 9;                 // along body: shoulder -> upper thigh
cell_outer = 98;
cell_pitch = 100;
cell_gap = cell_pitch - cell_outer;
cell_margin = cell_gap / 2;
cell_center = cell_outer / 2;

// [Velostat]
velostat_size = 50;
copper_size = 44;

// [Baseplate]
baseplate_thickness = 8;
cushion_w = cols * cell_pitch;
cushion_d = rows * cell_pitch;

// [Render quality]
$fn = 32;

// ====================================================================
// HELPERS
// ====================================================================
function cell_x(c) = c * cell_pitch + cell_margin;
function cell_y(r) = r * cell_pitch + cell_margin;
function hole_x(c) = c * cell_pitch + cell_pitch / 2;
function hole_y(r) = r * cell_pitch + cell_pitch / 2;

// ====================================================================
// FRAME
// ====================================================================
module frame() {
    color("#B0BEC5") {
        translate([0, 0, 0]) cube([cushion_w, 20, 20]);
        translate([0, cushion_d - 20, 0]) cube([cushion_w, 20, 20]);
        translate([0, 0, 0]) cube([20, cushion_d, 20]);
        translate([cushion_w - 20, 0, 0]) cube([20, cushion_d, 20]);
        translate([cushion_w/2 - 10, 0, 0]) cube([20, cushion_d, 20]);
        translate([0, cushion_d/2 - 10, 0]) cube([cushion_w, 20, 20]);
    }
}

// ====================================================================
// VALVE BRACKET
// ====================================================================
module single_bracket() {
    color("#37474F")
    difference() {
        cube([30, 30, 15]);
        translate([15, 15, -1]) cylinder(d=16, h=17);
        translate([4, 4, -1]) cylinder(d=3.2, h=17);
        translate([4, 26, -1]) cylinder(d=3.2, h=17);
        translate([26, 4, -1]) cylinder(d=3.2, h=17);
        translate([26, 26, -1]) cylinder(d=3.2, h=17);
    }
}

module all_brackets() {
    for (r = [0:rows-1])
    for (c = [0:cols-1])
        translate([hole_x(c) - 15, hole_y(r) - 15, 8])
            single_bracket();
}

// ====================================================================
// SOLENOID VALVES
// ====================================================================
module all_valves() {
    color("#1976D2")
    for (r = [0:rows-1])
    for (c = [0:cols-1])
        translate([hole_x(c), hole_y(r), 8])
            cylinder(d=16, h=12);
}

// ====================================================================
// AIR TUBES THROUGH BASEPLATE
// ====================================================================
module all_tubes() {
    color("#42A5F5")
    for (r = [0:rows-1])
    for (c = [0:cols-1])
        translate([hole_x(c), hole_y(r), 24])
            cylinder(d=4, h=18);
}

// ====================================================================
// BASEPLATE
// ====================================================================
module baseplate() {
    color("#78909C")
    difference() {
        cube([cushion_w, cushion_d, baseplate_thickness]);
        for (r = [0:rows-1])
        for (c = [0:cols-1])
            translate([hole_x(c), hole_y(r), -1])
                cylinder(d=4, h=baseplate_thickness + 2);
    }
}

// ====================================================================
// PRINTED CELL HOLDER + SILICONE BAG
// ====================================================================
module cell_holder() {
    // Simplified visual version of single_cell.scad.
    // Detailed rounded model remains in cad/single_cell.scad.
    color("#F9A825")
    difference() {
        cube([98, 98, 13]);
        translate([2.5, 2.5, 3]) cube([93, 93, 12]);
        translate([49, 49, -1]) cylinder(d=4, h=16);
    }
}

module silicone_bag(inf) {
    bag_h = 15 + 12 * inf;
    color("#A5D6F9", 0.65)
    translate([4, 4, 3])
        cube([90, 90, bag_h]);
}

module single_cell_stack(inf) {
    cell_holder();
    silicone_bag(inf);
}

module all_cells(inf) {
    for (r = [0:rows-1])
    for (c = [0:cols-1])
        translate([cell_x(c), cell_y(r), 40])
            single_cell_stack(inf);
}

// ====================================================================
// VELOSTAT + COPPER SANDWICH SENSOR PATCH
// ====================================================================
module sensor_patch(inf) {
    bag_h = 15 + 12 * inf;
    z0 = 40 + 3 + bag_h + 0.2;
    x0 = (cell_outer - velostat_size) / 2;
    y0 = (cell_outer - velostat_size) / 2;
    cx0 = (cell_outer - copper_size) / 2;
    cy0 = (cell_outer - copper_size) / 2;

    // lower copper electrode
    color("#D7A13B")
    translate([cx0, cy0, z0])
        cube([copper_size, copper_size, 0.25]);

    // Velostat patch, 50x50 mm
    color("#212121")
    translate([x0, y0, z0 + 0.35])
        cube([velostat_size, velostat_size, 0.35]);

    // upper copper electrode
    color("#D7A13B")
    translate([cx0, cy0, z0 + 0.8])
        cube([copper_size, copper_size, 0.25]);

    // simple wire tail routed toward the rear gap
    color("#D7A13B")
    translate([cell_outer/2 - 3, cell_outer - 2, z0 + 0.9])
        cube([6, 18, 0.25]);
}

module all_velostat(inf) {
    for (r = [0:rows-1])
    for (c = [0:cols-1])
        translate([cell_x(c), cell_y(r), 0])
            sensor_patch(inf);
}

// ====================================================================
// MANIFOLD - 1 inlet to 45 outlets
// ====================================================================
module manifold(x_off) {
    manifold_w = 180;
    manifold_d = 160;
    color("#9E9E9E")
    translate([x_off, 80, 30])
    difference() {
        cube([manifold_w, manifold_d, 30]);
        translate([3, 3, 3]) cube([manifold_w - 6, manifold_d - 6, 24]);
    }

    // blue pump inlet
    color("#1976D2")
    translate([x_off - 5, 80 + manifold_d/2, 45])
        rotate([0, 90, 0]) cylinder(d=8, h=10);

    // red 45 outlets to solenoid valves
    color("#D32F2F")
    for (r = [0:rows-1])
    for (c = [0:cols-1])
        translate([x_off + 20 + c * 32,
                   92 + r * 15,
                   60])
            cylinder(d=4, h=5);
}

// ====================================================================
// PATIENT BLOCK - simplified body contact zone
// ====================================================================
module patient() {
    color("#FFCCBC", 0.55)
    translate([cushion_w * 0.22, cushion_d * 0.15, 72])
        cube([cushion_w * 0.56, cushion_d * 0.70, 120]);
}

// ====================================================================
// TOP-LEVEL RENDER
// ====================================================================
if (view_mode == 0) {
    if (show_frame)      frame();
    if (show_brackets)   all_brackets();
    if (show_valves)     all_valves();
    if (show_tubes)      all_tubes();
    if (show_baseplate)  translate([0, 0, 32]) baseplate();
    if (show_cells)      all_cells(inflate);
    if (show_velostat)   all_velostat(inflate);
    if (show_manifold)   manifold(-230);
    if (show_patient)    patient();
}

if (view_mode == 1) {
    EX = 35;
    if (show_frame)      frame();
    if (show_brackets)   all_brackets();
    if (show_valves)     translate([0, 0, EX]) all_valves();
    if (show_tubes)      translate([0, 0, EX*1.5]) all_tubes();
    if (show_baseplate)  translate([0, 0, EX*2 + 32]) baseplate();
    if (show_cells)      translate([0, 0, EX*2.5]) all_cells(inflate);
    if (show_velostat)   translate([0, 0, EX*3]) all_velostat(inflate);
    if (show_patient)    translate([0, 0, EX*3 + 5]) patient();
    if (show_manifold)   translate([0, 0, EX]) manifold(-230);
}
