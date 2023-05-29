# 白色雑音の生成: ホワイトノイズをサンプリング周波数 16000 Hz で 3 秒分作成しプロットせよ．

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal


def main():
    fs = 16000  # sampling frequency (Hz)
    sig_len = 3  # signal length (sec.)

    t = np.arange(fs * sig_len) / fs  # time
    white_noise = np.random.randn(fs * sig_len)  # ホワイトノイズ

    # plot
    plt.title("White noise")
    plt.plot(t, white_noise)
    plt.ylabel("Amplitude")
    plt.xlabel("Time (sec.)")
    plt.show()

    # 確認方法 (スペクトルのパワーがフラットになることを確認)
    sig_len_sample = fs * sig_len  # signal length (sample)
    white_noise_spec = np.fft.rfft(white_noise)  # ホワイトノイズのスペクトル
    power = 10 * np.log10(np.abs(white_noise_spec) ** 2)
    freq = np.arange(sig_len_sample // 2 + 1) / sig_len_sample * fs
    plt.title("White noise (Freqency domain)")
    plt.plot(freq, power)
    plt.ylabel("Power")
    plt.xlabel("Freq. (Hz)")
    plt.show()

    # 確認方法 (自己相互相関関数を確認)
    t = (np.arange(sig_len_sample * 2 - 1) - sig_len_sample) / fs
    col = signal.fftconvolve(white_noise, white_noise[::-1]) / sig_len_sample

    plt.title("auto correlation")
    plt.plot(t, col)  # インデックス0でピークが1
    plt.show()


if __name__ == "__main__":
    main()
