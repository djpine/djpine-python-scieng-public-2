import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

width = 2.0
freq = 0.5

t = np.linspace(-10, 10, 128)
g = np.exp(-np.abs(t) / width) * np.sin(2.0 * np.pi * freq * t)
dt = t[1] - t[0]  # increment between times in time array

G = fftpack.fft(g)  # FFT of g
f = fftpack.fftfreq(g.size, d=dt)  # FFT frequenies
f = fftpack.fftshift(f)  # shift freqs from min to max
G = fftpack.fftshift(G)  # shift G order to match f

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6))
ax1.plot(t, g)
ax1.set_xlabel(r"$t$")
ax1.set_ylabel(r"$g(t)$")
ax1.set_ylim(-1, 1)
ax2.plot(f, np.real(G), color="C0", label="real part")
ax2.plot(f, np.imag(G), color="C1", label="imaginary part")
ax2.legend()
ax2.set_xlabel(r"$f$")
ax2.set_ylabel(r"$G(f)$")
for ax in (ax1, ax2):
    ax.axhline(color="gray", lw=0.5, zorder=-1)
    ax.axvline(color="gray", lw=0.5, zorder=-1)
plt.tight_layout()
plt.savefig("figures/fft_example.pdf")
plt.show()
