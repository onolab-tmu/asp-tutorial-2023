import numpy as np
import matplotlib.pyplot as plt
import q03


def plot_beampattern(w, p, fs, name="q08"):
    """ビームパターンを描画
    Args:
        w (ndarray): 周波数領域におけるビームフォーマのフィルタ
        p (ndarray): マイクアレイの座標
        fs (int): サンプリング周波数
    """
    F = w.shape[0]
    M = p.shape[1]
    a = np.empty([M, F, 360], dtype="complex")
    psi = np.empty([F, 360], dtype="complex")
    for theta in range(0, 360):
        for f in range(0, F):
            a[:, f, theta] = q03.array_vector(p, theta, (fs / 2) / (F - 1) * f)
            psi[f, theta] = np.dot(np.conjugate(w[f, :].T), a[:, f, theta])

    plt.figure(figsize=[6.0, 4.0])
    plt.pcolormesh(
        np.arange(0, 360),
        np.arange(F),
        20 * np.log10(np.abs(psi)),
        cmap="gray",
        vmin=-20,
    )
    plt.colorbar()
    plt.savefig(f"{name}_d={p[2,0]}.pdf")


if __name__ == "__main__":
    L = 1024
    S = 512
    F = L // 2 + 1
    fs = 16000
    d = 0.05
    p = np.array([[-d, 0, 0], [0, 0, 0], [d, 0, 0]])

    w = np.empty([F, 3], dtype="complex")
    for Fn in range(0, F):
        f = (fs / 2) / (F - 1) * Fn
        w[Fn, :] = q03.array_vector(p, 0, f)
    w = w / 3

    plot_beampattern(w, p, fs)
