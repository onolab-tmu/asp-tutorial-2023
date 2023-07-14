import numpy as np
import matplotlib.pyplot as plt


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


def ISTFT_ONE(S, X):
    F = X.shape[0]
    T = X.shape[1]
    N = 2 * (F - 1)
    M = S * (T - 1) + N

    one = np.ones(N)
    x = np.zeros(M)
    z = np.zeros((T, N))
    for t in range(T):
        for n in range(N):
            z[t, n] = np.fft.irfft(X[:, t])[n]
            x[t * S + n] += one[n] * z[t, n]

    return x


a = 1
f = 440
fs = 16000
s = 0.1

t = np.arange(0, s, 1 / fs)
x = a * np.sin(2 * np.pi * f * t)


L = 1000
S = 500
w = np.hamming(L)
X = stft(x, L, S, w)
y = ISTFT(S, X)

y1 = ISTFT_ONE(S, X)

plt.figure(figsize=[6.0, 4.0])
plt.plot(y1)
plt.show()


print(np.array([np.max(y), np.min(y)]))
print(np.array([np.max(y1), np.min(y1)]))
