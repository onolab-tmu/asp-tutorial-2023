from q07 import hamm
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    fs = 16000
    amp = 1
    f = 440
    sec = 3
    t = np.arange(sec * fs) / fs
    x = amp * np.sin(2 * np.pi * f * t)

    hamming = hamm(sec * fs)
    x_ham = x * hamming

    x_dft = np.fft.fft(x)
    hamm_dft = np.fft.fft(hamming)
    conv_x_ham = np.convolve(x_dft, hamm_dft, mode="same")
    conv_idft = np.fft.ifft(conv_x_ham)

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.title("x_hamm")
    plt.plot(t, x_ham)
    plt.xlabel("Time [s]")
    plt.ylabel("Amp")

    plt.subplot(1, 2, 2)
    plt.title("conv_idft")
    plt.plot(t, conv_idft / (sec * fs / 2))
    plt.xlabel("Time [s]")
    plt.ylabel("Amp")
    plt.show()
