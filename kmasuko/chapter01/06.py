import numpy as np


def snRatio(s, x):
    s_sum = np.sum(s**2)
    x_sum = np.sum(x**2)

    sn = 10 * np.log10(s_sum / x_sum)

    return sn
