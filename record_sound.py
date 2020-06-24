import sounddevice
from scipy.io.wavfile import write


def make_new_sound():
    channels = 2
    fs = 44100
    second = 5
    print("Recording...")
    record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=channels)
    sounddevice.wait()
    filename = input("Please enter a name for your file: ")
    write(str(filename) + ".wav", fs, record_voice)


make_new_sound()