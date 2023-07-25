import numpy as np


def composite(S, w):
    L = len(w)
    Q = int(L / S)
    ws = np.zeros(L)
    a = 0
    for l in range(L):
        for m in range(-(Q - 1), Q):
            if (l - m * S) >= 0 and L > (l - m * S):
                a += w[l - m * S] ** 2
        ws[l] = w[l] / a

        a = 0

    return ws


def ISTFT(S, X):
    """短時間逆フーリエ変換
    Args:
        S(int):シフト幅
        X(ndarray):入力信号
    Return
        x: 変換後の信号
    """
    F = X.shape[0]
    T = X.shape[1]
    N = 2 * (F - 1)
    M = S * (T - 1) + N

    com = np.hamming(N)
    com1 = composite(S, com)
    x = np.zeros(M)
    z = np.zeros((T, N))
    for t in range(T):
        for n in range(N):
            z[t, n] = np.fft.irfft(X[:, t])[n]
            x[t * S + n] += com1[n] * z[t, n]

    return x


S = 2
X = np.array([[1, 0, 0], [-1j, 0, 0], [-1, 0, 0]])

print(ISTFT(S, X))
