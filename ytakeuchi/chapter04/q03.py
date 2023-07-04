import numpy as np


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
    y = np.zeros((len(frames), L // 2 + 1), dtype="complex")  # rfftにより(L/2)+1の配列が返される
    for i in range(len(frames)):
        y[i] = np.fft.rfft(frames[i] * w)
    return y.T  # (2/L+1)xTの行列にするため，転置


##########確認コード##########

L = 5
S = 3
x = np.array([1, 3, 5, 7, 9])
w = np.hamming(L)
print(frame_split(L, S, x))
for frame in frame_split(L, S, x):
    print(frame * w)
X = stft(L, S, w, x)
print(X)  # 3x2の行列となるはず
print(np.shape(X))
