import numpy as np
import matplotlib.pyplot as plt

x33 = np.linspace(0, 4. * np.pi, 33)
y33 = np.sin(x33)
x129 = np.linspace(0, 4. * np.pi, 129)
y129 = np.sin(x129)

plt.figure(1, figsize=(9.5, 4))

plt.subplot(1, 2, 1)
plt.plot(x33, y33)

plt.subplot(1, 2, 2)
plt.plot(x129, y129)

plt.tight_layout()

# save plot to file
plt.savefig("figures/sineplot.pdf")

# display plot on screen
plt.show()
