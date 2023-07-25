import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import wave

from utils import gene_noise


if __name__ == "__main__":
    fs = 16000
    sec = 1
    amp = 1
    f = 440
    t = np.arange(fs * sec) / fs
    signal = np.sin(2 * np.pi * t * f)

    sn = 10
    noise = gene_noise(signal, sn)

    shifts = [0, 10, 20]
    x = []
    for i in shifts:
        x.append(np.pad(signal, (i,))[: fs * sec] + noise)
    x = np.array(x)

    n_channel = x.shape[0]
    plt.figure(figsize=(12, 8))
    plt.subplots_adjust(hspace=0.6)
    for i in range(n_channel):
        plt.subplot(n_channel, 1, (i + 1))
        plt.plot(t, x[i])
        plt.title(f"s[n - {shifts[i]}] + ε[n]")
        plt.xlabel("Time [s]")
        plt.xlim(0, 0.01)
    plt.show()

    sf.write("signal.wav", x.T, fs)
