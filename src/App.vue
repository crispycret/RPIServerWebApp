<script setup>
import { ref, reactive } from "vue";

var requestOptions = {
method: "GET",
redirect: 'follow',
};

const state = reactive({
  status: '',
  data: {},

})

fetchData()
function fetchData(){

  fetch("https://plantwaterer.ngrok.io/v1/data", requestOptions)
    .then((response) => { return response.json(); })
    .then(setResults)
    .catch((error) => console.log("Error", error));
}

function setResults(response){
  state.data = response.data
  console.log(state.data)
 
}

</script>



<template>
  <div>
    <div class = "soilMoisture"> Soil Moisture:{{ state.data.soilMoisture }}</div>
    <div class = "isEmpty"> Is empty:{{ state.data.isEmpty}}</div>
    <div class = "lightLevel"> Light Level{{ state.data.lightLevel }}</div>
    <div class = "pumpActive"> Pump Active:{{ state.data.pumpActive }}</div>
    <div class = "temperature"> Temperature:{{state.data.temperature}}</div>
    <div class = "pumpDuration">Pump Duration:{{state.data.pumpDuration}}</div>
    <div class = "pumpInterval">Pump Interval:{{state.data.pumpInterval}}</div>
  </div>
</template>




<style>
@import "./assets/base.css";
#app {
font-weight: normal;
padding: 2rem;

text-align: center;
background-color: #8e9dbd;
color: #0f4061;

}
.soilMoisture {
color: 'black'

}
.isEmpty {
color:'black'
}
.lightLevel {
color:'black'
}
.pumpActive {
color:'black'
}
.temperature {
color:'black'
}
.pumpDuration {
color:'black'
}
.pumpInterval {
color:'black'
}

</style>