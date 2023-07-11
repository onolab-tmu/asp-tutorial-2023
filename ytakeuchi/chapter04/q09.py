import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp


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


l = 1.0
fs = 16000
t = np.arange(0, l, 1 / fs)
x = chirp(t, f0=100, f1=16000, t1=l)
plt.plot(x)
plt.xlim([0, 1000])
plt.show()
plt.plot(x)
plt.xlim([15000, 16000])
plt.show()  # サンプリング定理により，8000Hzを超える周波数は変換できない

plt.subplots_adjust(hspace=0.6, wspace=0.5)

for i in range(4):
    L = int((2**i) * 100)
    S = int((2**i) * 50)
    w = np.hamming(L)
    X = stft(L, S, w, x)
    t_plt = np.arange(0, l, l / len(X[0]))  # 時間方向のラベル
    freq_sp = np.fft.fftfreq(L, 1 / fs)  # 周波数のラベル
    f_plt = abs(freq_sp[0 : len(X)])

    plt.subplot(2, 2, i + 1)
    plt.pcolormesh(t_plt, f_plt, np.log10(np.abs(X) ** 2))
    plt.colorbar(label="[dB]")
    plt.title(f"L={L}, S={S}")

plt.show()
# 窓幅が大きいほど周波数分解能が高く，小さいほど時間分解能が高い
