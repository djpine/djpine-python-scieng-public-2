import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

yup = np.array([0, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5])
ydn = np.array([5, 6, 4, 5, 3, 4, 2, 3, 1, 2, 0])
ypk = np.array([0, 2, 1, 3, 2, 4, 2, 3, 1, 2, 0])
x = np.linspace(0, 20, len(yup))

fig, ax = plt.subplots(figsize=(8.5, 4.5))

# Main plot
ax.plot(x, yup, color="C0")
ax.set_xlabel("time", fontsize=12)
ax.set_ylabel("distance", fontsize=12)

# Upper left inset plot
# Inset boundaries are fractions of figure size. (0,0 is bottom left)
left, bottom, width, height = [0.18, 0.61, 0.25, 0.25]
axUL = fig.add_axes([left, bottom, width, height])
axUL.plot(x, ydn, color="C1")

# Lower right inset plot
# Inset boundaries are fractions of figure size. (0,0 is bottom left)
left, bottom, width, height = [0.64, 0.21, 0.25, 0.25]
axLR = fig.add_axes([left, bottom, width, height])
axLR.plot(x, ypk, color="C2")

for axx in [axUL, axLR]:
    axx.set_xlabel("time", fontsize=10)
    axx.set_ylabel("distance", fontsize=10)
    axx.tick_params(labelsize=8)

# Upper middle inset image (large green & small red spheres)
# Inset boundaries are fractions of figure size. (0,0 is bottom left)
left, bottom, width, height = [0.42, 0.66, 0.2, 0.2]
axPIC = fig.add_axes([left, bottom, width, height])
axPIC.axis("off")
axPIC.imshow(Image.open("figures/cs6c60.jpg"))

fig.savefig("figures/inset.pdf")
plt.show()


"""
Introduction to Python for Science & Engineering, 2nd Edition
by David J. Pine
"""
