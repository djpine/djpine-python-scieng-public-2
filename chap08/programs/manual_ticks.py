import numpy as np
import matplotlib.pyplot as plt

phi = np.linspace(0.0, 6.0*np.pi, 200)
wave = np.sin(phi)

fig, ax = plt.subplots(figsize=(8.5, 4.5))
ax.plot(phi, wave)
ax.axhline(color="gray", lw=0.5, zorder=-1)
ax.set_xlim(0.0, 6.0)
ax.set_xticks(np.linspace(0.0, 6.0*np.pi, 7))
labels = ["$0$", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$", r"$5\pi$",
          r"$6\pi$"]
ax.set_xticklabels(labels)
ax.set_xlabel(r"$\phi$")
ax.set_ylabel(r"$\sin\phi$")

plt.savefig("./figures/manual_ticks.pdf")
plt.show()


"""
Introduction to Python for Science & Engineering, 2nd Edition
by David J. Pine
"""
