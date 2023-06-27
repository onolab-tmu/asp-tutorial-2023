import numpy as np


def linear_conv(x, h):
    N = x.size  # xの長さ
    z = np.zeros(2 * N - 1, dtype=int)  # 畳み込み結果用の配列
    for n in range(2 * N - 1):  # n = {0 ... 2N-2}
        for k in range(N):  # k = {0 ... N-1}
            if (n - k < 0) or (n - k > N - 1):
                z[n] += 0
            else:
                z[n] += x[k] * h[n - k]
    return z


#####確認コード#####
if __name__ == "__main__":
    x = np.array([3, 2, 1, 0], dtype=int)
    y = np.array([1, 0, 0, 1], dtype=int)

    print(linear_conv(x, y))
# 3213210になる
