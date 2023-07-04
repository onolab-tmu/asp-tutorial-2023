from pathlib import Path
from typing import Union
import numpy as np
import matplotlib.pyplot as plt
from q01 import dft


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

    x = np.zeros(8)
    x[0] = 1
    X = dft(x)

    plt.rcParams.update(config)
    fig, ax = plt.subplots(3, 1)
    ax[0].stem(x)
    ax[0].set_title("x")
    ax[0].grid()
    ax[1].stem(X.real)
    ax[1].set_title("X.real")
    ax[1].grid()
    ax[2].stem(X.imag)
    ax[2].set_title("X.imag")
    ax[2].grid()
    plt.tight_layout()
    plt.savefig(out_p / "02.pdf")
    plt.clf()
    plt.close()


if __name__ == "__main__":
    out_p = Path.cwd() / "outputs"
    if not out_p.exists():
        out_p.mkdir(parents=True)

    main(out_p)

    print("Finished")
