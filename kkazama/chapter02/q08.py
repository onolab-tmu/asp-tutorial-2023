import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt


def Hamming(N):
    w = np.zeros(N)
    for n in range(N):
        w[n] = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))

    return w


# 1.正弦波の生成
A = 1
f = 440
fs = 16000
sec = 3
N = fs * sec

t = np.arange(fs * sec) / fs

xt = A * np.sin(2 * np.pi * f * t)

h = Hamming(fs * sec)

x_hamming = xt * h

# 確認
plt.subplot(2, 1, 1)
plt.plot(t, xt)
plt.subplot(2, 1, 2)
plt.plot(t, x_hamming)
plt.show()
