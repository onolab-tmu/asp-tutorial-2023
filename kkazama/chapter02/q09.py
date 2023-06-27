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

xt_hamming = xt * h

X = np.fft.fft(xt)
X_hamming = np.fft.fft(xt_hamming)

freq = np.arange(len(X)) / len(X) * fs

# 確認
plt.subplot(2, 1, 1)
plt.plot(freq, 20 * np.log10(np.abs(X)))
plt.subplot(2, 1, 2)
plt.plot(freq, 20 * np.log10(np.abs(X_hamming)))
plt.show()
