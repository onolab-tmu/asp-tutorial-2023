import numpy as np
import matplotlib.pyplot as plt


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


def cc(x, h):
    N = x.size
    z = np.zeros(N)
    for n in range(N):
        for k in range(N):
            z[n] += x[k] * h[(n - k) % N]
    return z


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


x = np.array([4, 3, 2, 1])
y = np.array([1, 0, -1, 0])
print(lc(x, y))
print(cc(x, y))
print(clc(x, y))

plt.stem(lc(x, y))
plt.show()
plt.stem(cc(x, y))
plt.show()
plt.stem(clc(x, y))
plt.show()
