import numpy as np
import matplotlib.pyplot as plt

amp = 1
f = 440
fs = 16000
sec = 3

t = np.arange(sec * fs) / fs

y = amp * np.cos(2 * np.pi * f * t)

plt.figure()
plt.plot(t, y)
plt.xlabel("Time [s]")
plt.show()

y_fft = np.fft.fft(2 * y / (sec * fs))
y_freq = np.fft.fftfreq(sec * fs, d=1 / fs)

plt.figure()
plt.plot(y_freq, np.abs(y_fft))
plt.xlim(0, 500)
plt.xlabel("Freq [Hz]")
plt.show()
