import numpy as np
import matplotlib.pyplot as plt


def difference_equation(x):
    N = x.size  # 信号の長さ
    y = np.zeros(N, dtype=float)  # 結果用の配列

    NUM_TERMS = 5  # 方程式の項の数
    for n in range(N):
        for i in range(NUM_TERMS):
            if n - i >= 0:
                y[n] += x[n - i] / NUM_TERMS
    return y


if __name__ == "__main__":
    x = np.zeros(10, dtype=int)
    x[1] = 1

    print("difference_equation(x):\t{}".format(difference_equation(x)))
    plt.stem(x)
    plt.stem(difference_equation(x))
    plt.show()


"""
difference_equation(x):	[0.2 0.2 0.2 0.2 0.2 0.  0.  0.  0.  0. ]

"""
