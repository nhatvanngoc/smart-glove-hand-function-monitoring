"""
CAD Drawings Generator — SVG technical drawings for Air Cushion
================================================================
Generates:
  - Top view of 8x8 cell matrix
  - Single cell cross-section
  - Valve manifold layout
  - Pump + reservoir assembly
  - Pneumatic circuit diagram
"""
from __future__ import annotations
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle, Polygon, FancyArrowPatch
import numpy as np

OUT = Path(__file__).resolve().parent / "drawings"
OUT.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "figure.dpi": 110,
    "savefig.dpi": 200,   # Higher DPI for CAD-like quality
    "savefig.bbox": "tight",
    "font.family": ["DejaVu Sans", "sans-serif"],
    "font.size": 9,
    "lines.linewidth": 1.0,
})


def drawing_top_view_8x8():
    """Top view of 8x8 cell matrix with dimensions and labels."""
    fig, ax = plt.subplots(figsize=(14, 11))
    ax.set_xlim(0, 1100)
    ax.set_ylim(0, 900)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("TOP VIEW — Air Cushion 8x8 Cell Matrix\n"
                  "Total: 800 x 1000 mm (W x L) | Cell: 100x100 mm",
                  pad=14, fontsize=12, fontweight="bold")

    # Frame
    ax.add_patch(Rectangle((50, 50), 1000, 800, fill=False, edgecolor="black", linewidth=2))
    ax.text(550, 30, "1000 mm", ha="center", fontsize=10, fontweight="bold")
    ax.text(30, 450, "800 mm", ha="center", rotation=90, fontsize=10, fontweight="bold")

    # Draw 8x8 grid
    sacrum_cells = {(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)}
    heel_row = 7
    for r in range(8):
        for c in range(8):
            x = 50 + c * 100
            y = 50 + (7 - r) * 100
            color = "#FFE0B2" if (r, c) in sacrum_cells else "#E3F2FD"
            edge = "#B71C1C" if (r, c) in sacrum_cells else "#1976D2"
            ax.add_patch(Rectangle((x, y), 100, 100, facecolor=color, edgecolor=edge, linewidth=1))
            # Cell label
            cell_id = r * 8 + c
            ax.text(x + 50, y + 50, f"{cell_id}", ha="center", va="center",
                    fontsize=10, fontweight="bold", color="#0D47A1")
            # Piezocapacitive anchor marker
            if (r, c) in sacrum_cells and c in (3, 4, 5):
                ax.add_patch(Circle((x + 50, y + 50), 6, facecolor="#AD1457",
                                     edgecolor="black", linewidth=1.5))
                ax.text(x + 50, y + 70, "Pz", ha="center", va="center",
                        fontsize=7, fontweight="bold", color="#AD1457")

    # Row labels (anatomy)
    anatomy = [
        (7, "HEAD"), (6, "SHOULDER"), (5, "UPPER BACK"),
        (4, "SACRUM"), (3, "SACRUM"), (2, "BUTTOCK"),
        (1, "THIGH"), (0, "HEEL"),
    ]
    for r, name in anatomy:
        y = 50 + (7 - r) * 100
        ax.text(20, y + 50, name, ha="right", va="center", fontsize=8,
                fontweight="bold", color="#37474F", rotation=90)
        ax.text(1075, y + 50, f"R{r}", ha="left", va="center", fontsize=8,
                color="#37474F")

    # Column labels
    for c in range(8):
        x = 50 + c * 100
        ax.text(x + 50, 870, f"C{c}", ha="center", va="bottom",
                fontsize=9, fontweight="bold", color="#37474F")
        ax.text(x + 50, 25, f"{100*(c+1)} mm", ha="center", va="top",
                fontsize=7, color="#37474F")

    # Dimension lines
    ax.annotate("", xy=(50, 880), xytext=(1050, 880),
                arrowprops=dict(arrowstyle="<->", color="black", lw=1.2))
    # Pressure thresholds legend
    legend_text = ("Pressure thresholds (mmHg):\n"
                   "  SACRUM: 32  (cells 27,28,29,35,36,37,43,44,45)\n"
                   "  HEEL:   30  (row 7, cells 56-63)\n"
                   "  TROCH:  30  (lateral, cells 25,26,33,34)\n"
                   "  SCAP:   32  (prone, row 0)\n"
                   "  KNEE:   32  (prone, row 6)\n"
                   "  OTHER:  40  (default)")
    ax.text(550, -90, legend_text, ha="center", va="top", fontsize=9,
            family="monospace", color="#0D47A1")

    plt.savefig(OUT / "cushion_top_view_8x8.svg", format="svg")
    plt.savefig(OUT / "cushion_top_view_8x8.png")
    plt.close()
    print("Saved: cushion_top_view_8x8.svg + .png")


