import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt


def linear_conv(x, h):
    N = len(x)
    z = np.zeros(2 * N - 1)
    for n in range(z.size):
        for k in range(N):
            if n - k >= 0 and n - k <= N - 1:
                z[n] += x[k] * h[n - k]
    return z


def circular_conv(x, h):
    N = len(x)
    z = np.zeros(N, dtype=complex)

    for n in range(N):
        for k in range(N):
            z[n] += x[k] * h[(n - k) % N]

    return z


# 巡回畳み込み（ゼロ詰め）
def zero_padd_conv(x, h):
    N = len(x)
    x = np.pad(x, (0, N - 1))
    h = np.pad(h, (0, N - 1))

    z = circular_conv(x, h)
    return z


x = np.array([4, 3, 2, 1])
y = np.array([1, 0, -1, 0])

z_liner = linear_conv(x, y)
print(len(z_liner))
z_circlular = circular_conv(x, y)
print(len(z_circlular))
z_padd = zero_padd_conv(x, y)

# 確認
plt.subplot(3, 1, 1)
plt.stem(z_liner)
plt.subplot(3, 1, 2)
plt.stem(z_circlular)
plt.subplot(3, 1, 3)
plt.stem(z_padd)
plt.show()
