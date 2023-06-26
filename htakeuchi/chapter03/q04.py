import numpy as np

import matplotlib.pyplot as plt


# 1
def linear_conv(x, h):
    N = len(x)
    z = np.zeros(2 * N - 1)
    for n in range(2 * N - 1):
        for k in range(N):
            if not (n - k < 0 or n - k > N - 1):
                z[n] += x[k] * h[n - k]
    return z


# 2
def circular_conv(x, h):
    N = len(x)
    z = np.zeros(N)
    idx = np.arange(N)
    for n in range(N):
        h_idx = np.mod(n - idx, N)
        z[n] = np.sum(x * h[h_idx])
    return z


# 3
def zero_pad_circular_conv(x, y):
    N = len(x)
    x = np.pad(x, (0, N - 1))
    y = np.pad(y, (0, N - 1))
    z = circular_conv(x, y)
    return z


# 4
x = np.array([4, 3, 2, 1])
y = np.array([1, 0, -1, 0])

linear = linear_conv(x, y)
circular = circular_conv(x, y)
zero_pad_circular = zero_pad_circular_conv(x, y)

print("Linear conv\n", linear, "\n")
print("Circular conv\n", circular, "\n")
print("Zero padding circular conv\n", zero_pad_circular, "\n")


n = np.arange(len(linear))
plt.figure()
plt.stem(n, linear)
plt.title("Linear conv")
plt.xlabel("n")
plt.savefig("3_4_linear.png")

n = np.arange(len(circular))
plt.figure()
plt.stem(n, circular)
plt.title("Circular conv")
plt.xlabel("n")
plt.savefig("3_4_circular.png")

n = np.arange(len(zero_pad_circular))
plt.figure()
plt.stem(n, zero_pad_circular)
plt.title("Zero padding circular conv")
plt.xlabel("n")
plt.savefig("3_4_zero_pad.png")
