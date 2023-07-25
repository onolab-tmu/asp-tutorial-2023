import numpy as np


def spatial_correlation_matrix(X):
    """空間相関行列
    Args:
        X(ndarray): M個のF*Tの複素数行列
    Return:
        R(ndarray): 空間相関行列
    """
    M, F, T = np.shape(X)
    xft = np.zeros((F, M, T), dtype=np.complex64)
    for f in range(F):
        for m in range(M):
            xft[f][m] = X[m][f]

    R = np.zeros((F, M, M), dtype=np.complex64)
    for f in range(F):
        R[f] = np.dot(xft[f], np.conjugate(xft[f].T)) / T
    return R


X1 = np.array([[1, -1j, -1, 1j], [2, -2j, -2, 2j], [3, -3j, -3, 3j]])
X2 = np.array([[4, -2j, 1, 0], [2, -1j, 0, 0], [1, -1j, 1, 0]])
X = np.array([X1, X2])

R = spatial_correlation_matrix(X)
print(R)
