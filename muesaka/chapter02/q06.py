import numpy as np
import matplotlib.pyplot as plt


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
    calc_X = np.fft.fft(x)  # dft計算

    amp_spec = 10 * np.log10(np.abs(calc_X) ** 2)  # 振幅スペクトル（20log10でみやすく）
    phase_spec = np.angle(calc_X)  # 位相スペクトル
    freq_idx = sr * np.arange(calc_X.size) / calc_X.size  # 周波数インデックス

    fig, ax = plt.subplots(2, 1, tight_layout=True)  # calc_Xをプロットして確認
    ax[0].stem(freq_idx, amp_spec)
    ax[0].set_xlim(440 - 5, 440 + 5)  # 440 Hz周辺
    ax[0].set_title("amp_spec")
    ax[1].stem(freq_idx, phase_spec)
    ax[1].set_xlim(440 - 5, 440 + 5)  # 440 Hz周辺
    ax[1].set_title("phase_spec")

    plt.show()
