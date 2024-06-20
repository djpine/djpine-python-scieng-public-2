import numpy as np


def circle(r: float, x0: float, y0: float, n: int
           ) -> (np.ndarray, np.ndarray):
    theta = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    x, y = r * np.cos(theta), r * np.sin(theta)
    return x0 + x, y0 + y


cx, cy = circle(2.0, 1.0, -1.0, 5)
print("cx =", cx)
print("cy =", cy)


"""
Introduction to Python for Science & Engineering, 2nd Edition
by David J. Pine
"""
