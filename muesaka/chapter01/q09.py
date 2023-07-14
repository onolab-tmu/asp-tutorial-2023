import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import q01  # 問題1で作った関数を利用
import q04  # 問題4で作った関数を利用
import q06  # 問題6で作った関数を利用
import q07  # 問題7で作った関数を利用


if __name__ == "__main__":
    sr_down = 8000  # 間引き後のサンプリング周波数

    signal, sr = sf.read("q08.wav")  # 間引き前の信号とsr
    decimation = int(sr / sr_down)  # 入力のsr/出力のsrで間引きのステップ数を計算
    signal_down = signal[::decimation]  # decimationの数ごとに抽出（間引く）
    sf.write(
        "q09.wav", signal_down, sr_down, subtype="FLOAT"
    )  # 間引き処理の影響を考え精度維持のためFLOATを指定
