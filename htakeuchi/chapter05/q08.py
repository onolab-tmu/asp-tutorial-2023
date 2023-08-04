import numpy as np
import matplotlib.pyplot as plt


def array_manifold_vector(coordinate, theta, f):
    """
    theta : 音源方向（度数法）
    theta_rad : 音源方向（弧度法）
    coodinate : 座標の配列．サイズはMであり，m=1に対応する値はcoordinate[0]に格納．
    f : 周波数[Hz]
    a : アレイマニフォールドベクトル．m=1に対応する値をa[0]に格納
    """
    c = 334
    theta_rad = np.pi * theta / 180
    M = coordinate.shape[0]
    a = np.zeros(M, dtype=complex)
    u = np.array([np.sin(theta_rad), np.cos(theta_rad), 0])
    for m in range(M):
        p = np.array([coordinate[m][0], coordinate[m][1], 0])  # m=1に対応するのはcoordinate[0]．
        a[m] = np.exp(1j * 2 * np.pi * f / c * np.sum(u * p))
    return a


def DS(a):
    # a_H = np.conj(a).reshape(1, len(a))
    # a_ = a.reshape(len(a), 1)
    # print(np.dot(a_H, a_))  # len(a)と同じになるはず
    # w = a / np.dot(a_H, a_)
    w = a / len(a)
    return w


def BeamPattern(w_f, p_m, fs, filename):
    F = w_f.shape[0]
    M = w_f.shape[1]  # = p_m.shape[0]
    f_list = np.array([i * fs / 2 / (F - 1) for i in range(F)])
    theta_list = np.arange(361)

    Psi = np.zeros((F, len(theta_list)), dtype=complex)
    for f in range(F):
        for theta in theta_list:
            a_f_theta = array_manifold_vector(p_m, theta, f_list[f])
            w_f_H = np.conj(w_f)
            Psi[f][theta] = np.dot(w_f_H[f].reshape(1, M), a_f_theta.reshape(M, 1))

    plt.figure()
    plt.pcolormesh(theta_list, f_list, 20 * np.log10(np.abs(Psi)))
    plt.savefig(filename)


if __name__ == "__main__":
    fs = 16000
    d = 0.05
    p_m = np.array([[-d, 0, 0], [0, 0, 0], [d, 0, 0]])
    theta = 90
    F = 512
    M = p_m.shape[0]
    f_list = np.array([i * fs / 2 / (F - 1) for i in range(F)])
    a = np.zeros((F, M), dtype=complex)
    for f in range(F):
        a[f] = array_manifold_vector(p_m, theta, f_list[f])
    w_f = DS(a)

    filename = "5_8.png"
    BeamPattern(w_f, p_m, fs, filename)
