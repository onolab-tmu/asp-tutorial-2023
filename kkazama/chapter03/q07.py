import numpy as np
import matplotlib.pyplot as plt


# 再帰関数
def recursive_func(x, a, b, n):
    if n == 0:
        return b[n] / a[n] * x[n]
    else:
        y = - a[n] * recursive_func(x, a, b, n - 1) + b[n] * x[n] 
        return y / a[0]


# 差分方程式（一般系）
def difference_equation_recursive(x, a, b):
    N = len(x)
    y = np.zeros(N)

    for n in range(N):
        y[n] = recursive_func(x, a, b, n)

    return y


# 確認
x = np.zeros(10)
x[0] = 1

a = np.zeros(10) - 3
a[0] = 10
b = np.zeros(10) + 4


y = difference_equation_recursive(x, a, b)
np.set_printoptions(suppress=True)
print(y)
# [0.4   0.12   0.036   0.0108    0.00324   0.000972   0.0002916  0.00008748 0.00002624 0.00000787]

plt.stem(y)
plt.show()
