import numpy as np
from scipy import linalg


def hermitian(arr):
    return np.conjugate(arr.T)


def calc_scm(X_ft):
    n_mic, F, T = np.shape(X_ft)
    # 空間相関行列の計算
    Rf = np.zeros((F, n_mic, n_mic), dtype=np.complex64)
    # xft = np.zeros((F, n_mic, T), dtype=np.complex64)
    for f in range(F):
        for t in range(T):
            xft = X_ft[:, f, t]
            Rf[f] += np.dot(xft.reshape(n_mic, 1), hermitian(xft.reshape(n_mic, 1)))
    return Rf / T


def main():
    # 以下確認コード
    X1 = np.array([[1, -1j, -1, 1j], [2, -2j, -2, 2j], [3, -3j, -3, 3j]])
    X2 = np.array([[4, -2j, 1, 0], [2, -1j, 0, 0], [1, -1j, 1, 0]])
    x_array = np.array([X1, X2])
    Rf = calc_scm(x_array)
    print(Rf)


if __name__ == "__main__":
    main()
