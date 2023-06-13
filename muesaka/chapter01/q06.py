import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import q01  # 問題1で作った関数を利用
import q04  # 問題4で作った関数を利用


# 信号長の等しい信号sとxのSNRを計算
def calc_snr(s, x):
    snr = 10 * np.log10(np.sum(s**2) / np.sum(x**2))
    return snr


if __name__ == "__main__":
    A = 1.0  # 振幅
    sec = 3.0  # 信号長
    sr = 16000  # サンプリング周波数
    freq1 = 440  # 周波数 440Hz
    freq2 = 440  # 周波数 440Hz

    _, s = q01.generate_signal(A, sec, sr, freq1)  # 440Hzの正弦波sを生成
    _, x = q01.generate_signal(A, sec, sr, freq2)  # 440Hzの正弦波xを生成
    sampled_snr = calc_snr(s, x)  # sとxのSNRを計算
    print(f"周波数{freq1}と{freq2}のSNRは{sampled_snr}である")  # freq1とfreq1のsnrをprint
