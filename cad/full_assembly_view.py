"""
3D Visualization — Velostat DRAPE on top of cells
====================================================
Show new design with Velostat patches on top, draping over inflated cells.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

OUT = Path(__file__).resolve().parent / "drawings"
OUT.mkdir(parents=True, exist_ok=True)


def draw_box(ax, x, y, z, dx, dy, dz, color, alpha=1.0):
    v = np.array([[x, y, z], [x+dx, y, z], [x+dx, y+dy, z], [x, y+dy, z],
                  [x, y, z+dz], [x+dx, y, z+dz], [x+dx, y+dy, z+dz], [x, y+dy, z+dz]])
    faces = [[v[0], v[1], v[2], v[3]], [v[4], v[5], v[6], v[7]],
             [v[0], v[1], v[5], v[4]], [v[2], v[3], v[7], v[6]],
             [v[1], v[2], v[6], v[5]], [v[0], v[3], v[7], v[4]]]
    ax.add_collection3d(Poly3DCollection(faces, facecolors=color, alpha=alpha,
                                          edgecolor="black", linewidth=0.2))


def draw_cylinder(ax, cx, cy, cz, r, h, color, alpha=0.8):
    n = 16
    theta = np.linspace(0, 2*np.pi, n)
    z_top, z_bot = cz + h, cz
    for i in range(n):
        j = (i + 1) % n
        x0, x1 = cx + r*np.cos(theta[i]), cx + r*np.cos(theta[j])
        y0, y1 = cy + r*np.sin(theta[i]), cy + r*np.sin(theta[j])
        v = [[x0, y0, z_bot], [x1, y1, z_bot], [x1, y1, z_top], [x0, y0, z_top]]
        ax.add_collection3d(Poly3DCollection([v], facecolors=color, alpha=alpha,
                                                edgecolor="black", linewidth=0.2))
    for z_cap in [z_bot, z_top]:
        verts = [[cx + r*np.cos(t), cy + r*np.sin(t), z_cap] for t in theta]
        ax.add_collection3d(Poly3DCollection([verts], facecolors=color, alpha=alpha,
                                                edgecolor="black", linewidth=0.2))


def draw_draped_velostat(ax, cx, cy, base_z, inflate_h, color="#212121"):
    """
    Velostat patch 50x50mm, draped over inflated cell.
    Uses parabolic-like shape: 4 corners at lower z, center at higher z.
    """
    patch_w = 50
    n = 10
    # Top surface (dome): center higher, edges lower
    z_top = base_z + inflate_h + 0.5
    z_corner = base_z + inflate_h * 0.3  # corners sag down
    
    # Generate dome surface as grid of points
    x = np.linspace(cx - patch_w/2, cx + patch_w/2, n)
    y = np.linspace(cy - patch_w/2, cy + patch_w/2, n)
    X, Y = np.meshgrid(x, y)
    # Paraboloid: z = center_z - k*((x-cx)^2 + (y-cy)^2)
    dx_norm = (X - cx) / (patch_w/2)
    dy_norm = (Y - cy) / (patch_w/2)
    r2 = dx_norm**2 + dy_norm**2
    Z = z_top - (z_top - z_corner) * r2
    
    # Plot as surface
    ax.plot_surface(X, Y, Z, color=color, alpha=0.9, edgecolor="none", linewidth=0)


# ====================================================================
# 1. CROSS-SECTION SHOWING DRAPE EFFECT (key visualization)
# ====================================================================
def view_draping_cross_section():
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle("VELOSTAT DRAPE — How patch conforms to inflated cell shape",
                  fontsize=13, fontweight="bold")

    inflate_levels = [0.0, 0.5, 1.0]  # 0=xẹp, 0.5=nửa, 1=max
    titles = ["DEFLATED (inflate=0)", "HALF INFLATED (inflate=0.5)", "FULL INFLATED (inflate=1.0)"]

    for idx, (ax, inf, title) in enumerate(zip(axes, inflate_levels, titles)):
        ax.set_xlim(-50, 150)
        ax.set_ylim(-10, 40)
        ax.set_aspect("equal")
        ax.set_title(title, fontsize=11)
        ax.set_xlabel("Width (mm)")
        ax.set_ylabel("Height (mm)")

        # Base plate
        ax.add_patch(Rectangle((0, 0), 100, 8, facecolor="#90A4AE",
                                 edgecolor="black", linewidth=1.5))

        # Silicone membrane (inflate)
        h = 22 * inf
        if h > 0.5:
            # Outer wall
            ax.add_patch(Rectangle((0, 8), 100, h, facecolor="#FFCC80",
                                     edgecolor="#E65100", linewidth=1))
            # Hollow inside (subtract effect)
            ax.add_patch(Rectangle((1.5, 8), 97, h, facecolor="white",
                                     edgecolor="none", alpha=0.5))
            # Top edge of membrane
            ax.plot([0, 100], [8 + h, 8 + h], color="#E65100", linewidth=1.5)

        # Velostat patch - DRAPE shape
        patch_w = 50
        patch_cx = 50  # center
        # Parabolic shape: 4 corners at base, center lifted
        z_corner = 8 + h * 0.3
        z_center = 8 + h + 0.5
        
        # Draw as a curve
        n_pts = 30
        x_pts = np.linspace(25, 75, n_pts)
        z_pts = z_center - (z_center - z_corner) * ((x_pts - 50) / 25)**2
        
        ax.fill_between(x_pts, z_pts, z_pts + 0.3, color="#212121", alpha=0.9)
        ax.plot(x_pts, z_pts + 0.15, color="white", linewidth=1)

        # Wires from corners (going up)
        if inf > 0.05:
            for wx in [25, 75]:
                ax.plot([wx, wx], [z_corner + 0.3, 50], color="#FF9800",
                        linewidth=1, linestyle="--")

        # Patient above (skin line)
        skin_z = z_center + 1
        ax.plot([10, 90], [skin_z, skin_z], color="#E91E63", linewidth=2.5)
        ax.text(50, skin_z + 1, "Patient skin", ha="center", fontsize=8, color="#E91E63")

        # Annotations
        ax.text(50, -5, "BASEPLATE", ha="center", fontsize=8, color="#37474F", fontweight="bold")
        if h > 0.5:
            ax.text(110, 8 + h/2, f"Silicone\n({h:.0f}mm)", fontsize=7, color="#BF360C")
        ax.annotate("Velostat patch\n(50×50mm, DRAPED)",
                    xy=(50, z_center + 0.3), xytext=(50, 32),
                    fontsize=8, ha="center", color="#212121",
                    arrowprops=dict(arrowstyle="->", color="#212121"))
        ax.text(105, z_corner + 0.5, "corner\n(cố định)", fontsize=7, color="#FF9800", ha="left")
        ax.text(105, z_center + 0.5, "center\n(theo hình)", fontsize=7, color="#212121", ha="left")

        ax.grid(True, alpha=0.2)

    plt.tight_layout()
    plt.savefig(OUT / "velostat_drape_cross_section.png", dpi=150, bbox_inches="tight")
    plt.savefig(OUT / "velostat_drape_cross_section.svg", format="svg")
    plt.close()
    print("Saved: velostat_drape_cross_section.png + .svg")


# ====================================================================
# 2. FULL 3D ASSEMBLY WITH VELOSTAT DRAPE (isometric)
# ====================================================================
def view_assembly_with_drape():
    fig = plt.figure(figsize=(18, 11))
    ax = fig.add_subplot(111, projection="3d")

    inflate = 0.7

    # Frame
    color_frame = "#B0BEC5"
    for x, y in [(0,0), (780,0), (0,980), (780,980)]:
        draw_box(ax, x, y, 0, 20, 20, 20, color_frame, alpha=0.9)
    draw_box(ax, 0, 490, 0, 800, 20, 20, color_frame, alpha=0.9)
    draw_box(ax, 390, 0, 0, 20, 1000, 20, color_frame, alpha=0.9)

    # Brackets
    for qx in [0, 1]:
        for qy in [0, 1]:
            for r in range(4):
                for c in range(4):
                    x = qx*400 + c*100 + 35
                    y = qy*400 + r*100 + 35
                    draw_box(ax, x, y, 8, 30, 30, 15, "#37474F", alpha=0.9)

    # Valves
    for qx in [0, 1]:
        for qy in [0, 1]:
            for r in range(4):
                for c in range(4):
                    x = qx*400 + c*100 + 50
                    y = qy*400 + r*100 + 50
                    draw_cylinder(ax, x, y, 8, 8, 12, "#1976D2", alpha=0.95)

    # Tubes
    for qx in [0, 1]:
        for qy in [0, 1]:
            for r in range(4):
                for c in range(4):
                    x = qx*400 + c*100 + 50
                    y = qy*400 + r*100 + 50
                    draw_cylinder(ax, x, y, 24, 1.5, 16, "#42A5F5", alpha=0.9)

    # Baseplate
    draw_box(ax, 0, 0, 32, 800, 1000, 8, "#78909C", alpha=0.85)

    # Cells (inflated)
    for qx in [0, 1]:
        for qy in [0, 1]:
            for r in range(4):
                for c in range(4):
                    x = qx*400 + c*100
                    y = qy*400 + r*100
                    h = 22 * inflate
                    draw_box(ax, x+1.5, y+1.5, 40, 97, 97, h, "#FFCC80", alpha=0.6)

    # Highlight SACRUM cells
    for r in [3, 4, 5]:
        for c in [3, 4, 5]:
            x = c * 100
            y = r * 100
            h = 22 * inflate
            draw_box(ax, x+1.5, y+1.5, 40, 97, 97, h, "#FF8A65", alpha=0.7)

    # VELOSTAT PATCHES - DRAPED ON TOP
    for qx in [0, 1]:
        for qy in [0, 1]:
            for r in range(4):
                for c in range(4):
                    cx = qx*400 + c*100 + 50
                    cy = qy*400 + r*100 + 50
                    draw_draped_velostat(ax, cx, cy, 40, 22 * inflate)

    # Patient (transparent)
    color_patient = "#FFCDD2"
    draw_box(ax, 300, 350, 62.5, 200, 300, 150, color_patient, alpha=0.3)
    ax.text(500, 500, 140, "PATIENT\n(da)", ha="center", va="center",
            fontsize=11, color="#E91E63", fontweight="bold")

    # Manifold
    draw_box(ax, -250, 0, 30, 200, 100, 30, "#9E9E9E", alpha=0.85)
    draw_cylinder(ax, -255, 50, 45, 4, 10, "#1976D2", alpha=0.95)

    ax.set_xlim(-300, 850)
    ax.set_ylim(-100, 1100)
    ax.set_zlim(0, 230)
    ax.set_xlabel("X (mm)")
    ax.set_ylabel("Y (mm)")
    ax.set_zlabel("Z (mm)")
    ax.set_title("FULL ASSEMBLY — Velostat patches ON TOP, draped over inflated cells\n"
                  "Each cell has its own 50×50mm Velostat patch, conforming to cell shape",
                  fontsize=12, fontweight="bold")
    ax.view_init(elev=20, azim=-55)
    plt.tight_layout()
    plt.savefig(OUT / "full_assembly_with_drape_3d.png", dpi=150, bbox_inches="tight")
    plt.savefig(OUT / "full_assembly_with_drape_3d.svg", format="svg")
    plt.close()
    print("Saved: full_assembly_with_drape_3d.png + .svg")


# ====================================================================
# 3. WIRE ROUTING DIAGRAM (64 Velostat wires)
# ====================================================================
def view_wire_routing():
    fig, ax = plt.subplots(figsize=(14, 11))
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1100)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("WIRE ROUTING — 64 Velostat patches to STM32\n"
                  "Wires run along channels between cells, gather at edges",
                  fontsize=13, fontweight="bold")

    # Frame
    ax.add_patch(Rectangle((100, 50), 800, 1000, fill=False, edgecolor="black", linewidth=2.5))

    # 64 Velostat patches (50×50mm centered in each cell)
    for r in range(8):
        for c in range(8):
            cx = 100 + c*100 + 50
            cy = 50 + r*100 + 50
            # Patch
            color = "#B71C1C" if (3 <= r <= 5 and 3 <= c <= 5) else "#212121"
            ax.add_patch(Rectangle((cx-25, cy-25), 50, 50, facecolor=color,
                                     edgecolor="white", linewidth=1, alpha=0.9))
            cell_id = r * 8 + c
            ax.text(cx, cy, f"{cell_id}", ha="center", va="center",
                    fontsize=8, color="white", fontweight="bold")

    # Wire channels (between cells)
    # Horizontal channels (between rows)
    for r in range(7):
        y = 50 + (r+1) * 100 - 2  # gap between rows
        ax.plot([100, 900], [y, y], color="#FF9800", linewidth=2, linestyle=":")
    # Vertical channels (between cols)
    for c in range(7):
        x = 100 + (c+1) * 100 - 2
        ax.plot([x, x], [50, 1050], color="#FF9800", linewidth=2, linestyle=":")

    # Wires from patches to channels (representative)
    for r in range(8):
        for c in range(8):
            cx = 100 + c*100 + 50
            cy = 50 + r*100 + 50
            # To nearest channel
            if c < 7:
                target_x = 100 + (c+1) * 100 - 2
            else:
                target_x = 100 + c * 100 - 2
            ax.plot([cx + 25 if c < 7 else cx - 25, target_x], [cy, cy],
                    color="#FF9800", linewidth=0.5, alpha=0.7)

    # Wire gathering point (left edge)
    ax.add_patch(Rectangle((20, 480), 80, 140, facecolor="#1976D2",
                             edgecolor="black", linewidth=2))
    ax.text(60, 550, "STM32\n64 wires\nSPI MUX", ha="center", va="center",
            fontsize=11, color="white", fontweight="bold")

    # Show 8 representative wires going to STM32
    for r in [0, 1, 2, 3, 4, 5, 6, 7]:
        y_start = 50 + r * 100 + 50
        ax.plot([60, 100 + 100], [550, y_start], color="#FF9800",
                linewidth=1, alpha=0.5)

    # Legend
    legend_x = 920
    ax.add_patch(Rectangle((legend_x, 1000), 30, 20, facecolor="#212121", edgecolor="black"))
    ax.text(legend_x + 40, 1010, "Velostat patch\n(gần da nhất)", va="center", fontsize=9)
    ax.add_patch(Rectangle((legend_x, 970), 30, 20, facecolor="#B71C1C", edgecolor="black"))
    ax.text(legend_x + 40, 980, "Sacrum patch\n(8 patches)", va="center", fontsize=9)
    ax.plot([legend_x, legend_x + 30], [940, 940], color="#FF9800", linewidth=2, linestyle=":")
    ax.text(legend_x + 40, 940, "Wire channel\n(gap giữa cells)", va="center", fontsize=9)
    ax.add_patch(Rectangle((legend_x, 900), 30, 20, facecolor="#1976D2", edgecolor="black"))
    ax.text(legend_x + 40, 910, "STM32 (collect\nall 64 wires)", va="center", fontsize=9)

    # Notes
    ax.text(500, 30, "Mỗi patch 50×50mm, gắn lỏng ở 4 góc → DRAPE theo hình cell khi inflate",
            ha="center", fontsize=9, color="#212121", style="italic")

    plt.tight_layout()
    plt.savefig(OUT / "velostat_wire_routing.png", dpi=150, bbox_inches="tight")
    plt.savefig(OUT / "velostat_wire_routing.svg", format="svg")
    plt.close()
    print("Saved: velostat_wire_routing.png + .svg")


# ====================================================================
# 4. TOP VIEW WITH VELOSTAT PATCHES
# ====================================================================
def view_top_with_patches():
    fig, ax = plt.subplots(figsize=(14, 11))
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1100)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("TOP VIEW — 64 Velostat patches (50×50mm) on cells\n"
                  "Mỗi patch nằm giữa cell, có 4 góc cố định + drape ở giữa",
                  fontsize=13, fontweight="bold")

    # Frame
    ax.add_patch(Rectangle((100, 50), 800, 1000, fill=False, edgecolor="black", linewidth=2.5))

    # 64 cells (light fill)
    for r in range(8):
        for c in range(8):
            x = 100 + c*100
            y = 50 + r*100
            # Cell outer
            ax.add_patch(Rectangle((x, y), 100, 100, facecolor="#FFE0B2",
                                     edgecolor="#E65100", linewidth=0.5, alpha=0.4))

    # 64 Velostat patches (50×50mm, đen)
    for r in range(8):
        for c in range(8):
            cx = 100 + c*100 + 50
            cy = 50 + r*100 + 50
            is_sacrum = (3 <= r <= 5 and 3 <= c <= 5)
            color = "#B71C1C" if is_sacrum else "#212121"
            ax.add_patch(Rectangle((cx-25, cy-25), 50, 50, facecolor=color,
                                     edgecolor="white", linewidth=1.5, alpha=0.9))
            cell_id = r * 8 + c
            ax.text(cx, cy, str(cell_id), ha="center", va="center",
                    fontsize=8, color="white", fontweight="bold")
            # 4 corner anchors (dấu chấm trắng)
            for dx in [-25, 25]:
                for dy in [-25, 25]:
                    ax.add_patch(Circle((cx+dx, cy+dy), 1.5,
                                         facecolor="white", edgecolor="black", linewidth=0.3))

    # Annotate sacrum zone
    ax.add_patch(Rectangle((350, 350), 300, 300, fill=False,
                             edgecolor="#B71C1C", linewidth=2.5, linestyle="--"))
    ax.text(500, 330, "SACRUM zone (9 patches - red)", ha="center",
            fontsize=10, color="#B71C1C", fontweight="bold")

    # Wires (orange lines going to edge)
    for r in range(8):
        for c in range(8):
            cx = 100 + c*100 + 50
            cy = 50 + r*100 + 50
            if c < 7:
                ax.plot([cx + 25, cx + 25 + 22], [cy, cy], color="#FF9800", linewidth=0.5, alpha=0.6)

    plt.tight_layout()
    plt.savefig(OUT / "top_view_with_velostat_patches.png", dpi=150, bbox_inches="tight")
    plt.savefig(OUT / "top_view_with_velostat_patches.svg", format="svg")
    plt.close()
    print("Saved: top_view_with_velostat_patches.png + .svg")


if __name__ == "__main__":
    view_draping_cross_section()
    view_assembly_with_drape()
    view_wire_routing()
    view_top_with_patches()
    print(f"\nAll drape visualizations in: {OUT}")
