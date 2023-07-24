import numpy as np
import matplotlib.pyplot as plt


"""5. 合成窓を作成する関数"""


def synthesis_window(S, w):
    L = len(w)
    l = np.arange(L)
    Q = int(L / S)

    # 窓関数におけるインデックス0未満とL以上を作成．ただし，末尾にのみpaddingする．
    w_ = np.pad(w, (0, S * (Q - 1)))
    deno = np.zeros(L)  # 分母の配列．長さはL．
    for m in range(1 - Q, Q):
        idx = l - m * S  # 負の値でもOK．w_の末尾に0をpaddingしてある．
        deno += w_[idx] ** 2
    w_s = w / deno
    return w_s


L = 1000
S = 500
S2 = 250
S3 = 125
w = np.hamming(L)

w_s = synthesis_window(S, w)
w_s2 = synthesis_window(S2, w)
w_s3 = synthesis_window(S3, w)

l = np.arange(L)
plt.figure()
plt.subplots_adjust(hspace=0.7)
plt.subplot(3, 1, 1)
plt.title("Q = 0.5")
plt.plot(l, w_s)
plt.subplot(3, 1, 2)
plt.title("Q = 0.25")
plt.plot(l, w_s2)
plt.subplot(3, 1, 3)
plt.title("Q = 0.125")
plt.plot(l, w_s3)
plt.savefig("4_5.png")
