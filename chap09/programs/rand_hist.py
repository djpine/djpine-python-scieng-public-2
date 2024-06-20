import numpy as np
import matplotlib.pyplot as plt

n = 10000
seed = 743923
rng = np.random.default_rng(seed)
r = rng.random(n)              # uniform distribution between 0 & 1
rn = rng.standard_normal(n)    # normal distribution
ps = rng.poisson(10., n)       # Poisson distribution
ntgr = rng.integers(-5, 6, n)  # distribution of integers

fig, ax = plt.subplots(2, 2, figsize=(9, 5.5))
ax[0, 0].hist(r, bins=50, color="C0", rwidth=0.7, range=(0.0, 1.0))
ax[0, 0].set_xlabel(r"$x$")
ax[0, 0].set_ylabel(r"$N(x)$")
ax[0, 0].set_ylim(0.0, 1.1 * ax[0, 0].get_ylim()[1])
ax[0, 0].text(0.05, 0.98, "random({0:d})".format(n),
              ha="left", va="top", transform=ax[0, 0].transAxes)
ax[0, 1].hist(rn, bins=50, color="C1", rwidth=0.7)
ax[0, 1].set_xlabel(r"$x$")
ax[0, 1].set_ylabel(r"$N(x)$")
ax[0, 1].set_xlim(-3.5, 3.5)
ax[0, 1].set_ylim(0.0, 1.1 * ax[0, 1].get_ylim()[1])
ax[0, 1].text(0.05, 0.98, "standard_normal({0:d})".format(n),
              ha="left", va="top", transform=ax[0, 1].transAxes)
ax[1, 0].hist(ntgr, bins=11, range=(-5.5, 5.5), align="mid", color="C2", rwidth=0.8)
ax[1, 0].set_xlabel(r"$n$")
ax[1, 0].set_ylabel(r"$N(n)$")
ax[1, 0].set_ylim(0.0, 1.1 * ax[1, 0].get_ylim()[1])
ax[1, 0].text(0.05, 0.98, "integers(-5, 6, {0:d})".format(n),
              ha="left", va="top", transform=ax[1, 0].transAxes)
ax[1, 1].hist(ps, bins=25, range=(0, 25), color="C3", rwidth=0.8)
ax[1, 1].set_xlabel(r"$n$")
ax[1, 1].set_ylabel(r"$N(n)$")
ax[1, 1].set_ylim(0.0, 1.1 * ax[1, 1].get_ylim()[1])
ax[1, 1].text(0.05, 0.98, "poisson(10., {0:d})".format(n),
              ha="left", va="top", transform=ax[1, 1].transAxes)
fig.tight_layout()

fig.savefig("figures/rand_hist.pdf")
plt.show()