def drawing_cross_section_cell():
    """Cross-section of single air cell."""
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 200)
    ax.set_ylim(-40, 120)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("CROSS-SECTION — Single Air Cell (100 x 100 mm)\n"
                  "Inflated state — pressure 80 mmHg", pad=12,
                  fontsize=12, fontweight="bold")

    # Layers from bottom to top
    # 1. Base plate
    ax.add_patch(Rectangle((0, 0), 200, 8, facecolor="#90A4AE", edgecolor="black", lw=1))
    ax.text(100, 4, "PETG Base plate (8 mm)", ha="center", va="center",
            fontsize=9, color="white", fontweight="bold")

    # 2. Silicone membrane (collapsed)
    ax.add_patch(FancyBboxPatch((10, 8), 180, 22, boxstyle="round,pad=0.5,rounding_size=8",
                                  facecolor="#FFCC80", edgecolor="#E65100", lw=1))
    ax.text(100, 19, "Silicone membrane (1.5 mm FDA-grade)", ha="center", va="center",
            fontsize=8, color="#BF360C", fontweight="bold")

    # Air fill arrows
    ax.annotate("", xy=(50, 35), xytext=(50, 8),
                arrowprops=dict(arrowstyle="->", color="#1976D2", lw=2))
    ax.text(35, 22, "AIR\n80\nmmHg", ha="center", va="center", fontsize=8,
            color="#1976D2", fontweight="bold")

    # 3. Velostat sensor
    ax.add_patch(Rectangle((0, 30), 200, 2, facecolor="#37474F", edgecolor="black", lw=1))
    ax.text(100, 31, "Velostat pressure sensor (0.3 mm)", ha="center", va="center",
            fontsize=8, color="white", fontweight="bold")

    # 4. Top fabric (patient contact)
    ax.add_patch(Rectangle((0, 32), 200, 1, facecolor="#BCAAA4", edgecolor="black", lw=0.8))
    ax.text(100, 32.5, "Anti-shear fabric", ha="center", va="center",
            fontsize=7, color="#3E2723")

    # Foam support below
    ax.add_patch(Rectangle((0, -30), 200, 30, facecolor="#FFE0B2", edgecolor="#E65100", lw=0.8,
                            hatch="//"))
    ax.text(100, -15, "Foam support (5 cm) — passive safety\n"
                       "khi mất điện / mất khí nén",
            ha="center", va="center", fontsize=9, color="#BF360C", fontweight="bold")

    # Valve mount (below base plate)
    ax.add_patch(Rectangle((85, -45), 30, 15, facecolor="#37474F", edgecolor="black", lw=1))
    ax.text(100, -37.5, "Solenoid valve\n12V, NO", ha="center", va="center",
            fontsize=7, color="white", fontweight="bold")

    # Tube routing
    ax.plot([100, 100], [-45, -55], color="#1976D2", lw=2)
    ax.text(115, -50, "Tube\n4mm ID", fontsize=7, color="#1976D2", fontweight="bold")

    # Dimensions
    ax.annotate("", xy=(0, 105), xytext=(200, 105),
                arrowprops=dict(arrowstyle="<->", color="black", lw=1))
    ax.text(100, 110, "100 mm (cell width)", ha="center", fontsize=10, fontweight="bold")

    ax.annotate("", xy=(205, 0), xytext=(205, 32),
                arrowprops=dict(arrowstyle="<->", color="black", lw=1))
    ax.text(218, 16, "32 mm\n(working height)", ha="left", va="center",
            fontsize=9, fontweight="bold")

    ax.annotate("", xy=(205, 0), xytext=(205, -30),
                arrowprops=dict(arrowstyle="<->", color="#37474F", lw=0.8))
    ax.text(218, -15, "50 mm\nfoam", ha="left", va="center",
            fontsize=8, color="#37474F")

    # Layer labels on left
    ax.text(-20, 31, "Sensor", ha="right", va="center", fontsize=8, color="#37474F", rotation=90)
    ax.text(-20, 19, "Cell\nchamber", ha="right", va="center", fontsize=8, color="#BF360C", rotation=90)
    ax.text(-20, 4, "Base", ha="right", va="center", fontsize=8, color="#37474F", rotation=90)

    plt.savefig(OUT / "cushion_cell_cross_section.svg", format="svg")
    plt.savefig(OUT / "cushion_cell_cross_section.png")
    plt.close()
    print("Saved: cushion_cell_cross_section.svg + .png")


