import numpy as np
import matplotlib.pyplot as plt

# read data from file
xdata, ydata = np.loadtxt("wavy_pulse_data.txt", unpack=True)

# create x and y arrays for smooth curve
x = np.linspace(-10.0, 10.0, 200)
y = np.sin(x) * np.exp(-((x / 5.0) ** 2))

# create plot
plt.figure(1, figsize=(6, 4))

plt.plot(x, y, "-C0", label="model")  # blue line
plt.plot(xdata, ydata, "oC3", label="data")  # red circle
# label x & y axes
plt.xlabel("x")
plt.ylabel("transverse displacement")
# display legend using labels set in plot function calls
plt.legend(loc="upper right", title="legend")
# draw gray lines behind plotted data for y=0 and x=0
plt.axhline(color="gray", zorder=-1)
plt.axvline(color="gray", zorder=-1)

# save plot to file
plt.savefig("figures/wavy_pulse.pdf")

# display plot on screen
plt.show()
