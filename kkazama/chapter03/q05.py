import numpy as np
import matplotlib.pyplot as plt


# 差分方程式
def difference_equation(x):
    N = len(x)
    y = np.zeros(N)

    for n in range(N):
        for k in range(5):
            if n - k >= 0 and n - k < N:
                y[n] += 0.2 * x[n - k]

    return y


# 確認
x = np.zeros(10)
x[0] = 1

plt.stem(x)
plt.stem(difference_equation(x))
plt.show()
