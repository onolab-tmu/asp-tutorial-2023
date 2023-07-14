import numpy as np
import matplotlib.pyplot as plt


# 2
def circular_conv(x, h):
    N = len(x)
    z = np.zeros(N)
    idx = np.arange(N)
    for n in range(N):
        h_idx = np.mod(n - idx, N)
        z[n] = np.sum(x * h[h_idx])
    return z


# 3
def zero_pad_circular_conv(x, y):
    N = len(x)
    x = np.pad(x, (0, N - 1))
    y = np.pad(y, (0, N - 1))
    z = circular_conv(x, y)
    return z


# 確認用
x = np.array([0, 1, 2, 3, 4])
h = np.array([1, 3, 5, 7, 9])

print(zero_pad_circular_conv(x, h))  # 3-1と同じ結果になるはず
