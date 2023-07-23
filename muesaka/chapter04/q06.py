import numpy as np
import q05

"""
6と8は再合成誤差
7も1文，なにを追加したか

"""


def istft(X, S):
    F = X.shape[0]
    T = X.shape[1]
    N = 2 * (F - 1)
    M = S * (T - 1) + N

    x_hat = np.zeros(M, dtype="complex")
    z = np.zeros((T, N), dtype="complex")
    ws = q05.optimal_window(np.hamming(N), S)

    for t in range(T):
        z[t] = np.fft.irfft(X.T[t])
        x_hat[t * S : t * S + N] += ws * z[t]

    return x_hat
