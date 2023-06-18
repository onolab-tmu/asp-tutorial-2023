import numpy as np
import matplotlib.pyplot as plt


def hamm(n):
    """Hamming窓を作成
    Args:
        n(int):窓長
    Return:
        w(ndarray):ハミング窓
    """
    k = np.arange(n)
    w = 0.54 - 0.46 * np.cos(2 * np.pi * k / (n - 1))

    return w


if __name__ == "__main__":
    n = 1024
    ham = hamm(n)
    num_ham = np.hamming(n)

    plt.figure()
    plt.plot(ham)
    plt.plot(num_ham)
    plt.show()
