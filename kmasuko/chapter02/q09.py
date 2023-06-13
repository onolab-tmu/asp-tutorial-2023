from q07 import hamm
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    fs = 16000
    sec = 3

    hamming = hamm(sec * fs)
    hamm_dft = np.fft.fft(hamming)
    w = np.fft.fftfreq(len(hamming), 1 / fs)

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.plot(w, np.abs(hamm_dft) / (fs / 2))
    plt.xlim(0, fs / 2)
    plt.xlabel("Freq [Hz]")
    plt.ylabel("|X[k]|")

    plt.subplot(1, 2, 2)
    plt.scatter(w, np.angle(hamm_dft))
    plt.xlim(0, fs / 2)
    plt.xlabel("Freq [Hz]")
    plt.ylabel("∠X[k]")
    plt.show()
