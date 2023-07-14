import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import q01  # 問題1で作った関数を利用


# ホワイトノイズを返す
def generate_white_noise(sec, sr):
    t = np.linspace(0, sec, int(sr * sec))  # [0:s]の区間で要素数sr*sの等差数列を生成
    white_noise = np.random.normal(
        loc=0, scale=1, size=len(t)
    )  # 平均0標準偏差1（分散1）のガウシアンホワイトノイズを生成
    return t, white_noise


if __name__ == "__main__":
    sec = 3.0  # 信号長
    sr = 16000  # サンプリング周波数

    t, white_noise = generate_white_noise(sec, sr)  # ホワイトノイズを生成
    q01.plot_signal(
        t, white_noise, min=0, max=0.03, filename="q04.pdf"
    )  # 生成したホワイトノイズをプロット
