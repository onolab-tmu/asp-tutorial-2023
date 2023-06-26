import numpy as np
import matplotlib.pyplot as plt
import q01


if __name__ == "__main__":
    delta = np.array([1, 0, 0, 0, 0, 0, 0, 0])

    Delta = q01.my_dft(delta)
    delta_idft = q01.my_idft(Delta)

    N = np.arange(0, len(delta_idft))
    plt.figure(figsize=[6.0, 4.0])
    plt.stem(N, delta_idft)
    plt.savefig("q03.pdf")
