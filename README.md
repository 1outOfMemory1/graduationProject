# graduationProject
毕业设计 基于深度神经网络的语音识别
```bash 
文件夹目录如下所示
────src
    ├───asrt1.2  # 开源训练文件夹 训练模型
    │   ├───assets
    │   ├───model_language
    │   ├───speech_features
    │   └───utils   
    ├───drawPic   # 用于论文画图
    ├───flaskWeb  # 后端flask服务器 加载模型 提供文件上传 语音识别后端接口
    │   ├───draw_pic
    │   ├───model
    │   ├───model_language
    │   └───templates      
    ├───learn  # 学习文件夹 包括tensorflow kaldi rnn循环神经网络 和测试文件夹
    │   ├───kaldi
    │   ├───rnnLearn
    │   ├───tensorflowLearn
    │   └───test
    └───vueFont # 前端文件夹 使用vue3 + vite ，ui框架采用 Vue vben admin ，提供音频录制 语音识别等前端功能
```

```shell
1. 对于asrt1.2 文件夹 训练语音识别模型请参考https://wiki.ailemon.net/docs/asrt-doc/asrt-doc-1demhoid4inc6
2. 对于drawPic learn文件夹 使用python编码 安装响应的包直接执行就行
3. 对于flaskweb文件夹，将训练好的权重文件放入save_models子文件 重命名为SpeechModel24.model.h5 然后python backend.py 启动flask服务器
4. 对于vueFont文件夹 前端服务 执行 pnpm install 安装依赖后， 本地执行 npm run dev 启动前端服务器 
```