import numpy as np

n_mic = 3  # マイクの数
theta = 45  # 音源の方向[°]
d = 0.05  # マイク間の距離[m]
c = 334  # 音速[m/s]
f = 1000  # 周波数[Hz]

# 直線状アレイのアレイマニフォールドベクトル
amv = np.zeros((n_mic, 1), dtype=np.complex64)
theta = np.radians(theta)  # deg→radに変換
u = [np.sin(theta), np.cos(theta), 0]

for m in range(n_mic):
    pm = [d * (m - (n_mic - 1) / 2), 0, 0]
    inp = np.dot(pm, u)
    amv[m] = np.exp(1j * 2 * np.pi * f * inp / c)

print(amv)
