# import the pyplot and wavfile modules
import librosa
import matplotlib.pyplot as plot

from scipy.io import wavfile

# Read the wav file (mono)

signalData  ,samplingFrequency= librosa.load('F:/test/recordAudio/nihao.wav', sr=None, mono=False)
print(samplingFrequency)
# Plot the signal read from wav file

plot.subplot(211)

plot.title('Spectrogram of a wav file with piano music')
signalData = signalData * 1.0 / max(signalData)
plot.plot(signalData)

plot.xlabel('Sample')

plot.ylabel('Amplitude')

plot.subplot(212)

plot.specgram(signalData, Fs=samplingFrequency)

plot.xlabel('Time')

plot.ylabel('Frequency')

plot.show()