<template>
  <div class="p-5">
    <PageWrapper title="生成波形图">
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
    </PageWrapper>
    <div id="my_echart" style="width: 100%;height: 800px"></div>
  </div>
</template>
<script lang="ts">
import { defineComponent, Ref, ref } from "vue";
import { Input } from "ant-design-vue";
import { getSoundWaveListApi, getWavFileListApi } from "/@/api/sys/wav_process";
import { PageWrapper } from "/@/components/Page";
import { useECharts } from "/@/hooks/web/useECharts";
import { getLineData } from "/@/views/demo/charts/data";

export default defineComponent({

  name: "Menu2Demo",
  components: { Input, PageWrapper },
  data() {
    return {
      myChart : undefined,
      selected_wav_file: undefined,
      wav_list_options: []
    };
  },
  mounted() {
    this.myChart =useECharts().echarts.init(
      document.getElementById("my_echart")
    );
  },
  methods: {
    drawMyEchart(data) {
      let data_length = data.length
      let x_axis_list = []
      for(let i=0;i<data_length;i++){
        x_axis_list.push([i,data[i]])
      }
      this.myChart.setOption( {
        animation: false,
        grid: {
          top: 40,
          left: 50,
          right: 40,
          bottom: 50
        },
        xAxis: {
          name: 'x',
          minorTick: {
            show: true
          },
          minorSplitLine: {
            show: true
          }
        },
        yAxis: {
          name: 'y',
          minorTick: {
            show: true
          },
          minorSplitLine: {
            show: true
          }
        },
        lineStyle: {
          color: "#1f77b4",
        },
        dataZoom: [
          {
            show: true,
            type: 'inside',
            filterMode: 'none',
            xAxisIndex: [0],
            startValue: 0,
            endValue: data_length
          },
          {
            show: true,
            type: 'inside',
            filterMode: 'none',
            yAxisIndex: [0],
            startValue: -30000,
            endValue: 30000
          }
        ],
        series: [
          {
            type: 'line',
            showSymbol: false,
            clip: true,
            data: x_axis_list
          }
        ]
      });
    },
    generateBtnClick() {
      let params = { "wavFileName": this.selected_wav_file };
      getSoundWaveListApi(params).then((res) => {
        this.drawMyEchart(res)
      }, error => {
        console.log(error);
      });
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
      this.selected_wav_file = value;
    }
  }

});

</script>
