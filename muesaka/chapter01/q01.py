import matplotlib.pyplot as plt
import numpy as np


# 正弦波を返す
def generate_signal(A, sec, sr, freq):
    t = np.linspace(0, sec, int(sr * sec))  # [0:s]の区間で要素数sr*sの等差数列を生成
    signal = A * np.sin(2 * np.pi * freq * t)  # 正弦波Asin(2πft)の信号を数列tに合わせて生成
    return t, signal


# 単一信号をプロット
def plot_signal(t, signal, min, max, filename):
    plt.plot(t, signal)  # x=t, y=signalでプロット
    plt.xlim(min, max)  # x軸描画範囲
    plt.xlabel("Time")  # x軸ラベル
    plt.ylabel("Amplitude")  # y軸ラベル
    plt.savefig(filename)  # ファイル名で保存
    plt.show()  # ターミナルで描画


if __name__ == "__main__":
    A = 1.0  # 振幅
    sec = 3.0  # 信号長
    sr = 16000  # サンプリング周波数
    freq = 440  # 周波数

    t, signal = generate_signal(A, sec, sr, freq)  # 正弦波を生成
    plot_signal(t, signal, min=0, max=0.03, filename="q01.pdf")  # 生成した正弦波をプロット
