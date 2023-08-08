import numpy as np


# ゼロ詰め関数
def zero_pad(x, L, S):
    x = np.pad(x, L - S)

    if len(x) % S != 0:
        x = np.pad(x, (0, S - len(x) % S))

    return x


# 確認
x = [1, 2, 3]
L = 10
S = 5
x_pad = zero_pad(x, L, S)

print(x_pad)
