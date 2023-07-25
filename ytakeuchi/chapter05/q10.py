import numpy as np
import matplotlib.pyplot as plt
from q03 import calc_amv
from q04 import calc_spatial_corr
from q05 import zero_pad, frame_split, stft
from q06 import make_wn


def calc_spatial_sp(z, f):
    L = 1024
    S = 512
    win = np.hanning(L)
    M = len(z)
    Z = []
    for m in range(M):
        Z.append(stft(L, S, win, z[m]))
    Z = np.array(Z)
    R = calc_spatial_corr(Z)
    thetas = np.arange(360)
    p = np.array([[-0.05, 0, 0], [0, 0, 0], [0.05, 0, 0]])
    w = []
    for theta in thetas:
        a = calc_amv(p, theta, (16000 / 2) / (Z.shape[1] - 1) * f)
        w.append(a / (a.conj() @ a))
    w = np.array(w)
    P = []
    for theta in thetas:
        P.append(np.dot(np.dot(w[theta].conj(), R[f]), w[theta]))
    return np.array(P)


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

    plt.subplots_adjust(hspace=0.6, wspace=0.6)
    plt.figure(figsize=(32, 18))
    thetas = np.arange(360)
    for i in range(20, 30):
        P = calc_spatial_sp(x, i)
        plt.subplot(3, 4, i - 19)
        plt.plot(thetas, 20 * np.log10(np.abs(P)))
        plt.title(f"bin: {i} (freq: {8000/511*i:.1f}Hz)")
    plt.show()
