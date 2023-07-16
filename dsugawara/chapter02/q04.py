import numpy as np
import matplotlib.pyplot as plt
import q01

if __name__ == "__main__":
    delta = np.array([1, 0, 0, 0, 0, 0, 0, 0])

    Delta = q01.my_dft(delta)
    n = np.arange(0, len(Delta))

    fig = plt.figure(figsize=[6.0, 4.0])
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.stem(n, np.abs(Delta))
    ax1.set_title("amplitude")
    ax2 = fig.add_subplot(2, 1, 2)
    ax2.stem(n, np.angle(Delta))
    ax2.set_title("phase")
    plt.tight_layout()
    plt.savefig("q04.pdf")
