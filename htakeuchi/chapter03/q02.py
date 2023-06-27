import numpy as np
import matplotlib.pyplot as plt


def circular_conv(x, h):  # 巡回畳み込み
    N = len(x)
    z = np.zeros(N)
    idx = np.arange(N)
    for n in range(N):
        h_idx = np.mod(n - idx, N)  # 各nに対するインデクスを作成
        # h_idx = (n-idx) % N   # これでもよい
        # print(h_idx)   # 確認用
        # print(h[h_idx])
        z[n] = np.sum(x * h[h_idx])
    return z


# 解説
def circular_conv_fft(x, h):
    X = np.fft.fft(x)
    H = np.fft.fft(h)
    z = np.fft.ifft(X * H).real
    return z


# 確認用
x = np.array([0, 1, 2, 3, 4])
h = np.array([1, 3, 5, 7, 9])

print(circular_conv(x, h))  # [2,2,-2,-2]になるはず
print(circular_conv_fft(x, h))
