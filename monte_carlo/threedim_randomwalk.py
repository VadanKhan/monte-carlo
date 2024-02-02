"""
Author: Vadan Khan
Title: 3D random walk

This code generates a random walk of N steps in three dimensions. At each step, the walker moves
    one unit in the x, y, or z direction with equal probability. The position of the walker after 
    each step is stored in an array, and the entire random walk is plotted at the end. You can 
    adjust the number of steps in the walk by changing the N variable. This is a simple model for 
    the motion of a gas particle in three dimensions.

To edit the numper of points generated, edit NUMPNTS global variable

# noqa: W291
"""


import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


FIGURE_SAVE_LOCATION = Path().resolve() / "figures"
FIGURE_SAVE_LOCATION.mkdir(parents=True, exist_ok=True)

# Number of steps
N = 10000

# Array to store the positions
x_positions = np.zeros(N)
y_positions = np.zeros(N)
z_positions = np.zeros(N)

# Initial position
x_positions[0] = y_positions[0] = z_positions[0] = 0

# Perform the random walk
for i in range(1, N):
    # Generate a random step
    dx, dy, dz = np.random.choice([-1, 1], size=3)

    # Update the position
    x_positions[i] = x_positions[i-1] + dx
    y_positions[i] = y_positions[i-1] + dy
    z_positions[i] = z_positions[i-1] + dz

# Plot the random walk
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_positions, y_positions, z_positions)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('3D Random Walk')
plt.savefig(FIGURE_SAVE_LOCATION / "3d-monte-carlo-walk.png", dpi=300)
plt.show()
