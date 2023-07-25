import numpy as np


# 空間相関行列を計算
def calculate_spatial_correlation(X):
    M, F, T = X.shape  # 複素数行列Xは要素数MでF*Tのサイズ
    R = np.zeros((F, M, M), dtype="complex")  # 空間相関行列Rは要素数FでM*Mのサイズ

    # R[f]ごとに計算
    for f in range(F):
        # 総和処理
        for t in range(T):
            x_ft = X[:, f, t]
            R[f] += np.outer(x_ft, np.conjugate(x_ft))
        R[f] /= T  # 平均処理

    return R


if __name__ == "__main__":
    X1 = np.array([[1, -1j, -1, 1j], [2, -2j, -2, 2j], [3, -3j, -3, 3j]])  # 行列1
    X2 = np.array([[4, -2j, 1, 0], [2, -1j, 0, 0], [1, -1j, 1, 0]])  # 行列2
    X = np.array([X1, X2])

    print(calculate_spatial_correlation(X))
