


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


# import librosa
# import matplotlib.pyplot as plt
#
# signalData, samplingFrequency = librosa.load("static/save_file/2022-05-20,04-02-29-nihao.wav", sr=None, mono=False)
# plt.specgram(signalData,Fs=samplingFrequency)
# plt.savefig("./abc.png")


import os

from model.speech_model import ModelSpeech
from model.speech_model_zoo import SpeechModel251BN
from model.speech_features import Spectrogram
from model.LanguageModel2 import ModelLanguage

os.environ["CUDA_VISIBLE_DEVICES"] = "1"

AUDIO_LENGTH = 1600
AUDIO_FEATURE_LENGTH = 200
CHANNELS = 1
# 默认输出的拼音的表示大小是1428，即1427个拼音+1个空白块
OUTPUT_SIZE = 1428
sm251bn = SpeechModel251BN(
    input_shape=(AUDIO_LENGTH, AUDIO_FEATURE_LENGTH, CHANNELS),
    output_size=OUTPUT_SIZE
    )
feat = Spectrogram()
ms = ModelSpeech(sm251bn, feat, max_label_length=64)

ms.load_model('save_models/' + sm251bn.get_model_name() + '.model.h5')
res = ms.recognize_speech_from_file('output.wav')
print('*[提示] 声学模型语音识别结果：\n', res)

ml = ModelLanguage('model_language')
ml.LoadModel()
str_pinyin = res
res = ml.SpeechToText(str_pinyin)
print('语音识别最终结果：\n',res)
