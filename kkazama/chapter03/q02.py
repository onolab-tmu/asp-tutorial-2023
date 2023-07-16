import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt


# 巡回畳み込み
def circular_conv(x, h):
    N = len(x)
    z = np.zeros(N, dtype=complex)

    for n in range(N):
        for k in range(N):
            z[n] += x[k] * h[(n - k) % N]

    return z


# 確認
if __name__ == "__main__":
    x = np.array([3, 2, 1, 0], dtype=int)
    y = np.array([1, 0, 0, 1], dtype=int)

    print(circular_conv(x, y))
