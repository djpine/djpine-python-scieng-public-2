import numpy as np

def sinc(x):
    z = np.where(x == 0.0, 1.0, np.sin(x) / x)
    return z


x = np.linspace(-10, 10, 255)
y = sinc(x)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y)
ax.axhline(color="gray", lw=0.5, zorder=-1)
ax.axvline(color="gray", lw=0.5, zorder=-1)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$\mathrm{sinc}(x)$")
fig.show()


"""
Introduction to Python for Science & Engineering, 2nd Edition
by David J. Pine
"""
