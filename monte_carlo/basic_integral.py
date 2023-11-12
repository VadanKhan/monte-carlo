"""
Author: Vadan Khan
Title: Monte Carlo Basic Integral

This code generates random points in the unit square (0, 0) to (1, 1), and counts how many fall 
    under the curve y = x^2. The ratio of points under the curve to the total number of points is 
    an estimate of the integral of y = x^2 from 0 to 1. The code also plots the points and the curve
    for visualization. The estimated integral is printed at the end.

To edit the numper of points generated, edit NUMPNTS global variable

# noqa: W291
"""


import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

FIGURE_SAVE_LOCATION = Path().resolve() / "figures"
FIGURE_SAVE_LOCATION.mkdir(parents=True, exist_ok=True)

NUMPNTS = 1000


def monte_carlo_integral(num_samples):
    count = 0
    points_under_curve = []
    points_above_curve = []

    for _ in range(num_samples):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        if y <= x**2:
            count += 1
            points_under_curve.append((x, y))
        else:
            points_above_curve.append((x, y))

    integral_estimate = count / num_samples

    # Plot the points
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.scatter(*zip(*points_under_curve), color='b',
               label='Points Under Curve')
    ax.scatter(*zip(*points_above_curve), color='r',
               label='Points Above Curve')

    # Draw the curve
    x = np.linspace(0, 1, 100)
    y = x**2
    ax.plot(x, y, color='g', label='y=x^2')

    # Add a legend and title
    ax.legend()
    plt.title(f"Integral Estimate: {integral_estimate}")
    plt.savefig(FIGURE_SAVE_LOCATION / "integral.png", dpi=300)

    plt.show()

    return integral_estimate


if __name__ == "__main__":
    # Estimate integral with n samples
    estimated_integral = monte_carlo_integral(NUMPNTS)
    print(f"Estimated value of integral: {estimated_integral}")
