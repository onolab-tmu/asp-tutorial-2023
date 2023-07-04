import numpy as np


"""1. 零詰めを行う関数"""


def zero_padding(L, S, x):
    y = np.pad(x, (L - S, L - S))  # 先頭と末尾にL-S個の零詰め．
    r = len(y) % S  # 信号yの長さをSで割った余り．
    y = np.pad(y, (0, S - r))  # 末尾にS-r個零詰めすることで最終的な信号の長さはSの倍数になる．
    return y


"""2. フレームを出力する関数"""


def frame_t(L, S, x):
    y = zero_padding(L, S, x)  # 零詰めしたx．

    # 以下Tを求める．「零詰め後の長さからLを引いた数」とSの商はシフトできる回数を表している．Tの定義より1を加えて調整している．
    T = (len(y) - L) // S + 1
    x_t = np.zeros((T, L))
    l = np.arange(L)
    for t in range(T):
        x_t[t] = y[t * S + l]
    return x_t


"""確認用"""
print("確認用")
x = np.array([2, 3, 1, 5, 3, 6])
L = 8
S = 4

y = zero_padding(L, S, x)  # q01と同じ．
print(y)

x_t = frame_t(L, S, x)
print(x_t)


"""解説"""
print("\n解説")
L_ = 4
S_ = 3
x_ = np.ones(8)
x_pad = zero_padding(L_, S_, x_)
x_t_ = frame_t(L_, S_, x_)

print("x_pad : ", x_pad)
print("x_t : ", x_t_)
