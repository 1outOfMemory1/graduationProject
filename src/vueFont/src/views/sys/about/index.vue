<template>
  <div>
    <PageWrapper title="作者信息">
      <template #headerContent>
        <div style="margin-left: 40px" class="flex justify-between items-center">
        <span style="font-weight: bold;font-size: 20px" class="flex-1">
          <div style="font-size: 20px;font-weight: bold">开发者：尹浩男</div>
          <div style="font-size: 20px;font-weight: bold">毕业设计主题：深度学习语音识别</div>
          <div style="font-size: 20px;font-weight: bold">班级：计算机科学与技术18-5班</div>
        </span>

        </div>
        <div style="font-size: 40px;font-weight: bold"  title="开发信息">

        </div>
      </template>
    </PageWrapper>
    <PageWrapper title="关于">
      <template #headerContent>
        <div style="margin-left: 40px" class="flex justify-between items-center">
        <span style="font-weight: bold;font-size: 20px" class="flex-1">
          本项目是前端是基于vue-vben-admin 开源框架搭建，主要用于语音识别的相关功能的展示，主要功能有
          <div style="font-size: 20px;font-weight: bold">1.录制加载音频</div>
          <div style="font-size: 20px;font-weight: bold">2.绘制声波图和语谱图</div>
          <div style="font-size: 20px;font-weight: bold">3.语音转拼音，拼音转文字</div>
        </span>

        </div>
        <div style="font-size: 40px;font-weight: bold"  title="开发信息">

        </div>
      </template>
    </PageWrapper>
  </div>
</template>
<script lang="ts" >

  import { defineComponent } from "vue";
  import { PageWrapper } from '/@/components/Page';

  export default defineComponent({
    components: { PageWrapper}
  });

</script>
