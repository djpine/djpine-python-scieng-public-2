import math
import numba


@numba.vectorize(nopython=True)
def sinc(x):
    if x == 0.0:
        return 1.0
    else:
        return math.sin(x) / x
