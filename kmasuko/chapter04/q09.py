import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.signal import chirp
from q03 import stft


if __name__ == "__main__":
    sec = 1
    fs = 16000
    f_start = 100
    f_finish = 16000
    t = np.arange(fs * sec) / fs
    x = chirp(t, f0=f_start, f1=f_finish, t1=sec, method="linear")

    sd.play(x, fs)
    sd.wait()
    L = [100, 200, 400, 800]
    S = [50, 100, 200, 400]
    for i in range(len(L)):
        hamm = np.hamming(L[i])
        X = stft(L[i], S[i], hamm, x)
        tt = np.linspace(0, sec, X.shape[1])
        ff = np.linspace(0, fs / 2, X.shape[0])

        plt.subplot(4, 2, (2 * i) + 1)
        plt.pcolormesh(tt, ff, np.abs(X))

        plt.subplot(4, 2, 2 * (i + 1))
        plt.pcolormesh(tt, ff, np.angle(X))

    plt.show()
