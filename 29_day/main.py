# Day 29 - TerraSim: Terrain Heightmap Generator
# Procedural 2D & 3D terrain generator using layered noise functions.
# Produces natural-looking heightmaps and surface landscapes.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# ------------------------------------------------------------
# Terrain Generation (Layered Noise)
# ------------------------------------------------------------
def generate_terrain(size=150, roughness=4):
    """
    Generate a 2D terrain heightmap using layered sine waves and noise.
    size: grid dimension (size x size)
    roughness: number of noise layers (higher = more detail)
    """
    x = np.linspace(0, 5, size)
    y = np.linspace(0, 5, size)
    xx, yy = np.meshgrid(x, y)

    # Base terrain
    terrain = np.zeros_like(xx)

    # Add layered noise (fractal-like)
    for i in range(1, roughness + 1):
        frequency = i * 1.2
        amplitude = 1 / i
        terrain += amplitude * np.sin(xx * frequency + np.random.rand()) * np.cos(yy * frequency + np.random.rand())

    # Normalize between 0 and 1
    terrain = (terrain - terrain.min()) / (terrain.max() - terrain.min())
    return terrain


# ------------------------------------------------------------
# 2D Visualization
# ------------------------------------------------------------
def show_heightmap(terrain):
    plt.figure(figsize=(7, 7))
    plt.title("TerraSim – 2D Heightmap")
    plt.imshow(terrain, cmap="terrain")
    plt.colorbar(label="Height")
    plt.axis("off")
    plt.show()


# ------------------------------------------------------------
# 3D Visualization
# ------------------------------------------------------------
def show_3d_surface(terrain):
    size = terrain.shape[0]
    x = np.linspace(0, 5, size)
    y = np.linspace(0, 5, size)
    xx, yy = np.meshgrid(x, y)

    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection="3d")
    ax.set_title("TerraSim – 3D Terrain Surface")
    ax.plot_surface(xx, yy, terrain, cmap="terrain", linewidth=0, antialiased=True)
    ax.set_axis_off()
    plt.show()


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------
def main():
    print("TerraSim – Terrain Heightmap Generator")

    try:
        size = int(input("Enter map size (100–300 recommended, default 150): ") or 150)
        roughness = int(input("Enter roughness level (2–8 recommended, default 4): ") or 4)
    except ValueError:
        size, roughness = 150, 4

    view_mode = input("View mode: (1) 2D Heightmap, (2) 3D Surface (default = 1): ").strip()

    terrain = generate_terrain(size=size, roughness=roughness)

    if view_mode == "2":
        show_3d_surface(terrain)
    else:
        show_heightmap(terrain)


if __name__ == "__main__":
    main()
