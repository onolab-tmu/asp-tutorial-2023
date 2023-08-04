import numpy as np
import matplotlib.pyplot as plt
from q03 import calc_amv
from q08 import plot_bp


if __name__ == "__main__":
    theta = 0
    fs = 16000

    ds = [0.02, 0.05, 0.10]

    plt.subplots_adjust(wspace=0.6)
    plt.figure(figsize=(16, 3))
    for i, d in enumerate(ds):
        p = np.array([[-1, 0, 0], [0, 0, 0], [1, 0, 0]]) * d

        w = []
        for _f in range(512):
            w.append(calc_amv(p, theta, (fs / 2) / 511 * _f))
        w = np.array(w).T / 3.0

        plot_bp(w, p, fs, title=f"Beam pattern (d={d}m)", sub=130 + i + 1)
    plt.show()
