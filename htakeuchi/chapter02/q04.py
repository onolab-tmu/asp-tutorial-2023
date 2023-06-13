import numpy as np
import matplotlib.pyplot as plt

# 1
def DFT(x):
    N = len(x)
    n = np.arange(N)
    X = np.zeros(N, dtype=np.complex128)
    for k in range(N):
        X[k] = np.sum( x * np.e ** (-1j * 2 * np.pi * k * n / N))
    return np.round(X,5)

def IDFT(X):
    N = len(X)
    k = np.arange(N)
    x = np.zeros(N, dtype=np.complex128)
    for n in range(N):
        x[n] = np.sum(X * np.e ** (1j * 2 * np.pi * k * n / N))
    x /= N
    return np.round(x,5)


# 2
delta = [1,0,0,0,0,0,0,0]
delta_DFT = DFT(delta)
k = np.arange(len(delta_DFT))


# 4
delta_DFT_amp = np.abs(delta_DFT)
delta_DFT_pha = np.angle(delta_DFT)

print(delta_DFT_amp)
print(delta_DFT_pha)

plt.figure()
plt.subplots_adjust(wspace=0.5)
plt.subplot(1,2,1)
plt.stem(k,delta_DFT_amp)
plt.title("Amplitude Spectrum")
plt.xlabel("k [-]")
plt.ylabel("Amplitude [-]")
plt.subplot(1,2,2)
plt.stem(k,delta_DFT_pha)
plt.title("Phase Spectrum")
plt.xlabel("k [-]")
plt.ylabel("Phase [rad]")
plt.savefig("2_4.png")
