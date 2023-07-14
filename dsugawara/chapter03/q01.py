import numpy as np


def liner_conv(x, h):
    """線形畳み込みを計算
    Args:
        x(ndarray):信号
        h(ndarray):信号
    Return
        z(ndarray):畳み込み結果
    """
    N = len(x)
    z = np.zeros(2 * N - 1)
    for n in range(0, 2 * N - 1):
        for k in range(0, N):
            if n - k >= 0 and n - k <= N - 1:
                z[n] += x[k] * h[n - k]

    return z
