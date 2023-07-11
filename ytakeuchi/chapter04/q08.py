import numpy as np
import matplotlib.pyplot as plt


def zero_pad(L, S, x):
    y = np.pad(x, (L - S, L - S))
    len_modS = len(y) % S
    if len_modS > 0:
        y = np.pad(y, (0, S - len_modS))
    return y


def frame_split(L, S, x):
    x_tilde = zero_pad(L, S, x)
    L_array = np.arange(L)
    y = x_tilde[L_array].reshape(1, L)
    t = 1
    while t * S + L <= len(x_tilde):
        y = np.append(y, x_tilde[t * S + L_array].reshape(1, L), axis=0)
        t += 1
    return y


def stft(L, S, w, x):
    frames = frame_split(L, S, x)
    y = np.zeros((len(frames), L // 2 + 1), dtype="complex")  # rfftにより(L/2)+1の配列が返される
    for i in range(len(frames)):
        y[i] = np.fft.rfft(frames[i] * w)
    return y.T


def synth_window(S, w):
    Q = len(w) // S
    ws = np.zeros(len(w))
    for l in range(len(w)):
        sum_w = 0
        for m in range(1 - Q, Q):
            if l - m * S >= 0 and l - m * S < len(w):
                sum_w += w[l - m * S] ** 2
        ws[l] = w[l] / sum_w
    return ws


def istft(S, X):
    F = len(X)
    T = len(X[0])
    N = 2 * (F - 1)
    M = S * (T - 1) + N
    x_hat = np.zeros(M, dtype="complex")
    z = np.zeros((T, 2 * (F - 1)), dtype="complex")
    for t in range(T):
        z[t] = np.fft.irfft(X.T[t])
    ws = synth_window(S, np.hamming(N))
    n = np.arange(N)
    for t in range(T):
        x_hat[t * S + n] = x_hat[t * S + n] + ws[n] * z[t][n]
    return x_hat


def istft_ws_is_1(S, X):
    F = len(X)
    T = len(X[0])
    N = 2 * (F - 1)
    M = S * (T - 1) + N
    x_hat = np.zeros(M, dtype="complex")
    z = np.zeros((T, 2 * (F - 1)), dtype="complex")
    for t in range(T):
        z[t] = np.fft.irfft(X.T[t])
    ws = np.ones(N)
    n = np.arange(N)
    for t in range(T):
        x_hat[t * S + n] = x_hat[t * S + n] + ws[n] * z[t][n]
    return x_hat


A = 1
f = 440
fs = 16000
l = 0.1

t = np.arange(0, l, 1 / fs)
x = A * np.sin(2 * np.pi * f * t)

L = 1000
S = 500
w = np.hamming(L)

X = stft(L, S, w, x)
x_hat = istft(S, X)
x_hat_is_1 = istft_ws_is_1(S, X)

plt.subplot(211)
plt.plot(x_hat)
plt.subplot(212)
plt.plot(x_hat_is_1)
plt.show()

##########確認コード##########

# 再構成誤差を計算
print(np.sum(np.square(x_hat[L - S : L - S + len(x)] - x)))
print(np.sum(np.square(x_hat_is_1[L - S : L - S + len(x)] - x)))

# 元の信号との差分をプロット
plt.subplot(211)
plt.plot(x_hat[L - S : L - S + len(x)] - x)
plt.subplot(212)
plt.plot(x_hat_is_1[L - S : L - S + len(x)] - x)
plt.show()
