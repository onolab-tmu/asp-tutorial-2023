import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

# DFTの実装
def dft(x):
    N = len(x)
    X = np.zeros(N)
    for k in range(N):
        a = -1j * 2 * np.pi * k * np.arange(N)
        X[k] = np.sum(x * np.exp(a / N))

    return X

# IDFTの計算
def idft(X):
    N = len(X)
    x = np.zeros(N)
    for n in range(N):
        a = 1j * 2 * np.pi * np.arange(N) * n
        x[n] = np.sum(X * np.exp(a / N))

    x = x / N

    return x

# 8 点の単位インパルス信号
delta = np.zeros(8)
delta[0] = 1
dft_delta = dft(delta)

# 振幅スペクトル
plt.subplot(2, 1, 1)
plt.stem(np.abs(dft_delta))

# 位相スペクトル
plt.subplot(2, 1, 2)
plt.stem(np.angle(dft_delta))

plt.show()
