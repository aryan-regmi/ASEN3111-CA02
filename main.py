import numpy as np
from math import sqrt, radians


def radius(x: float, y: float, x1: float, y1: float):
    """
    Calculates the radius/polar distance between points

    (x1,y1) is the center of the circle
    """
    return sqrt((x - x1) ** 2 + (y - y1) ** 2)


# noinspection PyPep8Naming
def plot_airfoil_flow(c, alpha, v_inf, p_inf, rho_inf, N):
    # Define Domain
    xmin = -1
    xmax = 3.5
    ymin = -0.5
    ymax = 0.5

    # Define Number of Grid Points
    nx = 100
    ny = 100

    # Create Mesh Over Specified Domain
    x, y = np.meshgrid(np.linspace(xmin, xmax, nx), np.linspace(ymin, ymax, ny))

    # Define Flow Parameters
    delx = c / N  # Equidistant discrete vorticies

    alpha = radians(alpha)  # AOA [rad]

    xvec = np.linspace(0, c, N)  # Vector for x along the chord line
    xvec[0] = delx / 2  # Offset first point to avoid division by 0

    yvec = np.zeros(N)  # Vector for y along the chord line (Thin Airfoil Theory)

    gamma = lambda x_pos: 2 * alpha * v_inf * sqrt((1 - (x_pos / c)) / (x_pos / c))  # Vortex Sheet Strength

    Gamma = lambda x_i: gamma(x_i) * delx  # Discrete Vortex Strength

    # TODO: Finish rest of the function!

    pass
