<script setup>
  import { ref, reactive,} from "vue";
  import BarChart from './assets/components/BarChart.vue'
    // Import the functions you need from the SDKs you need
  import { initializeApp } from "firebase/app";
  import { getFirestore, collection, getDocs, query, where } from 'firebase/firestore/lite';
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyD_ZkIAmm-__MPMujSyZUXQBWa8LsH2QOI",
    authDomain: "test12-452ae.firebaseapp.com",
    projectId: "test12-452ae",
    storageBucket: "test12-452ae.appspot.com",
    messagingSenderId: "495868709078",
    appId: "1:495868709078:web:8bce2b8efda444776be177",
    measurementId: "G-TT894B2845"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const db = getFirestore(app);

  const state = reactive({
    status: '',
    data: {},
    postData: '',
    modeSetting: '',
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

  // yyyy/mm/dd
  let start = new Date('2022-04-15T18:00:00')
  let end = new Date('2022-04-16')

  getData()
  async function getData() {
    const colRef = collection(db, 'RaspberryData')

    // query by light level
    // const q = query(colRef, where("lightLevel",">", .8));
    // const querySnapshot = await getDocs(q)
    // querySnapshot.forEach((doc)=>{
    //   console.log(doc.id, " => ", doc.data());
    // })

    //query by date
    const q = query(colRef, 
    where("DateTime",">", start), 
    where("DateTime","<", end));

    const querySnapshot = await getDocs(q)
    querySnapshot.forEach((doc)=>{
      console.log(doc.id, " => ", doc.data());
    })

    console.log(querySnapshot)
    return querySnapshot;
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
        //then refresh data
        fetchData()
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
      if(state.data.mode == '1'){
        state.modeSetting = '- (AUTO)'
      } else if (state.data.mode == '2'){
        state.modeSetting = '- (TIMER)'
      } else{
        state.modeSetting = '- (OFF)'
      }
      console.log(state.data)
    }
  }
</script>

<script>
  export default {
    name: 'App',
    components: { BarChart }
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
          <div class="grid-item-title">Chart</div>
          <BarChart />
        </div>
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
          <div class="grid-item-data">{{state.data.mode}} {{state.modeSetting}}</div>
        </div>
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
          <input type="submit" class="input-button" v-on:click=fetchData() value="Refresh">
        </div>
      </div>
    </div>
</template>

<style>
  @import "./assets/base.css";
</style>