import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])  # 10点の単位インパルス信号

N = len(x)
y = np.zeros(N)

# 以下で差分方程式を求める．
for n in range(N):
    y[n] = 0.3 * y[n - 1] + 0.4 * x[n]  # y[-1] = 0 より
    print(y)

n = np.arange(N)  # プロット横軸用

plt.figure()
plt.stem(n, y)
plt.title("Difference equation")
plt.xlabel("n")
plt.savefig("3_6.png")
