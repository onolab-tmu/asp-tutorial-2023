import numpy as np
import matplotlib.pyplot as plt
import q03
import q06


def istft_ws_is_1(X, S):
    F = X.shape[0]
    T = X.shape[1]
    N = 2 * (F - 1)
    M = S * (T - 1) + N

    x_hat = np.zeros(M, dtype="complex")
    z = np.zeros((T, N), dtype="complex")
    # ws = q05.optimal_window(np.hamming(N), S)
    ws = np.ones(N)  # すべてのnに対して1

    for t in range(T):
        z[t] = np.fft.irfft(X[:, t])
        x_hat[t * S : t * S + N] += ws * z[t]

    return x_hat


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
    x_hat = q06.istft(X, S)
    x_hat_ws_is_1 = istft_ws_is_1(X, S)

    fig, ax = plt.subplots(2, 1)
    # ax[0].plot(np.abs(x_hat))
    ax[0].plot(x_hat[L - S : L - S + len(x)].real - x)  # 差分
    # ax[1].plot(np.abs(x_hat_ws_is_1))
    ax[1].plot(x_hat_ws_is_1[L - S : L - S + len(x)].real - x)  # 差分
    plt.tight_layout()
    plt.show()

    print(np.sum(np.square(x_hat[L - S : L - S + len(x)] - x)))  # 再構成誤差
    print(np.sum(np.square(x_hat_ws_is_1[L - S : L - S + len(x)] - x)))  # 再構成誤差
