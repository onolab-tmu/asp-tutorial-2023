from q01 import dft
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    fs = 16000
    amp = 1
    sec = 3
    f = 440
    t = np.arange(sec * fs) / fs
    x = amp * np.cos(2 * np.pi * f * t)
    w = np.fft.fftfreq(len(x), 1 / fs)
    x_dft = np.fft.fft(x)

    plt.figure()
    plt.plot(t, x)
    plt.xlim(0, 1 / f)
    plt.xlabel("Time [s]")
    plt.ylabel("Amp")
    plt.show()

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.plot(w, np.abs(x_dft) / (fs / 2))
    plt.xlim(0, fs / 2)
    plt.xlabel("Freq [Hz]")
    plt.ylabel("|X[k]|")

    plt.subplot(1, 2, 2)
    plt.stem(w, np.angle(x_dft))
    plt.xlim(f-3, f+3)
    plt.xlabel("Freq [Hz]")
    plt.ylabel("∠X[k]")
    plt.show()
