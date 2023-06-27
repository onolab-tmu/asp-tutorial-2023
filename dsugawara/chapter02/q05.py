import numpy as np
import matplotlib.pyplot as plt
import q01

if __name__ == "__main__":
    delta = np.array([1, 0, 0, 0, 0, 0, 0, 0])

    Delta = np.fft.fft(delta)
    print(Delta)

    my_Delta = q01.my_dft(delta)
    print(my_Delta)

    print(Delta == my_Delta)
