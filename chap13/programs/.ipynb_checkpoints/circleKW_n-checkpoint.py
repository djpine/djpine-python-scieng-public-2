import numpy as np
import numba


@numba.guvectorize([(numba.float64, numba.float64, numba.float64, numba.int32, numba.float64[:])],
                   "(),(),(),()->(n)", nopython=True)
def circle(r, x0, y0, m, x, y):
    theta = np.linspace(0.0, 2.0 * np.pi, m, endpoint=False)
    x[:] = x0 + r * np.cos(theta)


x0 = 0.0
y0 = 0.0
r = 1.0
n = 4

x = circle(r, x0, y0, n)
