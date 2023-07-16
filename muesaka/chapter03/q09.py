import numpy as np
import matplotlib.pyplot as plt
import q08


if __name__ == "__main__":
    N = 10
    a_N = 5
    b_N = 5
    a = np.zeros(a_N)
    a[0] = 1  # q05と同じ条件
    b = np.zeros(b_N) + 0.2  # q05と同じ条件

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
abs H:[1.00000000e+00 6.47213595e-01 8.32667268e-17 2.47213595e-01
 3.92523115e-17 2.00000000e-01 6.93889390e-17 2.47213595e-01
 2.42066971e-16 6.47213595e-01]
angle H:[ 0.00000000e+00 -1.25663706e+00  3.14159265e+00 -6.28318531e-01
 -2.35619449e+00  2.44929360e-16 -6.43501109e-01  6.28318531e-01
 -4.76467419e-01  1.25663706e+00]

"""
