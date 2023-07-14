import numpy as np


def culc_freq_response(a, b, f, fs):
    """周波数応答を計算
    Args:
        a(ndarray):定数
        b(ndarray):定数
        f(int):周波数
        fs(int):サンプリング周波数
    Return:
        H(ndarray):周波数応答
    """
    omega = 2 * np.pi * f / fs
    N = len(a)
    M = len(b)
    ka = np.arange(1, N)
    kb = np.arange(0, M)
    a = np.delete(a, 0)

    H = np.sum(b * np.exp(-1j * omega * kb)) / (
        1 + np.sum(a * np.exp(-1j * omega * ka))
    )

    return H


if __name__ == "__main__":
    x = np.zeros(10)
    x[0] = 1
    a = [0.2, 0.2, 0.2, 0.2, 0.2]
    b = [0.2, 0.2, 0.2, 0.2, 0.2]
    h = culc_freq_response(a, b, 1, 1)
    print(h)
