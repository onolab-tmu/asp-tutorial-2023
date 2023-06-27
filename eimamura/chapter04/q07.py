import numpy as np
import matplotlib.pyplot as plt


def general_defference_equation_recursion(a, b, x):
    N = x.size
    y = np.zeros(N)

    for n in range(N):
        y[n] = general_recursion(n, a, b, x)

    return y


def general_recursion(l, a, b, x):
    N = a.size
    M = b.size
    for n in range(1, N):
        for m in range(M):
            if l == 0:
                return b[m] * x[l]
            else:
                return -a[n] * general_recursion(l - 1, a, b, x) + b[m] * x[l]


x = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
a = np.array([1, -0.3, 0, 0, 0, 0, 0, 0, 0, 0])
b = np.array([0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(general_defference_equation_recursion(a, b, x))
plt.stem(general_defference_equation_recursion(a, b, x))
plt.show()
