import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import torchaudio

plt.rcParams['font.sans-serif'] = 'SimHei'  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

wav_file = 'F:/test/recordAudio/nihao.wav'

signal, sampleRate = torchaudio.load(wav_file)
signal = signal[0]


plt.plot(signal)


x = np.linspace(0, 1, 20000)
y = np.sin(2000 *np.pi * x) + 2* np.sin(4000*np.pi* x)

# 离散频率
xf = np.arange(len(y))

# 由于对称性，因此只取一半区域
xf_half = xf[range(int(len(x)/2))]

# 执行完fft以后，对各频率的能量进行归一化处理
yf = abs(fft(y))/len(x)

# 由于对称性，因此只取一半区间
yf_half = yf[range(int(len(x)/2))]

# plt.plot(xf_half, yf_half)

plt.show()