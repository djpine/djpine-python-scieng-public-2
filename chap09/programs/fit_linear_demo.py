import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import polynomial as P
import scipy.stats as ss


def linfit(x, y, w=None, full=False):
    """
    Fit to straight line: f(x) =  a + b x
    Inputs: x, y, and w (1/uncertainty) data arrays with length > 2.
    Ouputs: y-intercept a and slope b of best fit to data.
    """
    if w is None:
        w = w2 = 1.0
        s = x.size
    else:
        w2 = w * w
        s = w2.sum()
    sx = (x * w2).sum()
    sy = (y * w2).sum()
    sxx = (x * x * w2).sum()
    sxy = (x * y * w2).sum()
    d = s * sxx - sx * sx
    a = (sxx * sy - sx * sxy) / d  # y-intercept
    b = (s * sxy - sx * sy) / d  # slope
    if full:
        sig2_slope = s / d
        sig2_yint = sxx / d
        sig2_cross = -sx / d
        cov = np.array([[sig2_yint, sig2_cross],
                        [sig2_cross, sig2_slope]])
        residuals = (((y - a - b * x) * w) ** 2).sum()
        return (a, b), cov, residuals
    else:
        return (a, b)


# loads data from text file
x, y, unc = np.loadtxt("fit_linear_demo.txt", skiprows=5, unpack=True)

# define weighting function from uncertainties
w = 1.0 / unc
# fit data to straight line using linfit fitting routine above
coefs, cov, residuals = linfit(x, y, w=w, full=True)
# make y data from fit for plotting
lfit = coefs[0] + coefs[1] * x
# fit data to using numpy.polynomial.polynomial.polyfit routine
coefsP, statsP = P.polyfit(x, y, deg=1, w=w, full=True)
# get covariance matrix from deprecated np.polyfit routine
cO, covO = np.polyfit(x, y, deg=1, w=w, cov="unscaled")
# fit data with scipy.stats.linregress routine (no weighting possible)
lrout = ss.linregress(x, y)
regfit = lrout.intercept + lrout.slope * x

# linfit output for display in plot legend
a, da = coefs[0], np.sqrt(cov[0, 0])
b, db = coefs[1], np.sqrt(cov[1, 1])
ltxt = "\n'linfit' & 'polyfit' with weights"
ltxt += "\n" + r"$a = {0:0.2f} \pm {1:0.2f}$".format(a, da)
ltxt += "\n" + r"$b = {0:0.3f} \pm {1:0.3f}$".format(b, db)
ltxt += "\n" + r"$\chi^2 = {0:0.3f}$".format(residuals / (y.size-2))

# linregress output for display in plot legend
a, da = lrout.intercept, lrout.intercept_stderr
b, db = lrout.slope, lrout.stderr
rtxt = "\n'linregress' without weights"
rtxt += "\n" + r"$a = {0:0.2f} \pm {1:0.2f}$".format(a, da)
rtxt += "\n" + r"$b = {0:0.3f} \pm {1:0.3f}$".format(b, db)
rtxt += "\n" + r"$r^2 = {0:0.3f}$".format(lrout.rvalue)

fig, ax = plt.subplots(figsize=(9, 5))
ax.errorbar(x, y, yerr=unc, fmt="o")
ax.plot(x, lfit, "-", lw=0.5, zorder=-1, label=ltxt)
ax.plot(x, regfit, "-", lw=0.5, zorder=-1, dashes=(10, 4), label=rtxt)
ax.axhline(color="gray", lw=0.5, zorder=-2)
ax.legend(title=r"$f(x) = a + bx$")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")

plt.savefig("figures/fit_linear_demo.pdf")
plt.show()
