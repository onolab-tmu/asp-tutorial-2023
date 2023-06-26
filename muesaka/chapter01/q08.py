import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import q01  # 問題1で作った関数を利用
import q04  # 問題4で作った関数を利用
import q06  # 問題6で作った関数を利用
import q07  # 問題7で作った関数を利用


if __name__ == "__main__":
    A = 1.0  # 振幅
    sec = 3.0  # 信号長
    sr = 16000  # サンプリング周波数
    freq = 440  # 周波数
    snr = 6  # SNR（dB）

    t, signal = q01.generate_signal(A, sec, sr, freq)  # 正弦波を生成
    mixed_signal = q07.target_snr_mixed_signal(signal, snr)  # snrを指定して混合信号を作成
    sf.write("q08.wav", mixed_signal, sr, "PCM_16")  # 16bit PCMで保存
