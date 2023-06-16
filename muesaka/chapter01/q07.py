import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import q01  # 問題1で作った関数を利用
import q04  # 問題4で作った関数を利用
import q06  # 問題6で作った関数を利用


# 指定のSNRとなるようにホワイトノイズを調整した混合信号を返す
def target_snr_mixed_signal(s, snr):
    x = np.random.normal(loc=0, scale=1, size=len(s))  # 平均0標準偏差1（分散1）のガウシアンホワイトノイズを生成
    tmp1 = sum(s**2)  # 途中計算
    tmp2 = sum(x**2)  # 途中計算
    tmp3 = 10 ** (snr / 10)  # 途中計算
    scaled_amp = np.sqrt(tmp1 / tmp2 / tmp3)  # 調整した振幅を計算
    x = scaled_amp * x  # 調整した振幅をノイズにかけ合わせる
    mixed_signal = s + x  # 混合信号を作成
    return mixed_signal


if __name__ == "__main__":
    A = 1.0  # 振幅
    sec = 3.0  # 信号長
    sr = 16000  # サンプリング周波数
    freq = 440  # 周波数
    snr = 6  # SNR（dB）

    t, signal = q01.generate_signal(A, sec, sr, freq)  # 正弦波を生成
    mixed_signal = target_snr_mixed_signal(signal, snr)  # snrを指定して混合信号を作成

    noise = mixed_signal - signal  # 混合信号 - 元信号で期待したsnrのノイズが得られるか
    sampled_snr = q06.calc_snr(signal, noise)  # SNRを計算
    print(f"元信号とSNRが{snr}dBに対し混合信号-元信号で得たノイズのSNRは{sampled_snr}である")
