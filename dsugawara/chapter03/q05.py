import numpy as np
import matplotlib.pyplot as plt


def difference_equation(x):
    """差分方程式を計算
    Args:
        x(ndarray):入力信号
    Return:
        y(ndarray):計算結果
    """
    y = np.zeros(len(x))
    for n in range(0, len(x)):
        y[n] = (
            0.2 * x[n]
            + 0.2 * x[n - 1]
            + 0.2 * x[n - 2]
            + 0.2 * x[n - 3]
            + 0.2 * x[n - 4]
        )

    return y


if __name__ == "__main__":
    x = np.zeros(10)
    x[0] = 1
    y = difference_equation(x)

    plt.figure(figsize=[6.0, 4.0])
    plt.stem(y)
    plt.savefig("q05.pdf")
