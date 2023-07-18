import numpy as np
import matplotlib.pyplot as plt


# 合成窓
def window_synth(w, L, S):
    Q = L // S
    w_synth = np.zeros(L)

    for l in range(L):
        w_shift_sum = 0
        for m in range(-(Q - 1), Q):
            if (l - m * S) >= 0 and (l - m * S) < L:
                w_shift_sum += w[l - m * S]**2

        w_synth[l] = w[l] / w_shift_sum

    return w_synth


# 確認
L = 1000
S = 250
w = np.hamming(L)

w_synth = window_synth(w, L, S)

a = np.sum(w * w_synth)
print(a)

plt.subplot(2, 1, 1)
plt.plot(w)
plt.subplot(2, 1, 2)
plt.plot(w_synth)
plt.show()
