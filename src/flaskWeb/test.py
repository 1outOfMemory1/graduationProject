


# 遍历某个文件夹下的所有文件
# import os
# from os import path
#
# file = os.listdir("./save_file")
# for f in file:
#     # 字符串拼接
#     real_url = path.join("", f)
#     # 打印出来
#     print(real_url.split("\n"))


# 按照格式打印当前时间
# from datetime import datetime
# now = datetime.now()
# s2 = now.strftime("%Y/%m/%d,%H:%M:%S")
# # dd/mm/YY H:M:S format
# print("s2:", s2)


import librosa
import matplotlib.pyplot as plt

signalData, samplingFrequency = librosa.load("save_file/2022-05-20,04-02-29-nihao.wav", sr=None, mono=False)
plt.specgram(signalData,Fs=samplingFrequency)
plt.savefig("./abc.png")