import numpy as np
import matplotlib.pyplot as plt
import q07


def generate_signal(A, sec, sr, freq):
    t = np.linspace(0, sec, int(sr * sec))  # [0:s]の区間で要素数sr*sの等差数列を生成
    signal = A * np.sin(2 * np.pi * freq * t)  # 正弦波Asin(2πft)の信号を数列tに合わせて生成
    return t, signal


def circular_convolution(x, h):
    N = x.size
    n = np.arange(N)  # ファンシーインデックス
    z = np.zeros(N, dtype=complex)
    for k in range(N):
        z[k] = np.sum(x[n] * h[k - n])  # ファンシーインデックスで計算

    return z


if __name__ == "__main__":
    A = 1.0  # 振幅
    sec = 3.0  # 信号長
    sr = 16000  # サンプリング周波数
    freq = 440  # 周波数

    _, x = generate_signal(A, sec, sr, freq)  # 正弦波を生成
    w_x = q07.hamming(x.size)  # ハミング窓
    x_hamming = x * w_x  # q8の結果

    X = np.fft.fft(x)  # X[k] 信号のDFT
    Y = np.fft.fft(w_x)  # Y[k] 窓のDFT

    Z = circular_convolution(X, Y)  # 巡回畳み込み
    z = np.fft.ifft(Z)  # ifft

    fig, ax = plt.subplots(2, 1, tight_layout=True)  # q08とq10の結果を比較
    ax[0].plot(x_hamming.real)
    ax[0].set_title("x_hamming")
    ax[1].plot(z.real)
    ax[1].set_title("z")

    plt.show()
