import numpy as np


def cyclic_conv(x, h):
    """巡回畳み込みを計算
    Args:
        x(ndarray):信号
        h(ndarray):信号
    Return
        z(ndarray):畳み込み結果
    """
    N = len(x)
    z = np.zeros(N)
    for n in range(0, N):
        for k in range(0, N):
            z[n] += x[k] * h[(n - k) % N]

    return z
