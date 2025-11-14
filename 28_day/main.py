# Day 28 - FractaPy: Fractal Pattern Generator
# Generates beautiful recursive fractal trees using matplotlib.
# Adjust angle, depth, and color for unique patterns.

import matplotlib.pyplot as plt
import math
import random


# ------------------------------------------------------------
# Recursive Drawing Function
# ------------------------------------------------------------
def draw_branch(x, y, length, angle, depth, color_map):
    """Recursively draw branches of the fractal tree."""
    if depth == 0:
        return

    # Compute new end coordinates
    x2 = x + length * math.cos(math.radians(angle))
    y2 = y + length * math.sin(math.radians(angle))

    # Plot the current branch
    plt.plot([x, x2], [y, y2], color=color_map[depth % len(color_map)], linewidth=depth * 0.6)

    # Recurse to create new branches
    new_length = length * 0.7
    branch_angle = random.uniform(15, 35)
    draw_branch(x2, y2, new_length, angle - branch_angle, depth - 1, color_map)
    draw_branch(x2, y2, new_length, angle + branch_angle, depth - 1, color_map)


# ------------------------------------------------------------
# Fractal Tree Generator
# ------------------------------------------------------------
def generate_fractal_tree(depth=8, length=100):
    """Generate a random fractal tree pattern."""
    plt.figure(figsize=(8, 8))
    plt.axis("off")
    plt.title(f"FractaPy – Recursive Fractal Tree (Depth {depth})", fontsize=10)

    # Define color gradients for aesthetic diversity
    color_maps = [
        ["#0B3864", "#1C6EA4", "#8EC0E4", "#B4E1FF"],  # Cool blue
        ["#5D3FD3", "#8A2BE2", "#B76EFF", "#E6CCFF"],  # Purple
        ["#155E63", "#76C7C0", "#B5EAD7", "#C9F9FF"],  # Aqua green
        ["#8B4513", "#CD853F", "#DEB887", "#FFE4C4"],  # Warm brown
    ]

    color_map = random.choice(color_maps)

    # Draw trunk (start at bottom center)
    draw_branch(0, -250, length, 90, depth, color_map)
    plt.show()


# ------------------------------------------------------------
# Main Execution
# ------------------------------------------------------------
def main():
    print("FractaPy – Fractal Pattern Generator")
    try:
        depth = int(input("Enter recursion depth (5–12 recommended, default 8): ") or 8)
        length = int(input("Enter branch length (default 100): ") or 100)
    except ValueError:
        print("Invalid input, using default values.")
        depth, length = 8, 100

    generate_fractal_tree(depth, length)


if __name__ == "__main__":
    main()
