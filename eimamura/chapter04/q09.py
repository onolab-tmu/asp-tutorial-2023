import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp


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


fs = 16000
s = 1
t = np.arange(0, s, 1 / fs)
chirp = sp.chirp(t, 100, s, 16000)
L = np.array([100, 200, 400, 800])

for i in range(len(L)):
    S = L[i] // 2
    win = np.hamming(L[i])

    Chirp = stft(chirp, L[i], S, win)

    plt.subplot()
    plt.pcolormesh(np.abs(Chirp))
    plt.title(f"L = {L[i]}, S = {S}")
    plt.show()
