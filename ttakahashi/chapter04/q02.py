import numpy as np
from q01 import pad


def frame_div(x, L, S):
    x_pad = pad(x, L, S)
    T = int(np.floor((x_pad.size - L) / S)) + 1
    x_t = np.array([x_pad[t * S : t * S + L] for t in range(T)])
    return x_t


def main():
    L = 4
    S = 3

    x = np.ones(8)
    x_pad = pad(x, L, S)
    x_t = frame_div(x, L, S)

    print(f"x: {x}")
    print(f"x_pad: {x_pad}")
    print(f"x_t: {x_t}")
    print(f"x_t.shape: {x_t.shape}")


if __name__ == "__main__":
    main()

    print("Finished")
