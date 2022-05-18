import librosa
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

path = "F:/test/recordAudio/nihao.wav"
plt.figure(figsize=(15, 4.5))

# sr=None声音保持原采样频率， mono=False声音保持原通道数
data, fs = librosa.load(path, sr=16000, mono=False)

L = len(data)
print('Time:', L / fs)

# 归一化
data = data * 1.0 / max(data)

# 0.025s
framelength = 0.025
# NFFT点数=0.025*fs
framesize = int(framelength * fs)
print("NFFT:", framesize)

# 画语谱图
plt.specgram(data, NFFT=framesize, Fs=fs, window=np.hanning(M=framesize), scale_by_freq=True, sides='default')
plt.colorbar(format='%+2.0f ')
plt.ylabel('频率(Hz)')
plt.xlabel('时间(s)')
plt.title('语谱图')
plt.show()
