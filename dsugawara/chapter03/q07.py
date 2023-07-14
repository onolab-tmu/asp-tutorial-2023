import numpy as np


def gen_difference_equation(x, a, b):
    """一般系の差分方程式を計算
    Args:
        x(ndarray):入力信号
        a
        b
    Return:
        y(ndarray):計算結果
    """
    L = len(x)
    N = len(a)
    M = len(b)
    y = np.zeros(L)
    for n in range(0, L):
        for k1 in range(1, N):
            if n - k1 >= 0:
                y[n] = y[n] - a[k1] * y[n - k1]
        for k2 in range(0, M):
            if n - k2 >= 0:
                y[n] = y[n] + b[k2] * x[n - k2]

    y = y / a[0]

    return y


if __name__ == "__main__":
    x = np.zeros(10)
    x[0] = 1
    a = [1]
    b = [0.2, 0.2, 0.2, 0.2, 0.2]
    y1 = gen_difference_equation(x, a, b)
    print(y1)

    a = [1.0, -0.3]
    a[0] = 1
    b = [0.4]
    y2 = gen_difference_equation(x, a, b)
    print(y2)
