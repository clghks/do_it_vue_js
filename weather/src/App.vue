<template>
  <div id="app">
    <Location v-on:updateWeather="updateWeather" ></Location>
    <Weather v-if="weather !== null" v-bind:weather="weather"></Weather>
  </div>
</template>

<script>
import Location from './compoents/Location.vue'
import Weather from './compoents/Weather.vue'

const APK_KEY = 'd79e59f5bd965ebf88e8204e0831177e'
const DEFAULT_LOCATION = 'seoul'

export default {
  name: 'app',
  data () {
    return {
      weather: null
    }
  },
  mounted() {
    this.updateWeather(DEFAULT_LOCATION);
  },
  methods: {
    updateWeather(location) {
      this.$http.get('http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APK_KEY + '&units=metric')
        .then((respons) => {
          this.weather = respons.data
        })
    }
  },
  components: {
    Location: Location,
    Weather: Weather
  }
}
</script>

<style>
 html, body, #app {
   width: 100%;
   height: 100%;
   text-align: center;
   margin: 0px;
 }
</style>
