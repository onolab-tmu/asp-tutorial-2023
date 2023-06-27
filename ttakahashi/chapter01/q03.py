from pathlib import Path
from typing import Union
import numpy as np
import soundfile as sf


def main(input_dir: Union[Path, str], output_dir: Union[Path, str]):
    in_p = Path(input_dir)
    out_p = Path(output_dir)

    A = 1  # amplitude
    f = 660  # frequency (Hz)
    sec = 3  # time (sec)
    sr = 16000  # sampling rate (Hz)

    t = np.arange(sec * sr) / sr
    y1 = A * np.sin(2 * np.pi * f * t)
    y2, sr = sf.read(in_p / "02.wav")
    y = np.stack((y1, y2), axis=1)

    sf.write(out_p / "03.wav", y, sr, format="WAV", subtype="PCM_16")

    print(sf.info(out_p / "03.wav"))


if __name__ == "__main__":
    in_p = Path.cwd() / "outputs"
    out_p = Path.cwd() / "outputs"
    if not out_p.exists():
        out_p.mkdir(parents=True)

    main(in_p, out_p)

    print("Finished")
