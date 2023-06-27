import numpy as np


def circular_convolution(x, h):
    N = x.size  # 信号の長さ
    z = np.zeros(N, dtype=int)  # 畳み込み結果用の配列

    for n in range(N):
        for k in range(N):
            z[n] += x[k] * h[(n - k) % N]
    return z


# def circular_convolution(x, h):
#     X = np.fft.fft(x)
#     H = np.fft.fft(h)
#     z = np.fft.ifft(X * H).real  # 実部
#     return z


if __name__ == "__main__":
    x = np.array([3, 2, 1, 0], dtype=int)
    y = np.array([1, 0, 0, 1], dtype=int)

    print("circular_convolution(x,y):\t{}".format(circular_convolution(x, y)))

"""
[5 3 1 3]

"""
