import math


def sinc(x):
    if x == 0.0:
        return 1.0
    else:
        return math.sin(x) / x
