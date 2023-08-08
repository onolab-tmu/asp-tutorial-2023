import numpy as np
import matplotlib.pyplot as plt


def syn_window(S, L, win):
    """
    合成窓を計算

    Args:
        S(int):シフト長
        L(int):窓長
        win(ndarray):窓関数
    Return:
        syn_win(ndarray):合成窓関数
    """

    q = L // S
    syn_win = np.zeros(L)

    for l in range(L):
        summary = 0
        for m in range(-(q - 1), q):
            # print(f"{l - m * S}")
            if (l - m * S) >= 0 and (l - m * S) < L:
                summary += win[l - m * S] ** 2
        syn_win[l] = win[l] / summary

    return syn_win


if __name__ == "__main__":
    win_len = 1000
    hop_len = 500
    hamm = np.hamming(win_len)

    plt.figure()
    plt.subplot(2, 2, 1)
    plt.title("Hamming window")
    plt.plot(hamm)

    syn_win = syn_window(int(win_len / 2), win_len, hamm)
    plt.subplot(2, 2, 2)
    plt.title("L = 1000, S = 500")
    plt.plot(syn_win)

    syn_win = syn_window(int(win_len / 4), win_len, hamm)
    plt.subplot(2, 2, 3)
    plt.title("L = 1000, S = 250")
    plt.plot(syn_win)

    syn_win = syn_window(int(win_len / 8), win_len, hamm)
    plt.subplot(2, 2, 4)
    plt.title("L = 1000, S = 125")
    plt.plot(syn_win)
    plt.show()
