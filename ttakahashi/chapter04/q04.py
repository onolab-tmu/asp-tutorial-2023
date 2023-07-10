from pathlib import Path
from typing import Union
import numpy as np
import matplotlib.pyplot as plt
from q03 import stft


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


LABELS = {
    0: ("viridis", "Power spectrogram"),
    1: ("viridis", "Phase spectrogram"),
    2: (plt.cm.Reds, "Cosine of phase spectrogram"),
    3: (plt.cm.Blues, "Sine of hase spectrogram"),
}


def main(output_dir: Union[Path, str]):
    out_p = Path(output_dir)

    A = 1  # amplitude
    f = 440  # frequency (Hz)
    sec = 0.1  # time (sec)
    sr = 16000  # sampling rate (Hz)

    t = np.arange(sec * sr) / sr
    y = A * np.sin(2 * np.pi * f * t)

    L = 1000
    S = 500
    wnd = np.hamming(L)
    y_stft = stft(y, L, S, wnd)

    print(f"y_stft.shape: {y_stft.shape}")

    spec = [np.abs(y_stft), np.angle(y_stft), np.cos(np.angle(y_stft)), np.sin(np.angle(y_stft))]

    plt.rcParams.update(config)
    fig, ax = plt.subplots(4, 1)
    for i in range(len(spec)):
        # ax[i].pcolormesh(spec[i])
        ax[i].imshow(
            spec[i],
            cmap=LABELS[i][0],
            interpolation="nearest",
            aspect="auto",
            origin="lower",
            extent=[0, y_stft.shape[1], 0, y_stft.shape[0]],
        )
        ax[i].set_title(LABELS[i][1])
        ax[i].set_rasterized(True)
    fig.supxlabel("Frame")
    fig.supylabel("Frequency (Hz)")
    plt.tight_layout()
    fig.subplots_adjust(left=0.13, right=1 - 0.13, bottom=0.11, top=1 - 0.11, hspace=0.8)
    plt.savefig(out_p / "04.pdf", dpi=300)
    plt.clf()
    plt.close()


if __name__ == "__main__":
    out_p = Path.cwd() / "outputs"
    if not out_p.exists():
        out_p.mkdir(parents=True)

    main(out_p)

    print("Finished")
