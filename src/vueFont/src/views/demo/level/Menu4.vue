<template>
  <div class="p-5">
    <PageWrapper  title="语音转文字">
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
      <a-button type="primary">生成</a-button>

    </PageWrapper>

  </div>
</template>
<script lang="ts">

import { defineComponent, ref } from "vue";
import { Input } from "ant-design-vue";
import { getListWavFileApi } from "/@/api/sys/wav_process";
import { PageWrapper } from '/@/components/Page';
export default defineComponent({
  name: "Menu3Demo",
  components: { Input ,PageWrapper},
  mounted() {


  },

  updated() {

  },
  data() {
    return {
      selected_wav_file: undefined,
      wav_list_options: []
    };
  },
  methods: {
    focus() {
      this.wav_list_options = [];
      getListWavFileApi().then((res) => {
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
