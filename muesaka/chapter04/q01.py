import numpy as np


# 関数
def zero_padding(x, L, S):
    zero = np.zeros(L - S)
    x = np.block([zero, x, zero])  # 手順1

    is_multiple = x.shape[0] % S
    if is_multiple != 0:
        zero = np.zeros(S - is_multiple)
        x = np.block([x, zero])  # 手順2

    return x


if __name__ == "__main__":
    x = np.array([0, 1, 1, 1, 0])
    L = 4
    S = 2
    print(zero_padding(x, L, S))
