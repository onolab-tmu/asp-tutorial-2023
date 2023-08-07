import numpy as np
import matplotlib.pyplot as plt
import q03
import q08

if __name__ == "__main__":
    L = 1024
    S = 512
    F = L // 2 + 1
    fs = 16000

    d_list = [2, 5, 10]  # マイク間隔
    for d in d_list:
        p = np.array([[-d, 0, 0], [0, 0, 0], [d, 0, 0]])
        w = np.empty([F, 3], dtype="complex")
        for Fn in range(0, F):
            f = (fs / 2) / (F - 1) * Fn
            w[Fn, :] = q03.array_vector(p, 0, f)
        w = w / 3

        q08.plot_beampattern(w, p, fs, name="q09")
