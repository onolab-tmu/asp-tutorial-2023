import numpy as np


def circular_conv(x, h):
    N = x.size  # 信号の長さ
    z = np.zeros(N, dtype=int)  # 畳み込み結果用の配列

    for n in range(N):
        for k in range(N):
            z[n] += x[k] * h[(n - k) % N]
    return z


#####確認コード#####
if __name__ == "__main__":
    x = np.array([3, 2, 1, 0], dtype=int)
    y = np.array([1, 0, 0, 1], dtype=int)

    print(circular_conv(x, y))
# 5313と表示されるはず
