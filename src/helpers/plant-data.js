





export const getLast500 = async () => {
  try {
    let response = await fetch('https://watamatic-database.herokuapp.com/last500')
    response = await response.json()
    const collections = response.data
    return collections
  } catch (e) {
      console.log(e)
  }
  return null
}




export const formatAsTempOverTime = (collections, interval=3) => {

    let timestamps = []
    let temperatures = []




    for (const idx in collections) {
      let temperature = collections[idx].temperature
      let timestamp = new Date(collections[idx].created)
      timestamp = timestamp.toISOString().replace(/([^T]+)T([^\.]+).*/g, '$1 $2')
      timestamps.push(timestamp)
      temperatures.push(temperature)
    }

    const chartData = {
        labels: timestamps,
        datasets: [
          { 
            data: temperatures,
            backgroundColor: 'white',
            label: 'TEMPERATURE'
          }
          
        ],
        
    }

    return chartData


}



