




<template>
  <div style="width: 50vw; max-height: 100vh">
    <canvas id="temp-bar-chart"></canvas>
  </div>
</template>

<script>

import Chart from 'chart.js'
import { getLast500, formatAsTempOverTime } from '../helpers/plant-data.js'







export default {
  name: 'Temperature Bar Chart',

  data() {
    return {
    }
  },



  async mounted() {
    

    const collections = await getLast500()
    if (collections === null) return
    // console.log(collections)

    const data = formatAsTempOverTime(collections)

    console.log(data)

    const ctx = document.getElementById('temp-bar-chart');

    let c = new Chart(ctx, {  
      name: 'Temperature Bar Chart',
      type: 'bar',
      data: data,
      options: {
          scales: {
              y: {
                  beginAtZero: true
              }
          }
      }
    })

  }

}




</script>




