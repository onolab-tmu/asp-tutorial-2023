import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import q01  # 問題1で作った関数を利用
import q04  # 問題4で作った関数を利用

if __name__ == "__main__":
    A = 1.0  # 振幅
    sec = 3.0  # 信号長
    sr = 16000  # サンプリング周波数
    freq = 440  # 周波数

    t, signal = q01.generate_signal(A, sec, sr, freq)  # 正弦波を生成
    _, white_noise = q04.generate_white_noise(sec, sr)  # ホワイトノイズを生成
    mixed_signal = signal + white_noise  # 正弦波とホワイトノイズを足し合わせる
    q01.plot_signal(
        t, mixed_signal, min=0, max=0.03, filename="q05.pdf"
    )  # 生成した正弦波をプロット
