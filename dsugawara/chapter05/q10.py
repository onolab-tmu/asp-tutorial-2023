import numpy as np
import matplotlib.pyplot as plt
import q01
import q03
import q05
import q06
import q07
import q08


def spatial_spectrum(z):

    M = z.shape[0]

    L = 1024
    S = 512
    F = L // 2 + 1
    win = np.hanning(L)

    Z = []
    for m in range(0, M):
        Zm = q07.my_stft(L, S, z[m, :], win)
        Z.append(Zm)
    Z = np.array(Z)

    R = q05.scm(Z)

    F = Z.shape[1]
    w = np.empty([F, 360, M], dtype="complex")
    for f in range(0, F):
        for theta in range(0, 360):
            w[f, theta, :] = q01.linear_array_vector(0.05, M, theta, f)

    P = np.empty([F, 360], dtype="complex")
    for f in range(0, F):
        for theta in range(0, 360):
            P[f, theta] = np.conjugate(w[f, theta, :]).T @ R[f, :, :] @ w[f, theta, :]

    for f in range(21, 30):
        plt.figure(figsize=[6.0, 4.0])
        plt.plot(np.arange(0, 360), 20 * np.log10(np.abs(P[f, :])))
        plt.savefig(f"q10_f={f}.pdf")


if __name__ == "__main__":
    M = 3
    d = 0.05

    A = 1.0
    fs = 16000
    sec = 1
    f = 440
    t = np.arange(0, fs * sec) / fs

    s = A * np.sin(2 * np.pi * f * t)

    noise = q06.make_noise(s, 10)

    x1 = s + noise
    s2 = np.pad(s, [10, 0])
    x2 = s2[0 : len(s2) - 10] + noise
    s3 = np.pad(s, [20, 0])
    x3 = s3[0 : len(s3) - 20] + noise

    z = np.stack([x1, x2, x3])

    spatial_spectrum(z)
