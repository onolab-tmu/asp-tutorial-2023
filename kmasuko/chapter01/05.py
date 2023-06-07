import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


amp = 1
f = 440
fs = 16000
sec = 3

filepath = "mix.wav"
_format = "WAV"
subtype = "PCM_16"

t = np.arange(sec * fs) / fs

noise = np.random.randn(sec * fs)
y = amp * np.cos(2 * np.pi * f * t)

mix = y + noise

plt.figure()
plt.plot(t, mix)
plt.xlabel("Time [s]")
plt.show()

sf.write(filepath, mix, fs, format=_format, subtype=subtype)
