import numpy as np


def pad(x, L, S):
    x_pad = np.pad(x, [L - S, L - S])
    re = np.mod(x_pad.size, S)
    if re != 0:
        x_pad = np.pad(x_pad, [0, S - re])
    return x_pad


def main():
    L = 4
    S = 3

    x = np.ones(8)
    x_pad = pad(x, L, S)

    print(f"x: {x}")
    print(f"x_pad: {x_pad}")


if __name__ == "__main__":
    main()

    print("Finished")
