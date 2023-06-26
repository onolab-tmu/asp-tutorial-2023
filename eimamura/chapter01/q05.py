import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

a = 1
f = 440
fs = 16000
s = 3

t = np.arange(0, s, 1 / fs)
y = a * np.sin(2 * np.pi * f * t)

A = 1.0
sec = 3.0
fs = 16000

x = np.random.rand(round(fs * sec))

plt.plot(x)
plt.show()

fy = y + x

sf.write("1_5.wav", fy, fs)
plt.plot(fy)
plt.show

plt.plot(t, fy, label="Mix")
plt.plot(t, y, label="Sin wave")
plt.plot(t, x, label="White noise")
plt.xlim(0, 10 / fs)
plt.legend()
plt.show()
