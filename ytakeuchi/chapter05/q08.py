import numpy as np
import matplotlib.pyplot as plt
from q03 import calc_amv


def plot_bp(w, p, fs, title=None, sub=None):
    F = len(w[0])
    M = len(p)
    thetas = np.arange(360)
    Psi = []
    for theta in thetas:
        a = []
        for _f in range(F):
            a.append(calc_amv(p, theta, (fs / 2) / (F - 1) * _f))
        a = np.array(a).T
        Psi.append(np.sum(np.conjugate(w) * a, axis=0))
    Psi = np.array(Psi)
    if sub != None:  # subplotを用いる場合（subは配列として入力）
        plt.subplot(sub)
    plt.pcolormesh(thetas, np.arange(F) * fs / 2 / (F - 1), 20 * np.log10(np.abs(Psi.T)))
    if title != None:  # titleを描画する場合（titleは文字列として入力）
        plt.title(title)
    plt.colorbar()
    if sub == None:  # subplotが無い場合はshow
        plt.show()
    return


if __name__ == "__main__":
    theta_eval = [0, 30, 90, 180]
    fs = 16000
    p = np.array([[-0.05, 0, 0], [0, 0, 0], [0.05, 0, 0]])

    plt.subplots_adjust(hspace=0.4, wspace=0.3)
    plt.figure(figsize=(16, 9))
    for i, theta in enumerate(theta_eval):
        w = []
        for _f in range(512):
            w.append(calc_amv(p, theta, (fs / 2) / 511 * _f))
        w = np.array(w).T / 3.0

        plot_bp(w, p, fs, title=f"Beam pattern ({theta} [deg])", sub=220 + i + 1)
    plt.show()
