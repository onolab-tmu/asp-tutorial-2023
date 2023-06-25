import numpy as np
import matplotlib.pyplot as plt


def linear_conv(x, h):  # 線形畳み込み
    N = len(x)
    z = np.zeros(2 * N - 1)
    for n in range(2 * N - 1):
        for k in range(N):
            if not (n - k < 0 or n - k > N - 1):
                z[n] += x[k] * h[n - k]
    return z


# 確認用
x = np.array([0, 1, 2, 3, 4])
h = np.array([1, 3, 5, 7, 9])

print(linear_conv(x, h))  # [4,3,-2,-2,-2,-1,0]になるはず
