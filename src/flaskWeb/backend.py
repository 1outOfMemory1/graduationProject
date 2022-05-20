from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from datetime import datetime
from scipy.io import wavfile

import librosa
import matplotlib.pyplot as plt
import os

from model.speech_model import ModelSpeech
from model.speech_model_zoo import SpeechModel251BN
from model.speech_features import Spectrogram
from model.LanguageModel2 import ModelLanguage



app = Flask(__name__,static_folder="./static")
pwd = os.path.dirname(__file__)
# 定义文件的保存路径和文件名尾缀
upload_dir = "static/save_file"
UPLOAD_FOLDER = os.path.join(pwd, upload_dir)
ALLOWED_EXTENSIONS = {'wav'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
HOST = "localhost"
PORT = 5000

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
ml = ModelLanguage('model_language')
ml.LoadModel()





def commonSuccessResponse(res, message):
    return {"code": 0, "result": res, "message": message}

def commonErrorResponse(message):
    return {"code": 1, "result": None, "message": message}



def allowed_file(filename):
    """
    检验文件名尾缀是否满足格式要求
    :param filename:
    :return:
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """
    上传文件到save_file文件夹
    以requests上传举例
    wiht open('路径','rb') as file_obj:
        rsp = requests.post('http://localhost:5000/upload,files={'file':file_obj})
        print(rsp.text) --> file uploaded successfully
    """
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        now = datetime.now()
        time_str = now.strftime("%Y-%m-%d,%H-%M-%S")
        filename = time_str + "-" + filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'file uploaded successfully'
    return "file uploaded Fail"


@app.route("/get_wav_file_list")
def list_wav_file():
    file = os.listdir(upload_dir)
    file_list = []
    for f in file:
        file_list.append(f)
    return commonSuccessResponse(file_list, "成功获取已上传的wav文件列表")

@app.route("/get_sound_wave_list")
def get_sound_wave_pic_url():
    file_name =  request.args.get('wavFileName')
    file_path = upload_dir + "/" + file_name
    if os.path.exists(file_path):
        samplerate, signal = wavfile.read(file_path)
        return commonSuccessResponse(signal.tolist(),"获取{}录音文件解析数据成功".format(file_name) )
    else:
        return commonErrorResponse("{}文件不存在".format(file_name))

@app.route("/get_specgram_pic_url")
def get_specgram_pic():
    file_name = request.args.get('wavFileName')
    file_path = upload_dir + "/" + file_name
    if os.path.exists(file_path):
        signalData, samplingFrequency = librosa.load(file_path, sr=None, mono=False)
        plt.specgram(signalData,Fs=samplingFrequency)
        now = datetime.now()
        time_str = now.strftime("%Y-%m-%d,%H-%M-%S")
        plt.savefig("static/pic/{}.png".format(time_str))
        return commonSuccessResponse("http://{}:{}/static/pic/{}.png".format(HOST,PORT,time_str), "获取{}录音文件语谱图成功".format(file_name))
    else:
        return commonErrorResponse("{}文件不存在".format(file_name))





@app.route("/soundToPinyin")
def soundToPinyin():
    file_name = request.args.get('wavFileName')
    file_path = upload_dir + "/" + file_name
    if os.path.exists(file_path):
        res = ms.recognize_speech_from_file(file_path)
    # print('*[提示] 声学模型语音识别结果：\n', res)
        return commonSuccessResponse(res,"wav文件转为拼音成功")
    else:
        return commonErrorResponse("文件不存在，请检查文件路径")

@app.route("/pinyinToText")
def pinyinToText():
    str_pinyin = request.args.get('pinyin')
    str_pinyin_list = str_pinyin.split(",")
    res = ml.SpeechToText(str_pinyin_list)
    # print('*[提示] 声学模型语音识别结果：\n', res)
    return commonSuccessResponse(res,"拼音转换为文本成功")



if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
