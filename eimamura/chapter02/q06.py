"""2_6"""

import numpy as np
import matplotlib.pyplot as plt

a = 1
f = 440
fs = 16000
s = 3

t = np.arange(0, s, 1/fs)
y = a * np.sin(2*np.pi*f*t)

sin_DFT = np.fft.fft(y)
power = 10 * np.log10((np.abs(sin_DFT)) ** 2)
phase = np.angle(sin_DFT)
freq = np.fft.fftfreq(len(y), 1/fs)

plt.plot(freq,power)
plt.ylabel('power')
plt.show()
plt.plot(freq,phase)
plt.ylabel('phase')
plt.show()
plt.plot(freq,phase)
plt.ylabel('phase')
plt.xlim(435,445)
plt.show()