import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

c0 = sns.color_palette()  # default color palette (matplotlib)
c1 = sns.color_palette("rocket", 4)  # a Seaborn palette

xl = np.linspace(-8.0, 8.0, 200)
plt.figure(figsize=(7, 4))
for i, curvature in enumerate([0.1, 0.3, 0.9, 2.7]):
    xp = np.linspace(-8.0, 8.0, 20 * (i + 1))
    yy = 0.25 + curvature * xl**2
    plt.plot(xl, yy + 0.5 * i, color=c0[i])
    plt.plot(xl, -yy - 0.5 * i, color=c1[i])
    yy = 0.25 + curvature * xp**2
    plt.plot(xp, yy + i / 2, "o", color=c0[i], mec="black", mew=0.5)
    plt.plot(xp, -yy - i / 2, "o", color=c1[i], mec="black", mew=0.5)

plt.axhline(color="gray", lw=0.5, zorder=-2)  # draw x-axis
plt.axvline(color="gray", lw=0.5, zorder=-2)  # draw y-axis
plt.xlim(-8.0, 8.0)
plt.ylim(-8.0, 8.0)
plt.text(-6.0, 7.8, "Default\n  palette", va="top", ha="right")
plt.text(-6.0, -7.8, "Rocket\npalette", va="bottom", ha="right")

plt.tight_layout()
plt.savefig("figures/snscolors.pdf")
plt.show()
