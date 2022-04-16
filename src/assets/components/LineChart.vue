<script>
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, LinearScale, PointElement, CategoryScale} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, LineElement, LinearScale, PointElement, CategoryScale)
export default {
  name: 'LineChart',
  components: { Line },
  props: {
    chartId: {
      type: String,
      default: 'bar-chart'
    },
    datasetIdKey: {
      type: String,
      default: 'label'
    },
    width: {
      type: Number,
      default: 400
    },
    height: {
      type: Number,
      default: 400
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => {}
    },
    plugins: {
      type: Object,
      default: () => {}
    }
  },
  data() {
    return {
      chartData: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#E33344',
            borderColor: '#E33344',
            pointBackgroundColor: '#FFFFFF',
            data: [.40, .39, .10, .40, .39, .80, .40],
            tension: 0.3
          }
        ]
      },
      chartOptions: {
        scales: {
          y: {
            grace: "1%",
            title: {
              display: true,
              text:'Percentage',
              color: '#FFF'
            },
            beginAtZero: true,
            ticks: {
              color: '#FFF',
              min: 0,
              max: 1,
              stepSize: .1,
              format: {
                style: 'percent'
              }
            },
            grid: {
              color: 'rgba(255,255,255,.2)'
            }
          },
          x:{
            ticks: {
              color: '#FFF'
            },
            grid: {
              color: 'rgba(255,255,255,.2)'
            }
          }
        },
        plugins: {
          legend: {
            display: true,
            labels: {
              color: '#FFF'
            },
            onHover: (event, chartElements) => {
              event.native.target.style.cursor = 'pointer'
            },
            onLeave: (event, chartElements) => {
              event.native.target.style.cursor = 'default'
            }
          }
        },
        responsive: true
      }
    }
  }
}
</script>

<template>
  <Line
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
    :width="width"
    :height="height"
  />
</template>