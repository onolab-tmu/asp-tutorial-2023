import numpy as np
import matplotlib.pyplot as plt


# 8
def frequency_responce(a, b, f, fs):
    # a = np.pad(a, (1,0))   # 引数のaにおいて，a[0]がn=1の値に対応している場合は0を入れる．
    N = len(a) - 1
    M = len(b) - 1
    omega = 2 * np.pi * f / fs
    sum_b_e = 0
    sum_a_e = 1
    for k in range(M + 1):
        sum_b_e += b[k] * np.e ** (-1j * omega * k)
    for k in range(1, N + 1):
        sum_a_e += a[k] * np.e ** (-1j * omega * k)
    H = sum_b_e / sum_a_e
    return H


# 9
a = np.array([0])  # 再起なし
b = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
fs = 16000
N = 100

n = np.arange(N)
f = np.array(n * fs / N)  # fの配列

H = np.full(N, 0 + 0j, dtype=complex)  # 配列fと同じ大きさの配列
for i in range(N):
    H[i] = frequency_responce(a, b, f[i], fs)

# print(H)
amp_H = np.abs(H)
pha_H = np.angle(H)


plt.figure()
plt.stem(f, amp_H)
plt.title("Difference equation")
plt.xlabel("frequency [Hz]")
plt.ylabel("Amplitude [-]")
plt.savefig("3_9_amp.png")

plt.figure()
plt.stem(f, pha_H)
plt.title("Difference equation")
plt.xlabel("frequency [Hz]")
plt.ylabel("Phase [-]")
plt.savefig("3_9_pha.png")
