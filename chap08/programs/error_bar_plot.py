import numpy as np
import matplotlib.pyplot as plt

# read data from file
xdata, ydata, yerror = np.loadtxt('expDecayData.txt', unpack=True)

# create theoretical fitting curve
x = np.linspace(0, 45, 128)
y = 1.1 + 3.0 * x * np.exp(-(x / 10.0) ** 2)

# create plot
plt.figure(1, figsize=(7, 4))
plt.plot(x, y, '-k', label="theory")
plt.errorbar(xdata, ydata, fmt='oC0', label="data",
             xerr=1.25, yerr=yerror, ecolor='gray')
plt.axhline(color="gray", linewidth=0.5)  # draws line at y=0
plt.xlabel('x')
plt.ylabel('transverse displacement')
plt.legend(loc='upper right')

# save plot to file
plt.savefig('figures/ExpDecay.pdf')

# display plot on screen
plt.show()


"""
Introduction to Python for Science & Engineering, 2nd Edition
by David J. Pine
"""