def drawing_manifold():
    """Manifold block top view with 64 outlets."""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 240)
    ax.set_ylim(0, 140)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("MANIFOLD BLOCK — 64 outlets (8x8) + 1 inlet\n"
                  "Dimensions: 200 x 100 x 30 mm (PETG)", pad=12,
                  fontsize=12, fontweight="bold")

    # Main body
    ax.add_patch(FancyBboxPatch((20, 20), 200, 100, boxstyle="round,pad=2,rounding_size=5",
                                  facecolor="#90A4AE", edgecolor="black", lw=1.5))

    # Inlet (left side)
    ax.add_patch(Circle((10, 70), 8, facecolor="#1976D2", edgecolor="black", lw=1.5))
    ax.text(10, 70, "IN", ha="center", va="center", fontsize=8, color="white", fontweight="bold")
    ax.text(10, 50, "8mm\ntube", ha="center", va="top", fontsize=7, color="#1976D2")

    # 64 outlets in 8x8 pattern
    outlet_w = 180 / 8   # 22.5 mm per outlet horizontally
    outlet_h = 80 / 8    # 10 mm per outlet vertically

    for r in range(8):
        for c in range(8):
            cx = 30 + c * outlet_w + outlet_w / 2
            cy = 30 + r * outlet_h + outlet_h / 2
            ax.add_patch(Circle((cx, cy), 3, facecolor="#37474F", edgecolor="white", lw=0.5))
            cell_id = r * 8 + c
            ax.text(cx, cy - 4, str(cell_id), ha="center", va="center",
                    fontsize=5, color="white", fontweight="bold")

    # Pressure sensor port (top right)
    ax.add_patch(Circle((220, 110), 5, facecolor="#AD1457", edgecolor="black", lw=1))
    ax.text(220, 110, "P", ha="center", va="center", fontsize=7, color="white", fontweight="bold")
    ax.text(232, 110, "Pressure\nsensor\n0-100 mmHg", fontsize=7, va="center")

    # Dimensions
    ax.annotate("", xy=(20, 130), xytext=(220, 130),
                arrowprops=dict(arrowstyle="<->", color="black", lw=1))
    ax.text(120, 135, "200 mm", ha="center", fontsize=10, fontweight="bold")

    ax.annotate("", xy=(230, 20), xytext=(230, 120),
                arrowprops=dict(arrowstyle="<->", color="black", lw=1))
    ax.text(238, 70, "100 mm", ha="left", va="center", fontsize=10, fontweight="bold", rotation=90)

    # Internal channel (illustrative)
    ax.add_patch(Rectangle((24, 24), 192, 92, fill=False, edgecolor="#1976D2",
                            lw=0.5, linestyle="--"))
    ax.text(120, 124, "Internal channel: 200 x 100 mm", ha="center", fontsize=8,
            color="#1976D2", style="italic")

    plt.savefig(OUT / "cushion_manifold.svg", format="svg")
    plt.savefig(OUT / "cushion_manifold.png")
    plt.close()
    print("Saved: cushion_manifold.svg + .png")


