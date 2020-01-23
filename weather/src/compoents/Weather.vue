<template>
   <div class="container" :style="weatherCase.colors">
       <div class="upper">
           <i :class="weatherCase.icon" style="color:#ffffff; font-size: 100px; margin-top: 20px;"></i>
           <p class="location">{{ weather.name }}</p>
           <p class="temp">{{ weather.main.temp }}°</p>
       </div>
       <div class="lower">
           <p class="title">{{ weather.weather[0].main }}</p>
           <p class="subtitle">{{ weather.weather[0].description }}</p>
       </div>
   </div>
</template>

<script>
const weatherCases = {
 Rain: {
   colors : 'background-image: linear-gradient(#00C6FB, #005BEA)',
   icon: "fa fa-cloud-showers-heavy"
 },
 Clear: {
   colors : 'background-image: linear-gradient(#FEF253, #FF7300)',
   icon: "fa fa-sun"
 },
 Thunderstorm: {
   colors : 'background-image: linear-gradient(#00ECBC, #007ADF)',
   icon: "fa fa-poo-storm"
 },
 Clouds: {
   colors : 'background-image: linear-gradient(#D7D2CC, #304352)',
   icon: "fa fa-cloud"
 },
 Snow: {
   colors : 'background-image: linear-gradient(#7DE2FC, #B986E5)',
   icon: "fa fa-snowflake"
 },
 Drizzle: {
   colors : 'background-image: linear-gradient(#89F7FE, #66A6FF)',
   icon: "fa fa-cloud-showers-heavy"
 },
 Haze: {
   colors : 'background-image: linear-gradient(#89F7FE, #66A6FF)',
   icon: "fa fa-smog"
 },
 Mist: {
   colors : 'background-image: linear-gradient(#D7D2CC, #304352)',
   icon: "fa fa-smog"
 }
}

export default {
    props: ['weather'],
    computed: {
        weatherCase() {
           if (this.weather == null) {
               return weatherCases['Clear']
           }
           return weatherCases[this.weather.weather[0]['main']]
        }
    }
}
</script>

<style scoped>
   .container {
       flex: 1;
       width: 100%;
       height: 100%;
   }
   .upper {
       flex: 1;
       align-items: center;
       justify-content: center;
       background-color: transparent;
   }
   .temp {
       font-size: 48px;
       background-color: transparent;
       color: white;
       margin-top: 10px;
   }
   .location {
       font-size: 48px;
       background-color: transparent;
       color: white;
       margin-top: 15px;
   }
   .lower {
       flex: 1;
       align-items: center;
       justify-content: flex-end;
   }
   .title {
       font-size: 38px;
       background-color: transparent;
       color: white;
       margin-bottom: 10px;
       font-weight: 300px;
   }
   .subtitle {
       font-size: 24px;
       background-color: transparent;
       color: white;
       margin-bottom: 24px;
   }
</style>