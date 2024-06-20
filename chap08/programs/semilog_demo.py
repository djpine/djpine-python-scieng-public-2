import numpy as np
import matplotlib.pyplot as plt

# read data from file
time, counts, unc = np.loadtxt("semilog_demo.txt", unpack=True)

# create theoretical fitting curve
t_half = 14.0  # P-32 half life = 14 days
tau = t_half / np.log(2)  # exponential tau
N0 = 8200.0  # Initial count rate (per sec)
t = np.linspace(0, 180, 128)
N = N0 * np.exp(-t / tau)

# create plot
plt.figure(1, figsize=(9.5, 4))

plt.subplot(1, 2, 1)
plt.plot(t, N, color="C0", label="theory")
plt.plot(time, counts, "oC1", label="data")
plt.xlabel("time (days)")
plt.ylabel("counts per second")
plt.legend(loc="upper right")

plt.subplot(1, 2, 2)
plt.semilogy(t, N, color="C0", label="theory")
plt.semilogy(time, counts, "oC1", label="data")
plt.xlabel("time (days)")
plt.ylabel("counts per second")
plt.legend(loc="upper right")

plt.tight_layout()

plt.savefig("figures/semilog_demo.pdf")
plt.show()
