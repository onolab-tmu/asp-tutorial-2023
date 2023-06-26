import numpy as np
import q01
import q02


def circular_linear_convolution(x, h):
    N = x.size  # 信号の長さ

    x_pad = np.pad(x, (0, N - 1))  # 0埋め
    h_pad = np.pad(h, (0, N - 1))  # 0埋め
    return q02.circular_convolution(x_pad, h_pad)  # q02の関数を利用


if __name__ == "__main__":
    # x = np.array([3, 2, 1, 0], dtype=int)
    x = np.array([1, 1, 1, 1], dtype=int)

    # y = np.array([1, 0, 0, 1], dtype=int)
    y = np.array([1, 1, 1, 1], dtype=int)

    print("q01.linear_convolution(x,y):\t{}".format(q01.linear_convolution(x, y)))
    print("circular_linear_convolution(x,y):\t{}".format(circular_linear_convolution(x, y)))


"""
[3 2 1 3 2 1 0]
[3 2 1 3 1 1 0]

"""
