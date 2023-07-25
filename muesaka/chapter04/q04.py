import numpy as np
import matplotlib.pyplot as plt
import q03

if __name__ == "__main__":
    A = 1
    f = 440
    sr = 16000
    sec = 0.1
    L = 1000
    S = 500

    t = np.arange(sr * sec) / sr
    x = A * np.sin(f * 2 * np.pi * t)
    w = np.hamming(L)

    X = q03.stft(x, w, L, S)

    # プロット
    fig, ax = plt.subplots(2, 1)

    freq_fft = np.fft.fftfreq(L, 1 / sr)
    f_index = np.abs(freq_fft[0 : X.shape[0] + 1])

    ax[0].pcolormesh(np.log10(np.abs(X) ** 2))
    xticks = ax[0].get_xticks()
    yticks = (ax[0].get_yticks())[:-1]
    t_index = np.linspace(0, sec, X.shape[1] + 1)
    f_index = np.linspace(0, sr / 2, len(yticks), dtype=int)

    ax[0].set_xticks(xticks)
    ax[0].set_xticklabels(t_index)

    ax[0].set_yticks(yticks)
    ax[0].set_yticklabels(f_index)
    ax[0].set_title("np.abs(X)")

    ax[1].pcolormesh(np.angle(X))
    ax[1].set_xticks(xticks)
    ax[1].set_xticklabels(t_index)

    ax[1].set_yticks(yticks)
    ax[1].set_yticklabels(f_index)
    ax[1].set_title("np.angle(X)")

    plt.tight_layout()
    plt.show()
