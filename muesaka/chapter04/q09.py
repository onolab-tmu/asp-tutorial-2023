import numpy as np
import scipy.signal as sp
import q03
import matplotlib.pyplot as plt


if __name__ == "__main__":
    f0 = 100
    f1 = 16000
    sr = 16000
    sec = 1
    L = np.array([100, 200, 400, 800])
    S = np.array([50, 100, 200, 400])

    t = np.arange(sr * sec) / sr
    x = sp.chirp(t, f0, sec, f1)

    # プロット
    fig, ax = plt.subplots(2, 2)

    for i in range(len(L)):
        w = np.hamming(L[i])
        X = q03.stft(x, w, L[i], S[i])

        t_idx = np.linspace(0, sec, X.shape[1])
        freq = np.fft.fftfreq(L[i], 1 / sr)
        f_idx = np.abs(freq[0 : X.shape[0]])
        ax[i // 2, i % 2].pcolormesh(t_idx, f_idx, 10 * np.log10(np.abs(X) ** 2))
        ax[i // 2, i % 2].set_title(f"L={L[i]}, S={S[i]}")

    plt.tight_layout()
    plt.show()
