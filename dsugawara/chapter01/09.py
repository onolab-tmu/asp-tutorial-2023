import soundfile as sf

if __name__ == "__main__":
    x, fs = sf.read("08.wav")
    fs = 8000
    sf.write(file="09.wav", data=x, samplerate=fs)
