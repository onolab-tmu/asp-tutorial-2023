from q01 import dft
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    x = np.zeros(8)
    x[0] = 1
    x_dft = dft(x)
    x_npdft = np.fft.fft(x)

    plt.figure("自作dft")
    plt.subplot(1, 2, 1)
    plt.plot(np.abs(x_dft))
    plt.xlabel("k")
    plt.ylabel("|X[k]|")

    plt.subplot(1, 2, 2)
    plt.plot(np.angle(x_dft))
    plt.xlabel("k")
    plt.ylabel("∠X[k]")
    plt.show()

    plt.figure("Numpy_fft")
    plt.subplot(1, 2, 1)
    plt.plot(np.abs(x_npdft))
    plt.xlabel("k")
    plt.ylabel("|X[k]|")

    plt.subplot(1, 2, 2)
    plt.plot(np.angle(x_npdft))
    plt.xlabel("k")
    plt.ylabel("∠X[k]")
    plt.show()
