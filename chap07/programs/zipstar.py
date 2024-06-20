import numpy as np

x = [23.1, 45.9, 38.4, 29.7]
y = np.sin(np.array(x))
z = y ** 4

print("\nUsing explicit referencing")
for data in zip(x, y, z):
    print(f"{data[0]:6.1f}, {data[1]:8.3f}, {data[2]:7.2f}")

print("\nUsing implicit referencing")
for data in zip(x, y, z):
    print("{0:6.1f}, {1:8.3f}, {2:7.2f}".format(*data))


"""
Introduction to Python for Science & Engineering, 2nd Edition
by David J. Pine
"""
