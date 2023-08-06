import numpy as np
import matplotlib.pyplot as plt


def general_array_manifold_vector(p, theta, fs):
    c = 334
    u = np.array([np.sin(np.radians(theta)), np.cos(np.radians(theta)), 0])
    M = len(p)
    a = np.zeros(M, dtype="complex")

    for m in range(M):
        a[m] = np.exp(1j * 2 * np.pi * fs / c * u @ p[m])

    return a


def spatial_correlation_matrix(X):
    M, F, T = np.shape(X)
    xft = np.zeros((F, M, T), dtype=np.complex64)
    for f in range(F):
        for m in range(M):
            xft[f][m] = X[m][f]

    R = np.zeros((F, M, M), dtype=np.complex64)
    for f in range(F):
        R[f] = np.dot(xft[f], np.conjugate(xft[f].T)) / T
    return R


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


def calculate_amplitude_from_snr(s, snr):
    a = np.linalg.norm(s)
    x = np.random.randn(round(len(s)))
    x = a * x / (10 ** (snr / 20) * np.linalg.norm(x))
    return x


def spatial_spectrum(z, f):
    L = 1024
    S = 512
    d = 0.05
    fs = 16000
    p = np.array([[-d, 0, 0], [0, 0, 0], [d, 0, 0]])
    win = np.hanning(L)
    M = z.shape[0]

    Z = []
    for m in range(M):
        Z.append(stft(z[m], L, S, win))
    Z = np.array(Z)

    R = spatial_correlation_matrix(Z)
    thetas = np.arange(360)
    w = []
    for theta in thetas:
        a = general_array_manifold_vector(p, theta, fs / 2 / (Z.shape[1] - 1) * f)
        w.append(a / (a.conj() @ a))
    w = np.array(w)

    P = []
    for theta in thetas:
        P.append(np.dot(w[theta].conj(), R[f]) @ w[theta])
    return np.array(P)


if __name__ == "__main__":
    snr = 10
    s = 1
    fs = 16000
    a = 1
    f = 440

    t = np.arange(0, s, 1 / fs)
    y = a * np.sin(2 * np.pi * f * t)

    white_noise = calculate_amplitude_from_snr(y, snr)

    x = np.zeros((3, len(y)))
    for i in range(len(x)):
        x[i] = np.roll(y, i * 10) + white_noise

    for i in range(20, 30):
        plt.plot(np.arange(360), 20 * np.log10(np.abs(spatial_spectrum(x, i))))
        plt.title("bin : " + str(i))
        plt.show()
