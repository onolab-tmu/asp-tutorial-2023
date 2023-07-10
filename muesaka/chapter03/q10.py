import numpy as np
import matplotlib.pyplot as plt
import q08


if __name__ == "__main__":
    N = 10
    x = np.zeros(N, dtype=int)
    x[0] = 1  # 単位インパルス信号

    a = np.zeros(10)
    a[0] = 1
    a[1] = -0.3  # q06と同じ条件

    b = np.zeros(10)
    b[0] = 0.4  # q06と同じ条件

    fs = 16000
    f = np.arange(N) * fs / N
    omega = 2 * np.pi * f / fs
    H = q08.frequency_response(a, b, omega)

    print("abs H:{}".format(np.abs(H)))
    print("angle H:{}".format(np.angle(H)))

    fix, ax = plt.subplots(2, 1, tight_layout=True)
    ax[0].plot(omega, np.abs(H))
    ax[0].set_title("abs H")
    ax[1].plot(omega, np.angle(H))
    ax[1].set_title("angle H")
    plt.show()


"""
abs H:[0.57142857 0.5144339  0.42056599 0.35418898 0.31868613 0.30769231
 0.31868613 0.35418898 0.42056599 0.5144339 ]
angle H:[ 0.00000000e+00 -2.28772828e-01 -3.04678520e-01 -2.55408115e-01
 -1.40955555e-01 -2.82610800e-17  1.40955555e-01  2.55408115e-01
  3.04678520e-01  2.28772828e-01]

"""
