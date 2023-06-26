import numpy as np


def conv_circular(x, h):
    """
    巡回畳み込みを計算
    Args:
        x(ndarray):信号
        h(ndarray):インパルス応答
    Return:
        convolved_signal(ndarray):畳み込み信号
    """

    n = len(x)
    x = np.tile(x, (n, 1))
    h = h[::-1]
    conv = np.zeros((n, n), dtype=float)
    for i in range(n):
        conv[i] = np.roll(h, i + 1)

    convolved_signal = np.sum(x * conv, axis=1)

    return convolved_signal


def conv_circular_fft(x, h):
    """
    巡回畳み込みを周波数領域で計算
    Args:
        x(ndarray):信号
        h(ndarray):インパルス応答
    Return:
        convolved_signal(ndarray):畳み込み信号
    """

    x_fft = np.fft.fft(x)
    h_fft = np.fft.fft(h)
    convolved_signal = np.fft.ifft(x_fft * h_fft).real

    return convolved_signal


if __name__ == "__main__":
    x = [1, 0, -1, 2]
    h = [1, 2, 3, 4]

    z1 = conv_circular(x, h)
    z2 = conv_circular_fft(x, h)

    print(z1)
    print(z2)
