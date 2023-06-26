import numpy as np


def my_dft(x):
    """信号のDFTを計算する
    Args:
        x(ndarray):入力信号
    Return:
        X(ndarray):信号のDFT
    """
    N = len(x)
    n = np.arange(0, N)
    X = np.empty(N, dtype=np.complex128)
    for k in range(0, N):
        X[k] = np.sum(x * np.exp(-2j * np.pi * k * n / N))

    return X


def my_idft(X):
    """信号のIDFTを計算する
    Args:
        X(ndarray):入力信号
    Return:
        x(ndarray):信号のIDFT
    """
    N = len(X)
    k = np.arange(0, N)
    x = np.empty(N, dtype=np.float64)
    for n in range(0, N):
        x[n] = 1 / N * np.sum(X * np.exp(2j * np.pi * k * n / N))

    return x
