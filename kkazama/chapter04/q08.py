import numpy as np
import matplotlib.pyplot as plt
from q04 import stft
from q07 import istft
from q01 import zero_pad


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


def istft_w(X, S):
    F = X.shape[0]
    T = X.shape[1]

    N = 2 * (F - 1)
    M = S * (T - 1) + N

    x = np.zeros(M)
    z = np.zeros((T, N))
    w = np.zeros(N) + 1.0

    for t in range(T):
        for n in range(N):
            z[t][n] = np.fft.irfft(X[:, t])[n]
            x[t * S + n] = x[t * S + n] + w[n] * z[t][n]

    return x


# 確認
A = 1
f = 440
fs = 16000
sec = 0.1

t = np.arange(fs * sec) / fs
x = A * np.sin(2 * np.pi * f * t)

L = 1000
S = 500
w = np.hamming(L)

X = stft(x, L, S, w)

x_istft = istft(X, S)
x_istft_w = istft_w(X, S)

x_pad = zero_pad(x, L, S)

# 再構成誤差
diff = np.sum(x_pad - x_istft) ** 2
diff_w = np.sum(x_pad - x_istft_w) ** 2

print(diff)
print(diff_w)

plt.subplot(2, 1, 1)
plt.plot(x_istft)
plt.xlim([500, 1000])
plt.subplot(2, 1, 2)
plt.plot(x_istft_w)
plt.xlim([500, 1000])
plt.show()
