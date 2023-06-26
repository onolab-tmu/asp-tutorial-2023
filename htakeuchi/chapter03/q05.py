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


# 5
def linear_conv2(x, h):  # xとhの配列長が異なる場合の線形畳み込み
    N = len(x)
    M = len(h)
    z = np.zeros(N + M - 1)
    for n in range(N + M - 1):
        for k in range(N):
            if not (n - k < 0 or n - k > N - 1):
                z[n] += x[k] * h[n - k]
    return z


x = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])  # 単位インパルス信号(10点)
b = np.array([0.2, 0.2, 0.2, 0.2, 0.2])

y = linear_conv2(b, x)
print("y = ", y)

n = np.arange(len(y))

plt.figure()
plt.stem(n, y)
plt.title("Difference equation")
plt.xlabel("n")
plt.savefig("3_5.png")


# 信号xのプロット
n = np.arange(len(x))
plt.figure()
plt.stem(n, x)
plt.title("x")
plt.xlabel("n")
plt.savefig("3_5_x.png")
