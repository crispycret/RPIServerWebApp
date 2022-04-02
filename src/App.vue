<script setup>
  import { ref, reactive } from "vue";
  import Url from 'url'

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
  <div>
    <div class = "dataPoint"> Soil Moisture: {{parseFloat(state.data.soilMoisture*100).toFixed(2)}}%</div>
    <div class = "dataPoint"> Is empty: {{ state.data.isEmpty}}</div>
    <div class = "dataPoint"> Light Level: {{parseFloat(state.data.lightLevel*100).toFixed(2)}}%</div>
    <div class = "dataPoint"> Pump Active: {{ state.data.pumpActive }}</div>
    <div class = "dataPoint"> Temperature: {{state.data.temperature}} &#8457;</div>
    <div class = "dataPoint">Pump Duration: {{state.data.pumpDuration}} seconds</div>
    <div class = "dataPoint">Pump Interval: {{state.data.pumpInterval}} seconds</div>

    <div id="inputContainer">
      <div class="inputItemContainer">
        <label for="pumpDuration">Pump Duration: </label>
        <input class="textInput" id="pumpDuration" type="text" v-model="input.pumpDuration" placeholder="Duration">
      </div>
      <div class="inputItemContainer">
        <label for="pumpInterval">Pump Interval: </label>
        <input class="textInput" id="pumpInterval" type="text" v-model="input.pumpInterval" placeholder="Interval">
      </div>
      <div class="inputItemContainer">
        <label for="mode">Mode:</label>
        <input class="textInput" id='mode' type="text" v-model="input.mode" placeholder="Mode">
      </div>
      <button v-on:click=postData()>Submit</button>
    </div>
    <div>Received Data: {{state.postData}}</div>
  </div>
</template>

<style>
  @import "./assets/base.css";
  #app {
  font-weight: normal;
  padding: 2rem;
  display: flex;
  justify-content: center;

  text-align: center;
  background-color: #8e9dbd;
  color: #0f4061;
  }

  #inputContainer{
    display:flex;
    flex-direction: column;
  }

  .textInput{
    margin-left: 30px;
  }

  .inputItemContainer{
    padding: 0px 10px;
    display:flex;
    justify-content: space-between;
    padding: 10px 0px;
  }

  .dataPoint {
    color: 'black'
  }

</style>