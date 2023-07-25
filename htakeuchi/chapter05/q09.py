import numpy as np
import matplotlib.pyplot as plt
from q08 import array_manifold_vector, BeamPattern, DS


if __name__ == "__main__":
    fs = 16000
    d = [0.02, 0.05, 0.1]  # 単位はm

    p_m = np.array(
        [
            [[-d[0], 0, 0], [0, 0, 0], [d[0], 0, 0]],
            [[-d[1], 0, 0], [0, 0, 0], [d[1], 0, 0]],
            [[-d[2], 0, 0], [0, 0, 0], [d[2], 0, 0]],
        ]
    )

    theta = 0
    F = 512
    M = p_m[0].shape[0]

    f_list = np.array([i * fs / 2 / (F - 1) for i in range(F)])
    a = np.zeros((len(d), F, M), dtype=complex)

    for i in range(len(d)):
        for f in range(F):
            a[i][f] = array_manifold_vector(p_m[i], theta, f_list[f])
        w_f = DS(a[i])
        filename = "5_9_" + str(d[i]) + "cm.png"
        BeamPattern(w_f, p_m[i], fs, filename)
