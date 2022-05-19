<template>
  <div class="p-5">
    <a-select
      ref="select"
      :value="selected_wav_file"
      style="width: 120px"
      :options="wav_list_options"
      @focus="focus"
      @change="handleChange"
    >
    </a-select>
    <span style="display: inline-block;width: 10px;height: 10px"> </span>
    <span style="font-size: 15px"> 选择想要分析的已经保存的录音</span>
  </div>
</template>
<script lang="ts">
import { defineComponent, ref } from "vue";
  import { Input } from 'ant-design-vue';
  export default defineComponent({
    name: 'Menu4Demo',
    components: { Input },
    setup(){
      const  wav_list_options = [
        {
          value: 'aaa',
          label: 'aaa',
        }
      ]

      const focus = () => {
        console.log('focus');
      };

      const handleChange = (value: string) => {
        console.log(`selected ${value}`);
      };

      return{
        focus,
        handleChange,
        wav_list_options,
        selected_wav_file: ref<string | undefined>(undefined)
      }
    }
  });
</script>
