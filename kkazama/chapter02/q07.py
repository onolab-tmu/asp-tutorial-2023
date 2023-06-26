import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt


def Hamming(N):
    w = np.zeros(N)
    for n in range(N):
        w[n] = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))

    return w


# 確認
fs = 16000
sec = 3
N = fs * sec
h = Hamming(N)
plt.plot(h)
plt.show()
