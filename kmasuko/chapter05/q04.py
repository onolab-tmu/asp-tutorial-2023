import numpy as np


def spatial_corr(X: np.ndarray) -> np.ndarray:
    """空間相関行列を計算

    Arg:
        X (ndarray):複素スペクトル (M, freq, time)
    Return:
        ndarray:空間相関行列 (M, M)
    """

    M, f, T = X.shape
    R = np.sum(X[:, None, :, :] * X[None, :, :, :].conj(), axis=-1) / T
    R = R.transpose((2, 1, 0))
    """ R = []
    for i in range(f):
        s = np.zeros((M, M), dtype=complex)
        for t in range(T):
            s += X[:, i, t].reshape(M, 1) @ X[:, i, t].reshape(1, M).conj()
        R.append(s / T) """

    return R


if __name__ == "__main__":
    X = np.array(
        [
            [[1, -1.0j, -1, 1.0j], [2, -2.0j, -2, 2.0j], [3, -3.0j, -3, 3.0j]],
            [[4, -2.0j, 1, 0], [2, -2.0j, 0, 0], [1, -1.0j, 1, 0]],
        ]
    )

    R = spatial_corr(X)
    print()
    print(R.shape)
    print(R)
