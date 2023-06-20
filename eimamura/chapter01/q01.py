import numpy as np
import matplotlib.pyplot as plt

a = 1
f = 440
fs = 16000
s = 3

t = np.arange(0, s, 1 / fs)
y = a * np.sin(2 * np.pi * f * t)

plt.plot(t, y)

plt.xlim(0, 1 / f)
