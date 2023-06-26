from pathlib import Path
from typing import Optional, Union
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


config = {
    "figure.subplot.bottom": 0.15,
    "figure.subplot.left": 0.15,
    "figure.figsize": [10.0, 8.0],
    "font.size": 18.0,
    # "font.family": "Times New Roman",
    # "mathtext.fontset": "cm",
    "legend.borderaxespad": 1,
    # "lines.linewidth": 10,
    "savefig.transparent": True,
}


def main(output_dir: Union[Path, str]):
    out_p = Path(output_dir)

    sec = 3  # time (sec)
    sr = 16000  # sampling rate (Hz)

    t = np.arange(sec * sr) / sr
    y = np.random.randn(sr * sec)

    sf.write(out_p / "04.wav", y, sr, format="WAV", subtype="PCM_16")

    plt.rcParams.update(config)
    plt.plot(t, y)
    plt.xlim(0, sec)
    plt.ylim(min(y), max(y))
    plt.xlabel("Time (sec)")
    plt.ylabel("Amplitude")
    plt.title("White noise")
    plt.grid()
    plt.tight_layout()
    plt.savefig(out_p / "04.pdf")
    plt.clf()
    plt.close()


if __name__ == "__main__":
    out_p = Path.cwd() / "04/outputs"
    if not out_p.exists():
        out_p.mkdir(parents=True)

    main(out_p)

    print("Finished")
