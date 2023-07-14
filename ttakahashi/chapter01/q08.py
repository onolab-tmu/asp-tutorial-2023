from pathlib import Path
from typing import Union
import soundfile as sf

from q06 import calc_snr
from q07 import adjust_snr


def main(input_dir_02: Union[Path, str], input_dir_04: Union[Path, str], output_dir: Union[Path, str]):
    in_p_02 = Path(input_dir_02)
    in_p_04 = Path(input_dir_04)
    out_p = Path(output_dir)

    snr = 6

    y_02, sr = sf.read(in_p_02 / "02.wav")
    y_04, sr = sf.read(in_p_04 / "04.wav")
    mixture = adjust_snr(y_02, y_04, snr)

    print(f"SNR: {calc_snr(mixture, y_04)} (dB)")

    sf.write(out_p / "08.wav", mixture, sr, format="WAV", subtype="PCM_16")


if __name__ == "__main__":
    in_p_02 = Path.cwd() / "outputs"
    in_p_04 = Path.cwd() / "outputs"
    out_p = Path.cwd() / "outputs"
    if not out_p.exists():
        out_p.mkdir(parents=True)

    main(in_p_02, in_p_04, out_p)

    print("Finished")
