import numpy as np


def lc(x, h):
    N = x.size
    z = np.zeros(2 * N - 1)
    for n in range(2 * N - 1):
        for k in range(N):
            if (n - k < 0) or (n - k > N - 1):
                z[n] += 0
            else:
                z[n] += x[k] * h[n - k]

    return z


if __name__ == "__main__":
    x = np.array([3, 2, 1, 0])
    y = np.array([1, 0, 0, 1])
    print(lc(x, y))
