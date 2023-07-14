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
    sr_down = 8000

    y1, sr = sf.read(in_p / "08.wav")
    y2 = y1[:: sr // sr_down]

    t1 = np.arange(sec * sr) / sr
    t2 = np.arange(sec * sr_down) / sr_down

    sf.write(out_p / "09.wav", y2, sr_down, format="WAV", subtype="PCM_16")

    plt.rcParams.update(config)
    plt.plot(t1, y1, label="SR: 16000 (Hz)")
    plt.plot(t2, y2, label="SR: 8000 (Hz)")
    plt.legend(bbox_to_anchor=(1, 1), loc="upper right")
    plt.xlim(0, 0.001)
    plt.ylim(min(min(y1), min(y2)), max(max(y1), max(y2)))
    plt.xlabel("Time (sec)")
    plt.ylabel("Amplitude")
    plt.title("Down sampling")
    plt.grid()
    plt.tight_layout()
    plt.savefig(out_p / "09.pdf")
    plt.clf()
    plt.close()


if __name__ == "__main__":
    in_p = Path.cwd() / "outputs"
    out_p = Path.cwd() / "outputs"
    if not out_p.exists():
        out_p.mkdir(parents=True)

    main(in_p, out_p)

    print("Finished")
