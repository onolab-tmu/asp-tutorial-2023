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


def main(input_dir_02: Union[Path, str], input_dir_04: Union[Path, str], output_dir: Union[Path, str]):
    in_p_02 = Path(input_dir_02)
    in_p_04 = Path(input_dir_04)
    out_p = Path(output_dir)

    sec = 3  # time (sec)
    sr = 16000  # sampling rate (Hz)

    t = np.arange(sec * sr) / sr

    y_02, sr = sf.read(in_p_02 / "02.wav")
    y_04, sr = sf.read(in_p_04 / "04.wav")
    mixture = y_02 + y_04

    plt.rcParams.update(config)
    plt.plot(t, mixture)
    plt.xlim(0, 0.01)
    plt.ylim(min(mixture), max(mixture))
    plt.xlabel("Time (sec)")
    plt.ylabel("Amplitude")
    plt.title("Mixture")
    plt.grid()
    plt.tight_layout()
    plt.savefig(out_p / "05.pdf")
    plt.clf()
    plt.close()


if __name__ == "__main__":
    in_p_02 = Path.cwd() / "02/outputs"
    in_p_04 = Path.cwd() / "04/outputs"
    out_p = Path.cwd() / "05/outputs"
    if not out_p.exists():
        out_p.mkdir(parents=True)

    main(in_p_02, in_p_04, out_p)

    print("Finished")
