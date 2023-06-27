import numpy as np
import matplotlib.pyplot as plt
import q08

if __name__ == "__main__":
    fs = 16000
    N = 10
    a = [1, -0.3]
    b = [0.4]
    H = np.empty(N, dtype=complex)
    for i in range(0, N):
        f = i / N * fs
        H[i] = q08.culc_freq_response(a, b, f, fs)
    print(H)

    fig = plt.figure(figsize=[6.0, 6.0])
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    ax1.plot(np.abs(H))
    ax1.set_title("amp")
    ax2.plot(np.angle(H))
    ax2.set_title("phase")
    plt.tight_layout
    plt.savefig("q10.pdf")
