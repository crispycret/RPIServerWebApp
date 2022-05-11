





export const getLast500 = async () => {
  try {
    let response = await fetch('http://localhost:5000/last500')
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

    console.log(collections.length)



    for (const idx in collections) {
      let temperature = collections[idx].temperature
      let timestamp = new Date(collections[idx].created)
      timestamp = timestamp.toISOString().replace(/([^T]+)T([^\.]+).*/g, '$1 $2')
      timestamps.push(timestamp)
      temperatures.push(temperature)
    }

    const chartData = {
        labels: timestamps,
        datasets: [{ data: temperatures }]
    }

    return chartData


}



