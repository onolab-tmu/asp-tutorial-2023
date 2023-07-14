import numpy as np
import matplotlib.pyplot as plt
import q07


def generate_signal(A, sec, sr, freq):
    t = np.linspace(0, sec, int(sr * sec))  # [0:s]の区間で要素数sr*sの等差数列を生成
    signal = A * np.sin(2 * np.pi * freq * t)  # 正弦波Asin(2πft)の信号を数列tに合わせて生成
    return t, signal


if __name__ == "__main__":
    A = 1.0  # 振幅
    sec = 3.0  # 信号長
    sr = 16000  # サンプリング周波数
    freq = 440  # 周波数

    _, x = generate_signal(A, sec, sr, freq)  # 正弦波を生成
    w = q07.hamming(x.size)  # ハミング窓
    x_hamming = x * w  # 窓関数をかける

    fig, ax = plt.subplots(2, 1, tight_layout=True)  # x, x*wをプロットして確認
    ax[0].plot(x)
    ax[0].set_title("x")
    ax[1].plot(x * w)
    ax[1].set_title("x * w")

    plt.show()
