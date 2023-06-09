**注意: 「実装せよ」など特に明記されている場合を除いて，適当なライブラリを使用して構いません．**
推奨ライブラリは下記の通りです．また，下記ライブラリの使用を前提とした問題も一部出題されます．

- 行列・ベクトル計算: [numpy](https://numpy.org)
- 可視化: [matplotlib](https://matplotlib.org)
- 音声ファイル操作: [soundfile](https://pysoundfile.readthedocs.io/en/latest/)

# 第 1 章: 基礎

1. **正弦波の生成**: 振幅 1, 周波数 440 Hz の正弦波をサンプリング周波数 16000 Hz で 3 秒分作成しプロットせよ．
2. **WAV ファイルの作成（モノラル）**: 1.で作成した正弦波を 16bit PCM フォーマットで wav ファイルとして保存せよ．
3. **WAV ファイルの作成（ステレオ）**: 振幅 1, 周波数 660 Hz の正弦波をサンプリング周波数 16000 Hz で 3 秒分作成し，1.で作成した信号と合わせて 2ch の wav ファイルとして保存せよ．
4. **白色雑音の生成**: ホワイトノイズをサンプリング周波数 16000 Hz で 3 秒分作成しプロットせよ．
5. **信号の混合**: 1.で作成した正弦波と 4.で作成したホワイトノイズと正弦波を混合してプロットせよ．
6. **SN 比**: 信号長の等しい 2 個の信号 $s[n], x[n]\; (n = 0, \dots, N-1), $ の信号対雑音比 (SN比) $10 \log \frac{\sum _{n=0} ^{N-1} s[n] ^2}{\sum _{n=0} ^{N-1} x[n] ^2}$ を計算する関数を実装せよ．
7. **SN 比を指定した信号の混合（実装）**: SN 比を任意の値に設定できるようにホワイトノイズの振幅を調整する関数を実装せよ．元信号と所望の SN 比を入力として受け取り，ホワイトノイズを重畳した信号を出力すること．
8. **SN 比を指定した信号の混合（確認）**: 8.で実装した関数を用いて，6.と同様にホワイトノイズと正弦波の混合信号を作成し wav ファイルとして保存せよ．ただし，SN 比が 6dB となるようにすること．
9. **間引きによるダウンサンプリング**: 8.で保存した wav ファイルを読み込み，サンプリング周波数を 8kHz に変換して保存せよ．
10. **簡単なフィルタ処理**: 9.の信号に対して 5 点移動平均フィルタを適用した結果と元の信号をプロットせよ．

# 第 2 章: スペクトル解析

1. **DFT/IDFT の実装**: $N$ 点の信号 $x[n] \, (n = 0, \dots , N-1)$ の離散フーリエ変換 (DFT) $$X[k] = \sum _{n=0} ^{N-1} x[n] \exp \left( -j \frac{2\pi k n}{N} \right) \, (k = 0, \dots, N-1)$$ とその逆変換(IDFT)$$x[n] = \frac{1}{N} \sum _{k=0} ^{N-1} X[k] \exp \left( j \frac{2\pi k n}{N} \right) \, (n = 0, \dots, N-1)$$を計算する関数を実装せよ．
2. **DFT の確認**: 1.で実装した関数を用いて 8 点の単位インパルス信号 $\delta [n] = [1, 0, 0, 0, 0, 0, 0, 0]$ の DFT を計算せよ．
3. **IDFT の確認**: 2.の結果の IDFT を計算しプロットせよ．
4. **スペクトルの確認**: 2.の結果の振幅スペクトルおよび位相スペクトル $|X[k]|, \angle X[k] \, (k = 0, \dots, N-1)$ をプロットせよ．
5. **既存の実装との比較**: 8 点の単位インパルス信号の DFT を `numpy.fft.fft` 関数を用いて計算し，2.の結果と比較せよ．なお，これ以降 DFT を計算する場合は `numpy.fft.fft`関数を使用してよい．
6. **正弦波のスペクトル**: 第 1 章 1.で作成した信号の DFT を計算し，振幅スペクトルと位相スペクトルをプロットせよ．（プロットする際はデシベル表記にするために `20 * log10(np.abs(X))` などのようにしてデシベル表記になおしてから計算すると見やすいです．）
7. **窓関数**: 次式で定義される $N$点の Hamming 窓を作成する関数を実装せよ． $$w[n] = 0.54 - 0.46 \cos (2\pi \frac{n}{N - 1}) \, (n = 0, \dots, N-1)$$
8. **窓関数の確認**: 第 1 章 1.で作成した信号に対して 6.の窓関数を適用した信号をプロットせよ．
9. **窓関数の特性**: 第 1 章 1.で作成した信号と同じ長さの Hamming 窓を作成し，DFT を計算せよ．
10. **窓関数とスペクトルの関係**: 第 1 章 1.で作成した信号の DFT を $X[k] (k = 0, \dots, N-1)$，9.の結果を $Y[k] (k = 0, \dots, N-1)$ とする． $X[k]$ と $Y[k]$ の巡回畳み込み $Z[k] = \sum _{n=0} ^{N-1} X[n] Y[k-n] (k = 0, \dots, N-1)$ の IDFT を計算し 8.の結果と比較せよ．

# 第 3 章: 畳み込みと簡単なフィルタ処理

1. **線形畳み込み**: $N$ 点の信号 $x[n], h[n] (n = 0, \dots, N-1)$ の線形畳み込み $z[n] = \sum _{k = 0} ^{N-1} x[k] h[n - k], (n = 0, \dots, 2N - 2)$ を計算する関数を実装せよ．ただし， $n - k < 0$ または $n - k > N-1$ では信号の値は 0 とすること．
2. **巡回畳み込み**: $N$ 点の信号 $x[n], h[n] (n = 0, \dots, N-1)$ の巡回畳み込み $z[n] = \sum _{k = 0} ^{N-1} x[k] h[(n - k) \mod N], (n = 0, \dots, N-1)$ を計算する関数を実装せよ．ただし， $a \mod b$ は $a$ を $b$ で割った余りを表す．
3. **零詰め＋巡回畳み込み**: $N$ 点の信号 $x[n], y[n]$ に適切な零詰めを行って巡回畳み込みを計算することで，線形畳み込みと同じ結果を与える関数を実装せよ．
4. **各種畳み込みの関係**: 1., 2., 3. で実装した関数を用いて $x[n] = [4, 3, 2, 1]$ と $y[n] = [1, 0, -1, 0]$ の線形畳み込み，巡回畳み込み，零詰めを行った巡回畳み込みを計算し結果をプロットせよ．
5. **差分方程式（再帰なし）**: 次の差分方程式 $y[n] = 0.2 x[n] + 0.2 x[n-1] + 0.2 x[n-2] + 0.2 x[n-3] + 0.2 x[n-4]$ で表される信号 $y[n]$ をプロットせよ． ただし， $x[n]$ は単位インパルス信号として 10 点プロットせよ．
6. **差分方程式（再帰あり）**: 次の差分方程式 $y[n] = 0.3 y[n-1] + 0.4 x[n]$ で表される信号 $y[n]$ をプロットせよ． ただし， $x[n]$ は単位インパルス信号として 10 点プロットせよ．
7. **差分方程式（一般系）**: 一般の差分方程式 $a_0 y[n] = - \sum _{k = 1} ^{N} a_k y[n-k] + \sum _{k = 0} ^{M} b_k x[n - k]$ で表される信号を計算する関数を実装せよ．ただし，入力は $a_0, \dots, a_N (a_0 \neq 0)$ の配列， $b_0, \dots, b_M$ の配列，および入力信号 $x[n] (n = 1, \dots, L)$ とすること．
8. **周波数応答**: 次の差分方程式 $y[n] = - \sum _{k = 1} ^{N} a_k y[n-k] + \sum _{k = 0} ^{M} b_k x[n - k]$ で表される信号の周波数応答 $H(e^{j\omega}) = \frac{\sum _{k=0} ^M b_k e^{-j\omega k}}{1 + \sum _{k=1} ^{N} a_k e^{-j\omega k}}$ を計算する関数を実装せよ．ただし， $\omega$ はサンプリング周波数を $f_s$ としたときの正規化各周波数 $\omega = \frac{2 \pi f}{f_s} (0 \leq f \lt f_s)$ である．
9. **周波数応答の確認（再帰なし）**: 8.で実装した関数を用いて，5.の信号の周波数応答 $H(e^{j\omega})$ を計算し，振幅特性 $|H(e^{j\omega})|$ および位相特性 $\angle H(e^{j\omega})$ をプロットせよ．ただし，サンプリング周波数 $f_s = 16000$ とし，$f = 0, \frac{1}{N} f_s, \dots, \frac{N-1}{N} f_s$ まで計算せよ（$N$ は適当に決めてよい）．
10. **周波数応答の確認（再帰あり）**: 8.で実装した関数を用いて，6.の信号の周波数応答 $H(e^{j\omega})$ を計算し，振幅特性 $|H(e^{j\omega})|$ および位相特性 $\angle H(e^{j\omega})$ をプロットせよ．ただし，サンプリング周波数 $f_s = 16000$ とし，$f = 0, \frac{1}{N} f_s, \dots, \frac{N-1}{N} f_s$ まで計算せよ（$N$ は適当に決めてよい）．

# 第 4 章: 短時間フーリエ変換

1. **零詰め**: 窓幅 $L$ ，シフト幅 $S (\lt L)$，および $N$ 点の実数値信号 $x[n]$ $(n = 0, \dots, N-1)$ を入力とし，下記の手順で零詰めした信号を出力する関数を実装せよ．
   1. 入力の先頭および末尾に $L - S$ 個の零詰め: $[\underbrace{0, \dots, 0}_{L - S}, x[0], \dots, x[N-1], \underbrace{0, \dots, 0}_{L - S}]$
   2. 最終的な信号の長さが $S$ の倍数となるよう入力の末尾に零詰め
2. **フレーム分割**: 窓幅 $L$ ，シフト幅 $S (\lt L)$，および $N$ 点の実数値信号 $x[n]$ $(n = 0, \dots, N-1)$ を入力とし，1.で実装した関数を用いて $L$ 点の信号（以下，フレームと呼ぶ）の列を出力する関数を実装せよ．
   1. $t$ $(t = 0, \dots, T-1)$ 番目のフレームを次で求める: $x_t [l] \coloneqq \tilde{x}[tS+l]$ $(l = 0, \dots, L-1)$, ただし， $\tilde{x}[n]$ は零詰め後の入力
3. **STFT の実装**: 窓幅 $L$ ，シフト幅 $S (\lt L)$，窓関数 $w[l] (l = 0, \dots, L-1)$ ，および $N$ 点の実数値信号 $x[n]$ $(n = 0, \dots, N-1)$ を入力とし，下記の手順で $x[n]$ の短時間フーリエ変換を出力する関数を実装せよ．このとき，出力は $(\frac{L}{2}+1) \times T$ の複素数行列となることに注意せよ．
   1. 2.で実装した関数を用いて，各フレームに対して窓関数 $w[l] (l = 0, \dots, L-1)$ をかけ `np.fft.rfft` 関数を適用する．
4. **STFT の確認**: 振幅 1, 周波数 440 Hz の正弦波をサンプリング周波数 16000 Hz で 0.1 秒分作成し，2.で実装した関数を用いてスペクトログラムを計算せよ．ただし，窓幅を 1000，窓関数を Hamming 窓，シフト幅を 500 とすること．さらに，振幅スペクトログラム・位相スペクトログラムをプロットせよ．プロットには `matplotlib.pyplot.pcolormesh` を使用すること．
5. **合成窓**: シフト幅 $S$ と $L$ 点の窓関数 $w[l] (l = 0, \dots, L-1)$ を入力とし，次の結果を出力する関数を実装せよ．なお，これは逆短時間フーリエ変換に用いる最適合成窓のひとつである．
   1. $Q \gets \frac{L}{S}$
   2. $w_\mathrm{s}[l] = \frac{w[l]}{\sum _{m = -(Q - 1)} ^{Q - 1} (w[l - m S]) ^ 2}$
6. **ISTFT の実装**: シフト幅 $S$ および $F\times T$ の複素数行列 $X[f, t]$ $(f = 0, \dots, F-1,\quad t = 0, \dots, T-1)$ を入力とし，下記の手順で $M$ 点の信号 $\hat{x}[n]$ を出力する関数を実装せよ．
   1. 窓幅 $N$ を計算および出力信号の長さ $M$ を計算: $N \gets 2 (F - 1)$, $M \gets S (T - 1) + N$
   2. 出力信号を初期化: $\hat{x}[m] = 0 \quad \forall m$
   3. 各フレーム $t$ について逆 DFT を計算: $z_t[n] \gets \mathcal{F}^{-1}(X[0, t], \dots, X[F-1, t])[n]$ $(n = 0, \dots, N-1)$
      ただし，右辺は $F$ 点の複素数値信号 $X[0, t], \dots, X[F-1, t]$ を逆 DFT した結果の $n$ 番目の要素を表す．逆 DFT には `np.fft.irfft` 関数を使用すること．これにより， $z[n]$ の点数は $N = 2(F-1)$ となることに注意せよ．
   4. Overlap add の計算: $\hat{x}[t S + n] = \hat{x}[t S + n] + w_\mathrm{s}[n] z_t[n]$
      ただし， $w_\mathrm{s}[n]$ は 5.で計算される最適合成窓， $z_t[n]$は上で計算した逆 DFT である．
7. **ISTFT の確認**: 6.で実装した関数を用いて，4.の結果の逆短時間フーリエ変換を計算し結果をプロットせよ．
8. **合成窓の確認**: 6.の実装において，合成窓をすべての $n$ に対して $w_\mathrm{s}[n] = 1$ とした場合の ISTFT を実装し，前問の結果と比較せよ．
9. **不確定性原理の確認**: 周波数 100 ~ 16000 Hz のチャープ信号をサンプリング周波数 16000 Hz で 1 秒分作成し，窓幅/シフト幅を 100/50, 200/100, 400/200, 800/400 と変えながらスペクトログラムをプロットし結果を比較せよ．なお，チャープ信号の作成には `scipy.signal.chirp` 関数を使用せよ．
10. **時間周波数のインデクスと物理量との対応**: スペクトログラム，サンプリング周波数，シフト幅を入力とし，3.の実装で得られるスペクトログラムの縦軸と横軸の単位をそれぞれ周波数と秒に変換する関数を実装せよ．これを用いて，4.の結果を再度プロットして確認せよ．

# 第 5 章: アレイ信号処理基礎

1. **アレイマニフォールドベクトル（直線状アレイ）**: アレイ間隔 $d$ [m]，マイク数 $M$ ，音源方向 $\theta$，周波数 $f$ [Hz] を入力とし，2 次元平面における直線状等間隔アレイのアレイマニフォールドベクトル $\boldsymbol{a}$ を計算する関数を実装せよ．ただし， $c$ は音速を表し，本演習では $c = 334$ [m/s]とする．また， $\theta$ は $y$ 軸から反時計回りを正の向きにとるものとする．アレイマニフォールドベクトルの $m\quad (m=1,\dots,M)$ 番目の要素 $a_m$ は音源方向ベクトル $\boldsymbol{u}$ および$m$ 番目のマイクにおける位置ベクトル $\boldsymbol{p}_m$ を用いて次式で計算される．これを用いて， $d = 0.05$ [m]，$M = 3, \theta = 45 ^{\circ}$, $f = 1000$ [Hz] の場合の結果を print 文で確認せよ．
   $$
   \begin{align}
       a_m &= \exp \left( j \frac{2\pi f}{c} \boldsymbol{u} ^{\top} \boldsymbol{p}_{m} \right) \\
       \boldsymbol{u} &= \begin{bmatrix} \sin \theta & \cos \theta & 0 \end{bmatrix} ^{\top} \\
       \boldsymbol{p}_m &= \begin{bmatrix} \left( (m - 1) - \frac{M-1}{2} \right) d & 0 & 0 \end{bmatrix} ^{\top}
     \end{align}
   $$
2. **アレイマニフォールドベクトル（円状アレイ）**: 1.と同様に，アレイ半径 $r$ [m]，マイク数 $M$ ，音源方向 $\theta$，周波数 $f$ [Hz] を入力とし，2 次元平面における円状等間隔アレイのアレイマニフォールドベクトル $\boldsymbol{a}$ を計算する関数を実装せよ．これを用いて， $r = 0.05$ [m]，$M = 3, \theta = 45 ^{\circ}$, $f = 1000$ [Hz] の場合の結果を print 文で確認せよ．
   $$
   \begin{align}
       \boldsymbol{p}_m &= \begin{bmatrix} r \sin (\frac{2\pi}{M}(m-1)) & r \cos (\frac{2\pi}{M}(m-1)) & 0 \end{bmatrix} ^{\top}
     \end{align}
   $$
3. **アレイマニフォールドベクトル（一般）**: アレイの座標 $[x_1, y_1, 0], \dots, [x_M, y_M, 0]$ [m] ，音源方向 $\theta$，周波数 $f$ [Hz] を入力とし，2 次元平面における一般のマイクアレイのアレイマニフォールドベクトルを計算する関数を実装せよ．これを用いて，1.および 2.と同様の結果となるようなパラメータを与えて結果を print 文で確認せよ．
4. **空間相関行列の計算**: $M$ 個の $F\times T$ の複素数行列 $X_m[f, t]$ $(f = 0, \dots, F-1,\quad t = 0, \dots, T-1) \quad (m = 1,\dots, M)$ を入力とし，下記の手順で空間相関行列を計算する関数を実装せよ．出力は $F$ 個の $M\times M$ 複素数行列となることに注意すること．これを用いて， $X_1 = [[1, -1j, -1, 1j], [2, -2j, -2, 2j], [3, -3j, -3, 3j]]$, $X_2 = [[4, -2j, 1, 0], [2, -1j, 0, 0], [1, -j, 1, 0]]$ として結果を print 文で確認せよ．
   a. $\boldsymbol{x}_{ft} \coloneqq \begin{bmatrix} X_1[f, t] & \dots & X_M[f, t] \end{bmatrix} ^{\top}$
   b. $\boldsymbol{R}_{f} \gets \frac{1}{T} \sum _{t = 0} ^{T-1} \boldsymbol{x}_{ft} \boldsymbol{x}_{ft} ^{\mathsf{H}} \quad (f = 0, \dots, F-1)$ （$\boldsymbol{x}^\mathsf{H}$ は複素数ベクトル $\boldsymbol{x}$ の Hermite 転置を表す）
5. **空間相関行列の確認**: サンプリング周波数 16000 [Hz]，長さ 5 [s] のホワイトノイズを 2 チャネル作成し，窓幅 512・シフト幅 256・Hann 窓で STFT した信号に対して，4.で実装した関数を用いて空間相関行列を計算せよ．結果を $\boldsymbol{R}_{f} \quad (f = 0, \dots, 513)$ とするとき， $\boldsymbol{R}_{100}$ の実部を print 分で確認せよ．
6. **簡単な多チャネル観測シミュレーション**: サンプリング周波数 16000 [Hz]，長さ 1 [s] で振幅 1・周波数 440 [Hz]の正弦波 $s[n]$ と， $s[n]$ に対して SN 比 10dB になるよう振幅を調整したホワイトノイズ $\varepsilon[n]$ を作成せよ．さらに，$x_1[n] = s[n] + \varepsilon[n], x_2[n] = s[n-10] + \varepsilon[n], x_3[n] = s[n-20] + \varepsilon[n]$ として 3 チャネルの信号を作成し結果をプロットせよ．プロットの範囲は `[0, 0.01]` [s] など適当に拡大せよ．
7. **遅延和ビームフォーマ**: 次の手順で 6.の信号を強調した結果をプロットせよ．
   a. 6.の信号をチャネルごとに窓幅 1024・シフト幅 512・Hann 窓で STFT した結果を $X_1[f,t], X_2[f, t], X_3[f, t]$ とする．ただし， $F$ は周波数ビンの総数， $T$ はフレーム数である．
   a. $\boldsymbol{x}_{ft} \gets \begin{bmatrix} X_1[f, t] & X_2[f, t] & X_3[f, t]\end{bmatrix}^{\top}$
   b. 各周波数 $f = \frac{f_s / 2}{F-1} 0, \dots, \frac{f_s / 2}{F-1}$ ごとにビームフォーマ $\boldsymbol{w}_f = \frac{1}{3} \begin{bmatrix} \exp (-j 2\pi f \tau _1) & \exp (-j 2\pi f \tau _2) & \exp (-j 2\pi f \tau _3) & \end{bmatrix}$ を計算する．ただし， $\tau_1 = 0, \tau_2 = \frac{10}{f_s}, \tau_3 = \frac{20}{f_s}$ である．
   d. 各周波数ごとに $Y[f,t] = \boldsymbol{w}_{f}^{\mathsf{H}} \boldsymbol{x}_{ft}$ として強調信号を求める．
   d. $Y[f,t]$ を逆 STFT する．
8. **ビームパターン**: 周波数領域におけるビームフォーマのフィルタ $\boldsymbol{w}_f \quad (f = 0, \dots, F-1)$ ，マイクアレイの座標 $\boldsymbol{p}_m \quad (m = 1, \dots, M)$，サンプリング周波数 $f_s$ を入力とし，次の手順でビームパターンを描画する関数を実装せよ．これを用いて，1.の直線状アレイにおける遅延和ビームフォーマのビームパターンをプロットせよ．
   a. 角度 $\theta = 0, \dots, 360$ [deg] および周波数 $f = \frac{f_s / 2}{F-1} 0, \dots, \frac{f_s / 2}{F-1} F$ について 3.でアレイマニフォールドベクトル $\boldsymbol{a}_{f}(\theta)$ を計算する．
   b. 角度 $\theta = 0, \dots, 360$ [deg] について $\Psi (f, \theta) = \boldsymbol{w}_{f}^{\mathsf{H}} \boldsymbol{a}_{f} (\theta)$ を計算する．
   c. 横軸を角度，縦軸を周波数として $20 \log _{10} \lvert \Psi (f, \theta) \rvert$ をカラーバーでプロットする．
9. **空間サンプリング定理**: 空間的エイリアシングを避けるためにはマイク間隔 $d$ を $d \leq \frac{c}{2f}$ となるように選ぶ必要がある．ここで， $c$ [m/s] は音速，$f$ [Hz] は周波数である．8.で実装した関数を用いて，マイク間隔を 2 [cm], 5 [cm], 10 [cm] と変化させながら 1.で求めた直線状アレイのビームパターンをプロットし，結果を確認せよ．
10. **空間スペクトル**: $M$ チャネルの $N$ 点実数値信号 $z_{m}[n] \quad (m = 1, \dots, M)$ を入力とし，次の手順で空間スペクトルを計算する関数を実装せよ．これを用いて，マイク数 3，マイク間隔 0.05 m の直線状ビームフォーマおよび 6.で用いた信号を入力とし，周波数ビンインデクス $f=20, 21, \dots, 30$ ごとに結果を描画せよ．6.の信号は窓幅 1024・シフト幅 512・Hann 窓で STFT すること．
    a. 入力信号の STFT を $Z_m[f,t] \quad (f = 0, \dots, F-1,\; t = 0, \dots, T-1,\; m = 1,\dots, M)$ とする．
    b. 5.で実装した関数を用いて $Z_m[f,t]$ の空間相関行列を計算し $\boldsymbol{R}_{z}$ とする．
    c. 角度 $\theta = 0, \dots, 360$ [deg] についてビームフォーマ $\boldsymbol{w}(\theta)$ を計算する．
    d. 角度 $\theta = 0, \dots, 360$ [deg] について $P(\theta) = \boldsymbol{w} ^{\mathsf{H}} (\theta) \boldsymbol{R}_{z} \boldsymbol{w} (\theta)$ を計算する．
    e. 横軸を角度，縦軸を $20\log _{10} \lvert P(\theta) \rvert$ としてプロットする．

# 第 6 章 音源強調

- `datanet/datasets/SiSEC/UND/dev1/` から `dev1_female3_liverec_130ms_5cm_sim_{1,2}.wav` をダウンロードすること．
- 上記ファイルはインパルス応答が畳み込まれた 2 チャネルの信号になっている．マイク間隔は 5cm, 残響時間は 130ms．
- それぞれ音源 1, 2 と呼び，その和を観測信号と呼ぶ．
- 通常，音源 1, 2 の真値は得られないが，ここではアルゴリズムの実装と確認のため，真値が与えられたものとして良い．

1. 音源 1,2 を読み込み観測信号を作成せよ．各音源と観測信号を聴き比べ確認せよ．

2. 相対伝達関数の計算

   1. ある音源の多チャネル観測信号について，その音源の伝達関数は，観測信号の共分散行列の最大固有値に対応する固有ベクトルにより推定できる．音源 1 の伝達関数を求めよ．
   2. 伝達関数を $\boldsymbol{h}$，リファレンスマイク $r$ での伝達関数を $h_r$ とすると，相対伝達関数は $\boldsymbol{h} / h_r$ で与えられる．音源 1 の相対伝達関数を求めよ．
   3. 音源 1 の伝達関数と相対伝達関数をプロットし，比較せよ．

3. MVDR (minimum variance distortionless response) ビームフォーマ

   1. 音源 1 を目的音，音源 2 を雑音とする．相対伝達関数を用いて MVDR ビームフォーマを設計する関数を作成せよ．ビームフォーミングによる音源強調は以下で行われる．
      $$y_{ft} = \boldsymbol{w}_{f}^{\mathsf{H}} \boldsymbol{x}_{ft}$$
      ただし， $y_{ft}, \boldsymbol{w}_f, \boldsymbol{x}_{ft}$ はそれぞれ強調信号，空間フィルタ，観測信号の STFT 領域表現であり，$t, f$はフレームと周波数ビンのインデックスを表す．相対伝達関数を$\boldsymbol{a}_f$とし，MVDR ビームフォーマは以下で与えられる．
      $$\boldsymbol{w}_{f} = \cfrac{\boldsymbol{\Phi}_{\mathrm{n}, f}^{-1} \boldsymbol{a}_{f}}{\boldsymbol{a}^{\mathsf{H}}_{f} \boldsymbol{\Phi}_{\mathrm{n}, f}^{-1}\boldsymbol{a}_{f}}$$
      ここで， $\boldsymbol{\Phi}_{\mathrm{n}, f}$ は雑音の共分散行列であり，ここでは真値が与えられたものとする．
      すなわち，雑音（音源 2）の STFT 表現を $\boldsymbol{n}_{ft}$ とし
      $$\boldsymbol{\Phi}_{\mathrm{n}, f} = \frac{1}{T} \sum_{t=1}^{T} \boldsymbol{n}_{ft} \boldsymbol{n}_{ft}^{\mathsf{H}}$$
      である．
   2. MVDR ビームフォーマによる音源強調を行え．

4. MPDR (minimum power distortionless response) ビームフォーマ

   1. MPDR ビームフォーマを設計する関数を作成せよ． MPDR ビームフォーマでは，観測信号の共分散行列，すなわち
      $$\boldsymbol{\Phi}_{\mathrm{x}, f} = \frac{1}{T} \sum_{t=1}^{T} \boldsymbol{x}_{ft} \boldsymbol{x}_{ft}^{\mathsf{H}}$$
      を用いて空間フィルタを求める．空間フィルタの式は MVDR ビームフォーマと同一である．
   2. MPDR ビームフォーマによる音源強調を行え．

5. SN 比最大化ビームフォーマ

   1. SN 比最大化ビームフォーマを設計する関数を作成せよ．SN 比最大化ビームフォーマは以下の一般化固有値問題における最大固有値に対応する固有ベクトルとして与えられる．
      $$\boldsymbol{\Phi}_{\mathrm{s}, f}\boldsymbol{w}_f = \lambda_f \boldsymbol{\Phi}_{\mathrm{n}, f} \boldsymbol{w}_f$$
      ただし， $\boldsymbol{\Phi}_{\mathrm{s}, f}, \boldsymbol{\Phi}_{\mathrm{n}, f}$ はそれぞれ目的音と雑音の共分散行列を表す．
      ここでは真値が得られるものとして良い．
   2. SN 比最大化ビームフォーマにはゲインの任意性がある．後処理としてこれを補正せよ．補正フィルタを
      $$\boldsymbol{b}_f = \cfrac{\boldsymbol{\Phi}_{\mathrm{x}, f} \boldsymbol{w}_f}{\boldsymbol{w}_f^{\mathsf{H}} \boldsymbol{\Phi}_{\mathrm{x}, f} \boldsymbol{w}_f}$$
      とし，その任意（ここでは 1 番目とする）の要素を用いて
      $$\boldsymbol{w}_f \gets b_{1f} \boldsymbol{w}_f $$
      のように補正する．
   3. SN 比最大化ビームフォーマによる音源強調を行え．

6. スペクトルサブトラクション

   1. スペクトルサブトラクションを行う関数を作成せよ．
      $x_{ft}$を任意のチャネルでの観測信号，$n_{ft}$を雑音とする．
      強調信号$y_{ft}$の振幅を
      $$|y_{ft}| = \sqrt{\max(|x_{ft}|^{p} - \alpha|n_{ft}|^{p}, \ 0)}$$
      で推定する．
      強調信号は観測信号の位相を用いて
      $$y_{ft} \gets |y_{ft}| \frac{x_{ft}}{|x_{ft}|}$$
      で推定する．
   2. 音源 1 を目的音，音源 2 を雑音とする．$\alpha = 1, p = 2$ としてスペクトルサブトラクションによる音源強調を行え．ただし，チャネル 1 での観測信号に対して強調処理を適用することとする．

7. 理想バイナリマスク (ideal binary mask; IBM)

   1. 理想バイナリマスクを設計する関数を作成せよ．時間周波数マスキングによる音源強調は以下で行われる．
      $$y_{ft} = m_{ft} x_{ft}$$
      ただし， $m_{ft}, x_{ft}$ はそれぞれ時間周波数マスクと任意のチャネルの観測信号である．
      理想バイナリマスクは，目的音を $s_{ft}$ ，雑音を $n_{ft}$ とし，以下で設計される．
      $$m_{tf} = \begin{cases} 1 \quad (|s_{tf}| \geq |n_{tf}|) \\ 0 \quad (\text{otherwise}) \end{cases}$$
   2. 理想バイナリマスクによる音源強調を行え．ただし，チャネル 1 での観測信号に対して強調処理を適用することとする．

8. 理想ソフトマスク (ideal ratio mask; IRM)

   1. 理想ソフトマスクを設計する関数を作成せよ．理想ソフトマスクは以下で設計される．
      $$m_{tf} = \cfrac{|s_{tf}|^{\alpha}}{|s_{tf}|^{\alpha} + |n_{tf}|^{\alpha}}$$
   2. $\alpha = 1$とし，理想ソフトマスクによる音源強調を行え．ただし，チャネル 1 での観測信号に対して強調処理を適用することとする．
   3. $\alpha = 2$ として音源強調を行い，$\alpha = 1$および理想バイナリマスクの結果と比較せよ．

9. マルチチャネル Wiener フィルタ

   1. マルチチャネル Wiener フィルタを設計する関数実装せよ．マルチチャネル Wiener フィルタでは
      $$\boldsymbol{y}_{ft} = \boldsymbol{W}^{\mathsf{H}}_f \boldsymbol{x}_{ft}$$
      で音源強調を行う．ここで $\boldsymbol{y}_{ft} = [y_{1ft}, \ y_{2ft}]^{\top}$ であり，それぞれ各マイクでの強調信号である．
      フィルタは目的音と雑音の共分散行列を用いて
      $$\boldsymbol{W}_f = (\boldsymbol{\Phi}_{\mathrm{s}, f} + \mu\boldsymbol{\Phi}_{\mathrm{n}, f})^{-1}\boldsymbol{\Phi}_{\mathrm{s}, f}$$
      で設計される．
   2. $\mu = 1$ として，マルチチャネル Wiener フィルタによる音源強調を行え．
   3. $\mu = 0, \mu = 100$ などとしたときに想定される強調結果はどのようなものか考察せよ．それぞれのパラメータで音源強調を行い，結果を確認せよ．
   4. 8. との違いを考察せよ．

10. 各手法の比較と考察

    1. 3., 4., 5. の強調結果や指向特性をプロットし比較せよ．
    2. 6., 7., 8. の強調結果や時間周波数マスクをプロットし比較せよ．
    3. 3.-9. の強調結果を比較し，それぞれの手法の特徴を考察せよ．

11. (発展) 劣決定問題
    1. `/datanet/datasets/SiSEC/UND/dev1/` から `dev1_female3_liverec_130ms_5cm_sim_3.wav` をダウンロードせよ．これを音源 3 とする．
    2. 音源 2 を目的音，音源 1,3 を雑音とし，1.--9. の課題を実行せよ．ただし，1.--9.中の式は 2 音源を前提としているため，一般化が必要なことに注意すること．
    3. 各手法について，雑音が 1 つの場合と 2 つの場合の強調結果はどのように異なるか，結果を確認しながら考察せよ．
    4. 雑音が 2 つの場合について，10. と同様に，各手法を比較し考察せよ．

# 第 x 章: 音源方向推定

準備中

# 第 x 章: ブラインド音源分離

準備中

# 第 x 章: 残響除去

準備中

# 第 x 章: シミュレーション実験

準備中

# 参考文献

## 書籍

- [浅野: 音のアレイ信号処理, コロナ社, 2011.](https://www.coronasha.co.jp/np/isbn/9784339011166/)
  - アレイ信号処理の基礎からビームフォーミング，ブラインド音源分離にいたるまで詳しく書かれています．
- [貴家: ディジタル信号処理のエッセンス, オーム社, 2014.](https://www.ohmsha.co.jp/book/9784274216060/)
  - 標準的なディジタル信号処理の教科書です．フーリエ級数展開，フーリエ変換，離散時間フーリエ変換，離散フーリエ変換の関係が非常に明確に記述されています．例題が豊富でわかりやすいです．
- [戸上: Python で学ぶ音源分離, インプレス, 2020.](https://book.impress.co.jp/books/1119101154)
  - 音源分離をメインに扱うおそらく日本初の書籍です．Majorization-minimization 法による最適化，残響除去，独立低ランク行列分析など日本語の書籍ではこの本でしか見られない題材が豊富に含まれています．Python 実装も公開されていて，projection back など実装上気をつけなければいけない点も詳しく記述されています．[pyroomacoustics](https://github.com/LCAV/pyroomacoustics)を使ったシミュレーションも少し書かれています．
- [阿部, 八巻, 川又: Python 対応 ディジタル信号処理, 森北出版, 2021.](https://www.morikita.co.jp/books/mid/077661)
  - 例題が非常に豊富で python 実装も読みやすいです．Python はわかるがディジタル信号処理については勉強したことがないという人が最初に読むにはかなり良い本だと思います．フィルタ設計について 4 章にわたって極めて詳しく解説されています．音の信号処理に関してはあまり詳しくないので下記の書籍などが参考になります．フィルタ設計，畳み込みなどの問題の参考にしました．
- [川村: 音声音響信号処理の基礎と実践, コロナ社, 2021.](https://www.coronasha.co.jp/np/isbn/9784339014020/)
  - 音に関する信号処理について平易に解説されています．バイナリマスキング，画像の音変換など他の書籍ではあまり解説されていないものも詳しく書かれています．理論がメインという印象で実装に関しては同じ著者の[プログラム 101 付き 音声信号処理](https://shop.cqpub.co.jp/detail/2539/)が詳しいです．
- [森勢: ひたすら楽して音響信号解析, コロナ社, 2021.](https://www.coronasha.co.jp/np/isbn/9784339009392/)
  - タイトルの通り MATLAB を使ってとにかく楽に音響信号解析をするための本です．フーリエ変換，フィルタ設計の参考にしました．
- [山本, 高道: Python で学ぶ音声合成, インプレス, 2021.](https://book.impress.co.jp/books/1120101073)
  - 前述の Python で学ぶ音源分離と同じシリーズの書籍です．本書籍のために作成されたライブラリである[ttslearn](https://github.com/r9y9/ttslearn)が非常にわかりやすく python ライブラリ設計の参考になります．

## 解説記事

- [小野: 短時間フーリエ変換の基礎と応用, 日本音響学会誌, 2016.](https://doi.org/10.20697/jasj.72.12_764)
  - 短時間フーリエ変換が詳しく解説されています．
- [東京農工大学 矢田部 浩平 准教授](https://twitter.com/yatabe_)の解説記事
  6 回にわたる連載で短時間フーリエ変換が非常に詳しく解説されています．
  1. [第一回：連続信号と離散信号](https://doi.org/10.20697/jasj.77.4_262)
  1. [第二回：離散フーリエ変換](https://doi.org/10.20697/jasj.77.5_331)
  1. [第三回：短時間フーリエ変換](https://doi.org/10.20697/jasj.77.6_396)
  1. [第四回：信号の再構成と窓関数](https://doi.org/10.20697/jasj.77.7_463)
  1. [第五回：実装における諸注意](https://doi.org/10.20697/jasj.77.8_537)
  1. [第六回：時間周波数領域のスパース表現](https://doi.org/10.20697/jasj.77.9_609)

## Web サイト

- [香川高専 北村 大地 講師 ホームページ](http://d-kitamura.net/codes.html)
  - MATLAB ですが短時間フーリエ変換や様々なブラインド音源分離アルゴリズムの実装が公開されています．
- [やる夫で学ぶディジタル信号処理](http://www.ic.is.tohoku.ac.jp/~swk/lecture/yaruodsp/main.html)
  - 日本語で無料で公開されているディジタル信号処理に関する資料の中で最も網羅的かつわかりやすいです．
- [言語処理 100 本ノックを解き始める前に.md](https://gist.github.com/reiyw/9155edf600e85417e82d2e4e4bc9e637)
  - Linux コマンドや python の参考になるリンクがまとまっています．
