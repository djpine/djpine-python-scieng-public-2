import numpy as np
from numba import njit, float64, int64, types


@njit(types.UniTuple(float64[:], 2)(float64, float64, float64, int64))
def circle(r, x0=0.0, y0=0.0, n=12):
    theta = np.linspace(0., 2. * np.pi, n + 1)
    x = r * np.cos(theta[:-1])
    y = r * np.sin(theta[:-1])
    return x0 + x, y0 + y
