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


# 確認
x = [1, 1, 1, 1, 1, 1, 1, 1]
L = 4
S = 3
x_frame = frame_division(x, L, S)

print(x_frame)
print(x_frame.shape)
