<template>
  <div class="p-5">
    <PageWrapper   title="生成语谱图" >

    </PageWrapper>

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
    <img style="width: 100%;height: 800px" :src="imgPath"  >
  </div>
</template>
<script lang="ts">
import { defineComponent, ref } from "vue";
  import { Input } from 'ant-design-vue';
import { getSpecgramPicUrlApi, getWavFileListApi } from "/@/api/sys/wav_process";
import { PageWrapper } from '/@/components/Page';
import ImagePreview from "/@/components/Preview/src/Preview.vue";
  export default defineComponent({
    name: 'Menu4Demo',
    components: { ImagePreview, Input,PageWrapper },
    data() {
      return {
        imgPath : "public/resource/img/语音识别流程.png",
        selected_wav_file: undefined,
        wav_list_options: []
      };
    },
    methods: {
      generateBtnClick(){
        let params = { "wavFileName": this.selected_wav_file };
        getSpecgramPicUrlApi(params).then((res)=>{
          this.imgPath = res
        })
      },
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
        this.selected_wav_file = value
      },
    }
  });
</script>
