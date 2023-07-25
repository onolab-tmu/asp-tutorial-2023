import numpy as np
import matplotlib.pyplot as plt


def SN(s, x):
    """
    2つの信号sとxのSN比を求める関数
    """
    sum_s2 = 0
    sum_x2 = 0
    for i in range(len(x)):
        sum_s2 += s[i] ** 2
        sum_x2 += x[i] ** 2
    sn = 10 * np.log10(sum_s2 / sum_x2)
    return sn


def SN_noise(s, snr):
    """
    s : 元信号
    snr [dB] : SN比
    noise : 信号sに対するSN比がsnrとなるようなホワイトノイズ
    """
    size_s = len(s)
    noise = np.random.randn(size_s)
    noise = noise / np.sqrt(np.sum(noise**2))  # 正規化
    noise = noise * np.sqrt(np.sum(s**2))  # SN比は0になる．パワーがxと同じ．
    noise = noise * 10 ** (-snr / 20)  # パワーを求める際に2乗することや，log10をとること，雑音noiseのパワーはlog10の中で分母であることから，10**(-snr/20)．
    return noise


A = 1
f = 440
fs = 16000
sec = 1
snr = 10  # dB

t = np.array([i / fs for i in range(int(fs * sec))])
s = np.sin(2 * np.pi * f * t)

# 確認用
# plt.figure()
# plt.plot(t,s)
# plt.xlim(0, 1/440)
# plt.savefig("5_6_sin.png")

noise = SN_noise(s, snr)


# x_2におけるs[n-10]
s_roll2 = np.roll(s, 10)
for i in range(10):
    s_roll2[i] = 0

# x_3におけるs[n-20]
s_roll3 = np.roll(s, 20)
for i in range(20):
    s_roll3[i] = 0

x1 = s + noise
x2 = s_roll2 + noise
x3 = s_roll3 + noise


if __name__ == "__main__":
    # 確認用
    print("SNR : ", SN(s, noise))  # 10近い値になるはず

    # 確認用
    print("\n", s[0:30])
    print(s_roll2[0:30])
    print(s_roll3[0:30])

    plt.figure()
    plt.subplots_adjust(hspace=1.25)
    plt.subplot(3, 1, 1)
    plt.plot(t, x1)
    plt.xlim(0, 0.01)
    plt.title("x1")
    plt.xlabel("t [s]")
    plt.ylabel("Amplitude")
    plt.subplot(3, 1, 2)
    plt.plot(t, x2)
    plt.xlim(0, 0.01)
    plt.title("x2")
    plt.xlabel("t [s]")
    plt.ylabel("Amplitude")
    plt.subplot(3, 1, 3)
    plt.plot(t, x3)
    plt.xlim(0, 0.01)
    plt.title("x3")
    plt.xlabel("t [s]")
    plt.ylabel("Amplitude")
    plt.savefig("5_6.png")
