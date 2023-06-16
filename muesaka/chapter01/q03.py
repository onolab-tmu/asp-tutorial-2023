import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import q01  # 問題1で作った関数を利用


if __name__ == "__main__":
    A = 1.0  # 振幅
    sec = 3.0  # 信号長
    sr = 16000  # サンプリング周波数
    freq1 = 440  # 周波数 440Hz
    freq2 = 660  # 周波数 660Hz

    _, s = q01.generate_signal(A, sec, sr, freq1)  # 440Hzの正弦波sを生成
    _, x = q01.generate_signal(A, sec, sr, freq2)  # 660Hzの正弦波xを生成
    stereo_signal = np.stack([s, x], axis=1)  # sとxの2ch信号に変換（axis=1方向に結合）

    sf.write("q03.wav", stereo_signal, sr, "PCM_16")  # 16bit PCMで保存
