import numpy as np
import matplotlib.pyplot as plt
import q03


def axis_configuration(X, sr, S):
    F = X.shape[0]
    print(F)
    T = X.shape[1]
    print(T)
    L = (F - 1) * 2
    print(L)
    N = S * (T - 1) + L
    print(N)
    sec = N / sr
    print(sec)

    freq = np.fft.fftfreq(L, 1 / sr)
    f_idx = np.abs(freq[0 : X.shape[0]])
    t_idx = np.linspace(0, sec, T)
    print(t_idx)

    return f_idx, t_idx


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

    f_idx, t_idx = axis_configuration(X, sr, S)

    # プロット
    fig, ax = plt.subplots(2, 1)

    print(t_idx.shape)
    print(f_idx.shape)
    print(np.abs(X).shape)
    # ax[0].pcolormesh(t_idx, f_idx, 10 * np.log10(np.abs(X) ** 2))
    ax[0].pcolormesh(np.abs(X))
    ax[0].set_title("abs")
    print(t_idx[0:5])
    print(np.abs(X)[0])
    print(ax[0].get_xticks())

    ax[1].pcolormesh(t_idx, f_idx, np.angle(X))
    ax[1].set_title("angle")

    plt.tight_layout()
    plt.show()
