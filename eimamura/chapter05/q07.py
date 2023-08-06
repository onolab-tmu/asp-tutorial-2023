import numpy as np
import matplotlib.pyplot as plt


def pad(x, L, S):
    x_pad = np.pad(x, [L - S, L - S])
    re = np.mod(x_pad.size, S)
    if re != 0:
        x_pad = np.pad(x_pad, [0, S - re])
    return x_pad


def frame_div(x, L, S):
    x_pad = pad(x, L, S)
    T = int(np.floor((x_pad.size - L) / S)) + 1
    x_t = np.array([x_pad[t * S : t * S + L] for t in range(T)])
    return x_t


def stft(x, L, S, wnd):
    x_t = frame_div(x, L, S)
    T = len(x_t)
    X = np.array([np.fft.rfft(x_t[t] * wnd) for t in range(T)], dtype="complex")
    return X.T


def composite(S, w):
    L = len(w)
    Q = int(L / S)
    ws = np.zeros(L)
    a = 0
    for l in range(L):
        for m in range(-(Q - 1), Q):
            if (l - m * S) >= 0 and L > (l - m * S):
                a += w[l - m * S] ** 2
        ws[l] = w[l] / a
        a = 0

    return ws


def istft(S, X):
    F = X.shape[0]
    T = X.shape[1]
    N = 2 * (F - 1)
    M = S * (T - 1) + N

    com = np.hamming(N)
    com1 = composite(S, com)
    x = np.zeros(M)
    z = np.zeros((T, N))
    for t in range(T):
        for n in range(N):
            z[t, n] = np.fft.irfft(X[:, t])[n]
            x[t * S + n] += com1[n] * z[t, n]

    return x


def calculate_amplitude_from_snr(s, snr):
    a = np.linalg.norm(s)
    x = np.random.randn(round(len(s)))
    x = a * x / (10 ** (snr / 20) * np.linalg.norm(x))
    return x


if __name__ == "__main__":
    snr = 10
    s = 1
    fs = 16000
    a = 1
    f = 440
    L = 1024
    S = 512

    t = np.arange(0, s, 1 / fs)
    y = a * np.sin(2 * np.pi * f * t)

    s1 = a * np.sin(2 * np.pi * f * t)
    s2 = np.hstack((np.zeros(10), s1[:-10]))
    s3 = np.hstack((np.zeros(20), s1[:-20]))
    white_noise = calculate_amplitude_from_snr(y, snr)
    x1 = s1 + white_noise
    x2 = s2 + white_noise
    x3 = s3 + white_noise

    wnd = np.hamming(L)
    X1 = stft(x1, L, S, wnd)
    X2 = stft(x2, L, S, wnd)
    X3 = stft(x3, L, S, wnd)

    X = np.stack([X1, X2, X3])
    M, F, T = X.shape

    f = (fs / 2) / (F - 1) * np.arange(F)
    tau1 = 0
    tau2 = 10 / fs
    tau3 = 20 / fs
    w = (
        1
        / 3
        * np.array(
            [
                np.exp(-1j * 2 * np.pi * f * tau1),
                np.exp(-1j * 2 * np.pi * f * tau2),
                np.exp(-1j * 2 * np.pi * f * tau3),
            ]
        )
    )

    Y = np.sum(np.conjugate(w[:, :, None]) * X, axis=0)

    a = istft(S, Y)
    plt.plot(x1)
    plt.plot(a[L - S :])
    plt.xlim([0, 0.01 * fs])
    plt.legend(["obs,(x1)", "enh"])
    plt.show()
