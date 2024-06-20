def deriv(f, x, h=1.e-9, **params):
    return (f(x + h, **params) - f(x - h, **params)) / (2. * h)


"""
Introduction to Python for Science & Engineering, 2nd Edition
by David J. Pine
"""
