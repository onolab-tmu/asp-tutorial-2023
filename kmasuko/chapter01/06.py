import numpy as np


def snRatio(signal, noise):
    signal_power = np.sum(signal**2)
    noise_power = np.sum(noise**2)

    sn = 10 * np.log10(signal_power / noise_power)

    return sn
