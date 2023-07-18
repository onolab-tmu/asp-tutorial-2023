import numpy as np
from q04 import calc_spatial_corr


def zero_pad(L, S, x):
    y = np.pad(x, (L - S, L - S))
    len_modS = len(y) % S
    if len_modS > 0:
        y = np.pad(y, (0, S - len_modS))
    return y


def frame_split(L, S, x):
    x_tilde = zero_pad(L, S, x)
    L_array = np.arange(L)
    y = x_tilde[L_array].reshape(1, L)
    t = 1
    while t * S + L <= len(x_tilde):
        y = np.append(y, x_tilde[t * S + L_array].reshape(1, L), axis=0)
        t += 1
    return y


def stft(L, S, w, x):
    frames = frame_split(L, S, x)
    y = np.zeros((len(frames), L // 2 + 1), dtype="complex")
    for i in range(len(frames)):
        y[i] = np.fft.rfft(frames[i] * w)
    return y.T


if __name__ == "__main__":
    fs = 16000
    l = 5

    np.random.seed(0)
    wn1 = np.random.normal(0, 1, fs * l)
    wn2 = np.random.normal(0, 1, fs * l)

    L = 512
    S = 256
    w = np.hanning(L)

    WN1 = stft(L, S, w, wn1)
    WN2 = stft(L, S, w, wn2)

    WN = np.array([WN1, WN2])
    R = calc_spatial_corr(WN)
    print(np.shape(R))
    print(np.real(R[100]))
