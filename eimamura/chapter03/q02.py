import numpy as np


def cc(x, h):
    N = x.size
    z = np.zeros(N)
    for n in range(N):
        for k in range(N):
            z[n] += x[k] * h[(n - k) % N]
    return z


if __name__ == "__main__":
    x = np.array([3, 2, 1, 0])
    y = np.array([1, 0, 0, 1])
    print(cc(x, y))
