import numpy as np
import matplotlib.pyplot as plt

<<<<<<< HEAD

=======
>>>>>>> c3997293507c80cc63d552b80ed4562aec50b09f
def Hamming(w):
    N = len(w)
    w_hamming = np.zeros(N, dtype=complex)
    for n in range(N):
<<<<<<< HEAD
        w_hamming[n] = w[n] * (0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1)))
    return w_hamming


=======
        w_hamming[n] = w[n] * (0.54 - 0.46 * np.cos(2 * np.pi * n / (N-1)))   
    return w_hamming

>>>>>>> c3997293507c80cc63d552b80ed4562aec50b09f
a = 1
f = 440
fs = 16000
s = 3.0

<<<<<<< HEAD
t = np.arange(0, s, 1 / fs)
y = a * np.sin(2 * np.pi * f * t)

Y = np.fft.fft(y)

N = int(s * fs)
num = np.arange(0, N, 1)
hamming2 = 0.54 - 0.46 * np.cos(2 * np.pi * num / (N - 1))
hamming_DFT = np.fft.fft(hamming2)

a1 = np.convolve(Y, hamming_DFT, mode="same")
b1 = np.fft.ifft(a1)

conv = np.zeros(N, dtype=complex)

k = np.arange(0, N, 1)
for num in range(0, N):
    conv[k] += Y[num] * hamming_DFT[k - num]

conv_ifft = np.fft.ifft(conv)


print(conv_ifft)
plt.plot(b1)
plt.plot(conv_ifft)
plt.xlabel("time")
plt.ylabel("signal")
plt.show()
=======
t = np.arange(0, s, 1/fs)
y = a * np.sin(2*np.pi*f*t)

Y = np.fft.fft(y)

N = int(s*fs)
num = np.arange(0, N, 1)
hamming2 = 0.54 - 0.46 * np.cos(2 * np.pi * num / (N-1))
hamming_DFT = np.fft.fft(hamming2)

a = np.convolve(Y, hamming_DFT, mode="same") 
b = np.fft.ifft(a)

plt.plot(b)
plt.show()


def Hamming(w):
    N = len(w)
    w_hamming = np.zeros(N, dtype=complex)
    for n in range(N):
        w_hamming[n] = w[n] * (0.54 - 0.46 * np.cos(2 * np.pi * n / (N-1)))   
    return w_hamming

a = 1
f = 440
fs = 16000
s = 3

t = np.arange(0, s, 1/fs)
y = a * np.sin(2*np.pi*f*t)

hamming = Hamming(y)
print(hamming)
plt.plot(hamming)
plt.plot(b)
plt.show()
>>>>>>> c3997293507c80cc63d552b80ed4562aec50b09f
