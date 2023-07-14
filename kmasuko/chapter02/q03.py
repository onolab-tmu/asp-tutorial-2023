from q01 import dft, idft
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    x = np.zeros(8)  # [1,0,0,0,0,0,0,0]
    x[0] = 1
    x_dft = dft(x)
    x_idft = idft(x_dft)
    print(x_idft)

    plt.figure()
    plt.stem(x_idft)
    plt.ylabel("Amp")
    plt.show()
