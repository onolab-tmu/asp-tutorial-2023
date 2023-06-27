import numpy as np
import matplotlib.pyplot as plt

# 7
def Hamming(N):
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N-1))
    return np.round(w, 5)


#10
# def circular_conv(X, Y):
#     N = len(X)
#     Z = np.zeros(N, dtype=np.complex128)
#     Y_ = np.zeros(N, dtype=np.complex128)
#     for k in range(N):
#         for i in range(N):
#             Y_[i] = Y[k-i]
#         Z[k] = np.sum(X * Y_)
#     return Z

def circular_conv(X, Y):
    N = len(X)
    Z = np.zeros(N, dtype=np.complex128)
    Y_ = np.zeros(N, dtype=np.complex128)
    for k in range(N):
        Y_ = np.roll(Y[::-1], k+1)
        Z[k] = np.sum(X * Y_)
    return Z


#確認用
A = [1,0,2]
B = [2,1,1]

# C = [4,3,5] になるはず
C = circular_conv(A, B)
print("確認用")
print("C = ", C)


# 10
A = 1
f = 440
fs = 16000
sec = 3

t = np.array([i / fs for i in range(sec * fs)])
x = A * np.sin(2 * np.pi * f * t)

N = len(x)
w = Hamming(N)

X = np.fft.fft(x)
Y = np.fft.fft(w)

Z = circular_conv(X, Y)
Z_IDFT = np.fft.ifft(Z)

# Z_IDFT /= N

n = np.arange(N)

plt.figure()
plt.stem(n, Z_IDFT.real)
plt.xlabel("n [-]")
plt.ylabel("Amplitude [-]")
plt.savefig("2_10.png")
