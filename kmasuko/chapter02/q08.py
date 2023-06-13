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

    plt.figure()
    plt.plot(t, x_ham)
    plt.xlabel("Time [s]")
    plt.ylabel("Amp")
    plt.show()
