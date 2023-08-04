import numpy as np
import matplotlib.pyplot as plt

from q05 import zero_pad, frame_split, stft
from q06 import make_wn


def synth_window(S, w):
    Q = len(w) // S
    ws = np.zeros(len(w))
    for l in range(len(w)):
        sum_w = 0
        for m in range(1 - Q, Q):
            if l - m * S >= 0 and l - m * S < len(w):
                sum_w += w[l - m * S] ** 2
        ws[l] = w[l] / sum_w
    return ws


def istft(S, X):
    F = len(X)
    T = len(X[0])
    N = 2 * (F - 1)
    M = S * (T - 1) + N
    x_hat = np.zeros(M)
    z = np.zeros((T, 2 * (F - 1)))
    for t in range(T):
        z[t] = np.real(np.fft.irfft(X.T[t]))
    ws = synth_window(S, np.hamming(N))
    n = np.arange(N)
    for t in range(T):
        x_hat[t * S + n] = x_hat[t * S + n] + ws[n] * z[t][n]
    return x_hat


if __name__ == "__main__":
    A = 1
    f = 440
    fs = 16000
    l = 1

    t = np.arange(0, l, 1 / fs)
    s = A * np.sin(2 * np.pi * f * t)
    wn = make_wn(s, 10)

    x = np.zeros((3, len(s)))
    for i in range(len(x)):
        x[i] = np.roll(s, i * 10) + wn

    L = 1024
    S = 512
    w = np.hanning(L)

    X = np.array([stft(L, S, w, x[i]) for i in range(3)])
    F, T = np.shape(X)[1], np.shape(X)[2]  # M,F,T=X.shapeという表記も可能

    x_out = np.zeros((F, T, 3), dtype="complex")
    for f in range(F):
        for t in range(T):
            x_out[f][t] = np.array([X[0][f][t], X[1][f][t], X[2][f][t]])  # 転置していない

    w = np.zeros((F, 3), dtype="complex")
    tau = np.arange(3) * 10 / fs
    for f_idx in range(F):
        f = fs / 2 / (F - 1) * f_idx
        w[f_idx] = (
            np.array(
                [np.exp(-2j * np.pi * f * tau[0]), np.exp(-2j * np.pi * f * tau[1]), np.exp(-2j * np.pi * f * tau[2])]
            )
            / 3.0
        )

    Y = np.zeros((F, T), dtype="complex")
    for f in range(F):
        for t in range(T):
            Y[f][t] = np.dot(w[f].conj().T, x_out[f][t].T)

    y = istft(S, Y)
    plt.plot(y)
    plt.show()

    plt.plot(x[0])
    plt.plot(y[L - S :])
    plt.xlim([0, 0.01 * fs])
    plt.legend(["obs", "enh"])
    plt.show()

    y_adjust = y[L - S : len(x[0]) + L - S]
    print(f"Input SNR (x1):\t{10*np.log10(sum(s**2)/sum((x[0]-s)**2)):.2f}")
    print(f"Input SNR (x2):\t{10*np.log10(sum(s**2)/sum((x[1]-np.roll(s,10))**2)):.2f}")
    print(f"Input SNR (x3):\t{10*np.log10(sum(s**2)/sum((x[2]-np.roll(s,20))**2)):.2f}")
    print(f"Output SNR:\t{10*np.log10(sum(s**2)/sum((y_adjust-s)**2)):.2f}")