def drawing_pneumatic_circuit():
    """Pneumatic circuit diagram (ISO 1219 style)."""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 100)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("PNEUMATIC CIRCUIT — Air Cushion System\n"
                  "ISO 1219 symbol convention", pad=14,
                  fontsize=12, fontweight="bold")

    # Pump (circle with arrow)
    ax.add_patch(Circle((20, 50), 8, facecolor="#FFCC80", edgecolor="black", lw=2))
    ax.text(20, 50, "M", ha="center", va="center", fontsize=10, fontweight="bold")
    ax.text(20, 36, "Pump\n24V DC\n6 L/min", ha="center", va="top", fontsize=7)

    # Direction arrow
    ax.annotate("", xy=(38, 50), xytext=(28, 50),
                arrowprops=dict(arrowstyle="->", color="black", lw=2))

    # Reservoir (cylinder)
    ax.add_patch(Rectangle((40, 42), 20, 16, facecolor="#B0BEC5", edgecolor="black", lw=1.5))
    ax.text(50, 50, "R", ha="center", va="center", fontsize=9, fontweight="bold")
    ax.text(50, 35, "Reservoir\n2L buffer", ha="center", va="top", fontsize=7)

    # Safety valve (spring symbol)
    ax.annotate("", xy=(80, 50), xytext=(60, 50),
                arrowprops=dict(arrowstyle="->", color="black", lw=2))
    ax.add_patch(Polygon([[85, 47], [95, 47], [90, 53]], facecolor="white",
                          edgecolor="black", lw=1.5))
    ax.text(90, 35, "Safety valve\n0.6 bar", ha="center", va="top", fontsize=7)

    # Pressure regulator
    ax.annotate("", xy=(115, 50), xytext=(100, 50),
                arrowprops=dict(arrowstyle="->", color="black", lw=2))
    ax.add_patch(Rectangle((115, 44), 12, 12, facecolor="#90A4AE", edgecolor="black", lw=1.5))
    ax.text(121, 50, "PR", ha="center", va="center", fontsize=7, fontweight="bold")
    ax.text(121, 35, "Regulator\n0-100 mmHg", ha="center", va="top", fontsize=7)

    # Pressure sensor
    ax.add_patch(Circle((127, 50), 5, facecolor="#AD1457", edgecolor="black", lw=1.5))
    ax.text(127, 50, "P", ha="center", va="center", fontsize=7, color="white", fontweight="bold")

    # Main line to manifold
    ax.plot([130, 130], [50, 70], color="#1976D2", lw=2)
    ax.annotate("", xy=(130, 70), xytext=(130, 50),
                arrowprops=dict(arrowstyle="<-", color="#1976D2", lw=2))

    # Manifold (rectangle with 8x8 outlets)
    ax.add_patch(Rectangle((105, 70), 50, 20, facecolor="#90A4AE", edgecolor="black", lw=1.5))
    ax.text(130, 80, "MANIFOLD (64-way)", ha="center", va="center",
            fontsize=9, fontweight="bold")

    # 8 example outlets going down to cells
    for i in range(8):
        x = 110 + i * 6
        ax.plot([x, x], [70, 30], color="#37474F", lw=0.8)
        ax.add_patch(Rectangle((x - 2, 22), 4, 8, facecolor="#37474F", edgecolor="black", lw=0.5))
        ax.text(x, 18, f"{i}", ha="center", va="top", fontsize=6)

    # 64 cells (8x8 small grid)
    cell_w = 10
    for r in range(8):
        for c in range(8):
            x = 70 + c * cell_w
            y = 80 + r * 1.5
            ax.add_patch(Rectangle((x, y), 8, 1.2, facecolor="#FFE0B2",
                                    edgecolor="#E65100", lw=0.2))

    # Title bottom
    ax.text(70, 5, "Flow path: Pump → Reservoir → Safety valve → Regulator → "
                   "Manifold → 64 valves → 64 cells",
            ha="center", fontsize=8, color="#37474F", style="italic")

    plt.savefig(OUT / "cushion_pneumatic_circuit.svg", format="svg")
    plt.savefig(OUT / "cushion_pneumatic_circuit.png")
    plt.close()
    print("Saved: cushion_pneumatic_circuit.svg + .png")


