import numpy as np
import matplotlib.pyplot as plt
from q04 import spatial_correlation_matrix
from q05 import stft
from q08 import array_manifold_vector, DS
from q06 import x1, x2, x3


def SpatialSpectrum(z):
    M = z.shape[0]
    L = 1024
    S = 512
    w = np.hanning(L)
    fs = 16000

    # 直線状ビームフォーマ
    d = 0.05
    p_m = np.array([[-d, 0, 0], [0, 0, 0], [d, 0, 0]])

    F, T = stft(L, S, w, z[0]).shape  # FとTの値を取得する

    Z = np.zeros((M, F, T), dtype=complex)

    for m in range(M):
        Z[m] = stft(L, S, w, z[m])

    R = spatial_correlation_matrix(Z)
    # print(R)
    # plt.figure()
    # plt.pcolormesh(20 * np.log10(np.abs(Z[0])))
    # plt.colorbar()
    # plt.savefig("test.png")

    theta_list = np.arange(361)
    f_list = np.array([i * fs / 2 / (F - 1) for i in range(F)])
    f_idx = np.array([i for i in range(20, 31)])
    a = np.zeros((len(f_idx), len(theta_list), M), dtype=complex)
    P = np.zeros(361, dtype=complex)
    for f in range(len(f_idx)):
        for theta in theta_list:
            a[f][theta] = array_manifold_vector(p_m, theta, f_list[f_idx[f]])
            w = DS(a[f][theta])
            P[theta] = (np.conj(w).reshape(1, M) @ R[f_idx[f]]) @ w.reshape(M, 1)
        # print("\n", P, "\n")
        plt.figure()
        plt.plot(theta_list, 20 * np.log10(np.abs(P)))  # STFTの仕様によってy軸の値は変わる
        plt.title("f_bin : " + str(f_idx[f]))
        filename = "5_10_f" + str(f_idx[f]) + ".png"
        plt.savefig(filename)
        plt.close()


if __name__ == "__main__":
    # 6.で用いた信号
    x = np.stack([x1, x2, x3])
    SpatialSpectrum(x)
