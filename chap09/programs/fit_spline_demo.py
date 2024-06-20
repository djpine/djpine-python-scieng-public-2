import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline, UnivariateSpline

# load data from file
xdata, ydata, yunc = np.loadtxt("fit_spline_demo.txt", skiprows=5,
                                unpack=True)
# calculate splines
od1 = interp1d(xdata, ydata)
od3 = interp1d(xdata, ydata, kind=3)
cs = CubicSpline(xdata, ydata, bc_type="natural")
us = UnivariateSpline(xdata, ydata)
usw0 = UnivariateSpline(xdata, ydata, w=1.0 / yunc)
usw3 = UnivariateSpline(xdata, ydata, w=1.0 / yunc, s=3)
# array for plotting splines (many points for smooth plot)
xs = np.linspace(xdata.min(), xdata.max(), 100)

fig, ax = plt.subplots(2, 2, figsize=(9, 6), sharex=True, sharey=True)
ax[0, 0].plot(xs, od3(xs), "-C0", lw=1, zorder=-2,
              label="interp1d (kind=3)")
ax[0, 0].plot(xs, od1(xs), "-C1", lw=1, zorder=-2, dashes=(5, 2),
              label="interp1d")
ax[0, 1].plot(xs, cs(xs), "-C2", lw=1, zorder=-2,
              label="CubicSpline")
ax[1, 0].plot(xs, us(xs), "-C3", lw=1, zorder=-2,
              label="UnivariateSpline")
ax[1, 1].plot(xs, usw0(xs), "-C4", lw=1, zorder=-2,
              label="UnivariateSpline (weighted)")
ax[1, 1].plot(xs, usw3(xs), "-C4", lw=1, zorder=-2, dashes=(5, 2),
              label="UnivariateSpline (weighted, s=3)")
# Calculate and plot derivatives of Cubic and Univariate splines
ax[0, 1].plot(xs, cs.derivative(1)(xs), lw=0.8, zorder=-2,
              dashes=(10, 4), label=r"$dy/dx$")
ax[1, 0].plot(xs, us.derivative(1)(xs), lw=0.8, zorder=-2,
              dashes=(10, 4), label=r"$dy/dx$")
ax[1, 0].plot(xs, us.derivative(2)(xs), lw=0.8, zorder=-2,
              dashes=(4, 4), label=r"$d^2y/dx^2$")
# plot data & annotations on top of spline fits plotted above
abcd = [["(a)", "(b)"], ["(c)", "(d)"]]
for i in range(2):
    for j in range(2):
        ax[i, j].plot(xdata, ydata, "oC0", ms=3, lw=1)
        ax[i, j].legend()
        ax[i, j].text(0.01, 0.98, abcd[i][j], ha="left", va="top",
                      transform=ax[i, j].transAxes)
        ax[i, j].axhline(color="gray", lw=0.5, zorder=-3)
        ax[i, j].set_ylim(-21., 21.)
        if i == 1: ax[i, j].set_xlabel(r"$x$")
        if j == 0: ax[i, j].set_ylabel(r"$y$")
# include error bars for lower right plot (d)
ax[1, 1].errorbar(xdata, ydata, fmt="oC0", ms=3, yerr=yunc,
                  ecolor="gray", elinewidth=1, zorder=-1)

fig.tight_layout()
fig.savefig("figures/fit_spline_demo.pdf")
plt.show()
