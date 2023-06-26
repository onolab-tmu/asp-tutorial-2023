from pathlib import Path
from typing import Union
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


config = {
    "figure.subplot.bottom": 0.15,
    "figure.subplot.left": 0.15,
    "figure.figsize": [10, 8],
    "font.size": 24,
    "font.family": "Times New Roman",
    "mathtext.fontset": "cm",
    "legend.borderaxespad": 1,
    "lines.linewidth": 2,
    "savefig.transparent": True,
}


def main(input_dir: Union[Path, str], output_dir: Union[Path, str]):
    in_p = Path(input_dir)
    out_p = Path(output_dir)

    sec = 3  # time (sec)
    M = 5

    y1, sr = sf.read(in_p / "09.wav")
    y2 = [np.mean(y1[i : i + M]) if i < len(y1) - M else np.mean(y1[len(y1) - M :]) for i in range(len(y1))]
    t = np.arange(sec * sr) / sr

    plt.rcParams.update(config)
    plt.plot(t, y1, label="original")
    plt.plot(t, y2, label="averaged")
    plt.legend(bbox_to_anchor=(1, 1), loc="upper right")
    plt.xlim(0, sec)
    plt.ylim(min(min(y1), min(y2)), max(max(y1), max(y2)))
    plt.xlabel("Time (sec)")
    plt.ylabel("Amplitude")
    plt.title("5-point moviing average")
    plt.grid()
    plt.tight_layout()
    plt.savefig(out_p / "10.pdf")
    plt.clf()
    plt.close()


if __name__ == "__main__":
    in_p = Path.cwd() / "outputs"
    out_p = Path.cwd() / "outputs"
    if not out_p.exists():
        out_p.mkdir(parents=True)

    main(in_p, out_p)

    print("Finished")
