<template>
  <div class="p-5">
    <PageWrapper   title="生成波形图" >
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
    <div ref="chartRef" :style="{ height, width }"></div>
  </div>
</template>
<script lang="ts">
import { defineComponent, onMounted, Ref, ref } from "vue";
  import { Input } from 'ant-design-vue';
  import { getListWavFileApi } from "/@/api/sys/wav_process";
  import { PageWrapper } from '/@/components/Page';
import { useECharts } from "/@/hooks/web/useECharts";
import { getLineData } from "/@/views/demo/charts/data";

  export default defineComponent({

    name: 'Menu2Demo',
    components: { Input,PageWrapper },
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
    },
    setup() {
      const chartRef = ref<HTMLDivElement | null>(null);
      const { setOptions, echarts } = useECharts(chartRef as Ref<HTMLDivElement>);
      const { barData, lineData, category } = getLineData;
      onMounted(() => {
        setOptions({
          backgroundColor: '#0f375f',
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'shadow',
              label: {
                show: true,
                backgroundColor: '#333',
              },
            },
          },
          legend: {
            data: ['line', 'bar'],
            textStyle: {
              color: '#ccc',
            },
          },
          xAxis: {
            data: category,
            axisLine: {
              lineStyle: {
                color: '#ccc',
              },
            },
          },
          yAxis: {
            splitLine: { show: false },
            axisLine: {
              lineStyle: {
                color: '#ccc',
              },
            },
          },
          series: [
            {
              name: 'line',
              type: 'line',
              smooth: true,
              showAllSymbol: 'auto',
              symbol: 'emptyCircle',
              symbolSize: 15,
              data: lineData,
            },
            {
              name: 'bar',
              type: 'bar',
              barWidth: 10,
              itemStyle: {
                borderRadius: 5,
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  { offset: 0, color: '#14c8d4' },
                  { offset: 1, color: '#43eec6' },
                ]),
              },
              data: barData,
            },
            {
              name: 'line',
              type: 'bar',
              barGap: '-100%',
              barWidth: 10,
              itemStyle: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  { offset: 0, color: 'rgba(20,200,212,0.5)' },
                  { offset: 0.2, color: 'rgba(20,200,212,0.2)' },
                  { offset: 1, color: 'rgba(20,200,212,0)' },
                ]),
              },
              z: -12,
              data: lineData,
            },
            {
              name: 'dotted',
              type: 'pictorialBar',
              symbol: 'rect',
              itemStyle: {
                color: '#0f375f',
              },
              symbolRepeat: true,
              symbolSize: [12, 4],
              symbolMargin: 1,
              z: -10,
              data: lineData,
            },
          ],
        });
      });
      return { chartRef };
    },
  });

</script>
