// ====================================================================
// Pneumatic Manifold (1 inlet -> 64 outlets)
// ====================================================================

/* [Manifold] */
body_width = 200;
body_depth = 100;
body_height = 30;
wall = 3;
inlet_d = 8;
outlet_d = 4;
n_cols = 8;
n_rows = 8;

module manifold_body() {
    difference() {
        cube([body_width, body_depth, body_height]);
        translate([wall, wall, wall])
            cube([body_width - 2*wall, body_depth - 2*wall, body_height - wall]);
    }
}

module manifold_inlet() {
    translate([-1, body_depth/2, body_height/2])
        rotate([0, 90, 0])
            cylinder(d=inlet_d, h=wall + 2);
}

module manifold_outlets() {
    outlet_w = (body_width - 2*wall) / n_cols;
    outlet_h = (body_depth - 2*wall) / n_rows;
    for (r = [0, 1, 2, 3, 4, 5, 6, 7])
    for (c = [0, 1, 2, 3, 4, 5, 6, 7])
        translate([wall + (c + 0.5) * outlet_w,
                   wall + (r + 0.5) * outlet_h,
                   body_height - 1])
            cylinder(d=outlet_d, h=5);
}

// ====================================================================
// TOP-LEVEL RENDER (inlet=blue, outlets=red for clarity)
// ====================================================================
color("#9E9E9E") manifold_body();
color("#1976D2") manifold_inlet();
color("#D32F2F") manifold_outlets();
