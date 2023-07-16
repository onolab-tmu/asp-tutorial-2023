import numpy as np


def dft(x):
    N = x.size
    n = np.arange(N)  # ファンシーインデックス
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        X[k] = np.sum(x[n] * np.exp(-1j * 2 * np.pi * k * n / N))  # ファンシーインデックスを用いてsum計算
    return X


def idft(X):
    N = X.size
    k = np.arange(N)  # ファンシーインデックス
    x = np.zeros(N, dtype=complex)
    for n in range(N):
        x[n] = 1 / N * np.sum(X[k] * np.exp(1j * 2 * np.pi * k * n / N))  # ファンシーインデックスを用いてsum計算
    return x


if __name__ == "__main__":
    x = np.array([1, 2, 3, 4], dtype=float)
    calc_X = dft(x)  # dtf計算 complex型
    calc_x = np.abs(idft(calc_X))  # idft計算 realだけ抽出

    print("x:\t{}".format(x))  # 確認
    print("calc_X:\t{}".format(calc_X))  # 確認
    print("calc_x:\t{}".format(calc_x))  # 確認 xと同じになればよい
