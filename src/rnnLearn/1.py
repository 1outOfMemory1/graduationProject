import torch
import torchaudio
import torchaudio.functional as AF
import math
import logging
# pip install SoundFile
import matplotlib.pyplot as plt

wav_file = 'F:/test/recordAudio/a1.wav'
signal, samplerate = torchaudio.load(wav_file)
signal = signal[0]


def wav_show(t, sr=None):
    print("Shape of waveform: {}".format(t.size()))
    if sr: print("Sample rate of waveform: {}".format(sr))
    plt.figure(figsize=(15, 4.5))
    plt.plot(t.numpy())
    plt.show()


def frame_show(t):
    print("Shape of spectrogram: {}".format(t.size()))
    plt.figure(figsize=(15, 4.5))
    plt.imshow(t.abs().numpy(), cmap='gray')
    plt.colorbar()
    plt.show()


wav_show(signal, samplerate)
