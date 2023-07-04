import numpy as np
import matplotlib.pyplot as plt


def synth_window(S, w):
    Q = len(w) // S
    ws = np.zeros(len(w))
    for l in range(len(w)):
        sum_w = 0
        for m in range(1 - Q, Q):
            if l - m * S >= 0 and l - m * S < len(w):  # 存在しないインデックスは0として扱う
                sum_w += w[l - m * S] ** 2
        ws[l] = w[l] / sum_w
    return ws


##########確認コード##########

S = 2
w = np.array([0, 0.5, 1, 0.5, 0])  # Q=2
print(synth_window(S, w))
"""
ws[0]=0（分子が0）
ws[1]=0.5/(w[3]^2+w[1]^2)=0.5/(0.25+0.25)=1
ws[2]=1/(w[4]^2+w[2]^2+w[0]^2)=1/(0+1+0)=1
ws[3]=0.5/(w[3]^2+w[1]^2)=0.5/(0.25+0.25)=1
ws[4]=0（分子が0）
"""

plt.subplots_adjust(hspace=0.6, wspace=0.3)
L = 1000
w = np.hamming(L)
for i in range(4):
    S = L // (2 ** (i + 1))
    wn = synth_window(S, w)
    plt.subplot(2, 2, i + 1)
    plt.plot(wn)
    plt.title(f"S={S}, Q={L//S}")
plt.show()  # Sが小さくなるにつれてQが大きくなり，元の窓関数の定数倍に近づくはず
