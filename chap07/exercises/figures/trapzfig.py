from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(1, 1, figsize=(8, 4))
a, b = 0.0, 5.0
h = 0.5 * (b - a)
i, times = 0, 5
ax.plot([a, b], [-1, -1], "ko", ms=5)
for i in range(times):
    n = 2**i
    x = linspace(a + h, b - h, n)
    ax.plot(x, i * np.ones(x.size), "ro", ms=5)
    x = linspace(a, b, n + 1)
    ax.plot(x, i * np.ones(x.size), "ko", ms=5, mfc="white")
    h *= 0.5
ax.set_ylim(times - 0.75, -1.25)
ax.set_yticklabels(range(-1, n))
ax.set_ylabel("$n$")
xticklocs = (a, b)
xticklabs = ("$a$", "$b$")
axR = ax.twinx()
axR.set_ylim(times - 0.75, -1.25)
axR.set_xticks(xticklocs)
axR.set_xticklabels(xticklabs)
yt = [str(2**i) for i in range(-2, times)]
yt[1] = ""
axR.set_yticklabels(yt)
axR.set_ylabel("$2^{n-1}$")
plt.savefig("trapz.pdf")
plt.show()
