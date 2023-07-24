import numpy as np


def scm(X):

    """空間相関行列（spatial correation matrix）を求める

    Args:
        X (ndarray): 複素数行列

    Return:
        R: 空間相関行列

    """
    M, F, T = X.shape

    R = np.empty([F, M, M], dtype="complex")
    x = np.empty([F, M, T], dtype="complex")
    for f in range(0, F):
        for m in range(0, M):
            x[f, m] = X[m, f]
    for f in range(0, F):
        R[f] = np.dot(x[f], np.conjugate(x[f].T)) / T
    return R


if __name__ == "__main__":
    X1 = np.array([[1, -1j, -1, 1j], [2, -2j, -2, 2j], [3, -3j, -3, 3j]])
    X2 = np.array([[4, -2j, 1, 0], [2, -1j, 0, 0], [1, -1j, 1, 0]])
    X = np.array([X1, X2])

    print(scm(X))
