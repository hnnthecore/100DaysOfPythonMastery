# Day 26 - NeuralInk: Neural Network Visualizer
# A simple visualization of a feedforward neural network with random weights and activations.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# ------------------------------------------------------------
# Neural Network Configuration
# ------------------------------------------------------------
LAYER_SIZES = [3, 5, 4, 2]  # Input, hidden1, hidden2, output layers
ACTIVATION_FUNCTION = lambda x: 1 / (1 + np.exp(-x))  # Sigmoid activation


# ------------------------------------------------------------
# Utility Functions
# ------------------------------------------------------------
def generate_network(layer_sizes):
    """Generates random weights and biases for each layer."""
    weights = [np.random.randn(next_layer, current_layer) for current_layer, next_layer in zip(layer_sizes[:-1], layer_sizes[1:])]
    biases = [np.random.randn(n, 1) for n in layer_sizes[1:]]
    return weights, biases


def feedforward(inputs, weights, biases):
    """Computes activations layer by layer."""
    activations = [inputs]
    a = inputs
    for w, b in zip(weights, biases):
        z = np.dot(w, a) + b
        a = ACTIVATION_FUNCTION(z)
        activations.append(a)
    return activations


# ------------------------------------------------------------
# Visualization
# ------------------------------------------------------------
def draw_network(ax, layer_sizes, activations):
    """Draws the network layers and connections."""
    ax.clear()
    ax.axis("off")

    # Calculate layout
    layer_count = len(layer_sizes)
    v_spacing = 1
    h_spacing = 3

    positions = []
    for i, size in enumerate(layer_sizes):
        x = i * h_spacing
        y_positions = np.linspace(-(size - 1) * v_spacing / 2, (size - 1) * v_spacing / 2, size)
        positions.append([(x, y) for y in y_positions])

    # Draw connections
    for i in range(len(layer_sizes) - 1):
        for j, (x1, y1) in enumerate(positions[i]):
            for k, (x2, y2) in enumerate(positions[i + 1]):
                ax.plot([x1, x2], [y1, y2], color="gray", linewidth=0.5, alpha=0.5)

    # Draw neurons
    for i, layer in enumerate(positions):
        for j, (x, y) in enumerate(layer):
            a = activations[i][j, 0] if i < len(activations) else 0
            color_intensity = a
            circle = plt.Circle((x, y), 0.2, color=plt.cm.viridis(color_intensity))
            ax.add_patch(circle)
            if i == 0:
                ax.text(x - 0.8, y, f"x{j+1}", va="center", fontsize=8)
            elif i == len(layer_sizes) - 1:
                ax.text(x + 0.6, y, f"y{j+1}", va="center", fontsize=8)


def animate_network(i, ax, weights, biases):
    """Updates activations for each animation frame."""
    inputs = np.random.rand(LAYER_SIZES[0], 1)
    activations = feedforward(inputs, weights, biases)
    draw_network(ax, LAYER_SIZES, activations)


# ------------------------------------------------------------
# Main Execution
# ------------------------------------------------------------
def main():
    weights, biases = generate_network(LAYER_SIZES)

    fig, ax = plt.subplots(figsize=(8, 6))
    ani = animation.FuncAnimation(fig, animate_network, fargs=(ax, weights, biases), frames=50, interval=500)
    plt.show()


if __name__ == "__main__":
    main()
