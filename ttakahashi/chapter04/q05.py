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


def comp_wnd(wnd, S):
    L = wnd.size
    Q = int(np.floor(L / S))
    cwnd = np.empty(L, dtype=np.float64)
    for i in range(L):
        k = i - (Q - 1) * S
        if k < 0:
            k = 0
        cwnd[i] = wnd[i] / np.sum(wnd[k : i + (Q - 1) * S] ** 2)
    return cwnd


def main(output_dir: Union[Path, str]):
    out_p = Path(output_dir)

    L = 1000
    S = 500
    wnd = np.hamming(L)
    cwnd = comp_wnd(wnd, S)

    plt.rcParams.update(config)
    fig, ax = plt.subplots(2, 1)
    ax[0].plot(wnd)
    ax[0].grid()
    ax[0].set_title("Hamming window")
    ax[1].plot(cwnd)
    ax[1].set_title("Composite window")
    ax[1].grid()
    plt.tight_layout()
    plt.savefig(out_p / "05.pdf")
    plt.clf()
    plt.close()


if __name__ == "__main__":
    out_p = Path.cwd() / "outputs"
    if not out_p.exists():
        out_p.mkdir(parents=True)

    main(out_p)

    print("Finished")
