from flask import Flask,render_template
# 创建应用实例
app = Flask(__name__)
# 视图函数（路由）
@app.route("/")
def hello_world():
    return render_template("test.html")
# 启动服务
if __name__ == '__main__':
   app.run(debug = True)