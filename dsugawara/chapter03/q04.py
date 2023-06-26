import numpy as np
import matplotlib.pyplot as plt
import q01, q02, q03

if __name__ == "__main__":

    x = np.array([4, 3, 2, 1])
    y = np.array([1, 0, -1, 0])

    result_q01 = q01.liner_conv(x, y)
    result_q02 = q02.cyclic_conv(x, y)
    result_q03 = q03.cyclic_liner_conv(x, y)
    print(result_q01)
    print(result_q02)
    print(result_q03)

    fig = plt.figure(figsize=[6.0, 6.0])
    ax1 = fig.add_subplot(3, 1, 1)
    ax2 = fig.add_subplot(3, 1, 2)
    ax3 = fig.add_subplot(3, 1, 3)
    ax1.stem(result_q01)
    ax2.stem(result_q02)
    ax3.stem(result_q03)
    ax1.set_title("q01 liner convolution")
    ax2.set_title("q02 cyclic convolution")
    ax3.set_title("q03 cyclic convolution")
    fig.tight_layout()
    plt.savefig("q04.pdf")
