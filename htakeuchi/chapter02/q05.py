import numpy as np
import matplotlib.pyplot as plt

# 1
def DFT(x):
    N = len(x)
    n = np.arange(N)
    X = np.zeros(N, dtype=np.complex128)
    for k in range(N):
        X[k] = np.sum( x * np.e ** (-1j * 2 * np.pi * k * n / N))
    return np.round(X,5)

def IDFT(X):
    N = len(X)
    k = np.arange(N)
    x = np.zeros(N, dtype=np.complex128)
    for n in range(N):
        x[n] = np.sum(X * np.e ** (1j * 2 * np.pi * k * n / N))
    x /= N
    return np.round(x,5)


# 2
delta = [1,0,0,0,0,0,0,0]
print("2-2 で計算したDFT\n", DFT(delta), "\n")


# 5
print("2-5 で計算したDFT\n", np.fft.fft(delta))