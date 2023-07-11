import numpy as np


def synth_window(S, w):
    Q = len(w) // S
    ws = np.zeros(len(w))
    for l in range(len(w)):
        sum_w = 0
        for m in range(1 - Q, Q):
            if l - m * S >= 0 and l - m * S < len(w):
                sum_w += w[l - m * S] ** 2
        ws[l] = w[l] / sum_w
    return ws


def istft(S, X):
    F = len(X)
    T = len(X[0])
    N = 2 * (F - 1)
    M = S * (T - 1) + N
    x_hat = np.zeros(M, dtype="complex")
    z = np.zeros((T, 2 * (F - 1)), dtype="complex")
    for t in range(T):
        z[t] = np.fft.irfft(X.T[t])
    ws = synth_window(S, np.hamming(N))
    n = np.arange(N)
    for t in range(T):
        x_hat[t * S + n] = x_hat[t * S + n] + ws[n] * z[t][n]
    return x_hat


##########確認コード##########

# 問題7で確認
