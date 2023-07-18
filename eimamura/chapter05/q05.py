import numpy as np


def pad(x, L, S):
    x_pad = np.pad(x, [L - S, L - S])
    re = np.mod(x_pad.size, S)
    if re != 0:
        x_pad = np.pad(x_pad, [0, S - re])
    return x_pad


def frame_div(x, L, S):
    x_pad = pad(x, L, S)
    T = int(np.floor((x_pad.size - L) / S)) + 1
    x_t = np.array([x_pad[t * S : t * S + L] for t in range(T)])
    return x_t


def stft(x, L, S, wnd):
    x_t = frame_div(x, L, S)
    T = len(x_t)
    X = np.array([np.fft.rfft(x_t[t] * wnd) for t in range(T)], dtype="complex")
    return X.T


def spatial_correlation_matrix(X):
    M, F, T = np.shape(X)
    xft = np.zeros((F, M, T), dtype=np.complex64)
    for f in range(F):
        for m in range(M):
            xft[f][m] = X[m][f]

    R = np.zeros((F, M, M), dtype=np.complex64)
    for f in range(F):
        R[f] = np.dot(xft[f], np.conjugate(xft[f].T)) / T
    return R


fs = 16000
s = 5

np.random.seed(0)
wn1 = np.random.randn(fs * s)
wn2 = np.random.randn(fs * s)

L = 512
S = 256
win = np.hanning(L)

wn1 = stft(wn1, L, S, win)
wn2 = stft(wn2, L, S, win)
wn = np.stack([wn1, wn2])

a = spatial_correlation_matrix(wn)

print(a[100].real)
