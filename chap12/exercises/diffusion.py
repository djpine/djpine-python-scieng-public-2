import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

N = 200
# Create arrays of random jump lengths in random directions
rng = np.random.default_rng()
dr = rng.random(N-1)  # random number 0-1
angle = 2.0 * np.pi * rng.random(N-1)
dx = dr * np.cos(angle)
dy = dr * np.sin(angle)
# Add up the random jumps to make a random walk
x = np.insert(np.cumsum(dx), 0, 0.)  # insert 0 as
y = np.insert(np.cumsum(dy), 0, 0.)  # first point
