import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def f(r, theta):
    return r**2 * np.exp(-4.0 * ((r * (r - 1.0))**2)) * np.cos(theta)


# Make polar mesh
r = np.linspace(0.0, 2.0, 50)
th = np.linspace(0.0, 2.0 * np.pi, 50)
R, TH = np.meshgrid(r, th)

Z = f(R, TH)
# Translate polar grid to Cartesian grid for plotting
X, Y = R * np.cos(TH), R * np.sin(TH)

fig, ax = plt.subplots(1, 2, figsize=(9.2, 4),
                       subplot_kw={"projection": "3d"})
for i in range(2):
    ax[i].set_xlabel(r"$x$")
    ax[i].set_ylabel(r"$y$")
    ax[i].set_zlabel(r"$f(x,y)$")
    ax[i].view_init(20, -120)

# Plot wireframe and surface plots.
plt.subplots_adjust(left=0.04, bottom=0.04, right=0.96, top=0.96,
                    wspace=0.05)
p0 = ax[0].plot_wireframe(X, Y, Z, rcount=45, ccount=45, color="C0")
# cc = sns.color_palette("YlOrBr_r", as_cmap=True)
cc = sns.color_palette("dark:salmon", as_cmap=True)
p1 = ax[1].plot_surface(X, Y, Z, rcount=45, ccount=45, cmap=cc)
plt.savefig("./figures/surface_polar.pdf")
plt.show()
