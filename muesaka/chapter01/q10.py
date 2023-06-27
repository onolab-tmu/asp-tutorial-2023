import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import q01  # 問題1で作った関数を利用
import q04  # 問題4で作った関数を利用
import q06  # 問題6で作った関数を利用
import q07  # 問題7で作った関数を利用


# N点移動平均フィルタ
def moving_average_filter(signal, window_size):
    window = np.ones(window_size) / window_size  # すべて1/Nな配列を生成
    signal = np.convolve(signal, window, mode="same")  # 出力のサイズを変えないようsameを使う
    return signal


# 2信号を重ね合わせてプロット
def plot_overlapping_signals(t, s, x, min, max, filename):
    plt.plot(t, s)  # x=t, y=signalでプロット
    plt.plot(t, x)  # x=t, y=xでプロット
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
    window_size = 5  # N点移動平均フィルタ

    signal, sr = sf.read("q09.wav")  # 元信号
    filtered_signal = moving_average_filter(signal, window_size)  # 平均フィルタ適用後の信号
    t, _ = q01.generate_signal(A, sec, sr, freq)  # プロット用x軸を生成
    plot_overlapping_signals(
        t, signal, filtered_signal, min=0, max=3, filename="q10.pdf"
    )  # オーバラップさせて2信号をプロット
