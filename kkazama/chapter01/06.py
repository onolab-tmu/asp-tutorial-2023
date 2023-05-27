import numpy as np

def SNR(s, x):
    snr = 10 * np.log10(np.sum(s * s) / np.sum(x * x))
    return snr
