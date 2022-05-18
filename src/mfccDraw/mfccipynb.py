import torch
import torchaudio
import torchaudio.functional as AF
import math
import logging

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# wav_file = 'F:/test/recordAudio/nihao.wav'
wav_file = 'G:/资料备份/视频下载/123.wav'
# wav_file = 'F:/test/ASRT_v1.2.0/output.wav'
signal, samplerate = torchaudio.load(wav_file)
signal = signal[0]


def wav_show(signal, sr=None):
    if sr:
        print("音频采样率为: {}次/秒".format(sr))
    print("波形采样次数为: {},持续时间为{:.3f}s".format(len(signal), len(signal) / sr))
    plt.figure(figsize=(15, 4.5))
    plt.xlabel("时间/秒(s)")
    # plt.ylabel('yyyyyyyyyyy')
    time = [float(x / sr) for x in range(0, len(signal))]
    plt.plot(time, signal)
    plt.title('波形图,音频采样率为: {}次/秒，波形采样次数为: {}次,持续时间为{:.3f}秒'.format(sr, len(signal), len(signal) / sr))
    plt.show()


def frame_show(t):
    print("Shape of spectrogram: {}".format(t.size()))
    plt.figure(figsize=(15, 4.5))
    plt.imshow(t.abs().numpy(), cmap='gray')
    plt.colorbar()
    plt.show()


wav_show(signal, samplerate)
