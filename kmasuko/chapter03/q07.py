import numpy as np
import matplotlib.pyplot as plt
from q06 import y


def diff_equ(a, b, x):
    """
    差分方程式（一般系）
    Args:
        a(ndarray):係数
        b(ndarray):係数
        x(ndarray):入力信号
    Return:
        y(ndarray):出力信号
    """

    N, M, L = len(a), len(b), len(x)
    y = np.zeros(L)

    for l in range(0, L):
        ay = 0
        bx = 0
        for k in range(1, N):
            if l - k >= 0:
                ay += a[k] * y[l - k]
        for k in range(0, M):
            if l - k >= 0:
                bx += b[k] * x[l - k]

        y[l] = (-ay + bx) / a[0]

    return y


if __name__ == "__main__":
    length = 10
    a = np.zeros(length)
    a[0] = 1
    a[1] = -0.3
    b = np.zeros(length)
    b[0] = 0.4
    x = np.zeros(length)
    x[0] = 1

    y1 = diff_equ(a, b, x)
    print(y1)
    y2 = [y(x, i) for i in range(length)]
    print(y2)

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.stem(y1)

    plt.subplot(1, 2, 2)
    plt.stem(y2)
    plt.show()
