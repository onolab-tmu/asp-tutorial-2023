import numpy as np
import matplotlib.pyplot as plt


def de(x):
    N = x.size
    y = np.zeros(N)

    for n in range(N):
        if n == 0:
            y[n] = 0.2 * x[n]
        elif n == 1:
            y[n] = 0.2 * x[n] + 0.2 * x[n - 1]
        elif n == 2:
            y[n] = 0.2 * x[n] + 0.2 * x[n - 1] + 0.2 * x[n - 2]
        elif n == 3:
            y[n] = 0.2 * x[n] + 0.2 * x[n - 1] + 0.2 * x[n - 2] + 0.2 * x[n - 3]
        else:
            y[n] = 0.2 * x[n] + 0.2 * x[n - 1] + 0.2 * x[n - 2] + 0.2 * x[n - 3] + 0.2 * x[n - 4]
    return y


x = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(de(x))
plt.stem(de(x))
plt.ylim(0, 1)
plt.show()