def drawing_assembly_exploded():
    """Exploded view of cushion assembly."""
    fig, ax = plt.subplots(figsize=(14, 12))
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 100)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("EXPLODED ASSEMBLY — Air Cushion Layers (1 unit cell)",
                  pad=14, fontsize=12, fontweight="bold")

    # Layer 1: Top fabric
    ax.add_patch(Rectangle((30, 80), 60, 3, facecolor="#BCAAA4",
                            edgecolor="black", lw=1.5))
    ax.text(105, 81.5, "1. Anti-shear fabric (1 mm)", ha="left", va="center", fontsize=9)

    # Layer 2: Velostat
    ax.add_patch(Rectangle((30, 70), 60, 3, facecolor="#37474F",
                            edgecolor="black", lw=1.5))
    ax.text(105, 71.5, "2. Velostat sheet (0.3 mm)", ha="left", va="center",
            fontsize=9, color="white")

    # Layer 3: Silicone membrane
    ax.add_patch(FancyBboxPatch((30, 50), 60, 18, boxstyle="round,pad=1,rounding_size=4",
                                  facecolor="#FFCC80", edgecolor="#E65100", lw=1.5))
    ax.text(105, 59, "3. Silicone membrane cell\n     (1.5 mm, 64 cells)",
            ha="left", va="center", fontsize=9)

    # Layer 4: Base plate
    ax.add_patch(Rectangle((30, 35), 60, 8, facecolor="#90A4AE",
                            edgecolor="black", lw=1.5))
    ax.text(105, 39, "4. PETG base plate (8 mm)\n     with valve mounts",
            ha="left", va="center", fontsize=9)

    # Layer 5: Foam
    ax.add_patch(Rectangle((30, 10), 60, 18, facecolor="#FFE0B2",
                            edgecolor="#E65100", lw=1.5, hatch="//"))
    ax.text(105, 19, "5. Foam support (50 mm)\n     passive safety layer",
            ha="left", va="center", fontsize=9)

    # Explosion arrows (vertical)
    for y_pair in [(80, 76), (70, 64), (50, 45), (35, 30)]:
        ax.annotate("", xy=(20, y_pair[1]), xytext=(20, y_pair[0]),
                    arrowprops=dict(arrowstyle="->", color="#B71C1C", lw=1.5))
        ax.text(15, (y_pair[0] + y_pair[1]) / 2, "↑", ha="center", va="center",
                fontsize=10, color="#B71C1C", fontweight="bold")

    # Valve detail
    ax.add_patch(Rectangle((5, 35), 12, 8, facecolor="#37474F", edgecolor="black", lw=1.5))
    ax.text(11, 39, "Valve", ha="center", va="center", fontsize=7, color="white")
    ax.plot([17, 30], [39, 39], color="#1976D2", lw=1.5)
    ax.text(23, 42, "Tube 4mm", ha="center", fontsize=6, color="#1976D2")

    plt.savefig(OUT / "cushion_exploded_assembly.svg", format="svg")
    plt.savefig(OUT / "cushion_exploded_assembly.png")
    plt.close()
    print("Saved: cushion_exploded_assembly.svg + .png")


