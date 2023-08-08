import numpy as np
import matplotlib.pyplot as plt


# 合成窓
def window_synth(w, L, S):
    Q = L // S
    w_synth = np.zeros(L)

    for l in range(L):
        w_shift_sum = 0
        for m in range(-(Q - 1), Q):
            if (l - m * S) >= 0 and (l - m * S) < L:
                w_shift_sum += w[l - m * S]**2

        w_synth[l] = w[l] / w_shift_sum

    return w_synth


def istft(X, S):
    F = X.shape[0]
    T = X.shape[1]

    N = 2 * (F - 1)
    M = S * (T - 1) + N

    x = np.zeros(M)
    z = np.zeros((T, N))
    w = np.hamming(N)
    w_synth = window_synth(w)

    for t in range(T):
        for n in range(N):
            z[t][n] = np.fft.irfft(X[:, t])[n]
            x[t * S + n] = x[t * S + n] + w_synth[n] * z[t][n]

    return x
