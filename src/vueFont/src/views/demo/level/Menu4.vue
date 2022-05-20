<template>
  <div class="p-5">
    <div>
      <PageWrapper title="语音转文字">
        <a-select
          placeholder="选择想要分析的已经保存的录音"
          ref="select"
          :value="selected_wav_file"
          style="width: 250px"
          :options="wav_list_options"
          @focus="focus"
          @change="handleChange"
        >
        </a-select>
        <span style="display: inline-block;width: 10px;height: 10px"> </span>
        <a-button type="primary" @click="generateBtnClick">生成</a-button>
        <audio style="display: inline-block" :src="audioSrc" controls></audio>

      </PageWrapper>

    </div>
    <div style="width: 100%;height: 1000px;display: flex">
      <div style="margin-left: 40px;flex: 4;width: 50%;height: 100%;">
        <h1 style="font-size: 30px;font-weight: bold; text-align: center">语音转拼音</h1>
        <a-textarea   v-model:value="pinyinValue" placeholder="此处是经过DCNN和CTC网络得到的拼音序列" :rows="4" />
        <a-button type="primary" style="float: right;margin-top: 10px" @click="pinyinToTextBtnClick">拼音转文字</a-button>
      </div>
      <div style="flex: 1"></div>
      <div style="margin-right: 40px;flex: 4; width: 50%;height: 100%;">
        <h1 style="font-size: 30px;font-weight: bold; text-align: center">拼音转文字</h1>
        <a-textarea  v-model:value="textValue" placeholder="经过马尔科夫链的拼音推断出文本序列" :rows="4" />
      </div>
    </div>

  </div>
</template>
<script lang="ts">

import { defineComponent } from "vue";
import { Input } from "ant-design-vue";
import { getWavFileListApi,soundToPinyin,pinyinToText } from "/@/api/sys/wav_process";
import { PageWrapper } from "/@/components/Page";

export default defineComponent({
  name: "Menu3Demo",
  components: { Input, PageWrapper },
  mounted() {


  },

  updated() {

  },
  data() {
    return {
      audioSrc :"",
      pinyinValue: undefined,
      textValue : undefined,
      selected_wav_file: undefined,
      wav_list_options: []
    };
  },
  methods: {
    focus() {
      this.wav_list_options = [];
      getWavFileListApi().then((res) => {
        res.forEach((ele) => {
          this.wav_list_options.push({ value: ele, label: ele });
        });
      }, error => {
        console.log(error);
      });
    },
    handleChange(value: string) {
      this.audioSrc = "http://localhost:5000/static/save_file/" + value
      this.selected_wav_file = value;
    },
    generateBtnClick(){
      const soundParams = {wavFileName: this.selected_wav_file}
      soundToPinyin(soundParams).then((res)=>{
        this.pinyinValue = res
        const pinyinParams = {pinyin: res.toString()}
        pinyinToText(pinyinParams).then((res)=>{
          this.textValue = res
        })
      })

    },
    pinyinToTextBtnClick(){
      const pinyinParams = {pinyin: this.pinyinValue}
      pinyinToText(pinyinParams).then((res)=>{
        this.textValue = res
      })
    }
  }

});
</script>
