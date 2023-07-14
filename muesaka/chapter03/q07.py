import numpy as np
import matplotlib.pyplot as plt
import q06


def general_difference_equation(x, a, b):
    y = np.zeros(x.size, dtype=float)  # 結果用の配列

    for n in range(y.size):
        a_sum = 0  # aのsumを保存
        b_sum = 0  # bのsumを保存
        if n == 0:
            y[n] = b[n] * x[n]  # indexが負にならないようにする
        else:
            for k in range(1, a.size):
                if (n - k) >= 0:  # indexが正で
                    a_sum -= a[k] * y[n - k]
                else:
                    continue
            for k in range(0, b.size):
                if (n - k) >= 0:  # indexが正で
                    b_sum += b[k] * x[n - k]
                else:
                    continue
            y[n] = (a_sum + b_sum) / a[0]  # 左辺のa[0]で右辺を割りy[0]を計算

    return y


if __name__ == "__main__":
    x = np.zeros(10, dtype=int)
    x[0] = 1  # 単位インパルス信号

    a = np.zeros(10)
    a[0] = 1
    a[1] = -0.3  # q06と同じ条件

    b = np.zeros(10)
    b[0] = 0.4  # q06と同じ条件

    print("x:{}".format(x))
    print("general_difference_equation(x):{}".format(general_difference_equation(x, a, b)))
    print("recursive_difference_equation(x):{}".format(q06.recursive_difference_equation(x)))

    fix, ax = plt.subplots(3, 1, tight_layout=True)
    ax[0].stem(x)
    ax[0].set_title("x")
    ax[1].stem(general_difference_equation(x, a, b))
    ax[1].set_title("general_difference_equation(x, a, b)")
    ax[2].stem(q06.recursive_difference_equation(x))
    ax[2].set_title("recursive_difference_equation(x)")
    plt.show()


"""
x:[1 0 0 0 0 0 0 0 0 0]
general_difference_equation(x):[4.0000e-01 1.2000e-01 3.6000e-02 1.0800e-02 3.2400e-03 9.7200e-04
 2.9160e-04 8.7480e-05 2.6244e-05 7.8732e-06]
recursive_difference_equation(x):[4.0000e-01 1.2000e-01 3.6000e-02 1.0800e-02 3.2400e-03 9.7200e-04
 2.9160e-04 8.7480e-05 2.6244e-05 7.8732e-06]

"""
