import numpy as np


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
L = 4
S = 3
x = np.ones(8)
wnd = np.hamming(L)
x_stft = stft(x, L, S, wnd)

print(x_stft)
