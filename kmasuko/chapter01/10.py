import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import math


# 移動平均の補正
def valid_convolve(x, n_filter):
    b = np.ones(n_filter) / n_filter
    x_mean = np.convolve(x, b, mode="same")

    n_conv = math.ceil(n_filter / 2)

    x_mean[0] *= n_filter / n_conv
    for i in range(1, n_conv):
        x_mean[i] *= n_filter / (i + n_conv)
        x_mean[-i] *= n_filter / (i + n_conv - (n_filter % 2))

    return x_mean


filepath = "mix_downsample.wav"
save_filepath = "mix_5mean.wav"
_format = "WAV"
subtype = "PCM_16"
wave, samplerate = sf.read(filepath)

amp = 1
f = 440
fs = 16000
sec = 3
t = np.arange(sec * fs) / fs
x = np.cos(2 * np.pi * f * t)

n_filter = 5
flt = np.ones(n_filter) / n_filter

t_5mean = np.arange(len(wave)) / samplerate
wave_5mean = valid_convolve(wave, n_filter)

sf.write(save_filepath, wave_5mean, samplerate, format=_format, subtype=subtype)

plt.figure()
plt.plot(t_5mean, wave_5mean, label="5mean")
plt.plot(t, x, label="440[Hz]")
plt.xlabel("Time [s]")
plt.xlim(0, 0.01)
plt.legend()
plt.show()
