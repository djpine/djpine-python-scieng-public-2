import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

def tdl(x):
    y = 8.0 / x
    return np.tan(x) - np.sqrt(y * y - 1.0)

# Find true roots
rx1 = scipy.optimize.brentq(tdl, 0.5, 0.49 * np.pi)
rx2 = scipy.optimize.brentq(tdl, 0.51 * np.pi, 1.49 * np.pi)
rx3 = scipy.optimize.brentq(tdl, 1.51 * np.pi, 2.49 * np.pi)
rx = np.array([rx1, rx2, rx3])
ry = np.zeros(3)
# print true roots using a list comprehension
print("\nTrue roots:")
print("\n".join("f({0:0.5f}) = {1:0.2e}"
                .format(x, tdl(x)) for x in rx))

# Find false roots
rx1f = scipy.optimize.brentq(tdl, 0.49 * np.pi, 0.51 * np.pi)
rx2f = scipy.optimize.brentq(tdl, 1.49 * np.pi, 1.51 * np.pi)
rx3f = scipy.optimize.brentq(tdl, 2.49 * np.pi, 2.51 * np.pi)
rxf = np.array([rx1f, rx2f, rx3f])
# print false roots using a list comprehension
print("\nFalse roots:")
print("\n".join("f({0:0.5f}) = {1:0.2e}"
                .format(x, tdl(x)) for x in rxf))

# Plot function and various roots
x = np.linspace(0.7, 8, 128)
y = tdl(x)
# Create masked array for plotting
ymask = np.ma.masked_where(np.abs(y) > 20.0, y)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, ymask)
ax.axhline(color="black")
ax.axvline(x=np.pi / 2.0, color="gray", linestyle="--", zorder=-1)
ax.axvline(x=1.5 * np.pi, color="gray", linestyle="--", zorder=-1)
ax.axvline(x=2.5 * np.pi, color="gray", linestyle="--", zorder=-1)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$\tan\,x - \sqrt{(8/x)^2-1}$")
ax.set_ylim(-8, 8)

ax.plot(rx, ry, "og", ms=5, mfc="white", label="true roots")

ax.plot(rxf, ry, "xr", ms=5, label="false roots")
ax.legend(numpoints=1, fontsize="small", loc="upper right",
          bbox_to_anchor=(0.9, 0.97))
fig.tight_layout()
fig.savefig("./figures/root_brentq.pdf")
plt.show()
