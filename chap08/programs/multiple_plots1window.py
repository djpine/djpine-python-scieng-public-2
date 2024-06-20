import numpy as np
import matplotlib.pyplot as plt


# Define the sinc function, with output for x=0
# defined as a special case to avoid division by zero
def sinc(x):
    a = np.where(x == 0.0, 1.0, np.sin(x) / x)
    return a


x = np.arange(0.0, 10.0, 0.1)
y = np.exp(x)

t = np.linspace(-15.0, 15.0, 150)
z = sinc(t)

# create a figure window
fig = plt.figure(figsize=(9, 7))

# subplot: linear plot of exponential
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(x, y, "C0")
ax1.set_ylabel("distance (mm)")
ax1.set_title("exponential")

# subplot: semi-log plot of exponential
ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(x, y, "C2")
ax2.set_yscale("log")
# ax2.semilogy(x, y, 'C2')  # same as 2 previous lines
ax2.set_ylabel("distance (mm)")
ax2.set_title("exponential")

# subplot: wide subplot of sinc function
ax3 = fig.add_subplot(2, 1, 2)
ax3.plot(t, z, "C3")
ax3.axhline(color="gray")
ax3.axvline(color="gray")
ax3.set_ylabel("electric field")
ax3.set_title("sinc function")

for xl in [ax1, ax2, ax3]:
    xl.set_xlabel("time")

# fig.tight_layout() adjusts white space to
# avoid collisions between subplots
fig.tight_layout()
fig.savefig("figures/multiple_plots1window.pdf")
plt.show()
