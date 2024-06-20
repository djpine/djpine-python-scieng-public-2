"""Creates datan and figure for problem 9.4"""

import numpy as np
import matplotlib.pyplot as plt


w, xi1, dxi1, xi2, dxi2 = np.loadtxt("res.txt", skiprows=2, unpack=True)

dwspan = 0.05 * (w.max() - w.min())
wfit = np.linspace(w.min() - dwspan, w.max() + dwspan, 3 * w.size)

fig, ax = plt.subplots(figsize=(7.5, 5))
ax.errorbar(w, xi1, yerr=dxi1, fmt="o", ms=3, color="C0")

ax.errorbar(w, xi2, yerr=dxi2, fmt="o", ms=3, color="C1")

ax.text(45000.0, 3.4, r"$\chi^{\prime}(\omega)$", color="C0")
ax.text(78000.0, -3.0, r"$\chi^{\prime}(\omega)$", color="C0")
ax.text(70000.0, 3.8, r"$\chi^{\prime\prime}(\omega)$", color="C1")

ax.axhline(color="black", lw=0.5)
ax.set_xlabel(r"$\omega~~\mathrm{[s^{-1}]}$ ")
ax.set_ylabel(r"$\chi(\omega)$ ")

fig.tight_layout()
plt.savefig("res.pdf")
plt.show()
