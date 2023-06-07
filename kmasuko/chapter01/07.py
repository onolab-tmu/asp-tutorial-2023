import numpy as np
import matplotlib.pyplot as plt


def snRatio(signal, noise):
    signal_power = np.sum(signal**2)
    noise_power = np.sum(noise**2)

    sn = 10 * np.log10(signal_power / noise_power)

    return sn


def geneMixSignal(signal, sn):
    signal_power = np.sum(signal**2)
    noise = np.random.randn(len(signal))
    noise_power = np.sum(noise**2)
    noise_coef = np.sqrt(signal_power / noise_power / 10 ** (sn / 10))

    noise = noise_coef * noise
    print("snRatio: {}".format(snRatio(signal, noise)))

    mix = signal + noise

    return mix
