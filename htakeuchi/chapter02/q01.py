import numpy as np
import matplotlib.pyplot as plt

# def DFT(x):
#     N = len(x)
#     X = np.zeros(N, dtype=np.complex128)
#     for k in range(N):
#         for n in range(N):
#             X[k] += x[n] * np.e ** (-1j * 2 * np.pi * k * n / N)
#     return np.round(X,5)

def DFT(x):
    N = len(x)
    n = np.arange(N)
    X = np.zeros(N, dtype=np.complex128)
    for k in range(N):
        X[k] = np.sum( x * np.e ** (-1j * 2 * np.pi * k * n / N))
    return np.round(X,5)

# def IDFT(X):
#     N = len(X)
#     x = np.zeros(N, dtype=np.complex128)
#     for n in range(N):
#         for k in range(N):
#             x[n] += X[k] * np.e ** (1j * 2 * np.pi * k * n / N)
#         x[n] /= N
#     return np.round(x,5)

def IDFT(X):
    N = len(X)
    k = np.arange(N)
    x = np.zeros(N, dtype=np.complex128)
    for n in range(N):
        x[n] = np.sum(X * np.e ** (1j * 2 * np.pi * k * n / N))
    x /= N
    return np.round(x,5)


#確認用
x = [1+0j, 0+0j, -1+0j, 0+0j]
X = DFT(x)   # [0,2,0,2]になるはず
print("DFT( [1,0,-1,0] ) = ", X)
print("IDFT( DFT( [1,0,-1,0] ) ) = ", IDFT(X))

