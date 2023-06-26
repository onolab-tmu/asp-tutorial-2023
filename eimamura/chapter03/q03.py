import numpy as np


def clc(x, h):
    N = x.size
    x_pad = np.pad(x, (0, N - 1))
    h_pad = np.pad(h, (0, N - 1))
    N = x_pad.size
    z = np.zeros(N)
    for n in range(N):
        for k in range(N):
            z[n] += x_pad[k] * h_pad[(n - k) % N]
    return z


if __name__ == "__main__":
    x = np.array([3, 2, 1, 0])
    y = np.array([1, 0, 0, 1])
    print(clc(x, y))
