import numpy as np


def dft(x):
    N = x.size
    n = np.arange(N)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        X[k] = np.sum(x[n] * np.exp(-1j * 2 * np.pi * k * n / N))
    return X


def idft(X):
    N = X.size
    k = np.arange(N)
    x = np.zeros(N, dtype=complex)
    for n in range(N):
        x[n] = 1 / N * np.sum(X[k] * np.exp(1j * 2 * np.pi * k * n / N))
    return x


def main():
    x = np.array([1, 2, 3, 4])
    X = dft(x)
    idft_X = np.abs(idft(X))

    print(f"x: {x}")
    print(f"X: {X}")
    print(f"idft_X: {idft_X}")


if __name__ == "__main__":
    main()

    print("Finished")
