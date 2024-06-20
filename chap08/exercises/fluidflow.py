import numpy as np
import matplotlib.pyplot as plt

# Create a meshgrid
x, y = np.meshgrid(np.arange(0, 1.1, 0.1), np.arange(0, 1.1, 0.1))

# Set constant value
b = 1

# Calculate vector components
v_x = b * y
v_y = b * x

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5))

# Plot quiver plot
ax1.quiver(x, y, v_x, v_y, color="C0")
ax2.streamplot(x, y, v_x, v_y, color="C0")

# Set labels
for ax in [ax1, ax2]:
    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')

fig.tight_layout()
# Show the plot
fig.savefig("./figures/fluidflow.pdf")
fig.show()
