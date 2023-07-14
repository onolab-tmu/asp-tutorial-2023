import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt


# 線形畳み込み
def linear_conv(x, h):
    N = len(x)
    z = np.zeros(2 * N - 1)
    for n in range(z.size):
        for k in range(N):
            if n - k >= 0 and n - k <= N - 1:
                z[n] += x[k] * h[n - k]
    return z


# 確認
if __name__ == "__main__":
    x = np.array([3, 2, 1, 0], dtype=int)
    y = np.array([1, 0, 0, 1], dtype=int)

    print(linear_conv(x, y))
