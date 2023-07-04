import numpy as np
from q01 import pad
from q02 import frame_div


def stft(x, L, S, wnd):
    x_t = frame_div(x, L, S)
    T = len(x_t)
    X = np.array([np.fft.rfft(x_t[t] * wnd) for t in range(T)], dtype="complex")
    return X.T


def main():
    L = 4
    S = 3

    x = np.ones(8)
    wnd = np.hamming(L)
    x_pad = pad(x, L, S)
    x_t = frame_div(x, L, S)
    x_stft = stft(x, L, S, wnd)

    print(f"x: {x}")
    print(f"x_pad: {x_pad}")
    print(f"x_t: {x_t}")
    print(f"x_t.shape: {x_t.shape}")
    print(f"x_stft: {x_stft}")
    print(f"x_stft.shape: {x_stft.shape}")


if __name__ == "__main__":
    main()

    print("Finished")
