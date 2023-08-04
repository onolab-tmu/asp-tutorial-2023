import numpy as np
import matplotlib.pyplot as plt

from q03 import manifold_vector
from q08 import calc_beam_pattern


if __name__ == "__main__":
    n_mic = 3
    D = [0.02, 0.05, 0.10]
    n_d = len(D)
    theta = 0
    coords = []
    for d in D:
        temp = []
        for m in range(n_mic):
            temp.append([(m - (n_mic - 1) / 2) * d, 0, 0])
        coords.append(temp)
    coords = np.array(coords)

    F = 1000
    fs = 16000
    f_array = np.arange(F) * fs / 2 / (F - 1)

    plt.figure(figsize=(12, 8))
    for i in range(n_d):
        w = []
        for f in f_array:
            w.append(manifold_vector(coords[i], theta, f))
        w = np.array(w) / n_mic

        beam_pattern = calc_beam_pattern(w, coords[i], fs)
        beam_pattern = 20 * np.log10(np.abs(beam_pattern))

        angles = np.arange(360)
        X, Y = np.meshgrid(angles, f_array)

        plt.subplot(n_d, 1, i + 1)
        plt.title(f"Beam pattern (d = {D[i]} [m])")
        plt.pcolormesh(X, Y, beam_pattern, cmap="gray")
        plt.colorbar()
    plt.tight_layout()
    plt.show()
