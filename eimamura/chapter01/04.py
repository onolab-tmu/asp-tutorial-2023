import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

A = 1.0
sec = 3.0
fs = 16000

x = np.random.rand(round(fs*sec))

plt.plot(x)
plt.show()

x_spec = np.fft.rfft(x)

power = 10 * np.log10(np.abs(x_spec)**2)
freq = np.arange((fs*sec) // 2 + 1) / (fs*sec) * fs

plt.plot(freq,power)