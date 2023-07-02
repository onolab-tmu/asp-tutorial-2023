import numpy as np
import matplotlib.pyplot as plt


"""x, yのインデクスを1始まりに合わせている．x[0]=y[0]=0"""


# 以下での関数で差分方程式を求める．
def diff_equation7(a, b, x):
    # x = np.pad(x, (1,0))   # 引数のxにおいて，x[0]がn=1の値に対応している場合は0を入れる．
    L = len(x) - 1
    N = len(a) - 1
    M = len(b) - 1
    y = np.zeros(L + 1)
    for n in range(1, L + 1):
        sum_a_y = 0  # a*yの箇所
        sum_b_x = 0  # b*xの箇所
        for k in range(1, N + 1):
            if n - k > 0:
                sum_a_y += a[k] * y[n - k]
        for k in range(M + 1):
            if n - k > 0:
                sum_b_x += b[k] * x[n - k]
        y[n] = (-sum_a_y + sum_b_x) / a[0]
        # print(sum_a_y, sum_b_x, y[n])   # 確認用
    return y


# 確認用
x = np.array([0, 1, 2, 3])  # x[0] = 0 としている．値を持つインデクスは1~L．
a = np.array([2, 3])
b = np.array([1, 3, 2, 4])

y = diff_equation7(a, b, x)  # y = [0, 0.5, 1.75, 2.875] になるはず
print(y)

L = len(x)
n = np.arange(1, L + 1)  # プロット横軸用

plt.figure()
plt.stem(n, y)
plt.title("Difference equation")
plt.xlabel("n")
plt.savefig("3_7.png")


# 確認用(解説)
x2 = np.zeros(11)
x2[0] = 0
x2[1] = 1
a2 = np.array([1.0, -0.3])
a2[0] = 1
b2 = np.array([0.4])
y2 = diff_equation7(a2, b2, x2)
print(y2)


L2 = len(x2)
n2 = np.arange(1, L2 + 1)  # プロット横軸用

# q06.py の結果を1ずらしたグラフになる．インデクスを1からにしているから．
plt.figure()
plt.stem(n2, y2)
plt.title("Difference equation")
plt.xlabel("n")
plt.savefig("3_7_confirm.png")
