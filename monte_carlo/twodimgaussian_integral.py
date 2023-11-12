"""Author: Vadan Khan 
Title: Monte Carlo Guassian 2D Integral

This code generates random points in the unit cube (0, 0, 0) to (1, 1, 1), and counts how many fall 
    under the surface z = e(-(x2 + y^2)). The ratio of points under the surface to the total number
    of points is an estimate of the double integral of z = e(-(x2 + y^2)) over the square region 
    from (-1, -1) to (1, 1). The code also plots the points and the surface for visualization. The 
    estimated double integral with n samples is printed at the end.

NB we have used an unsuitable range of points here for visualization

To edit the number of points generated, edit NUMPNTS global variable"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

FIGURE_SAVE_LOCATION = Path().resolve() / "figures"
FIGURE_SAVE_LOCATION.mkdir(parents=True, exist_ok=True)

NUMPNTS = 10000


def monte_carlo_double_integral(num_samples):
    count = 0
    points_under_surface = []
    points_above_surface = []

    for _ in range(num_samples):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        z = np.random.uniform(0, 1)
        if z <= np.exp(-(x**2 + y**2)):
            count += 1
            points_under_surface.append((x, y, z))
        else:
            points_above_surface.append((x, y, z))

    integral_estimate = 4 * count / num_samples  # Multiply by 4 because the region is 2x2

    # Plot the points
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(*zip(*points_under_surface), color='b',
               label='Points Under Surface')
    ax.scatter(*zip(*points_above_surface), color='r',
               label='Points Above Surface')

    # Draw the surface
    x = y = np.linspace(-1, 1, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-(X**2 + Y**2))
    ax.plot_surface(X, Y, Z, color='g', alpha=0.5, label='z=e^(-(x^2+y^2))')

    # Add a legend and title
    ax.legend()
    plt.title(f"Double Integral Estimate: {integral_estimate}")
    plt.savefig(FIGURE_SAVE_LOCATION / "double_integral.png", dpi=300)

    plt.show()

    return integral_estimate


if __name__ == "__main__":
    # Estimate double integral with n samples
    estimated_double_integral = monte_carlo_double_integral(NUMPNTS)
    print(f"Estimated value of double integral: {estimated_double_integral}")
