import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataFile = ["ref_wavnum_1.txt", "ref_wavnum_2.txt",
            "ref_wavnum_3.txt", "ref_wavnum_4.txt", ]

fig, ax = plt.subplots(figsize=(8.5, 4.5))
c = sns.color_palette("flare_r", 6)  # a Seaborn palette
for i, fname in enumerate(dataFile):
    nu, sig = np.loadtxt(
        "twoScalesData/" + fname, unpack=True, delimiter="\t")
    ax.plot(nu, sig, color=c[i])
ax.set_xlabel("wavenumber [cm$^{-1}$]")
ax.set_ylabel("reflection")
ax.set_ylim(0.0, 1.0)
axtop = ax.twiny()
axtop.set_xlim(ax.get_xlim())
wavelen = np.array([1.0, 1.2, 1.5, 2.0, 2.5])  # microns
axtop.set_xticks(1e4 / wavelen)  # place ticks on top axis
axtop.set_xticklabels(wavelen)
axtop.set_xlabel(r"wavelength [$\mu$m]")

fig.savefig("figures/two_scales.pdf")
plt.show()


"""
Introduction to Python for Science & Engineering, 2nd Edition
by David J. Pine
"""
