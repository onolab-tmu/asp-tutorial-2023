import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


def SN(s, x):
    pow_s = np.sum(s**2)
    pow_x = np.sum(x**2)

    return 10 * np.log10(pow_s / pow_x)


a = np.array([3, 4, 5])
b = np.array([1, 2, 3])

print(SN(a, b))


def Wn(s, x, snr):
    pow_s = np.sum(s**2)
    pow_x = np.sum(x**2)

    x = np.sqrt(pow_s / pow_x / 10 ** (snr / 10))
    return x


def add_white_noise_with_snr(s, snr):
    white_noise = np.random.rand(len(s))
    coef = Wn(s, white_noise, snr)

    return s + coef * white_noise


snr = 0
s = 3
fs = 16000
a = 1
f = 440

t = np.arange(0, s, 1 / fs)
y = a * np.sin(2 * np.pi * f * t)
mix = add_white_noise_with_snr(y, snr)

wn = mix - y
print(SN(y, wn))
