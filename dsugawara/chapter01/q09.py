import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

if __name__ == "__main__":
    x, fs = sf.read("08.wav")
    fs_down = 8000
    step_down = fs // fs_down
    x_down = x[::step_down]

    sf.write(file="09.wav", data=x_down, samplerate=fs_down)

    # 確認
    t = np.arange(0, len(x) // fs, 1 / fs)
    t_down = np.arange(0, len(x_down) // fs_down, 1 / fs_down)

    plt.figure(figsize=[6.0, 4.0])
    plt.plot(t, x, marker=".", label=f"fs={fs}")
    plt.plot(t_down, x_down, marker="o", label=f"fs={fs_down}")
    plt.xlim(0, 16 / fs)
    plt.legend()
    plt.savefig("09conf.pdf")
