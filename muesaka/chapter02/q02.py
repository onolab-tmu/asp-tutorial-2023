import numpy as np
import matplotlib.pyplot as plt
import q01


if __name__ == "__main__":
    x = np.zeros(8, dtype=int)  # 8点のゼロ信号
    x[0] = 1  # xをインパルス信号にする

    calc_X = q01.dft(x)  # dft計算
    print("x:\t{}".format(x))
    print("calc_X:\t{}".format(calc_X))

    fig, ax = plt.subplots(3, 1, tight_layout=True)  # x, calc_Xをプロットして確認
    ax[0].stem(x)
    ax[0].set_title("x")
    ax[1].stem(calc_X.real)
    ax[1].set_title("calc_X.real")
    ax[2].stem(calc_X.imag)
    ax[2].set_title("calc_X.imag")

    plt.show()
