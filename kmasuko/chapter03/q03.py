import numpy as np
from q01 import conv_linear
from q02 import conv_circular


def conv_zero_pad(x, y):
    """
    ゼロ埋め巡回畳み込みを計算
    Args:
        x(ndarray):信号
        y(ndarray):信号
    Return:
        convolved_signal(ndarray):畳み込み信号
    """

    n = len(x)
    zero = np.zeros(n - 1)
    x = np.concatenate([x, zero], axis=0)
    x = np.tile(x, (2 * n - 1, 1))
    y = np.concatenate([y, zero], axis=0)[::-1]
    conv = np.zeros((2 * n - 1, 2 * n - 1), dtype=float)
    for i in range(2 * n - 1):
        conv[i] = np.roll(y, i + 1)

    convolved_signal = np.sum(x * conv, axis=1)

    return convolved_signal


if __name__ == "__main__":
    x = [1, 0, -1, 2]
    y = [1, 2, 3, 4]

    z1 = conv_zero_pad(x, y)
    z2 = conv_linear(x, y)

    print(z1)
    print(z2)
