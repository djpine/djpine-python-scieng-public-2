import math
import numba


@numba.vectorize([numba.float64(numba.float64, numba.float64)],
                 nopython=True)
def sinc(x, y):
    r = (x ** 2 + y ** 2) ** 0.5
    if r == 0.0:
        return 1.0
    else:
        return math.sin(r) / r


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    n = 100
    x = np.linspace(0.0, 10.0, n)
    y = np.linspace(-10.0, 10.0, n)
    f = sinc(x, y)

    X, Y = np.meshgrid(x, y)
    Z = sinc(X, Y)

    fig, ax = plt.subplots(figsize=(5, 4),
                           subplot_kw={"projection": "3d"})
    # Make surface plot
    fig.subplots_adjust(left=0.0, bottom=0.08, right=0.96,
                        top=0.96, wspace=0.05)
    p1 = ax.plot_surface(X, Y, Z, rcount=50, ccount=50, color="C1")

    fig.savefig("figures/sinc_2dnn.pdf")
    fig.show()
