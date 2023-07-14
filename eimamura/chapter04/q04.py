import numpy as np
import matplotlib.pyplot as plt


def zero_padding(L, S, x):
    L_S = L - S
    y_1 = []
    y_2 = []
    for i in range(L_S):
        y_1 += [0]
    a = y_1 + x + y_1
    for i in range(100):
        zero = i * S - len(a)
        if zero >= 0:
            for i in range(zero):
                y_2 += [0]
            break
    a += y_2

    return a


def split_frame(L, S, x):
    x_zero = zero_padding(L, S, x)
    T = int((len(x_zero) - L + 1) / S)
    xt = np.zeros((T, L))
    for t in range(T):
        for l in range(L):
            xt[t][l] = x_zero[t * S + l]

    return xt


def STFT(S, w, x):
    L = len(w)
    frame = split_frame(L, S, x)
    a = np.zeros((len(frame), L))
    for i in range(len(frame)):
        a[i] = frame[i] * w
    a = np.fft.rfft(a)

    return a


a = 1
f = 440
fs = 16000
s = 0.1

t = np.arange(0, s, 1 / fs)
y = a * np.sin(2 * np.pi * f * t)
x = y.tolist()

L = 1000
S = 500

w = np.hamming(L)
xt = split_frame(L, S, x)
xstft = STFT(S, w, x)

spec = [np.abs(xstft)]

plt.pcolormesh(np.abs(xstft).T)
plt.show()
plt.pcolormesh(np.angle(xstft).T)
plt.show()
plt.pcolormesh(np.cos(np.angle(xstft)).T)
plt.show()
plt.pcolormesh(np.sin(np.angle(xstft)).T)
plt.show()
