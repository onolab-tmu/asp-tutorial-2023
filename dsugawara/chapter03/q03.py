import numpy as np


def padding(x, y):
    """ゼロ詰めを行う
    Args:
        x(ndarray):ゼロ詰めを行う信号
        y(ndarray):ゼロ詰めを行う信号
    Return:
        x_pad(ndarray):ゼロ詰めをした信号
        y_pad(ndarray):ゼロ詰めをした信号
    """
    N = len(x)
    x_pad = np.pad(x, [0, N - 1])
    y_pad = np.pad(y, [0, N - 1])
    return x_pad, y_pad


def cyclic_liner_conv(x, h):
    """ゼロ詰めを行ってから巡回畳み込みを計算
    Args:
        x(ndarray):信号
        h(ndarray):信号
    Return
        z(ndarray):畳み込み結果
    """
    x, h = padding(x, h)
    N = len(x)
    z = np.zeros(N)
    for n in range(0, N):
        for k in range(0, N):
            z[n] += x[k] * h[(n - k) % N]

    return z
