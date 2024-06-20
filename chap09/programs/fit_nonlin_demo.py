import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize


# define fitting function
def gauss_poly_base(f, a, b, c, P, fp, fw):
    baseline = a + f * (b + f * c)  # quadratic polynomial
    return baseline + P * np.exp(-0.5 * ((f - fp) / fw) ** 2)


# read in spectrum from data file
# f=frequency, s=signal, ds=s uncertainty
f, s, ds = np.loadtxt("fit_nonlin_demo.txt", skiprows=5, unpack=True)

# initial guesses for fitting parameters
a0, b0, c0 = 0.3, 0.0, 0.0
P0, fp0, fw0 = 0.5, 44.0, 1.0

# fit data using SciPy"s Levenberg Marquart method
nlfit, nlpcov = scipy.optimize.curve_fit(
    gauss_poly_base, f, s, p0=[a0, b0, c0, P0, fp0, fw0], sigma=ds)
# unpack fitting parameters
a, b, c, P, fp, fw = nlfit
# unpack uncertainties in fitting parameters from
# the diagonal of the covariance matrix
da, db, dc, dP, dfp, dfw = [np.sqrt(nlpcov[j, j])
                            for j in range(nlfit.size)]

# create fitting function from fitted parameters
f_fit = np.linspace(36.0, 52.0, 128)
s_fit = gauss_poly_base(f_fit, a, b, c, P, fp, fw)

# Calculate residuals and reduced chi squared
resids = s - gauss_poly_base(f, a, b, c, P, fp, fw)
redchisqr = ((resids / ds) ** 2).sum() / float(f.size - 6)

# Create figure window to plot data
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.5, 6.5), sharex=True,
    gridspec_kw={"height_ratios": [6, 2], "hspace": 0.07})
# Top plot: data and fit
ax1.plot(f_fit, s_fit, "-C0")
ax1.errorbar(f, s, yerr=ds, fmt="oC3", ecolor="gray")
ax1.set_ylabel("absorbance)")
# Write values of fitting parameters on plot
tx = r"$a = {0:0.2f} \pm {1:0.2f}$".format(a, da)
tx += "\n" + r"$b = {0:0.3f} \pm {1:0.3f}$".format(b, db)
tx += "\n" + r"$c = {0:0.5f} \pm {1:0.5f}$".format(c, dc)
tx += "\n" + r"$P = {0:0.3f} \pm {1:0.3f}$".format(P, dP)
tx += "\n" + r"$f_p = {0:0.3f} \pm {1:0.3f}$".format(fp, dfp)
tx += "\n" + r"$f_w = {0:0.3f} \pm {1:0.3f}$".format(fw, dfw)
tx += "\n\n" + r"$\chi_r^2 = {0:0.2g}$".format(redchisqr)
ax1.text(0.01, 0.98, tx, va="top", ha="left", transform=ax1.transAxes)
ax1.set_title(r"$s(f)=a+bf+cf^2+P\,e^{-(f-f_p)^2/2f_w^2}$")
# Bottom plot: residuals
ax2.errorbar(f, resids, yerr=ds, ecolor="gray", fmt="oC3")
ax2.axhline(color="gray", lw=0.5, zorder=-1)
ax2.set_xlabel("frequency (THz)")
ax2.set_ylabel("residuals")
ax2.set_ylim(-0.1, 0.1)
fig.savefig("figures/fit_nonlin_demo.pdf")
plt.show()
