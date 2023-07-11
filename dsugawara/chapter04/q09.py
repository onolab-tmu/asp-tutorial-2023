import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt
import q03
import q10

if __name__ == "__main__":
    # チャープ信号の生成
    fs = 16000
    sec = 1
    t = np.arange(0, sec, 1 / fs)
    chirp = sp.chirp(t, 100, sec, 16000)

    # 窓幅/シフト幅の変更
    L = np.array([100, 200, 400, 800])
    for i in range(0, len(L)):
        S = L[i] // 2
        win = np.hamming(L[i])
        Chirp = q03.my_stft(L[i], S, chirp, win)

        freq, t = q10.calc_axis(Chirp, fs, S)
        plt.figure(figsize=[6.0, 4.0])
        plt.pcolormesh(t, freq, np.abs(Chirp))
        plt.title(f"L = {L[i]}, S = {S}")
        plt.savefig(f"q09-{i}.png")
