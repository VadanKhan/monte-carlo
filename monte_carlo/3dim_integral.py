"""Author: Vadan Khan 
Title: Monte Carlo 3D Integral

This code generates random points in the cube (-1, -1, -1) to (1, 1, 1), and counts how many fall 
    under the hypersurface w = e(-(x2 + y^2 + z^2)). The ratio of points under the hypersurface to 
    the total number of points is an estimate of the triple integral of w = e(-(x2 + y^2 + z^2)) 
    over the cube region from (-1, -1, -1) to (1, 1, 1). The estimated triple integral with n 
    samples is printed at the end. You can adjust the number of points used in the estimation by 
    changing the NUMPNTS variable.

Please note that this code does not include a plot because visualizing a 4D function is non-trivial 
    and typically requires some form of dimensionality reduction. If you need to visualize the 
    function or the points, you might consider a pairplot or a 3D scatterplot of (x, y, z) pairs 
    that fall under the hypersurface.

To edit the number of points generated, edit NUMPNTS global variable

# noqa: W291
"""

import numpy as np
from pathlib import Path

FIGURE_SAVE_LOCATION = Path().resolve() / "figures"
FIGURE_SAVE_LOCATION.mkdir(parents=True, exist_ok=True)

NUMPNTS = 1000


def monte_carlo_triple_integral(num_samples):
    count = 0

    for _ in range(num_samples):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        z = np.random.uniform(-1, 1)
        w = np.random.uniform(0, 1)
        if w <= np.exp(-(x**2 + y**2 + z**2)):
            count += 1

    integral_estimate = 8 * count / num_samples  # Multiply by 8 because the region is 2x2x2

    return integral_estimate


if __name__ == "__main__":
    # Estimate triple integral with n samples
    estimated_triple_integral = monte_carlo_triple_integral(NUMPNTS)
    print(f"Estimated value of triple integral: {estimated_triple_integral}")
