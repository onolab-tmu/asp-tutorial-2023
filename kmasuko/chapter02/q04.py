from q01 import dft
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    x = np.zeros(8)
    x[0] = 1
    # x[3] = 1
    x_dft = dft(x)

    plt.subplot(1, 2, 1)
    plt.plot(np.abs(x_dft))
    plt.xlabel("k")
    plt.ylabel("|X[k]|")

    plt.subplot(1, 2, 2)
    plt.plot(np.unwrap(np.angle(x_dft)))
    plt.xlabel("k")
    plt.ylabel("∠X[k]")
    plt.show()
