import numpy as np


def calc_amv(p, theta, f):
    c = 334
    u = np.array([np.sin(np.deg2rad(theta)), np.cos(np.deg2rad(theta)), 0])
    M = len(p)
    a = np.zeros(M, dtype="complex")
    for m in range(M):
        a[m] = np.exp(2j * np.pi * f / c * np.dot(u, p[m]))
    return a


if __name__ == "__main__":
    ##########1.の場合##########

    theta = 45
    f = 1000
    p = np.array([[-0.05, 0, 0], [0, 0, 0], [0.05, 0, 0]])

    a = calc_amv(p, theta, f)
    print(a)

    ##########2.の場合##########

    theta = 45
    f = 1000
    p = np.array([[0, 0.05, 0], [np.sqrt(3) / 40, -0.025, 0], [-np.sqrt(3) / 40, -0.025, 0]])

    a = calc_amv(p, theta, f)
    print(a)
