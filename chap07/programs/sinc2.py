import numpy as np

def sinc(x):
    y = []  # empty list to store results
    for xx in x:  # loops over in x array
        if xx == 0.0:  # appends result of 1.0 to
            y += [1.0]  # y list if xx is zero
        else:  # appends result of sin(xx)/xx to y
            y += [np.sin(xx) / xx]  # list if xx is not zero
    # converts y to array and returns array
    return np.array(y)


x = np.linspace(-10, 10, 21)
y = sinc(x)


"""
Introduction to Python for Science & Engineering, 2nd Edition
by David J. Pine
"""
