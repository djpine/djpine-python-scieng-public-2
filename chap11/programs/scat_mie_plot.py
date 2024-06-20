import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read in data
head = pd.read_table("scat_mie_data.csv", sep="=", nrows=4,
                     comment=",", header=None)
scat = pd.read_csv("scat_mie_data.csv", skiprows=4)

theta = (180. / np.pi) * np.arccos(scat.cos_theta)

fig, ax = plt.subplots(figsize=(6, 4))

ax.semilogy(theta, scat.f1, "o", color="C0", label="F1")
ax.semilogy(theta, scat.f2, "s", mec="C1", mfc="white", zorder=-1,
            label="F2")
ax.set_xlim(0., 180.)
ax.legend(loc="lower left")
ax.set_xlabel("theta (degrees)")
ax.set_ylabel("intensity")
for i in range(4):
    ax.text(0.98, 0.94-i/18, f"{head[0][i]} = {head[1][i]}",
            fontsize=10, ha="right", transform=ax.transAxes)
fig.tight_layout()
fig.savefig("figures/scat_mie_plot.pdf")
fig.show()
