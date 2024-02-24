import numpy as np
import sounddevice as sd
import math
from scipy.io.wavfile import write

def playArray(pts, time):
    samplerate = 44100.0
    sd.default.samplerate = samplerate
    volume = 10000
    total = len(pts)
    count = 0
    phase = 0.0
    print(1)
    samples = np.arange(samplerate * time ) / samplerate
    print(10)
    for i, val in enumerate(samples):
        freq = pts[count]
        freqRads = 2 * np.pi * freq / samplerate
        phase = phase + freqRads
        sampleValue = volume * np.sin(phase)
        samples[i] = sampleValue
        if ( i >  0 and i % (samplerate * time) == 0):
            count = count + 1

    wav_wave = np.array(samples, dtype=np.int16)
    sd.play(wav_wave, blocking=True)

    rate = 44100

    write('./output/test.wav', rate, wav_wave)
    print('oi')

pts = np.arange(121321, 1500, 10)
playArray(pts, 0.9)
