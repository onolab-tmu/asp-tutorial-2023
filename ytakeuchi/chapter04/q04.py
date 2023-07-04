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
    y = np.zeros((len(frames), L // 2 + 1), dtype="complex")  # rfftにより(L/2)+1の配列が返される
    for i in range(len(frames)):
        y[i] = np.fft.rfft(frames[i] * w)
    return y.T


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

t_plt = np.arange(0, l, l / len(X[0]))  # 時間方向のラベルを作成．STFT後のフレーム数に分割
freq_sp = np.fft.fftfreq(L, 1 / fs)  # fftfreq関数により周波数のラベルを作成
f_plt = abs(freq_sp[0 : len(X)])  # STFT後のフレーム長に合わせる

plt.pcolormesh(t_plt, f_plt, np.log10(np.abs(X) ** 2))
plt.colorbar(label="[dB]")
plt.show()  # 440HzにピークがたっていればOK
plt.pcolormesh(t_plt, f_plt, np.angle(X))
plt.colorbar(label="[rad]")
plt.show()
