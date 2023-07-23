import numpy as np
import q01


def split_frame(x, L, S):
    x = q01.zero_padding(x, L, S)  # 0埋め
    N = x.shape[0]
    T = (N - L) // S + 1  # Tのサイズ
    x_split = np.zeros((T, L))

    for t in range(T):
        x_split[t] = x[t * S : t * S + L]  # t番目のフレームを求める

    return x_split


if __name__ == "__main__":
    x = np.array([0, 1, 1, 1, 0])
    L = 4
    S = 2
    print(split_frame(x, L, S))
