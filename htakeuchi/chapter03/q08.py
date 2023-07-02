import numpy as np


def frequency_responce(a, b, f, fs):
    # a = np.pad(a, (1,0))   # 引数のaにおいて，a[0]がn=1の値に対応している場合は0を入れる．
    N = len(a) - 1
    M = len(b) - 1
    omega = 2 * np.pi * f / fs
    sum_b_e = 0
    sum_a_e = 1
    for k in range(M + 1):
        sum_b_e += b[k] * np.e ** (-1j * omega * k)
    for k in range(1, N + 1):
        sum_a_e += a[k] * np.e ** (-1j * omega * k)
    H = sum_b_e / sum_a_e
    return H


# 確認用
a = np.array([0])
b = np.array([1, 1, 1, 1, 1, 1, 1, 1])
f = 1
fs = 8

H = frequency_responce(a, b, f, fs)  # 0になるはず
print(np.round(H, 5))
