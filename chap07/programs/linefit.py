def linefit(x, y):
    """Returns slope and y-intercept of linear fit to (x,y)
    data set"""
    xavg = x.mean()
    slope = (y * (x - xavg)).sum() / (x * (x - xavg)).sum()
    yint = y.mean() - slope * xavg
    return yint, slope


"""
Introduction to Python for Science & Engineering, 2nd Edition
by David J. Pine
"""
