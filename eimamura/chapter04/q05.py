import numpy as np
import matplotlib.pyplot as plt


def composite(S, w):
    L = len(w)
    Q = int(L / S)
    ws = np.zeros(L)
    a = 0
    print("Q", Q)
    for l in range(L):
        for m in range(-(Q - 1), Q):
            if (l - m * S) >= 0 and L > (l - m * S):
                a += w[l - m * S] ** 2
        ws[l] = w[l] / a
        a = 0

    return ws


L = 100
S = 50
w = np.hamming(L)
y = composite(S, w)

plt.plot(y)
plt.title("Q=2")
plt.show()
