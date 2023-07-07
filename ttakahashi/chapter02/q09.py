from pathlib import Path
from typing import Union
import numpy as np
import matplotlib.pyplot as plt
from q07 import hamming


config = {
    "figure.subplot.bottom": 0.15,
    "figure.subplot.left": 0.15,
    "figure.figsize": [10, 8],
    "font.size": 24,
    "font.family": "Times New Roman",
    "mathtext.fontset": "cm",
    "pdf.fonttype": 42,
    "legend.borderaxespad": 1,
    "lines.linewidth": 2,
    "savefig.transparent": True,
}


def main(output_dir: Union[Path, str]):
    out_p = Path(output_dir)

    A = 1  # amplitude
    f = 440  # frequency (Hz)
    sec = 3  # time (sec)
    sr = 16000  # sampling rate (Hz)

    t = np.arange(sec * sr) / sr
    y = A * np.sin(2 * np.pi * f * t)
    w = hamming(y.size)
    y_hamming = y * w
    Y_hamming = np.fft.fft(y_hamming)

    mag_spec = 10 * np.log10(np.abs(Y_hamming) ** 2)
    freq_idx = sr * np.arange(Y_hamming.size) / Y_hamming.size

    plt.rcParams.update(config)
    plt.plot(freq_idx, mag_spec)
    plt.title("dft(y*h)")
    plt.grid()
    plt.tight_layout()
    plt.savefig(out_p / "09.pdf")
    plt.clf()
    plt.close()


if __name__ == "__main__":
    out_p = Path.cwd() / "outputs"
    if not out_p.exists():
        out_p.mkdir(parents=True)

    main(out_p)

    print("Finished")
