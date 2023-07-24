import numpy as np


"""1. 零詰めを行う関数"""


def zero_padding(L, S, x):
    y = np.pad(x, (L - S, L - S))  # 先頭と末尾にL-S個の零詰め．
    r = len(y) % S  # 信号yの長さをSで割った余り．
    y = np.pad(y, (0, S - r))  # 末尾にS-r個零詰めすることで最終的な信号の長さはSの倍数になる．
    return y


"""確認用"""
x = np.array([2, 3, 1, 5, 3, 6])
L = 8
S = 4

y = zero_padding(L, S, x)
print(y)


"""解説"""
print("\n解説")
L_ = 4
S_ = 3
x_ = np.ones(8)
x_pad = zero_padding(L_, S_, x_)
print(x_pad)
