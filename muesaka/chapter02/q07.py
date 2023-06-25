import numpy as np
import matplotlib.pyplot as plt


def hamming(N):
    n = np.arange(N)  # ファンシーインデックス
    w = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return w


if __name__ == "__main__":
    N = 8
    w = hamming(N)
    x = np.arange(N)

    fig, ax = plt.subplots(2, 1, tight_layout=True)  # x, x*wをプロットして確認
    ax[0].stem(x)
    ax[0].set_title("x")
    ax[1].stem(x * w)
    ax[1].set_title("x * w")

    plt.show()
