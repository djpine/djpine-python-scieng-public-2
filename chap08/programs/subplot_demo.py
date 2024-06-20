import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(0.01, 8.0, 0.04)
y = np.sqrt((8.0 / theta) ** 2 - 1.0)
ytan = np.tan(theta)
ytan = np.ma.masked_where(np.abs(ytan) > 20.0, ytan)
ycot = 1.0 / np.tan(theta)
ycot = np.ma.masked_where(np.abs(ycot) > 20.0, ycot)

plt.figure(figsize=(8.5, 6))

plt.subplot(2, 1, 1)
plt.plot(theta, y, linestyle=":")
plt.plot(theta, ytan)
plt.xlim(0, 8)
plt.ylim(-8, 8)
plt.axhline(color="gray", zorder=-1)
plt.axvline(x=0.5 * np.pi, color="gray", linestyle="--", zorder=-1)
plt.axvline(x=1.5 * np.pi, color="gray", linestyle="--", zorder=-1)
plt.axvline(x=2.5 * np.pi, color="gray", linestyle="--", zorder=-1)
plt.xlabel("theta")
plt.ylabel("tan(theta)")

plt.subplot(2, 1, 2)
plt.plot(theta, -y, linestyle=":")
plt.plot(theta, ycot)
plt.xlim(0, 8)
plt.ylim(-8, 8)
plt.axhline(color="gray", zorder=-1)
plt.axvline(x=np.pi, color="gray", linestyle="--", zorder=-1)
plt.axvline(x=2.0 * np.pi, color="gray", linestyle="--", zorder=-1)
plt.xlabel("theta")
plt.ylabel("cot(theta)")

plt.savefig("figures/subplot_demo.pdf")
plt.show()
