import numpy as np
import q01
import q02


def circular_linear_conv(x, h):
    N = x.size  # 信号の長さ

    x_pad = np.pad(x, (0, N - 1))  # 0埋め
    h_pad = np.pad(h, (0, N - 1))  # 0埋め
    return q02.circular_conv(x_pad, h_pad)  # q02の関数を利用


#####確認コード#####
if __name__ == "__main__":
    x = np.array([3, 2, 1, 0], dtype=int)
    y = np.array([1, 0, 0, 1], dtype=int)
    print(np.pad(x, (0, x.size)))
    print(q01.linear_conv(x, y))  # q01の関数を利用
    print(circular_linear_conv(x, y))

# どちらも3213210になるはず
