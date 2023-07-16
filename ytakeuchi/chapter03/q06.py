import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
y = np.zeros(10)

y[0] = 0.4 * x[0]  # y[0]はインデックスが負になるためfor文の外で計算
for n in range(1, len(y)):
    y[n] = 0.3 * y[n - 1] + 0.4 * x[n]

"""再帰関数を実装する手法もあり
def recursive_func(x, n): #y[n]を求める関数
    if n==0:
        return 0.4 * x[n]
    else:
        return 0.3 * recursive_func(x, n-1) + 0.4 * x[n] #自分自身の呼び出し（再帰）
"""

plt.stem(y)
plt.show()

##########確認コード##########

# 手計算により確認可能．初項0.4，公比0.3の等比数列となる
print(y)
