<script setup>
  import { ref, reactive } from "vue";

  const state = reactive({
    status: '',
    data: {},
    postData: ''
  })

  const input = reactive({
    pumpDuration: '',
    pumpInterval: '',
    mode: ''
  })

  var getRequestOptions = {
    method: "GET",
    redirect: 'follow',
  };

  var postRequestOptions = {
    method: "POST",
    body: JSON.stringify(input)
  }

  fetchData()
  function fetchData(){
    fetch("https://plantwaterer.ngrok.io/v1/data", getRequestOptions)
      .then((response) => { return response.json(); })
      .then(setResults)
      .catch((error) => console.log("Error", error));
  }

  function postData(){
    var url = new URL("https://plantwaterer.ngrok.io/v1/set"), params = input
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))

    fetch(url, postRequestOptions)
      .then((response) => { return response.json(); })
      .then((json)=>{
        state.postData = json
      })
      .catch((error) => console.log("Error", error));
  }

  function setErrorResponse(){
    let na = 'N/A'
    state.data.soilMoisture = na
    state.data.isEmpty = na
    state.data.lightLevel = na
    state.data.pumpActive = na
    state.data.temperature = na
    state.data.pumpDuration = na
    state.data.pumpInterval = na
  }

  function setResults(response){
    if(response.status != 'ok'){
      setErrorResponse()
    } else {
      state.data = response.data
      console.log(state.data)
    }
  }
</script>

<template>
  <div class="navbar">
    <h1 class="nav-title">PlantWaterer</h1>
    <div class="nav-item" id="nav-item-selected">Dashboard</div>
    <div class="nav-item">Option 2</div>
    <div class="nav-item">Option 3</div>
    <div class="nav-item">Option 4</div>
  </div>
  <div class="grid-container">
    <div class="grid">
      <div class="grid-item">
        <div class="grid-item-title">Soil Moisture</div>
        <div class="grid-item-data">{{parseFloat(state.data.soilMoisture*100).toFixed(2)}}%</div>
      </div>
      <div class="grid-item">
        <div class="grid-item-title">Is empty</div>
        <div class="grid-item-data">{{state.data.isEmpty}}</div>
      </div>
      <div class="grid-item">
        <div class="grid-item-title">Light Level</div>
        <div class="grid-item-data">{{parseFloat(state.data.lightLevel*100).toFixed(2)}}%</div>
      </div>
      <div class="grid-item">
        <div class="grid-item-title">Pump Active</div>
        <div class="grid-item-data">{{ state.data.pumpActive }}</div>
      </div>
      <div class="grid-item">
        <div class="grid-item-title">Temperature</div>
        <div class="grid-item-data">{{state.data.temperature}} &#8457;</div>
      </div>
      <div class="grid-item">
        <div class="grid-item-title">Pump Duration</div>
        <div class="grid-item-data">{{state.data.pumpDuration}} seconds</div>
      </div>
      <div class="grid-item">
        <div class="grid-item-title">Pump Interval</div>
        <div class="grid-item-data">{{state.data.pumpInterval}} seconds</div>
      </div>
      <div class="grid-item">
        <div class="grid-item-title">Mode</div>
        <div class="grid-item-data">{{state.data.mode}}</div>
      </div>
      <div></div>
      <div class="grid-item">
        <form action='' class="input-container" v-on:submit.prevent="onSubmit" @submit=postData()>
          <div>
            <p>Pump Duration</p>
            <input class="text-input" type="text" v-model="input.pumpDuration" placeholder="Duration" required>
          </div>
          <div>
            <p>Pump Interval</p>
            <input class="text-input" type="text" v-model="input.pumpInterval" placeholder="Interval" required>
          </div>
          <div>
            <p>RPI Mode</p>
            <input class="text-input" type="text" v-model="input.mode" placeholder="Mode" required>
          </div>
          <input type="submit" class="input-button">
        </form>
      </div>
      <div class="grid-item">
        <div class="grid-item-title">Received Data</div>
        <div class="grid-item-data">{{state.postData}}</div>
      </div>
      <div class="grid-item">
        <div class="grid-item-title">Refresh Data</div>
        <input type="submit" class="input-button" v-on:click=fetchData()>
      </div>
    </div>
  </div>
  
</template>

<style>
  @import "./assets/base.css";
</style>