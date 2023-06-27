import numpy as np
import matplotlib.pyplot as plt


def recursive_difference_equation(x):
    """再帰ありの差分方程式を計算
    Args:
        x(ndarray):入力信号
    Return:
        y(ndarray):計算結果
    """
    N = len(x)
    y = np.zeros(N)
    for n in range(0, N):
        if n == 0:
            y[n] = 0.4 * x[n]
        else:
            y[n] = 0.3 * y[n - 1] + 0.4 * x[n]

    return y


if __name__ == "__main__":
    x = np.zeros(10)
    x[0] = 1
    y = recursive_difference_equation(x)
    print(y)

    plt.figure(figsize=[6.0, 4.0])
    plt.stem(y)
    plt.savefig("q06.pdf")
