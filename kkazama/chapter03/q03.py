mport soundfile as sf
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


# 巡回畳み込み（ゼロ詰め）
def zero_padd_conv(x, h):
    N = len(x)
    x = np.pad(x, (0, N - 1))
    h = np.pad(h, (0, N - 1))

    z = circular_conv(x, h)
    return z
    