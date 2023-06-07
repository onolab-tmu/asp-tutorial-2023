import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


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


amp = 1
f = 440
fs = 16000
sec = 3
sn = 6

filepath = "mix_snRatio.wav"
_format = "WAV"
subtype = "PCM_16"

t = np.arange(sec * fs) / fs

x = amp * np.cos(2 * np.pi * f * t)
mix = geneMixSignal(x, sn)

sf.write(filepath, mix, fs, format=_format, subtype=subtype)
