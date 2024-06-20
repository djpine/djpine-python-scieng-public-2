import numpy as np
import numba


@numba.vectorize([numba.float64(numba.float64),
                  numba.complex128(numba.complex128)],
                 nopython=True)
def sinc(x):
    if x == 0.0:
        return 1.0
    else:
        return np.sin(x) / x


def sinc_n(x):
    return np.where(x == 0.0, 1.0, np.sin(x) / x)


if __name__ == "__main__":
    import time

    # Make NumPy arrayd with N elements
    N = int(1e4)
    x = np.linspace(-1000.0, 1000.0, N)

    # Compute sinc of NumPy array using NumPy sinc function
    start_pd = time.perf_counter()
    a = sinc_n(x)
    end_pd = time.perf_counter()
    runtime = end_pd - start_pd
    print("\nNumPy run time = {0:0.4g} secs".format(runtime))

    # Compute sine of NumPy array using Numba
    start_pd = time.perf_counter()
    a = sinc(x)
    end_pd = time.perf_counter()
    runtime = end_pd - start_pd
    print("\nNumba 1st run time = {0:0.4g} s (incl. compilation time)"
          .format(runtime))
    # Compute sine of NumPy array using Numba a 2nd time
    start_pd = time.perf_counter()
    a = sinc(x)
    end_pd = time.perf_counter()
    runtime = end_pd - start_pd
    print("\nNumba 2nd run time = {0:0.4g} s (w/o compilation time)"
          .format(runtime))
