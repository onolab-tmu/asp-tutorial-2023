import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

# DFTの実装
def dft(x):
    N = len(x)
    X = np.zeros(N)
    for n in range(N):
        a = -1j * 2 * np.pi * np.arange(N) * n
        X[n] = np.sum(x[n] * np.exp(a / N))

    return X

# IDFTの計算
def idft(X):
    N = len(X)
    x = np.zeros(N)
    for n in range(N):
        a = 1j * 2 * np.pi * np.arange(N) * n
        x[n] = np.sum(X[n] * np.exp(a / N))

    x = x / N

    return x
