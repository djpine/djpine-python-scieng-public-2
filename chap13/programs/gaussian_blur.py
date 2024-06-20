import numpy as np
import numba
import time
import matplotlib.pyplot as plt


@numba.jit(nopython=True)
def gaussian_blur(image, pxblur):
    # make gaussian filter of radius pxblur
    x = np.exp(-np.linspace(-2.0, 2.0, 2 * pxblur + 1) ** 2)
    fltr = np.outer(x, x)
    fltr /= fltr.mean() * fltr.size  # normalize filter
    # Apply filter (adapted from Numba Read the Docs)
    m, n = image.shape
    mf, nf = fltr.shape
    mf2 = mf // 2
    nf2 = nf // 2
    result = np.zeros(image.shape)
    for i in range(mf2, m - mf2):
        for j in range(nf2, n - nf2):
            num = 0.0
            for ii in range(mf):
                for jj in range(nf):
                    num += (fltr[mf - 1 - ii, nf - 1 - jj] *
                            image[i - mf2 + ii, j - nf2 + jj])
            result[i, j] = num
    # Return blurred image
    return result


# make image of random pixel values and set blur radius (pixels)
rng = np.random.default_rng()
image = rng.random((1024, 1024))
r_blur = 8

# Run calculation twice to determine jit compilation time
for i in range(2):
    start_pd = time.perf_counter()
    res = gaussian_blur(image, r_blur)
    end_pd = time.perf_counter()
    runtime = end_pd - start_pd
    print("\nrun time = {0:0.4g} seconds".format(runtime))

# Plot original image and Gaussian blurred image
fig, ax = plt.subplots(1, 2, figsize=(9.25, 4.6))
ax[0].imshow(image, vmin=0, vmax=image.max(), cmap="viridis")
ax[1].imshow(res, vmin=0, vmax=image.max(), cmap="viridis")
fig.subplots_adjust(top=1.0, bottom=0.02, left=0.05, right=0.99,
                    hspace=0.2, wspace=0.12)

fig.savefig("figures/gaussian_blur.pdf")
fig.show()
