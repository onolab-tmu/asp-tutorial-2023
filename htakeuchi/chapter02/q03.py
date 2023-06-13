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
delta_DFT = DFT(delta)

# 3
delta_DFT_IDFT = IDFT(delta_DFT)
print(delta_DFT_IDFT)

n = np.arange(len(delta_DFT_IDFT))

plt.figure()
plt.stem(n, delta_DFT_IDFT.real)
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.savefig("2_3.png")