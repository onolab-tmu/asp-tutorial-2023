import numpy as np
import matplotlib.pyplot as plt


def defference_equation_recursion(x):
    N = x.size
    y = np.zeros(N)

    for n in range(N):
        y[n] = recursion(x, n)

    return y


def recursion(x, n):
    if n == 0:
        return 0.4 * x[n]
    else:
        return 0.3 * recursion(x, n - 1) + 0.4 * x[n]


x = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(defference_equation_recursion(x))
plt.stem(defference_equation_recursion(x))
plt.show()
