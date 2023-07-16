from pathlib import Path
from typing import Union
import numpy as np
import matplotlib.pyplot as plt


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


def hamming(N):
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return w


def main(output_dir: Union[Path, str]):
    out_p = Path(output_dir)

    N = 8
    w = hamming(N)
    x = np.arange(N)

    plt.rcParams.update(config)
    fig, ax = plt.subplots(2, 1)
    ax[0].stem(x)
    ax[0].set_title("x")
    ax[0].grid()
    ax[1].stem(x * w)
    ax[1].set_title("x * w")
    ax[1].grid()
    plt.tight_layout()
    plt.savefig(out_p / "07.pdf")
    plt.clf()
    plt.close()


if __name__ == "__main__":
    out_p = Path.cwd() / "outputs"
    if not out_p.exists():
        out_p.mkdir(parents=True)

    main(out_p)

    print("Finished")
