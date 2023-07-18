import numpy as np


def general_array_manifold_vector(array, theta, f, c):
    theta = np.deg2rad(theta)
    n_mic = array[0].size
    amv = np.zeros((n_mic, 1), dtype=np.complex64)
    u = np.array([np.sin(theta), np.cos(theta), 0])
    for m in range(n_mic):
        inp = np.dot(array[m], u)
        amv[m] = np.exp(1j * 2 * 2 * np.pi * f * inp / c)
    return amv
