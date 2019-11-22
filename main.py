import numpy as np
from math import sqrt


def radius(x: float, y: float, x1: float, y1: float):
    """
    Calculates the radius/polar distance between points

    (x1,y1) is the center of the circle
    """
    return sqrt((x-x1)**2 + (y-y1)**2)
