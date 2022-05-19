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
        <a-button  type="primary"  class="record-start-btn btn">开始录音</a-button>
        <span style="display: inline-block; width: 10px; height: 10px"></span>
        <a-button danger class="record-finish-btn btn">结束录音</a-button>
        <span style="display: inline-block; width: 10px; height: 10px"></span>
        <a-button type="primary" :size="size">
          <template #icon>
            <DownloadOutlined />
          </template>
          保存录音
        </a-button>
        <audio controls style="display: inline-block"></audio>
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
  import { uploadApi } from '/@/api/sys/upload';

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
