import numpy as np
import matplotlib.pyplot as plt
import sys
import os

if len(sys.argv) < 3:
    print("Usage: python plot_data.py x.txt y1.txt y2.txt ...")
    sys.exit(1)

x_file = sys.argv[1]
y_files = sys.argv[2:]

for f in [x_file] + y_files:
    if not os.path.isfile(f):
        print(f"Error: file not found -> {f}")
        sys.exit(1)

x = np.loadtxt(x_file)

names = [
    "Vapor velocity", "Vapor bulk temperature", "Vapor pressure",
    "Wick velocity", "Wick bulk temperature", "Wick pressure",
    "Wall bulk temperature", "Outer wall temperature",
    "Wall-wick interface temperature", "Wick-vapor interface temperature",
    "Outer wall heat flux", "Wall-wick heat flux", "Wick-vapor heat flux",
    "Mass volumetric source"
]
units = [
    "[m/s]", "[K]", "[Pa]", "[m/s]", "[K]", "[Pa]",
    "[K]", "[K]", "[K]", "[K]",
    "[W/m²]", "[W/m²]", "[W/m²]", "[W/m³]"
]

n = len(y_files)
per_fig = 4
cols = 2
rows = (per_fig + cols - 1) // cols

for start in range(0, n, per_fig):
    end = min(start + per_fig, n)
    fig, axes = plt.subplots(rows, cols, figsize=(12, 3.5 * rows))
    axes = axes.flatten()

    for i, ax in enumerate(axes):
        idx = start + i
        if idx < end:
            y = np.loadtxt(y_files[idx])
            ax.plot(x, y)
            ax.set_title(f"{names[idx]} {units[idx]}")
            ax.set_xlabel("Axial length [m]")
            ax.grid(True)
        else:
            fig.delaxes(ax)

    plt.tight_layout()
    plt.show(block=False)

plt.pause(0.1)
plt.show()
