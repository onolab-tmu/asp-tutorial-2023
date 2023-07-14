import numpy as np
import matplotlib.pyplot as plt


def y(x, n):
    """
    差分方程式（再帰あり）

    Args:
        x(ndarray):入力信号
        n(int):時刻
    Return:
        out(double):出力信号
    """

    if n == 0:
        out = 0.4 * x[n]
    else:
        out = 0.3 * y(x, n - 1) + 0.4 * x[n]

    return out


if __name__ == "__main__":
    length = 10
    x = np.zeros(10)
    x[0] = 1
    signal = [y(x, i) for i in range(length)]
    print(signal)

    plt.figure()
    plt.stem(signal)
    plt.show()
