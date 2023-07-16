import numpy as np
import matplotlib.pyplot as plt
import q01
import q02
import q03


if __name__ == "__main__":
    x = np.array([4, 3, 2, 1], dtype=int)
    y = np.array([1, 0, -1, 0], dtype=int)

    print(q01.linear_conv(x, y))  # q01の関数を利用
    print(q02.circular_conv(x, y))  # q02の関数を利用
    print(q03.circular_linear_conv(x, y))  # q03の関数を利用

    print("q01.linear_conv(x,y):\t{}".format(q01.linear_conv(x, y)))
    print("q02.circular_conv(x,y):\t{}".format(q02.circular_conv(x, y)))
    print("q03.circular_linear_conv(x,y):\t{}".format(q03.circular_linear_conv(x, y)))
    plt.plot(q01.linear_conv(x, y))
    plt.plot(q02.circular_conv(x, y))
    plt.plot(q03.circular_linear_conv(x, y))
    plt.show()
