import matplotlib.pyplot as plt
import matplotlib.animation as anim
from PIL import Image
from glob import glob

fig, ax = plt.subplots(figsize=(3.6, 3.5))
fig.subplots_adjust(bottom=0, top=1, left=0, right=1)
ax.axis("off")

ims = []
for fname in sorted(glob("pacb/s0*.png")):
    # print(fname)  # uncomment to follow loading of images
    im = ax.imshow(Image.open(fname), animated=True)
    ims.append([im])

ani = anim.ArtistAnimation(fig, artists=ims, interval=33,
                           repeat=False)
# Uncomment to save as mp4 movie file.  Need ffmpeg.
# ani.save("movies/movie_from_images.mp4", writer="ffmpeg")

fig.show()
