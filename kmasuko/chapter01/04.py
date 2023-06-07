import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


filepath = "noise.wav"
_format = "WAV"
subtype = "PCM_16"

fs = 16000
sec = 3
t = np.arange(sec * fs) / fs

noise = np.random.randn(sec * fs)

plt.figure()
plt.subplot(1, 2, 1)
plt.plot(t, noise)
plt.xlabel("Time [s]")
plt.show()

sf.write(filepath, noise, fs, format=_format, subtype=subtype)
