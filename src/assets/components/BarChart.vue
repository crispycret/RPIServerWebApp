<template>
  <Bar
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

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
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
        labels: [ 'January', 'February', 'March', 'April' ],
        datasets: [{ 
          label: "Humidity",
          data: [.3, .33, .53, .72],
          backgroundColor: 'rgba(255, 99, 132, 1)',
          
        },{ 
          label: "WaterContent",
          data: [.13, .42, .45,.51],
          backgroundColor: 'rgba(54, 162, 235, 1)'
        }]
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