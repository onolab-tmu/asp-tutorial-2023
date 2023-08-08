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


def beam_pattern(w, p, fs):
    F = w.shape[0]

    deg = np.arange(360)
    f = np.arange(F) * (fs / 2) / (F - 1)
    psi = np.zeros((F, 360), dtype="complex")

    for _f in range(F):
        for theta in range(360):
            a = general_array_manifold_vector(p, theta, f[_f])
            psi[_f, theta] = np.conjugate(w[_f]) @ a

    plt.pcolormesh(deg, f, 20 * np.log10(abs(psi)))
    plt.colorbar()
    plt.show()

    return


if __name__ == "__main__":
    M = 3
    D = np.array([0.02, 0.05, 0.10])
    F = 1000
    fs = 16000

    for d in D:
        w = np.zeros((F, M), dtype="complex")
        p_linear = []
        for m in range(M):
            p_linear.append([((m - 1) - (M - 1) / 2) * d, 0, 0])
        p_linear = np.array(p_linear)

        beam_angle = 0
        f = (fs / 2) / (F - 1) * np.arange(F)
        w = []
        for _f in f:
            w.append(general_array_manifold_vector(p_linear, beam_angle, _f))
        w = np.array(w) / M

        beam_pattern(w, p_linear, fs)
