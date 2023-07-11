import numpy as np
import matplotlib.pyplot as plt


def zero_pad(L, S, x):
    y = np.pad(x, (L - S, L - S))
    len_modS = len(y) % S
    if len_modS > 0:
        y = np.pad(y, (0, S - len_modS))
    return y


def frame_split(L, S, x):
    x_tilde = zero_pad(L, S, x)
    L_array = np.arange(L)
    y = x_tilde[L_array].reshape(1, L)
    t = 1
    while t * S + L <= len(x_tilde):
        y = np.append(y, x_tilde[t * S + L_array].reshape(1, L), axis=0)
        t += 1
    return y


def stft(L, S, w, x):
    frames = frame_split(L, S, x)
    y = np.zeros((len(frames), L // 2 + 1), dtype="complex")
    for i in range(len(frames)):
        y[i] = np.fft.rfft(frames[i] * w)
    return y.T


def plot_freq_time(X, fs, S):
    L = (len(X) - 1) * 2  # 窓幅
    N = S * (len(X[0]) - 1) + L  # 元の信号のサンプル数
    l = N / fs  # 元の信号の時間
    t_plt = np.arange(0, l, l / len(X[0]))  # 時間方向のラベル（最初のゼロパディングを負の時間とする流派もある）
    freq_sp = np.fft.fftfreq(L, 1 / fs)  # 周波数のラベル
    f_plt = abs(freq_sp[0 : len(X)])
    plt.pcolormesh(t_plt, f_plt, np.log10(np.abs(X) ** 2))
    plt.colorbar(label="[dB]")
    plt.show()
    return


A = 1
f = 440
fs = 16000
l = 0.1

t = np.arange(0, l, 1 / fs)
x = A * np.sin(2 * np.pi * f * t)

L = 1000
S = 500
w = np.hamming(L)

X = stft(L, S, w, x)
plot_freq_time(X, fs, S)
