import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp
import q03
import q05
import q06

if __name__ == "__main__":

    # 信号の生成
    A = 1
    f = 440
    sec = 0.1
    fs = 16000
    t = np.arange(0, sec, 1 / fs)
    x = A * np.sin(2 * np.pi * f * t)

    # stft
    L = 1000
    S = L // 2
    win = np.hamming(L)
    X = q03.my_stft(L, S, x, win)

    # istft
    win_opt = q05.optimal_win(S, win)
    y = q06.my_istft(S, X, win_opt)

    # plot
    plt.figure(figsize=[6.0, 4.0])
    plt.plot(y)
    plt.savefig("q07.pdf")

    # 再構成誤差の確認
    import q01

    x_pad = q01.padding(L, S, x)
    print(np.sum((x_pad - y) ** 2))
    # output
    # 5.585221535385234e-29
