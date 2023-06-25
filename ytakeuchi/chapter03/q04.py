import numpy as np
import matplotlib.pyplot as plt


def conv_linear(x, h):
    N = len(x)
    z = np.zeros(2 * N - 1)
    for n in range(2 * N - 1):
        for k in range(N):
            if n - k >= 0 and n - k <= N - 1:
                z[n] += x[k] * h[n - k]
    return z


def conv_circular(x, h):
    N = len(x)
    z = np.zeros(N)
    for n in range(N):
        for k in range(N):
            z[n] += x[k] * h[(n - k) % N]
    return z


def conv_circular_zero(x, y):
    N = len(x)
    z = np.zeros(2 * N - 1)
    return conv_circular(np.pad(x, (0, N - 1)), np.pad(y, (0, N - 1)))


x = np.array([4, 3, 2, 1])
y = np.array([1, 0, -1, 0])

print(f"linear convolve: {conv_linear(x,y)}")
plt.stem(conv_linear(x, y))
plt.show()

print(f"circular convolve: {conv_circular(x,y)}")
plt.stem(conv_circular(x, y))
plt.show()

print(f"circular convolve with zero padding: {conv_circular_zero(x,y)}")
plt.stem(conv_circular_zero(x, y))
plt.show()

##########確認コード##########

plt.subplots_adjust(hspace=0.6)

for i in range(4):  # 線形畳み込み及び零埋めを行った巡回畳み込みの場合
    plt.stem(np.pad(x * y[i], (i, 0)), markerfmt="C" + str(i))  # 横軸の値が等しい点を足すと畳み込み後の値になるはず
plt.show()

for i in range(4):  # 巡回畳み込みの場合
    plt.stem(np.roll(x * y[i], i), markerfmt="C" + str(i))  # roll関数により巡回シフト
plt.show()
