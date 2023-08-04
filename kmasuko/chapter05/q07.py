import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import stft, istft
import soundfile as sf

if __name__ == "__main__":
    np.set_printoptions(linewidth=100)
    file = "signal.wav"
    x, fs = sf.read(file)
    t1 = np.arange(fs) / fs

    stft_args = {
        "fs": fs,
        "window": "hann",
        "nperseg": 1024,
        "noverlap": 512,
    }
    f, _, x_stft = stft(x.T, **stft_args)  # (n_channel, n_freq, n_frame)

    tau = np.array([0, 10 / fs, 20 / fs])
    wf = 1 / 3 * np.exp(-1.0j * 2 * np.pi * f[:, None] * tau[None, :])  # (n_freq, n_channel)

    y = wf.conj().T[:, :, None] * x_stft  # (n_channel, n_freq, n_frame)
    y = np.sum(y, axis=0)  # (n_freq, n_frame)
    t, en_signal = istft(y, **stft_args, time_axis=1, freq_axis=0)

    n_channel = x.T.shape[0]
    plt.figure(figsize=(12, 8))
    plt.plot(t1, x[:, 0])
    plt.plot(t, en_signal)
    plt.xlabel("Time [s]")
    plt.xlim(0, 0.01)
    plt.show()
