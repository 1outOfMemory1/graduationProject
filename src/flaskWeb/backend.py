import os
from os import path
from string import Template
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from datetime import datetime
from scipy.io import wavfile
app = Flask(__name__,static_folder="./static")
pwd = os.path.dirname(__file__)
import librosa
import matplotlib.pyplot as plt

# 定义文件的保存路径和文件名尾缀
upload_dir = "save_file"

UPLOAD_FOLDER = os.path.join(pwd, upload_dir)
ALLOWED_EXTENSIONS = {'wav'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

HOST = "localhost"
PORT = 5000


def commonSuccessResponse(res, message):
    return {"code": 0, "result": res, "message": message}

def commonErrorResponse(message):
    return {"code": 1, "result": None, "message": message}



@app.route('/index')
def index():
    """
    返回一个网页端提交的页面
    :return:
    """
    html = Template("""
    <!DOCTYPE html>
    <html>
       <body>

          <form action = "http://$HOST:$PORT/upload" method = "POST"
             enctype = "multipart/form-data">
             <input type = "file" name = "file" />
             <input type = "submit"/>
          </form>

       </body>
    </html>
    """)
    html = html.substitute({"HOST": HOST, "PORT": PORT})
    return html


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
        plt.savefig("static/{}.png".format(time_str))
        return commonSuccessResponse("http://{}:{}/static/{}.png".format(HOST,PORT,time_str), "获取{}录音文件语谱图成功".format(file_name))
    else:
        return commonErrorResponse("{}文件不存在".format(file_name))


@app.route("/download")
def download_file():
    file_name = request.args.get('fileId')
    file_path = os.path.join(pwd, 'src_file', file_name)
    if os.path.isfile(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "The downloaded file does not exist"

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
