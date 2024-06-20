import numpy as np
import scipy.special
import matplotlib.pyplot as plt

# create a figure window with subplots
fig, ax = plt.subplots(3, 2, figsize=(9.4, 8.1))

# create arrays for a few Bessel functions and plot them
x = np.linspace(0, 20, 256)
j0 = scipy.special.jv(0, x)  # J_0(x)
j1 = scipy.special.jv(1, x)  # J_1(x)
y0 = scipy.special.yv(0, x)  # Y_0(x)
y1 = scipy.special.yv(1, x)  # Y_1(x)
j0_zeros = scipy.special.jn_zeros(0, 6)
ax[0, 0].plot(x, j0, color="C0", label=r"$J_0(x)$")
ax[0, 0].plot(x, j1, color="C1", dashes=(5, 2), label=r"$J_1(x)$")
ax[0, 0].plot(j0_zeros, np.zeros(j0_zeros.size), "oC3", ms=3)
ax[0, 0].plot(x, y0, color="C2", dashes=(3, 2), label=r"$Y_0(x)$")
ax[0, 0].plot(x, y1, color="C3", dashes=(1, 2), label=r"$Y_1(x)$")
ax[0, 0].axhline(color="grey", lw=0.5, zorder=-1)
ax[0, 0].set_xlim(0, 20)
ax[0, 0].set_ylim(-1, 1)
ax[0, 0].text(0.5, 0.95, "Bessel", ha="center", va="top",
              transform=ax[0, 0].transAxes)
ax[0, 0].legend(loc="lower right", ncol=2)

# gamma function
x = np.linspace(-3.5, 6., 3601)
g = scipy.special.gamma(x)
g = np.ma.masked_outside(g, -100, 400)
ax[0, 1].plot(x, g, color="C0")
ax[0, 1].set_xlim(-3.5, 6)
ax[0, 1].axhline(color="grey", lw=0.5, zorder=-1)
ax[0, 1].axvline(color="grey", lw=0.5, zorder=-1)
ax[0, 1].set_ylim(-20, 100)
ax[0, 1].text(0.5, 0.95, "Gamma", ha="center",
              va="top", transform=ax[0, 1].transAxes)

# error function
x = np.linspace(0, 2.5, 256)
ef = scipy.special.erf(x)
ax[1, 0].plot(x, ef, color="C0")
ax[1, 0].set_xlim(0, 2.0)
ax[1, 0].set_ylim(0, 1.1)
ax[1, 0].axhline(y=1., color="grey", lw=0.5, dashes=(5, 2), zorder=-1)
ax[1, 0].text(0.5, 0.97, "Error", ha="center",
              va="top", transform=ax[1, 0].transAxes)

# Airy function
x = np.linspace(-15, 4, 256)
ai, aip, bi, bip = scipy.special.airy(x)
ax[1, 1].plot(x, ai, color="C0", label=r"$Ai(x)$")
ax[1, 1].plot(x, bi, color="C1", dashes=(5, 2), label=r"$Bi(x)$")
ax[1, 1].axhline(color="grey", lw=0.5, zorder=-1)
ax[1, 1].axvline(color="grey", lw=0.5, zorder=-1)
ax[1, 1].set_xlim(-15, 4)
ax[1, 1].set_ylim(-0.5, 0.8)
ax[1, 1].text(0.5, 0.95, "Airy", ha="center",
              va="top", transform=ax[1, 1].transAxes)
ax[1, 1].legend(loc="upper left")

# Legendre polynomials
x = np.linspace(-1, 1, 256)
lp0 = np.polynomial.Legendre.basis(0)(x)  # P_0(x)
lp1 = np.polynomial.Legendre.basis(1)(x)  # P_1(x)
lp2 = np.polynomial.Legendre.basis(2)(x)  # P_2(x)
lp3 = np.polynomial.Legendre.basis(3)(x)  # P_3(x)
ax[2, 0].plot(x, lp0, color="C0", label=r"$P_0(x)$")
ax[2, 0].plot(x, lp1, color="C1", dashes=(5, 2), label=r"$P_1(x)$")
ax[2, 0].plot(x, lp2, color="C2", dashes=(3, 2), label=r"$P_2(x)$")
ax[2, 0].plot(x, lp3, color="C3", dashes=(1, 2), label=r"$P_3(x)$")
ax[2, 0].axhline(color="grey", lw=0.5, zorder=-1)
ax[2, 0].axvline(color="grey", lw=0.5, zorder=-1)
ax[2, 0].set_xlim(-1, 1.)
ax[2, 0].set_ylim(-1, 1.1)
ax[2, 0].text(0.5, 0.9, "Legendre", ha="center",
              va="top", transform=ax[2, 0].transAxes)
ax[2, 0].legend(loc="lower right", ncol=2)

# Laguerre polynomials
x = np.linspace(-5, 8, 256)
lg0 = np.polynomial.Laguerre.basis(0)(x)  # L_0(x)
lg1 = np.polynomial.Laguerre.basis(1)(x)  # L_1(x)
lg2 = np.polynomial.Laguerre.basis(2)(x)  # L_2(x)
lg3 = np.polynomial.Laguerre.basis(3)(x)  # L_3(x)
ax[2, 1].plot(x, lg0, color="C0", label=r"$L_0(x)$")
ax[2, 1].plot(x, lg1, color="C1", dashes=(5, 2), label=r"$L_1(x)$")
ax[2, 1].plot(x, lg2, color="C2", dashes=(3, 2), label=r"$L_2(x)$")
ax[2, 1].plot(x, lg3, color="C3", dashes=(1, 2), label=r"$L_3(x)$")
ax[2, 1].axhline(color="grey", lw=0.5, zorder=-1)
ax[2, 1].axvline(color="grey", lw=0.5, zorder=-1)
ax[2, 1].set_xlim(-5, 7.2)
ax[2, 1].set_ylim(-5, 10)
ax[2, 1].text(0.5, 0.9, "Laguerre", ha="center",
              va="top", transform=ax[2, 1].transAxes)
ax[2, 1].legend(loc="lower left", ncol=2)
plt.tight_layout()
plt.savefig("./figures/special_functions.pdf")
plt.show()

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2022-01-28

Demonstrates calls to SciPy special functions and
plots them.
"""
