import numpy as np


def calc_dif_eq(a, b, x):
    y = np.zeros(len(x))
    N, M = len(a), len(b)
    for n in range(len(y)):
        for k in range(1, N):
            if n - k < 0:  # 負のインデックスは0として考えるため除外
                break
            y[n] -= a[k] * y[n - k]
        for k in range(M):
            if n - k < 0:
                break
            y[n] += b[k] * x[n - k]
    y = y / a[0]
    return y


# 再帰関数を用いる手法もある（q06参照）

##########確認コード##########

a = np.array([1, -0.3])  # 問6と同じ差分方程式
b = np.array([0.4])
x = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])

print(calc_dif_eq(a, b, x))  # 問6と同じ解となるはず
