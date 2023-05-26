import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

noise_amp = 1
fs = 16000
sec = 3

filepath = "noise.wav"
_format = "WAV"
subtype = "PCM_16"

t = np.arange(sec * fs) / fs

noise = 2 * noise_amp * (np.random.rand(sec * fs)) - noise_amp

plt.figure()
plt.plot(t, noise)
plt.xlabel("Time [s]")
plt.show()

sf.write(filepath, noise, fs, format=_format, subtype=subtype)
