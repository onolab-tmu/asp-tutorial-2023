import numpy as np
from utils import stft
from q04 import spatial_corr


if __name__ == "__main__":
    fs = 16000
    sec = 5
    np.random.seed(0)
    white = np.array([np.random.randn(fs * sec), np.random.randn(fs * sec)])

    win_len = 512
    shift_len = 256
    win = np.hanning(win_len)

    white_stft = []
    white_stft.append(stft(win_len, shift_len, win, white[0]))
    white_stft.append(stft(win_len, shift_len, win, white[1]))
    white_stft = np.array(white_stft)

    R = spatial_corr(white_stft)
    print(R.shape)
    print(R[100].real)
