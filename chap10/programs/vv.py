import numpy as np
import scipy.special
import matplotlib.pyplot as plt
from scipy.constants import Boltzmann as kB


class VVautocorr():
    """
    Calculates velocity autocorrelation function of colloidal particle
    suspended in a liquid.  All units are in SI.
    """

    def __init__(self, diameter=1.0e-6, dens_p=1050.0,  dens_f=998.2,
                 viscosity=1.0016e-3, vel_sound=1484.0, tempC=20.0):
        self.diameter = diameter           # particle diameter
        self.radius = 0.5 * self.diameter
        self.dens_p = dens_p               # particle mass density
        self.dens_f = dens_f               # fluid mass density
        self.viscosity = viscosity         # fluid viscostiy
        self.vel_sound = vel_sound         # sound velocity in fluid
        self.tempC = tempC                 # temperature degrees C
        self.tempK = tempC + 273.15
        self.mass_p = 4.0 * np.pi * self.radius**3 / 3.0 * self.dens_p
        self.mass_f = 4.0 * np.pi * self.radius**3 / 3.0 * self.dens_f
        self.mstar = self.mass_p + 0.5 * self.mass_f
        zeta = 6.0 * np.pi * self.viscosity * self.radius
        self.tauVort = dens_f * self.radius**2 / self.viscosity
        self.tauSound = self.radius / self.vel_sound
        self.tauVisc = self.mass_p / zeta

    def hinchVV(self, time):  # [seconds] NumPy array or single value
        # Velocity autocorrelation function from
        # Hinch, J. Fluid Mech. 72, 499 (1975)
        rhoRatio = self.dens_p / self. dens_f
        alpha = 1.5 / (np.sqrt(self.tauVort) * (1.0 + 2.0 * rhoRatio))
        dsc = np.sqrt((5.0 - 8.0 * rhoRatio) + 0j)
        alphaPlus = alpha * (3.0 + dsc)
        alphaMinus = alpha * (3.0 - dsc)
        A = kB * self.tempK / (2.0 * np.pi * self.radius**3 *
                            self.dens_p * dsc) * np.sqrt(self.tauVort)
        roott = np.sqrt(time)
        RPlus = alphaPlus * np.exp(alphaPlus * alphaPlus * time) \
                          * scipy.special.erfc(alphaPlus * roott)
        RMinus = alphaMinus * np.exp(alphaMinus * alphaMinus * time) \
                            * scipy.special.erfc(alphaMinus * roott)
        # Imaginary part is zero
        return np.real(A * (RPlus - RMinus))

    def langevinVV(self, time):
        # Velocity autocorrelation function from naive Langevin eqn
        vsqrd = kB * self.tempK / self.mass_p
        return vsqrd * np.exp(-time / self.tauVisc)

    def zwanzigVV(self, time):
        # Compressibility effect on velocity autocorrelation function
        # Zwanzig & Bixon, J. Fluid Mech. 69, 21 (1975)
        t = time / self.tauSound
        mratio = self.mstar / self.mass_p
        msqrt = np.sqrt(0j + 1.0 - (0.5 * self.mass_f/self.mass_p)**2)
        mrati = 1j * mratio / msqrt
        x1 = -1j * mratio + msqrt
        x2 = -1j * mratio - msqrt
        w1 = (1.0 - mrati) * np.exp(-1j * x1 * t)
        w2 = (1.0 + mrati) * np.exp(-1j * x2 * t)
        w = (0.25 * self.mass_f / self.mstar) * np.real(w1 + w2)
        return (self.mass_p / self.mstar) + w


if __name__ == "__main__":
    a = VVautocorr()  # instantiate with default variable values

    npts = 100
    tmin = 0.02 * a.tauSound
    tmax = 50.0 * a.tauVort
    t = np.logspace(np.log10(tmin), np.log10(tmax), npts)
    vvHinch = a.hinchVV(t)
    vvZwanzig = a.zwanzigVV(t)
    full = (a.mstar / a.mass_p) * vvHinch * vvZwanzig
    vvLangevin = a.langevinVV(t)

    fig, ax = plt.subplots(figsize=(6.5, 4.0))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.plot(t, full, lw=2, color="k", label="full model")
    ax.plot(t, vvHinch, lw=1, color="gray",
            dashes=(2, 2), label="incompressible model")
    ax.plot(t, vvLangevin, lw=1, color="C0",
            zorder=-2, label="naive model")
    vSqrd = kB * a.tempK / a.mass_p
    ax.set_ylim(vvHinch[-1], 2.0 * vSqrd)
    ax.set_xlabel(r"$t\ \mathrm{(seconds)}$")
    ax.set_ylabel(r"$\langle v(0)v(t) \rangle\ \mathrm{(m^2/s^2)}$")
    # Equipartition line
    ax.axhline(vSqrd, color="gray", dashes=(5, 2))
    ax.text(t[-10], vSqrd, "$k_BT/m$", va="center", ha="right",
            bbox=dict(fc="white", ec="white"))
    ax.legend()
    plt.tight_layout()
    plt.savefig("figures/vv.pdf")
    plt.show()
