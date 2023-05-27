import numpy as np
from matplotlib import pyplot as plt

# 1.正弦波の生成
A = 1
f = 440
fs = 16000
sec = 3

t = np.arange(0, sec, 1 / fs)

x1 = A * np.sin(2 * np.pi * f * t)

plt.xlim(0, 0.03)
plt.plot(t, x1)
plt.show()
