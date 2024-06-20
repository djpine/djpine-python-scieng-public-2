import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def e_field(x, z, d):
    # Return electric dipole vector field E = (ex, ez) at (x, z)
    zp, zn = z - 0.5 * d, z + 0.5 * d  # z-coords of pos & neg charges
    rp2 = x * x + zp * zp  # distance squared from positive charge
    rn2 = x * x + zn * zn  # distance squared from negative charge
    emagpl = 1.0 / rp2  # E-field magnitude from positive charge
    emagmi = 1.0 / rn2  # E-field magnitude from positive charge
    ex = (emagpl / np.sqrt(rp2) - emagmi / np.sqrt(rn2)) * x
    ez = emagpl * zp / np.sqrt(rp2) - emagmi * zn / np.sqrt(rn2)
    return ex, ez


X, Z = np.meshgrid(np.arange(-4.0, 4.01, 0.5),
                   np.arange(-4.0, 4.01, 0.5))
rmask = 1.8  # radius of meshgrid mask
mask = ~(X**2 + Z**2 < rmask**2)  # meshgrid mask

d = 1.0
Ex, Ez = e_field(X[mask], Z[mask], d)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5))
ax1.add_patch(Circle((0, 0), radius=rmask, fc="lightgray", zorder=1))
ax1.quiver(X[mask], Z[mask], Ex, Ez, scale=4.0, pivot="mid", zorder=2)

Ex, Ez = e_field(X, Z, d)
ax2.streamplot(X, Z, Ex, Ez, linewidth=0.75)

for ax in [ax1, ax2]:
    ax.set_aspect("equal")
    ax.plot([0.0, 0.0], [0.5 * d, -0.5 * d], "oC3", zorder=1)
    ax.plot([0.0], [0.5 * d], "+w", zorder=2)
    ax.plot([0.0], [-0.5 * d], "_w", zorder=2)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$z$")

plt.subplots_adjust(left=0.06, right=0.98, top=0.98, bottom=0.05)
plt.savefig("./figures/elec_dipole_vec_field.pdf")
plt.show()


"""
Introduction to Python for Science & Engineering, 2nd Edition
by David J. Pine
"""
