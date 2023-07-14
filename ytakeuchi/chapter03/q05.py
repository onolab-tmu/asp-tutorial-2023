import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
y = np.zeros(10)

y[0] = 0.2 * x[0]
y[1] = 0.2 * x[1] + 0.2 * x[0]
y[2] = 0.2 * x[2] + 0.2 * x[1] + 0.2 * x[0]
y[3] = 0.2 * x[3] + 0.2 * x[2] + 0.2 * x[1] + 0.2 * x[0]  # y[3]まではインデックスが負になるためfor文の外で計算
for n in range(4, len(y)):
    y[n] = 0.2 * x[n] + 0.2 * x[n - 1] + 0.2 * x[n - 2] + 0.2 * x[n - 3] + 0.2 * x[n - 4]
# for n in range(len(x)):
#     for i in range(5):
#         if n-i>=0:
#             y[n]+=x[n-i]/5 #今回の差分方程式の特性を利用．5という数値は項数

plt.stem(y)
plt.show()

##########確認コード##########

# 手計算により確認可能．0<=n<=4のときは0.2，それ以外は0
