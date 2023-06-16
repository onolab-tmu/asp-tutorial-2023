from pathlib import Path
from typing import Optional, Union
import numpy as np
import soundfile as sf


def calc_snr(s, x):
    return 10 * np.log10(np.sum(s**2) / np.sum(x**2))


def adjust_snr(s, x, snr):
    return (x / np.sqrt(np.sum(x**2))) * np.sqrt(np.sum(s**2)) * 10 ** (-snr / 20)


def main(input_dir_02: Union[Path, str], input_dir_04: Union[Path, str]):
    in_p_02 = Path(input_dir_02)
    in_p_04 = Path(input_dir_04)

    snr = 0

    y_02, sr = sf.read(in_p_02 / "02.wav")
    y_04, sr = sf.read(in_p_04 / "04.wav")
    mixture = adjust_snr(y_02, y_04, snr)

    print(f"SNR: {calc_snr(mixture, y_04)} (dB)")


if __name__ == "__main__":
    in_p_02 = Path.cwd() / "02/outputs"
    in_p_04 = Path.cwd() / "04/outputs"

    main(in_p_02, in_p_04)

    print("Finished")
