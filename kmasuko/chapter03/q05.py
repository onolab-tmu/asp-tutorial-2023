import numpy as np
import matplotlib.pyplot as plt


def x(n):
    """
    単位インパルス信号
    Args:
        n(int or ndarray):時刻
    Return:
        impulse(int or ndarray):単位インパルス
    """

    impluse = 0
    if n == 0:
        impluse = 1

    return impluse


def y(n):
    """
    差分方程式（再帰なし）
    Args:
        n(int):時刻
    Return:
        out(double):出力信号
    """

    out = 0.2 * x(n) + 0.2 * x(n - 1) + 0.2 * x(n - 2) + 0.2 * x(n - 3)

    return out


if __name__ == "__main__":
    length = 10
    signal = [y(i) for i in range(length)]

    plt.figure()
    plt.stem(signal)
    plt.show()
