import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import q01  # 問題1で作った関数を利用


if __name__ == "__main__":
    A = 1.0  # 振幅
    sec = 3.0  # 信号長
    sr = 16000  # サンプリング周波数
    freq = 440  # 周波数

    _, signal = q01.generate_signal(A, sec, sr, freq)  # 正弦波を生成
    sf.write("q02.wav", signal, sr, "PCM_16")  # 16bit PCMで保存
