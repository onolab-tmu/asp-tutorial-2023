import numpy as np
import matplotlib.pyplot as plt


# ゼロ詰め関数
def zero_pad(x, L, S):
    x = np.pad(x, L - S)

    if len(x) % S != 0:
        x = np.pad(x, (0, S - len(x) % S))

    return x


# フレーム分割
def frame_division(x, L, S):
    x = zero_pad(x, L, S)
    T = (len(x) - L) // S + 1

    x_frame = np.zeros((T, L))

    for t in range(T):
        x_frame[t] = x[t * S : t * S + L]

    return x_frame.T


# 短時間フーリエ変換
def stft(x, L, S, w):
    x_frame = frame_division(x, L, S).T
    T = len(x_frame)
    X = np.zeros((T, L // 2 + 1), dtype=complex)

    for t in range(T):
        x_t = x_frame[t] * w
        X[t] = np.fft.rfft(x_t)

    return X.T


# 確認
A = 1
f = 440
fs = 16000
sec = 0.1

t = np.arange(fs * sec) / fs
x = A * np.sin(2 * np.pi * f * t)

L = 1000
S = 500
w = np.hamming(L)

X = stft(x, L, S, w)

# プロット
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(6, 5))

p0 = ax[0].pcolormesh(np.abs(X))
ax[0].set_title("Amplitude spectrum")

p1 = ax[1].pcolormesh(np.angle(X))
ax[1].set_title("Phase spectrum")

plt.tight_layout()

plt.show()
