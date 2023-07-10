import numpy as np
import matplotlib.pyplot as plt


def recursive_difference_equation(x):
    y = np.zeros(x.size, dtype=float)  # 結果用の配列

    for n in range(x.size):
        if n == 0:
            y[n] = 0.4 * x[n]  # indexが負にならないようする
        else:
            y[n] = 0.3 * y[n - 1] + 0.4 * x[n]

    return y


if __name__ == "__main__":
    x = np.zeros(10, dtype=int)
    x[0] = 1  # 単位インパルス信号

    print("x:{}".format(x))
    print("recursive_difference_equation(x):{}".format(recursive_difference_equation(x)))

    fix, ax = plt.subplots(2, 1, tight_layout=True)
    ax[0].stem(x)
    ax[0].set_title("x")
    ax[1].stem(recursive_difference_equation(x))
    ax[1].set_title("recursive_difference_equation(x)")
    plt.show()


"""
x:[1 0 0 0 0 0 0 0 0 0]
recursive_difference_equation(x):[4.0000e-01 1.2000e-01 3.6000e-02 1.0800e-02 3.2400e-03 9.7200e-04
 2.9160e-04 8.7480e-05 2.6244e-05 7.8732e-06]

"""
