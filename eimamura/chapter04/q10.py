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


def calc_axis(X, fs, S):
    """スペクトログラムの縦軸を周波数, 横軸を時間に変換する
    Args:
        X(ndarray): スペクトログラム
        fs(int): サンプリング周波数
        S(int): シフト幅
    Return:
        ax_f(ndarray): 縦軸(周波数)
        ax_t(ndarray): 横軸(時間)
    """

    F = X.shape[0]
    T = X.shape[1]
    L = (F - 1) * 2

    axis_f = np.arange(0, F + 1) / F * fs / 2
    axif_t = (np.arange(0, T + 1) * S - (L - S)) / fs

    return axis_f, axif_t


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

axis_f, axif_t = calc_axis(X, fs, S)

plt.pcolormesh(axif_t, axis_f, np.abs(X))
plt.title(f"amp")
plt.show()

plt.pcolormesh(axif_t, axis_f, np.angle(X))
plt.title(f"phase")
plt.show()
