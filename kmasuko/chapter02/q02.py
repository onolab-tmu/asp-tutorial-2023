from q01 import dft
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    x = np.zeros(8)  # [1,0,0,0,0,0,0,0]
    x[0] = 1
    x_dft = dft(x)

    plt.figure()
    plt.plot(np.abs(x_dft))
    plt.xlabel("Freq [Hz]")
    plt.ylabel("Amp")
    plt.show()