def drawing_pressure_response():
    """Pressure response curve (time vs pressure)."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 100)
    ax.set_xlabel("Time (seconds)", fontsize=11)
    ax.set_ylabel("Cell pressure (mmHg)", fontsize=11)
    ax.set_title("Pressure Response — Single Cell\n"
                  "Step input 0 → 80 mmHg, deflate 80 → 0 mmHg",
                  fontsize=12, fontweight="bold")
    ax.grid(True, alpha=0.3, linestyle="--")

    t = np.linspace(0, 5, 200)
    # Inflation (0 to 1.2s, exponential rise to 80)
    inflate = 80 * (1 - np.exp(-t / 0.3))
    # Hold (1.2 to 3s)
    hold = np.where(t < 1.2, inflate, 80)
    # Deflation (3 to 4s)
    deflate = np.where(t < 3, 80, 80 * np.exp(-(t - 3) / 0.4))
    # Settle
    final = np.where(t < 4, deflate, 0)

    ax.plot(t, final, color="#1976D2", lw=2, label="Cell pressure")
    ax.axhline(32, color="#AD1457", lw=1.5, linestyle="--", label="Sacrum threshold (32 mmHg)")
    ax.axhline(80, color="#B71C1C", lw=1.5, linestyle=":", label="Safety max (80 mmHg)")

    # Annotations
    ax.annotate("Inflate\n0.96s (rise time)", xy=(0.96, 80), xytext=(0.5, 50),
                fontsize=9, color="#1976D2",
                arrowprops=dict(arrowstyle="->", color="#1976D2"))
    ax.annotate("Deflate\n0.92s (fall time)", xy=(3.92, 0), xytext=(3.5, 30),
                fontsize=9, color="#1976D2",
                arrowprops=dict(arrowstyle="->", color="#1976D2"))

    ax.legend(loc="lower right", fontsize=9)
    plt.tight_layout()
    plt.savefig(OUT / "cushion_pressure_response.svg", format="svg")
    plt.savefig(OUT / "cushion_pressure_response.png")
    plt.close()
    print("Saved: cushion_pressure_response.svg + .png")


def drawing_force_balance():
    """Force balance analysis: weight distribution across 64 cells."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("Force Balance — Body Weight Distribution on 64 Cells\n"
                  "(70 kg mannequin, supine)", fontsize=12, fontweight="bold")

    # Setup pressure map for 70 kg supine
    weight = np.full((8, 8), 8.0)  # ~8 kg/cell uniform
    # Sacrum zone (rows 3-5, cols 3-5) gets more weight
    weight[3:6, 3:6] = 15.0
    # Heels (row 7) some weight
    weight[7, :] = 12.0
    # Shoulders (row 0) some weight
    weight[0, :] = 11.0
    weight[0:2, 3:5] = 14.0

    # Plot 1: Weight per cell (heatmap)
    ax = axes[0]
    im = ax.imshow(weight, cmap="hot_r", vmin=0, vmax=20)
    ax.set_title("Body weight per cell (kg)")
    for r in range(8):
        for c in range(8):
            ax.text(c, r, f"{weight[r, c]:.1f}", ha="center", va="center",
                    color="black" if weight[r, c] < 12 else "white",
                    fontsize=8, fontweight="bold")
    plt.colorbar(im, ax=ax, label="kg/cell")
    ax.set_xlabel("Cell column")
    ax.set_ylabel("Cell row")

    # Plot 2: Required cell pressure
    cell_area = 0.01  # m²
    # P = F / A * mmHg/Pa conversion (1 Pa = 0.0075 mmHg)
    pressure_needed = weight * 9.81 / cell_area * 0.0075
    ax = axes[1]
    im = ax.imshow(pressure_needed, cmap="hot", vmin=0, vmax=120)
    ax.set_title("Required cell pressure (mmHg)")
    for r in range(8):
        for c in range(8):
            ax.text(c, r, f"{pressure_needed[r, c]:.0f}", ha="center", va="center",
                    color="black" if pressure_needed[r, c] < 60 else "white",
                    fontsize=8, fontweight="bold")
    plt.colorbar(im, ax=ax, label="mmHg")
    ax.set_xlabel("Cell column")
    ax.set_ylabel("Cell row")

    plt.tight_layout()
    plt.savefig(OUT / "cushion_force_balance.svg", format="svg")
    plt.savefig(OUT / "cushion_force_balance.png")
    plt.close()
    print("Saved: cushion_force_balance.svg + .png")


if __name__ == "__main__":
    drawing_top_view_8x8()
    drawing_cross_section_cell()
    drawing_manifold()
    drawing_pneumatic_circuit()
    drawing_assembly_exploded()
    drawing_pressure_response()
    drawing_force_balance()
    print(f"\nAll CAD drawings generated in: {OUT}")
