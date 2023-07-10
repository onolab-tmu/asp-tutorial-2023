import numpy as np


# L-Sこのゼロ詰め　Sの倍数になるようにゼロ詰めする関数
def padding(x, L, S):
    x_pad = np.pad(x, [L - S, L - S])  # 先頭と末尾をゼロ詰め
    re = np.mod(len(x), S)  # Sの倍数か調べる
    if re != 0:
        x_pad = np.pad(x_pad, [0, S - re])  # Sの余り分付け足す
    return x_pad


# フレーム分割
def frame_div(x, L, S):
    x_pad = padding(x, L, S)
    T = int(np.floor((x_pad.size - L) / S)) + 1
    x_t = np.array([x_pad[t * S : t * S + L] for t in range(T)])
    return x_t


def stft(x, L, S, w):
    x_t = frame_div(x, L, S)
    T = len(x_t)
    X = np.array([np.fft.rfft(x_t[t] * w) for t in range(T)], dtype="complex")
    return X.T


#####確認コード#####
L = 4
S = 3
x = np.ones(8)
wnd = np.hamming(L)
x_stft = stft(x, L, S, wnd)
