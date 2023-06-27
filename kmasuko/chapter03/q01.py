import numpy as np


def conv_linear(x, h):
    """
    線形畳み込みを計算
    Args:
        x(ndarray):信号
        h(ndarray):インパルス応答
    Return:
        convolved_signal(ndarray):畳み込み信号
    """

    n = len(x)
    x = np.tile(x, (2 * n - 1, 1))
    h = h[::-1]
    conv = np.zeros((2 * n - 1, n), dtype=float)
    for i in range(n):
        conv[i, : i + 1] = h[n - (i + 1) :]
    for i in range(n, 2 * n - 1):
        conv[i, (i + 1) - n :] = h[: 2 * n - (i + 1)]

    convolved_signal = np.sum(x * conv, axis=1)

    return convolved_signal


def conv_linear2(x, h):
    """
    線形畳み込みを計算
    Args:
        x(ndarray):信号
        h(ndarray):インパルス応答
    Return:
        convolved_signal(ndarray):畳み込み信号
    """

    n = len(x)
    convolved_signal = np.zeros(2 * n - 1)
    for i in range(2 * n - 1):
        for j in range(n):
            if (i - j <= n - 1) and (i - j >= 0):
                convolved_signal[i] += x[j] * h[i - j]

    return convolved_signal


if __name__ == "__main__":
    x = [1, 0, -1, 2]
    h = [1, 2, 3, 4]

    z1 = conv_linear(x, h)
    z2 = conv_linear2(x, h)

    print(z1)
    print(z2)
