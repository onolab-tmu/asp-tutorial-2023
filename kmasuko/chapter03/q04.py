import numpy as np
import matplotlib.pyplot as plt

from q01 import conv_linear
from q02 import conv_circular
from q03 import conv_zero_pad


if __name__ == "__main__":
    x = np.array([4, 3, 2, 1])
    y = np.array([1, 0, -1, 0])

    out_conv_linear = conv_linear(x, y)
    out_conv_circular = conv_circular(x, y)
    out_conv_zero = conv_zero_pad(x, y)

    plt.figure("各種畳み込みの関係")
    plt.subplot(1, 3, 1)
    plt.title("conv_linear")
    plt.stem(out_conv_linear)

    plt.subplot(1, 3, 2)
    plt.title("conv_circular")
    plt.stem(out_conv_circular)

    plt.subplot(1, 3, 3)
    plt.title("conv_zero_pad")
    plt.stem(out_conv_zero)
    plt.show()
