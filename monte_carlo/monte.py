"""
Author: Vadan Khan
Title: Monte Carlo Basic Demo

In this code, we randomly generate points in a 2x2 square and count how many fall within a unit 
circle centered at the origin. The ratio of points inside the circle to the total number of points 
is approximately pi/4, so we multiply our ratio by 4 to estimate pi. The more samples we use, the 
closer our estimate will be to the true value of pi.

To edit the numper of points generated, edit NUMPNTS global variable
"""


import numpy as np
import random
import matplotlib.pyplot as plt
from pathlib import Path

FIGURE_SAVE_LOCATION = Path().resolve() / "figures"
FIGURE_SAVE_LOCATION.mkdir(parents=True, exist_ok=True)

NUMPNTS = 10000


def estimate_pi(num_samples):
    num_inside_circle = 0
    points_inside_circle = []
    points_outside_circle = []

    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x**2 + y**2

        if distance <= 1:
            num_inside_circle += 1
            points_inside_circle.append((x, y))
        else:
            points_outside_circle.append((x, y))

    pi_estimate = 4 * num_inside_circle / num_samples

    # Plot the points
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.scatter(*zip(*points_inside_circle), color='b',
               label='Points Inside Circle')
    ax.scatter(*zip(*points_outside_circle), color='r',
               label='Points Outside Circle')

    # Draw the unit circle
    circle = plt.Circle((0, 0), 1, fill=False, color='g', label='Unit Circle')
    ax.add_artist(circle)

    # Add a legend and title
    ax.legend()
    plt.title(f"Pi Estimate: {pi_estimate}")
    plt.savefig(FIGURE_SAVE_LOCATION / "pi.png", dpi=300)

    plt.show()

    return pi_estimate


if __name__ == "__main__":
    # Estimate pi with 1 million samples
    estimated_pi = estimate_pi(NUMPNTS)
    print(f"Estimated value of pi: {estimated_pi}")
