<script setup>
  import { ref, reactive } from "vue";

  const state = reactive({
    status: '',
    data: {},
    postData: {}
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
  <div class = "data-container">

    <div class="data-display">
      <p>Soil Moisture: {{parseFloat(state.data.soilMoisture*100).toFixed(2)}}%</p>
      <p>Is empty: {{ state.data.isEmpty}}</p>
      <p>Light Level: {{parseFloat(state.data.lightLevel*100).toFixed(2)}}%</p>
      <p>Pump Active: {{ state.data.pumpActive }}</p>
      <p>Temperature: {{state.data.temperature}} &#8457;</p>
      <p>Pump Duration: {{state.data.pumpDuration}} seconds</p>
      <p>Pump Interval: {{state.data.pumpInterval}} seconds</p>
    </div>

    <div id="input-container">
      <div class="input-item-container">
        <label>Pump Duration:</label>
        <input class="textInput" type="text" v-model="input.pumpDuration" placeholder="Duration">
      </div>
      <div class="input-item-container">
        <label>Pump Interval:</label>
        <input class="textInput" type="text" v-model="input.pumpInterval" placeholder="Interval">
      </div>
      <div class="input-item-container">
        <label>Mode:</label>
        <input class="textInput" type="text" v-model="input.mode" placeholder="Mode">
      </div>
      <button v-on:click=postData()>Submit</button>
    </div>
    <div>Received Data: {{state.postData}}</div>
  </div>

</template>

<style>
  @import "./assets/base.css";
</style>