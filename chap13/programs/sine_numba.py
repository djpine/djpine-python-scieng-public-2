import numpy as np
import numba
import time


@numba.jit(nopython=True)
def trig(x):
    a = np.sin(x)
    return a


# Make NumPy arrayd with N elements
N = int(100)
x = np.linspace(-1000.0, 1000.0, N)

# Compute sine of NumPy array using NumPy sine function
start_pd = time.perf_counter()
a = np.sin(x)
end_pd = time.perf_counter()
runtime = end_pd - start_pd
print("\nNumPy run time = {0:0.4g} secs".format(runtime))

# Compute sine of NumPy array using Numba
start_pd = time.perf_counter()
a = trig(x)
end_pd = time.perf_counter()
runtime = end_pd - start_pd
print("\nNumba 1st run time = {0:0.4g} secs (incl. compilation time)"
      .format(runtime))
# Compute sine of NumPy array using Numba a 2nd time
start_pd = time.perf_counter()
a = trig(x)
end_pd = time.perf_counter()
runtime = end_pd - start_pd
print("\nNumba 2nd run time = {0:0.4g} secs (w/o compilation time)"
      .format(runtime))
