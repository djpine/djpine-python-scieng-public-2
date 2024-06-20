import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly

# loads data from text file
xdata, ydata, yunc = np.loadtxt("fit_poly_demo.txt", skiprows=5,
                                unpack=True)
# performs cubic (deg=3) polynomial fit to data
coefs, stats = poly.polyfit(xdata, ydata, deg=3, w=1./yunc, full=True)
# use old polyfit to get covariance matrix that poly.polyfit lacks
c, cov = np.polyfit(xdata, ydata, deg=3, w=1./yunc, cov=True)
# array for plotting fit
xfit = np.linspace(xdata.min(), xdata.max(), 100)

fig, ax = plt.subplots(figsize=(9, 5))
ax.errorbar(xdata, ydata, fmt="oC0", yerr=yunc, ecolor="gray")
ax.plot(xfit, poly.polyval(xfit, coefs), "-C1", zorder=-1)
ax.axhline(lw=0.5, color="k", zorder=-2)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
# get uncertainties from covariance matrix
coef_unc = [np.sqrt(cov[j, j]) for j in range(cov.shape[0])]
# invert order of coefficients for consistency with new polynomials
coef_unc = coef_unc[::-1]
# Print fit results on plot
alphabet = "abcd"
fitxt = r"$f(x)=a+b\,x+c\,x^2+d\,x^3$"
for i in range(stats[1]):
    st = "\n" + r"${0} = {1:0.3g} \pm {2:0.3g}$"
    fitxt += st.format(alphabet[i], coefs[i], coef_unc[i])
chisq_red = stats[0][0]/(ydata.size-stats[1])
fitxt += "\n" + r"$\chi_r^2={0:0.3g}$".format(chisq_red)
ax.text(0.02, 0.99, fitxt, ha="left", va="top",
        transform=ax.transAxes)

fig.savefig("figures/fit_poly_demo.pdf")
plt.show()
