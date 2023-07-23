import numpy as np
import matplotlib.pyplot as plt


def optimal_window(w, S):
    L = w.shape[0]
    Q = L // S
    ws = np.zeros(L)

    for l in range(L):
        tmp = 0
        for m in range(1 - Q, Q):
            if (l - m * S) >= 0 and (l - m * S) < L:
                tmp += w[l - m * S] ** 2
        ws[l] = w[l] / tmp

    return ws


if __name__ == "__main__":
    L = 1000
    S = 250
    w = np.hamming(L)

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(w)
    ax[0].set_title("w")
    ax[1].plot(optimal_window(w, S))
    ax[1].set_title("optional_window(w)")
    plt.tight_layout()
    plt.show()
