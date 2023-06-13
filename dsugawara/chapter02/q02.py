import numpy as np
import q01

if __name__ == "__main__":
    delta = np.array([1, 0, 0, 0, 0, 0, 0, 0])

    Delta = q01.my_dft(delta)
    print(Delta)
