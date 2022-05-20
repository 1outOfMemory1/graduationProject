<template>
  <div class="ant-row">
    <div  class="ant-col-11">
      <PageWrapper   title="音频文件上传" >
        <a-alert message="请上传一个wav文件" />
        <BasicUpload
          :maxSize="20"
          :maxNumber="10"
          @change="handleChange"
          :api="uploadApi"
          class="my-5"
          :accept="['.wav']"
        />
      </PageWrapper>
    </div>
    <div class="ant-col-1"></div>
    <div class="ant-col-12">
      <PageWrapper   title="音频录制" >
        <a-alert message="请点击录制按钮" />
        <a-button  type="primary"  @click="beginRecordAudio" class="record-start-btn btn">开始录音</a-button>
        <span style="display: inline-block; width: 10px; height: 10px"></span>
        <a-button danger  @click="endRecordAudio" class="record-finish-btn btn">结束录音</a-button>
        <span style="display: inline-block; width: 10px; height: 10px"></span>
        <a-button  @click="submitAudio" type="primary" :size="size">
          提交录音
        </a-button>
        <audio controls :src="recordSrc"  style="display: inline-block"></audio>
      </PageWrapper>
    </div>
    <img style="margin-top: -30px;width: 1800px;height: 800px" src="public/resource/img/语音识别流程.png">
  </div>

</template>
<script lang="ts">

import { defineComponent } from 'vue';
import { BasicUpload } from '/@/components/Upload';
import { useMessage } from '/@/hooks/web/useMessage';
import { BasicForm, FormSchema, useForm } from '/@/components/Form/index';
import { PageWrapper } from '/@/components/Page';
import { Alert } from 'ant-design-vue';
import { uploadApi, uploadSimpleApi } from "/@/api/sys/upload";
import Recorder from 'js-audio-recorder'

const schemas: FormSchema[] = [
  {
    field: 'field1',
    component: 'Upload',
    label: '字段1',
    colProps: {
      span: 8,
    },
    rules: [{ required: true, message: '请选择上传文件' }],
    componentProps: {
      api: uploadApi,
    },
  },
];
export default defineComponent({
  components: { BasicUpload, BasicForm, PageWrapper, [Alert.name]: Alert },
  data(){
    return{
      isRecording : false,
      recordSrc :"",
      recorder : new Recorder(
        {
          sampleBits: 16,                 // 采样位数，支持 8 或 16，默认是16
          sampleRate: 16000,              // 采样率，支持 11025、16000、22050、24000、44100、48000，根据浏览器默认值，我的chrome是48000
          numChannels: 1,                 // 声道，支持 1 或 2， 默认是1
          // compiling: false,(0.x版本中生效,1.x增加中)  // 是否边录边转换，默认是false
        }
      ),
      myAudioBlob : null
    }
  },
  mounted(){

  },
  methods:{
    beginRecordAudio() {
      this.$notification.success({
        message: '正在录音中',
        description:
          '可点击停止录音或者保存录音按钮停止录音',
      })
      this.recorder.start()
    },
    endRecordAudio() {
      this.recorder.stop()
      this.myAudioBlob = this.recorder.getWAVBlob()
      let url = window.URL.createObjectURL(this.myAudioBlob);
      this.recordSrc = url
      this.$notification.success({
        message: '录音结束',
        description:
          '录音结束，可使用下方播放条播放录音试听',
      })
    },
    submitAudio(){
      this.endRecordAudio()
      let formData = new FormData()
      let current_time = new Date().getTime();
      let file = new File([this.recorder.getWAV()],current_time+".wav")
      formData.append("file", file); // 文件对象
      uploadSimpleApi(formData).then((res)=>{
          // console.log(res)
        this.$notification.success({
          message: '上传服务成功',
          description:
            '已经上传服务器成功，可以查看波形图，语谱图和进行语音识别',
        })
      })

    }
  },
  setup() {
    const { createMessage } = useMessage();
    const [register] = useForm({
      labelWidth: 120,
      schemas,
      actionColOptions: {
        span: 16,
      },
    });
    return {
      handleChange: (list: string[]) => {
        createMessage.info(`已上传文件${JSON.stringify(list)}`);
      },
      uploadApi,
      register,
    };
  },
});
</script>
